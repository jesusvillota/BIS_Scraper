from __future__ import annotations
import argparse
from bis_scraper import load_config, scrape, bis_link, process_pdfs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scrape BIS PDFs based on tutorial1.ipynb")
    parser.add_argument("--config", default="config.yaml", help="Path to YAML config file")
    parser.add_argument("--test-link", action="store_true", help="Test bis_link function with config parameters")
    parser.add_argument("--extract-text", action="store_true", help="Extract text from PDFs in DOWNLOAD_DIR")
    parser.add_argument("--pdfs", nargs="*", help="Specific PDF files to process (if not specified, all PDFs in DOWNLOAD_DIR will be processed)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = load_config(args.config)
    
    if args.test_link:
        # Demonstrate the bis_link function
        link = bis_link(
            cfg["INITIAL_DATE"], 
            cfg["FINAL_DATE"], 
            1, 
            int(cfg["PAGE_LENGTH"])
        )
        print(f"🔗 Generated link: {link}")
    elif args.extract_text:
        # Extract text from PDFs
        process_pdfs(cfg["DOWNLOAD_DIR"], cfg["TEXT_DIR"], args.pdfs)
    else:
        # Run the scraper
        scrape(cfg)


if __name__ == "__main__":
    main()
