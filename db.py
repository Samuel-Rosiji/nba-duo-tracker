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

def insert_passing(passes_made, passes_received):
      collection = db["passes"]
      passes_made_records = passes_made.to_dict(orient="records")
      passes_received_records = passes_received.to_dict(orient="records")

      try:
            result_passes_made = collection.insert_many(passes_made_records)
            if len(result_passes_made.inserted_ids) == len(passes_made_records):
                  print(f"Successfully inserted {len(result_passes_made.inserted_ids)} documents into passes collection")
            else:
                  print(f"Warning exepected {len(passes_made_records)} but got {len(result_passes_made.inserted_ids)} documents into passes collection")

      except Exception as e:
            print(f"Insert failed: {e}")

      try:
             result_passes_received = collection.insert_many(passes_received_records)
             if len(result_passes_received.inserted_ids) == len(passes_received_records):
                   print(f"Successfully inserted {len(result_passes_received.inserted_ids)} documents into passes collection")
             else:
                   print(f"Warning exepected {len(passes_received_records)} but got {len(result_passes_received.inserted_ids)} documents into passes collection")
                   
      except Exception as e:
            print(f"Insert failed: {e}")

def get_top_duos(limit =20):
      collection = db["lineups"]
      pipeline = [
            {"$sort":{"MIN": -1}},
            {"$limit": limit}
      ]
      return list(collection.aggregate(pipeline))
            
