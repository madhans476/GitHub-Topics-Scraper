# GitHub Topics Scraper

This project is a Python-based web scraper that extracts information from the GitHub topics page. It gathers details about various topics and their top repositories, storing the collected data in CSV files for further analysis and use.

## Features

- Scrapes the [GitHub Topics](https://github.com/topics) page.
- Retrieves topic title, description, and URL.
- For each topic, retrieves the top 20 repositories.
- Extracts repository details: name, username, stars, and URL.
- Saves the data for each topic in separate CSV files within a specified directory.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/madhans476/github-topics-scraper.git
    cd github-topics-scraper
    ```

2. **Install the required packages:**

    You can install the necessary packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Create the directory structure:**

    Ensure that the directory for storing the CSV files exists:

    ```bash
    mkdir github_topics
    ```

## Usage

1. **Run the script:**

    Execute the script to start scraping:

    ```bash
    python ws_github_trending_topics.py
    ```

    The script will scrape the GitHub topics page, gather the required data, and save it in CSV files within the `github_topics` directory.

2. **Check the output:**

    The CSV files will be saved in the `github_topics` directory. Each file will be named after the respective topic, containing details of the top 20 repositories.

## Example

Example structure of the saved CSV files:

```plaintext
github_topics/
├── Trending_github_topics.csv
├── 3D.csv
├── AI.csv
├── Machine Learning.csv
├── Web Development.csv
└── ...
```
Each CSV file will have the following columns:

──Repo Name
──Username
──Stars
──Repo URL
