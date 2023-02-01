<a name="readme-top"></a>
<br />
<div align="center">
  <a href="https://github.com/ashishlamsal/sentiment-analysis">
    <img src="./frontend/public/logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Sentiment Analysis for Nepali Text</h3>

  <p align="center">
    In this project, we used MURIL (Multilingual Unsupervised Representations for Indian Languages), a multilingual BERT model, to perform sentiment analysis on Nepali text.
    <br />
    <a href="https://github.com/ashishlamsal/sentiment-analysis"><strong>View Demo »</strong></a>
    <br />
  </p>
</div>

<!-- omit in toc -->
## Table of Contents

- [About The Project](#about-the-project)
- [Dataset](#dataset)
- [Model](#model)
- [Installation](#installation)
  - [Step 1: Clone the project](#step-1-clone-the-project)
  - [Step 2: Install and Run Backend Application](#step-2-install-and-run-backend-application)
  - [Step 3: Install and Run Frontend Application](#step-3-install-and-run-frontend-application)
  - [Step 4: Open the application in browser](#step-4-open-the-application-in-browser)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## About The Project

[![Project Name Screen Shot][project-screenshot]](https://example.com)

Sentiment analysis is the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information. Sentiment analysis is widely applied to voice of the customer materials such as reviews and survey responses, online and social media, and healthcare materials for applications that range from marketing to customer service to clinical medicine. With the rise of deep language models, such as RoBERTa, also more difficult data domains can be analyzed, e.g., news texts where authors typically express their opinion/sentiment less explicitly.

Although there are some more works carried out in non-Nepali language, very few works have been carried out in Nepali language. The major objective of this project is to perform sentence level sentiment analysis in case of Nepali Language and perform EDA analysis in the available dataset.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Dataset

Source of the dataset [NepCOV19Tweets dataset](https://www.kaggle.com/datasets/mathew11111/nepcov19tweets) with 32,824 total tweets

- positive class: 14, 823 samples
- neutral class: 4,591 samples
- negative class: 13,410 samples

## Model

For this project, we have used a deep-learning approach based on MuRIL architecture. [MuRIL(Multilingual Representations for Indian Languages)](https://huggingface.co/google/muril-base-cased) is a BERT model pre-trained on 17 Indian languages and their transliterated counterparts. This model uses a BERT base architecture pretrained from scratch using the Wikipedia, Common Crawl, PMINDIA  and Dakshina  corpora for 17  Indian languages that includes Nepali as one of the languages. The model is then fine-tuned on the Nepali Covid-19 tweets dataset for sentiment analysis.

## Installation

### Step 1: Clone the project

```powershell
git clone https://github.com/ashishlamsal/sentiment-analysis.git
```

### Step 2: Install and Run Backend Application

```powershell
cd .\backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

> Note: You need to put the fine-tuned MURIL model in `\backend\ml\sentiment-model\3\`.

### Step 3: Install and Run Frontend Application

```powershell
cd .\frontend
yarn install
```

Create `.env` file inside `frontend` directory and add the following environment variables:

```plaintext
VITE_APP_BASE_URL=http://localhost:8000/run/predict
```

Finally, run the frontend application:

```powershell
yarn run dev
```

### Step 4: Open the application in browser

```http://127.0.0.1:5173/```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

> Note that the `gradio` app inside `backend/gradio` uses a private model from huggingface. In order to use private model from huggingface, you need to create a `.env` file inside `backend/gradio` directory and add the following environment variables:

```plaintext
HUGGINGFACE_TOKEN=<your-huggingface-token>
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](./LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

| <a href = "https://github.com/ashishlamsal"><img src = "https://avatars1.githubusercontent.com/u/59776422?s=400&v=4" width="144" style="border-radius:50%"></a> | <a href = "https://github.com/JanakSharma2055"><img src = "https://avatars.githubusercontent.com/u/60380225?v=4" width="144" style="border-radius:50%"></a> |
| :-: | :-: |
| [Ashish Lamsal](https://github.com/ashishlamsal) |[Janak Sharma](https://github.com/JanakSharma2055) |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [NepCOV19Tweets Dataset](https://www.hindawi.com/journals/cin/2021/2158184/)

    ```plaintext
    @article{sitaula2021deep,
    title={Deep learning-based methods for sentiment analysis on Nepali covid-19-related tweets},
    author={Sitaula, Chiranjibi and Basnet, Anish and Mainali, A and Shahi, Tej Bahadur},
    journal={Computational Intelligence and Neuroscience},
    volume={2021},
    year={2021},
    publisher={Hindawi}
    }
    ```

- [MuRIL: Multilingual Representations for Indian Languages](https://arxiv.org/abs/2103.10730)

    ```plaintext
    @misc{khanuja2021muril,
        title={MuRIL: Multilingual Representations for Indian Languages},
        author={Simran Khanuja and Diksha Bansal and Sarvesh Mehtani and Savya Khosla and Atreyee Dey and Balaji Gopalan and Dilip Kumar Margam and Pooja Aggarwal and Rajiv Teja Nagipogu and Shachi Dave and Shruti Gupta and Subhash Chandra Bose Gali and Vish Subramanian and Partha Talukdar},
        year={2021},
        eprint={2103.10730},
        archivePrefix={arXiv},
        primaryClass={cs.CL}
    }
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[project-screenshot]: ./assets/project-screenshot.png