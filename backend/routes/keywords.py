from flask import Blueprint, request, jsonify
from models.call import db, Keyword
from models.keyword import KeywordMapping

bp = Blueprint('keywords', __name__, url_prefix='/api/keywords')

@bp.route('/add', methods=['POST'])
def add_keyword():
    """Add a custom keyword"""
    data = request.json
    
    keyword_text = data.get('keyword')
    category = data.get('category')
    description = data.get('description', '')
    weight = data.get('weight', 1.0)
    
    if not keyword_text or not category:
        return jsonify({'error': 'Keyword and category required'}), 400
    
    existing = Keyword.query.filter_by(keyword=keyword_text).first()
    if existing:
        return jsonify({'error': 'Keyword already exists'}), 400
    
    keyword = Keyword(
        keyword=keyword_text,
        category=category,
        description=description,
        weight=weight
    )
    
    db.session.add(keyword)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'keyword': keyword.to_dict()
    }), 201

@bp.route('/list', methods=['GET'])
def list_keywords():
    """List all keywords"""
    keywords = Keyword.query.all()
    default_keywords = {
        category: KeywordMapping.DEFAULT_KEYWORDS[category]
        for category in KeywordMapping.DEFAULT_KEYWORDS
    }
    
    custom_keywords = {}
    for keyword in keywords:
        if keyword.category not in custom_keywords:
            custom_keywords[keyword.category] = []
        custom_keywords[keyword.category].append(keyword.to_dict())
    
    return jsonify({
        'default_keywords': default_keywords,
        'custom_keywords': custom_keywords
    }), 200

@bp.route('/delete/<keyword_id>', methods=['DELETE'])
def delete_keyword(keyword_id):
    """Delete a custom keyword"""
    keyword = Keyword.query.get(keyword_id)
    if not keyword:
        return jsonify({'error': 'Keyword not found'}), 404
    
    db.session.delete(keyword)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Keyword deleted'}), 200

@bp.route('/default', methods=['GET'])
def get_default_keywords():
    """Get default keywords"""
    return jsonify(KeywordMapping.DEFAULT_KEYWORDS), 200