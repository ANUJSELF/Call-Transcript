# AMEX Call Transcript System - API Documentation

## Overview
This API provides endpoints for managing call recordings, transcriptions, categorization, and summary generation.

## Base URL
```
http://localhost:5000/api
```

## Transcription Endpoints

### Upload Call Recording
```
POST /transcription/upload
Content-Type: multipart/form-data

Parameters:
- file: Audio file (MP3, WAV, M4A, FLAC)
- customer_name: Customer name
- agent_name: Agent name

Response:
{
  "success": true,
  "call_id": "uuid",
  "transcript": "Full transcript text",
  "status": "completed"
}
```

### Get Transcription Status
```
GET /transcription/status/<call_id>

Response:
{
  "call_id": "uuid",
  "status": "completed|processing|failed",
  "transcript": "Full transcript text"
}
```

### Get All Transcriptions
```
GET /transcription/all

Response:
{
  "total": 10,
  "calls": [...]
}
```

## Categorization Endpoints

### Categorize Call
```
POST /categorization/categorize/<call_id>

Response:
{
  "success": true,
  "call_id": "uuid",
  "categories": [...],
  "primary_category": "Account & Billing"
}
```

### Get Categories
```
GET /categorization/categories
```

## Summary Endpoints

### Generate Summary
```
POST /summary/generate/<call_id>

Response:
{
  "success": true,
  "summary": "Brief summary",
  "key_points": [...],
  "sentiment": "positive|negative|neutral"
}
```

## Keyword Endpoints

### Add Custom Keyword
```
POST /keywords/add
Content-Type: application/json

Body:
{
  "keyword": "billing issue",
  "category": "Account & Billing",
  "description": "Customer billing problem"
}
```

### List Keywords
```
GET /keywords/list
```

### Delete Keyword
```
DELETE /keywords/delete/<keyword_id>
```
