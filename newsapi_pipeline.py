import argparse
from datetime import datetime, timedelta
from pathlib import Path

import dlt
from loguru import logger  # Import Loguru
from newsapi.newsapi_client import NewsApiClient

# Get today's date and calculate the date range for a 24-hour period
today = datetime.utcnow().date()
before_yesterday = today - timedelta(days=2)

target_schema_name: str = dlt.config[f"{Path(__file__).stem}.destination.schema_name"]


# Define a resource for fetching articles from the US
@dlt.resource(table_name="articles_us_en", write_disposition="append")
def get_articles_us_en(api_key=dlt.secrets.value):
    logger.info("Fetching articles from the US (English)")
    newsapi = NewsApiClient(api_key=api_key)
    articles = newsapi.get_everything(
        language="en",
        q="Artificial Intelligence OR AI",
        from_param=before_yesterday.isoformat(),
        to=today.isoformat(),
        sort_by="publishedAt",
    )
    for article in articles["articles"]:
        yield article


# Define a resource for fetching articles from Germany
@dlt.resource(table_name="articles_de_de", write_disposition="append")
def get_articles_de_de(api_key=dlt.secrets.value):
    logger.info("Fetching articles from Germany (German)")
    newsapi = NewsApiClient(api_key=api_key)
    articles = newsapi.get_everything(
        language="de",
        q="Künstliche Intelligenz OR KI OR AI",
        from_param=before_yesterday.isoformat(),
        to=today.isoformat(),
        sort_by="publishedAt",
    )
    for article in articles["articles"]:
        yield article


# Define a resource for fetching articles from Spain
@dlt.resource(table_name="articles_es_es", write_disposition="append")
def get_articles_es_es(api_key=dlt.secrets.value):
    logger.info("Fetching articles from Spain (Spanish)")
    newsapi = NewsApiClient(api_key=api_key)
    articles = newsapi.get_everything(
        language="es",
        q="Inteligencia Artificial OR IA OR AI",
        from_param=before_yesterday.isoformat(),
        to=today.isoformat(),
        sort_by="publishedAt",
    )
    for article in articles["articles"]:
        yield article


# Define a resource for fetching articles from Russia
@dlt.resource(table_name="articles_ru_ru", write_disposition="append")
def get_articles_ru_ru(api_key=dlt.secrets.value):
    logger.info("Fetching articles from Russia (Russian)")
    newsapi = NewsApiClient(api_key=api_key)
    articles = newsapi.get_everything(
        language="ru",
        q="Искусственный интеллект OR ИИ OR AI",
        from_param=before_yesterday.isoformat(),
        to=today.isoformat(),
        sort_by="publishedAt",
    )
    for article in articles["articles"]:
        yield article


# Define a resource for fetching articles from France
@dlt.resource(table_name="articles_fr_fr", write_disposition="append")
def get_articles_fr_fr(api_key=dlt.secrets.value):
    logger.info("Fetching articles from France (French)")
    newsapi = NewsApiClient(api_key=api_key)
    articles = newsapi.get_everything(
        language="fr",
        q="Intelligence Artificielle OR IA OR AI",
        from_param=before_yesterday.isoformat(),
        to=today.isoformat(),
        sort_by="publishedAt",
    )
    for article in articles["articles"]:
        yield article


# Define a resource for fetching articles from Italy
@dlt.resource(table_name="articles_it_it", write_disposition="append")
def get_articles_it_it(api_key=dlt.secrets.value):
    logger.info("Fetching articles from Italy (Italian)")
    newsapi = NewsApiClient(api_key=api_key)
    articles = newsapi.get_everything(
        language="it",
        q="Intelligenza Artificiale OR IA OR AI",
        from_param=before_yesterday.isoformat(),
        to=today.isoformat(),
        sort_by="publishedAt",
    )
    for article in articles["articles"]:
        yield article


# Define a resource for fetching articles from the UK
@dlt.resource(table_name="articles_uk_gb", write_disposition="append")
def get_articles_uk_gb(api_key=dlt.secrets.value):
    logger.info("Fetching articles from the UK (English)")
    newsapi = NewsApiClient(api_key=api_key)
    articles = newsapi.get_everything(
        language="en",
        q="Artificial Intelligence OR AI",
        from_param=before_yesterday.isoformat(),
        to=today.isoformat(),
        sort_by="publishedAt",
    )
    for article in articles["articles"]:
        yield article


@dlt.source
def run_all_articles():
    return (
        get_articles_us_en(),
        get_articles_de_de(),
        get_articles_es_es(),
        get_articles_ru_ru(),
        get_articles_fr_fr(),
        get_articles_it_it(),
        get_articles_uk_gb(),
    )


def run_pipeline(destination="filesystem", full_refresh=False):
    pipeline = dlt.pipeline(
        pipeline_name="newsapi_articles",
        destination=destination,
        dataset_name=target_schema_name,
    )

    load_info = pipeline.run(
        run_all_articles(), write_disposition="replace" if full_refresh else "append"
    )

    logger.info(f"Load info: {load_info}")
    logger.success(f"All data processed and uploaded to {destination}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="Enable test mode")
    parser.add_argument(
        "--full-refresh", action="store_true", help="Perform a full refresh"
    )
    parser.add_argument("--log-level", default="INFO", help="Set log level")
    args = parser.parse_args()

    logger.remove()
    logger.add(sink=lambda msg: print(msg, end=""), level=args.log_level)

    destination = "duckdb" if args.test else "filesystem"

    run_pipeline(destination=destination, full_refresh=args.full_refresh)
