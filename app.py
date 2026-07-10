from agent import WeatherAgent


def main():

    agent = WeatherAgent()

    print("\n🌦️ Weather AI Agent")
    print("Type 'exit' to quit.\n")

    while True:

        message = input("You: ")

        if message.lower() == "exit":
            break

        reply = agent.chat(message)

        print(f"\nAssistant: {reply}\n")


if __name__ == "__main__":
    main()