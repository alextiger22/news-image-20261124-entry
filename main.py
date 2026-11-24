"""Entry for make.fun news-image-20261124.

Writes the news summary image for Tuesday 24 November 2026 to
/output/entry.png. The image is a newspaper front page summing up the
day's world news: COP31 talks collapse in Antalya, a Russian warship
sunk at Benghazi, a factory fire killing 24 in Indonesia, drone
strikes on Kyiv, cost-of-living protests in Lisbon, and Verstappen
winning the Las Vegas Grand Prix.

Deterministic: the program only copies the image the repository holds,
so both runs write the same bytes. No network access.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)


if __name__ == "__main__":
    main()
