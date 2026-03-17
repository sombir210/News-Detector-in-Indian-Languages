# Fake News Detector in Indian Languages (News Checker)

A simple AI-powered web application designed to verify news and claims, specifically focusing on Indian languages. It uses Google's Gemini AI to analyze claims against real-time web search results from DuckDuckGo.

## Features

- **Input Support**: Accepts news text or claims in various languages (optimized for Indian context).
- **Web Verification**: Searches the web for fact-checks and relevant articles using DuckDuckGo.
- **AI Analysis**: Uses Google Gemini to synthesize findings and provide a veracity verdict.
- **Source Transparency**: Displays the raw sources used for the analysis.
- **Simple UI**: Built with Streamlit for an easy-to-use interface.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or higher
- A Google API Key for accessing Gemini (GenAI).

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/VardaanSharma100/News-Detector-in-Indian-Languages.git
   cd "News-Detector-in-Indian-Languages"
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Secrets:**
   Create a folder named `.streamlit` in the root directory.
   Inside it, create a file named `secrets.toml`.
   Add your Google Gemini API key:
   ```toml
   GEMINI_API_KEY = "your_actual_api_key_here"
   ```

## Usage

1. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

2. **Check News:**
   - The application will open in your default web browser (usually at `http://localhost:8501`).
   - Paste the news text or claim you want to verify into the text area.
   - Click the "Check Veracity" button.
   - Wait for the AI to search and analyze.
   - Read the verdict and review the cited sources.

## Project Structure

- `app.py`: The main entry point for the Streamlit application (UI).
- `logic.py`: Contains the core logic for web searching (`ddgs`) and interacting with the AI model (`google-genai`).
- `requirements.txt`: List of Python dependencies.

## Technologies Used

- **Streamlit**: Web framework.
- **Google GenAI SDK**: For accessing the Gemini model.
- **DDGS (DuckDuckGo Search)**: For retrieving real-time information from the web.
- **Streamlit Secrets**: For managing sensitive configuration.
