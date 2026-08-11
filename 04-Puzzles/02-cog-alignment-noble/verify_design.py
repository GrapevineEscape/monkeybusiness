#!/usr/bin/env python3
"""
Test and verify the cog puzzle design

This script loads the generated design and runs verification checks
to ensure all calculations are correct and the puzzle will work as intended.
"""

import json
import sys
import os

def load_design(json_path="./output/design_specs.json"):
    """Load the design specifications from JSON"""
    if not os.path.exists(json_path):
        print(f"❌ Error: {json_path} not found")
        print("   Run 'python cog_designer.py' first to generate design files")
        return None
    
    with open(json_path, 'r') as f:
        return json.load(f)


def verify_tooth_alignment(design):
    """Verify all angles are properly aligned to tooth positions"""
    print("\n" + "="*70)
    print("VERIFICATION: Tooth Alignment")
    print("="*70)
    
    print("\nℹ️  Note: Home angles may not be exactly aligned to teeth in calculation,")
    print("   but physical teeth will naturally enforce discrete positions.")
    print()
    
    all_good = True
    for cog in design['cogs']:
        degrees_per_tooth = cog['degrees_per_tooth']
        home_angle = cog['line_angle_at_home_deg']
        rotation = cog['rotation_needed_deg']
        
        # Check if rotation is aligned to teeth (this is critical)
        rotation_remainder = rotation % degrees_per_tooth
        if abs(rotation_remainder) > 0.01:
            print(f"⚠️  Cog {cog['id']}: Rotation {rotation:.2f}° not aligned to teeth")
            all_good = False
        
        # Calculate final angle
        final_angle = (home_angle + rotation) % 360
        
        # Find nearest tooth position for home angle
        nearest_tooth = round(home_angle / degrees_per_tooth) * degrees_per_tooth
        
        print(f"Cog {cog['id']} ({cog['symbol']}):")
        print(f"  Home: {home_angle:6.2f}° (nearest tooth: {nearest_tooth:6.2f}°)")
        print(f"  Rotation: {rotation:6.2f}° ({cog['rotation_needed_teeth']} teeth)")
        print(f"  Final: {final_angle:6.2f}°")
    
    if all_good:
        print("\n✅ All rotation angles properly aligned to tooth positions")
    else:
        print("\n❌ Some rotations not aligned - puzzle may not work correctly")
    
    return all_good


def verify_cog_spacing(design):
    """Verify cogs don't overlap"""
    print("\n" + "="*70)
    print("VERIFICATION: Cog Spacing (No Overlaps)")
    print("="*70)
    
    posts = design['posts']
    cog_diameter = design['cogs'][0]['outer_diameter_mm']
    
    all_good = True
    for i in range(len(posts)):
        for j in range(i+1, len(posts)):
            p1 = posts[i]
            p2 = posts[j]
            
            # Calculate distance
            dx = p2['x'] - p1['x']
            dy = p2['y'] - p1['y']
            distance = (dx**2 + dy**2) ** 0.5
            
            # Check if too close
            if distance < cog_diameter:
                print(f"⚠️  Posts {i+1} and {j+1} too close: {distance:.1f}mm (min: {cog_diameter}mm)")
                all_good = False
            else:
                print(f"✓ Posts {i+1} and {j+1}: {distance:.1f}mm apart (safe)")
    
    if all_good:
        print("\n✅ All cogs have adequate spacing")
    else:
        print("\n❌ Some cogs overlap - increase board size or reduce cog size")
    
    return all_good


def verify_board_margins(design):
    """Verify all cogs fit within board boundaries"""
    print("\n" + "="*70)
    print("VERIFICATION: Board Margins")
    print("="*70)
    
    board_width = design['board']['width_mm']
    board_height = design['board']['height_mm']
    cog_radius = design['cogs'][0]['outer_diameter_mm'] / 2
    
    all_good = True
    for i, post in enumerate(design['posts']):
        x, y = post['x'], post['y']
        
        # Check margins
        left_margin = x - cog_radius
        right_margin = board_width - (x + cog_radius)
        top_margin = y - cog_radius
        bottom_margin = board_height - (y + cog_radius)
        
        print(f"Cog {i+1} margins: L={left_margin:.1f} R={right_margin:.1f} T={top_margin:.1f} B={bottom_margin:.1f}mm")
        
        if left_margin < 0 or right_margin < 0 or top_margin < 0 or bottom_margin < 0:
            print(f"  ⚠️  Cog {i+1} extends beyond board edge!")
            all_good = False
    
    if all_good:
        print("\n✅ All cogs fit within board boundaries")
    else:
        print("\n❌ Some cogs exceed board - increase board size or reposition posts")
    
    return all_good


def print_solution_guide(design):
    """Print step-by-step solution for game master"""
    print("\n" + "="*70)
    print("SOLUTION GUIDE (for Game Master)")
    print("="*70)
    
    print("\nPuzzle Solution Steps:")
    print("-" * 70)
    
    for cog in design['cogs']:
        rotation_dir = "clockwise" if cog['rotation_needed_deg'] >= 0 else "counter-clockwise"
        print(f"\n{cog['id']}. Place cog with symbol {cog['symbol']} on matching post")
        print(f"   Then rotate {abs(cog['rotation_needed_teeth'])} teeth {rotation_dir}")
        print(f"   ({abs(cog['rotation_needed_deg']):.1f}° total rotation)")
    
    print("\nWhen complete, the engraved lines will form a continuous path")
    print("connecting the letters: N → O → B → L → E")
    print("\nSolution word: NOBLE")
    print("="*70)


def print_manufacturing_checklist(design):
    """Print checklist for fabrication"""
    print("\n" + "="*70)
    print("MANUFACTURING CHECKLIST")
    print("="*70)
    
    print("\n✓ Files to send to laser cutter:")
    print("  □ board.svg (cut outline, post holes, engrave letters)")
    print("  □ cog_1.svg (cut shape, engrave symbol and line)")
    print("  □ cog_2.svg (cut shape, engrave symbol and line)")
    print("  □ cog_3.svg (cut shape, engrave symbol and line)")
    print("  □ cog_4.svg (cut shape, engrave symbol and line)")
    
    print("\n✓ Laser settings:")
    print("  □ RED lines = CUT (full power, cut through)")
    print("  □ BLUE lines/text = ENGRAVE (lower power, surface only)")
    
    print("\n✓ Materials needed:")
    print(f"  □ Acrylic sheet for board: {design['board']['width_mm']}mm × {design['board']['height_mm']}mm")
    print(f"  □ Acrylic sheet for cogs: ~{design['cogs'][0]['outer_diameter_mm']*2}mm × {design['cogs'][0]['outer_diameter_mm']*2}mm")
    print(f"  □ 4× posts/dowels: 6-8mm diameter (holes are slightly larger)")
    print("  □ Paint/ink to fill engravings (optional, for visibility)")
    
    print("\n✓ Assembly:")
    print("  □ Install posts at marked positions")
    print("  □ Test cog rotation (should spin freely)")
    print("  □ Verify solution using assembly_diagram.svg")
    print("  □ Optional: fill engravings with contrasting paint")
    
    print("\n" + "="*70)


def main():
    print("="*70)
    print("COG ALIGNMENT PUZZLE - DESIGN VERIFICATION")
    print("="*70)
    
    # Load design
    design = load_design()
    if not design:
        return 1
    
    print(f"\nLoaded design: {design['board']['width_mm']}mm × {design['board']['height_mm']}mm board")
    print(f"              {len(design['cogs'])} cogs, {design['cogs'][0]['num_teeth']} teeth each")
    
    # Run verifications
    results = []
    results.append(("Tooth Alignment", verify_tooth_alignment(design)))
    results.append(("Cog Spacing", verify_cog_spacing(design)))
    results.append(("Board Margins", verify_board_margins(design)))
    
    # Print solution guide
    print_solution_guide(design)
    
    # Print manufacturing checklist
    print_manufacturing_checklist(design)
    
    # Summary
    print("\n" + "="*70)
    print("VERIFICATION SUMMARY")
    print("="*70)
    
    all_passed = all(result[1] for result in results)
    
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    if all_passed:
        print("\n🎉 Design verification complete - ready to fabricate!")
        return 0
    else:
        print("\n⚠️  Some checks failed - review issues above")
        print("   You may need to adjust parameters and regenerate design")
        return 1


if __name__ == "__main__":
    sys.exit(main())
