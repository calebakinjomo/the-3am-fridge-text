#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun bounty u-deysumbrella-the-3am-fridge-text-4c3e721d.

Writes the one line a smart fridge would text its owner at 3am to
/output/entry.txt. Entry must be a single line, 1-140 UTF-8 chars.

Intent: the fridge plays the exhausted, slightly judgemental night-shift
voice — it has watched the owner do this exact 3am stare before, so it
skips the lecture and lands the punchline ("Take the cake") instead.
The humour is the contrast: a mundane appliance delivering a deadpan,
almost parental nudge about a yoghurt that will never apologise.
"""

import os

ENTRY = (
    "3am. You're standing here in your underwear, door open, staring at "
    "a yoghurt like it's going to apologise. It won't. Take the cake."
)

def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
