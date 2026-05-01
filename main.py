import os
from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel
import pymongo
import secrets
from typing import Optional

app = FastAPI(title="Waifu Database API", description="Secure and Private Waifu Database Management API")

# Fetching Database Connection from Environment Variables
URI = os.getenv("MONGODB_URI")

if not URI:
    raise RuntimeError("Critical Error: MONGODB_URI environment variable is not set.")

client = pymongo.MongoClient(URI, serverSelectionTimeoutMS=5000)
db = client['Waifuimm']
waifu_col = db['characters']
keys_col = db['api_keys'] 

# --- Models ---
class WaifuItem(BaseModel):
    name: str
    img_url: str
    rarity: str = "Common"
    event_tag: str = "Standard"
    source_message_id: int = 0
    added_by: str

class WaifuUpdateItem(BaseModel):
    img_url: Optional[str] = None
    rarity: Optional[str] = None
    event_tag: Optional[str] = None
    source_message_id: Optional[int] = None

# --- Security ---
def verify_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="Missing API Key. Please provide the 'x-api-key' header.")
    if not keys_col.find_one({"key": x_api_key}):
        raise HTTPException(status_code=403, detail="Invalid or unauthorized API Key provided.")
    return x_api_key

# --- Endpoints ---

@app.get("/")
def home_generate_key():
    new_key = "YUKI_" + secrets.token_hex(16)
    keys_col.insert_one({"key": new_key, "owner": "Admin"})
    return {
        "status": "success",
        "message": "Welcome to the Waifu Database API.",
        "api_key": new_key,
        "instruction": "Please store this API key securely. It must be provided in the 'x-api-key' header for authenticated requests (/Waifuadd, /Update, /Rmwafus)."
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

@app.get("/Find")
def find_waifu(name: str):
    """Search for a waifu by name (Case-insensitive)"""
    # $regex and $options: 'i' makes the search case-insensitive and allows partial matches
    results = list(waifu_col.find({"name": {"$regex": name, "$options": "i"}}))
    
    if not results:
        raise HTTPException(status_code=404, detail=f"No records found matching the name '{name}'.")
    
    for doc in results:
        doc['_id'] = str(doc['_id'])
        
    return {"status": "success", "total_found": len(results), "data": results}

@app.get("/List")
def list_waifus(skip: int = 0, limit: int = 50):
    """Retrieve a paginated list of waifus"""
    results = list(waifu_col.find().skip(skip).limit(limit))
    
    for doc in results:
        doc['_id'] = str(doc['_id'])
        
    return {"status": "success", "showing": len(results), "skip": skip, "limit": limit, "data": results}

@app.post("/Waifuadd")
def add_waifu(waifu: WaifuItem, api_key: str = Depends(verify_key)):
    data = waifu.dict()
    waifu_col.insert_one(data)
    return {
        "status": "success", 
        "message": f"Successfully added '{waifu.name}' to the database.",
        "added_by": waifu.added_by
    }

@app.put("/Update")
def update_waifu(name: str, update_data: WaifuUpdateItem, api_key: str = Depends(verify_key)):
    """Update specific fields of an existing waifu (Requires API Key)"""
    # Filter out fields that were not provided (None values)
    update_fields = {k: v for k, v in update_data.dict().items() if v is not None}
    
    if not update_fields:
        raise HTTPException(status_code=400, detail="No valid fields provided for update.")
        
    result = waifu_col.update_many({"name": name}, {"$set": update_fields})
    
    if result.modified_count > 0:
        return {"status": "success", "message": f"Successfully updated {result.modified_count} record(s) matching the name '{name}'."}
    
    raise HTTPException(status_code=404, detail=f"No records found or no changes made for the name '{name}'.")

@app.delete("/Rmwafus")
def rm_waifu(name: str, api_key: str = Depends(verify_key)):
    result = waifu_col.delete_many({"name": name})
    if result.deleted_count > 0:
        return {"status": "success", "message": f"Successfully deleted {result.deleted_count} record(s) matching the name '{name}'."}
    raise HTTPException(status_code=404, detail=f"No records found matching the name '{name}'.")
    
