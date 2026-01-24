# ☁️ Deploy RBAT to Cloud (No Local Setup Required)

Can't run RBAT locally? No problem! Deploy it to the cloud for free.

---

## 🚀 **Option 1: Deploy to Render (Recommended - Free)**

### **One-Click Deploy:**

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/ABDALLA-ELKHOULI/RBAT)

**OR Manual Steps:**

1. **Go to:** https://render.com/
2. **Sign up** with GitHub (free)
3. **Click:** New + → Blueprint
4. **Connect repository:** ABDALLA-ELKHOULI/RBAT
5. **Add Environment Variable:**
   - `ANTHROPIC_API_KEY` = Your key from https://console.anthropic.com/
6. **Click "Apply"**

⏱️ **Deployment time:** 10-15 minutes

Your app will be live at: `https://rbat-frontend.onrender.com`

---

## 🌈 **Option 2: Deploy to Railway**

1. **Go to:** https://railway.app/
2. **Sign up** with GitHub
3. **New Project** → **Deploy from GitHub repo**
4. **Select:** ABDALLA-ELKHOULI/RBAT
5. **Add Services:**
   - Backend (from `backend` folder)
   - Frontend (from `frontend` folder)
   - PostgreSQL database
6. **Add Environment Variables:**
   - `ANTHROPIC_API_KEY` = Your API key
   - `DATABASE_URL` = (automatically from PostgreSQL service)

⏱️ **Deployment time:** 10 minutes

**Free tier:** 500 hours/month

---

## 🔷 **Option 3: Deploy to Vercel + Railway**

**Best for production - Fast & Free**

### **Frontend on Vercel:**

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/ABDALLA-ELKHOULI/RBAT/tree/main/frontend)

1. Click the button above
2. Connect GitHub
3. Deploy frontend

### **Backend on Railway:**

1. https://railway.app/new
2. Deploy from GitHub → backend folder
3. Add PostgreSQL database
4. Add `ANTHROPIC_API_KEY`

Then connect frontend to backend URL.

---

## ☁️ **Option 4: Google Cloud Run**

**Professional deployment, pay-as-you-go**

```bash
# Install gcloud CLI
brew install google-cloud-sdk

# Login
gcloud auth login

# Deploy backend
gcloud run deploy rbat-backend \
  --source backend \
  --set-env-vars ANTHROPIC_API_KEY=your-key \
  --allow-unauthenticated

# Deploy frontend
gcloud run deploy rbat-frontend \
  --source frontend \
  --allow-unauthenticated
```

---

## 🟧 **Option 5: AWS (Professional)**

### **Using AWS Copilot:**

```bash
# Install AWS Copilot
brew install aws/tap/copilot-cli

# Initialize
copilot init

# Deploy
copilot deploy
```

### **Using ECS:**

1. Push images to ECR
2. Create ECS cluster
3. Define task definitions
4. Deploy services

See AWS documentation for detailed steps.

---

## 📦 **Option 6: Heroku**

```bash
# Install Heroku CLI
brew install heroku

# Login
heroku login

# Create app
heroku create rbat-app

# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set ANTHROPIC_API_KEY=your-key

# Deploy
git push heroku main
```

---

## 🐙 **Option 7: GitHub Codespaces (Run in Browser)**

**No deployment needed - run in the cloud IDE**

1. Go to: https://github.com/ABDALLA-ELKHOULI/RBAT
2. Click **Code** → **Codespaces** → **Create codespace**
3. Wait for environment to load
4. In terminal:
   ```bash
   cp .env.example .env
   nano .env  # Add your API key
   docker compose up
   ```
5. Click "Open in Browser" when ports are forwarded

**Free tier:** 60 hours/month

---

## 🌐 **Option 8: DigitalOcean App Platform**

1. **Go to:** https://cloud.digitalocean.com/apps
2. **Create App** → **GitHub**
3. **Select:** ABDALLA-ELKHOULI/RBAT
4. **Configure:**
   - Backend: Docker, `backend` folder
   - Frontend: Docker, `frontend` folder
   - Database: PostgreSQL
5. **Add environment variable:** `ANTHROPIC_API_KEY`
6. **Deploy**

**Cost:** $5/month (has free trial)

---

## 💰 **Cost Comparison**

| Platform | Free Tier | Paid Plan | Best For |
|----------|-----------|-----------|----------|
| **Render** | ✅ Free forever | $7/month | Easiest setup |
| **Railway** | 500 hrs/month | $5/month | Simple projects |
| **Vercel** | ✅ Unlimited | $20/month | Frontends |
| **Google Cloud Run** | $0 (usage-based) | Pay as you go | Production |
| **AWS** | 12 months free | Pay as you go | Enterprise |
| **Heroku** | ❌ No free tier | $7/month | Quick deploys |
| **DigitalOcean** | $200 credit | $5/month | Full control |
| **Codespaces** | 60 hrs/month | $0.18/hour | Development |

---

## ⚡ **Quick Comparison**

**Easiest:** Render (one-click deploy)
**Fastest:** Vercel (for frontend)
**Cheapest:** Railway or Render (free)
**Most Professional:** Google Cloud Run or AWS
**Best for Development:** GitHub Codespaces

---

## 🔑 **Don't Forget!**

All options require:
1. **Anthropic API Key** from https://console.anthropic.com/
2. **GitHub account** (free)

---

## 🆘 **Having Trouble?**

### **Render Issues:**
- Make sure `render.yaml` is in the repository
- Check environment variables are set
- View build logs for errors

### **Railway Issues:**
- Deploy services separately (not docker-compose)
- Check service logs
- Ensure database is connected

### **General Issues:**
- Verify API key is correct
- Check service health endpoints
- Review deployment logs

---

## 📧 **Need Help?**

1. Check the logs in your deployment platform
2. Verify environment variables
3. Make sure ANTHROPIC_API_KEY is set correctly
4. Open an issue on GitHub

---

**Recommended for beginners: Start with Render.com - it's the easiest!** 🚀
