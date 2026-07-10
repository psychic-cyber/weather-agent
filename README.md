# 🌦️ Weather AI Agent

An intelligent AI-powered Weather Agent built with **Python**, **OpenRouter LLM**, and **OpenWeather API**.

Instead of simply displaying weather data, the agent understands user questions, fetches live weather information, and generates human-friendly responses using an LLM.

---

## 🚀 Features

- 🤖 AI-powered conversational interface
- 🌍 Live weather using OpenWeather API
- 🧠 Natural language understanding with OpenRouter
- 📍 Automatic city extraction from user queries
- 🌡️ Real-time weather reports
- 💧 Humidity information
- 🌬️ Wind speed
- 🧭 Atmospheric pressure
- 🥵 Feels-like temperature
- ☁️ Weather condition
- 🏗️ Modular project architecture
- 🔐 Environment variables using `.env`

---

## 🖥️ Demo

```text
🌦️ Weather AI Agent

Type 'exit' to quit.

You: What's the weather in Lahore?

╔══════════════════════════════════════════════╗
            🌦️ WEATHER REPORT
╚══════════════════════════════════════════════╝

📍 City         : Lahore, PK

🌡️ Temperature : 31.4 °C
🥵 Feels Like  : 34.0 °C

☁️ Condition   : Clear Sky

💧 Humidity    : 53 %

🌬️ Wind Speed : 4.6 m/s

🧭 Pressure    : 995 hPa

═══════════════════════════════════════════════

Stay safe and have a wonderful day! 🌤️
```

---

# 📂 Project Structure

```text
weather-agent/
│
├── app.py
├── agent.py
├── README.md
├── requirements.txt
│
├── config/
│   └── settings.py
│
├── docs/
│
├── llm/
│   └── openrouter_client.py
│
├── prompts/
│   └── system_prompt.py
│
├── schemas/
│   └── tools.py
│
├── tests/
│
└── tools/
    └── weather_tool.py
```

---

# ⚙️ Technologies Used

- Python 3.10+
- OpenRouter API
- OpenWeather API
- OpenAI Python SDK
- Requests
- Python Dotenv

---

# 🛠️ Installation

Clone the repository

```bash
git clone https://github.com/psychic-cyber/weather-agent.git
```

Move into the project

```bash
cd weather-agent
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
OPENROUTER_API_KEY=YOUR_API_KEY

OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

OPENROUTER_MODEL=openrouter/free

OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY

OPENWEATHER_BASE_URL=https://api.openweathermap.org/data/2.5/weather
```

---

# ▶️ Run

```bash
python app.py
```

---

# 🏛️ Architecture

```text
             User
               │
               ▼
         Weather AI Agent
               │
               ▼
      Intent Detection (LLM)
               │
       ┌───────┴────────┐
       │                │
       ▼                ▼
Normal Chat      Weather Request
       │                │
       │                ▼
       │        Weather Tool
       │                │
       │                ▼
       │       OpenWeather API
       │                │
       └────────┬───────┘
                ▼
         Natural Response
                │
                ▼
               User
```

---

# 📌 Current Capabilities

✅ Chat with AI

✅ Detect weather-related queries

✅ Extract city names

✅ Fetch live weather

✅ Generate readable weather reports

---

# 🚧 Upcoming Features

- 🧠 Conversation Memory
- 🌅 Sunrise & Sunset
- 🌧️ Weather Forecast
- 🌫️ Air Quality Index (AQI)
- 🗺️ Maps Integration
- 🌎 Multi-language Support
- 📰 News Tool
- 🧮 Calculator Tool
- 💱 Currency Converter Tool
- 🔥 Multi-Tool AI Agent
- 🎨 Beautiful Terminal UI

---

# 👨‍💻 Author

**Muhammad Ibrahim**

GitHub: https://github.com/psychic-cyber

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
