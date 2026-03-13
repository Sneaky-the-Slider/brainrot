const TOTAL_PROMPTS = 20;
const params = new URLSearchParams(window.location.search);
const DEADPAN_PATH = "deadpan-brainrot-testing/deadpan-brainrot.json";
const CATALOG_PATH = "data_catalogs_2026.json";
const TRENDJACKER_PATH = "trendjacker_feed.json";
const ASMR_PATH = "channels/asmr/trigger_library.json";
const requested = Number(params.get("n"));
let currentIndex = Number.isFinite(requested) && requested >= 1 && requested <= TOTAL_PROMPTS
  ? requested
  : 1;
let deadpanEntries = [];
let deadpanIndex = 0;
let asmrTriggers = [];
let asmrCurrentTrigger = null;
let asmrAudioContext = null;
let asmrOscillator = null;
let asmrGainNode = null;
let asmrIsPlaying = false;

const elements = {
  counter: document.getElementById("counter"),
  status: document.getElementById("status"),
  sourcePrompt: document.getElementById("sourcePrompt"),
  auraPoints: document.getElementById("auraPoints"),
  fanumTax: document.getElementById("fanumTax"),
  mewingStreak: document.getElementById("mewingStreak"),
  ohio: document.getElementById("ohio"),
  skibidi: document.getElementById("skibidi"),
  grimace: document.getElementById("grimace"),
  rizz: document.getElementById("rizz"),
  tags: document.getElementById("tags"),
  rawJson: document.getElementById("rawJson"),
  toggleRaw: document.getElementById("toggleRaw"),
  prevBtn: document.getElementById("prevBtn"),
  nextBtn: document.getElementById("nextBtn"),
  randomBtn: document.getElementById("randomBtn"),
  deadpanId: document.getElementById("deadpanId"),
  deadpanStatus: document.getElementById("deadpanStatus"),
  deadpanText: document.getElementById("deadpanText"),
  deadpanPrev: document.getElementById("deadpanPrev"),
  deadpanNext: document.getElementById("deadpanNext"),
  deadpanRandom: document.getElementById("deadpanRandom"),
  catalogTitle: document.getElementById("catalogTitle"),
  catalogSubtitle: document.getElementById("catalogSubtitle"),
  catalogSummary: document.getElementById("catalogSummary"),
  catalogCapabilities: document.getElementById("catalogCapabilities"),
  catalogTrends: document.getElementById("catalogTrends"),
  catalogTools: document.getElementById("catalogTools"),
  catalogRecommendations: document.getElementById("catalogRecommendations"),
  historyTitle: document.getElementById("historyTitle"),
  historySubtitle: document.getElementById("historySubtitle"),
  historySummary: document.getElementById("historySummary"),
  historyDisclaimer: document.getElementById("historyDisclaimer"),
  historyTimeline: document.getElementById("historyTimeline"),
  historyNotes: document.getElementById("historyNotes"),
  historyGlossary: document.getElementById("historyGlossary"),
  trendjackerTitle: document.getElementById("trendjackerTitle"),
  trendjackerMeta: document.getElementById("trendjackerMeta"),
  trendjackerQuote: document.getElementById("trendjackerQuote"),
  trendjackerGrid: document.getElementById("trendjackerGrid"),
  trendjackerRefresh: document.getElementById("trendjackerRefresh"),
  asmrTitle: document.getElementById("asmrTitle"),
  asmrStatus: document.getElementById("asmrStatus"),
  asmrEmoji: document.getElementById("asmrEmoji"),
  asmrTriggerName: document.getElementById("asmrTriggerName"),
  asmrTriggerEffect: document.getElementById("asmrTriggerEffect"),
  asmrSlider: document.getElementById("asmrSlider"),
  asmrSliderValue: document.getElementById("asmrSliderValue"),
  asmrPlay: document.getElementById("asmrPlay"),
  asmrStop: document.getElementById("asmrStop"),
  asmrRandom: document.getElementById("asmrRandom"),
  asmrGrid: document.getElementById("asmrGrid"),
};

function updateCounter() {
  elements.counter.textContent = `${currentIndex} / ${TOTAL_PROMPTS}`;
}

function formatBoolean(value) {
  return value ? "TRUE" : "FALSE";
}

function setTags(tags) {
  elements.tags.innerHTML = "";
  if (!Array.isArray(tags) || tags.length === 0) {
    const tag = document.createElement("span");
    tag.className = "tag";
    tag.textContent = "No tags";
    elements.tags.appendChild(tag);
    return;
  }

  tags.forEach((item) => {
    const tag = document.createElement("span");
    tag.className = "tag";
    tag.textContent = item;
    elements.tags.appendChild(tag);
  });
}

function setHistoryNotes(notes) {
  elements.historyNotes.innerHTML = "";
  if (!Array.isArray(notes) || notes.length === 0) {
    return;
  }

  notes.forEach((note) => {
    const tag = document.createElement("span");
    tag.className = "tag";
    tag.textContent = note;
    elements.historyNotes.appendChild(tag);
  });
}

function setHistoryTimeline(items) {
  elements.historyTimeline.innerHTML = "";
  if (!Array.isArray(items) || items.length === 0) {
    return;
  }

  items.forEach((item) => {
    const row = document.createElement("div");
    row.className = "timeline-item";

    const year = document.createElement("div");
    year.className = "timeline-year";
    year.textContent = item.year ?? "--";

    const body = document.createElement("div");

    const label = document.createElement("div");
    label.className = "timeline-label";
    label.textContent = item.label ?? "--";

    const summary = document.createElement("div");
    summary.className = "timeline-summary";
    summary.textContent = item.summary ?? "--";

    body.appendChild(label);
    body.appendChild(summary);
    row.appendChild(year);
    row.appendChild(body);
    elements.historyTimeline.appendChild(row);
  });
}

function setHistoryGlossary(items) {
  elements.historyGlossary.innerHTML = "";
  if (!Array.isArray(items) || items.length === 0) {
    return;
  }

  const wrapper = document.createElement("div");
  wrapper.className = "glossary";

  items.forEach((item) => {
    const entry = document.createElement("div");
    entry.className = "glossary-item";

    const term = document.createElement("div");
    term.className = "glossary-term";
    term.textContent = item.term ?? "--";

    const def = document.createElement("div");
    def.textContent = item.definition ?? "--";

    entry.appendChild(term);
    entry.appendChild(def);
    wrapper.appendChild(entry);
  });

  elements.historyGlossary.appendChild(wrapper);
}

function setCatalogList(container, items) {
  container.innerHTML = "";
  if (!Array.isArray(items) || items.length === 0) {
    return;
  }

  items.forEach((item) => {
    const tag = document.createElement("span");
    tag.className = "tag";
    tag.textContent = item;
    container.appendChild(tag);
  });
}

function setCatalogTools(items) {
  elements.catalogTools.innerHTML = "";
  if (!Array.isArray(items) || items.length === 0) {
    return;
  }

  items.forEach((item) => {
    const card = document.createElement("div");
    card.className = "catalog-tool";

    const title = document.createElement("div");
    title.className = "catalog-tool-title";
    title.textContent = item.tool ?? "--";

    const meta = document.createElement("div");
    meta.className = "catalog-tool-meta";
    meta.textContent = [
      item.best_for ? `Best for: ${item.best_for}` : null,
      item.strengths ? `Strengths: ${item.strengths}` : null,
      item.deployment ? `Deployment: ${item.deployment}` : null,
      item.pricing ? `Pricing: ${item.pricing}` : null,
      item.rating ? `Rating: ${item.rating}` : null,
      item.drawbacks ? `Drawbacks: ${item.drawbacks}` : null,
    ].filter(Boolean).join(" | ");

    card.appendChild(title);
    card.appendChild(meta);
    elements.catalogTools.appendChild(card);
  });
}

function setCatalogLoading(message) {
  elements.catalogTitle.textContent = message;
  elements.catalogSubtitle.textContent = "";
  elements.catalogSummary.textContent = "";
  elements.catalogCapabilities.innerHTML = "";
  elements.catalogTrends.innerHTML = "";
  elements.catalogTools.innerHTML = "";
  elements.catalogRecommendations.innerHTML = "";
}

function setLoading(message) {
  elements.sourcePrompt.textContent = message;
  elements.status.textContent = "Status: --";
  elements.auraPoints.textContent = "--";
  elements.fanumTax.textContent = "--";
  elements.mewingStreak.textContent = "--";
  elements.ohio.textContent = "--";
  elements.skibidi.textContent = "--";
  elements.grimace.textContent = "--";
  elements.rizz.textContent = "--";
  setTags([]);
}

function setDeadpanLoading(message) {
  elements.deadpanId.textContent = "#--";
  elements.deadpanStatus.textContent = "Schema: --";
  elements.deadpanText.textContent = message;
}

function validateDeadpanEntry(entry) {
  return (
    entry &&
    Number.isInteger(entry.id) &&
    typeof entry.deadpan_brainrot === "string"
  );
}

function validateDeadpanCollection(data) {
  return Array.isArray(data) && data.every(validateDeadpanEntry);
}

function renderDeadpan() {
  if (!deadpanEntries.length) {
    setDeadpanLoading("No entries loaded.");
    return;
  }

  const entry = deadpanEntries[deadpanIndex];
  elements.deadpanId.textContent = `#${entry.id}`;
  elements.deadpanText.textContent = entry.deadpan_brainrot;
}

async function loadDeadpan() {
  setDeadpanLoading("Loading entries...");
  try {
    const response = await fetch(DEADPAN_PATH, { cache: "no-store" });
    if (!response.ok) {
      throw new Error("Deadpan collection not found");
    }
    const data = await response.json();
    const valid = validateDeadpanCollection(data);

    elements.deadpanStatus.textContent = valid ? "Schema: OK" : "Schema: INVALID";
    deadpanEntries = Array.isArray(data) ? data : [];
    deadpanIndex = 0;
    renderDeadpan();
  } catch (error) {
    setDeadpanLoading("Deadpan collection unavailable.");
    elements.deadpanStatus.textContent = "Schema: --";
  }
}

function clampDeadpanIndex(value) {
  if (!deadpanEntries.length) return 0;
  if (value < 0) return deadpanEntries.length - 1;
  if (value >= deadpanEntries.length) return 0;
  return value;
}

function setHistoryLoading(message) {
  elements.historyTitle.textContent = message;
  elements.historySubtitle.textContent = "";
  elements.historySummary.textContent = "";
  elements.historyDisclaimer.textContent = "";
  elements.historyTimeline.innerHTML = "";
  elements.historyNotes.innerHTML = "";
  elements.historyGlossary.innerHTML = "";
}

function updateUrl() {
  const url = new URL(window.location.href);
  url.searchParams.set("n", String(currentIndex));
  window.history.replaceState({}, "", url);
}

async function loadPrompt(index) {
  setLoading("Loading prompt...");
  updateCounter();

  try {
    const response = await fetch(`prompt_${index}.json`, { cache: "no-store" });
    if (!response.ok) {
      throw new Error("Prompt not found");
    }
    const data = await response.json();

    elements.status.textContent = `Status: ${data.status ?? "--"}`;
    elements.auraPoints.textContent = data.aura_points ?? "--";
    elements.fanumTax.textContent = data.fanum_tax_rate ?? "--";
    elements.mewingStreak.textContent = data.mewing_streak ?? "--";
    elements.ohio.textContent = data.brainrot_payload?.ohio_compatibility ?? "--";
    elements.skibidi.textContent = formatBoolean(Boolean(data.is_skibidi));
    elements.grimace.textContent = data.grimace_shake_status ?? "--";
    elements.rizz.textContent = data.brainrot_payload?.rizz_analysis ?? "--";
    elements.sourcePrompt.textContent = data.brainrot_payload?.source_prompt ?? "--";
    setTags(data.tags);

    elements.rawJson.textContent = JSON.stringify(data, null, 2);
    updateUrl();
  } catch (error) {
    setLoading("Prompt failed to load. Check that prompt files are present.");
    elements.status.textContent = "Status: ERROR";
  }
}

async function loadHistory() {
  setHistoryLoading("Loading history...");
  try {
    const response = await fetch("history_phreaking.json", { cache: "no-store" });
    if (!response.ok) {
      throw new Error("History not found");
    }
    const data = await response.json();

    elements.historyTitle.textContent = data.title ?? "History Archive";
    elements.historySubtitle.textContent = data.subtitle ?? "";
    elements.historySummary.textContent = data.summary ?? "";
    elements.historyDisclaimer.textContent = data.disclaimer ?? "";
    setHistoryTimeline(data.timeline);
    setHistoryNotes(data.ethics_notes);
    setHistoryGlossary(data.glossary);
  } catch (error) {
    setHistoryLoading("History archive unavailable.");
  }
}

async function loadCatalogs() {
  setCatalogLoading("Loading catalog overview...");
  try {
    const response = await fetch(CATALOG_PATH, { cache: "no-store" });
    if (!response.ok) {
      throw new Error("Catalog overview not found");
    }
    const data = await response.json();

    elements.catalogTitle.textContent = data.title ?? "Data Catalogs";
    elements.catalogSubtitle.textContent = data.subtitle ?? "";
    elements.catalogSummary.textContent = data.summary ?? "";
    setCatalogList(elements.catalogCapabilities, data.capabilities);
    setCatalogList(elements.catalogTrends, data.market_trends_2026);
    setCatalogTools(data.tools);
    setCatalogList(elements.catalogRecommendations, data.recommendations);
  } catch (error) {
    setCatalogLoading("Catalog overview unavailable.");
  }
}

function setTrendjackerLoading(message) {
  elements.trendjackerTitle.textContent = message;
  elements.trendjackerMeta.textContent = "--";
  elements.trendjackerQuote.innerHTML = "";
  elements.trendjackerGrid.innerHTML = "";
}

function formatTimestamp(timestamp) {
  const date = new Date(timestamp * 1000);
  const now = new Date();
  const diffMs = now - date;
  const diffHours = Math.floor(diffMs / (1000 * 60 * 60));

  if (diffHours < 1) return "Just now";
  if (diffHours < 24) return `${diffHours}h ago`;
  const diffDays = Math.floor(diffHours / 24);
  return `${diffDays}d ago`;
}

function initAudioContext() {
  if (!asmrAudioContext) {
    asmrAudioContext = new (window.AudioContext || window.webkitAudioContext)();
  }
}

function setASMRLoading(message) {
  elements.asmrTriggerName.textContent = message;
  elements.asmrTriggerEffect.textContent = "Loading...";
  elements.asmrGrid.innerHTML = "";
}

function updateBrainrotSlider() {
  const value = elements.asmrSlider.value / 100;
  elements.asmrSliderValue.textContent = value.toFixed(2);

  // Update current trigger effect based on slider
  if (asmrCurrentTrigger) {
    const baseEffect = asmrCurrentTrigger.effect;
    let modifier = "";

    if (value < 0.3) {
      modifier = " (Calm mode)";
    } else if (value < 0.7) {
      modifier = " (Balanced)";
    } else {
      modifier = " (Maximum confusion)";
    }

    elements.asmrTriggerEffect.textContent = baseEffect + modifier;
  }
}

function selectTrigger(trigger) {
  asmrCurrentTrigger = trigger;

  // Update UI
  elements.asmrEmoji.textContent = trigger.emoji;
  elements.asmrTriggerName.textContent = `${trigger.type}: ${trigger.object}`;
  elements.asmrTriggerEffect.textContent = trigger.effect;

  // Update active state
  document.querySelectorAll('.asmr-trigger-card').forEach(card => {
    card.classList.remove('active');
  });
  document.querySelector(`[data-trigger-id="${trigger.id}"]`)?.classList.add('active');

  updateBrainrotSlider();
}

function playASMR() {
  if (!asmrCurrentTrigger) {
    elements.asmrStatus.textContent = "Select a trigger first";
    return;
  }

  initAudioContext();
  stopASMR(); // Stop any existing audio

  // Create oscillator with trigger's frequency
  asmrOscillator = asmrAudioContext.createOscillator();
  asmrGainNode = asmrAudioContext.createGain();

  // Base frequency from trigger
  const baseFreq = parseFloat(asmrCurrentTrigger.frequency);

  // Adjust frequency based on brainrot slider
  const brainrotCoeff = elements.asmrSlider.value / 100;
  const frequency = baseFreq * (1 + (brainrotCoeff * 0.5)); // Higher brainrot = higher pitch

  asmrOscillator.type = brainrotCoeff > 0.7 ? 'sawtooth' : 'sine'; // Harsher sound at high brainrot
  asmrOscillator.frequency.setValueAtTime(frequency, asmrAudioContext.currentTime);

  // Volume control (quieter = more ASMR-like)
  const volume = 0.05 + (brainrotCoeff * 0.05); // Very quiet
  asmrGainNode.gain.setValueAtTime(volume, asmrAudioContext.currentTime);

  // Connect nodes
  asmrOscillator.connect(asmrGainNode);
  asmrGainNode.connect(asmrAudioContext.destination);

  // Start playing
  asmrOscillator.start();
  asmrIsPlaying = true;

  // Update UI
  elements.asmrStatus.textContent = "Playing";
  elements.asmrStatus.classList.add('playing');
  elements.asmrPlay.textContent = "⏸ Pause";

  // Auto-stop after duration
  setTimeout(() => {
    if (asmrIsPlaying) {
      stopASMR();
    }
  }, asmrCurrentTrigger.duration_seconds * 1000);
}

function stopASMR() {
  if (asmrOscillator) {
    asmrOscillator.stop();
    asmrOscillator.disconnect();
    asmrOscillator = null;
  }

  if (asmrGainNode) {
    asmrGainNode.disconnect();
    asmrGainNode = null;
  }

  asmrIsPlaying = false;

  // Update UI
  elements.asmrStatus.textContent = "Ready";
  elements.asmrStatus.classList.remove('playing');
  elements.asmrPlay.textContent = "▶ Play";
}

function randomTrigger() {
  if (!asmrTriggers.length) return;
  const random = asmrTriggers[Math.floor(Math.random() * asmrTriggers.length)];
  selectTrigger(random);
}

async function loadASMR() {
  setASMRLoading("Loading ASMR triggers...");

  try {
    const response = await fetch(ASMR_PATH, { cache: "no-store" });
    if (!response.ok) {
      throw new Error("ASMR library not found");
    }

    const data = await response.json();
    asmrTriggers = data.triggers || [];

    if (!asmrTriggers.length) {
      elements.asmrTriggerName.textContent = "No triggers available";
      return;
    }

    // Populate trigger grid
    elements.asmrGrid.innerHTML = "";

    asmrTriggers.forEach(trigger => {
      const card = document.createElement("div");
      card.className = "asmr-trigger-card";
      card.dataset.triggerId = trigger.id;
      card.onclick = () => selectTrigger(trigger);

      const header = document.createElement("div");
      header.className = "asmr-trigger-header";

      const emoji = document.createElement("div");
      emoji.className = "asmr-trigger-emoji";
      emoji.textContent = trigger.emoji;

      const title = document.createElement("div");
      title.className = "asmr-trigger-title";
      title.textContent = trigger.type;

      const category = document.createElement("div");
      category.className = `asmr-trigger-category ${trigger.category}`;
      category.textContent = trigger.category;

      header.appendChild(emoji);
      header.appendChild(title);
      header.appendChild(category);

      const meta = document.createElement("div");
      meta.className = "asmr-trigger-meta";
      meta.innerHTML = `
        <span>${trigger.frequency}</span>
        <span>${trigger.duration_seconds}s</span>
      `;

      const effect = document.createElement("div");
      effect.className = "asmr-trigger-effect-text";
      effect.textContent = trigger.effect;

      const brainrot = document.createElement("div");
      brainrot.className = "asmr-trigger-brainrot";

      const bar = document.createElement("div");
      bar.className = "asmr-brainrot-bar";

      const fill = document.createElement("div");
      fill.className = "asmr-brainrot-fill";
      fill.style.width = `${trigger.brainrot_level * 100}%`;

      bar.appendChild(fill);

      const value = document.createElement("div");
      value.className = "asmr-brainrot-value";
      value.textContent = trigger.brainrot_level.toFixed(2);

      brainrot.appendChild(bar);
      brainrot.appendChild(value);

      card.appendChild(header);
      card.appendChild(meta);
      card.appendChild(effect);
      card.appendChild(brainrot);

      elements.asmrGrid.appendChild(card);
    });

    // Select first trigger by default
    selectTrigger(asmrTriggers[0]);

  } catch (error) {
    setASMRLoading("ASMR library unavailable");
    console.error("ASMR load error:", error);
  }
}

async function loadTrendjacker() {
  setTrendjackerLoading("Loading Reddit trends...");
  try {
    const response = await fetch(TRENDJACKER_PATH, { cache: "no-store" });
    if (!response.ok) {
      throw new Error("Trendjacker feed not found");
    }
    const data = await response.json();

    // Header
    elements.trendjackerTitle.textContent = `r/${data.meta?.subreddit || "popular"} - Hot Trends`;
    const fetchTime = data.meta?.fetched_at_human || data.meta?.last_update_human || "--";
    const trendCount = data.trends?.length || 0;
    elements.trendjackerMeta.textContent = `${trendCount} trends • Updated: ${fetchTime.split('T')[0]}`;

    // Quote of the Day
    if (data.quote_of_the_day) {
      const q = data.quote_of_the_day;
      elements.trendjackerQuote.innerHTML = `
        <div class="trendjacker-quote-text">"${q.text}"</div>
        <div class="trendjacker-quote-meta">
          🔥 ${q.score?.toLocaleString() || 0} upvotes • ${q.author || "unknown"} • ${q.source || "reddit"}
        </div>
      `;
    }

    // Trends Grid (top 10)
    const topTrends = (data.trends || []).slice(0, 10);
    elements.trendjackerGrid.innerHTML = "";

    topTrends.forEach((trend) => {
      const card = document.createElement("div");
      card.className = "trend-card";
      card.onclick = () => window.open(trend.reddit_url || trend.url, "_blank");

      const header = document.createElement("div");
      header.className = "trend-header";

      const title = document.createElement("div");
      title.className = "trend-title";
      title.textContent = trend.title;

      const viral = document.createElement("div");
      viral.className = "trend-viral";
      viral.textContent = `${trend.viral_score || 0}%`;

      header.appendChild(title);
      header.appendChild(viral);

      const meta = document.createElement("div");
      meta.className = "trend-meta";
      meta.innerHTML = `
        <span>⬆️ ${trend.score?.toLocaleString() || 0}</span>
        <span>💬 ${trend.comments?.toLocaleString() || 0}</span>
        <span>r/${trend.subreddit || "unknown"}</span>
      `;

      card.appendChild(header);
      card.appendChild(meta);

      if (trend.snippet) {
        const snippet = document.createElement("div");
        snippet.className = "trend-snippet";
        snippet.textContent = trend.snippet.substring(0, 150) + (trend.snippet.length > 150 ? "..." : "");
        card.appendChild(snippet);
      }

      elements.trendjackerGrid.appendChild(card);
    });

  } catch (error) {
    setTrendjackerLoading("Trendjacker feed unavailable.");
    console.error("Trendjacker load error:", error);
  }
}

function clampIndex(value) {
  if (value < 1) return TOTAL_PROMPTS;
  if (value > TOTAL_PROMPTS) return 1;
  return value;
}

elements.prevBtn.addEventListener("click", () => {
  currentIndex = clampIndex(currentIndex - 1);
  loadPrompt(currentIndex);
});

elements.nextBtn.addEventListener("click", () => {
  currentIndex = clampIndex(currentIndex + 1);
  loadPrompt(currentIndex);
});

elements.randomBtn.addEventListener("click", () => {
  const next = Math.floor(Math.random() * TOTAL_PROMPTS) + 1;
  currentIndex = next;
  loadPrompt(currentIndex);
});

elements.toggleRaw.addEventListener("click", () => {
  const isHidden = elements.rawJson.hasAttribute("hidden");
  if (isHidden) {
    elements.rawJson.removeAttribute("hidden");
    elements.toggleRaw.textContent = "Hide JSON";
  } else {
    elements.rawJson.setAttribute("hidden", "");
    elements.toggleRaw.textContent = "Show JSON";
  }
});

elements.deadpanPrev.addEventListener("click", () => {
  deadpanIndex = clampDeadpanIndex(deadpanIndex - 1);
  renderDeadpan();
});

elements.deadpanNext.addEventListener("click", () => {
  deadpanIndex = clampDeadpanIndex(deadpanIndex + 1);
  renderDeadpan();
});

elements.deadpanRandom.addEventListener("click", () => {
  if (!deadpanEntries.length) return;
  deadpanIndex = Math.floor(Math.random() * deadpanEntries.length);
  renderDeadpan();
});

elements.trendjackerRefresh.addEventListener("click", () => {
  loadTrendjacker();
});

elements.asmrSlider.addEventListener("input", () => {
  updateBrainrotSlider();
});

elements.asmrPlay.addEventListener("click", () => {
  if (asmrIsPlaying) {
    stopASMR();
  } else {
    playASMR();
  }
});

elements.asmrStop.addEventListener("click", () => {
  stopASMR();
});

elements.asmrRandom.addEventListener("click", () => {
  randomTrigger();
});

updateCounter();
loadPrompt(currentIndex);
loadHistory();
loadDeadpan();
loadCatalogs();
loadTrendjacker();
loadASMR();
