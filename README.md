# GPT-3.5-Turbo Chatbot

This project is a simple chat application built using Streamlit and OpenAI's GPT-3.5-Turbo model. It allows users to interact with the GPT-3.5-Turbo model through a chat interface.

## Features

- Chat interface to interact with GPT-3.5-Turbo.
- Keeps a history of the chat conversation.
- Configurable via `config.json`.

## Prerequisites

- Python 3.7 or higher
- Streamlit
- OpenAI Python client

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sakethyalamanchili/GPT-3.5-Turbo-Chatbot.git
   cd GPT-3.5-Turbo-Chatbot
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `config.json` file in the root directory of the project with the following content:

   ```json
   {
     "OPENAI_API_KEY": "your-openai-api-key"
   }
   ```

   Replace `"your-openai-api-key"` with your actual OpenAI API key.

## Usage

1. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501` to interact with the chat interface.

## Code Overview

- `app.py`: The main script for running the Streamlit application. It sets up the Streamlit page, handles user input, and interacts with the OpenAI API.

- `config.json`: Configuration file for storing the OpenAI API key.

## Troubleshooting

- **Rate Limit Error**: If you encounter a rate limit error, you may have exceeded your OpenAI API usage quota. Check your OpenAI account and billing details.

- **Module Not Found Error**: Ensure all required packages are installed by running `pip install -r requirements.txt`.c
