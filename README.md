# ReplayGainsayer

ReplayGainsayer helps music fans identify the best masters of their favorite music and avoid remasters that suffer from the "loudness wars." It highlights albums with healthy dynamic range and warns about overly compressed releases.

## How it works

1. **Search streaming catalogs** – Enter an artist name and ReplayGainsayer finds albums across supported services.
2. **Measure album loudness** – Each album is analyzed for overall loudness (EBU/ITU LUFS, ReplayGain or similar).
3. **Report results** – Albums are labeled:
   - **Red**: brick walled (> –6 dBFS)
   - **Yellow**: heavily compressed (–11 to –6 dBFS)
   - **Green**: healthy dynamics (< –11 dBFS)

Eventually, ReplayGainsayer may help fans to discover the best masters across streaming platforms and choose to listen to better music.

## Staged development plan

1. **Spotify prototype**
   - Use Spotify's public API to search artists and fetch loudness data.
   - Compute average album loudness and show red/yellow/green results.

2. **More streaming services**
   - Expand to Qobuz and Tidal, followed by Apple Music and Amazon Music.
   - Eventually add YouTube Music and others as APIs or data become available.

3. **Cross-service comparison**
   - Present loudness information across services so listeners can choose the best master no matter where it is offered.

## Installation

Clone the repository and set up a Python virtual environment so dependencies do not pollute your base system:

```bash
git clone https://example.com/ReplayGainsayer.git
cd ReplayGainsayer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Spotify credentials

Create an application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) to obtain a **Client ID** and **Client Secret**. Store them in environment variables:

```bash
export SPOTIFY_CLIENT_ID=<your client id>
export SPOTIFY_CLIENT_SECRET=<your client secret>
```

## Usage

Run the tool with an artist name, passing in the credentials from the environment:

```bash
python -m replaygainsayer "Artist Name" \
  --client-id "$SPOTIFY_CLIENT_ID" \
  --client-secret "$SPOTIFY_CLIENT_SECRET"
```

The script `scripts/run_black_sabbath.sh` demonstrates running the program for the band **Black Sabbath**.

## Development

Run the automated tests with `pytest`:

```bash
pip install pytest
pytest
```

Contributions and ideas are welcome!
