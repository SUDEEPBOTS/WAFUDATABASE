<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;customColorList=12,20,24&amp;height=220&amp;section=header&amp;text=𝚆𝚊𝚒𝚏𝚞%20𝙳𝚊𝚝𝚊𝚋𝚊𝚜𝚎%20𝙰𝙿𝙸&amp;fontSize=60&amp;fontColor=fff&amp;animation=twinkling&amp;fontAlignY=40&amp;desc=Complete%20API%20Reference%20and%20Documentation&amp;descAlignY=62&amp;descSize=17" width="100%"/>

</div>

<div align="center">

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=20&duration=2500&pause=800&color=EC4899&center=true&vCenter=true&multiline=true&width=660&height=85&lines=Base+URL+→+https%3A%2F%2Fwafus.vercel.app;6000%2B+Waifus+in+the+Database;Fast+%7C+Secure+%7C+Easy+to+Integrate)](https://git.io/typing-svg)

</div>

<div align="center">

[![Stars](https://img.shields.io/github/stars/SUDEEPBOTS/WAFUDATABASE?style=for-the-badge&logo=github&color=ec4899&labelColor=1a1a2e)](https://github.com/SUDEEPBOTS/WAFUDATABASE/stargazers)
[![Forks](https://img.shields.io/github/forks/SUDEEPBOTS/WAFUDATABASE?style=for-the-badge&logo=github&color=a855f7&labelColor=1a1a2e)](https://github.com/SUDEEPBOTS/WAFUDATABASE/network/members)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
[![API Status](https://img.shields.io/website?url=https%3A%2F%2Fwafus.vercel.app%2FPing&style=for-the-badge&label=API+Status&color=22c55e&labelColor=1a1a2e)](https://wafus.vercel.app/Ping)
![Waifus](https://img.shields.io/badge/Waifus-6000%2B-ec4899?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyMWwtMS40NS0xLjMyQzUuNCAxNS4zNiAyIDEyLjI4IDIgOC41IDIgNS40MiA0LjQyIDMgNy41IDNjMS43NCAwIDMuNDEuODEgNC41IDIuMDlDMTMuMDkgMy44MSAxNC43NiAzIDE2LjUgMyAxOS41OCAzIDIyIDUuNDIgMjIgOC41YzAgMy43OC0zLjQgNi44Ni04LjU1IDExLjE5TDEyIDIxeiIvPjwvc3ZnPg==&labelColor=1a1a2e)

</div>

---

<div align="center">

## ─「 𝙱𝚊𝚜𝚎 𝚄𝚁𝙻 」─

# `https://wafus.vercel.app`

[![Interactive Docs](https://img.shields.io/badge/Interactive%20Docs-Swagger%20UI-ec4899?style=for-the-badge&logo=swagger&logoColor=white)](https://wafus.vercel.app/docs)

</div>

---

<img src="https://capsule-render.vercel.app/api?type=rect&amp;color=gradient&amp;customColorList=12,20,24&amp;height=4" width="100%"/>

## ─「 ˹ 𝙴ɴᴅᴘᴏɪɴᴛ 𝙾ᴠᴇʀᴠɪᴇᴡ ˼ 」─

```
🟢  PUBLIC   —  No authentication needed
🔴  PRIVATE  —  Requires  x-api-key  header
```

| 　 | ˹ 𝙼ᴇᴛʜᴏᴅ ˼ | ˹ 𝙴ɴᴅᴘᴏɪɴᴛ ˼ | ˹ 𝙳ᴇsᴄʀɪᴘᴛɪᴏɴ ˼ |
|---|--------|-----------|-------------|
| 🟢 | `GET` | `/` | Generate a new API Key |
| 🟢 | `GET` | `/Ping` | Check if API is online |
| 🟢 | `GET` | `/Stats` | Total waifus in database |
| 🟢 | `GET` | `/Random` | Get a random waifu |
| 🟢 | `GET` | `/Find?name=` | Search waifu by name |
| 🟢 | `GET` | `/List` | Paginated list of all waifus |
| 🔴 | `POST` | `/Waifuadd` | Add a new waifu |
| 🔴 | `PUT` | `/Update?name=` | Update waifu details |
| 🔴 | `DELETE` | `/Rmwafus?name=` | Delete a waifu |

<img src="https://capsule-render.vercel.app/api?type=rect&amp;color=gradient&amp;customColorList=12,20,24&amp;height=4" width="100%"/>

---

## ─「 ˹ 𝙰𝙿𝙸 𝙺ᴇʏ ˼ 」─

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

> 💡 **Save this key!** Every visit to `/` generates a brand new key.

---

<img src="https://capsule-render.vercel.app/api?type=rect&amp;color=gradient&amp;customColorList=12,20,24&amp;height=4" width="100%"/>

## ─「 ˹ 𝙿ᴜʙʟɪᴄ 𝚁ᴏᴜᴛᴇs ˼ 」─

---

### 🟢 ˹ 𝙿ɪɴɢ ˼ — `/Ping`

> Verify the API is live and operational.

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

### 🟢 ˹ 𝚂ᴛᴀᴛs ˼ — `/Stats`

> Returns the total number of waifus stored. Currently **6000+** and growing!

```http
GET https://wafus.vercel.app/Stats
```
```json
{
  "status": "success",
  "total_records": 6000,
  "database": "Waifuimm"
}
```

---

### 🟢 ˹ 𝚁ᴀɴᴅᴏᴍ ˼ — `/Random`

> Returns one completely random waifu. Perfect for gacha-style Telegram bots!

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

### 🟢 ˹ 𝙵ɪɴᴅ ˼ — `/Find?name=`

> Case-insensitive search. Partial names work — `re` matches `Rem`, `Rei`, `Revy`, etc.

```http
GET https://wafus.vercel.app/Find?name=rem
```

**Parameters:**

| ˹ 𝙿ᴀʀᴀᴍ ˼ | ˹ 𝚃ʏᴘᴇ ˼ | ˹ 𝚁ᴇǫᴜɪʀᴇᴅ ˼ | ˹ 𝙴xᴀᴍᴘʟᴇ ˼ |
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

> ❌ **404** if no match: `{ "detail": "No records found matching the name 'xyz'." }`

---

### 🟢 ˹ 𝙻ɪsᴛ ˼ — `/List`

> Retrieve all waifus with pagination. Navigate pages using `skip` and `limit`.

```http
GET https://wafus.vercel.app/List?skip=0&limit=50
```

**Parameters:**

| ˹ 𝙿ᴀʀᴀᴍ ˼ | ˹ 𝚃ʏᴘᴇ ˼ | ˹ 𝙳ᴇғᴀᴜʟᴛ ˼ | ˹ 𝙳ᴇsᴄʀɪᴘᴛɪᴏɴ ˼ |
|-------|------|---------|-------------|
| `skip` | int | `0` | Records to skip |
| `limit` | int | `50` | Max records per page |

```json
{
  "status": "success",
  "showing": 50,
  "skip": 0,
  "limit": 50,
  "data": [{ "..." }]
}
```

> 💡 **Page 2:** `?skip=50&limit=50` · **Page 3:** `?skip=100&limit=50`

---

<img src="https://capsule-render.vercel.app/api?type=rect&amp;color=gradient&amp;customColorList=12,20,24&amp;height=4" width="100%"/>

## ─「 ˹ 𝙿ʀɪᴠᴀᴛᴇ 𝚁ᴏᴜᴛᴇs ˼ 」─

> All protected routes require the `x-api-key` header.

```http
x-api-key: YUKI_your_key_here
```

---

### 🔴 ˹ 𝚆𝚊𝚒𝚏𝚞𝚊𝚍𝚍 ˼ — `POST /Waifuadd`

```http
POST https://wafus.vercel.app/Waifuadd
Content-Type: application/json
x-api-key: YUKI_your_key_here
```

**Body Fields:**

| ˹ 𝙵ɪᴇʟᴅ ˼ | ˹ 𝚃ʏᴘᴇ ˼ | ˹ 𝚁ᴇǫᴜɪʀᴇᴅ ˼ | ˹ 𝙳ᴇғᴀᴜʟᴛ ˼ | ˹ 𝙳ᴇsᴄʀɪᴘᴛɪᴏɴ ˼ |
|-------|------|----------|---------|-------------|
| `name` | string | ✅ | — | Waifu name |
| `img_url` | string | ✅ | — | Direct image URL |
| `rarity` | string | ❌ | `Common` | Common / Rare / Epic / Legendary |
| `event_tag` | string | ❌ | `Standard` | e.g. `Valentine`, `Anniversary` |
| `source_message_id` | int | ❌ | `0` | Telegram message ID |
| `added_by` | string | ✅ | — | Your name or username |

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

### 🔴 ˹ 𝚄ᴘᴅᴀᴛᴇ ˼ — `PUT /Update`

> Updates **all records** matching the name. Send only the fields you want to change.

```http
PUT https://wafus.vercel.app/Update?name=Rem
Content-Type: application/json
x-api-key: YUKI_your_key_here
```

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

> ❌ **400** — empty body sent · **404** — name not found in DB

---

### 🔴 ˹ 𝚁ᴍᴡᴀғᴜs ˼ — `DELETE /Rmwafus`

> Permanently deletes **all records** matching the given name. Cannot be undone.

```http
DELETE https://wafus.vercel.app/Rmwafus?name=Zero Two
x-api-key: YUKI_your_key_here
```

**Response:**
```json
{
  "status": "success",
  "message": "Successfully deleted 1 record(s) matching the name 'Zero Two'."
}
```

---

<img src="https://capsule-render.vercel.app/api?type=rect&amp;color=gradient&amp;customColorList=12,20,24&amp;height=4" width="100%"/>

## ─「 ˹ 𝙴ʀʀᴏʀ 𝚁ᴇғᴇʀᴇɴᴄᴇ ˼ 」─

| ˹ 𝙲ᴏᴅᴇ ˼ | ˹ 𝙼ᴇᴀɴɪɴɢ ˼ | ˹ 𝚁ᴇᴀsᴏɴ ˼ |
|-----------|---------|--------|
| `200` | ✅ Success | Everything worked fine |
| `400` | ❌ Bad Request | Empty or invalid body |
| `401` | 🔒 Unauthorized | `x-api-key` header missing |
| `403` | 🚫 Forbidden | API key is invalid |
| `404` | 🔍 Not Found | No matching records in DB |

---

## ─「 ˹ 𝚁ᴇᴘᴏ 𝚂ᴛᴀᴛs ˼ 」─

<div align="center">

![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=SUDEEPBOTS&repo=WAFUDATABASE&theme=tokyo-night&hide_border=true&area=true&color=ec4899&line=a855f7&point=ffffff)

[![Star History Chart](https://api.star-history.com/svg?repos=SUDEEPBOTS/WAFUDATABASE&type=Date&theme=dark)](https://star-history.com/#SUDEEPBOTS/WAFUDATABASE&Date)

</div>

---

## ─「 ˹ 𝚂ᴜᴘᴘᴏʀᴛ ˼ 」─

<div align="center">

[![Owner](https://img.shields.io/badge/Owner-Sudeep_Boss-ec4899?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Zcziiy)
[![Telegram](https://img.shields.io/badge/Contact-Telegram-a855f7?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Zcziiy)

<br>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=15&duration=3000&pause=600&color=EC4899&center=true&vCenter=true&width=520&lines=Star+this+repo+if+the+API+helped+you!;6000%2B+waifus+and+still+growing!;Made+with+love+by+Sudeep+Boss)](https://git.io/typing-svg)

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;customColorList=12,20,24&amp;height=130&amp;section=footer" width="100%"/>

</div>
