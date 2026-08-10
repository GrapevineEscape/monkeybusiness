# Inventory & Shopping List

**Rule: nothing is marked "Owned" unless explicitly confirmed by Russell.** Default status for every new item is `Needed`.

Status legend: `Needed` → `To Buy` (decided on a source/link) → `Ordered` → `Owned` → `In Build` → `Installed`

| Item | Needed For (Puzzle/Room) | Qty | Est. Cost | Status | Source/Link | Notes |
|---|---|---|---|---|---|---|
| Garage mascot prop (statue/figure, battery-operated) | Finale — trunk reveal / mantle | 1 | — | Needed | — | Possibly an animatronic monkey figure (grease monkey pun) — pending confirmation |
| Battery (specific/oddball type/size) for mascot | Early-game held item → Finale | 1+ | — | Needed | — | Should be a distinctive battery type so it's memorable as a held item |
| Video monitor/screen (small, mantle-mounted) | Finale — Tony's message | 1 | — | Needed | — | Needs video playback capability, ideally triggered on prop placement |
| Video monitor/screen (Manager greeting) | Act 1 — Manager intro | 1 | — | Needed | — | Could double up with other room screens depending on room design |
| Illuminated YES / NO push buttons | Finale — branching choice | 2 | — | Needed | — | Needs GPIO/relay integration, see `05-Software-Electronics/` |
| "Tony's Garage" sign (illuminated) | Set dressing | 1 | — | Needed | — | Must support a second illuminated line/sign underneath |
| "...IS FOR FAMILY" secondary sign (illuminated) | Finale — YES ending | 1 | — | Needed | — | Only lights on YES branch |
| Trunk / car prop with locking mechanism | Act 3 — mascot reveal | 1 | — | Needed | — | Lock mechanism TBD once puzzle design starts |
| Filing cabinet (lockable) | Evidence — "down and out" letters | 1 | — | Needed | — | |
| Audio playback prop (recordings — answering machine/cassette/dictaphone style) | Evidence — "the Don" recordings | 1+ | — | Needed | — | Needs two-part/reveal audio content |
| Framed photos (crossed-out figures, handshake photo, etc.) | Evidence | Several | — | Needed | — | Also need "lights up" versions for finale YES branch |
| Prop cash ("dirty money") | Evidence | — | — | Needed | — | |
| Donor ledger / paperwork props | Evidence — office/storage room; candidate Partner Line payoff | Several | — | Needed | — | |
| Partner Line desk card cradle / latch | Puzzle 03 — Dawn = Don payoff | 1 | — | Needed | — | Mechanical lean; see `04-Puzzles/03-partner-line-dawn/` |
| "THE DON" dummy partner card | Puzzle 03 — seated at reset | 1 | — | Needed | — | Misdirect texture |
| "DAWN" / Dawn Adams keyed card | Puzzle 03 — correct key | 1 | — | Needed | — | Magnet/shape key TBD |
| Sticky note ("use the name, not the nickname") | Puzzle 03 — instruction | 1 | — | Needed | — | |
| Optional Office desk handset / speaker for Dawn thank-you clip | Puzzle 03 — audio payoff | 1 | — | Needed | — | Optional upgrade; keep separate from start-game shop phone |
| Room lighting control (dimmable/addressable) | Finale ambiance shift | — | — | Needed | — | See `05-Software-Electronics/` |
| Speaker/audio system for finale music | Finale | — | — | Needed | — | |
| Desk (Office) | Set dressing — Office | 1 | — | Needed | — | |
| Chairs (Office) | Set dressing — Office | 2-3 | — | Needed | — | Sketch shows 2-3 |
| Mechanic station equipment/tool chest (Main Bay) | Set dressing — Main Garage Bay | 1 set | — | Needed | — | |
| Mechanic station equipment (private, Office) | Set dressing — Office | 1 set | — | Needed | — | Smaller/personal version |
| Storage shelving/boxes | Set dressing — Storage Closet | — | — | Needed | — | |
| Tool storage/pegboard | Set dressing — Tools Closet | — | — | Needed | — | Role of this room still TBD |
| Window prop (near entrance) | Set dressing — Main Bay | 1 | — | Needed | — | Possibly ties to "upstairs window" Frank watches from — open question |
| Interior doors w/ hardware (Office, Storage Closet) | Room build | 2 | — | Needed | — | Lock mechanisms TBD once puzzle design starts |
| Small TV/monitor (hidden screen) | Upstairs Window prop | 1 | — | Needed | — | See `05-Software-Electronics/props/upstairs-window/` |
| Cheap metal mini blinds | Upstairs Window prop | 1 | — | Needed | — | Sized to hidden screen |
| Servo motor(s) for blind tilt rod | Upstairs Window prop | 1-2 | — | Needed | — | |
| Small controller (Raspberry Pi or similar) | Upstairs Window prop | 1 | — | Needed | — | May be reusable/shared with other show-control needs |
| Window mounting frame/enclosure | Upstairs Window prop | 1 | — | Needed | — | Custom build |
| Wrench prop (for Sparky) | Mascot — Sparky | 1 | — | Needed | — | Sized for mascot to "hold" |
| "Sparky" nametag | Mascot | 1 | — | Needed | — | |
| Monkey figure/statue base (for Sparky) | Mascot | 1 | — | Needed | — | See `01-Story/characters.md` — static vs. simple animatronic TBD |
| Assorted small lockable containers (lockers, cabinets, drawers) | Scattered gates/clues, multiple zones | Several | — | Needed | — | Exact count/placement TBD in puzzle design |
| Power source prop (Tools Closet) | Tools Closet puzzle concept | 1 | — | Needed | — | e.g. battery bank/breaker box/generator prop — needs to route power elsewhere in room |
| Engine / lift-knobs / pulleys mechanism materials | Main Bay Mechanic Station puzzle concept | — | — | Needed | — | Not yet designed — placeholder |
| "Closed — Family Emergency" door sign | Set dressing — Entrance | 1 | — | Needed | — | See `01-Story/in-room-text.md` |
| "Sparky" nameplate (for empty Mascot Mount) | Set dressing — Main Bay | 1 | — | Needed | — | |
| Personal set-dressing items (mug, calendar, tools) | Set dressing — Main Bay | Several | — | Needed | — | Sells the "lived-in, recently used" feel |
| Bay door closure show-control (motor/sound trigger) | "Go Moment" — Phase 1 | 1 | — | Needed | — | Ties to timer start trigger |
| Job Ticket printer/prop (optional) | "Go Moment" — Phase 1 | 1 | — | Needed | — | Optional — old dot-matrix/receipt printer style |
| Large custom tachometer gauge face | Countdown Timer prop | 1 | — | Needed | — | See `05-Software-Electronics/props/countdown-gauge/` |
| Stepper/servo motor + driver (gauge needle) | Countdown Timer prop | 1 | — | Needed | — | |
| Addressable LED strip/ring (redline backlight) | Countdown Timer prop | 1 | — | Needed | — | |
| Microcontroller for gauge (Arduino/ESP32) | Countdown Timer prop | 1 | — | Needed | — | May be shared with central show-control |
| "Tony's Locker" cabinet | Adaptive difficulty assist | 1 | — | Needed | — | See `03-Flow/adaptive-difficulty.md` |
| Electronic lock (maglock/solenoid) for Tony's Locker | Adaptive difficulty assist | 1 | — | Needed | — | Remote-triggered, not puzzle-solved |
| GM control panel / trigger buttons (per assist tier) | Adaptive difficulty assist | Several | — | Needed | — | May share hardware with other show-control triggers |
| Sealed hint envelopes/compartment labels | Adaptive difficulty assist | Several | — | Needed | — | One per major bottleneck (Storage/Office/Tools/Trunk) |
| Period landline phone + answering machine base | Opening — Marion Cole start | 1 | — | Needed | — | See `05-Software-Electronics/props/answering-machine-phone/` |
| Blinking message LED + Play button wiring | Opening — answering machine | 1 set | — | Needed | — | |
| Audio playback module (phone) | Opening — Marion Cole | 1 | — | Needed | — | May share show-control PC/Pi with intercom |
| Wall-mount intercom shell | Frank voice channel | 1 | — | Needed | — | See `05-Software-Electronics/props/wall-intercom/` |
| Intercom speaker + optional call LED | Frank voice channel | 1 set | — | Needed | — | |
| Audio playback / show-control for Frank lines | Frank voice channel | 1 | — | Needed | — | Opening + assist lines; prefer shared sequencer with phone |
| Separate evidence recording prop (dictaphone/cassette) | Main — Tony/"Don" clue | 1 | — | Needed | — | Do not overload start-game phone |
| Keyring prop labeled "Tony's Garage" | Opening / set dressing | 1 | — | Needed | — | Optional; no longer required to "find" for Marion's message |
| Trunk multi-part lock mechanism (3-piece combination) | Trunk — multi-layered puzzle proposal | 1 | — | Needed | — | Not yet designed — see `03-Flow/puzzle-dependency-map.md` |

## Owned Already

_(nothing confirmed yet)_

## Running Cost Estimate

| Category | Est. Total |
|---|---|
| Room/Set build | — |
| Puzzles (physical) | — |
| Electronics/software | — |
| Consumables/misc | — |
| **Total** | **—** |
