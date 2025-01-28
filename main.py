from fastapi import FastAPI, UploadFile, File, Request
from utils.start_server import start_server

app = FastAPI()

@app.post("/upload/")
async def upload_image(request: Request, image_file: UploadFile = File(...)):
  pass 

if __name__ == "__main__":
  start_server()