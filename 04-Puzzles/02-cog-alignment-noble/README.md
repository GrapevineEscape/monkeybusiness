# Cog Alignment Puzzle → NOBLE

## Quick Start

This folder contains everything you need to design and fabricate the cog alignment puzzle.

### Files

- **`puzzle-concept.md`** - Complete puzzle design documentation (read this first!)
- **`cog_designer.py`** - Python tool to calculate positions and generate laser cutting files
- **`output/`** - Generated SVG files for manufacturing (created when you run the designer)

### Running the Designer

1. **Generate the design files:**

```bash
cd 04-Puzzles/02-cog-alignment-noble
python cog_designer.py
```

This will create an `output/` directory with:
- `board.svg` - Board with post holes and letter positions
- `cog_1.svg`, `cog_2.svg`, `cog_3.svg`, `cog_4.svg` - Individual cog designs
- `assembly_diagram.svg` - Solution reference showing correct alignment
- `design_specs.json` - All measurements and angles in JSON format

2. **Customize the design (optional):**

```bash
python cog_designer.py \
  --board-width 450 \
  --board-height 450 \
  --cog-diameter 90 \
  --num-teeth 24 \
  --output-dir ./custom_output
```

### Design Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--board-width` | 400mm | Width of the board |
| `--board-height` | 400mm | Height of the board |
| `--cog-diameter` | 80mm | Diameter of each cog |
| `--num-teeth` | 16 | Number of teeth per cog (determines rotation resolution) |
| `--output-dir` | ./output | Where to save SVG files |

**Tip:** More teeth = finer rotation control but more complex to manufacture. 12-24 teeth is recommended.

### Understanding the Design

#### How It Works

1. Four posts are positioned on the board at calculated locations
2. Each cog has:
   - A unique symbol (⚙, 🔧, 🔨, ⭐) that matches a symbol on the board
   - An engraved line at a specific "home" angle
   - Teeth around the edge for discrete rotation
3. When placed on the correct post and rotated to the solution position, all four lines align to form a continuous path
4. This path passes through letters spelling **N-O-B-L-E**

#### The Math

The designer calculates:
- **Post positions**: Placed in a roughly rectangular pattern with offsets for visual interest
- **Solution path**: A gentle curve through the board where the letters N-O-B-L-E are positioned
- **Line angles**: Each cog's line angle is calculated so that when rotated correctly, it points toward its segment of the solution path
- **Home positions**: Lines are intentionally offset from the solution angle to create the puzzle
- **Tooth alignment**: All angles snap to tooth positions (e.g., with 16 teeth, angles are multiples of 22.5°)

### Fabrication Instructions

#### Materials Needed
- Clear or frosted acrylic sheet (3-6mm thick)
- Access to a laser cutter/engraver
- Wooden dowels or metal standoffs for posts (6mm diameter recommended)
- Paint or ink to fill engravings (optional, for better visibility)

#### Laser Cutting Setup

**In your laser cutter software:**
1. Import the SVG files
2. Set layer colors:
   - **RED lines** = CUT (full power, cut through)
   - **BLUE lines/text** = ENGRAVE (lower power, surface engraving)
3. Material settings: Acrylic, 3-6mm thickness
4. Do a test cut on scrap material first!

**Engraving depth:**
- 0.5-1.0mm deep for lines and text
- If lines are hard to see, fill with contrasting acrylic paint

#### Assembly

1. Cut the board and drill holes for posts at marked positions
2. Install posts (glue dowels or screw in standoffs)
3. Cut all four cogs
4. Test fit - cogs should rotate freely on posts without wobbling
5. Optional: Add felt pads under cogs to reduce friction
6. Optional: Backlight the board with LED strips for dramatic effect

### Testing Your Puzzle

1. **Check the assembly diagram** (`assembly_diagram.svg`) to see the solution state
2. Place each cog on its matching post (by symbol)
3. Rotate each cog according to the "rotation needed" value in the console output
4. Verify that all lines align to form a continuous path through N-O-B-L-E

### Customization Ideas

#### Change the Word
Edit `cog_designer.py` around line 147 to change `letters = "NOBLE"` to any 5-letter word.

#### Change the Symbols
Edit line 49 to use different symbols:
```python
self.symbols = ["⚙", "🔧", "🔨", "⭐"]  # Change these!
```

#### Adjust Complexity
- **Easier**: Fewer teeth (12) = larger rotation increments
- **Harder**: More teeth (24) = finer control needed

#### Add Electronics
Consider adding:
- RFID tags on cogs + readers on posts to detect correct placement
- Reed switches + magnets to detect correct rotation
- LED strips that light up when puzzle is solved
- Solenoid lock that releases when solved

See `../../05-Software-Electronics/` for integration examples.

## Troubleshooting

**Lines are hard to see:**
- Fill engravings with paint/ink
- Use frosted acrylic instead of clear
- Add backlighting

**Cogs don't rotate smoothly:**
- Increase hole diameter (edit `post_diameter` parameter)
- Sand the edges of the center holes
- Add washers or spacers between cog and board

**Solution isn't clear:**
- Make sure engraved lines are visible (see above)
- Consider adding arrows or dots at line endpoints
- Include a clue card that mentions "align the lines"

**Posts are too close together:**
- Increase board size
- Decrease cog diameter
- Run designer with different parameters

## Questions or Issues?

Refer back to `puzzle-concept.md` for full design rationale and story integration ideas.
