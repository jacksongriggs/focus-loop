#!/bin/bash
# Plays a random file from sounds/ every 2-8 seconds at afplay volume 0.8.
# Stop with: pkill -f focus-loop.sh

DIR="$(cd "$(dirname "$0")" && pwd)"
SOUNDS="$DIR/sounds"
VOLUME=0.8

while true; do
    files=( "$SOUNDS"/*.wav "$SOUNDS"/*.aiff "$SOUNDS"/*.mp3 )
    existing=()
    for f in "${files[@]}"; do
        [ -f "$f" ] && existing+=("$f")
    done
    if [ "${#existing[@]}" -gt 0 ]; then
        pick="${existing[$((RANDOM % ${#existing[@]}))]}"
        afplay -v "$VOLUME" "$pick"
    else
        sleep 10
    fi
    sleep $((RANDOM % 7 + 2))
done
