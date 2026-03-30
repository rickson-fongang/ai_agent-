from registry import ToolRegistry
from memory import MemoryManager

from tools.calculator import CalculatorTool
from tools.time_tool import TimeTool
from tools.translation import TranslationTool
from tools.file_reader import FileReaderTool

from agent import Agent


def main():
    registry = ToolRegistry()
    memory = MemoryManager()

    # Register tools
    registry.register(CalculatorTool())
    registry.register(TimeTool())
    registry.register(TranslationTool())
    registry.register(FileReaderTool())

    agent = Agent(registry, memory)
    agent.run()


if __name__ == "__main__":
    main()