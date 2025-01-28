from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import JSONResponse, StreamingResponse
from utils.start_server import start_server
from utils.image import to_image_array, remove_background, preprocess_image, to_bytes_image
from utils.files import get_image

app = FastAPI()

@app.post("/upload")
async def upload_image(request: Request, upload_file: UploadFile | None = None):
  # Check file has been uploaded
  if not upload_file:
    return JSONResponse(content={"error": "File not provided"}, status_code=422)
  
  try:
    # Get file content as image
    # (also checks if `upload_file` is an image)
    content_image = await get_image(upload_file)

    # Convert image to bytes array
    image_array = to_image_array(content_image)

    # Remove image background
    image_bg_removed = remove_background(image_array)

    # Preprocess image for model (convert 28x28, greyscale, etc.)
    # TODO: implement model for annotations
    preprocessed_image = preprocess_image(image_bg_removed)

    # Convert to bytes image so it can be returned
    output_image = to_bytes_image(image_bg_removed)

    response_content = {
      "image": output_image,
    }

    return StreamingResponse(output_image, media_type="image/png")

  except Exception as e:
    return JSONResponse(content={"error": f"Couldn't process image: {str(e)}"}, status_code=500)

if __name__ == "__main__":
  start_server()