# Prop: Answering Machine Phone (Marion Cole / Game Start)

## Role

Diegetic **game start** control. Players enter Main, see a landline phone with a **blinking message light**, press **Play**, hear Marion Cole's estate voicemail, then the system hands off to Frank on the wall intercom.

## Player Experience

1. Room is "live" but the countdown has not started.
2. Phone message light blinks (obvious first interaction — pairs with the early "gimme" philosophy).
3. Player presses **Play** (physical button on the phone/base).
4. Marion Cole message plays through the phone's speaker (or a nearby dedicated speaker if volume needs help).
5. On message end → trigger show-control: Frank's wall intercom sequence begins (see [`../wall-intercom/README.md`](../wall-intercom/README.md)).
6. After Frank finishes → Go Moment (tachometer + bay door, etc.).

## In-Fiction Justification

Tony's shop phone has a new voicemail from the estate lawyer waiting. Frank has already overheard it (he's listening somehow — intercom tap / upstairs — doesn't need to be explained on day one).

## Build Placeholder (v1 approach)

| Piece | Notes |
|---|---|
| Period landline phone + answering machine base (or phone with integrated digital answering) | Prop shell; can be gutted |
| Blinking LED message light | Always on until Play, or pulse until Play |
| Momentary Play button | Wired to microcontroller / show-control |
| Audio playback | MP3 module, Raspberry Pi, or show-control PC playing `marion-cole-voicemail.wav` |
| Speaker | Built into base, or small external speaker hidden near desk |
| End-of-message signal | GPIO / OSC / MQTT / contact closure → wall intercom + game state "intro_started" |

**Reset between groups:** message light blinking again; Play armed; audio rewound/queued; do not auto-play.

## Possible Mid-Game Use (open — consider during puzzle design)

Confirmed for now: **game start** via Play → Marion Cole. **Not confirmed** that the phone stays one-shot after that.

Worth keeping as a live option when designing puzzles:

- **Inbound call** — phone rings mid-game; someone calls the shop (Dawn? a "customer"? Frank on a different line?). Players answer or let it go to a new message.
- **Outbound call** — players must dial a number found in a clue (parts supplier, "the Don," police non-emergency, etc.) and hear a response or unlock something.
- **Second message** — another blinking message appears later (new voicemail after a gate opens).

If we use any of these, the prop needs: ring sound, answer/hang-up path, dial pad (or fake keypad that accepts one magic number), and show-control hooks beyond "Play once." **Do not gut the phone so hard that ringing/dialing becomes impossible later** — leave headroom in the build even if v1 only implements Play + Marion.

## Do Not Confuse With

Later **evidence** recordings (Tony/"the Don" tapes) should still prefer a **separate** prop (dictaphone/cassette) unless a puzzle specifically wants the shop phone to hold that content.

## Script

See [`../../../01-Story/in-room-text.md`](../../../01-Story/in-room-text.md) — Marion Cole voicemail.

## Status

Concept confirmed as preferred opening. Not built. BOM draft in inventory.
