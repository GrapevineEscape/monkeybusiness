# Puzzles

Each puzzle — especially anything mechanically or electronically complex — gets its own subfolder here, e.g. `04-Puzzles/04-the-typewriter-cipher/`. Use [`_template/`](./_template/) as the starting point for a new puzzle folder.

## Design Philosophy

We are explicitly avoiding generic "lock + code" puzzles as the default. Instead:

- **Theme-first**: every puzzle mechanism should be justifiable in-world — it should feel like it belongs to the story/characters, not like a generic escape-room fixture bolted on.
- **Assumption, not accusation**: Main/Storage clues may *invite* a mob reading; they must never *state* it. Office is where wrong assumptions start to crack. See [`../03-Flow/suspicion-curve.md`](../03-Flow/suspicion-curve.md).
- **Novel interaction**: prefer mechanisms that feel a little magical or surprising — hidden reveals, transformation (something changes state in a satisfying physical/sensory way), multi-sensory clues (sound, light, smell, touch), or props that "come alive" via light electronics — over simply entering a number into a lock.
- **Branching-friendly**: where possible, puzzles should support multiple entry points or partial progress, so groups aren't fully blocked on one linear chain (ties into [`../03-Flow/`](../03-Flow/)).
- **Fair but surprising**: the "aha" should feel earned from clues already given, even if the delivery mechanism is unexpected.
- **Multi-layered/distributed preferred**: favor puzzles that hand out partial pieces across different zones/containers which only combine back at an earlier location — see flagship **car trunk** proposal in [`../03-Flow/puzzle-dependency-map.md`](../03-Flow/puzzle-dependency-map.md). Use zone/container language from [`../02-Room-Design/zones-and-containers.md`](../02-Room-Design/zones-and-containers.md).
- **Bypass-aware**: when designing a puzzle, consider whether it's a reasonable candidate for a mid-game difficulty bypass (see [`../03-Flow/adaptive-difficulty.md`](../03-Flow/adaptive-difficulty.md)) — not every puzzle needs one, but note it in the puzzle's doc if it is one.
- **Frank / phone as puzzle channels**: Frank's wall intercom is a recurring interaction surface. The shop phone is confirmed for game start; **may** also support inbound/outbound calls or a later message — keep that option in mind when inventing puzzles (see prop READMEs under `05-Software-Electronics/props/`).

## Puzzle Index

| # | Name | Room | Type | Status | Folder |
|---|---|---|---|---|---|
| 01 | Tool shadow / cork board → CIVIL | Main + Storage + Office | Multi-zone; placement + cipher | Concept — placement fix TBD | [`01-tool-shadow-board/`](./01-tool-shadow-board/puzzle-concept.md) |
| 02 | Path-tracing cogs | Pegboard + 3 find spots | Multi-zone; symbol-align overlays + path-trace | Concept — word/payoff TBD | [`02-path-tracing-cogs/`](./02-path-tracing-cogs/puzzle-concept.md) |
| 03 | Partner Line ("Call the Don") → DAWN | Main + Storage + Office | Cross-zone triangulation + physical name swap | Concept — payoff contents TBD | [`03-partner-line-dawn/`](./03-partner-line-dawn/puzzle-concept.md) |

## Status

Theme brainstorm started: [`theme-brainstorm-v1.md`](./theme-brainstorm-v1.md). Formal folders for #01–#03. Whittle remaining HOT themes next; lock payoffs on concepts already foldered.
