from __future__ import annotations
import argparse
from bis_scraper import load_config, scrape


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scrape BIS PDFs (matches notebook behavior)")
    parser.add_argument("--config", default="config.yaml", help="Path to YAML config file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = load_config(args.config)
    scrape(cfg)


if __name__ == "__main__":
    main()
