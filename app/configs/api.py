from pydantic import BaseSettings


class ApiEnvConfig(BaseSettings):
    env: str

    class Config:
        env_file_encoding = 'utf-8'
        env_prefix = 'api_'


class ApiDatabaseConfig(BaseSettings):
    driver: str = 'mysql'
    host: str
    database: str
    user: str
    password: str

    class Config:
        env_file_encoding = 'utf-8'
        env_prefix = 'mysql_'
