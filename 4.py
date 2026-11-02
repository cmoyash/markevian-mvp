from pathlib import Path
import json



def load_business_config(file):
    file_path = Path(file)

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found! {file_path}"
        )
    with open(file_path , "r" , encoding="utf-8") as f:
        data = json.load(f)
    return data
    

data = load_business_config("config/business_data.json")
print(data["business_name"])
print(data["target_industries"][0])
print(data["ideal_customer"]["has_existing_clients"])

try:
    data = load_business_config("config/galat_file.json")
except FileNotFoundError as e:
    print(f"Error: {e}")

   