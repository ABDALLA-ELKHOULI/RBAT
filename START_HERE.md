# 🚀 Quick Start - RBAT Platform

## You're Almost Ready!

Follow these 4 simple steps to get RBAT running:

---

## Step 1: Get Your API Key (2 minutes)

1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Click **"API Keys"** → **"Create Key"**
4. Copy the key (starts with `sk-ant-...`)

---

## Step 2: Add Your API Key (30 seconds)

Open the `.env` file and add your API key:

```bash
nano .env
```

Change line 5 from:
```
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

To:
```
ANTHROPIC_API_KEY=sk-ant-YOUR-ACTUAL-KEY-HERE
```

**Save with:** `Ctrl+X`, then `Y`, then `Enter`

---

## Step 3: Start the Backend (Terminal 1)

```bash
./start_backend.sh
```

**Wait for this message:**
```
🌾 RBAT v1.0.0 started!
📚 API Documentation: http://localhost:8000/docs
```

**Keep this terminal running!**

---

## Step 4: Start the Frontend (Terminal 2)

**Open a NEW terminal window**, then run:

```bash
cd /home/user/RBAT
./start_frontend.sh
```

**Wait for this message:**
```
ready - started server on 0.0.0.0:3000, url: http://localhost:3000
```

---

## 🎉 You're Done! Open Your Browser:

**Chat Interface (Start here!):**
```
http://localhost:3000/chat
```

**API Documentation:**
```
http://localhost:8000/docs
```

**Homepage:**
```
http://localhost:3000
```

---

## 💬 Try Asking:

Once the chat interface opens, try these questions:

- "What crops grow best in Riyadh during winter?"
- "Compare investment opportunities in date farming vs olive farming"
- "I have 100,000 SAR to invest in livestock in Al-Jouf. What do you recommend?"
- "Generate a feasibility study for aquaculture in Eastern Province"

---

## 🛑 To Stop the Platform:

Press `Ctrl+C` in each terminal window

---

## 🆘 Troubleshooting:

### PostgreSQL not running?
```bash
service postgresql start
# OR
sudo systemctl start postgresql
```

### Redis not running?
```bash
redis-server --daemonize yes
```

### Port already in use?
```bash
# Kill process on port 8000
lsof -i :8000
kill -9 <PID>

# Kill process on port 3000
lsof -i :3000
kill -9 <PID>
```

### Need to create database?
```bash
createdb rbat_db
psql rbat_db -c "CREATE EXTENSION vector;"
```

---

## 📁 Your Current Directory

Make sure you're in: `/home/user/RBAT`

```bash
cd /home/user/RBAT
ls
# You should see: start_backend.sh and start_frontend.sh
```

---

## ✅ Quick Checklist

- [ ] Got Anthropic API key from https://console.anthropic.com/
- [ ] Added API key to `.env` file
- [ ] PostgreSQL is running
- [ ] Backend started with `./start_backend.sh`
- [ ] Frontend started with `./start_frontend.sh` (in new terminal)
- [ ] Opened http://localhost:3000/chat in browser

---

**That's it! You're ready to use RBAT!** 🌾

For more detailed information, see:
- [GETTING_STARTED.md](GETTING_STARTED.md) - Complete guide
- [MANUAL_SETUP.md](MANUAL_SETUP.md) - Manual setup details
- [docs/API.md](docs/API.md) - API documentation
