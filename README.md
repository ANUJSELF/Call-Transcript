# AMEX Call Transcript System

A complete application for transcribing customer service call recordings, categorizing conversations, and generating summaries with sentiment analysis. Built with Flask backend and React frontend, following American Express design theme.

## Features

✨ **Core Features:**
- 🎙️ Audio transcription with support for multiple formats (MP3, WAV, M4A, FLAC)
- 📂 Automatic call categorization based on keywords
- 📋 Transcript summarization and key point extraction
- 😊 Sentiment analysis (positive, negative, neutral)
- 🏷️ Custom keyword management and tagging
- 📊 Analytics dashboard with call statistics
- 💳 American Express branded UI theme

## Tech Stack

**Backend:**
- Flask (Python web framework)
- SQLAlchemy (ORM)
- Google Cloud Speech API (Transcription)
- Transformers (Summarization & Sentiment Analysis)
- SQLite (Default database)

**Frontend:**
- React 18
- CSS3 with custom American Express theme
- Responsive design

## Quick Start

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

Backend: http://localhost:5000
Frontend: http://localhost:3000

## Project Structure
```
Call-Transcript/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── datasets/
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── .env.example
└── docs/
    └── API_DOCUMENTATION.md
```

## Default Categories
1. **Account & Billing** - Balance inquiries, payments, fees
2. **Card Services** - Card replacement, activation
3. **Rewards & Benefits** - Points, miles, travel perks
4. **Fraud & Security** - Unauthorized charges, security concerns
5. **Technical Support** - App errors, login issues
6. **Customer Inquiry** - General information requests
7. **Resolution & Satisfaction** - Issue resolution tracking

## API Documentation
See `docs/API_DOCUMENTATION.md` for complete API reference.

## Installation Guide
1. Clone the repository
2. Setup backend: `pip install -r backend/requirements.txt`
3. Setup frontend: `npm install` in frontend directory
4. Start backend: `python backend/app.py`
5. Start frontend: `npm start` in frontend directory

## License
MIT License

---
Built with ❤️ for American Express Customer Care