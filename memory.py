class MemoryManager:
    def __init__(self):
        self.history = []

    def add(self, role: str, content: str):
        self.history.append({
            "role": role,
            "content": content
        })

    def get(self):
        # Convert to Gemini format
        formatted = []
        for msg in self.history:
            formatted.append({
                "role": msg["role"],
                "parts": [{"text": msg["content"]}]
            })
        return formatted