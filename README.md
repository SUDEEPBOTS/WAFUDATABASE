<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=200&section=header&text=Waifu%20Database&fontSize=70&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Secure%20%26%20Private%20Waifu%20API%20%7C%20Powered%20by%20FastAPI%20%2B%20MongoDB&descAlignY=60&descSize=17" width="100%"/>

</div>

<div align="center">

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=20&duration=3000&pause=800&color=EC4899&center=true&vCenter=true&multiline=true&width=620&height=80&lines=🌸+The+Ultimate+Waifu+Database+API;⚡+Built+with+FastAPI+%2B+MongoDB;🔐+Secure+Key+Authentication+System)](https://git.io/typing-svg)

</div>

---

<div align="center">

[![Stars](https://img.shields.io/github/stars/SUDEEPBOTS/WAFUDATABASE?style=for-the-badge&logo=github&color=ec4899&labelColor=1a1a2e)](https://github.com/SUDEEPBOTS/WAFUDATABASE/stargazers)
[![Forks](https://img.shields.io/github/forks/SUDEEPBOTS/WAFUDATABASE?style=for-the-badge&logo=github&color=a855f7&labelColor=1a1a2e)](https://github.com/SUDEEPBOTS/WAFUDATABASE/network/members)
[![Issues](https://img.shields.io/github/issues/SUDEEPBOTS/WAFUDATABASE?style=for-the-badge&logo=github&color=f43f5e&labelColor=1a1a2e)](https://github.com/SUDEEPBOTS/WAFUDATABASE/issues)
[![Repo Size](https://img.shields.io/github/repo-size/SUDEEPBOTS/WAFUDATABASE?style=for-the-badge&logo=github&color=f59e0b&labelColor=1a1a2e)](https://github.com/SUDEEPBOTS/WAFUDATABASE)
[![Last Commit](https://img.shields.io/github/last-commit/SUDEEPBOTS/WAFUDATABASE?style=for-the-badge&logo=git&color=14b8a6&labelColor=1a1a2e)](https://github.com/SUDEEPBOTS/WAFUDATABASE/commits)

</div>

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![Python](https://img.shields.io/badge/Python_3.11-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

</div>

---

<div align="center">

## 🌐 Live API Base URL

### **`https://wafus.vercel.app`**

[![API Docs](https://img.shields.io/badge/Swagger%20UI%20Docs-/docs-ec4899?style=for-the-badge&logo=swagger&logoColor=white)](https://wafus.vercel.app/docs)
[![Ping](https://img.shields.io/badge/API%20Status-/Ping-22c55e?style=for-the-badge&logo=statuspage&logoColor=white)](https://wafus.vercel.app/Ping)

</div>

---

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24&height=4" width="100%"/>

## 📡 API Endpoints

### 🔓 Public Endpoints — No Key Required

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | [`/`](https://wafus.vercel.app/) | 🔑 Auto-generate a new API key |
| `GET` | [`/Ping`](https://wafus.vercel.app/Ping) | 🟢 Check if API is alive |
| `GET` | [`/Stats`](https://wafus.vercel.app/Stats) | 📊 Total waifu count in DB |
| `GET` | [`/Random`](https://wafus.vercel.app/Random) | 🎲 Get a random waifu |
| `GET` | [`/Find?name=`](https://wafus.vercel.app/Find?name=rem) | 🔍 Search waifu by name |
| `GET` | [`/List?skip=0&limit=50`](https://wafus.vercel.app/List) | 📋 Paginated waifu list |

### 🔐 Protected Endpoints — API Key Required (`x-api-key` header)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/Waifuadd` | ➕ Add a new waifu to database |
| `PUT` | `/Update?name=` | ✏️ Update waifu fields by name |
| `DELETE` | `/Rmwafus?name=` | 🗑️ Delete waifu records by name |

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24&height=4" width="100%"/>

---

## 🔑 Authentication

**Step 1** — Hit the root endpoint to auto-generate your API key:
```bash
GET https://wafus.vercel.app/
```
```json
{
  "status": "success",
  "api_key": "YUKI_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "instruction": "Provide this key in the 'x-api-key' header."
}
```

**Step 2** — Pass it in every protected request:
```bash
curl -H "x-api-key: YUKI_xxxx..." https://wafus.vercel.app/Waifuadd
```

> ⚠️ **Store your key safely.** Each visit to `/` generates a new key.

---

## 📦 Request & Response Examples

<details>
<summary><b>🎲 GET /Random — Random Waifu</b></summary>

```json
{
  "status": "success",
  "data": {
    "_id": "64f3a...",
    "id": "8492",
    "waifu_id": "8492",
    "name": "Rem",
    "img_url": "https://example.com/rem.jpg",
    "rarity": "Legendary",
    "event_tag": "Standard",
    "added_by": "Sudeep"
  }
}
```
</details>

<details>
<summary><b>➕ POST /Waifuadd — Add Waifu (Protected)</b></summary>

**Request Body:**
```json
{
  "name": "Zero Two",
  "img_url": "https://example.com/zerotwo.jpg",
  "rarity": "Legendary",
  "event_tag": "Valentine",
  "source_message_id": 1234,
  "added_by": "Sudeep"
}
```
**Response:**
```json
{
  "status": "success",
  "message": "Successfully added 'Zero Two' to the database.",
  "waifu_id": "53781",
  "added_by": "Sudeep"
}
```
</details>

<details>
<summary><b>✏️ PUT /Update — Update Waifu (Protected)</b></summary>

**Request:** `PUT /Update?name=Rem`
```json
{
  "rarity": "Mythic",
  "event_tag": "Anniversary"
}
```
**Response:**
```json
{
  "status": "success",
  "message": "Successfully updated 2 record(s) matching the name 'Rem'."
}
```
</details>

<details>
<summary><b>🗑️ DELETE /Rmwafus — Remove Waifu (Protected)</b></summary>

**Request:** `DELETE /Rmwafus?name=Zero Two`
```json
{
  "status": "success",
  "message": "Successfully deleted 1 record(s) matching the name 'Zero Two'."
}
```
</details>

---

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24&height=4" width="100%"/>

## 🚀 Self-Host / Deploy

### ☁️ Deploy on Vercel (Recommended)

<div align="center">

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/SUDEEPBOTS/WAFUDATABASE)

</div>

### 🖥️ Run Locally

<details>
<summary><b>📋 Click to expand local setup guide</b></summary>

<br>

**1️⃣ Clone the Repo**
```bash
git clone https://github.com/SUDEEPBOTS/WAFUDATABASE.git
cd WAFUDATABASE
```

**2️⃣ Create Virtual Environment**
```bash
python3.11 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

**4️⃣ Set Environment Variable**
```bash
export MONGODB_URI="your_mongodb_connection_string"
```

**5️⃣ Run the Server**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

**6️⃣ Open Swagger Docs**
```
http://localhost:8000/docs
```

</details>

---

## ⚙️ Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `MONGODB_URI` | ✅ Yes | Your MongoDB connection string |

---

## 📊 Repo Activity

<div align="center">

![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=SUDEEPBOTS&repo=WAFUDATABASE&theme=tokyo-night&hide_border=true&area=true&color=ec4899&line=a855f7&point=ffffff)

</div>

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=SUDEEPBOTS/WAFUDATABASE&type=Date&theme=dark)](https://star-history.com/#SUDEEPBOTS/WAFUDATABASE&Date)

</div>

---

## 🤝 Contact & Support

<div align="center">

[![Owner](https://img.shields.io/badge/Owner-Sudeep_Boss-ec4899?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Zcziiy)
[![Telegram](https://img.shields.io/badge/Support-Telegram-a855f7?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Zcziiy)

</div>

---

<div align="center">

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=15&duration=3000&pause=500&color=EC4899&center=true&vCenter=true&width=500&lines=⭐+Star+the+repo+if+it+helped+you!;🍴+Fork+%26+build+something+cool!;💖+Made+with+love+by+Sudeep+Boss)](https://git.io/typing-svg)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=120&section=footer" width="100%"/>

</div>

