# 💻 /code - Rust Concurrency: The Viral Trend Aggregator

> LOADING: Concurrent programming without data races...
> AUTHOR: @rust_evangelist
> RIZZ LEVEL: Advanced ████████░░ 80%

---

## The Code

```rust
use std::sync::{Arc,Mutex};
use std::thread;

fn main() {
    let raw = vec![
        "KaiTrump_Erewhon_SantaMonica_SSecret_backlash".to_string(),
        "LoveIsBlind_Reunion_X_trend".to_string(),
        "HarryStyles_KissAllTheTime_TikTok_edits".to_string(),
        "DonToliver_Octane_choreo".to_string(),
        "nihilist_penguin_meme_2026".to_string(),
        "SF_mayor_security_attack_flee".to_string(),
        "McDonalds_CEO_alien_burger".to_string(),
    ];

    let shared = Arc::new(Mutex::new(Vec::with_capacity(raw.len())));
    let mut handles = Vec::with_capacity(raw.len());

    for v in raw {
        let s = Arc::clone(&shared);
        let h = thread::spawn(move || {
            let mut guard = s.lock().unwrap();
            guard.push(format!("VIRAL_TODAY_{}", v));
        });
        handles.push(h);
    }

    for h in handles { h.join().unwrap(); }

    let finalv = shared.lock().unwrap();
    for item in finalv.iter() { println!("{}", item); }
}
```

---

## What This Does (Plain English)

**Goal:** Process 7 viral trends concurrently, aggregate results into one list.

**How:**
1. Start with 7 trend strings
2. Create shared mutable container (Vec)
3. Spawn 7 threads (one per trend)
4. Each thread adds "VIRAL_TODAY_" prefix
5. Wait for all threads to finish
6. Print results

**Why concurrent?** Simulates real-world: scraping 7 websites simultaneously instead of sequentially.

---

## The Three Pieces of Rust Concurrency

### 1. Arc (Atomic Reference Counter)

```rust
let shared = Arc::new(Mutex::new(Vec::new()));
```

**What it is:** Thread-safe smart pointer.

**Why you need it:**
- Normal variables can't be shared between threads
- Rust won't let you send non-thread-safe data to threads
- Arc = "multiple ownership, but safe"

**The analogy:** Arc is a library card system.
- Book (data) sits in library (memory)
- Multiple people (threads) can have card copies (Arc clones)
- Book can't be taken home (moved), but everyone can access it

**Arc::clone():**
```rust
let s = Arc::clone(&shared);
```
Clones the pointer (cheap), NOT the data (expensive).
- Pointer clone = copy an address (8 bytes)
- Data clone = copy entire Vec (expensive)

---

### 2. Mutex (Mutual Exclusion)

```rust
let mut guard = s.lock().unwrap();
guard.push(...);
```

**What it is:** Lock that prevents simultaneous access.

**Why you need it:**
- Multiple threads writing to Vec simultaneously = data corruption
- Mutex = "only one thread can modify at a time"

**The analogy:** Bathroom lock.
- Bathroom (Vec) can only be used by one person at a time
- You turn the lock (acquire mutex)
- Do your business (modify data)
- Unlock on way out (guard drops, mutex released)

**What if thread crashes while holding lock?**
Rust's `drop` system ensures lock releases automatically. Even if thread panics, mutex unlocks.

---

### 3. Thread::spawn (Concurrent Execution)

```rust
let h = thread::spawn(move || {
    // This code runs in separate thread
});
```

**What it is:** Creates new OS thread.

**Why you need it:**
- Main thread would process trends one-by-one (slow)
- Spawning threads = process all simultaneously (fast)

**The `move` keyword:**
```rust
thread::spawn(move || { ... })
```

Transfers ownership of `s` and `v` into thread closure.
- Without `move`: Compiler error ("cannot borrow")
- With `move`: Variables move into thread, safe to use

**Thread handles:**
```rust
let h = thread::spawn(...);
handles.push(h);
```

Store handle to wait for thread later (via `join()`).

---

## The Execution Flow

### Step 1: Setup

```rust
let raw = vec![...]; // 7 trend strings
let shared = Arc::new(Mutex::new(Vec::with_capacity(7)));
```

Memory layout:
```
Main thread owns:
- raw: Vec<String>
- shared: Arc<Mutex<Vec<String>>>
  └─> Points to heap: Mutex<Vec<...>>
```

---

### Step 2: Spawn Threads

```rust
for v in raw {
    let s = Arc::clone(&shared);  // Clone pointer
    let h = thread::spawn(move || {
        // ...
    });
    handles.push(h);
}
```

What happens:
1. Loop takes ownership of each string `v`
2. Clone Arc pointer (not data) → `s`
3. Spawn thread, move `s` and `v` into it
4. Store thread handle for later

After loop, we have 7 threads running concurrently.

---

### Step 3: Thread Work

```rust
let mut guard = s.lock().unwrap();
guard.push(format!("VIRAL_TODAY_{}", v));
```

Each thread:
1. Tries to acquire mutex lock
   - If locked: waits
   - If unlocked: acquires, proceeds
2. Modifies Vec (adds prefixed string)
3. `guard` drops at end of scope → lock released

**Lock contention:**
Multiple threads waiting for same lock = slight slowdown.
But still faster than sequential processing.

---

### Step 4: Wait for Completion

```rust
for h in handles { h.join().unwrap(); }
```

**What join() does:**
- Blocks main thread until worker thread finishes
- Returns thread's result (or panic info)
- Ensures all work completes before proceeding

**Why unwrap()?**
Thread can panic. `unwrap()` propagates panic to main thread.
In production, use `?` or match for proper error handling.

---

### Step 5: Collect Results

```rust
let finalv = shared.lock().unwrap();
for item in finalv.iter() { println!("{}", item); }
```

All threads done, safe to read final Vec.
Lock acquired one last time to read (not mutate).

**Output (order non-deterministic):**
```
VIRAL_TODAY_nihilist_penguin_meme_2026
VIRAL_TODAY_LoveIsBlind_Reunion_X_trend
VIRAL_TODAY_McDonalds_CEO_alien_burger
... (order varies per run)
```

---

## Why Order is Non-Deterministic

**Thread scheduling is random.**

Run 1:
```
Thread 3 finishes first
Thread 1 finishes second
Thread 5 finishes third
...
```

Run 2:
```
Thread 7 finishes first
Thread 2 finishes second
Thread 4 finishes third
...
```

**If you need order:**
- Add index to each thread
- Sort results after aggregation
- Or use channels instead of shared Vec

---

## The Real-World Version

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let urls = vec![
        "https://twitter.com/trending",
        "https://tiktok.com/discover",
        "https://reddit.com/r/all",
    ];

    let results = Arc::new(Mutex::new(Vec::new()));
    let mut handles = vec![];

    for url in urls {
        let r = Arc::clone(&results);
        let h = thread::spawn(move || {
            // In reality: HTTP request to URL
            let trends = fetch_trends(url); // Simulated

            let mut guard = r.lock().unwrap();
            guard.extend(trends);
        });
        handles.push(h);
    }

    for h in handles { h.join().unwrap(); }

    let final_trends = results.lock().unwrap();
    println!("Aggregated {} trends", final_trends.len());
}

fn fetch_trends(url: &str) -> Vec<String> {
    // Simulated API call
    vec![format!("trend_from_{}", url)]
}
```

**Use cases:**
- Scraping multiple websites
- Parallel API calls
- Batch processing
- Real-time aggregation

---

## Common Mistakes (And How to Fix Them)

### Mistake 1: Forgetting Arc

```rust
// ❌ Won't compile
let shared = Mutex::new(Vec::new());
thread::spawn(move || {
    shared.lock(); // ERROR: Mutex not thread-safe without Arc
});
```

**Fix:**
```rust
// ✅ Compiles
let shared = Arc::new(Mutex::new(Vec::new()));
let s = Arc::clone(&shared);
thread::spawn(move || {
    s.lock(); // OK
});
```

---

### Mistake 2: Deadlock

```rust
// ❌ Deadlock risk
let guard1 = mutex1.lock().unwrap();
let guard2 = mutex2.lock().unwrap(); // Thread 2 does opposite order
```

**Fix:** Always acquire locks in same order across all threads.

---

### Mistake 3: Holding Lock Too Long

```rust
// ❌ Bad: Holds lock during sleep
let mut guard = mutex.lock().unwrap();
thread::sleep(Duration::from_secs(10)); // Other threads wait!
guard.push(data);
```

**Fix:**
```rust
// ✅ Good: Release lock early
{
    let mut guard = mutex.lock().unwrap();
    guard.push(data);
} // guard drops here, lock released

thread::sleep(Duration::from_secs(10)); // Lock not held
```

---

## Alternative: Channels (Message Passing)

Rust also has channels (like Go):

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    for trend in vec!["trend1", "trend2", "trend3"] {
        let tx_clone = tx.clone();
        thread::spawn(move || {
            tx_clone.send(format!("VIRAL_{}", trend)).unwrap();
        });
    }

    drop(tx); // Close sender so receiver stops waiting

    for received in rx {
        println!("{}", received);
    }
}
```

**Channels vs Shared State:**
- Channels: "Don't communicate by sharing memory; share memory by communicating"
- Shared state: Traditional locking approach
- Both valid, choose based on use case

---

## Performance Notes

**Arc overhead:**
- Clone: ~atomic increment (fast)
- Drop: ~atomic decrement (fast)
- Negligible compared to actual work

**Mutex overhead:**
- Lock: ~atomic compare-and-swap (fast if uncontended)
- Unlock: ~atomic store (fast)
- Contention: Threads wait (unavoidable)

**Thread overhead:**
- Spawn: ~microseconds per thread
- Context switch: ~microseconds
- Worth it if thread does >1ms of work

**This example:**
- 7 threads doing trivial work → overhead > benefit
- Real scraping: 7 threads fetching URLs → huge benefit

---

## The Electrician's Take

This code is like parallel conduit runs.

**Sequential (one electrician):**
- Run conduit 1 → 30 minutes
- Run conduit 2 → 30 minutes
- Run conduit 3 → 30 minutes
- Total: 90 minutes

**Concurrent (three electricians):**
- All run simultaneously → 30 minutes total
- Coordination needed (Arc/Mutex)
- Slightly slower than solo (lock contention)
- But 3x faster overall

**Same principle. Different domain.**

---

## Try It Yourself

**Challenge 1: Add Thread IDs**
Print which thread processed each trend.

**Challenge 2: Sort Results**
Maintain original order despite concurrency.

**Challenge 3: Error Handling**
What if a thread panics? Handle gracefully.

**Challenge 4: Real HTTP**
Use `reqwest` crate to fetch actual URLs.

**Challenge 5: Channel Version**
Rewrite using channels instead of shared Vec.

---

> **ANALYZE IT. THEN BUILD YOUR OWN.**

Build a concurrent scraper that fetches:
- Twitter trending topics
- Reddit front page
- Hacker News top stories

Aggregate into one list. No data races. No panics.

That's how you learn Rust concurrency. Not by reading the book.

---

**TAGS:** #Rust #Concurrency #ArcMutex #Threads #ZeroDataRaces
**DIFFICULTY:** Advanced
**TIME TO MASTER:** 1 week of parallel projects
**SIGMA RATING:** █████████░ 90% (essential for systems programming)

---

*"Concurrency is not parallelism. But both are sigma."*

**— Rob Pike, probably**
