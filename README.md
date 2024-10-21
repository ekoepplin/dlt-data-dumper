# NewsAPI Data Ingestion with DLT

This project demonstrates how to ingest data from the NewsAPI using the Data Load Tool (DLT) library. It fetches top headlines, article searches, and news sources, then loads them into a DuckDB database.

## Features

- Fetch top headlines from NewsAPI
- Search for articles on specific topics
- Retrieve news sources information
- Load data into DuckDB using DLT
- Jupyter notebook for interactive data exploration

## Prerequisites

- Python 3.11.8
- Poetry for dependency management

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd dlt-newsapi-ingestion
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

3. Activate the virtual environment:
   ```
   poetry shell
   ```

4. Set up your NewsAPI key:
   - Sign up for a free API key at [https://newsapi.org/](https://newsapi.org/)
   - Set the API key as an environment variable:
     ```
     export NEWS_API_KEY=your_api_key_here
     ```

## Usage

### Running the Pipeline

To run the data ingestion pipeline, use the `newsapi_pipeline.py` script. This script supports various command-line options for different execution modes:

1. Normal mode:
   ```
   python newsapi_pipeline.py
   ```

2. Test mode (uses DuckDB instead of filesystem):
   ```
   python newsapi_pipeline.py --test
   ```

3. Full refresh (replaces existing data instead of appending):
   ```
   python newsapi_pipeline.py --full-refresh
   ```

4. Custom log level:
   ```
   python newsapi_pipeline.py --log-level DEBUG
   ```

You can also combine these options as needed. For example:
```
python newsapi_pipeline.py --test --full-refresh --log-level DEBUG
```

This script will fetch data from NewsAPI and load it into either a filesystem-based storage (default) or a DuckDB database (in test mode).

### Exploring Data with Jupyter Notebook

1. Start Jupyter Notebook:
   ```
   jupyter notebook
   ```

2. Open the `eda-newsapi.ipynb` notebook in your browser.

3. Run the cells to fetch data and perform exploratory data analysis.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE).
