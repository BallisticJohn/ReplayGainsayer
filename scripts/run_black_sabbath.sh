#!/usr/bin/env bash
# Simple script to run ReplayGainsayer for the band Black Sabbath.
# Requires SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET environment variables.

if [[ -z "$SPOTIFY_CLIENT_ID" || -z "$SPOTIFY_CLIENT_SECRET" ]]; then
  echo "Please set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET env vars." >&2
  exit 1
fi

python -m replaygainsayer "Black Sabbath" \
  --client-id "$SPOTIFY_CLIENT_ID" \
  --client-secret "$SPOTIFY_CLIENT_SECRET"
