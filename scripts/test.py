import requests
from PIL import Image
import random
import io

url = 'http://127.0.0.1:8000/upload'

print("Starting test...\n")

# Choose random file id to test with
n = random.randrange(1, 8)

try:
  with open(f'data/test-images/{n}.jpeg', 'rb') as f:
    files = {"upload_file": (f.name, f, "multipart/form-data")}
    res = requests.post(
      url=url, 
      files=files
    )
    
    if res.status_code == 200:
      print(f"{n} successfully processed")
      image = Image.open(io.BytesIO(res.content))
      image.show()
    else:
      print(f"{n} failed")
      print(res.text)

except FileNotFoundError:
  print(f"File {n} not found. Skipping.")
except Exception as e:
  print(f"Error processing file {n}: {str(e)}")

print("\nTest completed.")