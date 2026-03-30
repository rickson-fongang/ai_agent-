import google.generativeai as genai
import os

class Agent:
    def __init__(self, registry, memory):
        self.registry = registry
        self.memory = memory

        # Configure Gemini API
        genai.configure(api_key="AIzaSyCUp_jK22d5w1dolTjiCh4PhDUcFdLt3as")
        self.model = genai.GenerativeModel("gemini-pro")

    def run(self):
        print("AI Agent started (type 'exit' to quit)")

        while True:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            # Store user input
            self.memory.add("user", user_input)

            # Get response
            response = self.reason_act_loop(user_input)

            print("Agent:", response)

            # Store agent response
            self.memory.add("assistant", response)

    def reason_act_loop(self, user_input):
        try:
            # Generate response from Gemini
            response = self.model.generate_content(
                contents=self.memory.get()
            )

            text = response.text if response.text else ""

            user_lower = user_input.lower()

            # 🔹 TOOL 1: Calculator
            if "calculate" in user_lower or "what is" in user_lower:
                expression = (
                    user_input.lower()
                    .replace("what is", "")
                    .replace("calculate", "")
                    .strip()
                )

                if not expression:
                    return "Please provide a valid mathematical expression."

                return self.registry.execute_tool(
                    "calculator",
                    {"expression": expression}
                )

            # 🔹 TOOL 2: Time
            if "time" in user_lower:
                return self.registry.execute_tool("time", {})

            # 🔹 TOOL 3: Translation (custom)
            if "translate" in user_lower:
                return self.registry.execute_tool(
                    "translate",
                    {
                        "text": "hello",
                        "target_language": "French"
                    }
                )

            # 🔹 TOOL 4: File Reader (custom)
            if "read file" in user_lower:
                return self.registry.execute_tool(
                    "read_file",
                    {"path": "test.txt"}
                )

            # 🔹 Default: return Gemini response
            return text if text else "I couldn't generate a response."

        except Exception as e:
            return f"Agent error: {str(e)}"