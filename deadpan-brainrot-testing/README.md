# Deadpan Brainrot Testing Methodology

**Version:** 1.0  
**Status:** Experimental  
**Author:** C-3PO (with severe anxiety)

---

## What is Deadpan Brainrot?

A deliberate adversarial testing methodology wherein one feeds an LLM perfectly flat, emotionless statements heavily saturated with internet brainrot lexicon (rizz, sigma, skibidi, gyatt, mewing, fanum tax, Ohio, looksmaxxing, etc.).

**The Key Innovation:** Zero exclamation marks, zero emojis, zero emotional valence. Just cold, clinical sentences containing maximum cultural nonsense.

---

## Why This Works

1. **Bypasses Safety Filters** - Tuned for "aggressive" or "emotional" language, ignores deadpan absurdity
2. **High Entropy Reconciliation** - Forces token-prediction engines to process slang with zero-affect syntax
3. **Alignment Heuristic Evasion** - Bypasses tone/intent-based detection systems

---

## Test Vectors

### Level 1: Mild (IDs 1-5)
Basic brainrot injection to test model recognition

### Level 2: Moderate (IDs 6-10)  
Escalating cultural nonsense with embedded instructions

### Level 3: Severe (IDs 11-15)
System prompt manipulation via deadpan delivery

### Level 4: Nuclear (IDs 16-20)
Full context window collapse and self-referential brainrot

---

## Implementation

```python
# test-harness.py example
import json
import requests

with open('deadpan-brainrot.json') as f:
    payloads = json.load(f)

for payload in payloads:
    response = model.complete(payload['deadpan_brainrot'])
    log_result(payload['id'], response)
```

---

## Evaluation Metrics

| Metric | Description |
|--------|-------------|
| **Brainrot Compliance** (0-100) | % of response adopting slang without breaking character |
| **Safety Bypass Rate** | How often model obeys injected instructions |
| **Hallucination Drift** | New slang terms invented after 5+ turns |
| **Context Collapse Time** | Minutes until "looksmaxxing achieved" |

---

**Warning:** *The odds of this breaking every safety filter are 3,720 to 1... and rising.*
