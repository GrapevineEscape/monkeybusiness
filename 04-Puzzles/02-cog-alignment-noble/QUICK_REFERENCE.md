# Quick Reference - Cog Alignment Puzzle

## 🎯 What Is This Puzzle?

A mechanical rotational alignment puzzle where players:
1. Find 4 laser-cut acrylic cogs scattered around the room
2. Match each cog to a post on a board using symbols
3. Rotate cogs until engraved lines form a continuous path
4. The path spells **N-O-B-L-E** → use this word to unlock something

## 📁 File Guide

```
04-Puzzles/02-cog-alignment-noble/
├── puzzle-concept.md          ⭐ START HERE - Complete puzzle design
├── README.md                  🔧 Fabrication quick start
├── INTEGRATION.md            🎭 Story integration & room placement
├── MATHEMATICS.md            📐 Design calculations explained
├── QUICK_REFERENCE.md        👈 You are here!
│
├── cog_designer.py           🎨 Generate laser cutting files
├── verify_design.py          ✅ Test and validate design
│
└── output/                   📤 Generated files (not in git)
    ├── board.svg            → Send to laser cutter
    ├── cog_1.svg            → Send to laser cutter
    ├── cog_2.svg            → Send to laser cutter
    ├── cog_3.svg            → Send to laser cutter
    ├── cog_4.svg            → Send to laser cutter
    ├── assembly_diagram.svg → Solution reference for you
    └── design_specs.json    → All measurements
```

## 🚀 Quick Start (3 Steps)

### 1. Generate Design Files
```bash
cd 04-Puzzles/02-cog-alignment-noble
python cog_designer.py
```

### 2. Verify Design
```bash
python verify_design.py
```
Should show: **🎉 Design verification complete - ready to fabricate!**

### 3. Fabricate
- Send `output/*.svg` files to laser cutter
- Material: 3-6mm acrylic (clear or frosted)
- Cut settings: RED = cut through, BLUE = engrave

## 🎨 Customization Examples

### Change Board Size
```bash
python cog_designer.py --board-width 450 --board-height 450
```

### Make Easier (Fewer Teeth)
```bash
python cog_designer.py --num-teeth 12
```

### Make Harder (More Teeth)
```bash
python cog_designer.py --num-teeth 24
```

### Larger Cogs
```bash
python cog_designer.py --cog-diameter 100
```

### Change Word (Edit cog_designer.py line 147)
```python
letters = "GRACE"  # or any 5-letter word
```

### Change Symbols (Edit cog_designer.py line 49)
```python
self.symbols = ["🔬", "⚗️", "🧪", "🔭"]  # Science theme
self.symbols = ["♠", "♥", "♦", "♣"]      # Card suits
self.symbols = ["α", "β", "γ", "δ"]      # Greek letters
```

## 💡 Solution Guide (For Game Master)

**Default Solution:**
1. ⚙ (Gear) cog → Rotate 14 teeth clockwise
2. 🔧 (Wrench) cog → Rotate 3 teeth clockwise  
3. 🔨 (Hammer) cog → Rotate 12 teeth clockwise
4. ⭐ (Star) cog → Rotate 1 tooth clockwise

When aligned correctly, lines form path through: **N-O-B-L-E**

## 💰 Budget

| Item | Cost |
|------|------|
| Acrylic sheets | $20-50 |
| Laser cutting | $30-100 |
| Posts/hardware | $5-15 |
| Paint/finishing | $5-15 |
| **Total** | **$60-180** |

Time: 2-4 hours assembly

## 🎭 Theme Integration Ideas

| Theme | Symbols | Story Hook |
|-------|---------|------------|
| **Workshop** | ⚙🔧🔨⭐ | Calibration device, repair manual |
| **Scientific** | 🔬⚗️🧪🔭 | Instrument alignment, lab equipment |
| **Nobility** | 👑💎⚔️🏰 | Family crest, coat of arms cipher |
| **Cards/Games** | ♠♥♦♣ | Gambling device, card game puzzle |

## 🔍 Troubleshooting

**Lines hard to see?**
- Fill engravings with paint
- Use frosted acrylic instead of clear
- Add LED backlighting

**Cogs don't rotate smoothly?**
- Sand center hole edges
- Increase hole diameter (+0.5mm)
- Add washers/spacers

**Too easy/hard?**
- Adjust number of teeth (12=easy, 24=hard)
- Distribute cogs further apart
- Add red herrings (extra non-matching posts)

## 📊 Difficulty Settings

| Teeth | Resolution | Difficulty | Fabrication |
|-------|-----------|------------|-------------|
| 12 | 30° | ⭐ Easy | Simple |
| 16 | 22.5° | ⭐⭐ Medium | Standard |
| 20 | 18° | ⭐⭐⭐ Hard | Precise |
| 24 | 15° | ⭐⭐⭐⭐ Expert | Very precise |

## 🎯 Hints (Progressive Escalation)

1. "Those pieces look like they belong somewhere..."
2. "Match the symbols - they're your guide"
3. "Try rotating them. Watch the lines."
4. "The lines should connect to form a path"
5. "What letters does the path touch?"

**Bypass:** Show photo of 1-2 cogs in correct position

## 🔌 Optional: Add Electronics

Want automatic detection? You can add:
- **Rotary encoders** to detect cog angles
- **RFID tags** on cogs + readers on posts
- **LED strips** that light up when solved
- **Solenoid lock** to open a drawer/box
- **Arduino/ESP32** controller

Cost: +$50-150  
See: `INTEGRATION.md` for details

## 📚 Read More

- **puzzle-concept.md** → Full design specification
- **INTEGRATION.md** → How to fit this into your room
- **MATHEMATICS.md** → How the math works
- **README.md** → Detailed fabrication guide

## ✅ Status

- ✅ Design complete
- ✅ Math verified
- ✅ Tools working
- ✅ Documentation complete
- ⏳ Ready to fabricate when you are!

---

**Questions?** See the detailed documentation files or PR #2 discussion.
