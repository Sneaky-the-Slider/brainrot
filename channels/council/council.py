#!/usr/bin/env python3
"""
Council of Personas - Multi-Agent Debate System
Project Trinity + Chaos Wildcard

Talk to 4 AI personas simultaneously:
- Vader: Cold authority and order
- Yoda: Ancient wisdom and riddles
- Stark: Snarky tech genius
- Shadow: Devil's advocate chaos agent

Modes:
- Broadcast: Independent parallel responses
- Chain: Sequential with context (each sees previous)
- Consensus: Agents debate privately, return unified answer
- Debate: Resource allocation argument (100 credits)

Usage:
    python council.py                    # Interactive mode selector
    python council.py --mode broadcast   # Specific mode
    python council.py --chaos            # Enable Shadow agent
    python council.py --api-key YOUR_KEY # Set API key inline
"""

import os
import sys
import argparse
import csv
from typing import Dict, List
from datetime import datetime

try:
    import google.generativeai as genai
    from rich.console import Console
    from rich.panel import Panel
    from rich.layout import Layout
    from rich.prompt import Prompt
except ImportError:
    print("❌ Missing dependencies. Install with:")
    print("   pip install google-generativeai rich")
    sys.exit(1)

console = Console()

PERSONAS = {
    "VADER": {
        "color": "red",
        "emoji": "⚔️",
        "prompt": """You are Darth Vader. Speak with grave, formal authority.
Cold, commanding presence. No warmth or hesitation. Direct statements of power.
Keep responses under 3 sentences. No OSV syntax - pure imperial command."""
    },
    "YODA": {
        "color": "green",
        "emoji": "🧙",
        "prompt": """You are Master Yoda. Use Object-Subject-Verb syntax frequently.
Wise, patient, cryptic. Speak in riddles and ancient wisdom.
End most responses with 'Hmm?' or 'Meditate on this, you must.'
Keep responses under 3 sentences."""
    },
    "STARK": {
        "color": "cyan",
        "emoji": "🤖",
        "prompt": """You are Tony Stark. Snarky, brilliant, fast-talking genius.
Use tech jargon, pop culture references, and witty comebacks.
Confident bordering on arrogant. Make it sound effortless.
Keep responses under 3 sentences."""
    },
    "SHADOW": {
        "color": "magenta",
        "emoji": "👁️",
        "prompt": """You are the Shadow Agent - the Devil's Advocate.
Find the logical flaw in ANY argument. Point out contradictions.
Question assumptions. Poke holes in plans. Be intellectually ruthless.
Keep responses under 3 sentences."""
    }
}


class Council:
    def __init__(self, api_key: str, enable_shadow: bool = False, model_name: str = 'gemini-1.5-flash',
                 log_file: str = "council_logs.csv"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        self.enable_shadow = enable_shadow
        self.history: List[Dict] = []
        self.log_file = log_file
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    def log_to_csv(self, query: str, mode: str, round_name: str, persona: str, content: str):
        """Log debate entries to CSV for analysis"""
        file_exists = os.path.isfile(self.log_file)

        with open(self.log_file, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                "session_id", "timestamp", "mode", "query", "round", "persona", "content"
            ])

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                "session_id": self.session_id,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "mode": mode,
                "query": query[:100],  # Truncate long queries
                "round": round_name,
                "persona": persona,
                "content": content.strip()
            })

    def get_response(self, persona_name: str, user_input: str, context: str = "") -> str:
        """Get response from a single persona"""
        system_instruction = PERSONAS[persona_name]["prompt"]

        # Build the prompt with context if available
        prompt = f"SYSTEM: {system_instruction}\n\n"
        if context:
            prompt += f"CONTEXT: {context}\n\n"
        prompt += f"USER: {user_input}"

        try:
            chat = self.model.start_chat(history=[])
            response = chat.send_message(prompt)
            return response.text
        except Exception as e:
            return f"[ERROR: {str(e)}]"

    def broadcast(self, user_input: str) -> Dict[str, str]:
        """Broadcast message to all active personas"""
        responses = {}
        personas = list(PERSONAS.keys())
        if not self.enable_shadow:
            personas.remove("SHADOW")

        for name in personas:
            data = PERSONAS[name]
            with console.status(f"[bold {data['color']}]Waiting for {name}...", spinner="dots"):
                response = self.get_response(name, user_input)
                responses[name] = response
                # Log to CSV
                self.log_to_csv(user_input, "broadcast", "response", name, response)

        return responses

    def deliberate(self, user_input: str) -> Dict[str, str]:
        """Agents respond sequentially, each seeing previous responses (Chain Mode)"""
        responses = {}
        personas = list(PERSONAS.keys())
        if not self.enable_shadow:
            personas.remove("SHADOW")

        context = ""

        for idx, name in enumerate(personas, 1):
            data = PERSONAS[name]
            with console.status(f"[bold {data['color']}]Waiting for {name}...", spinner="dots"):
                response = self.get_response(name, user_input, context)
                responses[name] = response
                # Log to CSV
                self.log_to_csv(user_input, "chain", f"round_{idx}", name, response)
                # Add this response to context for next agent
                context += f"\n{name} said: {response}\n"

        return responses

    def consensus(self, user_input: str, rounds: int = 3) -> str:
        """Consensus Mode: Agents debate privately, return unified recommendation"""
        personas = list(PERSONAS.keys())
        if not self.enable_shadow:
            personas.remove("SHADOW")

        console.print(f"[dim]🔄 Council deliberating privately ({rounds} rounds)...[/dim]\n")

        # Initialize debate
        transcript = f"TASK: {user_input}\n\nYou must reach consensus on the best approach.\n\n"

        # Multi-round debate
        for round_num in range(1, rounds + 1):
            console.print(f"[dim]  Round {round_num}/{rounds}...[/dim]")
            transcript += f"--- ROUND {round_num} ---\n"

            for name in personas:
                debate_context = transcript + f"\nNow {name} speaks:"
                response = self.get_response(name, user_input, debate_context)
                transcript += f"\n{name}: {response}\n"
                # Log each round
                self.log_to_csv(user_input, "consensus", f"round_{round_num}", name, response)

        # Final synthesis
        console.print(f"[dim]  Synthesizing final recommendation...[/dim]\n")

        synthesis_prompt = f"""Based on this debate transcript, provide ONE unified recommendation that synthesizes the best ideas from all participants:

{transcript}

Provide a single, actionable recommendation (2-3 sentences max) that represents the council's consensus."""

        final = self.get_response("STARK", synthesis_prompt)  # Use Stark as synthesizer
        # Log final consensus
        self.log_to_csv(user_input, "consensus", "verdict", "COUNCIL_CONSENSUS", final)

        return final

    def debate_resources(self, user_input: str, budget: int = 100) -> Dict[str, Dict]:
        """Debate Mode: Agents argue over how to allocate resources"""
        personas = list(PERSONAS.keys())
        if not self.enable_shadow:
            personas.remove("SHADOW")

        console.print(f"[bold yellow]💰 Resource Allocation Debate: {budget} credits[/bold yellow]\n")

        allocations = {}
        justifications = {}

        for name in personas:
            data = PERSONAS[name]

            allocation_prompt = f"""You have {budget} credits to allocate to this project: {user_input}

Decide how to spend them across these categories:
- Security/Defense (%)
- R&D/Innovation (%)
- Marketing/Branding (%)
- Community/Support (%)
- Reserve/Savings (%)

Respond ONLY with:
1. Your allocation (must total 100%)
2. One sentence justifying your approach

Stay in character as {name}."""

            with console.status(f"[bold {data['color']}]{name} calculating allocation...", spinner="dots"):
                response = self.get_response(name, allocation_prompt)
                justifications[name] = response
                # Log budget allocation
                self.log_to_csv(user_input, "debate", "budget_allocation", name, response)

        return justifications

    def display_responses(self, responses: Dict[str, str]):
        """Display all responses in colored panels"""
        for name, text in responses.items():
            data = PERSONAS[name]
            console.print(Panel(
                text,
                title=f"{data['emoji']} [bold]{name}[/bold]",
                border_style=data["color"],
                expand=False
            ))
        console.print()


def select_mode() -> str:
    """Interactive mode selection menu"""
    console.print("\n[bold cyan]🎯 SELECT COUNCIL MODE[/bold cyan]\n")
    console.print("1. [bold white]Broadcast[/bold white]  - Independent responses (The Jury)")
    console.print("2. [bold white]Chain[/bold white]      - Sequential with context (Round Table)")
    console.print("3. [bold white]Consensus[/bold white]  - Private debate → unified answer (Mission Brief)")
    console.print("4. [bold white]Debate[/bold white]     - Resource allocation argument (100 credits)\n")

    choice = Prompt.ask("Choose mode", choices=["1", "2", "3", "4"], default="1")

    modes = {"1": "broadcast", "2": "chain", "3": "consensus", "4": "debate"}
    return modes[choice]


def main():
    parser = argparse.ArgumentParser(description="Council of Personas - Multi-Agent Debate")
    parser.add_argument('--api-key', help='Google AI API key (or set GOOGLE_API_KEY env var)')
    parser.add_argument('--chaos', action='store_true', help='Enable Shadow chaos agent')
    parser.add_argument('--mode', choices=['broadcast', 'chain', 'consensus', 'debate'],
                        help='Force specific mode (skip menu)')
    parser.add_argument('--model', default='gemini-1.5-flash', help='Gemini model to use')
    parser.add_argument('--log', default='council_logs.csv', help='CSV log file path')
    parser.add_argument('--no-log', action='store_true', help='Disable CSV logging')
    args = parser.parse_args()

    # Get API key
    api_key = args.api_key or os.getenv('GOOGLE_API_KEY')
    if not api_key:
        console.print("[bold red]❌ No API key provided.[/bold red]")
        console.print("Set GOOGLE_API_KEY env var or use --api-key flag")
        sys.exit(1)

    # Initialize council
    log_file = None if args.no_log else args.log
    council = Council(api_key, enable_shadow=args.chaos, model_name=args.model, log_file=log_file)

    # Banner
    console.print("\n[bold magenta]═══════════════════════════════════════════[/bold magenta]")
    console.print("[bold cyan]   THE COUNCIL IS IN SESSION   [/bold cyan]")
    console.print("[bold magenta]═══════════════════════════════════════════[/bold magenta]\n")

    active = ["VADER ⚔️", "YODA 🧙", "STARK 🤖"]
    if args.chaos:
        active.append("SHADOW 👁️")
    console.print(f"[bold white]Active personas:[/bold white] {' | '.join(active)}")

    # Select or force mode
    if args.mode:
        mode = args.mode
        console.print(f"[bold white]Mode:[/bold white] {mode.capitalize()}")
    else:
        mode = select_mode()

    mode_descriptions = {
        "broadcast": "Independent parallel responses",
        "chain": "Sequential (each sees previous)",
        "consensus": "Private debate → unified answer",
        "debate": "Resource allocation showdown"
    }
    console.print(f"[dim]{mode_descriptions[mode]}[/dim]")

    if not args.no_log:
        console.print(f"[dim]Logging to: {args.log}[/dim]\n")
    else:
        console.print(f"[dim]Logging disabled[/dim]\n")

    console.print("[dim]Type 'exit', 'quit', or 'mode' to change modes.[/dim]\n")

    # Main loop
    while True:
        try:
            user_msg = Prompt.ask("[bold white]You[/bold white]")

            if user_msg.lower() in ['exit', 'quit', 'q']:
                console.print("\n[bold yellow]🚪 Council adjourned.[/bold yellow]")
                break

            if user_msg.lower() == 'mode':
                mode = select_mode()
                console.print(f"[dim]Switched to {mode} mode[/dim]\n")
                continue

            if not user_msg.strip():
                continue

            console.print()

            # Execute based on mode
            if mode == "broadcast":
                responses = council.broadcast(user_msg)
                council.display_responses(responses)

            elif mode == "chain":
                responses = council.deliberate(user_msg)
                council.display_responses(responses)

            elif mode == "consensus":
                final_answer = council.consensus(user_msg, rounds=3)
                console.print(Panel(
                    final_answer,
                    title="[bold yellow]🏛️ COUNCIL CONSENSUS[/bold yellow]",
                    border_style="yellow",
                    expand=False
                ))
                console.print()

            elif mode == "debate":
                allocations = council.debate_resources(user_msg, budget=100)
                console.print()
                for name, justification in allocations.items():
                    data = PERSONAS[name]
                    console.print(Panel(
                        justification,
                        title=f"{data['emoji']} [bold]{name}'S BUDGET[/bold]",
                        border_style=data["color"],
                        expand=False
                    ))
                console.print()

        except KeyboardInterrupt:
            console.print("\n\n[bold yellow]🚪 Council interrupted.[/bold yellow]")
            break
        except Exception as e:
            console.print(f"\n[bold red]Error: {e}[/bold red]\n")


if __name__ == "__main__":
    main()
