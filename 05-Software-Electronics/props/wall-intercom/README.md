# Prop: Wall Intercom (Frank)

## Role

Frank's primary **voice channel** into the room — shop wall intercom. He is **not a one-and-done intro**; expect **ongoing interaction** throughout the game (opening, watching/comments, assists, story beats, reset/end handoffs). Design show-control and line lists with multiple triggerable cues, not a single opening clip.

### Planned / likely Frank touchpoints

| When | Purpose |
|---|---|
| After Marion Cole message | Opening monologue |
| Mid-game (periodic / event-based) | Gruff comments, "I'm watching," pressure without full spoilers |
| Adaptive difficulty | Tony's Locker / assist framing |
| Near trunk / finale (optional) | Reaction beats before Tony's video takes over |
| Time pressure (optional) | Short nudges as tach nears redline |

GM should be able to fire canned lines manually; automatic triggers for known beats.

## Player Experience (opening)

1. Answering machine message ends (see [`../answering-machine-phone/README.md`](../answering-machine-phone/README.md)).
2. Wall intercom **clicks/crackles** (attention cue — optional call light or "TALK" LED).
3. Frank's opening monologue plays (gruff, overheard the lawyer, sends them to work, explains tachometer, plants the trunk).
4. Intercom clicks off → Go Moment.

## Relationship to Other Props

| Prop | Relationship |
|---|---|
| Answering machine phone | Upstream trigger — message end starts Frank |
| Upstairs window | Visual presence of Frank watching; **audio is this intercom**, not the window. Window stays eyes/shadow; intercom is voice |
| Tony's Locker assist | Mid-game Frank lines can reuse this same intercom |
| Finale monitor (Tony) | Separate system — Tony is video on the Mascot Mount, not the intercom |

## Build Placeholder (v1 approach)

| Piece | Notes |
|---|---|
| Wall-mount intercom shell (vintage shop/office look) | Can be hollow prop faceplate |
| Speaker (in unit or remote) | Clear midrange for dialogue |
| Optional call light / "IN USE" LED | Lights when Frank is speaking |
| Audio playback | Same show-control brain as answering machine preferred (one sequencer for intro) |
| Optional mic (v2) | Only if we want live GM Frank; v1 = pre-recorded + triggered lines |
| Trigger inputs | Start-of-intro (from phone end); assist tier 1/2/3 cues; manual GM "play line X" |

**Show-control note:** treat intro as a short state machine: `IDLE → MARION_PLAYING → FRANK_INTRO → GAME_RUNNING`. Intercom is the output device for `FRANK_*` states.

## Script

See [`../../../01-Story/in-room-text.md`](../../../01-Story/in-room-text.md) — Frank opening + assist lines in [`../../../03-Flow/adaptive-difficulty.md`](../../../03-Flow/adaptive-difficulty.md).

## Status

Concept confirmed as Frank's voice delivery. Not built. BOM draft in inventory.
