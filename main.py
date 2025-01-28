from fastapi import FastAPI, UploadFile, File, Request
import uvicorn

app = FastAPI()

#  image_file: UploadFile = File(...)

@app.post("/upload/")
async def upload_image(request: Request):
  return request.headers


def start_server():
  """Start API server"""
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
  start_server()