from tools.base_tool import BaseTool

class CalculatorTool(BaseTool):
    def name(self):
        return "calculator"

    def description(self):
        return "Performs mathematical calculations"

    def execute(self, args):
        expression = args.get("expression", "")
        try:
            return str(eval(expression))
        except Exception:
            return "Invalid mathematical expression"

    def get_declaration(self):
        return {
            "name": "calculator",
            "description": "Evaluate math expressions",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string"}
                },
                "required": ["expression"]
            }
        }