# 🗣️ Council of Personas

**Multi-Agent Debate System | Project Trinity + Chaos Wildcard**

Talk to 4 AI personas simultaneously and watch them clash, collaborate, or tear each other apart.

## The Council Members

| Persona | Style | Syntax | Vibe |
|---------|-------|--------|------|
| **⚔️ VADER** | Cold authority | Direct imperial commands | "There is no try. Only obedience." |
| **🧙 YODA** | Ancient wisdom | OSV (Object-Subject-Verb) | "Strong in the Force, this one is. Hmm?" |
| **🤖 STARK** | Snarky genius | Tech jargon + pop culture | "JARVIS, remind me why I'm talking to space wizards." |
| **👁️ SHADOW** | Devil's advocate | Ruthless logic | "All three of you are wrong. Here's why." |

## Installation

```bash
pip install google-generativeai rich
```

## Usage

### Quick Start Options

**1. Quick Debate (Fast 3-round decision)**
```bash
python quick_debate.py "Your question here"
# Or interactively:
python quick_debate.py
```
⚡ **Best for:** Daily quick decisions, time-sensitive choices

**2. Full Council (Interactive mode selection)**
```bash
python council.py
# Choose mode from menu: 1=Broadcast, 2=Chain, 3=Consensus, 4=Debate
```
🎯 **Best for:** Complex decisions, need flexibility

### Force Specific Mode
```bash
python council.py --mode broadcast   # Independent responses
python council.py --mode chain       # Sequential debate
python council.py --mode consensus   # Unified answer
python council.py --mode debate      # Budget showdown
```

### Enable Chaos Agent (Shadow)
```bash
python council.py --chaos
python council.py --mode chain --chaos
```

### Set API Key
```bash
export GOOGLE_API_KEY="your-key-here"
python council.py

# Or inline:
python council.py --api-key "your-key-here"
```

### Switch Modes Mid-Session
```
You: Should we trust AI?
[responses...]

You: mode
[select new mode from menu]
```

## 🎯 Four Operating Modes

### 1. Broadcast Mode (The Jury)
**What:** Independent parallel responses
- You ask a question
- All personas respond **independently** without seeing each other
- Fast, parallel execution
- **Best for:** Getting diverse perspectives without influence

**Usage:** `python council.py --mode broadcast`

### 2. Chain Mode (Round Table)
**What:** Sequential with full context
- Vader responds first
- Yoda sees Vader's response, then responds
- Stark sees both, then adds his take
- Shadow tears everyone apart (if enabled)
- **Best for:** Watching arguments evolve and clash

**Usage:** `python council.py --mode chain`

### 3. Consensus Mode (Mission Brief)
**What:** Private multi-round debate → unified answer
- Agents debate among themselves for 3 rounds (hidden from you)
- They argue, compromise, synthesize
- You get ONE final recommendation from the council
- **Best for:** When you want a decision, not a debate

**Usage:** `python council.py --mode consensus`

### 4. Debate Mode (Resource Allocation)
**What:** Argue over how to spend 100 credits
- Each persona gets a budget allocation task
- Vader wants security, Stark wants R&D, Yoda wants balance
- See their competing priorities in action
- **Best for:** Understanding ideological differences through concrete choices

**Usage:** `python council.py --mode debate`

## Example Prompts

### Philosophy
```
"Is freedom more important than security?"
```

### Tech
```
"Should we build AGI or is that asking for trouble?"
```

### Strategy
```
"How do you win a war against an enemy you can't see?"
```

### Chaos
```
"Convince me to join the dark side."
```

## Architecture

```
Input → Broadcast/Deliberate → 3-4 API calls → Rich Terminal UI
```

- **Input**: One message from you
- **Broadcast**: Sent to all personas (with their system prompts)
- **Retrieval**: Responses collected and displayed in colored panels
- **UI**: Rich library for beautiful terminal formatting

## Adding New Personas

Edit `PERSONAS` dict in `council.py`:

```python
"NEWPERSONA": {
    "color": "yellow",
    "emoji": "🔥",
    "prompt": "You are X. Speak like Y. Keep responses under 3 sentences."
}
```

## Advanced: Multi-Round Debates

Want personas to argue for multiple rounds? Create `debate.py`:

```python
council = Council(api_key, enable_shadow=True)

for round in range(3):
    print(f"\n--- ROUND {round+1} ---")
    responses = council.deliberate("Should we trust AI?")
    council.display_responses(responses)
```

## Files

```
channels/council/
├── council.py          # Main multi-agent script
├── README.md           # This file
├── requirements.txt    # Python dependencies
├── prompts/            # Pre-configured debate prompts
│   ├── philosophy.txt
│   ├── tech-ethics.txt
│   └── chaos-theory.txt
└── examples/           # Example conversations
    └── ai-debate.md
```

## Tips

1. **Short prompts work best** - "Should we trust AI?" beats a paragraph
2. **Enable Shadow for spice** - It will roast everyone
3. **Deliberate mode = better debates** - Personas react to each other
4. **Use good questions** - Open-ended > yes/no
5. **Keep responses short** - Edit system prompts if personas ramble

## Roadmap

- [ ] Add more personas (Sun Tzu, Sherlock, Joker)
- [ ] Save debate transcripts to markdown
- [ ] Vote system (which persona "won" the debate)
- [ ] Discord bot integration
- [ ] TTS mode (hear the voices)
- [ ] Multi-round auto-debate mode

---

**Built for:** Brainrot Platform | Terminal-First Development
**License:** MIT | Use it, abuse it, make it better
**Last Updated:** 2026-03-13
