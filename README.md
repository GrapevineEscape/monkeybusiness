# Monkey Business — Escape Room Project

This is the hub for the *Monkey Business* escape room: story, room design, puzzle flow, individual puzzles, and the software/electronics that bring it all to life.

## Project Spaces

| Folder | Purpose |
|---|---|
| [`00-Project-Management/`](./00-Project-Management/README.md) | Inventory & shopping list, budget, timeline, decision log |
| [`01-Story/`](./01-Story/README.md) | Backstory, characters, narrative arc, in-room text/props copy |
| [`02-Room-Design/`](./02-Room-Design/README.md) | Physical layout, room-by-room concept, set design/theming |
| [`03-Flow/`](./03-Flow/README.md) | Puzzle dependency map — how puzzles branch/gate each other toward the goal |
| [`04-Puzzles/`](./04-Puzzles/README.md) | One folder per puzzle (design, props, solution, build notes) |
| [`05-Software-Electronics/`](./05-Software-Electronics/README.md) | Hardware list, wiring notes, firmware/code for props |
| [`06-Assets/`](./06-Assets/) | Reference images, moodboards, audio, inspiration |

## Status

**Story locked**: *Tony's Garage* — you inherit your late Uncle Tony's auto shop; evidence suggests he was mob-connected, but it's revealed he was secretly funding anonymous car repairs for people in crisis, partnered with the Chief of Police. Ends on a values-based branching choice. Full details in [`01-Story/`](./01-Story/README.md).

**Room concept captured**: one room, one group; **3 zones** (Main, Storage, Office) plus **containers** (trunk, lockers, drawers, etc.) — see [`02-Room-Design/zones-and-containers.md`](./02-Room-Design/zones-and-containers.md) and the player [`walkthrough`](./02-Room-Design/walkthrough.md).

Next up: finish open sequencing/evidence questions, then puzzle flow and design.

## Ground Rules We're Following

- Nothing is considered purchased unless explicitly confirmed — track everything in [`00-Project-Management/inventory-shopping-list.md`](./00-Project-Management/inventory-shopping-list.md).
- Puzzles should be thematic and inventive, not generic "find the key/enter the code" locks — see [`04-Puzzles/README.md`](./04-Puzzles/README.md) for the design philosophy.
- Every complex puzzle gets its own subfolder under `04-Puzzles/`.
- Big open questions and decisions get logged in [`00-Project-Management/decision-log.md`](./00-Project-Management/decision-log.md) so we don't relitigate them later.
