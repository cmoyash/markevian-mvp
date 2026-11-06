
#Import important modules
from services.gemini_services import GeminiService
from google.genai import types

#Variables
gemini = GeminiService()

#prompts
prompt =  " whats the weather of mumbai"

#Tools

def get_weather(city: str) -> str:
    if city.lower() == "mumbai":
        return "32^"
    elif city.lower() == "dehli":
        return "28^"
    else:
        return "unknown city"


#Tool schema

weather_tool = {
    "name" : "get_weather" ,
    "description" : "gives temperature on given city" ,
    "parameters" : {
        "type" : "object" ,
        "properties" : {
            "city" : {
                "type" : "string"
            }
        } , "required" : ["city"]
    }
}



tool_response = gemini.generate_response(
    prompt=prompt , 
    config=types.GenerateContentConfig(
        tools=[types.Tool(function_declarations=[weather_tool])]
    )
)

call = tool_response.function_calls[0]
print(f"Gemini wants {call.name} with {call.args}")
response_content = tool_response.candidates[0].content


if call.name == "get_weather":
    result = get_weather(**call.args)
print(f"Tool Result: {result}")


final_response = gemini.generate_with_history(
    contents=[
             types.Content(role="user" , parts= [types.Part(text=prompt)]) ,
        response_content , 
        types.Content(role="user" , parts=[types.Part(function_response=types.FunctionResponse(
            name="get_weather" ,
            response={"result" : result}
        ))])
    ]
)


print(final_response.text)