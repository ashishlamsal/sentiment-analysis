import { useState, useEffect } from "react";
import NavBar from "./components/NavBar";

export default function App() {
  const [theme, setTheme] = useState("light");
  const toggleTheme = () => {
    setTheme(theme === "dark" ? "light" : "dark");
  };

  useEffect(() => {
    document.querySelector("html").setAttribute("data-theme", theme);
  }, [theme]);

  return (
    <div className="h-screen w-screen">
      <NavBar toggleTheme={toggleTheme} />
      <main className="container max-w-2xl mx-auto text-center pt-6">
        <h1 className="text-4xl font-bold mt-4 py-4">Sentiment Analysis</h1>
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
              placeholder="Type here…"
              className="input input-bordered input-lg w-full max-w-lg"
            />
            <button className="btn btn-square btn-lg">
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
            </button>
          </div>
        </div>
        <div className="py-2">
          <span className="text-9xl">😭</span>
          <span className="text-9xl">😐</span>
          <span className="text-9xl">🥳</span>
        </div>
      </main>
    </div>
  );
}
