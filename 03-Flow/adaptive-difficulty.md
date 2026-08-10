# Adaptive Difficulty — Mid-Game Assist

## Philosophy

Preference confirmed: don't try to guess difficulty upfront (no pre-game easy/hard mode toggle for now). Instead, **react mid-game** if a group is visibly struggling, by opening up an alternate, easier pathway — not just a verbal hint. This keeps every group's *starting* experience identical and only intervenes when it's actually needed.

This is distinct from (and complements) the per-puzzle hint escalation already tracked in the puzzle template ([`../04-Puzzles/_template/puzzle-template.md`](../04-Puzzles/_template/puzzle-template.md)) — that's GM-delivered verbal hints for one specific puzzle; this is a room-wide, physical, story-justified fallback.

## Core Mechanism: "Tony's Locker" (proposed name)

A **container** (cabinet/locker) that's **physically present and visible from early in the game**, but locked from the start and easy to dismiss as ordinary scenery (it shouldn't look like "the hint box"). It holds **sealed envelopes or clearly-labeled compartments**, one per major bottleneck (e.g. room gates "Storage" / "Office", or container gates "Tools Closet" / "Car trunk"). It cannot be opened by solving a puzzle — only via a **remote-triggered electronic lock** (maglock/solenoid), fired by the GM or an automatic time-based fallback.

Contents per compartment (concept, not finalized) — should make the *current* bottleneck meaningfully easier without just handing over the answer outright:
- A more direct/explicit rephrasing of an existing clue (e.g., spelling out the "Dawn/Don" phonetic connection more plainly instead of requiring inference)
- A duplicate/spare part for a multi-layered puzzle (see [`puzzle-dependency-map.md`](./puzzle-dependency-map.md) Trunk proposal) — effectively skipping the need to find one of the 3 pieces
- A shortcut item (e.g., a spare key) that bypasses one physical lock entirely

## In-Fiction Framing — Frank

Rather than an obvious meta "hint system," this is framed as **Frank grudgingly helping** over the **wall intercom** (same prop as his opening) — consistent with his character and foreshadowing his warmth at the end. Draft line, triggered by the GM/automatic system:

> "...Alright, alright. Enough standing around, I've got a life too, you know. Tony kept extra parts in his locker for just this kinda thing. Go look. And don't get used to it."

This can be reused/lightly varied for each tier of assist.

## Trigger Model: Hybrid (recommended)

- **Manual (primary):** GM monitors the room (camera/audio) and triggers the unlock whenever they judge the group is stuck — most flexible, matches how well-run rooms actually operate.
- **Automatic (fallback):** time-based triggers fire regardless, in case the room is unstaffed in the moment or the GM misses a cue. Proposed checkpoints (as a fraction of total game time, since exact duration isn't set yet):

| Checkpoint | Trigger (approx.) | Tier |
|---|---|---|
| Soft nudge | ~40% of time elapsed, Storage Closet not yet cleared | Tier 1 — Frank gives a verbal nudge via his monitor, no physical unlock yet |
| Cabinet unlock | ~60% of time elapsed, Office not yet reached | Tier 2 — Tony's Locker unlocks; Frank's line directs them to the relevant envelope |
| Strong bypass | ~85% of time elapsed, car trunk container not yet opened | Tier 3 — a near-direct solution/bypass, prioritizing "the group finishes and has a good time" over difficulty |

Exact percentages/checkpoints should be tuned once total game duration and real playtest data exist — treat this table as a starting structure, not final numbers.

## Technical Implementation (ties to `05-Software-Electronics/`)

- Tony's Locker needs an electronically-actuated lock (maglock or solenoid bolt) wired to the room's central show-control system.
- A simple GM control panel button per tier for manual triggering.
- Automatic fallback timers can likely share the same controller driving the countdown gauge ([`../05-Software-Electronics/props/countdown-gauge/README.md`](../05-Software-Electronics/props/countdown-gauge/README.md)), since both care about elapsed time.

## Open Questions

- Exact contents of each envelope/compartment — depends on final puzzle designs, so revisit once `04-Puzzles/` fills in.
- Should assist ever be *offered* to the players directly (e.g., a discreet "ask for help" button/intercom to Frank) rather than purely GM/automatic-judged? Leaning toward GM/automatic-only for now to preserve immersion, but flagging as a future option.
- Whether unlocking Tony's Locker should be visually/audibly noticeable in the moment (a click + light) or subtle enough that players have to notice it themselves.
- Naming — "Tony's Locker" is a placeholder; open to alternatives.

## Status

Concept and mechanism designed; not yet built. Revisit checkpoint percentages once game duration and specific puzzles are set.
