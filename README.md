# Batteraskcat-API - Tarot Application Backend for Batteraskcat

Backend API for a Tarot card reading application built with FastAPI.

## Description

Batteraskcat-API provides a REST API for working with Tarot cards. The application allows you to get a random card from the deck with its description and image.

## Features

- **Random Card Drawing**: API endpoint to get a random Tarot card with description


## Requirements

- Python 3.12+
- uv (recommended) or pip

## Installation and Setup

### 1. Clone the Project

```bash
git clone <repository-url>
cd batteraskcat-api
```

### 2. Install Dependencies

Using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

### 3. Pre-launch Configuration

#### Create Card Images Directory

Before running, you need to create the `card_images` directory and place card images in it:

```bash
mkdir card_images
```

#### Card Configuration File Structure

The `cards.json` file must contain a dictionary of cards with the following structure:

```json
{
    "card_name": {
        "display_name": "Card display name",
        "description": "Card description",
    }
}
```

**Example:**
```json
{
    "fool": {
        "display_name": "0 — The Fool",
        "description": "A fresh start and exciting adventures await. Trust the journey and embrace new beginnings with an open heart.",
    },
}
```

### 4. Running the Application

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Project Structure

```
kitarot/
├── api/                    # API routers
│   └── batteraskcat_api.py # Main API endpoints
├── core/                   # Core application logic
│   └── one_card_logic.py   # Card handling logic
├── card_images/            # Card images (create manually)
├── cards.json              # Card configuration
├── main.py                 # FastAPI application entry point
├── pyproject.toml          # Project configuration and dependencies
└── README.md               # This file
```

## Development

### Adding New Cards

1. Add the card image to the `card_images/` directory
2. Add card information to the `cards.json` file
