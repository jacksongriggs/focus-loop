#!/usr/bin/env python3
"""How long each sound takes to die away: a stand-in for reverb.

    python3 tail.py sounds/*.wav

tail = time from the last moment the level is within 10 dB of the peak to
the moment it has fallen 30 dB below the peak (10 ms RMS windows). A dry
sound stops quickly; one in a live room rings on. "open" means the file
ends before the level has fallen that far.
"""
import array, math, subprocess, sys

SR, WIN = 22050, 220
rows = []
for f in sys.argv[1:]:
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", f, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True).stdout
    x = array.array("h", raw)
    db = []
    for i in range(0, len(x) - WIN, WIN):
        rms = math.sqrt(sum(v * v for v in x[i:i + WIN]) / WIN) or 1e-9
        db.append(20 * math.log10(rms / 32768))
    peak = max(db)
    last10 = max(i for i, v in enumerate(db) if v >= peak - 10)
    end = next((i for i in range(last10, len(db)) if db[i] <= peak - 30), None)
    floor = min(db[last10:]) - peak
    t = (end - last10) * WIN / SR if end is not None else None
    rows.append((t if t is not None else 99, f.split("/")[-1], len(x) / SR, t, floor))
for _, name, dur, t, floor in sorted(rows):
    print(f"{name:22s} {dur:5.2f}s  tail {'open' if t is None else f'{t:.2f}s':>6}  falls to {floor:+.0f} dB")
