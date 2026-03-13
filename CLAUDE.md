# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Brainrot is a community-driven learning platform that teaches through real code examples rather than tutorials. The philosophy: "Learn code. Read real examples. Make your own decisions." Built for self-learners who figure things out by doing.

The platform organizes content into channels: `/code`, `/crypto`, `/sports`, `/stoicism`, `/guns`, `/gangster`, `/l33t`, `/asmr`, `/trades`, and `/brainrot`.

## Development Environment

- **Platform**: Linux (Termux-centric development on Android)
- **Languages**: Python 3, Bash
- **Key Dependencies**:
  - Python standard library (json, time, random, curses)
  - termux-tts for text-to-speech functionality
  - GitHub CLI (gh) for automation

## Core Commands (via Makefile)

```bash
make help       # Show available commands
make dashboard  # Launch the Sigma TUI (curses-based terminal dashboard)
make mutate     # Trigger autonomous edit cycle (updates GEMINI_BRAINROT.md and BRAINROT_CONFIG.yml)
make pulse      # Generate new telemetry data (updates deadpan-brainrot.json)
make status     # Display git status and recent system state
make speak      # Use termux-tts to vocalize the latest system log entry
```

## Architecture & Key Systems

### Autonomous Mutation System
The repository features a self-modifying architecture simulating continuous optimization:

- **auto_edit.sh**: The autonomous mutation engine that appends timestamped "machine thoughts" to `GEMINI_BRAINROT.md` and updates the `last_sync` timestamp in `BRAINROT_CONFIG.yml`. Automatically commits and pushes changes.
- **GitHub Actions**: `.github/workflows/pulse.yml` runs mutations hourly and on pushes to specific branches (`feature/pulse-meter`, `hardening/atomic-refactor-67`).

### Telemetry & Monitoring
- **processor.py**: Calculates system metrics including neural load, status, and "Ohio risk factor" (logarithmic scaling based on load). Outputs to `deadpan-brainrot.json`.
- **sigma_dash.py**: Real-time curses TUI displaying system metrics (OHIO risk, RIZZ index, FANUM tax rate, event logs).

### Configuration
- **BRAINROT_CONFIG.yml**: Central system configuration with core parameters, metrics thresholds, and subsystem definitions. Uses creative terminology ("rizz_index", "fanum_tax_rate", "skibidi_latency", "ohio_containment").

### Repository Health
- **audit.sh**: Comprehensive health check script covering 30+ areas (documentation, DX, security, architecture). Can run in report-only mode or create GitHub issues with `--apply` flag.

## File Structure

```
/root/brainrot/
├── Makefile                    # Master control interface
├── auto_edit.sh               # Autonomous mutation engine
├── processor.py               # Telemetry generator
├── sigma_dash.py              # TUI dashboard
├── speak.sh                   # TTS integration
├── audit.sh                   # Repository health auditor
├── BRAINROT_CONFIG.yml        # System configuration
├── GEMINI_BRAINROT.md         # Living system log (continuously updated)
├── deadpan-brainrot.json      # Current telemetry state
├── README.md                  # Project vision and philosophy
├── SUPPORT.md                 # Support channels
├── CONTRIBUTORS               # Project contributors
└── .github/workflows/pulse.yml # Automated mutation workflow
```

## Development Workflow

1. **Making Changes**: Work on feature branches (e.g., `feature/pulse-meter`) or hardening branches (e.g., `hardening/atomic-refactor-67`)
2. **Testing Dashboard**: Run `make dashboard` to verify TUI functionality
3. **Testing Mutations**: Run `make mutate` locally before pushing
4. **Checking Health**: Run `./audit.sh` to identify missing components or improvements
5. **Generating Telemetry**: Run `make pulse` to update system metrics

## Special Considerations

- The project uses creative "brainrot" terminology throughout (Ohio, rizz, sigma, fanum tax) - this is intentional and part of the project's identity
- The autonomous mutation system is a key feature, not a bug - it simulates self-aware repository optimization
- TTS integration via `termux-tts-speak` requires Termux environment
- GitHub Actions bot commits as "Imperial-Bot" with email `bot@brainrot.internal`

## Python Scripts

All Python scripts use Python 3 and are self-contained with minimal dependencies:
- Run directly: `python3 script_name.py`
- No virtual environment or package manager required for current scripts
- Uses only Python standard library (except termux-tts command-line tool)

## Git Workflow

- Main branch: `main`
- Feature branches trigger automated workflows
- Autonomous mutations push directly from GitHub Actions
- Project maintains a playful, experimental commit style (e.g., "auto-edit: recursive self-optimization cycle [SIGMA]")
