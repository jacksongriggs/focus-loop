#!/usr/bin/env python3
"""Cut a long recording into one file per sound, at its silences.

    python3 split.py incoming/yle.mp3 sounds yle

Each piece is peak-normalised to -2 dB (at most +24 dB of gain).
"""
import re, subprocess, sys

src, out, prefix = sys.argv[1], sys.argv[2], sys.argv[3]
PAD, MIN = 0.06, 0.15

def ffmpeg(*args):
    return subprocess.run(["ffmpeg", "-hide_banner", *args], capture_output=True, text=True).stderr

log = ffmpeg("-i", src, "-af", "silencedetect=noise=-38dB:d=0.35", "-f", "null", "-")
starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", log)]
ends = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", log)]
# a sound runs from one silence's end to the next silence's start
pieces = [(e, s) for e, s in zip(ends, starts[1:]) if s - e >= MIN]

for n, (a, b) in enumerate(pieces, 1):
    a, d = max(0, a - PAD), b - a + 2 * PAD
    cut = ["-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", src]
    peak = float(re.search(r"max_volume: (-?[0-9.]+)", ffmpeg(*cut, "-af", "volumedetect", "-f", "null", "-")).group(1))
    gain = min(24.0, -2.0 - peak)
    name = f"{out}/{prefix}-{n:02d}.wav"
    ffmpeg("-y", *cut, "-af", f"volume={gain:.1f}dB,afade=t=in:d=0.02", name)
    print(f"{name}  {d:.2f}s  peak {peak:.1f} dB  gain {gain:+.1f} dB")
