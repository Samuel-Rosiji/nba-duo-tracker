from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["nba_duos"]

def insert_lineups(df):
    collection = db["lineups"]
    records = df.to_dict(orient="records")
    collection.drop() # clear old data before reinsterting 

    try:
          result = collection.insert_many(records)
          if len(result.inserted_ids) == len(records):
                print(f"Successfully Inserted {len(result.inserted_ids)} documents into lineups collections")
          else:
                print(f"Warning expected{len(records)} but only inserted {len(result.inserted_ids)}documents into lineups collections")
            
    except Exception as e:
          print(f"Insert failed: {e}")