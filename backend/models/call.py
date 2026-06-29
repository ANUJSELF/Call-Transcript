from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

class Call(db.Model):
    """Call recording model"""
    __tablename__ = 'calls'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    call_date = db.Column(db.DateTime, default=datetime.utcnow)
    customer_name = db.Column(db.String(255))
    agent_name = db.Column(db.String(255))
    duration_seconds = db.Column(db.Integer)
    file_path = db.Column(db.String(500), unique=True)
    
    # Transcription data
    transcript = db.Column(db.Text)
    transcription_status = db.Column(db.String(50), default='pending')
    
    # Categorization
    categories = db.Column(db.JSON)
    primary_category = db.Column(db.String(100))
    
    # Summary
    summary = db.Column(db.Text)
    key_points = db.Column(db.JSON)
    sentiment = db.Column(db.String(50))
    
    # Keywords
    keywords_found = db.Column(db.JSON)
    
    # Metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    notes = db.Column(db.Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'call_date': self.call_date.isoformat(),
            'customer_name': self.customer_name,
            'agent_name': self.agent_name,
            'duration_seconds': self.duration_seconds,
            'transcript': self.transcript,
            'transcription_status': self.transcription_status,
            'categories': self.categories,
            'primary_category': self.primary_category,
            'summary': self.summary,
            'key_points': self.key_points,
            'sentiment': self.sentiment,
            'keywords_found': self.keywords_found,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'notes': self.notes
        }

class Keyword(db.Model):
    """Custom keyword model for categorization"""
    __tablename__ = 'keywords'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    keyword = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    weight = db.Column(db.Float, default=1.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'keyword': self.keyword,
            'category': self.category,
            'description': self.description,
            'weight': self.weight,
            'created_at': self.created_at.isoformat()
        }