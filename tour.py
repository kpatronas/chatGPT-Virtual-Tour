from fastapi import FastAPI,APIRouter,Response,Request
from pydantic import BaseModel
import uvicorn
import json
import openai
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(middleware=[ Middleware(CORSMiddleware, allow_origins=["*"])])
api_router = APIRouter()

class Coor(BaseModel):
    lon: float
    lat: float

@api_router.get('/api/tour/')
async def get_endpoint(lon:str,lat:str) -> dict:
    """ GET Request """
    response                = {}
    response['body']        = {}
    response['status_code'] = 0

    try:
        openai.api_key = 'REPLACE-THIS-WITH-YOUR-OPENAI-KEY'
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[ {"role": "user", "content": "Can you tell me historical info about place with longitude: %s and latitude: %s, also some nice sights to visit and a video with most views in youtube as embedded video"%(lon,lat)}])

        coor = {}
        coor['lon']  = lon
        coor['lat']  = lat
        coor['tour'] = completion.choices[0].message.content
        response['body']        = coor
        response['status_code'] = 200
    except Exception as ex:
        response['body']        = str(ex)
        response['status_code'] = 500

    return Response(content     = json.dumps(response['body'],indent=4),
                    media_type  = "application/json",
                    status_code = response['status_code'])

app.include_router(api_router)

if __name__ == '__main__':

    uvicorn.run(app, host = "0.0.0.0", port = 8001, log_level = "debug")
