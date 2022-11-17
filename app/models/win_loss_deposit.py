import sqlalchemy
from configs.database import metadata


win_loss_deposit = sqlalchemy.Table(
    'win_loss_deposit_tbl',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer),
    sqlalchemy.Column('date', sqlalchemy.Date),
    sqlalchemy.Column('deposit', sqlalchemy.Integer),
    sqlalchemy.Column("team_id", sqlalchemy.Integer),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
)
