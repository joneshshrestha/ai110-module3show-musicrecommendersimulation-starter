"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def print_recommendations(profile_name: str, recommendations: list) -> None:
    print(f"\n=== {profile_name} ===\n")
    for i, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        reasons = [
            reason.strip() for reason in explanation.split(";") if reason.strip()
        ]

        print(f"[{i}] {song['title']}")
        print(f"    Final Score : {score:.2f}")
        print("    Reasons     :")
        for reason in reasons:
            print(f"      - {reason}")
        print("-" * 40)


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Core profiles for behavior analysis
    user_profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.92},
    }

    # Edge/adversarial profiles to test unexpected behavior
    adversarial_profiles = {
        "Conflicting Vibe (happy + very high energy)": {
            "genre": "ambient",
            "mood": "happy",
            "energy": 0.95,
        },
        "Sparse Preference (only energy)": {"energy": 0.8},
        "Out-of-Range Energy": {"genre": "pop", "mood": "happy", "energy": 1.4},
    }

    print("\nRunning core profiles...")
    for profile_name, user_prefs in user_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(profile_name, recommendations)

    print("\nRunning edge/adversarial profiles...")
    for profile_name, user_prefs in adversarial_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=3)
        print_recommendations(profile_name, recommendations)


if __name__ == "__main__":
    main()
