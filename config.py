import os
from dotenv import load_dotenv
load_dotenv()




class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME")

    @staticmethod
    def validate() -> None:
        if not Config.GEMINI_API_KEY:
            raise ValueError(
                f"GEMINI API KEY NOT FOUND"
            )

