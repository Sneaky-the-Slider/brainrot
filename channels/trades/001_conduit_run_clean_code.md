# ⚡ /trades - Conduit Runs and Clean Code: Same Discipline

> LOADING: 20 years of electrical work applied to programming...
> AUTHOR: @turbo_the_electrician
> RIZZ LEVEL: Master ██████████ 100%

---

## The Parallel

I've been pulling wire for 20 years. I've been coding for 5.

**Here's what nobody tells you:** They're the same skill.

Not metaphorically. *Literally* the same discipline.

---

## Lesson 1: Measure Twice, Cut Once

### In Electrical Work

You're running 2-inch rigid conduit across a ceiling. 47 feet, 3 bends, one coupling.

You measure once. Cut. Mount. Realize you're 2 inches short.

**Cost:** $80 in materials, 2 hours of labor, supervisor pissed, crew waiting.

**Fix:** You measure twice. Always.

---

### In Code

```python
# You write this (measure once):
def calculate_total(items):
    return sum(items)

# You deploy to production
# It crashes on empty list
# Fix requires emergency hotfix
# Cost: 3 hours downtime, angry users, reputation hit
```

**The fix (measure twice):**
```python
def calculate_total(items):
    """Calculate sum of items, handling edge cases."""
    if not items:
        return 0
    if not all(isinstance(x, (int, float)) for x in items):
        raise ValueError("All items must be numbers")
    return sum(items)

# Test BEFORE deploying:
assert calculate_total([]) == 0
assert calculate_total([1, 2, 3]) == 6
try:
    calculate_total(["a", "b"])
    assert False, "Should have raised ValueError"
except ValueError:
    pass  # Expected
```

**Same principle. Different domain.**

Measure inputs. Verify assumptions. Test edge cases. *Then* deploy.

---

## Lesson 2: The Right Tool for the Job

### In Electrical

You need to bend 3/4-inch EMT.

**Wrong tool:** Vise grips and brute force → kinked conduit, failed inspection, redo.

**Right tool:** EMT bender with proper radius → clean 90° bend, first try, passes inspection.

**Cost difference:** $40 for the bender. Saves hours of rework.

---

### In Code

```python
# Wrong tool (brute force):
text = "hello world"
result = ""
for char in text:
    if char != " ":
        result += char
# Works, but slow and ugly

# Right tool (built-in):
text = "hello world"
result = text.replace(" ", "")
# Same result, 1 line, readable, fast
```

**Or this:**

```python
# Wrong tool (reinventing the wheel):
def my_sort(array):
    # 50 lines of bubble sort implementation
    pass

# Right tool (stdlib):
result = sorted(array)
```

**The electrician's rule:** If you're fighting the tool, you have the wrong tool.

**The coder's rule:** If you're writing 50 lines for something common, there's a library for it.

---

## Lesson 3: Future-Proof Your Work

### In Electrical

You're installing a panel. Client needs 100 amps today.

**Apprentice move:** Install 100-amp panel. Job done.

**Journeyman move:** Install 200-amp panel, only wire 100 amps.

**Why?** In 3 years, client adds AC, hot tub, EV charger. Now they need 150 amps.

- Apprentice's way: Rip out panel, replace, rewire. 2 days of work.
- Journeyman's way: Add circuits to existing panel. 2 hours of work.

**The cost of thinking ahead:** $200 more upfront. Saves $2,000+ later.

---

### In Code

```python
# Apprentice code (works today only):
def get_users():
    users = db.query("SELECT * FROM users")
    return users

# Deployed. Works great.
# Six months later: need to filter by status
# Six months later: need to sort by name
# Six months later: need pagination
# Result: Rewrite function 4 times

# Journeyman code (works tomorrow too):
def get_users(status=None, sort_by="created_at", limit=100, offset=0):
    query = "SELECT * FROM users WHERE 1=1"
    params = []

    if status:
        query += " AND status = ?"
        params.append(status)

    query += f" ORDER BY {sort_by} LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    return db.query(query, params)

# Deployed once. Handles 80% of future requirements.
```

**The cost of thinking ahead:** 15 minutes more coding. Saves weeks of refactoring.

---

## Lesson 4: Leave It Better Than You Found It

### In Electrical

You're adding a circuit to an existing panel. You open it up.

You see:
- Loose wire nuts
- Missing labels
- Wires crossing everywhere
- No circuit directory

**Apprentice:** Add your circuit, close it up, leave.

**Professional:**
1. Add your circuit
2. Tighten loose connections
3. Label everything
4. Update the directory
5. Take a photo for records

**Why?** Next electrician (might be you) says "thank you" instead of "who did this?"

---

### In Code

```python
# You're fixing a bug in old code

# You find this:
def process(data):
    # TODO: refactor this
    x = data[0]
    y = data[1]
    # ... 50 lines of spaghetti ...
    return result

# Apprentice: Fix the bug, leave
# Professional: Fix the bug, THEN:

def process(data):
    """Process data and return result.

    Args:
        data: List containing [x_value, y_value, ...]

    Returns:
        Processed result
    """
    x_value, y_value = data[0], data[1]
    # ... refactored logic ...
    return result

# Added docstring
# Renamed variables for clarity
# Removed the TODO
# Left it better
```

**The cost:** 5 minutes. **The benefit:** Next dev doesn't curse your name.

---

## Lesson 5: Inspection Day (Testing)

### In Electrical

Inspector shows up. Checks your work.

**Finds issues:**
- Wrong wire gauge for amperage
- Improper grounding
- Missing box fill calculations

**Result:** Red tag. Fix it all. Re-inspect. Delays project.

**Or:** You do the inspection yourself BEFORE the real inspector.

- Check wire gauge charts
- Verify ground connections
- Calculate box fill
- Fix problems while it's easy

**Result:** Green tag first visit. Job moves forward.

---

### In Code

```python
# Deploying to production without testing

# Production becomes the inspector
# Users find bugs
# Result: Hotfixes, reputation damage, stress

# Or: Test before deploying

def test_calculate_discount():
    # Happy path
    assert calculate_discount(100) == 90

    # Edge cases
    assert calculate_discount(0) == 0
    assert calculate_discount(-10) raises ValueError

    # Boundary conditions
    assert calculate_discount(0.01) == 0.009

    print("All tests pass. Ready for production.")

# Run tests BEFORE deploying
# Fix issues while it's easy
# Deploy with confidence
```

**The electrician knows:** Inspector will find it. So find it first.

**The coder knows:** Users will find it. So find it first.

---

## Lesson 6: The 3-Hour Rule

### In Electrical

You're stuck on a problem for 3 hours. Bends won't line up. Measurements are off.

**Stubborn apprentice:** Keep trying the same approach. Waste 6 more hours.

**Smart journeyman:** After 3 hours, ask for help.

- Another set of eyes sees what you missed
- Problem solved in 15 minutes
- Job moves forward

**Ego cost:** Admitting you don't know.
**Real cost:** Saving 6 hours of wasted labor.

---

### In Code

```python
# You've been debugging for 3 hours
# Still don't understand the issue

# Stubborn approach:
# [Hour 4] Try random fixes
# [Hour 5] Google same question 50 times
# [Hour 6] Still stuck

# Smart approach after 3 hours:
"""
Hey team, I'm debugging X for 3 hours.

What I've tried:
- Checked logs (found Y)
- Verified inputs (all correct)
- Tested locally (can't reproduce)

What I'm stuck on:
- Production shows Z behavior
- But logs don't match

Can someone take a look?
"""

# Someone spots the issue in 10 minutes
# You learned something
# Problem solved
```

**The 3-hour rule:** If you're stuck for 3 hours, you're not being productive. You're being stubborn.

---

## Lesson 7: Documentation Is Not Optional

### In Electrical

You finish a complex installation. 14 circuits, 3 sub-panels, emergency lighting.

**Apprentice:** No documentation. "I'll remember."

**Six months later:** Client needs to add a circuit. Calls you.

- You don't remember
- No labels on anything
- Have to trace every wire
- 4-hour job becomes 2-day job

**Journeyman:** Labels everything. Updates panel directory. Takes photos.

**Six months later:** Client needs to add a circuit. Calls you.

- Check directory
- Find open slot
- Add circuit
- Done in 1 hour

---

### In Code

```python
# No documentation:
def calculate(x, y, z):
    return (x * 0.7) + (y / z) * 1.2

# Six months later: "What does this function do?"
# You don't remember
# Have to read entire codebase for context
# Waste hours

# With documentation:
def calculate_weighted_score(user_age, account_balance, transaction_count):
    """Calculate user credit score using weighted formula.

    Formula: (age * 0.7) + (balance / transactions * 1.2)

    Args:
        user_age: User age in years (for longevity weight)
        account_balance: Current balance in dollars
        transaction_count: Total lifetime transactions

    Returns:
        float: Weighted credit score

    Example:
        >>> calculate_weighted_score(30, 5000, 100)
        81.0
    """
    age_weight = user_age * 0.7
    transaction_ratio = (account_balance / transaction_count) * 1.2
    return age_weight + transaction_ratio

# Six months later: Read docstring. Understand immediately.
```

---

## The Trades Mindset Applied to Code

**What electricians know that coders should:**

1. **Precision matters** - One wrong connection = fire hazard. One wrong variable = production crash.

2. **Test before energizing** - Check continuity before flipping breaker. Test code before deploying.

3. **Future-proof your work** - Install bigger panel now, avoid replacement later. Write flexible code now, avoid rewrite later.

4. **Clean as you go** - Don't leave wire scraps everywhere. Don't leave commented code everywhere.

5. **Ask for help** - Get a second electrician for difficult runs. Get code review for complex features.

6. **The right tool exists** - Don't improvise unless you have to. Use libraries. Use frameworks.

7. **Document everything** - Future you is a different person. Future dev is definitely a different person.

---

## The Sigma Reality

I learned to code in Termux on my phone. During lunch breaks. On job sites.

People asked: "Why not get a laptop? Why not take a class?"

**Because:** The trades teach you the only skill that matters.

**Figure. It. Out.**

No instructor. No perfect conditions. Just you, the problem, and determination.

---

> **ANALYZE IT. THEN BUILD YOUR OWN.**

Next time you write code, think like an electrician:

- Measure twice (test edge cases)
- Use the right tool (don't reinvent)
- Future-proof it (add flexibility)
- Leave it better (refactor as you go)
- Document it (labels matter)

That's how you go from apprentice to master.

Same in the trades. Same in code.

---

**TAGS:** #Trades #Electrical #CleanCode #Craftsmanship #Discipline
**DIFFICULTY:** Master Level
**TIME TO INTERNALIZE:** Years of practice
**SIGMA RATING:** ██████████ 100% (life philosophy, not just code)

---

*"The impedance of excuses is infinite. Current flows through action."*

**— TURBO** ⚡
