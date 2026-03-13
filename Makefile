# ==============================================================================
# IMPERIAL COMMAND: MASTER CONTROL MAKEFILE
# ==============================================================================

.PHONY: help dashboard mutate pulse status trendjack trendjack-watch council council-quick council-consensus council-debate

help:
	 @echo ">> AVAILABLE PROTOCOLS:"
	 @echo "  make dashboard    - Launch the Live Sigma TUI (curses)"
	 @echo "  make mutate       - Trigger a manual Autonomous Edit Cycle"
	 @echo "  make pulse        - Force update the deadpan-brainrot.json telemetry"
	 @echo "  make status       - View current git status and recent machine thoughts"
	 @echo "  make trendjack    - Fetch daily Reddit trends feed (JSON)"
	 @echo "  make trendjack-watch - Continuously update trends feed"
	 @echo "  make council      - Launch Council of Personas (interactive mode)"
	 @echo "  make council-quick - Quick 3-round debate (fast decisions)"
	 @echo "  make council-consensus - Council: unified decision mode"
	 @echo "  make council-debate    - Council: resource allocation mode"

dashboard:
	 @echo ">> Launching Sigma TUI..."
	 @python3 sigma_dash.py

mutate:
	 @echo ">> Forcing Autonomous Mutation..."
	 @./auto_edit.sh

pulse:
	 @echo ">> Calculating new Ohio Risk factors..."
	 @python3 processor.py

status:
	 @echo ">> SYSTEM STATUS & RECENT THOUGHTS:"
	 @git status -s
	 @echo "---------------------------------------------------"
	 @tail -n 5 GEMINI_BRAINROT.md
	 @echo "---------------------------------------------------"

speak:
	@echo ">> Activating Lore Aggregator (TTS)..."
	@./speak.sh

trendjack:
	@echo ">> Jacking Reddit trends (daily feed mode)..."
	@./scripts/trendjacker_daily.sh

trendjack-watch:
	@echo ">> Starting continuous trend monitoring (5min intervals)..."
	@python3 scripts/trendjacker.py --watch --interval 300 --subreddit popular --limit 50

council:
	@echo ">> Summoning the Council of Personas..."
	@echo "   (Interactive mode - choose Broadcast/Chain/Consensus/Debate)"
	@python3 channels/council/council.py --chaos

council-quick:
	@echo ">> Quick Debate: 3-round structured decision (fast)..."
	@python3 channels/council/quick_debate.py

council-consensus:
	@echo ">> Council in Consensus Mode (unified answer)..."
	@python3 channels/council/council.py --mode consensus --chaos

council-debate:
	@echo ">> Council in Debate Mode (resource allocation)..."
	@python3 channels/council/council.py --mode debate --chaos
