# Scraper for Analysis

A Python-based web scraping project designed to collect structured data from websites and export it into analyzable formats such as CSV.
The project demonstrates clean project structure, modular scraping architecture, and proper Git workflow for collaborative development.

## Project Overview

This project demonstrates:
- Web scraping with Python
- HTML parsing using BeautifulSoup
- HTTP requests handling
- Data cleaning and preprocessing
- Exporting structured datasets for analysis
- Modular scraper architecture
- Git branching workflow
- The scraper extracts useful data from web pages and organizes it into datasets that can later be used for data analysis, machine learning, or visualization tasks.

## Project Structure

```
Scraper_for_Analysis/
│
├── pyproject.toml            # Project dependencies and metadata
├── README.md                 # Project documentation
│
├── data/                     # Output datasets
│   └── scraped_data.csv
│
├── src/
│   ├── main.py               # Entry point of the scraper
│   │
│   └── scraper/
│       ├── crawler.py        # Website navigation and crawling
│       ├── parsers.py        # Extracts structured data from HTML
│       ├── exporters.py      # Exports data to CSV
│       └── utils.py          # Helper and cleaning functions
│
└── tests/                    # Future test cases
```
## Requirements

- Python 3.10+
- Internet connection
- Package manager (uv recommended)

## Required Python libraries:

- requests
- beautifulsoup4
- pytest (optional for testing)

## Setup Instructions
### 1. Clone the Repository

git clone https://github.com/SOBAN-SAQIB/Scraper_for_Analysis.git
cd Scraper_for_Analysis

### 2. Install Dependencies
- Using uv (recommended):
 ```bash
uv pip install -r requirements.txt
 ```
- or install manually:
```bash
pip install requests beautifulsoup4
```
## Running the Scraper

Run the project from the root directory.

- Using uv
- uv run src/main.py
- Using Python
- python src/main.py

The scraper will start collecting data and export the results to the data folder.

## Git Workflow

This project follows a structured branching strategy.


## Development Workflow
- 1. Start with main branch
- 2. Create dev branch
```bash
   └─ Development work happens here
   ```
- 3. Create feature branches
 ```bash
   └─ Create feature/product-details
   └─ Create feature/catalog-navigation
   └─ Create fix/url-resolution
	 └─ Create fix/deduplication

```
- 4. Merge features into dev
- 5. Test functionality
- 6. Merge dev into main
 ```bash
   └─ Final stable version
```
## Scraper Components

### Crawler (crawler.py)

Responsible for navigating through the website.

-Functions may include:
- Discovering pages
- Handling pagination
- Collecting page URLs
- Sending HTTP requests

### Parsers (parsers.py)

Extract structured information from HTML pages.

Typical extracted fields:

- Titles
- Prices
- Descriptions
- Links
- Other metadata

### Exporters (exporters.py)

Responsible for saving the scraped data.

- Exports data to:
- CSV files
- Structured datasets for analysis

### Utilities (utils.py)

Helper functions used across the project.

- Text cleaning
- URL normalization
- Safe dictionary access
- Data formatting

## Key Features
### Modular Scraper Architecture

Each component of the scraper has a dedicated role:

- Crawling
- Parsing
- Cleaning
- Exporting



## Structured Data Export

Scraped data is saved in CSV format, making it easy to use for:

- Data analysis
- Machine learning
- Visualization
- Error Handling



## Future Improvements

Possible improvements include:
- Adding async scraping
- Implementing database storage
- Adding logging system
- Creating data visualization pipeline
- Adding unit tests

## License

This project is created for educational and learning purposes.

## Author

- Soban Saqib
- Data Science Student
- Python | Web Scraping | Data Analysis

GitHub:
https://github.com/SOBAN-SAQIB
