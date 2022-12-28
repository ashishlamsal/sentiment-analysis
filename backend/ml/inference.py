from transformers import AutoConfig, AutoTokenizer, AutoModelForSequenceClassification
import torch
import os


WORKING_DIR = os.getcwd()




def get_sentiment(text):
    id2label= {
    0: "negative",
    1: "neutral",
    2: "postive"
            }

    label2id = {
        "negative": 0,
        "neutral": 1,
        "postive": 2
            }

    saved_checkpoint = f'{WORKING_DIR}/ml/sentiment_model/3/'

    config = AutoConfig.from_pretrained(saved_checkpoint, label2id=label2id, id2label=id2label)
    tokenizer = AutoTokenizer.from_pretrained(saved_checkpoint)
    model = AutoModelForSequenceClassification.from_pretrained(saved_checkpoint, num_labels=3)

    tokens = tokenizer(text,padding=True,truncation=True, return_tensors="pt")
    tokens = {name: tensor.cpu() for name, tensor in tokens.items()}
    model = model.cpu()
    with torch.no_grad():
        predictions = model(**tokens)[0].cpu().numpy()

    top_prediction = predictions.argmax().item()
    return config.id2label[top_prediction] if top_prediction in [0,1,2] else 'no prediction'