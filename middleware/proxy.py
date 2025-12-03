from fastapi import Request
from fastapi.responses import JSONResponse
from cache import cache
import httpx

origin = "https://dummyjson.com"

async def proxy_cache_middleware(request: Request, call_next):

    if request.url.path.startswith("/products"):
        cache_key = str(request.url)

        # Check cache → HIT
        if cache_key in cache:
            return JSONResponse(content=cache[cache_key], headers={"X-CACHE": "HIT"})

       
    response = await call_next(request)
    
    # For other paths not cached → forward normally
    return response
    


  
  
  