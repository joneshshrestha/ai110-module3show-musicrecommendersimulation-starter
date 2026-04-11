import csv

from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """

    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and return typed song dictionaries."""
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": int(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences and return score plus reasons."""
    score = 0.0
    reasons: List[str] = []

    favorite_genre = user_prefs.get("favorite_genre", user_prefs.get("genre", ""))
    favorite_mood = user_prefs.get("favorite_mood", user_prefs.get("mood", ""))
    target_energy = float(
        user_prefs.get("target_energy", user_prefs.get("energy", 0.5))
    )

    if song["genre"] == favorite_genre:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == favorite_mood:
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Closeness-based energy score: exact match gets full points.
    energy_similarity = max(0.0, 1.0 - abs(float(song["energy"]) - target_energy))
    energy_points = 1.25 * energy_similarity
    score += energy_points
    reasons.append(f"energy closeness ({energy_similarity:.2f}) (+{energy_points:.2f})")

    return score, reasons


def recommend_songs(
    user_prefs: Dict, songs: List[Dict], k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top-k recommendations."""
    ranked = sorted(
        (
            (song, score, "; ".join(reasons))
            for song in songs
            for score, reasons in [score_song(user_prefs, song)]
        ),
        key=lambda item: item[1],
        reverse=True,
    )
    return ranked[:k]
