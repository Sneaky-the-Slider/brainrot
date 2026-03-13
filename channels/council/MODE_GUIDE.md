# 🎯 Council Mode Selection Guide

**TL;DR:** Which mode should you use?

---

## ⚡ Ultra-Fast Path: Quick Debate

**Use `quick_debate.py` when:**
- You need a decision in under 60 seconds
- Daily micro-decisions (meetings, emails, small purchases)
- Time-sensitive choices
- You want the structure of debate without menu navigation

```bash
python quick_debate.py "Should I take this meeting?"
# 3 rounds: Stance → Rebuttal → Verdict
# Done in ~30 seconds
```

---

## Quick Decision Tree (Full Council)

```
Do you need a DECISION or a DISCUSSION?
│
├─ DECISION → Use Consensus Mode
│   └─ You get: One unified recommendation
│
└─ DISCUSSION → Continue below
    │
    Do you want to see them CLASH?
    │
    ├─ YES → Use Chain Mode
    │   └─ You get: Sequential debate with escalating arguments
    │
    └─ NO → Continue below
        │
        Do you care about SPECIFIC TRADEOFFS?
        │
        ├─ YES → Use Debate Mode
        │   └─ You get: Budget allocation revealing priorities
        │
        └─ NO → Use Broadcast Mode
            └─ You get: Pure diverse perspectives
```

---

## Mode Comparison Table

| Mode | Script | Speed | Clash Level | Output Type | Best For |
|------|--------|-------|-------------|-------------|----------|
| **Quick Debate** | `quick_debate.py` | ⚡⚡⚡⚡ | Medium | 1 verdict (visible debate) | Daily fast decisions |
| **Broadcast** | `council.py` | ⚡⚡⚡ | Low | 3-4 independent answers | Quick diverse takes |
| **Chain** | `council.py` | ⚡⚡ | High | 3-4 sequential responses | Watching debates unfold |
| **Consensus** | `council.py` | ⚡ | Hidden | 1 unified answer | Complex decisions |
| **Debate** | `council.py` | ⚡⚡ | Medium | 3-4 budget proposals | Understanding tradeoffs |

---

## When to Use Each Mode

### 🎯 Broadcast Mode (The Jury)

**Use when:**
- You want multiple independent perspectives fast
- You're brainstorming and want variety
- You don't care if they contradict each other
- Time is limited

**Don't use when:**
- You want them to argue
- You need one clear answer
- Context matters (each needs to hear others)

**Example questions:**
- "What's the biggest risk in AI?"
- "Give me your take on remote work"
- "React to this idea: [your pitch]"

---

### 🔗 Chain Mode (Round Table)

**Use when:**
- You want to watch arguments evolve
- Each response builds on previous ones
- You enjoy intellectual combat
- You want to see who "wins"

**Don't use when:**
- You're in a hurry
- You want unbiased opinions (later personas are influenced)
- You need a unified decision

**Example questions:**
- "Should we trust AI?"
- "What's more important: freedom or security?"
- "How do we solve climate change?"

**Pro tip:** Add `--chaos` to watch Shadow destroy everyone's logic.

---

### 🏛️ Consensus Mode (Mission Brief)

**Use when:**
- You need ONE actionable recommendation
- You don't want to read a debate
- Decision fatigue is real
- You trust the council to argue on your behalf

**Don't use when:**
- You want to see the debate process
- Multiple perspectives are valuable
- You enjoy reading arguments

**Example questions:**
- "Should I quit my job to build a startup?"
- "B2B or B2C first?"
- "Which tech stack for our MVP?"

**Pro tip:** This is "manager mode" - you get the executive summary, skip the meeting.

---

### 💰 Debate Mode (Resource Allocation)

**Use when:**
- You want to see ideological priorities through money
- Tradeoffs matter more than abstract philosophy
- You're actually planning a budget
- You want to expose hidden biases

**Don't use when:**
- The question isn't about resources/tradeoffs
- You don't care about priorities
- You want philosophical answers

**Example questions:**
- "How should we spend our first $100k?"
- "Allocate engineering hours: features vs. tech debt"
- "Marketing budget: paid ads vs. content vs. community?"

**Pro tip:** The budget reveals what they REALLY value, not what they say they value.

---

## Mode Switching Strategy

You can type `mode` mid-session to switch. Here's when to do it:

1. **Start with Broadcast** to get quick takes
2. **Switch to Chain** if you want to see them argue about a specific point
3. **Switch to Consensus** when you need a decision
4. **Switch to Debate** when abstract talk gets annoying and you need concrete allocation

---

## Advanced: Mode Combinations

Run the same question through multiple modes:

```bash
# Round 1: Get diverse takes
python council.py --mode broadcast
You: "Should we open-source our core tech?"

# Round 2: See them debate it
python council.py --mode chain
You: "Should we open-source our core tech?"

# Round 3: Get a decision
python council.py --mode consensus
You: "Should we open-source our core tech?"
```

This gives you:
- Diverse unbiased opinions (broadcast)
- The full argument (chain)
- A final recommendation (consensus)

---

## Mode Personality Match

If you only use one mode, pick based on your personality:

- **Type A / Decisive** → Consensus Mode
- **Philosophical / Curious** → Chain Mode
- **ADHD / Quick thinker** → Broadcast Mode
- **Strategic / Numbers person** → Debate Mode

---

## The Meta Question

"Which mode should I use for this question?"

**Answer:** Ask that in **Broadcast Mode** and let them tell you. 😎

---

*Pro tip: Start with Broadcast. If any answer triggers "wait, but what about..." → switch to Chain Mode and watch them fight.*
