"""Loudness analysis utilities."""

from typing import Iterable

try:
    import pyloudnorm as pyln
except ImportError:  # pragma: no cover - pyloudnorm is optional
    pyln = None  # type: ignore


def measure_loudness(samples: Iterable[float], sample_rate: int) -> float:
    """Return integrated loudness in LUFS for the given audio samples."""
    if pyln is None:
        raise RuntimeError(
            "pyloudnorm is required for loudness measurement. Install it via pip."
        )
    meter = pyln.Meter(sample_rate)
    return meter.integrated_loudness(samples)


def classify_loudness(lufs: float) -> str:
    """Return RYG classification for a given loudness level."""
    if lufs > -6:
        return "red"
    if -11 < lufs <= -6:
        return "yellow"
    return "green"
