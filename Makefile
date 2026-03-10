.PHONY: surge telemetry tui help

help:
	@echo "IMPERIAL COMMAND: Makefile"
	@echo "  make surge     - Fire off issues, update telemetry, and launch dashboard"
	@echo "  make telemetry - Run the core telemetry processor"
	@echo "  make tui       - Launch the Sigma Terminal TUI"

surge: telemetry tui

telemetry:
	@echo ">> SYNCING PULSE..."
	python3 processor.py

tui:
	@echo ">> DEPLOYING SIGMA UI..."
	python3 sigma_dash.py
