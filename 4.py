from pathlib import Path
from models.buisness_profile import BusinessProfile
from typing import Any
import json


def load_business_config(file: Any) -> dict:
    file_path = Path(file)

    if not file_path.exists():
        raise FileNotFoundError(f"file not found: {file_path}")

    with open(file_path , "r" , encoding="utf-8") as f:
        data = json.load(f)
    return data




data = load_business_config("knowledgebase_data/business_data.json")

business_profile = BusinessProfile(**data)

print(business_profile.business_name)
print(business_profile.target_industries[0])