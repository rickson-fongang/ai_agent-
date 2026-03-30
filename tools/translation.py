from tools.base_tool import BaseTool

class TranslationTool(BaseTool):
    def name(self):
        return "translate"

    def description(self):
        return "Translate text into another language"

    def execute(self, args):
        text = args.get("text")
        lang = args.get("target_language")
        return f"Translated '{text}' to {lang}"  # simple mock

    def get_declaration(self):
        return {
            "name": "translate",
            "description": "Translate text",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"},
                    "target_language": {"type": "string"}
                },
                "required": ["text", "target_language"]
            }
        }