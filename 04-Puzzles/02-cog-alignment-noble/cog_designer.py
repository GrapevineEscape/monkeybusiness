#!/usr/bin/env python3
"""
Cog Alignment Puzzle Designer
==============================

This tool calculates the precise positions, angles, and dimensions needed to 
fabricate a rotational alignment puzzle where four cogs must be correctly 
positioned and rotated to spell out "NOBLE" with aligned engraved lines.

Mathematical Approach:
----------------------
1. Define 4 post positions on the board in 2D space
2. Define a "solution path" that passes through positions where letters N-O-B-L-E will be placed
3. Calculate the angle from each post position to where its line should intersect the path
4. Design cogs with appropriate number of teeth (determining rotation resolution)
5. Generate SVG files for laser cutting/engraving

Usage:
------
    python cog_designer.py [--preview] [--output-dir ./output]

Author: Cog Puzzle Designer v1.0
"""

import argparse
import json
import math
import sys
from dataclasses import dataclass, asdict
from typing import List, Tuple, Optional
import os


@dataclass
class Point:
    """2D point in mm"""
    x: float
    y: float
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def distance_to(self, other: 'Point') -> float:
        """Euclidean distance to another point"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def angle_to(self, other: 'Point') -> float:
        """Angle in degrees from this point to another (0° = right, 90° = up)"""
        dx = other.x - self.x
        dy = other.y - self.y
        return math.degrees(math.atan2(dy, dx))
    
    def to_tuple(self) -> Tuple[float, float]:
        return (self.x, self.y)


@dataclass
class Cog:
    """Represents a single cog with its properties"""
    id: int
    post_position: Point
    symbol: str
    num_teeth: int
    outer_diameter: float  # mm
    inner_diameter: float  # mm (center hole)
    line_angle_at_home: float  # degrees, angle of engraved line when cog is at "home" position
    solution_angle: float  # degrees, rotation needed from home to reach solution
    line_length: float  # mm, length of engraved line from center


@dataclass
class BoardDesign:
    """Complete puzzle board design specification"""
    board_width: float  # mm
    board_height: float  # mm
    posts: List[Point]
    letters: List[Tuple[Point, str]]  # (position, letter)
    cogs: List[Cog]
    solution_path: List[Point]  # The continuous line path through N-O-B-L-E


class CogPuzzleDesigner:
    """Main designer class for the cog alignment puzzle"""
    
    def __init__(self, 
                 board_size: Tuple[float, float] = (400, 400),  # mm
                 cog_diameter: float = 80.0,  # mm
                 num_teeth: int = 16,
                 post_diameter: float = 6.0):  # mm
        
        self.board_width, self.board_height = board_size
        self.cog_diameter = cog_diameter
        self.cog_radius = cog_diameter / 2.0
        self.num_teeth = num_teeth
        self.post_diameter = post_diameter
        self.post_hole_diameter = post_diameter + 1.0  # slightly larger for smooth rotation
        
        # Symbols to use on cogs (can be customized)
        self.symbols = ["⚙", "🔧", "🔨", "⭐"]  # Gear, wrench, hammer, star
        
    def design_puzzle(self) -> BoardDesign:
        """
        Main design method - calculates all positions and angles
        """
        print("🔧 Designing cog alignment puzzle...")
        print(f"   Board: {self.board_width}mm × {self.board_height}mm")
        print(f"   Cog diameter: {self.cog_diameter}mm")
        print(f"   Number of teeth per cog: {self.num_teeth}")
        print(f"   Rotation resolution: {360/self.num_teeth}° per tooth\n")
        
        # Step 1: Position the 4 posts
        posts = self._calculate_post_positions()
        print(f"✓ Post positions calculated")
        
        # Step 2: Design the solution path (where the aligned lines will form)
        solution_path, letters = self._design_solution_path()
        print(f"✓ Solution path designed through letters: N-O-B-L-E")
        
        # Step 3: Calculate line angles for each cog
        cogs = self._design_cogs(posts, solution_path)
        print(f"✓ Cog specifications calculated\n")
        
        return BoardDesign(
            board_width=self.board_width,
            board_height=self.board_height,
            posts=posts,
            letters=letters,
            cogs=cogs,
            solution_path=solution_path
        )
    
    def _calculate_post_positions(self) -> List[Point]:
        """
        Calculate positions for the 4 posts
        Strategy: Place posts in a roughly rectangular pattern with some offset
        to make the puzzle more interesting
        """
        # Use a grid with offsets for visual interest
        margin = self.cog_diameter * 1.2  # Minimum margin from edge
        
        # Create a 2x2 grid with some asymmetry
        posts = [
            Point(margin + 20, margin + 10),  # Top-left (slightly offset)
            Point(self.board_width - margin - 30, margin + 25),  # Top-right
            Point(margin + 35, self.board_height - margin - 15),  # Bottom-left
            Point(self.board_width - margin - 10, self.board_height - margin - 20),  # Bottom-right
        ]
        
        # Verify no overlap
        for i, p1 in enumerate(posts):
            for j, p2 in enumerate(posts):
                if i < j:
                    dist = p1.distance_to(p2)
                    if dist < self.cog_diameter:
                        print(f"⚠️  WARNING: Posts {i} and {j} are too close ({dist:.1f}mm)")
        
        return posts
    
    def _design_solution_path(self) -> Tuple[List[Point], List[Tuple[Point, str]]]:
        """
        Design the path that the aligned lines will form, placing letters N-O-B-L-E
        Strategy: Create a smooth path (could be a curve, zigzag, or organic shape)
        """
        # Create a gently curved path from top-left to bottom-right
        # The path will have 5 key points where letters will be placed
        
        start_x = 60
        start_y = 60
        end_x = self.board_width - 60
        end_y = self.board_height - 60
        
        # Generate 5 points along a gentle S-curve
        letters = "NOBLE"
        path_points = []
        letter_positions = []
        
        for i, letter in enumerate(letters):
            t = i / (len(letters) - 1)  # Parameter from 0 to 1
            
            # S-curve formula
            x = start_x + (end_x - start_x) * t
            y = start_y + (end_y - start_y) * t + 40 * math.sin(t * math.pi * 2)
            
            point = Point(x, y)
            path_points.append(point)
            letter_positions.append((point, letter))
        
        return path_points, letter_positions
    
    def _design_cogs(self, posts: List[Point], solution_path: List[Point]) -> List[Cog]:
        """
        Design each cog with proper line angles
        Strategy: For each post, determine which segment of the solution path
        it should connect to, then calculate the required line angle
        """
        cogs = []
        
        # Assign each post to a segment of the solution path
        # We'll use a simple nearest-neighbor approach for this example
        # In a real design, you'd want to manually curate this for best aesthetics
        
        assignments = [
            (0, 0, 1),  # Post 0 connects to path segment N→O
            (1, 1, 2),  # Post 1 connects to path segment O→B
            (2, 2, 3),  # Post 2 connects to path segment B→L
            (3, 3, 4),  # Post 3 connects to path segment L→E
        ]
        
        for cog_id, (post_idx, path_start_idx, path_end_idx) in enumerate(assignments):
            post = posts[post_idx]
            path_start = solution_path[path_start_idx]
            path_end = solution_path[path_end_idx]
            
            # Calculate where this cog's line should intersect the path
            # Use the midpoint of the path segment for simplicity
            target_point = Point(
                (path_start.x + path_end.x) / 2,
                (path_start.y + path_end.y) / 2
            )
            
            # Calculate angle from post to target point
            solution_line_angle = post.angle_to(target_point)
            
            # Set "home" position to a different angle (this creates the puzzle!)
            # We'll offset each cog by a different amount
            home_offsets = [45, -60, 90, -30]  # degrees
            line_angle_at_home = solution_line_angle + home_offsets[cog_id]
            
            # Calculate how much rotation is needed (in tooth increments)
            rotation_needed = (solution_line_angle - line_angle_at_home) % 360
            
            # Round to nearest tooth position
            degrees_per_tooth = 360 / self.num_teeth
            teeth_to_rotate = round(rotation_needed / degrees_per_tooth)
            solution_angle = teeth_to_rotate * degrees_per_tooth
            
            # Adjusted home angle to match tooth positions exactly
            adjusted_home_angle = (solution_line_angle - solution_angle) % 360
            
            cog = Cog(
                id=cog_id,
                post_position=post,
                symbol=self.symbols[cog_id],
                num_teeth=self.num_teeth,
                outer_diameter=self.cog_diameter,
                inner_diameter=self.post_hole_diameter,
                line_angle_at_home=adjusted_home_angle,
                solution_angle=solution_angle,
                line_length=self.cog_radius * 0.8  # Line extends 80% to edge
            )
            
            cogs.append(cog)
        
        return cogs
    
    def print_design_summary(self, design: BoardDesign):
        """Print a human-readable summary of the design"""
        print("=" * 70)
        print("COG ALIGNMENT PUZZLE - DESIGN SPECIFICATION")
        print("=" * 70)
        print()
        print(f"Board Dimensions: {design.board_width}mm × {design.board_height}mm")
        print()
        print("POST POSITIONS (from top-left corner):")
        print("-" * 70)
        for i, post in enumerate(design.posts):
            print(f"  Post {i+1}: X={post.x:6.1f}mm, Y={post.y:6.1f}mm")
        print()
        
        print("LETTER POSITIONS:")
        print("-" * 70)
        for pos, letter in design.letters:
            print(f"  {letter}: X={pos.x:6.1f}mm, Y={pos.y:6.1f}mm")
        print()
        
        print("COG SPECIFICATIONS:")
        print("-" * 70)
        for cog in design.cogs:
            print(f"  Cog #{cog.id + 1} (Symbol: {cog.symbol})")
            print(f"    • Post position: ({cog.post_position.x:.1f}, {cog.post_position.y:.1f})mm")
            print(f"    • Diameter: {cog.outer_diameter}mm")
            print(f"    • Teeth: {cog.num_teeth} ({360/cog.num_teeth:.1f}° per tooth)")
            print(f"    • Line angle at HOME: {cog.line_angle_at_home:.1f}°")
            print(f"    • Rotation needed: {cog.solution_angle:.1f}° ({int(cog.solution_angle/(360/cog.num_teeth))} teeth)")
            print(f"    • Line length: {cog.line_length:.1f}mm")
            print()
        
        print("MANUFACTURING NOTES:")
        print("-" * 70)
        print(f"  • Material: 3-6mm clear or frosted acrylic")
        print(f"  • Post holes: {design.cogs[0].inner_diameter:.1f}mm diameter")
        print(f"  • Engrave depth: 0.5-1.0mm (adjust for visibility)")
        print(f"  • Consider filling engravings with contrasting paint")
        print("=" * 70)
        print()
    
    def generate_svg(self, design: BoardDesign, output_dir: str = "./output"):
        """Generate SVG files for laser cutting"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate board SVG
        board_svg = self._generate_board_svg(design)
        board_path = os.path.join(output_dir, "board.svg")
        with open(board_path, 'w') as f:
            f.write(board_svg)
        print(f"✓ Board SVG saved: {board_path}")
        
        # Generate individual cog SVGs
        for cog in design.cogs:
            cog_svg = self._generate_cog_svg(cog)
            cog_path = os.path.join(output_dir, f"cog_{cog.id + 1}.svg")
            with open(cog_path, 'w') as f:
                f.write(cog_svg)
            print(f"✓ Cog #{cog.id + 1} SVG saved: {cog_path}")
        
        # Generate assembly diagram
        assembly_svg = self._generate_assembly_diagram(design)
        assembly_path = os.path.join(output_dir, "assembly_diagram.svg")
        with open(assembly_path, 'w') as f:
            f.write(assembly_svg)
        print(f"✓ Assembly diagram saved: {assembly_path}")
        
    def _generate_board_svg(self, design: BoardDesign) -> str:
        """Generate SVG for the board with post holes and letters"""
        svg_parts = [
            f'<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{design.board_width}mm" height="{design.board_height}mm" viewBox="0 0 {design.board_width} {design.board_height}">',
            f'  <!-- Board outline (CUT) -->',
            f'  <rect x="0" y="0" width="{design.board_width}" height="{design.board_height}" fill="none" stroke="red" stroke-width="0.1"/>',
            f'',
            f'  <!-- Post holes (CUT) -->',
        ]
        
        for i, post in enumerate(design.posts):
            hole_radius = design.cogs[0].inner_diameter / 2
            svg_parts.append(f'  <circle cx="{post.x}" cy="{post.y}" r="{hole_radius}" fill="none" stroke="red" stroke-width="0.1"/>')
            svg_parts.append(f'  <!-- Post {i+1} at ({post.x:.1f}, {post.y:.1f}) -->')
        
        svg_parts.append(f'')
        svg_parts.append(f'  <!-- Letters (ENGRAVE) -->')
        
        for pos, letter in design.letters:
            svg_parts.append(f'  <text x="{pos.x}" y="{pos.y}" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle" fill="blue" stroke="none">{letter}</text>')
        
        svg_parts.append(f'')
        svg_parts.append(f'  <!-- Solution path (reference only - not cut) -->')
        svg_parts.append(f'  <polyline points="')
        
        for point in design.solution_path:
            svg_parts.append(f'    {point.x},{point.y}')
        
        svg_parts.append(f'  " fill="none" stroke="gray" stroke-width="0.5" stroke-dasharray="2,2" opacity="0.3"/>')
        svg_parts.append(f'</svg>')
        
        return '\n'.join(svg_parts)
    
    def _generate_cog_svg(self, cog: Cog) -> str:
        """Generate SVG for a single cog"""
        # Center the cog in its own coordinate space
        center_x = cog.outer_diameter + 20
        center_y = cog.outer_diameter + 20
        canvas_size = (cog.outer_diameter + 40) * 2
        
        svg_parts = [
            f'<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_size}mm" height="{canvas_size}mm" viewBox="0 0 {canvas_size} {canvas_size}">',
            f'  <!-- Cog {cog.id + 1} - Symbol: {cog.symbol} -->',
            f'',
        ]
        
        # Draw the gear teeth
        outer_radius = cog.outer_diameter / 2
        inner_radius = outer_radius * 0.9  # Tooth depth
        tooth_angle = 360 / cog.num_teeth
        
        # Generate gear path
        path_points = []
        for i in range(cog.num_teeth):
            angle_start = math.radians(i * tooth_angle)
            angle_mid = math.radians(i * tooth_angle + tooth_angle / 2)
            angle_end = math.radians((i + 1) * tooth_angle)
            
            # Outer arc
            x1 = center_x + outer_radius * math.cos(angle_start)
            y1 = center_y + outer_radius * math.sin(angle_start)
            
            x2 = center_x + outer_radius * math.cos(angle_mid)
            y2 = center_y + outer_radius * math.sin(angle_mid)
            
            # Inner point (valley)
            x3 = center_x + inner_radius * math.cos(angle_mid)
            y3 = center_y + inner_radius * math.sin(angle_mid)
            
            if i == 0:
                path_points.append(f"M {x1:.2f},{y1:.2f}")
            
            path_points.append(f"L {x2:.2f},{y2:.2f}")
            path_points.append(f"L {x3:.2f},{y3:.2f}")
        
        path_points.append("Z")
        
        svg_parts.append(f'  <!-- Cog outline with teeth (CUT) -->')
        svg_parts.append(f'  <path d="{" ".join(path_points)}" fill="none" stroke="red" stroke-width="0.1"/>')
        
        # Center hole
        hole_radius = cog.inner_diameter / 2
        svg_parts.append(f'')
        svg_parts.append(f'  <!-- Center hole (CUT) -->')
        svg_parts.append(f'  <circle cx="{center_x}" cy="{center_y}" r="{hole_radius}" fill="none" stroke="red" stroke-width="0.1"/>')
        
        # Engraved line at HOME position
        line_angle_rad = math.radians(cog.line_angle_at_home)
        line_end_x = center_x + cog.line_length * math.cos(line_angle_rad)
        line_end_y = center_y + cog.line_length * math.sin(line_angle_rad)
        
        svg_parts.append(f'')
        svg_parts.append(f'  <!-- Engraved line (ENGRAVE) - at HOME position: {cog.line_angle_at_home:.1f}° -->')
        svg_parts.append(f'  <line x1="{center_x}" y1="{center_y}" x2="{line_end_x}" y2="{line_end_y}" stroke="blue" stroke-width="1"/>')
        
        # Symbol (engrave)
        svg_parts.append(f'')
        svg_parts.append(f'  <!-- Symbol (ENGRAVE) -->')
        svg_parts.append(f'  <text x="{center_x}" y="{center_y - cog.line_length/2}" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle" fill="blue">{cog.symbol}</text>')
        
        # Add reference marks
        svg_parts.append(f'')
        svg_parts.append(f'  <!-- Reference: rotation needed = {cog.solution_angle:.1f}° ({int(cog.solution_angle/(360/cog.num_teeth))} teeth clockwise) -->')
        
        svg_parts.append(f'</svg>')
        
        return '\n'.join(svg_parts)
    
    def _generate_assembly_diagram(self, design: BoardDesign) -> str:
        """Generate an assembly/solution diagram showing correct positions"""
        svg_parts = [
            f'<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{design.board_width}mm" height="{design.board_height}mm" viewBox="0 0 {design.board_width} {design.board_height}">',
            f'  <!-- ASSEMBLY DIAGRAM - Shows solution state -->',
            f'  <rect x="0" y="0" width="{design.board_width}" height="{design.board_height}" fill="white" stroke="black" stroke-width="1"/>',
            f'',
        ]
        
        # Draw solution path
        svg_parts.append(f'  <!-- Solution path -->')
        svg_parts.append(f'  <polyline points="')
        for point in design.solution_path:
            svg_parts.append(f'    {point.x},{point.y}')
        svg_parts.append(f'  " fill="none" stroke="green" stroke-width="2"/>')
        svg_parts.append(f'')
        
        # Draw letters
        for pos, letter in design.letters:
            svg_parts.append(f'  <circle cx="{pos.x}" cy="{pos.y}" r="8" fill="lightgreen"/>')
            svg_parts.append(f'  <text x="{pos.x}" y="{pos.y + 4}" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle">{letter}</text>')
        
        svg_parts.append(f'')
        
        # Draw cogs in solution position
        for cog in design.cogs:
            post = cog.post_position
            outer_radius = cog.outer_diameter / 2
            
            # Draw cog circle
            svg_parts.append(f'  <!-- Cog {cog.id + 1} at solution position -->')
            svg_parts.append(f'  <circle cx="{post.x}" cy="{post.y}" r="{outer_radius}" fill="none" stroke="blue" stroke-width="1" opacity="0.5"/>')
            
            # Draw line in SOLUTION position
            solution_angle_rad = math.radians(cog.line_angle_at_home + cog.solution_angle)
            line_end_x = post.x + cog.line_length * math.cos(solution_angle_rad)
            line_end_y = post.y + cog.line_length * math.sin(solution_angle_rad)
            
            svg_parts.append(f'  <line x1="{post.x}" y1="{post.y}" x2="{line_end_x}" y2="{line_end_y}" stroke="red" stroke-width="2"/>')
            
            # Draw symbol
            svg_parts.append(f'  <text x="{post.x}" y="{post.y - outer_radius - 5}" font-family="Arial" font-size="14" text-anchor="middle">{cog.symbol}</text>')
        
        svg_parts.append(f'</svg>')
        
        return '\n'.join(svg_parts)
    
    def save_design_json(self, design: BoardDesign, output_dir: str = "./output"):
        """Save design as JSON for reference"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Convert design to dict
        design_dict = {
            "board": {
                "width_mm": design.board_width,
                "height_mm": design.board_height,
            },
            "posts": [{"x": p.x, "y": p.y} for p in design.posts],
            "letters": [{"x": pos.x, "y": pos.y, "letter": letter} for pos, letter in design.letters],
            "cogs": [
                {
                    "id": cog.id + 1,
                    "symbol": cog.symbol,
                    "post_position": {"x": cog.post_position.x, "y": cog.post_position.y},
                    "outer_diameter_mm": cog.outer_diameter,
                    "num_teeth": cog.num_teeth,
                    "degrees_per_tooth": 360 / cog.num_teeth,
                    "line_angle_at_home_deg": cog.line_angle_at_home,
                    "rotation_needed_deg": cog.solution_angle,
                    "rotation_needed_teeth": int(cog.solution_angle / (360 / cog.num_teeth)),
                    "line_length_mm": cog.line_length,
                }
                for cog in design.cogs
            ]
        }
        
        json_path = os.path.join(output_dir, "design_specs.json")
        with open(json_path, 'w') as f:
            json.dump(design_dict, f, indent=2)
        
        print(f"✓ Design specifications saved: {json_path}")


def main():
    parser = argparse.ArgumentParser(description="Design a cog alignment puzzle")
    parser.add_argument("--board-width", type=float, default=400, help="Board width in mm (default: 400)")
    parser.add_argument("--board-height", type=float, default=400, help="Board height in mm (default: 400)")
    parser.add_argument("--cog-diameter", type=float, default=80, help="Cog diameter in mm (default: 80)")
    parser.add_argument("--num-teeth", type=int, default=16, help="Number of teeth per cog (default: 16)")
    parser.add_argument("--output-dir", type=str, default="./output", help="Output directory for SVG files")
    parser.add_argument("--no-svg", action="store_true", help="Skip SVG generation")
    
    args = parser.parse_args()
    
    # Create designer
    designer = CogPuzzleDesigner(
        board_size=(args.board_width, args.board_height),
        cog_diameter=args.cog_diameter,
        num_teeth=args.num_teeth
    )
    
    # Generate design
    design = designer.design_puzzle()
    
    # Print summary
    designer.print_design_summary(design)
    
    # Generate SVG files
    if not args.no_svg:
        print("\n🎨 Generating laser cutting files...")
        designer.generate_svg(design, args.output_dir)
        designer.save_design_json(design, args.output_dir)
        print(f"\n✓ All files saved to: {args.output_dir}/")
        print("\nNext steps:")
        print("  1. Review the SVG files")
        print("  2. Send board.svg and cog_*.svg to your laser cutter")
        print("  3. Use RED lines for cutting, BLUE for engraving")
        print("  4. Review assembly_diagram.svg for the solution state")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
