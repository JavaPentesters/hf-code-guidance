from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoImageProcessor


# 情感分析
# transformers.pipelines.text_classification.TextClassificationPipeline 
def sentiment_analysis(text):
    classifier = pipeline('sentiment-analysis')
    result = classifier(text)
    return result

# 加载预训练的分词器（tokenizer）
def tokenizer(tex):
    tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
    sequence = "In a hole in the ground there lived a hobbit."
    print(tokenizer(sequence))

if __name__ == "__main__":
    result = tokenizer()
    print(result)

