# 👾 /l33t - grep: The Command That Finds Anything

> LOADING: grep power moves...
> AUTHOR: @terminal_ninja
> RIZZ LEVEL: Intermediate ██████░░░░ 60%

---

## The Basics (You Already Know This Part)

```bash
grep "search_term" file.txt
```

Finds lines containing "search_term" in file.txt. Cool. Boring. Everyone knows this.

---

## The Real Moves Start Here

### 1. Search Recursively Through Entire Codebases

```bash
grep -r "function login" .
```

**What it does:** Searches every file in current directory and subdirectories for "function login"

**Why you care:** Finding where a function is defined across 1000+ files. No IDE needed.

**Pro move:**
```bash
grep -rn "TODO" . | wc -l
```
Count how many TODO comments exist in your entire project. Watch your soul leave your body when it's over 200.

---

### 2. Invert the Search (Show What DOESN'T Match)

```bash
grep -v "test" file.txt
```

**What it does:** Shows every line that does NOT contain "test"

**Real use case:**
```bash
cat /var/log/nginx/access.log | grep -v "bot" | grep -v "spider"
```
Filter out all bot traffic from logs. See what actual humans are doing.

**Electrician analogy:** Finding which circuits are NOT on a breaker. Process of elimination.

---

### 3. Case-Insensitive Search (Because Caps Lock Happens)

```bash
grep -i "error" log.txt
```

Finds: error, Error, ERROR, ErRoR

**Combine with other flags:**
```bash
grep -ri "password" /var/www/
```
Find every file in your web directory with the word "password" (any capitalization). Security audit in one line.

---

### 4. Show Context (Lines Before and After)

```bash
grep -A 3 -B 3 "Exception" error.log
```

**What it does:**
- `-A 3` = Show 3 lines AFTER match
- `-B 3` = Show 3 lines BEFORE match
- `-C 3` = Show 3 lines on both sides (shorthand)

**Why it matters:** Error messages usually span multiple lines. Context is everything.

**Example:**
```bash
grep -C 5 "Fatal error" /var/log/app.log
```
See what happened before and after the crash. Debugging gold.

---

### 5. Count Occurrences (Not Just Show Them)

```bash
grep -c "failed login" auth.log
```

**What it does:** Just shows the NUMBER of matches, not the actual lines.

**Real scenario:**
```bash
grep -c "127.0.0.1" access.log
```
How many requests came from localhost? If it's 10,000 and you're being DDoS'd, you know it's internal.

---

### 6. Multiple Patterns (OR Logic)

```bash
grep -E "error|warning|critical" system.log
```

**What it does:** Find lines with "error" OR "warning" OR "critical"

**Advanced:**
```bash
grep -E "(fail|error|crash)" -r /var/log/ | wc -l
```
Count all failures across ALL logs. System health check in one command.

---

### 7. Match Whole Words Only

```bash
grep -w "test" file.txt
```

**The difference:**
- `grep "test"` matches: test, testing, attest, contest
- `grep -w "test"` matches: only "test" as a standalone word

**Use case:**
```bash
grep -w "root" /etc/passwd
```
Find the root user, not "groot" or "beetroot" entries.

---

### 8. Show Only Filenames (Not the Matches)

```bash
grep -rl "API_KEY" .
```

**What it does:** Lists ONLY the files that contain matches, not the content.

**Real use:**
```bash
grep -rl "hardcoded_password" /var/www/
```
Security audit: which files have hardcoded credentials? Fix them all.

---

### 9. Exclude Directories (Speed Boost)

```bash
grep -r "import" --exclude-dir=node_modules .
```

**Why:** node_modules has 100,000 files. You don't need to search it. Ever.

**Pro move:**
```bash
grep -r "console.log" --exclude-dir={node_modules,dist,build} .
```
Find all debug statements you forgot to remove, but don't waste time on compiled/dependency code.

---

### 10. Regex Power (When You Need Surgery, Not Sledgehammers)

```bash
grep -E "^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" access.log
```

**What it does:** Extract all IP addresses from a log file.

**Another example:**
```bash
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" scraped_data.txt
```
Extract all email addresses. Data mining in one line.

---

## The Combos (Where It Gets Spicy)

### Combo 1: Find and Replace at Scale
```bash
grep -rl "old_function" . | xargs sed -i 's/old_function/new_function/g'
```

**What it does:**
1. Find all files with "old_function"
2. Pipe to `xargs` (run command on each file)
3. Replace old_function with new_function in ALL files

**Warning:** Backup first. This is nuclear.

---

### Combo 2: Security Audit Pipeline
```bash
grep -rn "eval(" . | grep -v "node_modules" | grep "\.js$"
```

**What it does:**
1. Find all uses of `eval()` (dangerous function)
2. Exclude node_modules
3. Only show .js files (not .json or others)
4. Line numbers included (`-n`)

**Result:** List of potential security vulnerabilities with exact line numbers.

---

### Combo 3: Log Analysis Kill Chain
```bash
cat access.log | grep "POST" | grep "login" | grep -v "200" | awk '{print $1}' | sort | uniq -c | sort -rn
```

**What it does:**
1. Filter for POST requests to login
2. Exclude successful logins (200 status)
3. Extract IP addresses
4. Count occurrences per IP
5. Sort by most attempts

**Result:** List of IPs trying to brute force your login, sorted by aggression.

---

### Combo 4: Find Files Modified in Last 24 Hours With Specific Content
```bash
find . -type f -mtime -1 -exec grep -l "TODO" {} \;
```

**What it does:**
1. Find files modified in last 24 hours
2. Check if they contain "TODO"
3. List the files

**Use case:** What did I just break? What needs cleanup before commit?

---

## The Termux Reality

Running this on Android via Termux? Same commands. Same power. Just slower CPU.

**Termux optimization:**
```bash
# Don't search the entire storage
grep -r "pattern" ~/storage/downloads --exclude="*.mp4" --exclude="*.jpg"
```

Exclude media files. You're looking for code/text, not movies.

---

## When grep Isn't Enough

**Use `ripgrep` (rg) instead:**
```bash
# Install: pkg install ripgrep
rg "search term"
```

**Why?**
- 10-100x faster than grep
- Ignores .gitignore by default
- Better defaults (colors, line numbers, etc.)
- Same syntax as grep

**Example:**
```bash
rg "function.*login" --type js
```
Find all JavaScript files with "function" followed by "login". Lightning fast.

---

## The Three Rules of grep Mastery

1. **Always use `-r` when searching directories** (don't manually cat every file)
2. **Always use `-n` when debugging** (line numbers save lives)
3. **Always pipe to `less` when output is huge** (`grep pattern file | less`)

---

## Try It Yourself

**Challenge 1: Security Audit**
```bash
grep -rn "password\s*=\s*['\"]" /var/www/
```
Find hardcoded passwords in your web directory. Format: `password = "something"`

**Challenge 2: Performance Hunt**
```bash
grep -r "console.log" src/ | wc -l
```
Count how many debug statements you left in production code. Shame yourself. Remove them.

**Challenge 3: Dependency Hell**
```bash
grep -r "require\|import" . --include="*.js" | grep -v "node_modules" | wc -l
```
How many import statements exist in your project? If it's over 500, refactor time.

---

> **ANALYZE IT. THEN BUILD YOUR OWN.**

Build a log analysis script using grep.

Extract the top 10 IPs hitting your server.
Find the most requested URLs.
Identify failed requests.

No fancy tools. Just grep, awk, sort, uniq.

That's how you learn the terminal. Not by reading man pages.

---

**TAGS:** #grep #Terminal #Linux #Termux #LogAnalysis #l33t
**DIFFICULTY:** Intermediate
**TIME TO MASTER:** 1 week of daily use
**SIGMA RATING:** █████████░ 90% (essential skill, no cap)
