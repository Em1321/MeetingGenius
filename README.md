# Meeting Summarizer and Action Items Extractor API

This project is a Python-based application that uses FastAPI and Hugging Face’s Transformers to process meeting transcripts. It leverages Google’s FLAN-T5-base model to generate a detailed meeting summary and extract a bullet list of action items from a given transcript. The project is designed to be simple, modular, and easy to test—whether through an interactive API or directly from the console.

## Features

- **Detailed Meeting Summary:** Produces a brief summary.
- **Action Items Extraction:** Identifies and lists specific action items from the meeting.
- **RESTful API:** Built with FastAPI for quick development and interactive documentation.
- **Console Testing:** Easily test the functions directly from the Python interpreter.
- **Extensible:** Ready for further customization or fine-tuning on your own data.

## Project Structure

```
meeting-summarizer/
├── main.py
├── requirements.txt
└── README.md
```

- **main.py:** Contains the FastAPI application, endpoints, and functions for generating summaries and extracting action items.
- **requirements.txt:** Lists all required Python packages.
- **README.md:** This documentation file.

## Requirements

- Python 3.8 or higher

Dependencies (listed in `requirements.txt`):
- fastapi
- uvicorn
- transformers
- torch

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/meeting-summarizer.git
   cd meeting-summarizer
   ```

2. **Create a Virtual Environment (Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the API

To start the API server, run:

```bash
uvicorn main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000). Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive testing via Swagger UI.

### API Endpoint: `/summarize_actions`

- **Method:** POST
- **Request Body (JSON):**

  ```json
  {
    "transcript": "Your meeting transcript goes here..."
  }
  ```

- **Example Request:**

  ```json
  {
    "transcript": "During today's meeting, the project team discussed the progress of the new software launch. Alex reported that the beta version is ready and that initial user testing identified a few minor issues that need fixing. Jenna suggested updating the marketing strategy to target a broader audience and proposed launching a social media campaign. Michael raised concerns about the tight deadlines and requested additional resources to ensure quality. The team agreed on a set of action items: Alex will address the beta issues, Jenna will draft an updated marketing plan, and Michael will assess resource requirements. A follow-up meeting was scheduled for next Tuesday."
  }
  ```

- **Expected Response:**

  ```json
  {
    "summary": "A brief summary covering discussion on the software launch.",
    "action_items": "Bullet list of action items: - Alex will address beta issues; - Jenna will draft an updated marketing plan; - Michael will assess resource requirements."
  }
  ```

## Testing in the Console

To test the functions directly from the Python console without running the API:

1. Open a terminal in the project directory and activate your virtual environment.
2. Start the Python interpreter by running:

   ```bash
   python
   ```

3. Run the following commands:

   ```python
   from main import generate_summary, generate_action_items

   test_transcript = (
       "During today's meeting, the project team discussed the progress of the new software launch. "
       "Alex reported that the beta version is ready and that initial user testing identified a few minor issues that need fixing. "
       "Jenna suggested updating the marketing strategy to target a broader audience and proposed launching a social media campaign. "
       "Michael raised concerns about the tight deadlines and requested additional resources to ensure quality. "
       "The team agreed on a set of action items: Alex will address the beta issues, Jenna will draft an updated marketing plan, "
       "and Michael will assess resource requirements. A follow-up meeting was scheduled for next Tuesday."
   )

   summary = generate_summary(test_transcript)
   actions = generate_action_items(test_transcript)

   print("Summary:")
   print(summary)
   print("\nAction Items:")
   print(actions)
   ```

This will print the generated summary and action items to the console.

## License

This project is licensed under the MIT License.  
> **Note:** Place the full text of the MIT License in a file named `LICENSE` in the root directory.

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)
- [Google FLAN-T5 Model Card](https://huggingface.co/google/flan-t5-base)

## Next Steps

- **Prompt and Parameter Tuning:** Experiment with different prompt wordings or generation parameters (e.g., `max_new_tokens`, `temperature`, `num_beams`) to improve output detail.
- **Fine-Tuning:** Consider fine-tuning the model on a dataset specific to your meeting transcripts for even better performance.
- **Deployment:** Containerize the application using Docker or deploy to a cloud provider for production use.


