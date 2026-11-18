#!/usr/bin/env python3
"""Build the 17 Nov 2026 world-news summary image (1024x1024 PNG).

Deterministic: fixed text, fixed layout, no network, no randomness.
Run locally only; main.py in the entry repo just copies entry.png.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (253, 246, 227)
INK = (17, 17, 17)
RED = (178, 34, 34)
GREY = (90, 90, 90)
YELLOW = (255, 210, 0)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, f, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, f, fill=INK, lh=None):
    if lh is None:
        lh = int(f.size * 1.25)
    for ln in lines:
        draw.text((x, y), ln, font=f, fill=fill)
        y += lh
    return y


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# top bar
d.rectangle([0, 0, W, 44], fill=INK)
d.text((24, 10), "TUESDAY 17 NOVEMBER 2026", font=font(SANS_B, 22), fill=(255, 255, 255))
right = "THE WORLD IN ONE IMAGE"
d.text((W - 24 - d.textlength(right, font=font(SANS_B, 22)), 10),
       right, font=font(SANS_B, 22), fill=YELLOW)

# masthead
y = 62
d.text((24, y), "THE WORLD", font=font(SERIF_B, 108), fill=INK)
y += 118
d.text((24, y), "One day, six stories  —  Tuesday 17 November 2026",
       font=font(SANS_B, 26), fill=RED)
y += 44
d.line([(24, y), (W - 24, y)], fill=INK, width=4)
y += 18

stories = [
    ("1  US AND IRAN TRADE FIRE",
     "US jets strike an Iranian missile site on Qeshm Island after Iran fires drones at a US radar in Bahrain — its third attack on Bahrain in five days.",
     True),
    ("2  KERCH BRIDGE HIT AGAIN",
     "Ukrainian drones strike the bridge to Crimea for a second day running, and a road section falls into the strait.",
     False),
    ("3  NVIDIA RECORDS, HUANG NOT BACK",
     "Revenue tops $115 billion, about double a year earlier — but the board will not bring back ousted chief Jensen Huang.",
     False),
    ("4  TRUMP HEADS TO ASIA",
     "The president travels to the APEC summit in Shenzhen for talks with Xi Jinping and Vladimir Putin, after a Quad summit in Manila.",
     False),
    ("5  EU STATES PLAN RWANDA RETURN HUB",
     "Germany, Denmark, Austria, Greece and the Netherlands will send rejected asylum seekers to Rwanda; transfers could start in 2027.",
     False),
    ("6  US LOSES MEASLES-FREE STATUS",
     "After 26 years, the US loses its measles elimination status amid 5,400 cases and 10 deaths — the worst year since the early 1990s.",
     False),
]

# lead story
title, body, _ = stories[0]
f_t = font(SANS_B, 32)
f_b = font(SANS, 24)
lines = wrap(d, body, f_b, W - 80)
box_h = 34 + len(lines) * 30 + 28
d.rectangle([24, y, W - 24, y + box_h], outline=RED, width=3)
yy = y + 14
d.text((40, yy), title, font=f_t, fill=RED)
yy += 46
text_block(d, 40, yy, lines, f_b, lh=30)
y = y + box_h + 16

# 2x2 grid for stories 2-5
grid = stories[1:5]
col_w = (W - 48 - 16) // 2
row_h = 168
for i, (t, b, _) in enumerate(grid):
    gx = 24 + (i % 2) * (col_w + 16)
    gy = y + (i // 2) * (row_h + 16)
    d.rectangle([gx, gy, gx + col_w, gy + row_h], outline=INK, width=2)
    tl = wrap(d, t, font(SANS_B, 19), col_w - 28)
    text_block(d, gx + 14, gy + 10, tl[:2], font(SANS_B, 19), lh=23)
    bl = wrap(d, b, font(SANS, 19), col_w - 28)
    text_block(d, gx + 14, gy + 10 + len(tl[:2]) * 23 + 8, bl[:4], font(SANS, 19), lh=24)
y = y + 2 * row_h + 16 + 16

# bottom story
t, b, _ = stories[5]
d.rectangle([24, y, W - 24, y + 108], fill=INK)
d.text((40, y + 12), t, font=font(SANS_B, 24), fill=YELLOW)
bl = wrap(d, b, font(SANS, 20), W - 80)
text_block(d, 40, y + 48, bl, font(SANS, 20), fill=(255, 255, 255), lh=26)
y = y + 108 + 14

# footer
d.text((24, H - 34), "Sources: AP, Reuters, BBC, CBS, NPR, Al Jazeera  —  17 Nov 2026",
       font=font(SANS, 18), fill=GREY)

img.save("entry.png", format="PNG", optimize=True)
print("saved entry.png")
