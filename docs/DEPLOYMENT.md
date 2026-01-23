# RBAT Deployment Guide

This guide covers deploying RBAT to various cloud platforms.

## Prerequisites

- Docker and Docker Compose installed
- Git repository access
- API keys:
  - Anthropic API key (required)
  - OpenWeather API key (recommended)
  - NewsAPI key (optional)
  - NASA API key (optional)

## Local Development

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd RBAT
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```
ANTHROPIC_API_KEY=your_key_here
OPENWEATHER_API_KEY=your_key_here
NEWS_API_KEY=your_key_here
```

### 3. Start Services

```bash
docker-compose up
```

Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Cloud Deployment

### AWS Deployment

#### Option 1: AWS ECS (Elastic Container Service)

**1. Build and Push Docker Images**

```bash
# Build images
docker build -t rbat-backend ./backend
docker build -t rbat-frontend ./frontend

# Tag for ECR
docker tag rbat-backend:latest <account-id>.dkr.ecr.<region>.amazonaws.com/rbat-backend:latest
docker tag rbat-frontend:latest <account-id>.dkr.ecr.<region>.amazonaws.com/rbat-frontend:latest

# Push to ECR
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/rbat-backend:latest
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/rbat-frontend:latest
```

**2. Create RDS PostgreSQL Database**

```bash
aws rds create-db-instance \
  --db-instance-identifier rbat-db \
  --db-instance-class db.t3.medium \
  --engine postgres \
  --engine-version 16 \
  --master-username rbat_user \
  --master-user-password <secure-password> \
  --allocated-storage 20 \
  --vpc-security-group-ids <security-group-id>
```

**3. Create ECS Task Definitions**

See `deployment/aws/ecs-task-definition.json`

**4. Deploy to ECS**

```bash
aws ecs create-service \
  --cluster rbat-cluster \
  --service-name rbat-backend \
  --task-definition rbat-backend \
  --desired-count 2 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[<subnet-ids>],securityGroups=[<sg-ids>],assignPublicIp=ENABLED}"
```

#### Option 2: AWS App Runner

```bash
aws apprunner create-service \
  --service-name rbat-backend \
  --source-configuration "{\"ImageRepository\":{\"ImageIdentifier\":\"<ecr-image-url>\",\"ImageRepositoryType\":\"ECR\"}}" \
  --instance-configuration "{\"Cpu\":\"1024\",\"Memory\":\"2048\"}"
```

### Google Cloud Platform

#### Cloud Run Deployment

**1. Build and Push to GCR**

```bash
# Enable services
gcloud services enable run.googleapis.com
gcloud services enable sql-component.googleapis.com

# Build and push
gcloud builds submit --tag gcr.io/<project-id>/rbat-backend ./backend
gcloud builds submit --tag gcr.io/<project-id>/rbat-frontend ./frontend
```

**2. Create Cloud SQL PostgreSQL**

```bash
gcloud sql instances create rbat-db \
  --database-version=POSTGRES_16 \
  --tier=db-f1-micro \
  --region=us-central1

gcloud sql databases create rbat_db --instance=rbat-db
gcloud sql users create rbat_user --instance=rbat-db --password=<secure-password>
```

**3. Deploy to Cloud Run**

```bash
# Backend
gcloud run deploy rbat-backend \
  --image gcr.io/<project-id>/rbat-backend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars DATABASE_URL="<cloud-sql-connection-string>" \
  --set-env-vars ANTHROPIC_API_KEY="<your-key>"

# Frontend
gcloud run deploy rbat-frontend \
  --image gcr.io/<project-id>/rbat-frontend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars NEXT_PUBLIC_API_URL="<backend-url>"
```

### Azure Deployment

#### Azure Container Apps

**1. Create Resources**

```bash
# Resource group
az group create --name rbat-rg --location eastus

# Container registry
az acr create --resource-group rbat-rg --name rbatregistry --sku Basic

# PostgreSQL
az postgres flexible-server create \
  --resource-group rbat-rg \
  --name rbat-db \
  --location eastus \
  --admin-user rbat_user \
  --admin-password <secure-password> \
  --sku-name Standard_B1ms \
  --version 16
```

**2. Build and Push**

```bash
az acr build --registry rbatregistry --image rbat-backend:latest ./backend
az acr build --registry rbatregistry --image rbat-frontend:latest ./frontend
```

**3. Deploy Container Apps**

```bash
az containerapp create \
  --name rbat-backend \
  --resource-group rbat-rg \
  --image rbatregistry.azurecr.io/rbat-backend:latest \
  --target-port 8000 \
  --ingress external \
  --env-vars DATABASE_URL="<postgres-url>" ANTHROPIC_API_KEY="<your-key>"
```

## Database Setup

### Initialize Database

After deploying, initialize the database schema:

```bash
# Connect to your backend container/pod
docker exec -it <backend-container> bash

# Run migrations (if using Alembic)
alembic upgrade head

# Or initialize directly
python -c "from app.core.database import init_db; init_db()"
```

### Load Sample Data

```bash
# Load sample Saudi regions
python scripts/load_regions.py

# Load sample crops
python scripts/load_crops.py
```

## Environment Variables

Required environment variables for production:

```bash
# Database
DATABASE_URL=postgresql://user:pass@host:5432/dbname

# AI
ANTHROPIC_API_KEY=sk-ant-...

# External APIs (optional)
OPENWEATHER_API_KEY=...
NEWS_API_KEY=...
NASA_API_KEY=...

# Security
SECRET_KEY=<long-random-string>

# Application
DEBUG=False
BACKEND_CORS_ORIGINS=["https://your-frontend-domain.com"]
```

## Monitoring and Logging

### Health Checks

- Backend: `GET /health`
- Database: Ensure pgvector extension is installed

### Logging

Configure log aggregation:
- AWS: CloudWatch Logs
- GCP: Cloud Logging
- Azure: Application Insights

## Scaling

### Horizontal Scaling

- Backend: Scale API containers based on CPU/memory
- Database: Use read replicas for queries
- Cache: Add Redis cluster for better performance

### Vertical Scaling

Recommended minimum specs:
- Backend: 2 vCPU, 4 GB RAM
- Database: 2 vCPU, 8 GB RAM
- Frontend: 1 vCPU, 2 GB RAM

## Security

### SSL/TLS

Use managed certificates:
- AWS: ACM (AWS Certificate Manager)
- GCP: Managed SSL certificates
- Azure: App Service Certificates

### API Security

- Enable rate limiting
- Use API keys for external access
- Implement CORS properly
- Keep dependencies updated

## Backup and Recovery

### Database Backups

```bash
# AWS RDS - Automated backups enabled by default
# GCP Cloud SQL - Enable automated backups
gcloud sql backups create --instance=rbat-db

# Manual backup
pg_dump -h <host> -U rbat_user rbat_db > backup.sql
```

## Cost Optimization

- Use spot instances for non-critical workloads
- Implement auto-scaling
- Use CDN for frontend assets
- Enable database query caching
- Archive old data regularly

## Troubleshooting

### Common Issues

**Database connection fails:**
- Check security groups/firewall rules
- Verify DATABASE_URL format
- Ensure pgvector extension is installed

**API returns 500 errors:**
- Check API key validity
- Review application logs
- Verify environment variables

**Frontend can't connect to backend:**
- Verify NEXT_PUBLIC_API_URL
- Check CORS settings
- Ensure backend is accessible

## Support

For deployment issues:
1. Check logs first
2. Review documentation
3. Open GitHub issue with details
