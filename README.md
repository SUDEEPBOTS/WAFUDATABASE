<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=220&section=header&text=Waifu%20Database%20API&fontSize=65&fontColor=fff&animation=twinkling&fontAlignY=40&desc=🌸%20Complete%20API%20Reference%20%26%20Documentation&descAlignY=62&descSize=18" width="100%"/>

</div>

<div align="center">

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=20&duration=2500&pause=800&color=EC4899&center=true&vCenter=true&multiline=true&width=650&height=85&lines=🔗+Base+URL+→+https%3A%2F%2Fwafus.vercel.app;⚡+Fast+%7C+Secure+%7C+Easy+to+Use;🌸+Thousands+of+Waifus+at+your+fingertips)](https://git.io/typing-svg)

</div>

<div align="center">

[![Stars](https://img.shields.io/github/stars/SUDEEPBOTS/WAFUDATABASE?style=for-the-badge&logo=github&color=ec4899&labelColor=1a1a2e)](https://github.com/SUDEEPBOTS/WAFUDATABASE/stargazers)
[![Forks](https://img.shields.io/github/forks/SUDEEPBOTS/WAFUDATABASE?style=for-the-badge&logo=github&color=a855f7&labelColor=1a1a2e)](https://github.com/SUDEEPBOTS/WAFUDATABASE/network/members)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
[![API Status](https://img.shields.io/website?url=https%3A%2F%2Fwafus.vercel.app%2FPing&style=for-the-badge&label=API+Status&color=22c55e&labelColor=1a1a2e)](https://wafus.vercel.app/Ping)

</div>

---

<div align="center">

## 🌐 Base URL

# `https://wafus.vercel.app`

[![Open Swagger Docs](https://img.shields.io/badge/Interactive%20Docs-Swagger%20UI-ec4899?style=for-the-badge&logo=swagger&logoColor=white)](https://wafus.vercel.app/docs)

</div>

---

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24&height=4" width="100%"/>

<div align="center">

## 📋 Endpoint Overview

</div>

```
🟢 PUBLIC  — No authentication needed
🔴 PRIVATE — Requires x-api-key header
```

| Badge | Method | Endpoint | What it does |
|-------|--------|----------|--------------|
| 🟢 | `GET` | `/` | Generate a new API Key |
| 🟢 | `GET` | `/Ping` | Check if API is online |
| 🟢 | `GET` | `/Stats` | Total waifus in database |
| 🟢 | `GET` | `/Random` | Get a random waifu |
| 🟢 | `GET` | `/Find?name=` | Search waifu by name |
| 🟢 | `GET` | `/List` | Paginated list of all waifus |
| 🔴 | `POST` | `/Waifuadd` | Add a new waifu |
| 🔴 | `PUT` | `/Update?name=` | Update waifu details |
| 🔴 | `DELETE` | `/Rmwafus?name=` | Delete a waifu |

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24&height=4" width="100%"/>

---

## 🔑 Step 1 — Get Your API Key

> Hit the root endpoint **once** to auto-generate your personal API key.

**Request:**
```http
GET https://wafus.vercel.app/
```

**Response:**
```json
{
  "status": "success",
  "message": "Welcome to the Waifu Database API.",
  "api_key": "YUKI_3f8a21c94e7b...",
  "instruction": "Provide this key in the 'x-api-key' header for protected routes."
}
```

> 💡 **Save this key!** Every time you visit `/`, a brand new key is created.

---

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24&height=4" width="100%"/>

## 🟢 Public Endpoints

---

### 🏓 `/Ping` — Health Check

> Just to make sure the API is alive and responding.

```http
GET https://wafus.vercel.app/Ping
```

```json
{
  "status": "success",
  "message": "API is operational and running smoothly."
}
```

---

### 📊 `/Stats` — Database Statistics

> See how many waifus are currently stored.

```http
GET https://wafus.vercel.app/Stats
```

```json
{
  "status": "success",
  "total_records": 4821,
  "database": "Waifuimm"
}
```

---

### 🎲 `/Random` — Random Waifu

> Returns one completely random waifu from the database. Perfect for gacha-style bots!

```http
GET https://wafus.vercel.app/Random
```

```json
{
  "status": "success",
  "data": {
    "_id": "64f3a9c2b1e4f0001a2b3c4d",
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

---

### 🔍 `/Find` — Search by Name

> Case-insensitive search. Partial names work too — `re` will match `Rem`, `Rei`, `Revy`, etc.

```http
GET https://wafus.vercel.app/Find?name=rem
```

**Parameters:**

| Param | Type | Required | Example |
|-------|------|----------|---------|
| `name` | string | ✅ Yes | `?name=rem` |

```json
{
  "status": "success",
  "total_found": 3,
  "data": [
    {
      "id": "8492",
      "waifu_id": "8492",
      "name": "Rem",
      "img_url": "https://example.com/rem.jpg",
      "rarity": "Legendary",
      "event_tag": "Standard",
      "added_by": "Sudeep"
    }
  ]
}
```

> ❌ **404** if no match found:
> ```json
> { "detail": "No records found matching the name 'xyz'." }
> ```

---

### 📋 `/List` — Paginated Waifu List

> Retrieve all waifus with pagination support. Use `skip` and `limit` to navigate pages.

```http
GET https://wafus.vercel.app/List?skip=0&limit=50
```

**Parameters:**

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `skip` | int | `0` | How many records to skip |
| `limit` | int | `50` | Max records to return per page |

```json
{
  "status": "success",
  "showing": 50,
  "skip": 0,
  "limit": 50,
  "data": [ { "..." } ]
}
```

> 💡 **Page 2:** `?skip=50&limit=50` · **Page 3:** `?skip=100&limit=50`

---

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24&height=4" width="100%"/>

## 🔴 Protected Endpoints

> All protected routes require the `x-api-key` header.

```http
x-api-key: YUKI_your_key_here
```

---

### ➕ `/Waifuadd` — Add a New Waifu

```http
POST https://wafus.vercel.app/Waifuadd
```

**Headers:**
```
x-api-key: YUKI_your_key_here
Content-Type: application/json
```

**Request Body:**

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `name` | string | ✅ | — | Waifu name |
| `img_url` | string | ✅ | — | Direct image URL |
| `rarity` | string | ❌ | `Common` | Common / Rare / Epic / Legendary |
| `event_tag` | string | ❌ | `Standard` | Event label e.g. `Valentine` |
| `source_message_id` | int | ❌ | `0` | Telegram message ID if any |
| `added_by` | string | ✅ | — | Your name / username |

```json
{
  "name": "Zero Two",
  "img_url": "https://example.com/zerotwo.jpg",
  "rarity": "Legendary",
  "event_tag": "Valentine",
  "source_message_id": 0,
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

---

### ✏️ `/Update` — Update Waifu Details

> Updates **all records** matching the given name. Only send fields you want to change.

```http
PUT https://wafus.vercel.app/Update?name=Rem
```

**Headers:**
```
x-api-key: YUKI_your_key_here
Content-Type: application/json
```

**Parameters:**

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ Yes | Exact name to target |

**Request Body** *(only the fields you want to update)*:

```json
{
  "img_url": "https://example.com/rem_new.jpg",
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

> ❌ **400** if body is empty · **404** if name not found

---

### 🗑️ `/Rmwafus` — Delete a Waifu

> Permanently deletes **all records** matching the given name.

```http
DELETE https://wafus.vercel.app/Rmwafus?name=Zero Two
```

**Headers:**
```
x-api-key: YUKI_your_key_here
```

**Parameters:**

| Param | Type | Required |
|-------|------|----------|
| `name` | string | ✅ Yes |

**Response:**
```json
{
  "status": "success",
  "message": "Successfully deleted 1 record(s) matching the name 'Zero Two'."
}
```

> ⚠️ This action is **permanent** and cannot be undone.

---

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24&height=4" width="100%"/>

## ⚠️ Error Reference

| HTTP Code | Meaning | Reason |
|-----------|---------|--------|
| `200` | ✅ Success | Everything worked fine |
| `400` | ❌ Bad Request | Empty or invalid body sent |
| `401` | 🔒 Unauthorized | `x-api-key` header is missing |
| `403` | 🚫 Forbidden | API key is invalid or wrong |
| `404` | 🔍 Not Found | No matching records found in DB |

---

## 📊 Repo Stats

<div align="center">

![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=SUDEEPBOTS&repo=WAFUDATABASE&theme=tokyo-night&hide_border=true&area=true&color=ec4899&line=a855f7&point=ffffff)

[![Star History Chart](https://api.star-history.com/svg?repos=SUDEEPBOTS/WAFUDATABASE&type=Date&theme=dark)](https://star-history.com/#SUDEEPBOTS/WAFUDATABASE&Date)

</div>

---

## 🤝 Support

<div align="center">

[![Owner](https://img.shields.io/badge/Owner-Sudeep_Boss-ec4899?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Zcziiy)
[![Telegram](https://img.shields.io/badge/Contact-Telegram-a855f7?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Zcziiy)

<br>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=15&duration=3000&pause=600&color=EC4899&center=true&vCenter=true&width=500&lines=⭐+Star+this+repo+if+the+API+helped+you!;🍴+Fork+%26+integrate+into+your+bot!;💖+Made+with+love+by+Sudeep+Boss)](https://git.io/typing-svg)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=130&section=footer" width="100%"/>

</div>
