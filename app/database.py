# from elasticsearch import Elasticsearch
#
# es = Elasticsearch(
#     [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}]
# )
# sample_items = [
#     {"name": "Sample Item 1", "description": "Description 1", "price": 10.00},
#     {"name": "Sample Item 2", "description": "Description 2", "price": 20.00},
#     {"name": "Sample Item 3", "description": "Description 3", "price": 30.00},
# ]
#
# for item in sample_items:
#     es.index(index="items", body=item)

from elasticsearch import Elasticsearch
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

es = Elasticsearch([{"host": "elasticsearch", "port": 9200, "scheme": "http"}])


def create_index(index_name):
    """
    Description: Create an index

    Args: index_name ('str'): Name of index

    Returns: None
    """
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)
        logger.info(f"Created index: {index_name}")
    else:
        logger.info(f"Index {index_name} already exists")
