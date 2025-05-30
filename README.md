# 🎵 Spotify ETL Pipeline

This project extracts track metadata from the Spotify Web API and stores it into a MySQL database for analysis and reporting. It automates the ETL (Extract, Transform, Load) process using Python and Spotipy, making it easier to collect, manage, and query Spotify track data.

## 🚀 Features

- Extracts track data (name, artist, album, popularity, duration) from Spotify URLs.
- Cleans and transforms track information.
- Stores the data into a MySQL database table (`spotify_tracks`).
- Includes SQL scripts for:
  - Most popular track
  - Average popularity
  - Tracks longer than 4 minutes
  - Popularity classification (Very Popular, Popular, Less Popular)

## 🧰 Tech Stack

- **Python 3.x**
- **Spotipy** – Python client for the Spotify Web API
- **MySQL** – Relational database for data storage
- **SQL** – For querying and analyzing data