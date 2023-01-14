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

- [1. About The Project](#1-about-the-project)
- [2. Installation](#2-installation)
  - [2.1. Clone the project](#21-clone-the-project)
  - [2.2. Install and Run Backend Application](#22-install-and-run-backend-application)
  - [2.3. Install and Run Frontend Application](#23-install-and-run-frontend-application)
  - [2.4. Open the application in browser](#24-open-the-application-in-browser)
- [3. License](#3-license)
- [4. Contact](#4-contact)
- [5. Acknowledgments](#5-acknowledgments)

## 1. About The Project

[![Project Name Screen Shot][project-screenshot]](https://example.com)

Sentiment analysis is the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information. Sentiment analysis is widely applied to voice of the customer materials such as reviews and survey responses, online and social media, and healthcare materials for applications that range from marketing to customer service to clinical medicine. With the rise of deep language models, such as RoBERTa, also more difficult data domains can be analyzed, e.g., news texts where authors typically express their opinion/sentiment less explicitly.

Although there are some more works carried out in non-Nepali language, very few works have been carried out in Nepali language. The major objective of this project is to perform sentence level sentiment analysis in case of Nepali Language and perform EDA analysis in the available dataset.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 2. Installation

### 2.1. Clone the project

```git clone https://github.com/ashishlamsal/sentiment-analysis.git```

### 2.2. Install and Run Backend Application

```powershell
cd .\backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### 2.3. Install and Run Frontend Application

```powershell
cd .\frontend
yarn install
yarn run dev
```

### 2.4. Open the application in browser

```http://127.0.0.1:5173/```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## 3. License

Distributed under the MIT License. See [LICENSE](./LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## 4. Contact

| <a href = "https://github.com/ashishlamsal"><img src = "https://avatars1.githubusercontent.com/u/59776422?s=400&v=4" width="144" style="border-radius:50%"></a> | <a href = "https://github.com/JanakSharma2055"><img src = "https://avatars.githubusercontent.com/u/60380225?v=4" width="144" style="border-radius:50%"></a> |
| :-: | :-: |
| [Ashish Lamsal](https://github.com/ashishlamsal) |[Janak Sharma](https://github.com/JanakSharma2055) |

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## 5. Acknowledgments

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