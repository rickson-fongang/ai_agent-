from typing import Dict
from tools.base_tool import BaseTool

class ToolRegistry:
    def __init__(self):
        self.tools: Dict[str, BaseTool] = {}

    def register(self, tool: BaseTool):
        self.tools[tool.name()] = tool

    def get_tool(self, name: str):
        return self.tools.get(name)

    def execute_tool(self, name: str, args: Dict):
        tool = self.get_tool(name)
        if not tool:
            return f"Error: Tool '{name}' not found"

        try:
            return tool.execute(args)
        except Exception as e:
            return f"Tool execution error: {str(e)}"

    def get_declarations(self):
        return [tool.get_declaration() for tool in self.tools.values()]