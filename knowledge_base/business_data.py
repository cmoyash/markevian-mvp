from pathlib import Path
from models.buisness_profile import BusinessProfile
from typing import Any
import json





class KnowledgeBase:
    def __init__(self , profile: BusinessProfile):
        self.profile = profile

    def load_business_config( self , file: Any) -> dict:
        file_path = Path(file)

        if not file_path.exists():
            raise FileNotFoundError(f"file not found: {file_path}")

        with open(file_path , "r" , encoding="utf-8") as f:
            data = json.load(f)
        return data

    
