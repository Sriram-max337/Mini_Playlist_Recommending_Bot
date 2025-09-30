🎧 Psycho Playlist Recommender Bot

A silly idea turned into a working mini-app 
This Python + JSON CLI bot recommends playlists randomly without repeating until you’ve cycled through them all. And yes… it even remembers your history across runs.

🚀 Features

Add or delete playlists easily.

Get random recommendations without repeats until every playlist is suggested.

Persists your playlists & history using JSON (mini DB style).

Shows already recommended playlists (history check).

Shuffles fresh once all are seen → “Psycho bot resets cycle”.

Simple CLI menu, user-friendly flow, with tiny UX vibes (time.sleep() magic ✨).

🛠️ Tech Used

Python (core logic, CLI flow)

JSON (persistent storage)

os (auto-create JSON file on first run)

time (smooth UX pacing)

📖 Usage

Clone this repo.

Run the script:

python Playlistbot.py


Follow the menu:

1. Add Playlist
2. Del Playlist
3. Get Rec
4. Show all the Playlists
5. Show already recommended playlists
6. Exit

💡 Example
🎧 Recommended : Leo
🎧 Recommended : KGF
Playlist Shuffled by Psycho bot New-Fresh Recs...
🎧 Recommended : Vikram

🎯 Learnings

Logic & conditional flow

File I/O (JSON dump/load)

Error handling

State management

Basic CLI UX thinking

🤡 Why I built this

Started with silly scripts → ended up building something actually useful and fun.
Also… a little dopamine hit before jumping back into DSA grind �
