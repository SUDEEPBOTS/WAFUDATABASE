import os
from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel
import pymongo
import secrets

app = FastAPI(title="Waifu Database API", description="Secure and Private Waifu Database Management API")

# Fetching Database Connection from Environment Variables
URI = os.getenv("MONGODB_URI")

if not URI:
    raise RuntimeError("Critical Error: MONGODB_URI environment variable is not set.")

client = pymongo.MongoClient(URI, serverSelectionTimeoutMS=5000)
db = client['Waifuimm']
waifu_col = db['characters']
keys_col = db['api_keys'] 

class WaifuItem(BaseModel):
    name: str
    img_url: str
    rarity: str = "Common"
    event_tag: str = "Standard"
    source_message_id: int = 0
    added_by: str

def verify_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="Missing API Key. Please provide the 'x-api-key' header.")
    if not keys_col.find_one({"key": x_api_key}):
        raise HTTPException(status_code=403, detail="Invalid or unauthorized API Key provided.")
    return x_api_key

@app.get("/")
def home_generate_key():
    new_key = "YUKI_" + secrets.token_hex(16)
    keys_col.insert_one({"key": new_key, "owner": "Admin"})
    return {
        "status": "success",
        "message": "Welcome to the Waifu Database API.",
        "api_key": new_key,
        "instruction": "Please store this API key securely. It must be provided in the 'x-api-key' header for authenticated requests (/Waifuadd, /Rmwafus)."
    }

@app.get("/Ping")
def ping():
    return {"status": "success", "message": "API is operational and running smoothly."}

@app.get("/Stats")
def stats():
    total = waifu_col.count_documents({})
    return {"status": "success", "total_records": total, "database": "Waifuimm"}

@app.get("/Random")
def get_random():
    random_waifu = list(waifu_col.aggregate([{"$sample": {"size": 1}}]))
    if random_waifu:
        waifu = random_waifu[0]
        waifu['_id'] = str(waifu['_id'])
        return {"status": "success", "data": waifu}
    return {"status": "failed", "message": "No records found in the database."}

@app.post("/Waifuadd")
def add_waifu(waifu: WaifuItem, api_key: str = Depends(verify_key)):
    data = waifu.dict()
    waifu_col.insert_one(data)
    return {
        "status": "success", 
        "message": f"Successfully added '{waifu.name}' to the database.",
        "added_by": waifu.added_by
    }

@app.delete("/Rmwafus")
def rm_waifu(name: str, api_key: str = Depends(verify_key)):
    result = waifu_col.delete_many({"name": name})
    if result.deleted_count > 0:
        return {"status": "success", "message": f"Successfully deleted {result.deleted_count} record(s) matching the name '{name}'."}
    raise HTTPException(status_code=404, detail=f"No records found matching the name '{name}'.")
  
