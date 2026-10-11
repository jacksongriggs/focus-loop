# focus-loop

Plays a random sound from `sounds/` every 2-8 seconds, at afplay volume 0.8.
System output volume is not changed. macOS only (`afplay`).

## Run and stop

    nohup ~/Developer/tools/focus-loop/focus-loop.sh >/dev/null 2>&1 &
    pkill -f focus-loop.sh

## Licence

- **Scripts and this README:** MIT (`LICENSE`).
- **Recordings:** each keeps the licence in the table below. None is mine;
  all are from Wikimedia Commons.

## Sounds

Changes made: Ogg files converted to WAV with ffmpeg; the Yle recording cut
into pieces and each piece peak-normalised. A changed CC BY-SA file stays
under its CC BY-SA licence; the Yle pieces stay under CC BY 3.0.

| File | Length | Author | Source | Licence |
|---|---|---|---|---|
| `short-pop.wav` | 0.4 s | Subhashish Panigrahi | [Human fart.wav](https://commons.wikimedia.org/wiki/File:Human_fart.wav) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| `aimee.wav` | 1.3 s | PlatypussyPatrick | [Flatulence d'Aimée.ogg](https://commons.wikimedia.org/wiki/File:Flatulence_d%27Aim%C3%A9e.ogg) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| `fart.wav` | 1.4 s | El Charpi | [Fart.ogg](https://commons.wikimedia.org/wiki/File:Fart.ogg) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| `jjzh.wav` | 1.9 s | Prononcateur | [Flatulences 03°2° JJZh.ogg](https://commons.wikimedia.org/wiki/File:Flatulences_03%C2%B02%C2%B0_JJZh.ogg) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| `frt755.wav` | 2.6 s | Horst Frank | [Frt755 1.ogg](https://commons.wikimedia.org/wiki/File:Frt755_1.ogg) | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) |
| `flatus.wav` | 4.6 s | JohnSumisu | [Flatus.wav](https://commons.wikimedia.org/wiki/File:Flatus.wav) | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) |
| `yle-*.wav` (38 files), `incoming/yle.mp3` | 0.3-5.7 s | Yle Arkisto (via Freesound; uploaded to Commons by Zache) | [425594 ylearkisto farts-pieruja.wav](https://commons.wikimedia.org/wiki/File:425594_ylearkisto_farts-pieruja.wav) | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0) |

## Rebuilding the Yle pieces

`incoming/yle.mp3` is Commons' 64 kbps MP3 copy of the recording.

    python3 split.py incoming/yle.mp3 sounds yle

That writes `yle-01` to `yle-48`. Ten are then moved out: see `rejected/`.
Needs ffmpeg and python3.

Still to add (Commons answered 429 on 12 Oct 2026): `Flatulence.wav`,
`Menselijke wind drietraps.wav`, `Flatulence de Clément.ogg`.

## rejected/

Kept out of rotation, with the reason.

- **Speech, not sound effects:** eight Lingua Libre clips by "Flame, not lame"
  (`LL-Q1860 (eng)-Flame, not lame-fart …`, CC0) and `Fart (avk).wav` by
  Luce Vergeaux (CC0). People saying phrases with "fart" in them, picked by
  filename on 12 Oct 2026; do not put them back.
- **Near silent:** `yle-16`, `yle-29` (peak below -32 dB).
- **`reverb/`:** eight Yle pieces whose level took 0.3 s or more to fall
  30 dB after the sound (`tail.py`), taken as reverb and not judged by ear;
  and `fart-wet-rumble.wav` ([Wet fart tummy rumbles.ogg](https://commons.wikimedia.org/wiki/File:Wet_fart_tummy_rumbles.ogg),
  by natalie via PDSounds, public domain), removed by ear the same day.
