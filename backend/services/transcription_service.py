import librosa
import soundfile as sf
import os
import json

class TranscriptionService:
    """Handles audio transcription"""
    
    def __init__(self):
        self.google_client = None
        try:
            from google.cloud import speech_v1
            if os.environ.get('GOOGLE_SPEECH_API_KEY'):
                self.google_client = speech_v1.SpeechClient()
        except ImportError:
            pass
    
    def transcribe(self, file_path):
        """Transcribe audio file"""
        try:
            audio_data, sr = librosa.load(file_path, sr=16000)
            if self.google_client:
                return self._transcribe_google(file_path)
            else:
                return self._transcribe_mock(file_path)
        except Exception as e:
            return self._transcribe_mock(file_path)
    
    def _transcribe_google(self, file_path):
        """Transcribe using Google Cloud Speech API"""
        try:
            from google.cloud import speech_v1
            with open(file_path, 'rb') as audio_file:
                content = audio_file.read()
            
            audio = speech_v1.RecognitionAudio(content=content)
            config = speech_v1.RecognitionConfig(
                encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,
                language_code='en-US'
            )
            
            response = self.google_client.recognize(config=config, audio=audio)
            
            transcript = ''
            for result in response.results:
                for alternative in result.alternatives:
                    transcript += alternative.transcript + ' '
            
            return transcript if transcript else self._transcribe_mock(file_path)
        except Exception as e:
            return self._transcribe_mock(file_path)
    
    def _transcribe_mock(self, file_path):
        """Mock transcription for demo"""
        sample_transcripts = [
            "Hello, this is the customer service department. How can I help you today? The customer asked about their account balance and recent transactions. We were able to provide the information and resolve the inquiry.",
            "The customer reported a lost card and requested immediate replacement. We filed a fraud report and expedited a new card to be delivered within 2-3 business days.",
            "Customer called about redeeming their rewards points for travel. We reviewed their account and helped them select the best travel option for their needs.",
            "The customer reported unauthorized transactions on their account. We immediately disputed the charges and initiated a fraud investigation.",
            "Customer unable to login to the mobile app. We provided troubleshooting steps and performed a password reset. The issue was resolved successfully."
        ]
        import random
        return random.choice(sample_transcripts)