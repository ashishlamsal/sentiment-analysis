import { useState, useEffect } from "react";
import NavBar from "./components/NavBar";
import axios from "axios";

export default function App() {
  const [inputValue, setInputValue] = useState("");
  const [sentiment, setSentiment] = useState("");
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const [theme, setTheme] = useState("light");
  const toggleTheme = () => {
    setTheme(theme === "dark" ? "light" : "dark");
  };

  const handleClick = async () => {
    setIsLoading(true);
    try {
      const response = await axios.post(import.meta.env.VITE_APP_BASE_URL, {
        data: [inputValue],
        // add headers
        headers: {
          "Content-Type": "application/json",
        },
      });

      // get result in json format
      const result = await response.data;

      // set sentiment
      const predicted_label = result["data"][0]["predicted_label"];

      setSentiment(predicted_label);
      setResult(result["data"][0]["each_class_pred"]);
    } catch (err) {
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    document.querySelector("html").setAttribute("data-theme", theme);
  }, [theme]);

  return (
    <div className="h-screen w-screen">
      <NavBar toggleTheme={toggleTheme} />
      <main className="container max-w-2xl mx-auto text-center pt-6">
        <h1 className="text-4xl font-bold mt-4 py-4">
          Sentiment Analysis for Nepali Text
        </h1>
        {/* add subheading decription */}
        <p className="text-gray-500 mb-4 pb-6 text-center">
          In this project, we used MURIL (Multilingual Unsupervised
          Representations for Indian Languages), a multilingual BERT model, to
          perform sentiment analysis on Nepali text. We fine-tuned it on a
          labeled dataset of Nepali text to optimize it for the specific task of
          sentiment analysis.
        </p>

        <div className="form-control my-4">
          <div className="input-group justify-center">
            <input
              type="text"
              placeholder="Type here in Nepali…"
              className="input input-bordered input-lg w-full max-w-lg"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
            />
            <button
              className={`btn btn-square btn-lg ${isLoading ? "loading" : ""}`}
              onClick={handleClick}
            >
              {isLoading ? (
                ""
              ) : (
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-6 w-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                  />
                </svg>
              )}
            </button>
          </div>
        </div>
        {result && (
          <div className="flex justify-evenly items-center stats shadow mx-11">
            <div className="py-2 stat place-items-center">
              {sentiment === "positive" && <span className="text-8xl">🥳</span>}
              {sentiment === "negative" && <span className="text-8xl">😭</span>}
              {sentiment === "neutral" && <span className="text-8xl">😐</span>}
            </div>
            <ul className="menu w-100 stat place-items-center">
              <li className="py-2">
                Positive: {(result["positive"] * 100).toFixed(2)}%
              </li>
              <progress
                className="progress progress-success w-56"
                value={result["positive"] * 100}
                max="100"
              ></progress>
              <li className="py-2">
                Neutral: {(result["neutral"] * 100).toFixed(2)}%
              </li>
              <progress
                className="progress w-56"
                value={result["neutral"] * 100}
                max="100"
              ></progress>
              <li className="py-2">
                Negative: {(result["negative"] * 100).toFixed(2)}%
              </li>
              <progress
                className="progress progress-error w-56"
                value={result["negative"] * 100}
                max="100"
              ></progress>
            </ul>
          </div>
        )}
      </main>
    </div>
  );
}
