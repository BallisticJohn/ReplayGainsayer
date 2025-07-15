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

## Development

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

Clone the repository and install dependencies using pip:

```bash
 git clone https://example.com/ReplayGainsayer.git
 cd ReplayGainsayer
 pip install -r requirements.txt
```

## Usage

Run the tool with an artist name to see loudness information:

```bash
 python -m replaygainsayer --artist "Artist Name"
```

Contributions and ideas are welcome!