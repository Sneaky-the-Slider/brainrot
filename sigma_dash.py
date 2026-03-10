import curses
import time
import random
import json

def draw_dashboard(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    
    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        # Simulated Data
        ohio_risk = random.randint(70, 99)
        rizz = random.randint(3000, 9001)
        bar = "#" * (ohio_risk // 3) + "-" * (33 - (ohio_risk // 3))
        
        # Header
        stdscr.addstr(1, 2, "=== IMPERIAL COMMAND: SIGMA TERMINAL ===", curses.A_BOLD)
        stdscr.addstr(3, 2, f"Target Repo : Turbo-the-tech-dev/brainrot")
        stdscr.addstr(4, 2, f"Connection  : SECURE (Termux Local)")
        
        # Metrics
        stdscr.addstr(6, 2, f"OHIO RISK  : [{bar}] {ohio_risk}%")
        stdscr.addstr(7, 2, f"RIZZ INDEX : {rizz} (CRITICAL)")
        stdscr.addstr(8, 2, f"FANUM TAX  : 0.05% (ROUTED TO /DEV/NULL)")
        
        # Logs
        stdscr.addstr(10, 2, "--- LIVE EVENT LOG ---")
        stdscr.addstr(11, 2, f"> [{time.strftime('%H:%M:%S')}] Pulse synchronized with absolute_velocity.json")
        stdscr.addstr(12, 2, f"> [{time.strftime('%H:%M:%S')}] Auto-Triage bot merged 3 PRs.")
        
        stdscr.addstr(height-2, 2, "Press 'q' to exit back to standard shell.", curses.A_DIM)
        
        stdscr.refresh()
        
        # Check for exit
        c = stdscr.getch()
        if c == ord('q'):
            break
            
        time.sleep(0.5)

if __name__ == "__main__":
    curses.wrapper(draw_dashboard)
