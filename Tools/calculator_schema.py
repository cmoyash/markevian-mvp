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

print(calculator_tool)