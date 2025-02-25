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

def push_env():
  """Run the push_env"""
  import scripts.push_env
  scripts.push_env.main()

def main():
  parser = argparse.ArgumentParser(
    description="Run a specified script.",
    formatter_class=argparse.RawTextHelpFormatter
  )
  
  functions = {
    "test_api": test_api,
    "test_random_colour_match": test_random_colour_match,
    "test_image_colour_match": test_image_colour_match,
    "push_env": push_env,
  }
  
  functions_list = "\n\t".join(functions.keys())
  parser.add_argument(
    "function",
    choices=functions.keys(),
    help=f"\nAvailable scripts:\n\t{functions_list}"
  )
  
  args = parser.parse_args()
  
  # Call the selected function
  functions[args.function]()

if __name__ == "__main__":
  main()