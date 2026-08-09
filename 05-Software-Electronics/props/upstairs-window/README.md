# Prop: Fake Upstairs Window (Frank's Watching Eyes)

## Concept (as described)

A fake "upstairs" window, mounted high on a double-height wall near the entrance. Behind cheap metal mini-blinds sits a hidden screen showing a **shadow that roams back and forth**, implying Frank is pacing around up there watching the player. Periodically — timed to the video — the blinds are **forced open by servo motors**, revealing **a pair of bloodshot cartoon eyes** that peer into the room and look around for a second or two. Then the motors retract, the blinds return to their normal closed position, and the shadow resumes moving as if nothing happened.

## Effect Sequence (single loop)

1. Blinds closed. Screen shows a shadow silhouette drifting/pacing behind the blinds (ambient, ongoing).
2. At a scripted moment, the shadow settles toward the center.
3. Servo(s) snap the blind slats open.
4. Screen content switches (or reveals a physical prop) showing large bloodshot cartoon eyes, which "look around" for ~1-2 seconds.
5. Servo(s) release, slats snap back closed.
6. Screen reverts to the ambient pacing shadow. Loop repeats on a timer (with some randomness so it doesn't feel too mechanical) throughout the game.

## Feasibility Verdict

**Feasible.** This is a well-trodden effect in prop-building/haunted-attraction circles (motorizing cheap blinds is a common DIY hack). The main engineering risk is mechanical (reliable, quiet-enough, repeatable blind-tilt actuation over hundreds of cycles), not electronic — the video/trigger sync is the easy part if we drive everything from one controller.

## Proposed Technical Approach

### Reveal method: video-based eyes (recommended over a physical eye prop)

Use the **same hidden screen** for both the pacing shadow and the eyes — when it's time to reveal, the video content itself cuts to a close-up of the eyes rather than needing a separate physical eyeball mechanism. This means one device (a small computer) drives both the visual and the servo trigger, so they're inherently in sync — no cross-system timing to get wrong. A physical eye prop is a possible future upgrade, not needed for v1.

### Controller

A single small computer (e.g. Raspberry Pi) running a looping script that:
- Plays a pre-made video loop (shadow pacing → eyes close-up → shadow resumes) on the hidden screen via HDMI.
- Fires a GPIO signal to a servo (directly, or via a simple driver board) at the exact moments the blinds should snap open and closed.

Because the whole sequence is a fixed, pre-authored loop (not reactive to player behavior), this **does not require real-time video analysis or sensors** — just a script with hard-coded timings matched to the video file. This significantly simplifies the build.

### Blind actuation

Cheap horizontal mini blinds have a tilt rod that normally turns via a wand or twist rod. Recommended v1 approach: **motorize the tilt rod directly with a small servo**, rotating it to snap the slats from closed to open and back. This requires relatively little torque and is the simplest mechanical modification. (A full lift/raise of the entire blind is a flashier but riskier stretch goal — parking it as a "v2" idea.)

### Sound

Consider a short mechanical "snap"/creak sound effect on the reveal, routed through the room's audio system (or a small dedicated speaker) — sells the surprise even if the real servo motion is quiet, and can mask any servo noise.

## Bill of Materials (draft — added to master inventory)

- Small TV/monitor (hidden behind the blinds)
- Cheap metal mini blinds, sized to the screen/window opening
- Servo motor(s) for the tilt rod (start with 1, add a 2nd if slats don't open evenly from one end)
- Small controller (Raspberry Pi or similar) with HDMI out + GPIO
- Mounting frame/enclosure (window casing to hide the screen bezel and mechanism, built to match the garage's set dressing)
- Speaker (if not routed through central audio) for the reveal sound effect

## Open Questions / Risks

- **Ceiling/wall height confirmation** — need actual double-height clearance measurements before finalizing window size/mounting height.
- **Video/graphics production** — need to actually create the shadow-pacing loop and the bloodshot-eyes close-up video asset (art/animation task, not electronics).
- **Mechanical reliability** — how many cycles the servo/tilt-rod linkage needs to survive per event, and across the room's operating life, should drive motor/linkage selection (a beefier micro-servo or geared motor may outlast a cheap hobby servo).
- **Reset/override** — game master should have a manual way to force the blinds closed/reset the loop between groups in case of a mid-cycle malfunction.
- **v2 stretch goal** — full blind lift/raise instead of just tilt, and/or a physical eye prop, if v1 proves too subtle.

## Next Steps

1. Prototype the servo + tilt-rod mechanism alone (no video yet) to prove the physical snap-open/snap-closed motion is reliable and looks/sounds right.
2. Produce a rough placeholder video loop (even a simple animated silhouette + simple eyes) to test full sync end-to-end.
3. Decide final mounting approach once real wall/ceiling measurements are available.

## Status

Concept captured, feasibility assessed as viable. Not yet built or prototyped.
