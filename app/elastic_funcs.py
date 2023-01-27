import json
import urllib3

# from typing import List
from datetime import datetime

from elasticsearch import Elasticsearch

from config import ES_NAME, ES_HOST, ES_PASS


urllib3.disable_warnings()
es = Elasticsearch(ES_HOST, basic_auth=[ES_NAME, ES_PASS], verify_certs=False)


def create_query(from_timestamp: int, to_timestamp: int):
    q = {
       "query": {
            "range": {
                "timestamp": {
                    "gte": from_timestamp,
                    "lt": to_timestamp
                }
            }
        }
    }
    return q


def post_to_index(json_filename: str, index_name: str):
    with open(json_filename) as f:
        data = json.load(f)
    for field in data['data']:
        es.index(index=index_name, document=field)


def get_index_sources(index_name: str) -> list[dict]:
    resp = es.search(index=index_name, query={"match_all": {}})

    return [d['_source'] for d in resp.body['hits']['hits']]


def count_fileds(index_name: str,
                 from_timestamp: int, to_timestamp: int):
    return es.count(index=index_name,
                    body=create_query(from_timestamp, to_timestamp))['count']
