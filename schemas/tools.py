WEATHER_TOOL_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The name of the city. Example: Lahore, Islamabad, Karachi"
                    }
                },
                "required": ["city"],
                "additionalProperties": False
            }
        }
    }
]