import databases
import sqlalchemy

from configs.api import ApiEnvConfig, ApiDatabaseConfig


# config読み込み
api_db_config = ApiDatabaseConfig()
api_env_config = ApiEnvConfig()

# DBのURL設定
url_template = '{driver}://{user}:{password}@{host}/{database}?charset=utf8mb4'
url = url_template.format(**api_db_config.dict())
if api_env_config.env == 'production':
    url += '&ssl=true'

DATABASE_URL = databases.DatabaseURL(url=url)
db = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
