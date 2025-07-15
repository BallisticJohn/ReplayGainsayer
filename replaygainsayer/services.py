"""Streaming service integrations for ReplayGainsayer."""

from dataclasses import dataclass
from typing import List

try:
    import spotipy
    from spotipy import Spotify
    from spotipy.oauth2 import SpotifyClientCredentials
except ImportError:  # pragma: no cover - spotipy is optional
    spotipy = None  # type: ignore


@dataclass
class Album:
    """Basic album representation."""

    name: str
    id: str


class BaseService:
    """Base class for streaming service implementations."""

    def get_albums(self, artist_name: str) -> List[Album]:
        raise NotImplementedError


class SpotifyService(BaseService):
    """Interact with the Spotify API to fetch albums."""

    def __init__(self, client_id: str, client_secret: str):
        if spotipy is None:
            raise RuntimeError(
                "spotipy is required for Spotify integration. Install it via pip."
            )
        creds = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.api = Spotify(client_credentials_manager=creds)

    def get_albums(self, artist_name: str) -> List[Album]:
        results = self.api.search(q=f"artist:{artist_name}", type="album")
        albums = []
        for item in results.get("albums", {}).get("items", []):
            albums.append(Album(name=item["name"], id=item["id"]))
        return albums
