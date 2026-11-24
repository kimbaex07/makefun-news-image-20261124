#!/usr/bin/env python3
"""Entry program for news-image-20261124 (Tuesday 24 November 2026).

The entry is a single picture of the day's world news, held in this
repository as entry.png. This program places an exact copy of that
picture at $MAKEFUN_OUTPUT_DIR/entry.png (default /output). It draws
nothing and changes nothing at run time, so the grader's two runs
always write identical bytes.

The picture is a "THE WORLD IN ONE DAY — TUESDAY, 24 NOVEMBER 2026"
front page: three illustrated leads plus a "THE DAY IN BRIEF" digest.
Every story on it was checked against reporting of Tuesday
24 November 2026:

Leads:
  - RUSSIAN JETS SPARK KOREA ALERT: several Russian military
    aircraft entered South Korea's air-defence zone near Ulleung
    Island on Tuesday morning; Seoul scrambled fighter jets, an
    island shelter alert was lifted minutes later, and the military
    said no airspace was violated. (Reuters / AP / Yonhap, 24 Nov)
  - AN ISLAND EMPTIED IN A DAY: all 40-50 residents of Kanton
    Island, Kiribati, were moved to Tarawa with 24 hours' notice;
    officials cite strong El Nino weather, poor housing and the
    island's remoteness, and some were told return may take four
    years. (PINA, 24 Nov 2026)
  - ALIBABA DENIES CHIP DIVERSION: Alibaba said its Singapore unit
    Apex never diverted restricted chips and will defend its rights,
    a day after Washington blacklisted Apex and Megaspeed;
    Singapore's prime minister said probes continue and the
    city-state will not be used to evade US export controls.
    (Reuters / market wires, 24 Nov 2026)

Digest:
  - BRAZIL: the lower house approves the main text of Lula's fiscal
    plan; the Senate backed it on 21 Nov. (market wire, 24 Nov)
  - PACIFIC: after COP31 ended without a deal, Pacific island
    nations press on alone on climate. (PINA, 24 Nov 2026)
  - MARKETS: Chinese chip shares jump about 4% as Asian markets
    rally on the blacklist news. (market wire, 24 Nov 2026)
  - INDIA: the Supreme Court grants bail on medical grounds to a
    Godhra convict. (Times of India / The Hindu, 24 Nov 2026)
  - PAKISTAN: a magnitude 4.0 quake strikes near the Afghan border;
    Lahore tops world pollution rankings. (Times of India, 24 Nov)
  - THAILAND: protesters march 16 km to a Bangkok refinery demanding
    lower refining margins. (24 Nov 2026 morning brief)
  - USA: Chicago's O'Hare briefly halts arrivals over a staffing
    shortage in the Thanksgiving rush. (Times of India, 24 Nov)

Standard library only; no network access; no files are read besides
entry.png in this directory.
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    """Copy entry.png beside this file into the output directory."""
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    if not source.is_file():
        print(f"missing image: {source}", file=sys.stderr)
        return 1
    size = source.stat().st_size
    if size > MAX_BYTES:
        print(f"image too big: {size} bytes", file=sys.stderr)
        return 1
    with source.open("rb") as handle:
        if handle.read(len(PNG_MAGIC)) != PNG_MAGIC:
            print("image is not a PNG file", file=sys.stderr)
            return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / IMAGE_NAME
    shutil.copyfile(source, target)
    if target.stat().st_size != size:
        print("copy size mismatch", file=sys.stderr)
        return 1
    print(f"wrote {target} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
