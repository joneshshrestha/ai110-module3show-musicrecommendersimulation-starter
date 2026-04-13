# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This recommender suggests songs from a small catalog based on a user's genre, mood, and energy preference.
It is made for classroom exploration and learning, not for production users.
It assumes a user can be represented by a few simple preferences.

Intended use:
- Testing and learning how recommendation scoring works
- Comparing how weight changes affect top results

Non-intended use:
- Real music personalization for actual users
- Any high-stakes decision making
- Claims about broad music taste across cultures or communities

---

## 3. How the Model Works  

The model reads each song and gives it points.
It gives points for genre match and mood match.
Then it gives a bigger score when the song's energy is close to the user's target energy.
After I tested sensitivity, I reduced genre weight and increased energy weight.
Finally, it sorts all songs by score and returns the top results.

---

## 4. Data  

The dataset has 18 songs.
It includes genres like pop, lofi, rock, ambient, jazz, synthwave, hip-hop, classical, reggae, folk, metal, latin, and more.
It includes moods like happy, chill, intense, relaxed, focused, dark, dreamy, and playful.
I expanded the starter data to add more genres and moods.
The biggest limit is size: the catalog is tiny and cannot represent full real-world taste.

---

## 5. Strengths  

It works well for clear profiles like Chill Lofi and Deep Intense Rock.
The top results usually make sense when genre and mood are specific.
The reason strings are also helpful, because I can see exactly why a song ranked high.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

One weakness I noticed is that the model can over-focus on energy and rank songs that are numerically close, even when the genre fit is not great. After I changed the weights, this became more obvious because high-energy songs were pushed up even if they did not match the user’s main style. The system also uses exact genre and mood matches, so it does not handle “nearby” tastes very well (for example, pop vs indie pop). Because the catalog is small and uneven, users who like underrepresented genres can get less relevant recommendations.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

I tested six profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Conflicting Vibe (happy + very high energy), Sparse Preference (only energy), and Out-of-Range Energy. I looked at whether the top songs matched the profile's intended vibe and whether the reason strings made sense with the score. For the core profiles, results were mostly intuitive: Chill Lofi surfaced Library Rain and Midnight Coding, and Deep Intense Rock surfaced Storm Runner. What surprised me was how often songs like Gym Hero and Sunrise City still appeared across very different profiles, which showed me that energy is currently dominating the ranking more than I expected.

---

## 8. Future Work  

1. Add more user preferences (tempo, valence, danceability, acoustic preference) into scoring.
2. Add a diversity rule so top results are not all from one style.
3. Add soft matching between similar genres and moods instead of exact-only matching.

---

## 9. Personal Reflection  

My biggest learning moment was seeing how one weight change can completely reorder the top songs.
AI tools helped me move faster when writing code and testing profiles, but I still had to double-check outputs, imports, and whether the recommendations actually made sense.
What surprised me most is that a simple point system can still feel like a real recommender, especially when the reasons match what I expected.
At the same time, the same simple logic can over-push one song like Gym Hero across very different users.
If I extend this project, I want to add more preference features and a diversity rule so the top results are not driven by energy alone.
