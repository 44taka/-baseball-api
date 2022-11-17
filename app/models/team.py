import sqlalchemy
from configs.database import metadata


team = sqlalchemy.Table(
    'team_mst',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer),
    sqlalchemy.Column('league_kbn', sqlalchemy.SmallInteger),
    sqlalchemy.Column('team_name', sqlalchemy.String),
    sqlalchemy.Column('team_color_cd', sqlalchemy.String),
    sqlalchemy.Column('yahoo_team_id', sqlalchemy.Integer),
    sqlalchemy.Column('date', sqlalchemy.Date),
    sqlalchemy.Column('is_deleted', sqlalchemy.Integer),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime),
)
