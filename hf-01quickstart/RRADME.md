

## 安装步骤
1.‌创建conda环境
```shell
conda create -n transformers_env python=3.13
conda activate transformers_env
conda deactivate
```

2.‌安装Transformers库‌：在激活的环境中，使用以下命令安装Transformers库：
```shell
conda install -c huggingface transformers
pip install torch torchvision torchaudio
conda activate transformers_env

```

3.‌验证安装‌：安装完成后，可以通过以下命令验证Transformers库是否成功安装：
```shell
python -c "from transformers import pipeline; print(pipeline.__version__)"
```

如果说用到了 conda 虚拟环境，则需要找到虚拟环境对应的 python 路径，可以使用 whereis python 查看，比如：
在所配置的 launch.json 文件中的 configurations 列表中加入这一行：
"pythonPath": "/opt/anaconda3/envs/transformers_env/bin/python"



## 智能体和工具

https://huggingface.co/docs/transformers/zh/agents

copipnda install accelerate spaces diffuser
/opt/anaconda3/envs/transformers_env/bin/python install accelerate diffusers

## 使用LLM进行文本生成

https://huggingface.co/docs/transformers/zh/llm_tutorial

/opt/anaconda3/envs/transformers_env/bin/python install transformers bitsandbytes>=0.39.0 -q

## smolagents

pip install smolagents
