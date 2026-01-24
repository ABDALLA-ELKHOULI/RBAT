# 🛠️ Manual Setup (Without Docker)

If you can't or don't want to use Docker, follow these steps to run RBAT manually.

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 14+
- Redis (optional)

---

## Step 1: Install PostgreSQL

### Ubuntu/Debian

```bash
# Install PostgreSQL
sudo apt-get update
sudo apt-get install -y postgresql postgresql-contrib

# Install pgvector extension
sudo apt-get install -y postgresql-14-pgvector

# Start PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create database and user
sudo -u postgres psql << EOF
CREATE DATABASE rbat_db;
CREATE USER rbat_user WITH PASSWORD 'rbat_password';
GRANT ALL PRIVILEGES ON DATABASE rbat_db TO rbat_user;
\c rbat_db
CREATE EXTENSION vector;
EOF
```

---

## Step 2: Install Redis (Optional but recommended)

```bash
sudo apt-get install -y redis-server
sudo systemctl start redis
sudo systemctl enable redis
```

---

## Step 3: Set Up Backend (Python)

```bash
# Navigate to backend directory
cd /home/user/RBAT/backend

# Install Python 3.11 if needed
sudo apt-get install -y python3.11 python3.11-venv python3-pip

# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Go back to RBAT root
cd ..

# Configure environment
cp .env.example .env

# Edit .env file - ADD YOUR ANTHROPIC API KEY!
nano .env
```

**Edit the .env file and set:**
```
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
DATABASE_URL=postgresql://rbat_user:rbat_password@localhost:5432/rbat_db
REDIS_URL=redis://localhost:6379
```

**Start the backend:**
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Leave this terminal running and open a new one for the frontend.

---

## Step 4: Set Up Frontend (Next.js)

Open a **new terminal**:

```bash
# Install Node.js 18+ if needed
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Navigate to frontend directory
cd /home/user/RBAT/frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

---

## Step 5: Access the Platform

**Backend API:** http://localhost:8000
**API Docs:** http://localhost:8000/docs
**Frontend:** http://localhost:3000
**Chat Interface:** http://localhost:3000/chat

---

## Quick Start Commands

### Terminal 1 (Backend):
```bash
cd /home/user/RBAT/backend
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Terminal 2 (Frontend):
```bash
cd /home/user/RBAT/frontend
npm run dev
```

---

## Troubleshooting

### PostgreSQL Connection Error

```bash
# Check if PostgreSQL is running
sudo systemctl status postgresql

# Check if database exists
sudo -u postgres psql -l | grep rbat_db

# Test connection
psql -U rbat_user -d rbat_db -h localhost
# Password: rbat_password
```

### Python Dependencies Error

```bash
# Make sure you're in the virtual environment
source backend/venv/bin/activate

# Reinstall dependencies
pip install -r backend/requirements.txt
```

### Node.js/npm Error

```bash
# Check Node version (need 18+)
node --version

# Clear npm cache
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Port Already in Use

```bash
# Find what's using port 8000
lsof -i :8000
kill -9 <PID>

# Find what's using port 3000
lsof -i :3000
kill -9 <PID>
```

### Missing Anthropic API Key

Make sure `.env` file has:
```
ANTHROPIC_API_KEY=sk-ant-your-real-key-here
```

No quotes, no spaces. Get your key from https://console.anthropic.com/

---

## Production Deployment

For production, you should:

1. **Use a production WSGI server:**
   ```bash
   pip install gunicorn
   gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

2. **Build the frontend:**
   ```bash
   cd frontend
   npm run build
   npm start
   ```

3. **Use Nginx as reverse proxy**

4. **Enable HTTPS**

5. **Set up proper database backups**

See DEPLOYMENT.md for full production setup guide.
