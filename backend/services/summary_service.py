import re

class SummaryService:
    """Handles transcript summarization"""
    
    def __init__(self):
        try:
            from transformers import pipeline
            self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
            self.sentiment_analyzer = pipeline("sentiment-analysis")
        except:
            self.summarizer = None
            self.sentiment_analyzer = None
    
    def generate_summary(self, transcript):
        """Generate summary and key points"""
        sentences = re.split(r'[.!?]+', transcript)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if len(transcript) > 100 and self.summarizer:
            try:
                summary_result = self.summarizer(transcript[:1024], max_length=150, min_length=50, do_sample=False)
                summary = summary_result[0]['summary_text']
            except:
                summary = self._extractive_summary(sentences)
        else:
            summary = self._extractive_summary(sentences)
        
        key_points = self._extract_key_points(sentences)
        sentiment = self._analyze_sentiment(transcript)
        
        return {
            'summary': summary,
            'key_points': key_points,
            'sentiment': sentiment
        }
    
    def _extractive_summary(self, sentences):
        """Simple extractive summary"""
        if len(sentences) <= 3:
            return ' '.join(sentences)
        
        summary_sentences = [
            sentences[0],
            sentences[len(sentences) // 2],
            sentences[-1]
        ]
        return ' '.join(summary_sentences)
    
    def _extract_key_points(self, sentences):
        """Extract key points from sentences"""
        key_sentences = sorted(sentences, key=len, reverse=True)[:3]
        return key_sentences[:3]
    
    def _analyze_sentiment(self, text):
        """Analyze sentiment of text"""
        try:
            if self.sentiment_analyzer:
                result = self.sentiment_analyzer(text[:512])
                label = result[0]['label']
                score = result[0]['score']
                
                if label == 'POSITIVE' and score > 0.7:
                    return 'positive'
                elif label == 'NEGATIVE' and score > 0.7:
                    return 'negative'
                else:
                    return 'neutral'
        except:
            pass
        
        return 'neutral'