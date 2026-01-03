from OLD_agent import SimpleAgent

agent = SimpleAgent("Agent-1")

print("🤖 Simple Python Agent Started (type 'bye' to exit)")

while True:
    user_input = input("You: ")

    observation = agent.observe(user_input)
    action = agent.decide(observation)
    response = agent.act(action)

    print("Agent:", response)

    if action == "exit":
        break
