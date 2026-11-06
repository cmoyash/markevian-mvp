from services.gemini_services import GeminiService
from google.genai import types


def calculator(a: int , b: int , operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return f"invaliod operation"

calculator_tool = {
    "name": "calculator",
    "description": "Performs basic arithmetic operations",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number"},
            "b": {"type": "number"},
            "operation": {"type": "string", "enum": ["+", "-", "*", "/"]}
        },
        "required": ["a", "b", "operation"]
    }
}


gemini = GeminiService()
prompt = "What is 25 * 4?"


response = gemini.generate_response(
    prompt=prompt ,
    config = types.GenerateContentConfig(
        tools = [types.Tool(function_declarations=[calculator_tool])]
    )
)
print(f"Function Calls: {response.function_calls}")
print(f"Text: {response.text}")

