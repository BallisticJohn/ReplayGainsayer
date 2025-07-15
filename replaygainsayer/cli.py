"""Command line interface for ReplayGainsayer."""

import argparse
from typing import List

from .services import SpotifyService, Album
from .loudness import classify_loudness


class CLI:
    """Main CLI handler."""

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description=__doc__)
        self.parser.add_argument("artist", help="Artist name to search for")
        self.parser.add_argument("--client-id", required=True)
        self.parser.add_argument("--client-secret", required=True)

    def run(self, argv: List[str] | None = None) -> None:
        args = self.parser.parse_args(argv)
        service = SpotifyService(args.client_id, args.client_secret)
        albums = service.get_albums(args.artist)
        print(f"Found {len(albums)} albums for {args.artist}:")
        for album in albums:
            # Placeholder: we have no audio to measure, so display album name only
            lufs = -12.0  # fake value for demonstration
            label = classify_loudness(lufs)
            print(f"  {album.name} -> {label} ({lufs} LUFS)")


def main(argv: List[str] | None = None) -> None:
    CLI().run(argv)


if __name__ == "__main__":
    main()
