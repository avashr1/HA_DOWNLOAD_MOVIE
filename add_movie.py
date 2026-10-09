import json

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify,request
import sqlite3
import os

load_dotenv()

# Configuration is read from environment variables (or a local .env file).
# See .env.example for the full list.
RADARR_URL = os.environ["RADARR_URL"].rstrip("/")
API_KEY = os.environ["RADARR_API_KEY"]
QUALITY_PROFILE_ID = int(os.environ.get("RADARR_QUALITY_PROFILE_ID", "1"))
ROOT_FOLDER_PATH = os.environ["RADARR_ROOT_FOLDER_PATH"]

app = Flask(__name__)



@app.route('/add-movie',methods=['POST'])
def add_movie():

        data = request.get_json()

        movie_id = data.get('imdb_id')

        headers = {
            "X-Api-Key": API_KEY,
            "Content-Type": "application/json"
        }

        # do movie lookup
        url = RADARR_URL + '/api/v3/movie/lookup/imdb'
        response = requests.get(url, headers=headers, params={'imdbId': movie_id})

        v_lookup = response.json()

        v_title = v_lookup['title']
        v_tmdbId = v_lookup['tmdbId']

        movie_data = {
            "title": v_title,
            "tmdbId": v_tmdbId,
            "imdbId": movie_id,
            "qualityProfileId": QUALITY_PROFILE_ID,
            "rootFolderPath": ROOT_FOLDER_PATH,
            "monitored": True,
            "addOptions": {
                "searchForMovie": True
            }
        }

        json_payload = json.dumps(movie_data)

        response_post = requests.post(RADARR_URL + '/api/v3/movie', headers=headers, json=movie_data)
        return jsonify({"success": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
