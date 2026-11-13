# The Sky Whale

A luminous whale swims through a starry night sky, its body traced
with glowing cyan light, a full moon above and a sea of clouds below.
The idea is simple: the biggest creature of the ocean, set free in
the biggest sky — a shape anyone recognises at a glance, lit up like
something that should not be there.

## How the entry works

1. `main.py` copies the vendored `art.png` to `/output/entry.png`.
2. It reads the output back and compares it byte for byte with the source.
3. It parses the JPEG header (standard library only) and checks the
   image is 1024x1024, and refuses a file over the 1 MiB cap.

Any mismatch or wrong size fails loudly; on success it prints a
confirmation line with the file size.

## Files

- `art.png` — the artwork (JPEG bytes, 1024x1024)
- `main.py` — the entry program (Python 3, standard library only)
- `LICENSE` — MIT
