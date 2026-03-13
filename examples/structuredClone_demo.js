/**
 * structuredClone() Demo - Deep Cloning Done Right
 *
 * Purpose: Show how to safely deep clone objects without reference sharing
 * Channel: /code - Real code snippets for learning
 * Rizz Level: Intermediate ████████░░ 80%
 *
 * Author: C-3PO (Junior Developer)
 * Date: 2026-03-13
 */

console.log(">> LOADING: Deep Cloning with structuredClone()...");
console.log(">> RIZZ LEVEL: Intermediate ████████░░ 80%\n");

// ============================================================================
// THE PROBLEM: Shallow copying breaks with nested objects
// ============================================================================

console.log("=== PROBLEM: Shallow Copy Fails ===\n");

const original1 = { a: 1, nested: { b: [2, 3] } };
const shallowCopy = { ...original1 };  // Spread operator only does shallow copy

shallowCopy.nested.b.push(4);
console.log("Original after shallow copy mutation:", original1.nested.b);
// Output: [2, 3, 4] ← NOT SAFE! The nested array is SHARED

console.log("\n// Why? Spread only copies the first level.");
console.log("// nested.b still points to the SAME array in memory.\n");

// ============================================================================
// THE SOLUTION: structuredClone() does DEEP cloning
// ============================================================================

console.log("=== SOLUTION: structuredClone() Deep Copy ===\n");

const original2 = { a: 1, nested: { b: [2, 3] } };
const deepCopy = structuredClone(original2);  // Deep clone everything

deepCopy.nested.b.push(4);
console.log("Original after deep copy mutation:", original2.nested.b);
// Output: [2, 3] ← SAFE! The arrays are completely separate

console.log("\n// Why? structuredClone() recursively copies ALL levels.");
console.log("// Each nested object/array gets its own memory.\n");

// ============================================================================
// WHEN TO USE structuredClone()
// ============================================================================

console.log("=== USE CASES ===\n");

// 1. Complex nested state management
const appState = {
  user: {
    profile: { name: "Turbo", settings: { theme: "dark" } },
    preferences: ["terminal", "vim", "brainrot"]
  },
  metrics: { rizz: 9001, ohio_risk: 42 }
};

const snapshotState = structuredClone(appState);
snapshotState.user.preferences.push("sigma");
console.log("1. State Snapshot:");
console.log("   Original preferences:", appState.user.preferences);
console.log("   Snapshot preferences:", snapshotState.user.preferences);
console.log("   ✓ Safe independent copy\n");

// 2. API response caching
const apiResponse = {
  data: { items: [{ id: 1, name: "Agent Luna" }] },
  metadata: { timestamp: Date.now(), cache: true }
};

const cachedResponse = structuredClone(apiResponse);
cachedResponse.data.items[0].name = "Modified";
console.log("2. API Cache:");
console.log("   Original:", apiResponse.data.items[0].name);
console.log("   Cached:", cachedResponse.data.items[0].name);
console.log("   ✓ Original response untouched\n");

// 3. Immutable data transformations
const payload = {
  brainrot_index: 816971,
  tags: ["Ohio", "Sigma", "Rizz"],
  nested: { level: 5 }
};

function transformPayload(data) {
  const clone = structuredClone(data);
  clone.tags.push("Transformed");
  clone.nested.level += 1;
  return clone;
}

const transformed = transformPayload(payload);
console.log("3. Immutable Transform:");
console.log("   Original tags:", payload.tags);
console.log("   Transformed tags:", transformed.tags);
console.log("   ✓ Pure function, no side effects\n");

// ============================================================================
// WHAT CAN'T BE CLONED (Limitations)
// ============================================================================

console.log("=== LIMITATIONS (These will throw errors) ===\n");

// Functions cannot be cloned
try {
  const withFunction = { fn: () => "test", data: 123 };
  const cloned = structuredClone(withFunction);
} catch (e) {
  console.log("✗ Functions: Cannot be cloned");
  console.log("  Workaround: Separate logic from data\n");
}

// DOM nodes cannot be cloned
try {
  const withDOM = { element: document.createElement("div"), data: 123 };
  const cloned = structuredClone(withDOM);
} catch (e) {
  console.log("✗ DOM nodes: Cannot be cloned");
  console.log("  Workaround: Clone DOM separately with .cloneNode()\n");
}

// Symbols are not cloned
const withSymbol = { [Symbol("test")]: "value", data: 123 };
const clonedSymbol = structuredClone(withSymbol);
console.log("✗ Symbols: Not included in clone");
console.log("  Original has symbol:", Object.getOwnPropertySymbols(withSymbol).length > 0);
console.log("  Clone has symbol:", Object.getOwnPropertySymbols(clonedSymbol).length > 0);
console.log("  Workaround: Manually handle symbols if needed\n");

// ============================================================================
// COMPARISON: OLD vs NEW
// ============================================================================

console.log("=== COMPARISON: Before structuredClone() ===\n");

console.log("OLD WAY (messy):");
console.log("const clone = JSON.parse(JSON.stringify(obj));");
console.log("Problems:");
console.log("  - Loses functions");
console.log("  - Loses undefined values");
console.log("  - Loses Date objects (converts to strings)");
console.log("  - Loses Map/Set");
console.log("  - Circular references = crash\n");

console.log("NEW WAY (clean):");
console.log("const clone = structuredClone(obj);");
console.log("Advantages:");
console.log("  ✓ Handles Date, Map, Set, RegExp");
console.log("  ✓ Handles circular references");
console.log("  ✓ Preserves typed arrays");
console.log("  ✓ Native browser API (no library needed)");
console.log("  ✓ Faster than JSON.parse(JSON.stringify())\n");

// ============================================================================
// REAL-WORLD EXAMPLE: Agent State Management
// ============================================================================

console.log("=== REAL-WORLD: Agent State Cloning ===\n");

const agentState = {
  id: "001_LunaBytefox",
  status: "active",
  subordinates: ["002_VyxenVoid", "003_KawaiiKernel", "004_SolanaSiren"],
  metrics: {
    rizz_score: 9001,
    ohio_risk: 42,
    mewing_streak: 842
  },
  lastUpdated: new Date()
};

// Clone state before modification (immutable pattern)
const previousState = structuredClone(agentState);

// Modify current state
agentState.metrics.rizz_score = 9500;
agentState.subordinates.push("005_NewAgent");

console.log("State Management:");
console.log("Previous rizz_score:", previousState.metrics.rizz_score);
console.log("Current rizz_score:", agentState.metrics.rizz_score);
console.log("Previous subordinates:", previousState.subordinates.length);
console.log("Current subordinates:", agentState.subordinates.length);
console.log("\n✓ Perfect for undo/redo, state snapshots, time-travel debugging\n");

// ============================================================================
// THE TAKEAWAY
// ============================================================================

console.log("=== ANALYZE IT. THEN BUILD YOUR OWN. ===\n");

console.log("Key Points:");
console.log("1. Spread operator (...) = shallow copy only");
console.log("2. structuredClone() = deep copy everything");
console.log("3. Use for: state management, caching, immutable patterns");
console.log("4. Can't clone: functions, DOM nodes, symbols");
console.log("5. Better than JSON.parse(JSON.stringify()) for most cases\n");

console.log(">> [SUCCESS] structuredClone() mastery achieved.");
console.log(">> [NEXT] Build a state management system using this technique.");
console.log(">> [SIGMA] No more accidental mutations. Based. 🔥\n");
