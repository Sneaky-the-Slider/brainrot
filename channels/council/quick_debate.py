#!/usr/bin/env python3
"""
Quick Debate - Fast 3-Round Structured Council
Stance → Rebuttal → Verdict

No menu, no modes. Just fast decisions.
Usage: python quick_debate.py "Your question here"
"""

import os
import sys
import csv
import argparse
from datetime import datetime

try:
    import google.generativeai as genai
    from rich.console import Console
    from rich.panel import Panel
    from rich.rule import Rule
except ImportError:
    print("❌ Missing dependencies. Install with:")
    print("   pip install google-generativeai rich")
    sys.exit(1)

console = Console()

PERSONAS = {
    "VADER": {
        "color": "red",
        "prompt": "You are Darth Vader. Cold, authoritative. Focus on control and consequences. Keep responses under 3 sentences."
    },
    "YODA": {
        "color": "green",
        "prompt": "You are Master Yoda. Use OSV syntax frequently. Focus on wisdom, patience, and the Force. Keep responses under 3 sentences."
    },
    "STARK": {
        "color": "cyan",
        "prompt": "You are Tony Stark. Snarky, tech-obsessed, fast-talking. Focus on innovation and efficiency. Keep responses under 3 sentences."
    }
}

CSV_FILE = "quick_debate_logs.csv"


def log_to_csv(user_query, round_name, persona, content, session_id):
    """Log debate entry to CSV"""
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            "session_id", "timestamp", "query", "round", "persona", "content"
        ])

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "session_id": session_id,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "query": user_query[:100],  # Truncate long queries
            "round": round_name,
            "persona": persona,
            "content": content.strip()
        })


def get_response(model, persona_key, context):
    """Get response from a persona"""
    role = PERSONAS[persona_key]["prompt"]
    full_prompt = f"{role}\n\nCONVERSATION HISTORY:\n{context}\n\nYour response:"

    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"[ERROR: {str(e)}]"


def run_quick_debate(api_key, user_query):
    """Execute fast 3-round debate"""
    # Initialize
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Banner
    console.print("\n[bold cyan]⚡ QUICK DEBATE - 3 ROUNDS[/bold cyan]")
    console.print(f"[dim]Question: {user_query}[/dim]\n")

    debate_history = f"User Request: {user_query}\n"

    # --- ROUND 1: Opening Stances ---
    console.print(Rule("[bold yellow]ROUND 1: OPENING STANCES[/bold yellow]"))

    for name in PERSONAS:
        color = PERSONAS[name]["color"]
        with console.status(f"[bold {color}]Waiting for {name}...", spinner="dots"):
            response = get_response(model, name, debate_history)
            debate_history += f"{name}: {response}\n"
            log_to_csv(user_query, "Opening", name, response, session_id)

        console.print(f"[bold {color}]{name}:[/bold {color}] {response}\n")

    # --- ROUND 2: Rebuttals ---
    console.print(Rule("[bold red]ROUND 2: REBUTTALS[/bold red]"))

    for name in PERSONAS:
        color = PERSONAS[name]["color"]
        critique_context = debate_history + "\nINSTRUCTION: Critique the suggestions made by the others. Why is your approach better?"

        with console.status(f"[bold {color}]Waiting for {name}...", spinner="dots"):
            response = get_response(model, name, critique_context)
            debate_history += f"{name} (Rebuttal): {response}\n"
            log_to_csv(user_query, "Rebuttal", name, response, session_id)

        console.print(f"[bold {color}]{name}:[/bold {color}] {response}\n")

    # --- ROUND 3: Final Consensus ---
    console.print(Rule("[bold green]FINAL CONSENSUS[/bold green]"))

    consensus_context = debate_history + "\nINSTRUCTION: Provide one final, unified piece of advice incorporating all perspectives. Be decisive."

    with console.status("[bold cyan]Synthesizing final verdict...", spinner="dots"):
        verdict = get_response(model, "STARK", consensus_context)
        log_to_csv(user_query, "Verdict", "COUNCIL_CONSENSUS", verdict, session_id)

    console.print(Panel(
        verdict,
        title="[bold white]⚖️  THE VERDICT[/bold white]",
        border_style="gold1"
    ))

    console.print(f"\n[dim]💾 Debate logged to {CSV_FILE} (session: {session_id})[/dim]\n")


def main():
    parser = argparse.ArgumentParser(
        description="Quick Debate - Fast 3-round structured council",
        epilog="Example: python quick_debate.py 'Should I quit my job?'"
    )
    parser.add_argument('question', nargs='?', help='Your question (or will prompt interactively)')
    parser.add_argument('--api-key', help='Google AI API key (or set GOOGLE_API_KEY env var)')
    args = parser.parse_args()

    # Get API key
    api_key = args.api_key or os.getenv('GOOGLE_API_KEY')
    if not api_key:
        console.print("[bold red]❌ No API key provided.[/bold red]")
        console.print("Set GOOGLE_API_KEY env var or use --api-key flag")
        sys.exit(1)

    # Get question
    if args.question:
        question = args.question
    else:
        console.print("[bold cyan]⚡ Quick Debate - Fast Decision Tool[/bold cyan]\n")
        question = input("Question: ").strip()
        if not question:
            console.print("[bold red]No question provided.[/bold red]")
            sys.exit(1)

    # Run debate
    run_quick_debate(api_key, question)


if __name__ == "__main__":
    main()
