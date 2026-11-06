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


def search_web(query):
    return f"Searching for: {query}"


def  fake_agent_decision(user_query):
    if "-" in user_query or "*" in user_query or  "/"  in user_query or "+" in user_query:
        return "calculator"
    elif "search" in user_query:
        return "search_tool"
    else:
        return "unknown"




def fake_tool_dispatch(tool_name , args):
    if tool_name == "calculator":
        return calculator(**args)
    elif tool_name == "search_tool":
        return search_web(args["query"])
    else:
        return "Tool not found"


user_query = "25 * 4"



print(fake_tool_dispatch("calculator" , {"a" : 25 , "b" : 4 , "operation": "*"}))
print(fake_tool_dispatch("calculator", {"a": 25, "b" : 4, "operation": "*"})) 