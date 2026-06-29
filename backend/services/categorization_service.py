from models.keyword import KeywordMapping

class CategorizationService:
    """Handles call categorization"""
    
    def __init__(self):
        self.keywords = KeywordMapping.DEFAULT_KEYWORDS
    
    def categorize(self, transcript):
        """Categorize transcript based on keywords"""
        transcript_lower = transcript.lower()
        category_scores = {category: 0 for category in self.keywords.keys()}
        keywords_found = []
        
        for category, keywords in self.keywords.items():
            for keyword in keywords:
                if keyword.lower() in transcript_lower:
                    category_scores[category] += 1
                    keywords_found.append({
                        'keyword': keyword,
                        'category': category
                    })
        
        primary_category = max(category_scores, key=category_scores.get) if category_scores else 'General Inquiry'
        all_categories = [cat for cat, score in category_scores.items() if score > 0]
        if not all_categories:
            all_categories = ['General Inquiry']
        
        return {
            'all_categories': all_categories,
            'primary_category': primary_category,
            'keywords_found': keywords_found,
            'category_scores': category_scores
        }