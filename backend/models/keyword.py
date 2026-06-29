from datetime import datetime
import uuid

class KeywordMapping:
    """In-memory keyword mapping for quick lookups"""
    
    DEFAULT_KEYWORDS = {
        'Account & Billing': [
            'account balance', 'credit limit', 'payment', 'bill', 'charge', 'fee',
            'annual fee', 'interest rate', 'statement', 'minimum payment'
        ],
        'Card Services': [
            'card replacement', 'lost card', 'stolen card', 'card activation',
            'card pin', 'chip card', 'contactless', 'digital wallet'
        ],
        'Rewards & Benefits': [
            'points', 'miles', 'rewards', 'cashback', 'benefits', 'travel',
            'lounge access', 'concierge', 'insurance'
        ],
        'Fraud & Security': [
            'fraud', 'unauthorized', 'suspicious', 'security', 'compromise',
            'breach', 'protection', 'liability'
        ],
        'Technical Support': [
            'app error', 'website', 'login', 'access', 'technical', 'bug',
            'not working', 'crash', 'loading'
        ],
        'Customer Inquiry': [
            'question', 'inquiry', 'information', 'how to', 'can i', 'would i',
            'when', 'where', 'why'
        ],
        'Resolution & Satisfaction': [
            'resolved', 'issue fixed', 'thank you', 'satisfied', 'happy',
            'solution', 'help', 'assistance'
        ]
    }