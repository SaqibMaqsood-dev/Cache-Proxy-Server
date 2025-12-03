from fastapi import FastAPI , Request , APIRouter
from fastapi.responses import  JSONResponse
from cache import cache



import httpx
router = APIRouter()


origin = "https://dummyjson.com"


router = APIRouter()

@router.get("/products/{id}")
async def get_products_by_id(id : int  ,  request : Request):
    async with httpx.AsyncClient() as client :
        cache_key = str(request.url.path)

        if cache_key in cache:
            return JSONResponse(content=cache[cache_key], headers={"X-CACHE": "HIT"})
        
        url = origin + request.url.path
        data = await  client.get(url)   
        cache[cache_key] = data.json()
        print(cache)
        
         # MISS → fetch from origin
        
        return JSONResponse(content=data.json() , headers={"X-CACHE" : "MISS"})
    