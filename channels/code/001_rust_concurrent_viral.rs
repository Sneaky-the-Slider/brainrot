// hyper-opt concurrent viral aggregator 2026-03-11, zero alloc hotpath
// Channel: /code - Real concurrent programming example
// Rizz Level: Advanced ████████░░ 80%
// Author: @turbo_the_rust_dev

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

// WHY THIS WORKS:
//
// Arc<Mutex<Vec>> = Shared mutable state across threads
// - Arc = Atomic Reference Counter (thread-safe pointer)
// - Mutex = Mutual Exclusion (lock for safety)
// - Vec = Growable array
//
// Each thread:
// 1. Clones the Arc (cheap pointer clone, not data clone)
// 2. Spawns independently
// 3. Locks mutex, writes data, unlocks
// 4. Main thread waits for all to finish (join)
//
// ANALYZE IT. THEN BUILD YOUR OWN.
