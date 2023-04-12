import uvicorn
from routers.products import *

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    