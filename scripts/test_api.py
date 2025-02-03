import requests
import random
import json
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Auth0 Config
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
AUTH0_AUDIENCE = os.getenv("AUTH0_AUDIENCE")
TOKEN_URL = f"https://{AUTH0_DOMAIN}/oauth/token"

UPLOAD_URL = "http://127.0.0.1:8000/"

def get_auth0_token():
  """Fetch an Auth0 access token."""
  try:
    res = requests.post(
      TOKEN_URL,
      headers={"Content-Type": "application/json"},
      data=json.dumps({
        "client_id": AUTH0_CLIENT_ID,
        "client_secret": AUTH0_CLIENT_SECRET,
        "audience": AUTH0_AUDIENCE,
        "grant_type": "client_credentials"
      }),
    )
    res.raise_for_status()
    return res.json().get("access_token")
  except requests.exceptions.RequestException as e:
    print(f"Error fetching Auth0 token: {e}")
    return None

def test_upload():
  """Test uploading an image with the fetched token."""
  print("Starting test...\n")
  
  token = get_auth0_token()
  if not token:
    print("Failed to retrieve token. Exiting.")
    return
  
  n = random.randrange(1, 8)  # Choose random file ID

  try:
    with open(f"data/test-images/{n}.jpeg", "rb") as f:
      files = {"upload_file": (f.name, f, "multipart/form-data")}
      res = requests.post(
        url=UPLOAD_URL,
        headers={"Authorization": f"Bearer {token}"},
        files=files,
      )

      if res.status_code == 200:
        print(f"{n} successfully processed")
        print(res.content)
      else:
        print(f"{n} failed with status {res.status_code}")
        print(res.text)

  except FileNotFoundError:
    print(f"File {n} not found. Skipping.")
  except Exception as e:
    print(f"Error processing file {n}: {str(e)}")

  print("\nTest completed.")

if __name__ == "__main__":
  test_upload()