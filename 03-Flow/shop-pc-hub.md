# Shop PC Hub (Main) — Flow Pin

**Status:** Direction pinned by Russell (2026-08-10) — editable whiteboard, not built.  
**Where:** **Main** garage bay — a greasy shop computer players return to all game.  
**Prop/build notes:** [`../05-Software-Electronics/props/shop-pc-hub/README.md`](../05-Software-Electronics/props/shop-pc-hub/README.md)

---

## Why it exists

Main needs a **diegetic hub**: one place with a menu of jobs that unlock or matter at different times. Not a magic puzzle box — a shop PC mechanics actually use (and leave passwords on sticky notes for).

Players log in early (easy), then keep coming back as new menu items become useful or newly unlocked.

---

## Login (easy on purpose)

- Login screen at game start (or after Go Moment).
- Credentials on a **sticky note** on the monitor/bezel (classic mechanic behavior).
- Getting in is a **gimme**, not a gate — teaches “use the PC” without friction.
- Optional flavor: username `tony` / `frank` / `shop`; password something dumb like `sparekey` or `sparky1`.

---

## Menu (multi-use hub)

Exact menu labels TBD. Working set from Russell:

| Menu item | Role in flow | Notes |
|---|---|---|
| **Parts lookup** | Feeds puzzle 04 (and maybe others) | Enter/select make·model (from letter/book/scraps) + match polaroid → part number / dispense unlock. See [`../04-Puzzles/04-parts-book-corolla/puzzle-concept.md`](../04-Puzzles/04-parts-book-corolla/puzzle-concept.md). |
| **Customer lookup** | Story + puzzle channel | Search “down and out” / job tickets; early misread as ledger of marks; later re-reads as people helped. May gate a clue or confirm a name. |
| **Air / compressor control** | Physical gate in Main | e.g. “release air pressure” / enable compressor circuit — **locked in software until something else is solved** (or until a code is found). Ties to air-compressor rethink in theme brainstorm. |
| **(Future slots)** | Keep headroom | Work orders, bay camera (fake), invoice print (DO NOT invoice irony), clock/time stamp, etc. Grey out until needed. |

Menu items can be:
- **Always available** but useless until you have the right info (parts lookup), or
- **Greyed out / “ACCESS DENIED”** until a prior puzzle unlocks them (air release).

---

## Place in the main game flow

```
Go Moment (phone → Frank → tach)
  -> Main exploration
       -> Shop PC: sticky-note login (gimme)
            -> HUB active for the rest of the game
                 -> Parts lookup ........ when letter + polaroid (+ book) exist
                 -> Customer lookup .... when a name/ticket is found
                 -> Air/compressor ..... when its unlock condition is met
                 -> (other menu items as designed)
  -> Storage / Office still gated by room doors as usual
  -> Players bounce back to Main PC as the recurring station
```

**Design rule:** The PC is a **Main anchor**. Cross-room puzzles may send you *to* the PC with new info; the PC should rarely be the only copy of a critical story reveal (suspicion-curve paper/audio still matters).

---

## Suspicion-curve notes

| Screen | Early misread | Later read |
|---|---|---|
| Customer list / “no invoice” flags | Off-books jobs, people who “owe” | Charity cases Tony covered |
| Parts order for Friday | Shady deadline | Staged free repair |
| Locked air control | “What are they hiding” | Ordinary shop interlock + puzzle gate |

Copy law still applies — no screen should say mob/mafia/hit.

---

## Open questions

1. Which menu item unlocks first after login (besides browsing empties)?
2. Does **air release** unlock a hose/tool for lug nuts, a blow-gun reveal, or a latch elsewhere?
3. Is customer lookup read-only flavor + one code, or a full mini-puzzle?
4. One shared show-control Pi/PC vs a dedicated shop-PC machine players touch?
5. How hard to make the UI feel period-shop without building a real inventory system?

---

## Status

Pinned to Main flow as the multi-use hub. Parts lookup is the first concrete consumer (puzzle 04). Air/compressor + customer lookup slotted as additional menu work. Build approach lives under `05-Software-Electronics/props/shop-pc-hub/`.
