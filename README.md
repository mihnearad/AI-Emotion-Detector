# AI Webcam Mood Improver

This project utilizes OpenAI's **GPT-3.5-turbo** model to create a mood improver bot based on webcam analysis.

## Features

- Analyze webcam feed for **age**, **gender**, and **emotion**.
- Interact with the *GPT-3.5-turbo* model based on the webcam analysis results.
- Mood improvement suggestions from the chatbot.

## Getting Started

1. **Clone the repository:**
   - `git clone https://github.com/your-username/ai-webcam-mood-improver.git`
   - `cd ai-webcam-mood-improver`

3. **Set up OpenAI API key:**
   - Create a `.env` file in the project root.
   - Add your OpenAI API key to the `.env` file:
     ```plaintext
     OPENAI_API_KEY=your-api-key-here
     ```

4. **Run the webcam analysis and OpenAI interaction script:**
   - `python analyze_webcam.py`

## Usage

- Adjust the `duration` parameter in `analyze_webcam.py` to control the analysis duration.
- Customize the user message and system instruction in `main_script.py` to suit your application.

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
