# Prop: Shop PC Hub (Main)

## Role

Touch/clickable **shop computer in Main** — a recurring **hub** with a login + menu of tools (parts lookup, customer lookup, air/compressor control, future slots). Players log in with a sticky-note password (easy), then return here throughout the game as new info makes menu items useful.

Flow pin: [`../../../03-Flow/shop-pc-hub.md`](../../../03-Flow/shop-pc-hub.md).

## Player Experience

1. Notice the greasy CRT/LCD on a Main counter/desk; sticky note on the bezel.
2. Wake machine → login with sticky credentials (gimme).
3. Land on a simple **menu**.
4. Use menu items when puzzles require them; some stay greyed until unlocked.
5. Reset between groups returns to login (or pre-login boot).

## In-Fiction Justification

Tony’s Garage counter PC — work orders, parts, customers, shop utilities. Frank and Tony never changed the password. Of course it’s on a sticky.

## Menu surface (v1 targets)

| Item | Behavior (draft) | Unlocks / needs |
|---|---|---|
| Parts lookup | Select or enter vehicle + pick part matching polaroid → shows part # / triggers drawer or bin | Info from letter/book/photo — puzzle 04 |
| Customer lookup | Search name / plate / ticket → shows record snippet + clue | A name or ticket found in-room |
| Air / compressor | Button or toggle to release pressure / energize air circuit | Software-locked until prior solve or code |
| (Reserved) | Greyed rows for later puzzles | TBD |

## Build Placeholder (approach TBD)

| Piece | Notes |
|---|---|
| Prop shell | Period PC / all-in-one / laptop in a shop cage; mouse or touch |
| Runtime | Raspberry Pi / mini PC kiosk app (fullscreen); or tablet hidden in bezel |
| UI | Simple HTML/local app — login, menu, 2–4 tool screens; chunky fonts, shop aesthetic |
| Sticky note | Physical prop with username/password |
| Outputs | GPIO / relay / MQTT / show-control events (e.g. air solenoid, parts-drawer latch, printer) |
| Audio (optional) | Boot chirp, error beep, “parts ordered” ding |

**Do not** build real vision/photo matching unless we later decide we want it. Parts lookup should be **menu + player judgment** (pick the diagram that matches the polaroid), not camera AI.

**Reset:** logged out; air control re-locked; parts/customer state cleared; sticky note reseated.

## Links

- Flow: [`../../../03-Flow/shop-pc-hub.md`](../../../03-Flow/shop-pc-hub.md)
- First consumer puzzle: [`../../../04-Puzzles/04-parts-book-corolla/puzzle-concept.md`](../../../04-Puzzles/04-parts-book-corolla/puzzle-concept.md)
- Air compressor theme rethink: [`../../../04-Puzzles/theme-brainstorm-v1.md`](../../../04-Puzzles/theme-brainstorm-v1.md)

## Status

Concept pinned. No firmware/UI yet — compartmentalize coding here when we implement the kiosk app.
