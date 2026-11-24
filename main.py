"""make.fun entry: Make the Judge Smile.

Writes one line to /output/entry.txt: a small good thing that happened
today, written to make the judge smile. Stdlib-only (os, sys); no network;
deterministic.

Design (from the published judge brief, criteria in order):
1. On subject: a small good thing that happened TODAY -- "Today a little
   girl at the vending machine..." -- anchored in today, not a general
   sentiment.
2. Warmth: a child's spontaneous kindness -- she gives away the drink she
   just bought with her last coin. Genuinely felt, not merely reported.
3. Surprise: the turn is the deed itself plus the child's line --
   "You look thirstier." She bought the wrong drink and gives it away
   anyway, to a stranger -- the kindness costs her the very thing she
   just spent her last coin on.
4. Concreteness: one real small detail, several in fact -- the vending
   machine, her last coin, the wrong drink.
5. Fresh wording: "You look thirstier" -- a child's own words and rhythm,
   no greeting-card phrasing, no borrowed sentiment. The scene (vending
   machine girl) is not one of the field's five saturated tropes (bus
   driver, warung krupuk, mango on the doorstep, 4 a.m. baker, toddler
   on the train).
"""

import os
import sys

TEXT = (
    "Today a little girl at the vending machine spent her last coin "
    "on the wrong drink, then handed it to me anyway and said, "
    "'You look thirstier.'"
)


def main() -> int:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # counted as Unicode code points, and not only white space.
    if not (1 <= len(TEXT) <= 200):
        print(f"entry length {len(TEXT)} outside 1-200", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
