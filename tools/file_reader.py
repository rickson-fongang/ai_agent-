from tools.base_tool import BaseTool

class FileReaderTool(BaseTool):
    def name(self):
        return "read_file"

    def description(self):
        return "Reads a local file"

    def execute(self, args):
        path = args.get("path")
        try:
            with open(path, "r") as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"

    def get_declaration(self):
        return {
            "name": "read_file",
            "description": "Read file content",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"}
                },
                "required": ["path"]
            }
        }