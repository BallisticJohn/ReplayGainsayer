import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import builtins
from unittest import mock

from replaygainsayer.cli import CLI
from replaygainsayer.services import Album


def test_cli_lists_black_sabbath_albums(capsys):
    albums = [
        Album(name="Paranoid", id="1"),
        Album(name="Master of Reality", id="2"),
    ]
    with mock.patch("replaygainsayer.cli.SpotifyService") as service_cls:
        service_cls.return_value.get_albums.return_value = albums
        CLI().run(["Black Sabbath", "--client-id", "id", "--client-secret", "secret"])
    output = capsys.readouterr().out
    assert "Found 2 albums for Black Sabbath:" in output
    assert "Paranoid" in output
    assert "Master of Reality" in output
