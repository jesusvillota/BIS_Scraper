from __future__ import annotations
import os
from typing import Any, Dict
import yaml


def load_config(path: str) -> Dict[str, Any]:
    """Load YAML configuration from the given path.

    Returns a plain dict with keys used by the scraper.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    # Provide minimal defaults only if keys are missing, but keep exact behavior otherwise
    defaults = {
        "BASE_URL": "https://www.bis.org",
        "DOWNLOAD_DIR": "downloads",
        "INITIAL_DATE": "01/01/2000",
        "FINAL_DATE": "11/08/2025",
        "PAGE_LENGTH": 10,
        "MAX_PAGE": 2,
    }
    for k, v in defaults.items():
        data.setdefault(k, v)

    # Normalize download dir to ensure it exists later
    data["DOWNLOAD_DIR"] = os.path.normpath(str(data["DOWNLOAD_DIR"]))
    return data
