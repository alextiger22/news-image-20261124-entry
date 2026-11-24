"""Entry for make.fun news-image-20261124.

Writes the news summary image for Tuesday 24 November 2026 to
/output/entry.png. The image is a newspaper front page summing up the
day's world news: COP31 talks collapse in Antalya, a Russian warship
sunk at Benghazi, a factory fire killing 24 in Indonesia, drone
strikes on Kyiv, cost-of-living protests in Lisbon, and Verstappen
winning the Las Vegas Grand Prix.

Deterministic: the program only copies the image the repository holds,
so both runs write the same bytes. No network access. After copying,
the program validates the output is a PNG of 1024 by 1024 pixels and
at most 1 MiB, and fails loudly otherwise.
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

MAX_BYTES = 1024 * 1024


def _validate_png(path: str) -> None:
    """Check path is a PNG of 1024x1024 and at most 1 MiB (stdlib only)."""
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        sys.exit("entry.png is %d bytes, over the 1 MiB limit" % size)
    with open(path, "rb") as f:
        header = f.read(33)
    if header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        sys.exit("entry.png is not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    if (width, height) != (1024, 1024):
        sys.exit("entry.png is %dx%d, expected 1024x1024" % (width, height))


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)
    _validate_png(dest)
    print("wrote %s (%d bytes)" % (dest, os.path.getsize(dest)))


if __name__ == "__main__":
    main()
