import argparse

def test_api():
  """Run the test_api script"""
  import scripts.test_api
  scripts.test_api.test_upload()

def test_random_colour_match():
  """Run the test_colour_match"""
  import scripts.test_colour_match
  scripts.test_colour_match.random_colour_match()

def test_image_colour_match():
  """Run the test_colour_match"""
  import scripts.test_colour_match
  scripts.test_colour_match.image_colour_match()

def main():
  parser = argparse.ArgumentParser(description="Run a specified test function.")
  parser.add_argument("function", choices=["test_api", "test_random_colour_match", "test_image_colour_match"],
                      help="Name of the function to run")
  args = parser.parse_args()
  
  # Call the selected function
  globals()[args.function]()

if __name__ == "__main__":
  main()