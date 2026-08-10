# Walkthrough — The Player Experience

This traces what the player actually sees, does, and feels across the **three zones** (Main → Storage → Office) and the **containers** inside them. Vocabulary: [`zones-and-containers.md`](./zones-and-containers.md). It does **not** define puzzle mechanics — those come later in [`../04-Puzzles/`](../04-Puzzles/). Where a "how do they get access" moment happens, it's marked as `[ACCESS TBD]`.

**Confirmed access order:**
- **Zones:** Main (start) → **Storage** → **Office**
- **Major container (last):** Car trunk → Sparky → Mascot Mount → Finale

Access is gated, not branching. Tools Closet is treated as a **container** (not a 4th zone); sequencing still open. Other containers (lockers, cabinets, drawers, filing cabinet, Tony's Locker, etc.) are additional gates/clue holders — see the living list in [`zones-and-containers.md`](./zones-and-containers.md).

---

## Phase 0 — Entrance & Arrival

Players enter Tony's Garage for the first time as the new owner. First impressions matter: this should feel like a real, lived-in auto shop that's mid-breath — like Tony stepped out five minutes ago — not spooky, just unfamiliar and a little heavy (they're here because their uncle died).

- **Before the door**: a small "CLOSED — Family Emergency" sign still hanging — easy to miss, plants "something recent happened here" before players see anything else.
- **Crossing the threshold**: dim, half-on shop lighting (not "closed for the night," more "nobody's opened up properly today"); quiet ambient sound (dripping pipe, distant radio static).
- **First impressions of the Main Bay**: a workbench with personal touches (Tony's coffee mug, a wall calendar flipped to a specific date — implicitly the day he died, never explicitly pointed out), the parked car with its trunk visibly chained/padlocked sitting center-stage, the "Tony's Garage" sign overhead unlit/dim (its big lit moment is reserved for the finale), the **Mascot Mount** empty but with a small nameplate already reading "Sparky" (players feel his absence specifically, not just "empty pedestal"), and the fake upstairs window with blinds shut, a shadow occasionally drifting behind it.
- **Emotional arc for this first minute**: grief/solemnity → unfamiliarity → unease. Frank's gruffness lands as contrast after Marion Cole.
- **Game start device:** a shop **phone with answering machine** sits in Main; **message light blinking**. Players press **Play** to hear Marion Cole and begin the intro sequence. Build: [`../05-Software-Electronics/props/answering-machine-phone/README.md`](../05-Software-Electronics/props/answering-machine-phone/README.md).

## Phase 1 — Frank's Greeting & the Job Begins (Main Garage Bay)

- Marion Cole's message ends → **wall intercom** clicks/crackles — **Frank** addresses the room. He's been listening and is annoyed by the lawyer's sentimentality ("always with the speeches"). Full line in [`../01-Story/in-room-text.md`](../01-Story/in-room-text.md). Build: [`../05-Software-Electronics/props/wall-intercom/README.md`](../05-Software-Electronics/props/wall-intercom/README.md).
- **Staging:** Frank's *voice* = wall intercom; Frank's *presence* = upstairs window (shadow/eyes). Same character, two props — don't put his dialogue on a CRT for the opening unless we add video later as an upgrade.
- He's gruff, clearly unhappy about the succession, but sends the player to work — and plants the things that will drive the whole game:
  1. **"Follow in Tony's footsteps... there's a lot of work to be done."** — establishes the player's task is to act as Tony would.
  2. **"Don't forget to take care of that dead thing in the trunk of the car."** — plants the car/trunk as a visible, looming objective from minute one.
  3. **An explicit explanation of the countdown gauge** ("that gauge up there runs down while you work... when she hits the red, we're done here") — necessary since the tachometer's readout is intentionally ambiguous (see [`../05-Software-Electronics/props/countdown-gauge/README.md`](../05-Software-Electronics/props/countdown-gauge/README.md)); players need to know *what it is* even if not the exact time remaining.
- Players can now see the parked car with its trunk (visibly locked) sitting in the bay — a constant reminder of unfinished, ominous-sounding business.
- Players should also notice the **Mascot Mount** near the sign — visibly empty/incomplete, an obvious "something goes here" fixture, though its significance isn't clear yet.

### The "Go" Moment (timer start)

To make the timer start feel diegetic rather than a GM pressing a button offscreen, bundle these to fire together the instant Frank finishes his last line ("I'll be around. I'm always around."):

1. The countdown gauge starts sweeping — see [`../05-Software-Electronics/props/countdown-gauge/README.md`](../05-Software-Electronics/props/countdown-gauge/README.md).
2. The bay door behind the players rumbles shut (chain/motor sound) — a satisfying "you're committed now" beat that doubles as a natural trigger point for the above.
3. **Optional, on-theme:** an old ticket printer/punch-clock chatters out a physical **"Job Ticket #1"** prop — a tangible first objective that fits the garage setting, instead of a modern printed rules sheet.

### Avoiding First-Minute Freeze

Frank's dialogue plants a vague ongoing task ("run the shop") plus one concrete but currently-blocked anchor (the trunk). Since the trunk is locked, players' actual first move is "search the Main Bay for the first real gate" — the exact moment groups tend to freeze. **Recommend seeding one obvious, low-difficulty "gimme" puzzle prominently in the Main Bay** just to get hands moving in the first minute or two. Not designed yet — just flagged as a requirement.

## Phase 2 — Main Bay (deepen the wrong assumption)

You're new to the trade; Frank seems against you; odd details pile up. Early puzzles should **push further into suspicion**, not toward the truth. Hard rule: **nothing states "mob"** — players invent that. See [`../03-Flow/suspicion-curve.md`](../03-Flow/suspicion-curve.md).

- **Photo of Uncle Tony** — know his face.
- **Recording: Tony & "the Don"** "taking care of" an old man — *sounds* sinister; text never says crime.
- **Mechanic Station** — physical puzzle idea (engine/pulleys) — backlog.
- **Distinctive battery** — long-lead item for Sparky later.
- Frank watching from upstairs window.

**Design intent:** ambiguous "bad vibes" that a reasonable player over-reads as crime.

## Phase 3 — Storage `[ACCESS TBD]` (peak wrong certainty)

Still **no reframe**. Storage should make the dark assumption feel airtight — while remaining literally innocent under a later reading.

- **Handshake photo** (Tony + unnamed Chief) — player may think "corrupt cop"; photo never says that.
- Filing cabinet / letters / crossed-out "taken care of" photos / cash — same pattern: misreadable, not accusatory.

Exit Storage believing you inherited something shady. Truth not yet available.

## Phase 4 — Office `[ACCESS TBD]` (turn starts here)

**First place assumptions start to crack.** Cascade of a-has as old clues re-read — not one exposition dump.

- **Labeled photo: Chief Dawn Adams** — with handshake + "the Don" recording → **"Don" = Dawn** (one a-ha among several).
- Calendar / ledger / personal papers that don't fit the crime story (or fit charity better).

**Design flag:** give players ways to *use* realizations in-game (e.g. DAWN), and prefer multiple mini-reveals over a single "here's the truth" document.

## Phase 5 — Tools Closet container (sequencing + role still open)

**Not a zone** — a container (or sub-area of Main). Leading concept: a **power source** here needs to be connected/routed to power something elsewhere. Alternatives: several small nested containers, or one bigger puzzle. Sequencing relative to Storage/Office still open.

## Phase 6 — The Cascade (Office onward)

The turn that **started in Office** completes as each earlier clue flips:

- "The Don" → Dawn Adams (partner, not boss)
- "Taken care of" → helped, not harmed
- Overnight work → charity repairs
- Cash → anonymous donor fund
- Letters → real help requests

Emotional core of the room: *"I assumed wrong — and every clue told a different story."* Optional: re-light or re-annotate 1–2 earlier props so the click is physical, not only mental.

## Phase 7 — Opening the Car Trunk container `[ACCESS TBD]` (last major gate)

Having pieced together the truth, the player opens the **car trunk** (a container in Main — not a zone). Inside: **Sparky**, lifeless, missing his battery.

**Proposed mechanism (multi-layered puzzle pattern):** the trunk lock requires 3 parts sourced from Storage, Office, and the Tools Closet container — only combining when brought back to the trunk. See [`../03-Flow/puzzle-dependency-map.md`](../03-Flow/puzzle-dependency-map.md) (not finalized).

## Phase 8 — The Finale (Main Bay, Mascot Mount)

1. Player installs the battery (carried since Phase 2) into Sparky.
2. Places Sparky on the **Mascot Mount**.
3. The mount's small monitor lights up: **Tony's** recorded message plays (full script in [`../01-Story/in-room-text.md`](../01-Story/in-room-text.md)).
4. Player is asked: *"Are you ready to join the family?"* — **YES / NO** buttons light up beneath the monitor.
5. Branch resolves per [`../01-Story/narrative-arc.md`](../01-Story/narrative-arc.md) — either a quiet, warm handoff to **Frank**, or the full lights/music/dual-signage payoff.

---

## Contingency: Mid-Game Difficulty Assist

Layered on top of the whole sequence above: if a group is visibly struggling, Frank can grudgingly unlock an assist cabinet ("Tony's Locker") containing easier/duplicate clues for whichever gate is currently blocking them — framed in-character rather than as an obvious hint system. Full design in [`../03-Flow/adaptive-difficulty.md`](../03-Flow/adaptive-difficulty.md).

## Open Questions From This Pass

1. Confirm Tools Closet as a **container** in Main (not a zone), and its sequencing relative to Storage/Office.
2. **Exact evidence split** — which zone/container holds filing cabinet, dirty money, calendar, crossed-out photos, letters (beyond the two confirmed photos).
3. **"Dawn = Don" payoff mechanic** — concept drafted as Partner Line card-swap in [`../04-Puzzles/03-partner-line-dawn/puzzle-concept.md`](../04-Puzzles/03-partner-line-dawn/puzzle-concept.md); still need to lock payoff contents (ledger vs audio vs trunk part).
4. Main Mechanic Station puzzle design.
5. Tools Closet power-source: what it powers, how the connection works.
