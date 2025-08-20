# BIS Scraper

© Jesus Villota Miranda 2025. All rights reserved.

A comprehensive tool for scraping central bank speeches published by the Bank for International Settlements (BIS). This project provides an automated way to collect, download, and extract text from speech PDFs available on the BIS website.

## Project Purpose

The BIS Scraper is designed to automate the collection of central bank speeches for research, analysis, and archival purposes. It navigates through the BIS website's speech repository, extracts links to speech PDFs, downloads them, and optionally converts them to plain text for easier analysis.

## Features

- Automated scraping of BIS central bank speeches
- PDF downloading with configurable parameters
- Text extraction from downloaded PDFs
- Fully configurable via YAML configuration
- Command-line interface for easy execution

## Project Structure

```
BIS_Scraper/
├── bis_scraper/            # Core package containing scraping logic
│   ├── __init__.py         # Package exports
│   ├── config_loader.py    # Configuration handling
│   ├── scraper.py          # Main scraping implementation
│   └── pdf_extractor.py    # PDF text extraction utilities
├── downloads/              # Default directory for downloaded PDFs
├── texts/                  # Directory for extracted text files
├── config.yaml             # Configuration file
├── main.py                 # CLI entry point
├── pyproject.toml          # Project metadata and dependencies
├── poetry.lock             # Dependency lock file
├── requirements.txt        # Traditional requirements file
└── README.md               # This documentation
```

## Getting Started

### Installation

#### Using Poetry (recommended)
```bash
# Install dependencies using Poetry
poetry install
# Activate the virtual environment
poetry shell
```

#### Using pip
```bash
pip install -r requirements.txt
```

### Configuration

Edit the `config.yaml` file to customize the scraper's behavior:

```yaml
BASE_URL: "https://www.bis.org"    # Base URL for the BIS website
DOWNLOAD_DIR: "downloads"          # Directory for saving PDFs
TEXT_DIR: "texts"                  # Directory for saving extracted text files
INITIAL_DATE: "01/01/2000"         # Start date for speeches (MM/DD/YYYY)
FINAL_DATE: "11/08/2025"           # End date for speeches (MM/DD/YYYY)
PAGE_LENGTH: 10                    # Number of results per page
MAX_PAGE: 2                        # Maximum number of pages to scrape
```

### Usage

Run the scraper with the default configuration:

```bash
poetry run python main.py
```

Extract text from downloaded PDFs:

```bash
poetry run python main.py --extract-text
```

Extract text from specific PDF files:

```bash
poetry run python main.py --extract-text --pdfs r250715b.pdf r250717h.pdf
```

Test the URL generation functionality:

```bash
poetry run python main.py --test-link
```

Or specify a custom configuration file:

```bash
poetry run python main.py --config custom_config.yaml
```


## Requirements

- Python 3.11 or higher
- Google Chrome installed
- ChromeDriver available on your system PATH (required for Selenium)

## Dependencies

- selenium: For browser automation
- requests: For downloading PDFs
- PyYAML: For configuration parsing
- PyPDF2: For PDF text extraction

For questions or contributions, feel free to open an issue or pull request.
