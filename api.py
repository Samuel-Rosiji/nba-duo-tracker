from fastapi import FastAPI, HTTPException
from db import db 
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()

collection = db["lineups"]



@app.get("/top_ten_duos", response_description="List top 20 duos")
def get_top_ten_duos(limit: int=10): 
    collection = db["lineups"]
    pipeline = [
            {"$sort":{"MIN": -1}},
            {"$limit": limit}
      ]
    output = list(collection.aggregate(pipeline))
    for doc in output:
        doc["_id"] = str(doc["_id"])
    return JSONResponse(content=output)

@app.get("/top_duos_by_team", response_description="List of two duos for each team")
def get_top_duos_by_team(limit: int=10):
    collection = db["lineups"]
        
    pipeline = [
            # your stages here
            {"$match": {"MIN": {
                "$gte": 1000 
            }} }, 
            {"$group": {
                "_id": "$TEAM_ABBREVIATION",
                "combined_plus_minus": {"$sum": "$PLUS_MINUS"}
            }}, 
            {"$sort": {
                "combined_plus_minus": -1 
            } }, 
            {"$limit": 10},
            {"$project": {
                "_id": 0,
                "TEAM_ABBREVIATION": "$_id",
                "combined_plus_minus": 1 
            }}
        ]
        
    results = list(collection.aggregate(pipeline))
    return JSONResponse(content=results)

@app.get("/passing/{player_id}")
def get_passing(player_id: int):
    collection = db["passes"]
    result = list(collection.find({"PLAYER_ID": player_id}))
    for doc in result:
        doc["_id"] = str(doc["_id"])
    return JSONResponse(content=result)

@app.get("/duos/{team}")
def get_duos_by_team(team: str):
    collection = db["lineups"]
    result = list(collection.find({"TEAM_ABBREVIATION": team}))
    for doc in result:
        doc["_id"] = str(doc["_id"])
    return JSONResponse(content=result)
