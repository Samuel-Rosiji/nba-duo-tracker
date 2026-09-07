# NBA Duo Tracker

Live site: [nba-duo-tracker.com](https://nba-duo-tracker.com)

## Project Overview

NBA Duo Tracker is a two-man pairing data tracking system that analyses how specific duos perform together. The current version is a prototype covering the 2025/26 regular season and the top 50 duos by minutes played. This information is presented in four ways:

- A scatter plot of the top 100 duos by minutes together, showing the relationship between time on court and plus/minus
- A list of the top 10 duo combinations with a minimum of 500 minutes together
- A combined team plus/minus ranking based on qualifying duos with a minimum of 500 minutes this season
- A passing connection search — enter any player name from the top 50 duos to see passes made and received with their primary duo partner

This project uses `nba_api`, a Python client package for NBA.com's stats endpoints. Data fetched from the NBA API is loaded into a MongoDB database and transformed via aggregation pipelines to produce the statistics shown in the dashboard. The results are exposed as a REST API using FastAPI and visualised in a plain HTML/JS frontend.

## Data Pipeline

1. `fetch.py` pulls two-man lineup data for the full season from NBA.com via `nba_api`
2. `fetch_passing.py` pulls passing connection data for each of the top 50 duos
3. Both datasets are inserted into MongoDB Atlas collections (`lineups` and `passes`)
4. `aggregations.py` defines the MongoDB aggregation pipelines used to transform the raw data
5. `api.py` exposes the transformed data as JSON via FastAPI endpoints
6. `main.py` orchestrates the full pipeline end to end

## Tech Stack

- **Backend** — Python (FastAPI, Uvicorn, pymongo, pandas, nba_api, python-dotenv)
- **Database** — MongoDB Atlas
- **Frontend** — HTML, CSS, JavaScript (Chart.js)
- **Deployment** — Railway (API), Cloudflare Pages (frontend)

## How to Run Locally

1. Install MongoDB Community
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

2. Clone the repo and set up a virtual environment
```bash
git clone https://github.com/Samuel-Rosiji/nba-duo-tracker.git
cd nba-duo-tracker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Create a `.env` file in the project root

MONGO_URI=mongodb://localhost:27017/


4. Populate the database
```bash
python main.py
```

5. Start the API server
```bash
uvicorn api:app --reload
```

6. Open `index.html` in your browser

## API Endpoints

| Endpoint | Description |
|---|---|
| `GET /top_ten_duos?limit=10` | Top duos by minutes together |
| `GET /top_duos_by_team?limit=10` | Teams ranked by combined duo plus/minus (min. 500 mins) |
| `GET /passing/search/{name}` | Passing connection for a player by name (e.g. Kevin Durant)|
| `GET /passing/{player_id}` | Passing connection for a player by NBA player ID |
| `GET /duos/{team}` | All duos for a given team abbreviation (e.g. DEN) |

> **Note:** For local testing, update the `API` variable in `index.html` from the Railway URL to `http://127.0.0.1:8000` before opening the file in your browser.