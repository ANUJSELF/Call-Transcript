from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Import routes
from routes import transcription, categorization, summary, keywords

# Register blueprints
app.register_blueprint(transcription.bp)
app.register_blueprint(categorization.bp)
app.register_blueprint(summary.bp)
app.register_blueprint(keywords.bp)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()}), 200

@app.route('/api/version', methods=['GET'])
def version():
    return jsonify({'version': '1.0.0', 'app': 'Call Transcript System'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)