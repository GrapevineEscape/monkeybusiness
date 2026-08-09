# Flow

This is the "HOW do players get from start to goal" layer — the map of puzzle dependencies, branches, and gates that connects [`01-Story/`](../01-Story/) to the individual puzzles in [`04-Puzzles/`](../04-Puzzles/).

- [`puzzle-dependency-map.md`](./puzzle-dependency-map.md) — gates, branches, idea backlog
- [`suspicion-curve.md`](./suspicion-curve.md) — Main/Storage deepen wrong assumption; Office starts the turn; room never says "mob"
- [`adaptive-difficulty.md`](./adaptive-difficulty.md) — mid-game assist (Tony's Locker)
- [`progression-flowchart.md`](./progression-flowchart.md) — visual flowchart (when drawn)

## Design Philosophy

- Prefer **branching** among containers; zone access stays Main → Storage → Office.
- Every gate should serve a story beat.
- **Suspicion curve:** early work pushes *into* the dark assumption; **Office** is first reframe; nothing ever *states* mob — see [`suspicion-curve.md`](./suspicion-curve.md).
- **Multi-layered/distributed puzzles** preferred — see Trunk proposal in `puzzle-dependency-map.md`.
- **Mid-game adaptive difficulty** — [`adaptive-difficulty.md`](./adaptive-difficulty.md).

## Status

Access backbone: Main → Storage → Office; last major container = car trunk. Suspicion curve locked ([`suspicion-curve.md`](./suspicion-curve.md)). Multi-layer trunk proposed. Assist: [`adaptive-difficulty.md`](./adaptive-difficulty.md). No individual puzzles designed yet.
