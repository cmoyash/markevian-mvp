from google import genai
from config import Config
from typing import Any
from google.genai import types
from typing import List , Any




class GeminiService:
    def __init__(self):
        Config.validate()
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)

    def generate_response(self , prompt: str , config:Any = None ) -> types.GenerateContentResponse:
        try:
            response = self.client.models.generate_content(
                model=Config.MODEL_NAME ,
                contents=prompt ,
                config= config

            )
            return response
        except Exception as e:
            raise RuntimeError(
                f"Server error {e}"
            )

    def generate_with_history(self , contents: List , config: Any = None) -> types.GenerateContentResponse:
        try:
            response =  self.client.models.generate_content(
                model=Config.MODEL_NAME ,
                contents= contents ,
                config=config
            )
            return response
        except Exception as e:
            raise RuntimeError(
                f"Server error {e}"
            )
