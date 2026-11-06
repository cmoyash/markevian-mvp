from services.gemini_services import GeminiService
from google.genai import types



#prompts
prompt = "40 * 5"

#  Variables
gemini = GeminiService()

#Tool schema

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

#Tools

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



#Main Logic

tool_response = gemini.generate_response(
    prompt=prompt ,
    config = types.GenerateContentConfig(
        tools=[types.Tool(function_declarations=[calculator_tool])]
    )
)

call = tool_response.function_calls[0]
model_content = tool_response.candidates[0].content
print(f"Gemini wants {call.name} with {call.args}")
args =  call.args

result = calculator(**args)



final_response = gemini.generate_with_history(
    contents=[
        types.Content(role="user" , parts=[types.Part(text=prompt)]) ,
        model_content ,  
        types.Content(role= "user" , parts=[types.Part(function_response = types.FunctionResponse(
            name="calculator" ,
            response= {"result" : result}
        ))])
    ]
)

print(final_response.text)