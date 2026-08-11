# Show Control

How puzzles trigger effects across the room and how the game is reset between
groups.

Linked from [`README.md`](./README.md). Depends on [`hardware/`](./hardware/)
and [`firmware/`](./firmware/).

## Architecture question (open)

- **Central controller** coordinating all props, vs. **standalone props** that
  each run their own logic. Likely a mix; decide per prop.

## Intro sequence

The opening runs as a state machine (see [`README.md`](./README.md)):

`IDLE → MARION_PLAYING → FRANK_INTRO → GAME_RUNNING`

- Kicked off by the [`props/answering-machine-phone/`](./props/answering-machine-phone/README.md) message light + Play.
- Frank's voice via [`props/wall-intercom/`](./props/wall-intercom/README.md) and presence via [`props/upstairs-window/`](./props/upstairs-window/README.md).
- Hands off to `GAME_RUNNING`, which starts the [`props/countdown-gauge/`](./props/countdown-gauge/README.md) tachometer timer.

## Master reset (to define)

- One action returns every prop, light, lock, and the countdown gauge to its
  start state for the next group.

## Status

Placeholder — sequence sketched, controller architecture and reset procedure
not yet decided.
