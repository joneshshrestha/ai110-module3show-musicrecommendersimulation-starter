# Reflection: Profile Pair Comparisons

I compared the outputs pair by pair to check what changed and why.

- High-Energy Pop vs Chill Lofi: High-Energy Pop pushes upbeat songs like Sunrise City and Gym Hero, while Chill Lofi shifts to Library Rain and Midnight Coding because the energy target is much lower and both genre and mood align.
- High-Energy Pop vs Deep Intense Rock: Both profiles keep high-energy tracks near the top, but Deep Intense Rock promotes Storm Runner because genre and mood both match rock/intense.
- High-Energy Pop vs Conflicting Vibe: Conflicting Vibe still surfaces happy songs, but high energy keeps Gym Hero competitive even without a genre match.
- High-Energy Pop vs Sparse Preference: Sparse Preference looks almost like an energy leaderboard, so songs close to 0.8 rise even when genre/mood are not specified.
- High-Energy Pop vs Out-of-Range Energy: Out-of-Range Energy still returns pop/happy songs first because category matches add points when the energy target is unrealistic.

- Chill Lofi vs Deep Intense Rock: Chill Lofi favors low-energy calm tracks, while Deep Intense Rock jumps to very high-energy songs because the energy gap term strongly separates them.
- Chill Lofi vs Conflicting Vibe: Chill Lofi rewards lofi/chill alignment, while Conflicting Vibe pulls toward happier and higher-energy tracks, so top songs become less genre-consistent.
- Chill Lofi vs Sparse Preference: Chill Lofi keeps lofi songs at the top, but Sparse Preference ignores style and mostly follows energy closeness.
- Chill Lofi vs Out-of-Range Energy: Chill Lofi gives clear low-energy picks, while Out-of-Range Energy weakens the energy signal and category matches matter more.

- Deep Intense Rock vs Conflicting Vibe: Deep Intense Rock keeps Storm Runner first, but Conflicting Vibe can push Sunrise City and Rooftop Lights up due to happy mood and high energy closeness.
- Deep Intense Rock vs Sparse Preference: Deep Intense Rock still prefers intense songs, while Sparse Preference removes style constraints and becomes mostly numeric matching.
- Deep Intense Rock vs Out-of-Range Energy: Deep Intense Rock behaves as expected, but Out-of-Range Energy compresses differences and lets category points dominate.

- Conflicting Vibe vs Sparse Preference: Conflicting Vibe still gives a mood bonus to happy songs, while Sparse Preference has no mood/genre anchors and is easier to "trick" by energy alone.
- Conflicting Vibe vs Out-of-Range Energy: Both are edge cases, but Out-of-Range Energy reduces energy usefulness so category matches become the tie-breaker.

- Sparse Preference vs Out-of-Range Energy: Sparse Preference produces pure energy-nearest results, while Out-of-Range Energy makes every song relatively far so the small genre/mood bonuses decide more of the final order.

Gym Hero keeps showing up for many profiles because it has very high energy, and the current scoring gives energy a large weight. Even when a user asks for something more specific, a close energy match can still beat a weaker genre or mood fit.
