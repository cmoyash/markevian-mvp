
from typing import Dict

def validate_tool_input(data: Dict):
    if "city" not in data:
        return "Error: city is required"
    elif not isinstance(data["city"] , str) :
        return "Error: city must be string"
    else:
        return "Data is valid"


data = {"city" : "mumbai"}


result = validate_tool_input(data=data)
print(result)




def get_weather(city: str) -> str:
    if city.lower() == "mumabi":
        return "32^"
    elif city.lower() == "dehli":
        return ""