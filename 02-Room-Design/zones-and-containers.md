# Zones & Containers

Canonical vocabulary for this project. Use these terms going forward.

## Zones

A **zone** is a player-enterable space — a room or open area of the shop. There are exactly **three**:

| Zone | Description |
|---|---|
| **Main** (Main Garage Bay) | The open shop floor: entrance, sign, Mechanic Station, Mascot Mount, parked car, Frank's window, etc. |
| **Storage** (Storage Closet) | Enclosed room, accessed first among the gated rooms |
| **Office** | Enclosed room, Tony's private workspace, accessed after Storage |

Zones can contain containers. Zones are not containers.

## Containers

A **container** is anything that can hold something else (clue, item, puzzle part, assist material). Containers sit *inside* zones (or, rarely, are nested inside other containers). Containers may be locked, unlocked, gated by puzzles, or GM-triggered.

**Do not call the Trunk a zone.** It is a container in Main.

### Container Inventory (living list)

Add a row whenever we invent a new thing that holds something else. Status: `Confirmed` = named in story/design; `Proposed` = floated, not locked.

| Container | Zone | Type | Holds (known / intended) | Status | Notes |
|---|---|---|---|---|---|
| Shop phone / answering machine | Main | Phone + message store | Marion Cole voicemail (game start); Play button | Confirmed | Start device — see `05-Software-Electronics/props/answering-machine-phone/` |
| Shop PC hub | Main | Interactive terminal / kiosk | Login + menu (parts, customers, air, …) | Proposed (flow-pinned) | Recurring Main hub — see `03-Flow/shop-pc-hub.md` + `05-Software-Electronics/props/shop-pc-hub/` |
| Car trunk | Main | Locked vehicle compartment | Sparky (mascot); last major gate | Confirmed | Multi-layer 3-part lock proposed; not a zone |
| Tony's Locker | Main (placement TBD) | Assist cabinet/locker | Mid-game easier clues / spare parts (envelopes) | Confirmed (mechanism) | GM/auto unlock only — not puzzle-solved |
| Desk drawer(s) | Office | Furniture drawer | TBD | Proposed | Typical "locked drawer" container |
| Filing cabinet | Storage (placement TBD) | Multi-drawer cabinet | "Down and out" letters; other records | Confirmed as prop; zone TBD if moved | Each drawer can be its own nested container if locked separately |
| Assorted lockers | TBD | Employee/shop lockers | Clues / parts | Proposed | Scattered gates |
| Assorted cabinets | TBD | Shop cabinets | Clues / parts | Proposed | Scattered gates |
| Safe / strongbox | TBD | Secure box | TBD | Proposed | Only if we add one |
| Boxes / crates | Storage (likely) | Open or closed storage | Records, parts | Proposed | May be unlocked set dressing or mini-gates |
| Recording device | Main (likely) | Playback prop that "holds" audio | Tony/"Don" recording(s) | Confirmed as clue vehicle | Counts as a container only if it stores/hides a physical or digital payload players extract |
| Sparky (mascot) | Trunk → Mascot Mount | Figure with battery bay | Battery compartment (receives early-game battery) | Confirmed | Nested container: holds the battery once installed |
| Battery (as held item) | Found early in Main | Item | N/A — *not* a container | — | Listed so we don't confuse held items with containers |
| Tools Closet | Main? or TBD | Enclosed closet | Power source / tools / puzzle parts | **Needs classification** | Was previously called a 4th "zone"; under this model it is almost certainly a **container** (or a sub-area of Main), not a 4th zone — confirm |

### Nested containers

Allowed and expected. Example: Filing cabinet (container) → locked top drawer (container) → envelope (container) → letter (content).

When documenting puzzles, say: *"Unlock container X in zone Y to get Z"* — never *"enter the trunk zone."*

## Access language (updated)

**Zone access (gated):** Main (start) → Storage → Office.

**Container access:** individual locks/puzzles throughout; the Car trunk is the last major container gate before the finale (Sparky → Mascot Mount).

## Related docs

- [`concept-overview.md`](./concept-overview.md)
- [`floorplan.md`](./floorplan.md)
- [`walkthrough.md`](./walkthrough.md)
- [`../03-Flow/puzzle-dependency-map.md`](../03-Flow/puzzle-dependency-map.md)
