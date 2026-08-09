# Prop: Countdown Timer — "The Tachometer"

## Concept (confirmed)

An oversized automotive **tachometer (RPM gauge)** mounted prominently in the Main Garage Bay, doubling as the room's countdown timer. A single needle sweeps clockwise from idle (game start) toward a **redline zone** (time's up) over the course of the game — no numbers required for players to feel the tension building.

## Why a Tachometer

| Concept | Read | Verdict |
|---|---|---|
| **Tachometer / RPM gauge** | Needle sweeps toward redline | **Recommended** — iconic, immediately legible as "danger approaching" without needing to read numbers, perfectly on-theme for a garage |
| Fuel gauge (Full → Empty) | "Running out of gas" | Nice metaphor, less visceral than redlining |
| Hydraulic/air pressure gauge | Needle climbs toward max pressure | Good alternate if a "building pressure" feel is preferred over "speed" |
| Vintage oil-brand wall clock, motorized single hand | Shop decor clock | Easiest to build, least dramatic/thematic |
| Digital pump-style number display | Precise minutes remaining | Good as a *secondary* discreet readout, weak as the sole hero prop |

## Recommended Design

- Large custom gauge face (printed/silkscreened, or a real oversized tachometer housing repurposed), scaled to the room's total game length rather than real RPM.
- Single needle driven by a stepper or geared DC motor, controlled by a microcontroller counting down total game time and mapping elapsed time to needle angle.
- **Redline zone** (final chunk of time) backlit via addressable LEDs — dark/unlit for most of the game, glowing red once time is short.
- Optional: a subtle ambient engine-idle hum (via the room's audio system) that rises in pitch as time passes, peaking as the needle nears redline — reinforces tension sonically as well as visually.
- Start trigger: tied to the "Go Moment" in [`../../../02-Room-Design/walkthrough.md`](../../../02-Room-Design/walkthrough.md) — i.e., the end of Frank's opening line / bay door closing, not a separate manual GM action.

## Precision vs. Immersion — Decided

**Ambiguous/dramatic only** — no secondary digital countdown. The tachometer is the sole time reference; players read tension off the needle's position, not an exact number.

**Requirement:** because the readout is ambiguous, the team must still be explicitly told *what it represents* (even if not the exact time). Frank's opening line now includes a direct explanation — see [`../../../01-Story/in-room-text.md`](../../../01-Story/in-room-text.md) — something like *"that gauge up there runs down while you work — when she hits the red, we're done here, one way or another."* Ambiguous ≠ unexplained.

## Feasibility

**Feasible.** Stepper/servo-driven prop gauge needles controlled by a microcontroller are a well-documented technique in the escape-room/prop-building community. The main effort is graphic design of the gauge face and the mounting/housing, not the electronics.

## Bill of Materials (draft — added to master inventory)

- Large gauge face (custom-printed face, or a repurposed/oversized real tachometer housing)
- Stepper or servo motor + driver board
- Microcontroller (Arduino/ESP32) — possibly shared with the room's central show-control system rather than a dedicated unit
- Addressable LED strip/ring for the redline backlight
- Mounting bracket/housing

## Open Questions

- Exact mounting location within the Main Bay (near the sign/Mechanic Station per the floorplan)
- GM pause/adjust capability — standard for escape room timers, should be included
- **Total game duration** — still an open question from the original project kickoff; needed to calibrate the gauge's idle-to-redline mapping and the [`adaptive-difficulty.md`](../../../03-Flow/adaptive-difficulty.md) checkpoint timings

## Status

Concept confirmed (tachometer, ambiguous readout). Not yet designed/built.
