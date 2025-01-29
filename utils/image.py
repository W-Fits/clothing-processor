from typing import Any, Tuple
from PIL import ImageFile, Image
import numpy as np
from numpy.typing import NDArray
import rembg
import io
import base64
from collections import Counter

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


def remove_background(image_array: NDArray[Any]) -> tuple[NDArray[Any], Image.Image]:
  """Removes background from a NumPy image array -> Image."""
  if image_array is None or image_array.size == 0:
    raise ValueError("Input image array is None or empty.")

  try:
    output_array = rembg.remove(image_array)
    output_image = Image.fromarray(output_array)
  except Exception as e:
    raise ValueError(f"Failed to remove background from the image: {e}")

  return output_array, output_image


def to_bytes_image(image: Image.Image) -> io.BytesIO:
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
  
def to_base64(image: Image.Image) -> str:
  """Convert a PIL Image to a Base64 encoded string."""
  buffer = to_bytes_image(image)
  return base64.b64encode(buffer.read()).decode("utf-8")  # Encode to Base64


def get_colour(image_array: NDArray[Any]) -> str:
  """Find the dominant colour of an image with a removed background -> Hexcode."""
  
  if image_array.shape[-1] != 4:
    raise ValueError("Expected an RGBA image array.")

  pixels = image_array.reshape(-1, 4)
  non_transparent_pixels = pixels[pixels[:, 3] > 10, :3]  # Alpha > 10 to filter near-transparent pixels

  # If only transparent pixels
  if len(non_transparent_pixels) == 0:
    raise ValueError("No visible pixels found in the image.")

  # Get as RBG
  most_common = Counter(map(tuple, non_transparent_pixels)).most_common(1)
  rgb = most_common[0][0]  # (R, G, B)
  
  # Return as hexcode
  return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"