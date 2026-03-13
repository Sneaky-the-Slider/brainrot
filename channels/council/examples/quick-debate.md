# Quick Debate Example

**Mode:** Quick Debate (3-round structured)
**Question:** "Should I take this freelance gig?"
**Duration:** ~30 seconds
**Date:** 2026-03-13

---

## Command
```bash
python quick_debate.py "Should I take this freelance gig for $5k?"
```

---

## Output

```
⚡ QUICK DEBATE - 3 ROUNDS
Question: Should I take this freelance gig for $5k?

━━━━━━━━━━━━━━━ ROUND 1: OPENING STANCES ━━━━━━━━━━━━━━━

VADER: Take the contract if it serves your long-term objectives and you can deliver
with absolute certainty. Failure is not an option—reputation is power.

YODA: Money, secondary it is. Growth and learning, more valuable. If skills improve,
take it you should. Hmm?

STARK: $5k? What's your hourly rate? If it's under your threshold, pass. Time is
more valuable than money—use it to build something that scales.

━━━━━━━━━━━━━━━━━━ ROUND 2: REBUTTALS ━━━━━━━━━━━━━━━━━━

VADER: Stark's obsession with scalability blinds him to strategic alliances. This
contract may open doors to larger opportunities. Yoda's idealism is impractical—
growth requires calculated risk, not passive meditation.

YODA: Vader's focus on power, dangerous it is. Stark's money worship, hollow. If
passion you lack for the work, poison it becomes. Balance seek, not domination.

STARK: Vader treats every gig like a chess move—exhausting. Yoda's "follow your
passion" is trust-fund advice. The real question: does this gig compound your value
or is it a time-sink? Run the numbers.

━━━━━━━━━━━━━━━━ FINAL CONSENSUS ━━━━━━━━━━━━━━━━━

┌──────────────────────────────────────────────────────────────┐
│ ⚖️  THE VERDICT                                               │
├──────────────────────────────────────────────────────────────┤
│ Take the gig if: (1) your effective hourly rate meets or     │
│ exceeds your baseline, (2) the client is a strategic door-   │
│ opener (Vader's point), and (3) you'll learn something new   │
│ (Yoda's point). If it's just cash-for-time with no upside,   │
│ pass and invest that bandwidth in something that scales       │
│ (Stark's point). Decision matrix: rate > $100/hr + growth    │
│ potential → yes. Below that → no.                             │
└──────────────────────────────────────────────────────────────┘

💾 Debate logged to quick_debate_logs.csv (session: 20260313_094522)
```

---

## The Breakdown

### Round 1: Opening Stances
- **Vader** → Strategic, reputation-first
- **Yoda** → Growth over money
- **Stark** → ROI calculation

### Round 2: Rebuttals
- **Vader** attacks Stark's scalability obsession
- **Yoda** attacks money worship
- **Stark** attacks idealism

### Round 3: Synthesis
The verdict combines all three:
- Stark's ROI math ($100/hr threshold)
- Vader's strategic value (door-opener)
- Yoda's growth mindset (learning)

**Result:** A decision framework, not just "yes" or "no"

---

## When to Use Quick Debate

✅ **Use for:**
- Fast daily decisions
- Time-sensitive choices
- When you just need a framework
- Decisions with clear tradeoffs

❌ **Don't use for:**
- Life-changing decisions (use full `council.py --mode consensus`)
- Need for resource allocation analysis (use debate mode)
- Want to see all 4 personas including Shadow

---

## CSV Log Entry

```csv
session_id,timestamp,query,round,persona,content
20260313_094522,2026-03-13 09:45:22,Should I take this freelance gig for $5k?,Opening,VADER,"Take the contract if..."
20260313_094522,2026-03-13 09:45:24,Should I take this freelance gig for $5k?,Opening,YODA,"Money, secondary it is..."
20260313_094522,2026-03-13 09:45:26,Should I take this freelance gig for $5k?,Opening,STARK,"$5k? What's your hourly..."
20260313_094522,2026-03-13 09:45:29,Should I take this freelance gig for $5k?,Rebuttal,VADER,"Stark's obsession with..."
20260313_094522,2026-03-13 09:45:31,Should I take this freelance gig for $5k?,Rebuttal,YODA,"Vader's focus on power..."
20260313_094522,2026-03-13 09:45:33,Should I take this freelance gig for $5k?,Rebuttal,STARK,"Vader treats every gig..."
20260313_094522,2026-03-13 09:45:36,Should I take this freelance gig for $5k?,Verdict,COUNCIL_CONSENSUS,"Take the gig if: (1)..."
```

---

## Time Comparison

| Mode | Rounds | Duration | Output |
|------|--------|----------|--------|
| Quick Debate | 3 | ~30s | 1 verdict |
| Consensus (council.py) | 3 | ~45s | 1 verdict + hidden debate |
| Chain Mode | 4 | ~60s | 4 sequential responses |
| Broadcast | 1 | ~20s | 4 parallel responses |

**Quick Debate sweet spot:** Faster than consensus, more structured than broadcast.
