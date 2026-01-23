# RBAT API Documentation

Base URL: `http://localhost:8000/api/v1`

## Authentication

Currently, the API is open for development. In production, implement API key authentication.

## AI Agent Endpoints

### Query Agent

Ask the AI agent any agriculture-related question.

**Endpoint:** `POST /api/v1/agent/query`

**Request:**
```json
{
  "query": "What crops grow best in Riyadh?",
  "conversation_history": []
}
```

**Response:**
```json
{
  "response": "Based on the climate data for Riyadh...",
  "references": [
    {
      "id": 1,
      "title": "Agriculture in Saudi Arabia",
      "year": 2023,
      "url": "https://..."
    }
  ],
  "context_used": {
    "crops_count": 5,
    "livestock_count": 0,
    "references_count": 10
  },
  "model": "claude-sonnet-4-5-20250929",
  "usage": {
    "input_tokens": 1500,
    "output_tokens": 800
  }
}
```

### Recommend Crops

Get crop recommendations for specific conditions.

**Endpoint:** `POST /api/v1/agent/recommend-crops`

**Request:**
```json
{
  "region": "Riyadh",
  "season": "winter",
  "water_availability": "moderate",
  "budget_sar": 50000
}
```

### Analyze Livestock

Analyze livestock farming opportunities.

**Endpoint:** `POST /api/v1/agent/analyze-livestock`

**Request:**
```json
{
  "region": "Al-Jouf",
  "livestock_type": "sheep",
  "investment_amount": 100000
}
```

### Market Forecast

Forecast market conditions for agricultural products.

**Endpoint:** `POST /api/v1/agent/forecast-market`

**Request:**
```json
{
  "product": "wheat",
  "months_ahead": 6
}
```

### Generate Report

Generate comprehensive research reports.

**Endpoint:** `POST /api/v1/agent/generate-report`

**Request:**
```json
{
  "topic": "Date palm cultivation in Saudi Arabia",
  "region": "Al-Ahsa"
}
```

### Weather Advisory

Get agricultural advisory based on weather forecast.

**Endpoint:** `POST /api/v1/agent/weather-advisory`

**Request:**
```json
{
  "region": "Riyadh",
  "days_ahead": 7
}
```

### Chat

Interactive chat with conversation context.

**Endpoint:** `POST /api/v1/agent/chat`

**Request:**
```json
{
  "message": "Tell me more about that",
  "conversation_history": [
    {"role": "user", "content": "What are the best crops?"},
    {"role": "assistant", "content": "The best crops are..."}
  ]
}
```

## Crops Endpoints

### List Crops

**Endpoint:** `GET /api/v1/crops`

**Parameters:**
- `skip` (optional): Number of records to skip
- `limit` (optional): Maximum records to return
- `category` (optional): Filter by category
- `search` (optional): Search term

**Example:**
```
GET /api/v1/crops?category=vegetables&search=tomato
```

### Get Crop Details

**Endpoint:** `GET /api/v1/crops/{crop_id}`

### Get Crop Suitability

**Endpoint:** `GET /api/v1/crops/{crop_id}/suitability?region_id=1`

### List Categories

**Endpoint:** `GET /api/v1/crops/categories/list`

## Livestock Endpoints

### List Livestock

**Endpoint:** `GET /api/v1/livestock`

**Parameters:**
- `category`: cattle, sheep, goats, camels, poultry
- `search`: Search term

### Get Livestock Details

**Endpoint:** `GET /api/v1/livestock/{livestock_id}`

### Get Breeds

**Endpoint:** `GET /api/v1/livestock/{livestock_id}/breeds`

## Fisheries Endpoints

### List Fisheries

**Endpoint:** `GET /api/v1/fisheries`

**Parameters:**
- `type`: marine, freshwater, brackish
- `search`: Search term

### Get Fishery Details

**Endpoint:** `GET /api/v1/fisheries/{fishery_id}`

### Get Species

**Endpoint:** `GET /api/v1/fisheries/{fishery_id}/species`

## Climate Endpoints

### List Regions

**Endpoint:** `GET /api/v1/climate/regions`

Returns all Saudi Arabian regions with agricultural data.

### Get Region Details

**Endpoint:** `GET /api/v1/climate/regions/{region_id}`

### Get Climate Data

**Endpoint:** `GET /api/v1/climate/data`

**Parameters:**
- `region_id` (required): Region ID
- `start_date` (optional): Start date (YYYY-MM-DD)
- `end_date` (optional): End date (YYYY-MM-DD)

**Example:**
```
GET /api/v1/climate/data?region_id=1&start_date=2024-01-01&end_date=2024-01-31
```

### Get Weather Forecast

**Endpoint:** `GET /api/v1/climate/forecast`

**Parameters:**
- `region_id` (required): Region ID
- `days` (optional, default=7): Number of days (1-30)

### Get Current Conditions

**Endpoint:** `GET /api/v1/climate/current/{region_id}`

## Reports Endpoints

### Generate Report

**Endpoint:** `POST /api/v1/reports/generate`

**Request:**
```json
{
  "title": "Agriculture Investment Opportunities in Riyadh",
  "topic": "investment opportunities",
  "region": "Riyadh",
  "include_crops": true,
  "include_livestock": true,
  "include_fisheries": true,
  "include_climate": true,
  "include_market_analysis": true,
  "include_forecasts": true,
  "format": "json"
}
```

**Formats:**
- `json`: JSON response (default)
- `pdf`: PDF document (coming soon)
- `excel`: Excel spreadsheet (coming soon)

### List Templates

**Endpoint:** `GET /api/v1/reports/templates`

Returns available report templates.

## Error Responses

All endpoints return standard error responses:

**400 Bad Request:**
```json
{
  "error": "Bad Request",
  "detail": "Invalid region_id"
}
```

**404 Not Found:**
```json
{
  "error": "Not Found",
  "detail": "Crop not found"
}
```

**500 Internal Server Error:**
```json
{
  "error": "Internal server error",
  "detail": "An error occurred"
}
```

## Rate Limiting

Currently no rate limiting in development. In production:
- 1000 requests per hour per IP
- 100 requests per minute per IP
- Heavy endpoints (AI agent, reports): 10 requests per minute

## Interactive Documentation

Visit http://localhost:8000/docs for interactive API documentation with Swagger UI.

Visit http://localhost:8000/redoc for alternative documentation with ReDoc.
