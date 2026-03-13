# 🔥 BRAINROT VAULTS - Infinite AI Prompt Generators

**Single-file viral prompt machines. Zero dependencies. Infinite variations.**

---

## What Are Vaults?

Vaults are **single HTML file applications** that generate endless variations of AI image prompts for platforms like:
- Midjourney
- DALL-E
- Stable Diffusion
- Flux
- Any text-to-image generator

Each vault targets a specific theme (sigma, dogs, cats, dinos) with:
- **Base templates** (6 per vault, hand-crafted)
- **Random generation** (click button → infinite new prompts)
- **One-click copy** (clipboard integration)
- **Confetti explosions** (because why not)
- **Neon aesthetics** (2026 brainrot energy)

---

## Available Vaults

### 🧿 [Sigma Vault](sigma_vault.html)
**Theme:** Viral TikTok sigma energy, aura-maxxing, mogging challenges
**Color:** Cyan/Emerald
**Prompt Focus:** Safe poses, baggy hoodies, Italian brainrot vibes

### 🐾 [Dog Vault](dog_vault.html)
**Theme:** Viral TikTok puppy content, zoomies, bark challenges
**Color:** Orange/Yellow
**Prompt Focus:** Cute-safe doggos, bandanas, wholesome energy

### 🐱 [Cat Vault](cat_vault.html)
**Theme:** Viral TikTok cat content, meow-sync, loaf mode
**Color:** Purple/Pink
**Prompt Focus:** Cute-safe cats, purr vibes, feline energy

### 🦖 [Dino Vault](dino_vault.html)
**Theme:** Viral TikTok prehistoric content, roar challenges, stomp energy
**Color:** Lime/Emerald
**Prompt Focus:** Roar-safe dinos, cyber aesthetic, fossil rizz

### 🏠 [Vault Hub](index.html)
Central navigation page with stats, tech specs, and vault grid.

---

## Technical Architecture

```
Each Vault = ONE HTML file containing:
├── HTML structure
├── Tailwind CSS (via CDN)
├── Vanilla JavaScript
└── Zero build process
```

**Dependencies:** NONE (Tailwind CDN doesn't count)
**Build Tools:** NONE (just open the file)
**Framework:** WHO NEEDS ONE

---

## How It Works

### 1. Base Templates
Each vault starts with 6 hand-crafted prompt templates:
```javascript
{
  name: "cyberrizz.xo",
  desc: "Neon sigma dancer...",
  prompt: "Ultra-detailed 8k render of..."
}
```

### 2. Random Generation
Click "GO VIRAL" button → generates new variation:
```javascript
function viralize() {
  const templates = ["sigma king", "rizz lord", ...];
  const name = "sigma_" + random() + ".xo";
  const prompt = "8k viral TikTok AI " + random_template + "...";
  // Creates new card
}
```

### 3. Confetti Animation
30 emoji particles fly across screen on each generation:
```javascript
for(let i=0;i<30;i++){
  // Create emoji element
  // Animate across screen
  // Remove after 1.5s
}
```

### 4. Clipboard Copy
One-click copy with toast notification:
```javascript
function copyPrompt(p) {
  navigator.clipboard.writeText(p);
  // Show toast: "PROMPT COPIED"
}
```

---

## Creating New Vaults

Want to add a new theme? Here's the template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<title>BRAINROT [THEME] VAULT 2026</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>
/* Update colors for theme */
body { background: linear-gradient(180deg, #0a0a0a, #YOUR_COLOR); }
.neon { text-shadow: 0 0 20px #YOUR_COLOR; }
</style>
</head>
<body class="min-h-screen text-white font-mono">

<header>
  <h1>BRAINROT<br>[THEME] VAULT</h1>
  <button onclick="viralize()">GO VIRAL 🔥 [EMOJI]</button>
</header>

<div id="feed" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"></div>

<script>
const baseItems = [
  {name:"...", desc:"...", prompt:"..."},
  // Add 6 base templates
];

function createCard(b) { /* Card HTML */ }
function renderFeed() { /* Render all cards */ }
function viralize() { /* Generate new variation */ }
function copyPrompt(p) { /* Clipboard copy */ }

renderFeed();
</script>
</body>
</html>
```

**Steps:**
1. Copy any existing vault HTML
2. Change colors (background gradient, neon glow, borders)
3. Change emoji (🦊, 🐉, 🚀, etc.)
4. Write 6 base templates
5. Update generation templates
6. Test in browser
7. Add to `index.html` vault grid

---

## Design Principles

### 1. Single-File Philosophy
No build tools. No npm. No webpack. Just HTML.

**Why?**
- Works anywhere (phone, tablet, laptop)
- No "npm install" dependency hell
- Share via single file
- Open and go viral

### 2. Zero-Dep Architecture
Only external resource: Tailwind CDN

**Why?**
- Tailwind provides all styling needs
- CDN = fast load, no local storage
- No framework lock-in
- Vanilla JS = maximum compatibility

### 3. Infinite Generation
Templates + randomization = unlimited variations

**Why?**
- Never run out of prompt ideas
- Each generation feels fresh
- Encourages experimentation
- High replay value

### 4. Playful UX
Confetti, neon, animations, hover effects

**Why?**
- Brainrot aesthetic = essential
- Gamifies prompt generation
- Encourages sharing ("check this out!")
- Makes boring task fun

---

## Use Cases

**For Creators:**
- Generate hundreds of prompts in minutes
- Test variations before committing tokens
- Find the perfect prompt formula
- Build prompt libraries

**For Learners:**
- Study effective prompt patterns
- Understand prompt engineering
- See what makes prompts "viral"
- Learn by example

**For Teams:**
- Rapid prototyping visual concepts
- Brainstorm campaigns
- Generate mockups
- Share prompt libraries

---

## Stats

```
Vaults Created:       5
Total Lines:         673
File Size (avg):    ~5.5KB
Dependencies:         0
Build Time:          0ms
Load Time:         <100ms
Prompts Generated:    ∞
Rizz Level:          MAX
```

---

## Future Vaults (Ideas)

- 🎨 Art Vault - Painting styles, art movements
- 🚗 Car Vault - Vehicle designs, automotive aesthetics
- 🌆 City Vault - Urban landscapes, architecture
- 🎮 Game Vault - Video game character concepts
- 🍔 Food Vault - Culinary photography prompts
- 🎭 Theater Vault - Dramatic scenes, stage concepts
- 🏔️ Nature Vault - Landscapes, environmental art
- 🤖 Robot Vault - Mech designs, AI aesthetics

---

## Contributing

Want to add a vault? Follow these rules:

**Do:**
- Keep it single-file
- Use Tailwind CDN
- Write 6+ base templates
- Add theme-appropriate confetti emojis
- Test on mobile
- Match existing UX patterns

**Don't:**
- Add npm dependencies
- Require build process
- Use frameworks (React, Vue, etc.)
- Generate unsafe/NSFW prompts
- Overcomplicate the code

---

## Technical Notes

### Clipboard API
```javascript
navigator.clipboard.writeText(text);
```
**Requires:** HTTPS or localhost (browser security)

### Animation Performance
Confetti uses `position: fixed` + `transform` (GPU accelerated)
- 30 particles per generation
- 1.2s animation duration
- Auto-cleanup after completion

### Responsive Design
Tailwind classes handle all breakpoints:
- Mobile: 1 column
- Tablet: 2 columns
- Desktop: 3 columns

### Browser Support
Works in all modern browsers (Chrome, Firefox, Safari, Edge)
- CSS Grid
- ES6 JavaScript
- Template literals
- Arrow functions

---

*"The impedance of excuses is infinite. Current flows through action."*

**— TURBO** ⚡

Generate. Copy. Create. Repeat.
