# Software & Electronics

Cross-cutting technical systems that power props/puzzles (sensors, relays, RFID, lighting, sound, show-control, etc.). Puzzle-specific electronics can live either here (if shared/reusable) or inside the puzzle's own folder under [`../04-Puzzles/`](../04-Puzzles/) (if puzzle-specific) — link between them either way.

- [`hardware/`](./hardware/) — hardware list, wiring diagrams, datasheets/notes per component
- [`firmware/`](./firmware/) — microcontroller code (Arduino/ESP32/Raspberry Pi/etc.)
- [`props/`](./props/) — one subfolder per complex automated prop/effect (feasibility notes, technical approach, BOM), e.g. [`props/upstairs-window/`](./props/upstairs-window/README.md)
- [`show-control.md`](./show-control.md) — how puzzles trigger effects across the room (central controller vs. standalone props), master reset procedure

## Status

Prop folders (placeholders — not built unless noted):

| Prop | Role |
|---|---|
| [`props/answering-machine-phone/`](./props/answering-machine-phone/README.md) | Blinking message light → Play → Marion Cole; **starts intro** |
| [`props/wall-intercom/`](./props/wall-intercom/README.md) | Frank's voice channel (opening + mid-game assists) |
| [`props/upstairs-window/`](./props/upstairs-window/README.md) | Frank visual presence (shadow + blinds + eyes) |
| [`props/countdown-gauge/`](./props/countdown-gauge/README.md) | Tachometer timer (confirmed concept) |
| [`props/shop-pc-hub/`](./props/shop-pc-hub/README.md) | Main shop PC — login + menu hub (parts / customers / air / …) |

Intro show-control sequence: `IDLE → MARION_PLAYING → FRANK_INTRO → GAME_RUNNING`.

Shop PC hub is a **compartmentalized** kiosk app when we build it — flow pin in [`../03-Flow/shop-pc-hub.md`](../03-Flow/shop-pc-hub.md). Otherwise still early — other puzzle-specific electronics TBD.
