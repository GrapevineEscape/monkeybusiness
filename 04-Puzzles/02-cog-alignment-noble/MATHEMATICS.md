# Mathematical Design Explanation

## Overview

The cog alignment puzzle requires precise calculation of positions and angles to ensure that when all four cogs are correctly rotated, their engraved lines form a continuous path through the letters N-O-B-L-E. This document explains the mathematics behind the design tool.

## Core Concepts

### 1. Coordinate System

The board uses a standard 2D Cartesian coordinate system:
- Origin (0, 0) is at the **top-left** corner
- X-axis increases **rightward**
- Y-axis increases **downward**
- Units: millimeters (mm)

### 2. Angle Convention

Angles are measured in degrees:
- 0° points **right** (positive X direction)
- 90° points **down** (positive Y direction)
- 180° points **left** (negative X direction)
- 270° points **up** (negative Y direction)
- Rotation is **clockwise** (standard for physical objects)

## Design Process

### Step 1: Post Positioning

Four posts must be positioned on the board such that:
1. No two posts are too close (minimum distance = cog diameter)
2. Posts are distributed across the board for visual interest
3. All posts are within safe margins from board edges

**Current implementation** uses a 2×2 grid with asymmetric offsets:

```
Post positions (for 400×400mm board, 80mm cog diameter):
- Post 0: (116, 106) - top-left region
- Post 1: (274, 121) - top-right region
- Post 2: (131, 289) - bottom-left region
- Post 3: (294, 284) - bottom-right region
```

**Formula for minimum distance:**
```
min_distance = cog_diameter
```

### Step 2: Solution Path Design

The solution path is where the aligned lines will form a continuous path. Letters N-O-B-L-E are placed along this path.

**Current implementation** uses a parametric S-curve:

```python
for i in range(5):  # 5 letters
    t = i / 4  # parameter from 0 to 1
    x = start_x + (end_x - start_x) * t
    y = start_y + (end_y - start_y) * t + amplitude * sin(t * π * 2)
```

This creates points:
- N at t=0: (60, 60)
- O at t=0.25: (130, 170)
- B at t=0.5: (200, 200)
- L at t=0.75: (270, 230)
- E at t=1.0: (340, 340)

### Step 3: Line Angle Calculation

For each cog, we need to determine:
1. **Target point**: Where this cog's line should intersect the solution path
2. **Solution angle**: Angle from post to target point (when puzzle is solved)
3. **Home angle**: Angle of line when cog is in starting position (creates the puzzle!)

**Angle from point A to point B:**
```python
angle = atan2(B.y - A.y, B.x - A.x) * (180/π)
```

**Example for Cog 1:**
- Post at (116, 106)
- Target at (95, 115) [midpoint between N and O]
- Solution angle: atan2(115-106, 95-116) = atan2(9, -21) ≈ 156.8°

### Step 4: Tooth Quantization

Cogs have discrete teeth, so rotation angles must snap to tooth positions.

**Degrees per tooth:**
```
θ_tooth = 360° / num_teeth
```

For 16 teeth:
```
θ_tooth = 360° / 16 = 22.5°
```

**Snapping angle to nearest tooth:**
```python
teeth_count = round(angle / θ_tooth)
snapped_angle = teeth_count * θ_tooth
```

### Step 5: Home Position Calculation

To create the puzzle, each cog's line starts at a "home" angle different from the solution angle.

**Offset strategy:**
```python
home_offsets = [45°, -60°, 90°, -30°]  # Different for each cog
line_angle_at_home = solution_angle + home_offset
```

**Rotation needed (before quantization):**
```
rotation_raw = (solution_angle - home_angle) mod 360°
```

**Rotation needed (after quantization):**
```python
teeth_to_rotate = round(rotation_raw / θ_tooth)
rotation_quantized = teeth_to_rotate * θ_tooth
```

**Adjusted home angle (to ensure exact tooth alignment):**
```
adjusted_home = (solution_angle - rotation_quantized) mod 360°
```

## Example Calculation Walkthrough

Let's trace through **Cog #1** in detail:

### Given:
- Board: 400mm × 400mm
- Cog diameter: 80mm
- Teeth: 16 (22.5° per tooth)
- Post position: (116.0, 106.0)

### Step 1: Determine target point
Cog 1 connects path segment N→O:
- N at (60, 60)
- O at (130, 170)
- Target = midpoint = ((60+130)/2, (60+170)/2) = (95, 115)

### Step 2: Calculate solution angle
```
angle = atan2(115 - 106, 95 - 116)
      = atan2(9, -21)
      = 156.80°
```

### Step 3: Apply home offset
```
home_offset = 45°
line_at_home_raw = 156.80° + 45° = 201.80°
```

### Step 4: Calculate rotation needed
```
rotation_needed = (156.80° - 201.80°) mod 360°
                = -45° mod 360°
                = 315°
```

### Step 5: Quantize to teeth
```
teeth_needed = round(315° / 22.5°) = round(14.0) = 14 teeth
rotation_quantized = 14 × 22.5° = 315° (exact!)
```

### Step 6: Adjust home angle for exact alignment
```
adjusted_home = (156.80° - 315°) mod 360°
              = -158.2° mod 360°
              = 201.8°
```

### Final Results for Cog #1:
- **Line angle at HOME:** 201.8°
- **Rotation needed:** 315° (14 teeth clockwise)
- **Final angle at solution:** (201.8° + 315°) mod 360° = 156.8°

## Verification

To verify the design is correct:

### 1. Check tooth alignment
All angles should be multiples of θ_tooth:
```
angle mod θ_tooth ≈ 0
```

### 2. Check solution alignment
When all cogs are rotated to solution position, their lines should:
- Point toward their respective path segments
- Form a visually continuous path
- Pass through or near their assigned letters

### 3. Check physical constraints
- No cog overlap: distance between posts ≥ cog_diameter
- Posts within board: post_position + cog_radius < board_edge
- Lines visible: line_length < cog_radius

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Angle from A to B | `atan2(B.y - A.y, B.x - A.x) × (180/π)` |
| Distance between points | `√[(x₂-x₁)² + (y₂-y₁)²]` |
| Degrees per tooth | `360° / num_teeth` |
| Snap angle to teeth | `round(angle / θ_tooth) × θ_tooth` |
| Rotation needed | `(target_angle - current_angle) mod 360°` |
| Teeth to rotate | `round(rotation_angle / θ_tooth)` |

## Customization Parameters

The design tool exposes these parameters for customization:

| Parameter | Default | Effect | Constraints |
|-----------|---------|--------|-------------|
| `board_width` | 400mm | Horizontal space available | Must fit cogs with margins |
| `board_height` | 400mm | Vertical space available | Must fit cogs with margins |
| `cog_diameter` | 80mm | Size of each cog | Smaller = more compact |
| `num_teeth` | 16 | Rotation resolution | More = finer control, harder to make |
| `post_diameter` | 6mm | Dowel/standoff size | Affects center hole size |

### Difficulty Tuning via Teeth Count

| Teeth | Degrees/Tooth | Difficulty | Notes |
|-------|---------------|------------|-------|
| 12 | 30° | Easy | Large increments, forgiving |
| 16 | 22.5° | Medium | Good balance |
| 20 | 18° | Medium-Hard | Finer control needed |
| 24 | 15° | Hard | Very precise |
| 32 | 11.25° | Very Hard | Expert precision |

## Extending the Design

### Changing the Word

To spell a different word:
1. Change `letters = "NOBLE"` to your word (line 147)
2. Adjust path_points generation for word length
3. Re-run design tool

### Changing Number of Cogs

Currently hardcoded to 4 cogs. To change:
1. Adjust post generation (add/remove positions)
2. Adjust path segment assignments
3. Update symbols list

### Different Path Shapes

Edit the `_design_solution_path()` method to create:
- **Straight line:** Remove sine term
- **Circle:** Use parametric circle equations
- **Zigzag:** Use piecewise linear segments
- **Custom:** Define explicit points

Example for straight diagonal:
```python
x = start_x + (end_x - start_x) * t
y = start_y + (end_y - start_y) * t
```

## Troubleshooting Calculations

**Problem: Cogs overlap**
- Increase `board_size` or decrease `cog_diameter`
- Check: `distance(post_i, post_j) ≥ cog_diameter`

**Problem: Lines don't align in solution**
- Verify all angles are properly quantized to teeth
- Check calculation: `(home_angle + rotation) mod 360° = solution_angle`

**Problem: Letters not on path**
- Adjust solution path amplitude or shape
- Verify letter positions calculated correctly

**Problem: Rotation angles seem wrong**
- Check angle convention (clockwise vs counter-clockwise)
- Verify modulo arithmetic: `-45° mod 360° = 315°`

## Advanced Topics

### Optimization

The current design uses a simple assignment strategy (post → path segment). For optimal aesthetics, you could:

1. **Minimize total line length:** Solve assignment problem
2. **Balance rotation difficulty:** Ensure similar rotation amounts
3. **Maximize visual clarity:** Avoid lines crossing too many times

### Alternative Alignment Detection

Instead of visual alignment, use:
- **Conductive paint:** Lines complete circuit when aligned
- **Optical sensors:** Detect line positions
- **RFID tags:** Detect cog positions and rotations
- **Hall effect sensors:** Magnets at correct positions

### Multi-word Puzzles

Use the same principle for multiple words:
- Each cog set spells one word
- Combine words for final answer
- Example: Four 3-cog sets spelling CODE-BLUE-DOOR-FIVE

## References

- Coordinate geometry: [Standard 2D Cartesian system](https://en.wikipedia.org/wiki/Cartesian_coordinate_system)
- Angle calculations: [atan2 function](https://en.wikipedia.org/wiki/Atan2)
- Modular arithmetic: [Modulo operation](https://en.wikipedia.org/wiki/Modulo_operation)
- Parametric curves: [Parametric equations](https://en.wikipedia.org/wiki/Parametric_equation)
