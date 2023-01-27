import json
import urllib3

from elasticsearch import Elasticsearch

from config import ES_NAME, ES_HOST, ES_PASS


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
es = Elasticsearch(ES_HOST, basic_auth=[ES_NAME, ES_PASS],
                   verify_certs=False, ssl_show_warn=False)


def post_to_index(json_filename: str, index_name: str):
    with open(json_filename) as f:
        data = json.load(f)
    for field in data['data']:
        es.index(index=index_name, document=field)


def get_index_sources(index_name: str) -> list[dict]:
    resp = es.search(index=index_name, query={"match_all": {}})

    return [d['_source'] for d in resp.body['hits']['hits']]


def get_aggregations(index_name: str,
                     from_timestamp: int, to_timestamp: int):
    query = {
        "range": {
            "timestamp": {
                "gte": from_timestamp,
                "lt": to_timestamp
            }
        }
    }
    aggs = {
            "math_values": {"stats": {"field": "value"}}
    }

    result = es.search(index=index_name,
                       query=query, aggs=aggs).body
    return result['aggregations']['math_values']
