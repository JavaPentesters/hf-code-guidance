from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from huggingface_hub import login

# 输入你的 Hugging Face 账户 Token，这里把自己的刚刚创建的token粘贴进来就行啦
login("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")

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
