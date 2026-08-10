# Rooms & Containers

Canonical vocabulary for this project. Use these terms going forward.

> **Note:** Older docs sometimes said "zone." That means the same three **rooms** below. Prefer **room** in new writing.

## Format

**Three-room escape, one group at a time.** Players move through three connected physical rooms (not one open space subdivided on paper). Booking/format is still a single group experience — not a multi-group circuit of unrelated rooms.

## Rooms (exactly three)

A **room** is a player-enterable enclosed (or bay) space with its own footprint. There are exactly **three**:

| Room | Relative size | Description |
|---|---|---|
| **Main** (Main Garage Bay) | **Largest** — the main room | Open shop floor: entrance, sign, Mechanic Station, Mascot Mount, parked car, Frank's window, etc. |
| **Storage** (Storage Closet) | **Small** | Small enclosed room off Main; accessed first among the gated rooms |
| **Office** | **Mid-size** | Mid-size enclosed room off Main; Tony's private workspace; accessed after Storage |

Rooms can contain containers. Rooms are not containers.

**Do not invent a 4th room.** Tools Closet (if kept) is a **container** / closet off Main, not a fourth room.

## Containers

A **container** is anything that can hold something else (clue, item, puzzle part, assist material). Containers sit *inside* rooms (or, rarely, are nested inside other containers). Containers may be locked, unlocked, gated by puzzles, or GM-triggered.

**Do not call the Trunk a room.** It is a container in Main.

### Container Inventory (living list)

Add a row whenever we invent a new thing that holds something else. Status: `Confirmed` = named in story/design; `Proposed` = floated, not locked.

| Container | Room | Type | Holds (known / intended) | Status | Notes |
|---|---|---|---|---|---|
| Shop phone / answering machine | Main | Phone + message store | Marion Cole voicemail (game start); Play button | Confirmed | Start device — see `05-Software-Electronics/props/answering-machine-phone/` |
| Car trunk | Main | Locked vehicle compartment | Sparky (mascot); last major gate | Confirmed | Multi-layer 3-part lock proposed; not a room |
| Tony's Locker | Main (placement TBD) | Assist cabinet/locker | Mid-game easier clues / spare parts (envelopes) | Confirmed (mechanism) | GM/auto unlock only — not puzzle-solved |
| Desk drawer(s) | Office | Furniture drawer | TBD | Proposed | Typical "locked drawer" container |
| Filing cabinet | Storage (placement TBD) | Multi-drawer cabinet | "Down and out" letters; other records | Confirmed as prop; room TBD if moved | Each drawer can be its own nested container if locked separately |
| Assorted lockers | TBD | Employee/shop lockers | Clues / parts | Proposed | Scattered gates |
| Assorted cabinets | TBD | Shop cabinets | Clues / parts | Proposed | Scattered gates |
| Safe / strongbox | TBD | Secure box | TBD | Proposed | Only if we add one |
| Boxes / crates | Storage (likely) | Open or closed storage | Records, parts | Proposed | May be unlocked set dressing or mini-gates |
| Recording device | Main (likely) | Playback prop that "holds" audio | Tony/"Don" recording(s) | Confirmed as clue vehicle | Counts as a container only if it stores/hides a physical or digital payload players extract |
| Sparky (mascot) | Trunk → Mascot Mount | Figure with battery bay | Battery compartment (receives early-game battery) | Confirmed | Nested container: holds the battery once installed |
| Battery (as held item) | Found early in Main | Item | N/A — *not* a container | — | Listed so we don't confuse held items with containers |
| Tools Closet | Main? or TBD | Enclosed closet | Power source / tools / puzzle parts | **Needs classification** | Not a 4th room — closet/container (or sub-area of Main); confirm |

### Nested containers

Allowed and expected. Example: Filing cabinet (container) → locked top drawer (container) → envelope (container) → letter (content).

When documenting puzzles, say: *"Unlock container X in room Y to get Z"* — never *"enter the trunk room."*

## Access language

**Room access (gated):** Main (start) → Storage → Office.

**Container access:** individual locks/puzzles throughout; the Car trunk is the last major container gate before the finale (Sparky → Mascot Mount).

## Related docs

- [`concept-overview.md`](./concept-overview.md)
- [`floorplan.md`](./floorplan.md)
- [`walkthrough.md`](./walkthrough.md)
- [`../03-Flow/puzzle-dependency-map.md`](../03-Flow/puzzle-dependency-map.md)
