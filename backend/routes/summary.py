from flask import Blueprint, request, jsonify
from services.summary_service import SummaryService
from models.call import db, Call

bp = Blueprint('summary', __name__, url_prefix='/api/summary')
summary_service = SummaryService()

@bp.route('/generate/<call_id>', methods=['POST'])
def generate_summary(call_id):
    """Generate summary for a call"""
    call = Call.query.get(call_id)
    if not call:
        return jsonify({'error': 'Call not found'}), 404
    
    if not call.transcript:
        return jsonify({'error': 'Transcript not available'}), 400
    
    try:
        summary_data = summary_service.generate_summary(call.transcript)
        call.summary = summary_data['summary']
        call.key_points = summary_data['key_points']
        call.sentiment = summary_data['sentiment']
        db.session.commit()
        
        return jsonify({
            'success': True,
            'call_id': call_id,
            'summary': summary_data['summary'],
            'key_points': summary_data['key_points'],
            'sentiment': summary_data['sentiment']
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/<call_id>', methods=['GET'])
def get_summary(call_id):
    """Get summary for a call"""
    call = Call.query.get(call_id)
    if not call:
        return jsonify({'error': 'Call not found'}), 404
    
    return jsonify({
        'call_id': call_id,
        'summary': call.summary,
        'key_points': call.key_points,
        'sentiment': call.sentiment
    }), 200