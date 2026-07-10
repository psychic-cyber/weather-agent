import json

from llm.openrouter_client import client

from config.settings import OPENROUTER_MODEL

from prompts.system_prompt import SYSTEM_PROMPT

from tools.weather_tool import get_weather


class WeatherAgent:

    def ask_llm(self, messages):

        response = client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=messages,
        )

        return response.choices[0].message.content.strip()

    def should_use_weather_tool(self, user_message):

        prompt = f"""
You are an AI routing assistant.

Determine whether the user's message requires REAL-TIME weather information.

Reply with ONLY one word.

YES
or
NO

User:
{user_message}
"""

        answer = self.ask_llm(
            [
                {
                    "role": "system",
                    "content": "Answer only YES or NO.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ]
        )

        return answer.upper() == "YES"

    def extract_city(self, user_message):

        prompt = f"""
Extract only the city name.

User:
{user_message}

Return ONLY the city.

Example:

Lahore

Islamabad

Karachi
"""

        city = self.ask_llm(
            [
                {
                    "role": "system",
                    "content": "Return only the city name.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ]
        )

        return city.strip()

    def generate_weather_response(self, question, weather):

        return f"""
    ╔══════════════════════════════════════════════╗
            🌦️  WEATHER REPORT
    ╚══════════════════════════════════════════════╝

    📍 City         : {weather['city']}, {weather['country']}

    🌡️ Temperature : {weather['temperature']} °C
    🥵 Feels Like  : {weather['feels_like']} °C

    ☁️ Condition   : {weather['condition'].title()}

    💧 Humidity    : {weather['humidity']} %

    🌬️ Wind Speed : {weather['wind_speed']} m/s

    🧭 Pressure    : {weather['pressure']} hPa

    ═══════════════════════════════════════════════

    Stay safe and have a wonderful day! 🌤️
    """.strip()

    def chat(self, user_message):

        if self.should_use_weather_tool(user_message):

            city = self.extract_city(user_message)

            weather = get_weather(city)

            if weather["success"]:

                return self.generate_weather_response(
                    user_message,
                    weather,
                )

            return weather["error"]

        return self.ask_llm(
            [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ]
        )