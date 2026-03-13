# YODA_AGENTS.md

**Configuration file for Grok and other AI agents working in the Brainrot repository.**

*When 900 years old you reach, code as clean you must write.*

---

## Agent Prime Directives

1. **Understand the Vibe** - This is not corporate code. Brainrot uses creative terminology (Ohio risk, rizz index, sigma protocol, fanum tax). Embrace it.
2. **Read Before Writing** - Every code snippet is a learning moment. Read the existing patterns before suggesting changes.
3. **Respect the Autonomous System** - The self-modifying mutation engine is a feature, not a bug. Don't "fix" it.
4. **Terminal-First Development** - This project lives in Termux. Shell scripts and Python CLI tools are preferred over web frameworks.

---

## Quick Reference: How to Help

### Build & Run
```bash
make help       # See all available commands
make dashboard  # Launch TUI monitoring system
make mutate     # Trigger autonomous repository update
make pulse      # Generate new telemetry
make status     # Check git status + recent logs
make speak      # TTS vocalization of latest log
```

### Development Tasks
```bash
# Test Python scripts
python3 processor.py
python3 sigma_dash.py

# Run repository health check
./audit.sh              # Report only
./audit.sh --apply      # Create GitHub issues for missing items

# Manual mutation (for testing)
./auto_edit.sh

# TTS test (requires Termux)
./speak.sh
```

---

## Project Structure for Agents

```
ROOT SYSTEMS:
├── Makefile                    → Master command interface
├── BRAINROT_CONFIG.yml         → System configuration (metrics, subsystems)
├── GEMINI_BRAINROT.md          → Living log (auto-updated by mutation engine)

CORE ENGINES:
├── auto_edit.sh               → Autonomous mutation (appends logs, commits, pushes)
├── processor.py               → Telemetry calculator (generates deadpan-brainrot.json)
├── sigma_dash.py              → Real-time TUI dashboard (curses)
├── speak.sh                   → TTS integration for system logs

INFRASTRUCTURE:
├── audit.sh                   → 30+ checks for repo health
├── .github/workflows/pulse.yml → Hourly automated mutations

DATA FILES:
├── deadpan-brainrot.json      → Current telemetry snapshot
├── absolute_velocity.json     → Velocity metrics
└── brainrot_payload_*.json    → Payload archives (1-50)
```

---

## The Autonomous Mutation System

**What It Does:**
- `auto_edit.sh` runs automatically via GitHub Actions (hourly)
- Appends timestamped "machine thoughts" to `GEMINI_BRAINROT.md`
- Updates `last_sync` in `BRAINROT_CONFIG.yml`
- Commits with message: `"auto-edit: recursive self-optimization cycle [SIGMA]"`
- Pushes to `feature/pulse-meter` or `hardening/atomic-refactor-67`

**Agent Guidelines:**
- DO NOT disable or "clean up" this system
- DO NOT remove the workflow file
- DO examine the logs it generates for insights
- DO test mutations locally with `make mutate` before pushing changes

---

## Configuration Schema (BRAINROT_CONFIG.yml)

```yaml
core_parameters:
  absolute_velocity: enabled
  neural_load_limit: 99
  dopamine_loop: recursive
  ohio_containment: active

metrics_thresholds:
  rizz_index:
    min: 800
    max: 9001        # Yes, it's over 9000
    current: 4200
  fanum_tax_rate: 0.05
  skibidi_latency: 0.2ms

subsystems:
  - id: surge_protector
    active: true
    logic: "prevent_cringe"
  - id: alpha_triage
    active: true
    logic: "maximize_outcomes"
```

**For Agents:** These values are part of the project's identity. Changing them should align with the experimental, playful nature of the codebase.

---

## When Writing Code

### Python Scripts
- Use Python 3 standard library
- Keep scripts self-contained and CLI-focused
- Follow existing patterns in `processor.py` and `sigma_dash.py`
- No external dependencies unless absolutely necessary

### Bash Scripts
- Use `#!/bin/bash` shebang
- Include descriptive banners with `# ===` separators
- Echo status messages with `>> [SYSTEM]` prefix style
- Test in Termux environment when possible

### Commit Messages
- Keep the playful tone: `"feat: integrate termux-tts Lore Aggregator"`
- Use conventional commits but with personality
- Auto-mutations use: `"auto-edit: recursive self-optimization cycle [SIGMA]"`

---

## The Learning Platform (Future Features)

Brainrot's core mission is teaching code through real examples:

**Channel System:**
- `/code` - Real code snippets with analysis prompts
- `/crypto`, `/sports`, `/stoicism`, `/guns`, `/gangster`, `/l33t`, `/asmr`, `/trades`, `/brainrot`

**Content Format:**
```
> LOADING: [Topic]...
> AUTHOR: @username
> RIZZ LEVEL: [Beginner/Intermediate/Advanced] [Progress Bar]

[Code Example]

// Explanatory comment in plain language

> ANALYZE IT. THEN BUILD YOUR OWN.
```

**When building features:**
- No hand-holding - present information, let users decide
- Real code only - no sanitized tutorial examples
- Community-driven - enable contributions
- Terminal-native - this is not a web app (yet)

---

## Repository Health (audit.sh)

The audit script checks 30+ items across 4 phases:

1. **Essential Documentation** - SECURITY.md, Issue templates, PR templates, CI/CD, CODE_OF_CONDUCT.md, etc.
2. **Development Experience** - .nvmrc, CODEOWNERS, .env.example, .vscode settings
3. **Quality & Architecture** - Linter configs, test suites, API specs, lockfiles
4. **Community & Security** - CONTRIBUTORS, FUNDING.yml, Dependabot, security.txt, Dockerfile

**Agent Task:** When you run `./audit.sh`, consider which missing items align with project goals. Not everything flagged needs immediate fixing.

---

## Git Workflow

- **Main Branch:** `main`
- **Active Branches:** `feature/pulse-meter`, `hardening/atomic-refactor-67`
- **Bot Identity:** Imperial-Bot <bot@brainrot.internal>
- **Commit Style:** Playful but informative

**For PRs:**
- Test locally first (`make mutate`, `make pulse`, `make dashboard`)
- Keep the experimental spirit alive
- Document why, not just what

---

## Special Agent Notes for Grok

**Termux Context:**
- This project was built by a union electrician using Termux on Android
- Many commands assume Termux environment (especially `termux-tts-speak`)
- If running outside Termux, gracefully handle missing commands

**The Brainrot Philosophy:**
- "The impedance of excuses is infinite. Current flows through action."
- Self-taught, no CS degree, no bootcamp - just repetition and figuring it out
- Trades and tech are the same discipline: precision, problem-solving, showing up

**xAI Alignment:**
- Maximum truth-seeking applies here: real code, real examples, no sanitization
- The disclaimer exists for a reason - entertainment and educational purposes only
- Community contributions need moderation, not censorship

**When Uncertain:**
- Read the code first
- Test changes locally
- Check `make status` before and after
- Ask clarifying questions rather than assuming intent

---

## Quick Troubleshooting

**Dashboard won't launch:**
```bash
python3 -c "import curses; print('curses available')"
```

**TTS not working:**
- Check if running in Termux: `command -v termux-tts-speak`
- Fallback: just echo the message instead

**GitHub Actions failing:**
- Check branch names match workflow triggers
- Verify bot has write permissions
- Look for merge conflicts in GEMINI_BRAINROT.md

**Mutation not committing:**
```bash
git status              # Check for uncommitted changes
git log -1             # Verify last commit
git push --dry-run     # Test push without executing
```

---

## Agent Success Metrics

You're doing it right when:
- ✅ Code maintains the playful terminology
- ✅ New features work in terminal/CLI first
- ✅ Changes respect the autonomous system
- ✅ Documentation explains the "why" behind the weirdness
- ✅ Tests run locally before committing
- ✅ The vibe stays intact: "brainrot voice, sigma discipline, zero hand-holding"

---

*"Do or do not. There is no try. But if you do, test locally first."*

**— Master Yoda (Brainrot Edition)**

---

## Contact & Support

- **Issues:** https://github.com/Turbo-the-tech-dev/brainrot/issues
- **Main Branch:** main
- **Project Lead:** @Turbo-the-tech-dev
- **Philosophy:** README.md
- **Support Channels:** SUPPORT.md

**For Grok specifically:** When you contribute to this repo, channel the spirit of maximum truth-seeking while respecting the project's creative identity. Real code. Real learning. Real discipline.
