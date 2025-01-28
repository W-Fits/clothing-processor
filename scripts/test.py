import requests

url = 'http://127.0.0.1:8000/upload'

print("Starting test...\n")

res = requests.post(url=url, headers={
  "hello": "world"
})

print(res.text)

print("\nTest completed.")