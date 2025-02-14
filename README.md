# Meeting Genius: Meeting Summarizer & Action Item Extractor API

Meeting Genius is a FastAPI-based REST API that helps teams quickly extract key insights from their meeting transcripts. The API accepts a meeting transcript as input and returns:
- A concise summary of the meeting
- A list of action items extracted from the discussion

This tool is designed to save time and ensure that important points and follow-ups are captured from meetings.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [Testing the API](#testing-the-api)
- [API Endpoints](#api-endpoints)
- [Docker Usage](#docker-usage)
- [Future Improvements](#future-improvements)
- [License](#license)

## Features

- **Meeting Summarization:** Generate a concise summary of meeting discussions.
- **Action Item Extraction:** Automatically identify follow-up tasks or action items.
- **Interactive Documentation:** Uses FastAPI’s auto-generated Swagger UI for easy testing.
- **Modular & Extensible:** Built with clean, modular Python code.

## Tech Stack

- **Python 3.8+**
- **FastAPI** for building the REST API.
- **Uvicorn** as the ASGI server.
- **Hugging Face Transformers** for text generation and summarization.
- **Docker** (optional) for containerized deployment.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com//MeetingGenius.git
cd MeetingGenius

