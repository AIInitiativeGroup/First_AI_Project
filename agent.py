class SimpleAgent:
    def __init__(self, name):
        self.name = name
        self.memory = []

    def observe(self, user_input):
        """Receive input from environment"""
        self.memory.append(user_input)
        return user_input.lower()

    def decide(self, observation):
        """Decide action based on input"""
        if "hello" in observation:
            return "greet"
        elif "time" in observation:
            return "time"
        elif "bye" in observation:
            return "exit"
        else:
            return "unknown"

    def act(self, action):
        """Perform action"""
        if action == "greet":
            return "Hello! I am your Python Agent 🤖"
        elif action == "time":
            from datetime import datetime
            return f"Current time is {datetime.now().strftime('%H:%M:%S')}"
        elif action == "exit":
            return "Goodbye! 👋"
        else:
            return "I don't understand yet, but I'm learning!"
