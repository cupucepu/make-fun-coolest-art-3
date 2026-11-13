"""Entry for make.fun coolest-art-01: The Sky Whale.

A luminous whale swims through a starry night sky, glowing cyan
against the dark, a full moon above and a sea of clouds below.

The program copies the vendored art.png (JPEG bytes) to
/output/entry.png, reads it back and compares it byte for byte,
and checks the JPEG header says 1024x1024, so a wrong-sized
or wrong file fails loudly instead of silently scoring zero.
"""

import os
import shutil
import struct
import sys


def jpeg_dimensions(path):
    """Read (width, height) from a JPEG file's SOF marker, stdlib only."""
    with open(path, "rb") as f:
        if f.read(2) != b"\xff\xd8":
            raise ValueError("not a JPEG file (missing SOI marker)")
        while True:
            marker = f.read(1)
            while marker == b"\xff":
                marker = f.read(1)
            if not marker:
                raise ValueError("no SOF marker found")
            code = marker[0]
            if code in (0xC0, 0xC1, 0xC2):
                f.read(3)
                height, width = struct.unpack(">HH", f.read(4))
                return width, height
            length = struct.unpack(">H", f.read(2))[0]
            f.seek(length - 2, 1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "art.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    if os.path.getsize(src) > 1048576:
        print(f"error: art.png is over the 1 MiB cap: {os.path.getsize(src)} bytes",
              file=sys.stderr)
        sys.exit(1)
    shutil.copyfile(src, out)
    with open(src, "rb") as f:
        original = f.read()
    with open(out, "rb") as f:
        copied = f.read()
    if original != copied:
        print("error: /output/entry.png differs from art.png", file=sys.stderr)
        sys.exit(1)
    width, height = jpeg_dimensions(out)
    if (width, height) != (1024, 1024):
        print(f"error: unexpected JPEG dimensions {width}x{height}, "
              "expected 1024x1024", file=sys.stderr)
        sys.exit(1)
    print(f"ok: /output/entry.png is a byte-identical 1024x1024 copy "
          f"of art.png ({os.path.getsize(out)} bytes)")


if __name__ == "__main__":
    main()
