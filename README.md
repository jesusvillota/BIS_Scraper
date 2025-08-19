# Scrape BIS

© Jesus Villota Miranda 2025. All rights reserved.

Minimal repository wrapping the original `scrape-Bis.ipynb` notebook. It provides a YAML-configurable CLI entrypoint while keeping the original notebook untouched and fully usable.

## Quick start

1. Install dependencies
```bash
pip install -r requirements.txt
```

2. Adjust settings in `config.yaml` if needed.

3. Run
```bash
python main.py --config config.yaml
```

This preserves the same behavior as the notebook: it iterates pages, opens each review, finds a PDF link, and downloads it to the configured folder.

## Notes
- You must have Google Chrome and a compatible ChromeDriver available on PATH for Selenium's `webdriver.Chrome()`.
- The original notebook `scrape-Bis.ipynb` remains unchanged for users who prefer running it directly.

