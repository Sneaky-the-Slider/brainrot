# 📊 Council Debate Logging

All council debates are automatically logged to `council_logs.csv` for analysis, research, or just revisiting epic debates.

## CSV Structure

```csv
session_id,timestamp,mode,query,round,persona,content
20260313_140522,2026-03-13 14:05:25,chain,Should we trust AI?,round_1,VADER,"Trust is irrelevant..."
20260313_140522,2026-03-13 14:05:28,chain,Should we trust AI?,round_2,YODA,"Dangerous, blind trust is..."
20260313_140522,2026-03-13 14:05:31,chain,Should we trust AI?,round_3,STARK,"I trust JARVIS because..."
```

### Fields

- **session_id** - Unique ID for each council session (timestamp-based)
- **timestamp** - Exact time of response
- **mode** - Which mode was used (broadcast/chain/consensus/debate)
- **query** - Your original question (truncated to 100 chars)
- **round** - Round number or stage (round_1, round_2, verdict, etc.)
- **persona** - Which agent responded
- **content** - The full response text

## Usage Examples

### Basic Usage (auto-enabled)
```bash
python council.py
# Logs to council_logs.csv by default
```

### Custom Log File
```bash
python council.py --log my_debates.csv
```

### Disable Logging
```bash
python council.py --no-log
```

## Analysis Scripts

### 1. View Recent Debates
```python
import pandas as pd

df = pd.read_csv('council_logs.csv')
recent = df[df['session_id'] == df['session_id'].max()]
print(recent[['persona', 'round', 'content']])
```

### 2. Compare Persona Response Times
```python
import pandas as pd

df = pd.read_csv('council_logs.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Group by persona and count responses
persona_stats = df.groupby('persona').agg({
    'content': ['count', lambda x: x.str.len().mean()]
})
print(persona_stats)
```

### 3. Extract All Consensus Verdicts
```python
import pandas as pd

df = pd.read_csv('council_logs.csv')
verdicts = df[df['round'] == 'verdict']
print(verdicts[['timestamp', 'query', 'content']])
```

### 4. Find Most Debated Topics
```python
import pandas as pd

df = pd.read_csv('council_logs.csv')
topic_counts = df.groupby('query').size().sort_values(ascending=False)
print(topic_counts.head(10))
```

## Log Management

### Cleanup Old Sessions
```bash
# Keep only last 100 sessions
python -c "
import pandas as pd
df = pd.read_csv('council_logs.csv')
recent_sessions = df['session_id'].unique()[-100:]
df_clean = df[df['session_id'].isin(recent_sessions)]
df_clean.to_csv('council_logs.csv', index=False)
"
```

### Export to JSON
```bash
python -c "
import pandas as pd
df = pd.read_csv('council_logs.csv')
df.to_json('council_logs.json', orient='records', indent=2)
"
```

### Search Debates
```bash
# Find all debates about AI
grep -i "AI" council_logs.csv
```

## Research Applications

### 1. Persona Bias Analysis
Track which persona tends toward which solutions:
- Vader → security/control
- Yoda → balance/patience
- Stark → innovation/speed
- Shadow → contrarian/skeptical

### 2. Mode Effectiveness
Compare consensus quality across modes:
- Broadcast: diverse but potentially contradictory
- Chain: argumentative but thorough
- Consensus: unified but time-consuming
- Debate: reveals priorities through resource allocation

### 3. Question Quality
Analyze which question formats produce better debates:
- Open-ended vs. binary
- Philosophical vs. tactical
- Abstract vs. concrete

## Privacy Note

**Logs contain:**
- Your questions/prompts
- AI responses
- Timestamps

**Logs do NOT contain:**
- API keys
- Personal identifying information
- System details

Keep your log files secure if your questions contain sensitive business/personal info.

## Integration with Other Tools

### Export to Obsidian
```bash
python -c "
import csv
with open('council_logs.csv') as f:
    reader = csv.DictReader(f)
    sessions = {}
    for row in reader:
        sid = row['session_id']
        if sid not in sessions:
            sessions[sid] = []
        sessions[sid].append(row)

    for sid, rows in sessions.items():
        with open(f'debate_{sid}.md', 'w') as out:
            out.write(f'# Council Debate: {rows[0][\"query\"]}\n\n')
            for r in rows:
                out.write(f'**{r[\"persona\"]}** ({r[\"round\"]}): {r[\"content\"]}\n\n')
"
```

### Feed to Another AI for Meta-Analysis
```bash
# Get last session, ask GPT-4 to summarize
python -c "
import pandas as pd
df = pd.read_csv('council_logs.csv')
last = df[df['session_id'] == df['session_id'].max()]
print(last.to_string())
" | pbcopy  # Now paste into ChatGPT/Claude
```

---

**Pro tip:** Run `--no-log` for casual chats. Enable logging for important decisions you want to review later.
