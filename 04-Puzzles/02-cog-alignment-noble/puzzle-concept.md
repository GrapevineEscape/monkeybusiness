# Puzzle: Cog Alignment → NOBLE

## Summary

Players discover four laser-engraved acrylic cogs, each bearing a unique symbol and an engraved line. By matching symbols on the cogs to corresponding symbols on a board with four posts, players determine where each cog belongs. When all four cogs are placed on their correct posts and rotated to align, the engraved lines form a single continuous path that connects letters spelling **N-O-B-L-E**.

## Story Justification

_(To be determined based on your escape room narrative — could be tied to a character who values precision, a mechanical device, a family crest, industrial heritage, etc.)_

This puzzle fits the **theme-first** philosophy by using a mechanical, tactile interaction that feels intentional and crafted rather than arbitrary. The cogs could represent:
- A precision instrument or gauge repair manual
- A family lineage or coat of arms ("NOBLE" bloodline)
- A mechanical safe or vault locking mechanism
- An industrial blueprint or schematic

## Player Experience (Step by Step)

1. **Discovery**: Players find four acrylic cogs scattered in different locations (or in a container). Each cog has:
   - A unique symbol engraved on it (e.g., hammer, wrench, gear, star)
   - A line engraved through the cog face
   - Teeth around the edge allowing rotation

2. **Initial Observation**: Players notice a board (wooden or acrylic) with:
   - Four posts/pins positioned at specific locations
   - Symbols marked near each post that match the cog symbols
   - Letters (N, O, B, L, E) scattered around the board

3. **Placement**: Players match each cog to its corresponding post by symbol. The cogs fit loosely enough to rotate but stay in place.

4. **Alignment Challenge**: Players experiment with rotating the cogs, eventually noticing that the engraved lines can connect.

5. **Aha Moment**: When all cogs are rotated correctly, the four lines form one continuous path that passes through/connects to letters in sequence: N → O → B → L → E.

6. **Outcome**: The word "NOBLE" is revealed as the solution (could be a code, a password, a keyword for another puzzle, or trigger an electronic mechanism).

## Solution Mechanism

### Physical Components

**Board:**
- Rigid acrylic or wood base (~12" × 12" to 18" × 18")
- Four posts (dowels or standoffs) at calculated positions
- Letters N, O, B, L, E engraved or adhered at specific positions
- Symbols engraved near each post for cog matching

**Cogs:**
- 4 circular acrylic pieces (3mm-6mm thick)
- Diameter: ~3-4" each
- Teeth around perimeter (12-24 teeth per cog for discrete rotation positions)
- Center hole sized to fit loosely on posts for easy rotation
- Each cog has:
  - Unique matching symbol engraved
  - Line engraved from center outward (or across the face) at a specific angle
  - Optional: small alignment markers or dots

### Mathematical Design

The design requires precise calculation of:
1. **Post positions** on the board (4 positions in 2D space)
2. **Letter positions** (N, O, B, L, E) on the board
3. **Number of teeth** per cog (determines rotational resolution)
4. **Line angles** on each cog when in "home" position
5. **Correct rotation angle** for each cog to achieve alignment

**Key Constraints:**
- All lines must be aligned (form a continuous path) in the solution state
- The path must intersect/pass through the letters N-O-B-L-E in sequence
- Each cog must have a unique correct rotation position
- The puzzle should be solvable but not immediately obvious

**Design Tool:**
See `cog_designer.py` in this folder for a Python script that calculates:
- Optimal post positions
- Line angles and orientations  
- Manufacturing specifications for laser cutting
- SVG output for fabrication

## Location

- **Zone:** _(To be determined — Storage, Office, or distributed?)_
- **Container(s):** 
  - Cogs could be scattered: one in a drawer, one in a toolbox, one on a shelf, one inside another puzzle container
  - Board could be mounted on a wall, stored in the office, or hidden behind another element

## Inputs / Outputs (for Flow map)

- **Requires (from other puzzles/story):**
  - Access to the locations where cogs are hidden
  - Possibly a clue that hints at the word NOBLE or the concept of alignment
  
- **Produces (feeds into):**
  - The word "NOBLE" as output
  - Could unlock: a combination lock, a computer password, a drawer code, or trigger an electronic release
  
- **Branch notes:** 
  - Players might try forcing cogs onto wrong posts (design should make wrong posts obviously incorrect via symbol mismatch)
  - If stuck, hint could reveal "look at the symbols" or "align the lines"
  - Mid-difficulty: could include a partial solution card showing one cog in correct position

## Materials / Build Notes

| Item | Purpose | Estimated Cost | Source |
|---|---|---|---|
| Clear or frosted acrylic sheet (1/4" or 3mm) | Board base | $20-40 | Local plastics supplier or online |
| Clear acrylic (3-6mm thick, ~12" × 12") | Four cogs | $15-30 | Same source |
| Wooden dowels or metal standoffs (4 pcs) | Posts for cog mounting | $5-10 | Hardware store |
| Laser cutting/engraving service | Cut cogs with teeth, engrave symbols and lines | $40-80 | Local makerspace or online service (Ponoko, SendCutSend) |
| Small washers or spacers (optional) | Keep cogs elevated and freely rotating | $2-5 | Hardware store |

**Fabrication Steps:**
1. Run `cog_designer.py` to generate SVG files for laser cutting
2. Send SVG files to laser cutter with material specs:
   - Cut profile for cog outlines and teeth
   - Engrave profile for symbols, lines, and letters
3. Drill holes in board for posts at calculated positions
4. Install posts (glue dowels or screw in standoffs)
5. Test fit cogs and ensure smooth rotation

**Assembly:**
- Posts should allow cogs to rotate freely but not wobble excessively
- Consider adding small felt pads on the underside of cogs to reduce friction
- If using clear acrylic, consider backlighting the board for dramatic effect

## Electronics/Software (if applicable)

**Optional Enhancements:**
- **Electronic verification**: RFID tags or conductive paint on cogs, sensors on posts to detect correct alignment → trigger a solenoid lock, LED indicator, or audio cue
- **Lighting**: LED strip around board perimeter or underneath to highlight the aligned line path
- **Integration**: Output signal could unlock a drawer, activate another prop, or send a message to Frank's intercom

If implementing electronics, see: `../../05-Software-Electronics/props/[puzzle-name]/`

## Difficulty & Fail-Safes

- **Estimated solve time:** 5-8 minutes once all cogs are collected (assuming distributed discovery adds 5-10 min)
  
- **Hint escalation:**
  1. "Look closely at the symbols on both the cogs and the board"
  2. "Try rotating the cogs once they're placed — pay attention to the engraved lines"
  3. "The lines should form a continuous path that connects letters"

- **Reset procedure:** 
  - Spin all cogs to random positions
  - If cogs are distributed, replace them in original hiding spots
  
- **Mid-game assist bypass candidate?** **Yes** — if team is struggling:
  - Provide a photo or card showing one or two cogs in their correct rotational positions
  - Provide the word "NOBLE" directly with context ("this is the alignment word")

## Open Questions / Risks

1. **Number of teeth per cog:** More teeth = finer rotation control but harder to manufacture precisely. 12 teeth (30° increments) is a good starting point; 16 or 24 teeth possible.

2. **Line visibility:** Engraved lines on clear acrylic might be hard to see. Options:
   - Use frosted/colored acrylic
   - Fill engravings with paint or ink
   - Backlight the board

3. **Cog size and board layout:** Need to ensure cogs don't overlap when placed on posts. The Python tool will calculate safe spacing.

4. **Ambiguity in "continuous line":** Players need to understand what "aligned" means. Consider:
   - Making the lines bold/obvious
   - Adding small dots or arrows at line endpoints
   - Including a clue that mentions "continuous path" or "connect the letters"

5. **Theme integration:** What symbols should be on the cogs? Should match the story:
   - Tools (hammer, saw, wrench, screwdriver) if in a workshop setting
   - Suits (hearts, spades, clubs, diamonds) if tied to a game/gambling theme
   - Alchemical/scientific symbols if tied to a laboratory
   - Family crests/heraldry if tied to nobility theme

6. **Distribution strategy:** Where should the four cogs be hidden?
   - All together (easier, faster)
   - Distributed (forces exploration, creates mini-goals)
   - Some locked behind other puzzles (creates dependencies)

---

**Next Steps:**
- [ ] Determine story context and theme for symbols
- [ ] Run `cog_designer.py` to generate initial layout
- [ ] Review calculated positions and adjust parameters
- [ ] Create laser cutting files (SVG)
- [ ] Source materials
- [ ] Test prototype with paper cutouts before final fabrication
