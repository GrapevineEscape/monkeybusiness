# Puzzle Dependency Map

This will become the full gating diagram once puzzles are formally designed in [`../04-Puzzles/`](../04-Puzzles/). For now: confirmed backbone + idea backlog.

Vocabulary: **zones** vs **containers** — see [`../02-Room-Design/zones-and-containers.md`](../02-Room-Design/zones-and-containers.md).

## Confirmed Backbone

```
ZONE: Main (start)
  -> Shop PC hub (sticky-note login gimme; recurring Main station)
       menu: Parts lookup | Customer lookup | Air/compressor | (future)
  -> ZONE: Storage [gate: puzzle(s) TBD]
    -> ZONE: Office [gate: puzzle(s) TBD]
      -> CONTAINER: Tools Closet (sequencing open; not a zone) [gate TBD]
        -> CONTAINER: Car trunk [gate TBD] -- last major container
          -> Finale: Mascot Mount (battery + Sparky) -> Tony -> YES/NO
```

Players bounce back to the **Shop PC in Main** as info from Storage/Office makes menu items useful. Hub detail: [`shop-pc-hub.md`](./shop-pc-hub.md).

Plus: other containers (Tony's Locker, filing cabinet, drawers, lockers, cabinets) not yet mapped to specific gates.

## Multi-Layered Puzzle Pattern (preferred)

Get **part** of a solution in one place, **another part** later, then bring pieces back where they combine and finally work.

**Proposed flagship — Car trunk container:**

- Trunk lock requires **3 parts**, sourced from Storage, Office, and the Tools Closet container.
- Zone access stays Storage → Office; Tools Closet container can slot in relative to those.
- Parts only combine at the trunk (back in Main — "back to the beginning").
- Tools Closet power-source idea can feed extracting that container's part.

## Idea Backlog

| Idea | Where | Notes |
|---|---|---|
| Engine / lift-knobs / pulleys | Main — Mechanic Station | Physical puzzle → something usable elsewhere |
| Power source routed elsewhere | Tools Closet **container** | Cable / trigger / etc. |
| "Dawn = Don" payoff | Cross-zone (Main + Storage + Office) | **Concept foldered** — [`../04-Puzzles/03-partner-line-dawn/puzzle-concept.md`](../04-Puzzles/03-partner-line-dawn/puzzle-concept.md). Lean: seat DAWN card on Office Partner Line (not Storage→Office gate). Payoff contents TBD (ledger / reframe audio / trunk part). |
| Parts book / tech photo → part # | Main + Storage (+ Office scrap?) | **Concept foldered** — [`../04-Puzzles/04-parts-book-corolla/puzzle-concept.md`](../04-Puzzles/04-parts-book-corolla/puzzle-concept.md). Letter + polaroid; **book for make/model**, **Shop PC Parts lookup** for part # → drawer/bin. |
| **Shop PC hub** | **Main (recurring)** | **Pinned** — [`shop-pc-hub.md`](./shop-pc-hub.md). Sticky login; menu: parts, customers, air/compressor, future. Prop: [`../05-Software-Electronics/props/shop-pc-hub/`](../05-Software-Electronics/props/shop-pc-hub/README.md). |
| Several small gates vs one big puzzle | Storage; Tools Closet container | Decide per location |
| Frank intercom beats (ongoing) | Main (heard room-wide) | Not a gate by itself — flavor, pressure, assists, optional story beats |
| Shop phone ring / dial / 2nd message | Main — phone container | Optional mid-game; leave build headroom — see answering-machine-phone prop. Partner Line puzzle prefers a *separate* Office handset so the start-game phone stays clean. |

## Design Philosophy Reminder

Main access sequence for **zones** is gated/linear (Storage → Office). Branching still applies among containers within/around that backbone, and at the finale (YES/NO).

## Early Formal Puzzle Wiring (draft)

| Puzzle | Gate role | Requires | Produces |
|---|---|---|---|
| 01 Tool shadow / CIVIL | Multi-zone; Office drawer cipher (+ placement feeds something else — Option C lean) | Tools Main+Storage; Roman legend; Office strip | CIVIL drawer; placement payoff TBD |
| 02 Path-tracing cogs | Cross-zone layer; payoff TBD | Cogs at 3 find spots | Path-word → TBD |
| 03 Partner Line (Dawn = Don) | **Office container** beat (not the Office door gate) | Triangulation clues Main+Storage+Office | Reframe unlock — ledger / Dawn audio / trunk part TBD |
| 04 Parts book / tech photo | Main + Storage research; drawer/bin payoff | Letter + polaroid; book (make/model); **Shop PC parts lookup** | Bagged part + clue packet (gate role TBD) |
| Shop PC hub | Main recurring station (not a room gate) | Sticky-note login | Unlocks/serves menu tools over the whole game |

## Status

Backbone confirmed + **Shop PC hub pinned in Main**. Puzzles 01–04 in concept folders; zone gates and trunk 3-part sources still unassigned.
