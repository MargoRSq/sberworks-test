from starlette.config import Config

config = Config(".env")

ES_NAME: str = config("ELASTIC_USERNAME")
ES_PASS: str = config("ELASTIC_PASSWORD")
ES_HOST: str = config("ES_HOST")
ES_PORT: str = config("ES_PORT")
