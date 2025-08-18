"""bis_scraper package: modularized scraping logic for BIS PDFs.

This package mirrors the behavior found in the `scrape-Bis.ipynb` notebook without adding features.
"""

from .scraper import scrape
from .config_loader import load_config

__all__ = ["scrape", "load_config"]
