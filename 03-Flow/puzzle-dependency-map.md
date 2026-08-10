# Puzzle Dependency Map

This will become the full gating diagram once puzzles are formally designed in [`../04-Puzzles/`](../04-Puzzles/). For now: confirmed backbone + idea backlog.

Vocabulary: **rooms** vs **containers** (older "zone" = room) — see [`../02-Room-Design/zones-and-containers.md`](../02-Room-Design/zones-and-containers.md). Three rooms: Main (largest) → Storage (small) → Office (mid-size).

## Confirmed Backbone

```
ROOM: Main garage (start, largest)
  -> ROOM: Storage (small) [gate: puzzle(s) TBD]
    -> ROOM: Office (mid-size) [gate: puzzle(s) TBD]
      -> CONTAINER: Tools Closet (sequencing open; not a 4th room) [gate TBD]
        -> CONTAINER: Car trunk [gate TBD] -- last major container
          -> Finale: Mascot Mount (battery + Sparky) -> Tony -> YES/NO
```

Plus: other containers (Tony's Locker, filing cabinet, drawers, lockers, cabinets) not yet mapped to specific gates.

## Multi-Layered Puzzle Pattern (preferred)

Get **part** of a solution in one place, **another part** later, then bring pieces back where they combine and finally work.

**Proposed flagship — Car trunk container:**

- Trunk lock requires **3 parts**, sourced from Storage, Office, and the Tools Closet container.
- Room access stays Storage → Office; Tools Closet container can slot in relative to those.
- Parts only combine at the trunk (back in Main — "back to the beginning").
- Tools Closet power-source idea can feed extracting that container's part.

## Idea Backlog

| Idea | Where | Notes |
|---|---|---|
| Engine / lift-knobs / pulleys | Main — Mechanic Station | Physical puzzle → something usable elsewhere |
| Power source routed elsewhere | Tools Closet **container** | Cable / trigger / etc. |
| "Dawn = Don" payoff | Cross-room (Main + Storage + Office) | Must be *used* in-game, not only mental |
| Several small gates vs one big puzzle | Storage; Tools Closet container | Decide per location |
| Frank intercom beats (ongoing) | Main (heard room-wide) | Not a gate by itself — flavor, pressure, assists, optional story beats |
| Shop phone ring / dial / 2nd message | Main — phone container | Optional mid-game; leave build headroom — see answering-machine-phone prop |

## Design Philosophy Reminder

Main access sequence for **rooms** is gated/linear (Storage → Office). Branching still applies among containers within/around that backbone, and at the finale (YES/NO).

## Status

Backbone confirmed (three-room layout). Individual puzzles live under [`../04-Puzzles/`](../04-Puzzles/).
