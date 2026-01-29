import requests
import json

import os
from dotenv import load_dotenv


load_dotenv(dotenv_path="/Users/eshwar/Documents/YoutubeDataAnalysis/.env",override=True)

# from dotenv import dotenv_values

# config = dotenv_values("/Users/eshwar/Documents/YoutubeDataAnalysis/.env")
# print(config)



API_KEY = os.getenv("API_KEY") 
CHANNEL_NAME = "eshwar7886"

def get_playlist_id():

    try: 


        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_NAME}&key={API_KEY}"

        response = requests.get(url)

        response.raise_for_status

        data = response.json()
        # print(json.dumps(data,indent=4))

        channel_list = data['items'][0]
        channel_playlist_id = channel_list['contentDetails']['relatedPlaylists']['uploads']

        print(channel_playlist_id)
    
    except requests.exceptions.RequestException as e:
        raise e 
    
if __name__ == "__main__":
    get_playlist_id()


    
