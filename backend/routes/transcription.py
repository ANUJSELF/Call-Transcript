from flask import Blueprint, request, jsonify
from services.transcription_service import TranscriptionService
from models.call import db, Call
import os
from werkzeug.utils import secure_filename
import uuid
from datetime import datetime

bp = Blueprint('transcription', __name__, url_prefix='/api/transcription')
transcription_service = TranscriptionService()

ALLOWED_EXTENSIONS = {'mp3', 'wav', 'm4a', 'flac'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/upload', methods=['POST'])
def upload_call():
    """Upload and process a call recording"""
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    
    # Extract form data
    customer_name = request.form.get('customer_name', 'Unknown')
    agent_name = request.form.get('agent_name', 'Unknown')
    
    # Save file
    filename = secure_filename(f"{uuid.uuid4()}_{file.filename}")
    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
    
    # Create call record
    call = Call(
        customer_name=customer_name,
        agent_name=agent_name,
        file_path=file_path,
        transcription_status='processing'
    )
    db.session.add(call)
    db.session.commit()
    
    # Start transcription
    try:
        transcript = transcription_service.transcribe(file_path)
        call.transcript = transcript
        call.transcription_status = 'completed'
        db.session.commit()
        
        return jsonify({
            'success': True,
            'call_id': call.id,
            'transcript': transcript,
            'status': 'completed'
        }), 200
    
    except Exception as e:
        call.transcription_status = 'failed'
        db.session.commit()
        return jsonify({'error': str(e), 'call_id': call.id}), 500

@bp.route('/status/<call_id>', methods=['GET'])
def get_transcription_status(call_id):
    """Get transcription status"""
    call = Call.query.get(call_id)
    if not call:
        return jsonify({'error': 'Call not found'}), 404
    
    return jsonify({
        'call_id': call_id,
        'status': call.transcription_status,
        'transcript': call.transcript
    }), 200

@bp.route('/all', methods=['GET'])
def get_all_transcriptions():
    """Get all transcriptions"""
    calls = Call.query.all()
    return jsonify({
        'total': len(calls),
        'calls': [call.to_dict() for call in calls]
    }), 200