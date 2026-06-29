from flask import Blueprint, request, jsonify
from services.categorization_service import CategorizationService
from models.call import db, Call
from models.keyword import KeywordMapping

bp = Blueprint('categorization', __name__, url_prefix='/api/categorization')
categorization_service = CategorizationService()

@bp.route('/categorize/<call_id>', methods=['POST'])
def categorize_call(call_id):
    """Categorize a call based on transcript"""
    call = Call.query.get(call_id)
    if not call:
        return jsonify({'error': 'Call not found'}), 404
    
    if not call.transcript:
        return jsonify({'error': 'Transcript not available'}), 400
    
    try:
        categories = categorization_service.categorize(call.transcript)
        call.categories = categories['all_categories']
        call.primary_category = categories['primary_category']
        call.keywords_found = categories['keywords_found']
        db.session.commit()
        
        return jsonify({
            'success': True,
            'call_id': call_id,
            'categories': categories['all_categories'],
            'primary_category': categories['primary_category'],
            'keywords_found': categories['keywords_found']
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/categories', methods=['GET'])
def get_categories():
    """Get all available categories"""
    categories = list(KeywordMapping.DEFAULT_KEYWORDS.keys())
    return jsonify({'categories': categories}), 200

@bp.route('/filter', methods=['POST'])
def filter_by_category():
    """Filter calls by category"""
    data = request.json
    category = data.get('category')
    
    if not category:
        return jsonify({'error': 'Category required'}), 400
    
    calls = Call.query.all()
    filtered_calls = [
        call.to_dict() for call in calls 
        if call.primary_category == category
    ]
    
    return jsonify({
        'category': category,
        'count': len(filtered_calls),
        'calls': filtered_calls
    }), 200