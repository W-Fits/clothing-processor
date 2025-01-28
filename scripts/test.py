import requests

url = 'http://127.0.0.1:8000/upload'

print("Starting test...\n")

for i in range(1, 8 + 1):
  try:
    with open(f'data/test-images/{i}.jpeg', 'rb') as file:
      obj = {'image': file}
      res = requests.post(
        url=url, 
        files=obj
      )
      
      if res.status_code == 200:
        print(f"{i} successfully processed")
      else:
        print(f"{i} failed")
        print(res.text)

  except FileNotFoundError:
    print(f"File {i} not found. Skipping.")
  except Exception as e:
    print(f"Error processing file {i}: {str(e)}")

print("\nTest completed.")