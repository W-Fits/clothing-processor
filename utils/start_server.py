import uvicorn

def start_server():
  """Start API server"""
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
