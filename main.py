import argparse
import uvicorn
from fastapi import FastAPI

app = FastAPI()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port",    type=int, default=3000)
    args = parser.parse_args()

    uvicorn.run("main:app", host="127.0.0.1", port=args.port, reload=True)