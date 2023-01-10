from transformers import AutoConfig, AutoTokenizer, AutoModelForSequenceClassification
import torch
import os


WORKING_DIR = os.getcwd()


def get_sentiment(text):
    id2label = {
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
   

    config = AutoConfig.from_pretrained(
        saved_checkpoint, label2id=label2id, id2label=id2label)
    tokenizer = AutoTokenizer.from_pretrained(saved_checkpoint)
    model = AutoModelForSequenceClassification.from_pretrained(
        saved_checkpoint, num_labels=3)

    tokens = tokenizer(text, padding=True, truncation=True,
                       return_tensors="pt")
    tokens = {name: tensor.cpu() for name, tensor in tokens.items()}
    model = model.cpu()
    with torch.no_grad():
        logits = model(**tokens)[0]
        normalized_pred = torch.softmax(logits, dim=1).cpu().numpy()
        print(normalized_pred[0])
    each_class_score = normalized_pred[0]  # normalized pred was 2d array
    top_prediction = normalized_pred.argmax().item()
    top_prediction_score = each_class_score[top_prediction]
    predicted_label = config.id2label[top_prediction] or "no prediction"
    each_class_pred = {config.id2label[id]: float(score) for id, score in enumerate(each_class_score)}
    return {"predicted_label": predicted_label,
            "predicted_score": float(top_prediction_score),
            "each_class_pred": each_class_pred,
            } or "No Prediction"


if __name__ == "__main__":

    print(get_sentiment("hello people"))
    print("hello world")
