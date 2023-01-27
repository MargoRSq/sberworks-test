from starlette.config import Config

config = Config("../.env")

ES_NAME: str = config("ES_USERNAME")
ES_PASS: str = config("ES_PASSWORD")
ES_HOST: str = config("ES_HOST")
