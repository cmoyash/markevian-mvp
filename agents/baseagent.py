from abc import ABC , abstractmethod
from services.gemini_services import GeminiService


class BaseAgent(ABC):
    def __init__(self , gemini: GeminiService):
        self.gemini = gemini
    
    @abstractmethod
    def build_prompt(self):
        pass