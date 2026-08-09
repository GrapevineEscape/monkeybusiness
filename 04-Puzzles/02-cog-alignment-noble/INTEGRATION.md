# Puzzle Integration Guide: Cog Alignment → NOBLE

## Story Integration Options

Since your escape room's theme and narrative haven't been fully defined yet for this puzzle, here are several ways to integrate the **Cog Alignment → NOBLE** puzzle into your existing story:

### Option 1: Family Heritage / Nobility Theme
**Justification:** The word "NOBLE" directly references nobility, lineage, or aristocracy.

- **Story hook:** The protagonist's family has a noble lineage that's been hidden or forgotten
- **In-world explanation:** This is a family crest puzzle, a coat of arms cipher, or a test left by an ancestor
- **Placement:** Office or Main area, perhaps in a drawer or safe that contains family documents
- **Cog distribution:** 
  - One cog in a photo album (family history)
  - One in a desk drawer (personal items)
  - One in a locked box (valuables)
  - One hidden behind a picture frame (secrets)

### Option 2: Mechanical Workshop / Repair Manual Theme
**Justification:** Cogs are inherently mechanical and fit workshop/industrial settings.

- **Story hook:** The protagonist or antagonist was an engineer, machinist, or precision craftsperson
- **In-world explanation:** This is a calibration device, a machine timing mechanism, or a repair manual cipher
- **Placement:** Storage area or workshop zone
- **Cog distribution:**
  - In toolboxes (matching the tool symbols: hammer, wrench, gear, etc.)
  - On shelves with other mechanical parts
  - One might be used as a part of another puzzle initially

### Option 3: Precision Ethics / Moral Code Theme
**Justification:** "NOBLE" can mean virtuous, honorable, or morally upright (not just aristocratic).

- **Story hook:** The protagonist was trying to prove their innocence or clear someone's name
- **In-world explanation:** This represents a moral compass or ethical framework that must be "aligned"
- **Placement:** Office area where character does their thinking/planning
- **Cog distribution:** Each cog represents a virtue or principle, distributed where those qualities are demonstrated

### Option 4: Scientific / Research Lab Theme
**Justification:** Precision alignment is central to scientific instruments (microscopes, telescopes, spectrometers).

- **Story hook:** The character was conducting important research or making a discovery
- **In-world explanation:** Optical alignment device, instrument calibration puzzle
- **Placement:** Office or a "research area"
- **Could substitute:** Change symbols to chemical elements, scientific icons, or atomic models

## Puzzle Flow Integration

### Prerequisites (What players need first)
- **Access** to the locations where cogs are hidden
- **Optional:** A clue or document that hints at:
  - The concept of alignment
  - The word "NOBLE" or its meaning
  - Instructions like "When precision aligns, nobility reveals itself"

### Outputs (What this puzzle unlocks)
The solved puzzle reveals **"NOBLE"** which could:

1. **Be a password/code:**
   - Computer password
   - Combination lock word-to-number cipher (N=14, O=15, B=2, L=12, E=5)
   - Safe combination using keypad

2. **Trigger an electronic mechanism:**
   - Use sensors to detect correct alignment (see Electronics section)
   - Open a drawer, door, or container
   - Activate a recording, message, or Frank's intercom

3. **Be thematic information:**
   - Reveals a character trait
   - Part of a larger message: "NOBLE CAUSE", "NOBLE SACRIFICE", "NOBLE INTENTION"
   - Leads to finding something marked with "NOBLE" (Noble Street address, Noble Chemical Co., etc.)

4. **Feed into meta-puzzle:**
   - One of several keywords needed for final solution
   - Part of a larger phrase or sentence

## Recommended Placement in Puzzle Dependency Map

Based on your existing flow structure in `../03-Flow/puzzle-dependency-map.md`:

### Early-to-Mid Game Puzzle
**Rationale:** 
- Requires collecting 4 items (encourages exploration)
- Has clear physical feedback (alignment is visible)
- Not too complex once you understand the mechanic
- Can be bypassed with hints if players struggle

### Parallel Path
This puzzle can run parallel to other puzzles because:
- It's self-contained (doesn't block critical path items)
- Players can collect cogs opportunistically while solving other puzzles
- The board can be accessible from the start, building anticipation

### Suggested Dependencies

**This puzzle REQUIRES:**
- Access to hiding spots (may require solving 1-2 earlier puzzles to unlock areas)

**This puzzle ENABLES:**
- Access to a mid-game location or container
- OR: One of several keywords needed for final puzzle
- OR: Story revelation that changes player interpretation of earlier clues

## Difficulty Tuning

### Base Difficulty: Medium
- **What makes it easier:**
  - Symbols clearly match (no guessing where cogs go)
  - Lines are visible when aligned (clear success state)
  - Limited rotation options (16 positions per cog)
  
- **What makes it harder:**
  - Must find all 4 cogs first
  - Trial-and-error could take time without understanding the goal
  - Lines might be subtle depending on fabrication

### Hints (Progressive Escalation)

**Hint 1** (if players have cogs but aren't trying the board):
- "Those pieces look like they fit on something... have you found anywhere with matching symbols?"

**Hint 2** (if players placed cogs but aren't rotating them):
- "Try rotating the pieces on the board. Pay attention to the engraved lines."

**Hint 3** (if players are rotating but not seeing the connection):
- "When everything is aligned correctly, the lines should form a continuous path."

**Hint 4** (if players aligned lines but don't see letters):
- "What does the path connect? Look at what the line passes through."

**Bypass** (if time is critical):
- Provide a photo showing one or two cogs in correct position
- OR: Give them the word "NOBLE" directly with context

## Electronics Integration (Optional)

If you want to add automated verification or effects:

### Simple Version: Visual Feedback Only
- Manual puzzle, game master observes solution via camera
- OR: Conductive paint on cogs + DIY continuity sensor

### Advanced Version: Full Electronic Detection
See `../../05-Software-Electronics/props/cog-alignment-puzzle/` (to be created if you want this)

**Components needed:**
- 4 rotary encoders or potentiometers (detect cog rotation angle)
- OR: RFID tags on cogs + RFID readers on posts
- Microcontroller (Arduino, Raspberry Pi Pico, ESP32)
- Output device:
  - Solenoid lock to open a drawer/box
  - LED strip that lights up the solution path
  - Sound effect or voice message
  - Signal to other puzzle props

**How it works:**
1. Each post has a sensor that detects cog rotation angle
2. Microcontroller checks if all 4 cogs are at correct angles (with some tolerance)
3. When all aligned, trigger output mechanism

**Cost estimate:** $30-60 in electronics + programming time

## Visual Design Considerations

### Aesthetics
- **Clear acrylic** = modern, clean, puzzle-like (good for abstract/contemporary rooms)
- **Frosted acrylic** = softer, more elegant (good for office/home settings)
- **Wood cogs** = warmer, vintage/industrial feel (requires more precise CNC work)
- **Mixed materials** = acrylic cogs on wood board (nice contrast)

### Engraving Visibility
If lines are hard to see:
- Fill engravings with acrylic paint (contrasting color)
- Use a paint pen or fine-tip marker
- Apply wood stain then wipe surface (stain stays in grooves)
- Backlight the board (LED strip underneath)

### Size Considerations
**Current default:** 400mm × 400mm board (15.7" × 15.7")

- **Larger board (500mm+):** Easier to see, more dramatic, but needs more space
- **Smaller board (300mm):** More compact, but cogs might feel cramped

**Cog size:** 80mm diameter (3.1") is good for:
- Clear visibility of symbols and lines
- Easy manipulation by players
- Not too delicate

## Fabrication Cost Estimate

| Item | Low End | High End |
|------|---------|----------|
| Acrylic sheet | $20 | $50 |
| Laser cutting service | $30 | $100 |
| Posts/hardware | $5 | $15 |
| Paint/finishing | $5 | $15 |
| **Total (basic)** | **$60** | **$180** |
| **+ Electronics (optional)** | **+$50** | **+$150** |

**Time estimate:**
- Design review & customization: 1-2 hours
- Fabrication (outsourced): 3-7 days turnaround
- Assembly & testing: 2-4 hours
- Integration with room: 1-2 hours

## Next Steps

1. **Decide on theme/story integration** (see options above)
2. **Determine placement** in your room layout (see `../../02-Room-Design/`)
3. **Plan cog distribution** strategy (where to hide each cog)
4. **Customize symbols** if needed (edit `cog_designer.py`)
5. **Run design tool** to generate files
6. **Prototype test** with paper cutouts before final fabrication
7. **Order materials** and send SVGs to laser cutter
8. **Assemble and playtest**
9. **Update flow map** in `../../03-Flow/puzzle-dependency-map.md`

## Questions to Consider

- [ ] What symbols fit your theme? (tools, scientific, alchemical, suits, etc.)
- [ ] Should cogs be distributed or kept together?
- [ ] What does "NOBLE" unlock or reveal?
- [ ] Do you want electronic feedback or keep it purely mechanical?
- [ ] Where in the room does this make most sense thematically?
- [ ] Should this be on the critical path or a side quest?
- [ ] What's the story reason this puzzle exists in-world?
