import gradio as gr
import torch
import os
from transformers import AutoConfig, AutoTokenizer, AutoModelForSequenceClassification
from gradio.components import JSON, Textbox
from dotenv import load_dotenv

load_dotenv()


def sentiment_analysis(text):
    id2label = {0: "negative", 1: "neutral", 2: "positive"}
    label2id = {"negative": 0, "neutral": 1, "positive": 2}

    auth_token = os.getenv("HUGGINGFACE_TOKEN") or True
    saved_checkpoint = f"ashishlamsal/sentiment-analysis-nepali"

    config = AutoConfig.from_pretrained(
        saved_checkpoint,
        label2id=label2id,
        id2label=id2label,
        use_auth_token=auth_token,
    )
    tokenizer = AutoTokenizer.from_pretrained(
        saved_checkpoint, use_auth_token=auth_token
    )
    model = AutoModelForSequenceClassification.from_pretrained(
        saved_checkpoint, num_labels=3, use_auth_token=auth_token
    )

    tokens = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    tokens = {name: tensor.cpu() for name, tensor in tokens.items()}
    model = model.cpu()
    with torch.no_grad():
        logits = model(**tokens)[0]
        normalized_pred = torch.softmax(logits, dim=1).cpu().numpy()

    each_class_score = normalized_pred[0]  # normalized pred was 2d array
    top_prediction = normalized_pred.argmax().item()
    top_prediction_score = each_class_score[top_prediction]
    predicted_label = config.id2label[top_prediction] or "no prediction"
    each_class_pred = {
        config.id2label[id]: float(score) for id, score in enumerate(each_class_score)
    }
    return {
        "predicted_label": predicted_label,
        "predicted_score": float(top_prediction_score),
        "each_class_pred": each_class_pred,
    } or "No Prediction"


iface = gr.Interface(
    fn=sentiment_analysis,
    inputs=Textbox(lines=3, label="Text"),
    outputs=JSON(label="Prediction"),
    title="Sentiment Analysis for Nepali Text",
    description="Predict the sentiment of a Nepali text using a finetuned MURIL model.",
    interpretation="default",
    examples=[
        # positive example
        ["कोभिड विरुद्ध राष्ट्रव्यापी खोप अभियान"],
        # neutral example
        ["मेरो नाम कोरोना भाइरस हो"],
        # negative example
        ["भारतबाट घर फर्किने क्रम बढेसंँगै नाकामा संक्रमितको संख्यापनि बढ्न थालेको छ"],
    ],
)

iface.launch()

# {
#     "data": [
#         {
#             "predicted_label": "negative",
#             "predicted_score": 0.9930140376091003,
#             "each_class_pred": {
#                 "negative": 0.9930140376091003,
#                 "neutral": 0.002179638249799609,
#                 "positive": 0.0048062680289149284,
#             },
#         }
#     ],
#     "is_generating": false,
#     "duration": 2.1564486026763916,
#     "average_duration": 2.2250293493270874,
# }
