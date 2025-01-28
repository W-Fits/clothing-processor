from typing import Any
from PIL import ImageFile, Image
import numpy as np
from numpy.typing import NDArray
import rembg
import io

def to_image_array(image: ImageFile.Image) -> NDArray[Any]:
  """Converts a PIL Image to a NumPy array -> NDArray[Any]."""
  if image is None:
    raise ValueError("Input image is None.")
  
  try:
    image_array = np.array(image)
  except Exception as e:
    raise ValueError(f"Failed to convert image to NumPy array: {e}")
  
  if image_array.size == 0:
    raise ValueError("Produced an empty image array.")

  return image_array


def remove_background(image_array: NDArray[Any]) -> Image:
  """Removes background from a NumPy image array -> Image."""
  if image_array is None or image_array.size == 0:
    raise ValueError("Input image array is None or empty.")

  try:
    output_array = rembg.remove(image_array)
    output_image = Image.fromarray(output_array)
  except Exception as e:
    raise ValueError(f"Failed to remove background from the image: {e}")

  return output_image


def to_bytes_image(image: Image) -> io.BytesIO:
  """Converts a PIL Image to a BytesIO object -> io.BytesIO."""
  try:
    bytes_image = io.BytesIO()
    image.save(bytes_image, format='PNG')
    bytes_image.seek(0)
    return bytes_image
  
  except Exception as e:
    raise ValueError(f"Error converting image to bytes: {e}")


def preprocess_image(image: Image.Image) -> NDArray[Any]:
  """Prepares a PIL Image for model input -> NDArray[Any]."""
  if not isinstance(image, Image.Image):
    raise ValueError("Input must be a valid PIL Image.")

  try:
    # Convert to grayscale and resize to 28x28
    image = image.convert('L').resize((28, 28))
    # Convert to numpy array and normalise to [0, 1]
    image_array = np.array(image) / 255.0
    # Add channel and batch dimensions: (1, 28, 28, 1)
    image_array = np.expand_dims(image_array, axis=(0, -1))
    return image_array
  
  except Exception as e:
    raise ValueError(f"Error during image preprocessing: {e}")