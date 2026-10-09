# HA_DOWNLOAD_MOVIE

A small Flask service that adds a movie to [Radarr](https://radarr.video/) by IMDb ID
and starts a search for it. You can call it from Home Assistant or any other HTTP client.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # then edit .env with your own values
python add_movie.py
```

### Configuration

All settings come from environment variables (or a `.env` file in the project root):

| Variable                     | Description                                        |
|------------------------------|----------------------------------------------------|
| `RADARR_URL`                 | Base URL of Radarr, e.g. `http://radarr:7878`      |
| `RADARR_API_KEY`             | Radarr API key (Settings > General > Security)     |
| `RADARR_QUALITY_PROFILE_ID`  | Quality profile ID for new movies (default `1`)    |
| `RADARR_ROOT_FOLDER_PATH`    | Root folder where Radarr stores movies             |

Keep your `.env` file out of version control. It is already listed in `.gitignore`.

## Usage

```bash
curl -X POST http://localhost:5000/add-movie \
     -H "Content-Type: application/json" \
     -d '{"imdb_id": "tt0111161"}'
```
