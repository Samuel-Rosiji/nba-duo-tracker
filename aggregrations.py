from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["nba_duos"]

def top_duos_by_plus_minus(limit=10):
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
    
    results = collection.aggregate(pipeline)
    for doc in results:
        print(doc)

if __name__ == "__main__":
    top_duos_by_plus_minus()