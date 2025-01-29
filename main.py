from fastapi import FastAPI, UploadFile, Request, Depends
from fastapi.responses import JSONResponse
from utils.start_server import start_server
from utils.image import to_image_array, remove_background, preprocess_image, to_base64
from utils.files import get_image
from utils.predictions import load_model, predict_class
from utils.auth import auth0_auth_middleware

# Initialise FastAPI app
app = FastAPI()

# Load tensorflow model
model = load_model()

@app.post("/", dependencies=[Depends(auth0_auth_middleware)])
async def upload_image(upload_file: UploadFile | None = None):
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
    preprocessed_image = preprocess_image(image_bg_removed)

    # Make predictions
    predicted_class = predict_class(model, preprocessed_image)

    # Convert the image to a Base64 string
    image_base64 = to_base64(image_bg_removed)

    response_content = {
      "image": image_base64,
      "class": predicted_class
    }

    return JSONResponse(content=response_content)

  except Exception as e:
    return JSONResponse(content={"error": f"Couldn't process image: {str(e)}"}, status_code=500)

if __name__ == "__main__":
  start_server()