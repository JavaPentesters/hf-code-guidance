from transformers import ToolCollection, ReactCodeAgent

image_tool_collection = ToolCollection({"collection_slug": "huggingface-tools/diffusion-tools-6630bb19a942c2306a2cdb6f"})
agent = ReactCodeAgent(tools=[*image_tool_collection.tools], add_base_tools=True)

agent.run("Please draw me a picture of rivers and lakes.")