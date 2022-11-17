from loguru import logger

from configs.database import db
from models.win_loss_deposit import win_loss_deposit
from models.team import team


async def get_list(league_kbn: int, term: int):
    # TODO sqlalchemyで曜日指定の条件を追加したいけど、どうやるの。。？
    query = win_loss_deposit.join(team, win_loss_deposit.c.team_id == team.c.id)\
        .select()\
        .with_only_columns([
            # 取得したいカラムを指定
            win_loss_deposit,
            team.c.team_name,
            team.c.team_color_cd,
        ])\
        .where(win_loss_deposit.c.date >= '2022-03-25') \
        .where(win_loss_deposit.c.date < '2022-10-04') \
        .order_by(win_loss_deposit.c.date)

    # リーグ指定
    if league_kbn is not None:
        query = query.where(team.c.league_kbn == league_kbn)

    # 期間指定
    if term == 0 or term is None:
        query = query.where(win_loss_deposit.c.date >= '2022-03-25') \
            .where(win_loss_deposit.c.date < '2022-10-04')
    elif term == 1:
        query = query.where(win_loss_deposit.c.date >= '2022-03-25') \
            .where(win_loss_deposit.c.date < '2022-05-01')
    elif term == 2:
        query = query.where(win_loss_deposit.c.date >= '2022-05-01') \
            .where(win_loss_deposit.c.date < '2022-06-01')
    elif term == 3:
        query = query.where(win_loss_deposit.c.date >= '2022-06-01') \
            .where(win_loss_deposit.c.date < '2022-07-01')
    elif term == 4:
        query = query.where(win_loss_deposit.c.date >= '2022-07-01') \
            .where(win_loss_deposit.c.date < '2022-08-01')
    elif term == 5:
        query = query.where(win_loss_deposit.c.date >= '2022-08-01') \
            .where(win_loss_deposit.c.date < '2022-09-01')
    elif term == 6:
        query = query.where(win_loss_deposit.c.date >= '2022-09-01') \
            .where(win_loss_deposit.c.date < '2022-10-04')

    logger.debug(query)
    result = await db.fetch_all(query)
    # logger.debug(result)

    # TODO::リファクタしたい
    tmp_data = []
    tmp_team_id = []
    for index, datum in enumerate(result):
        # TODO::sqlで曜日指定したい
        # if datum.date.weekday() not in [0, 2, 4]:
        #     continue

        if len(tmp_data) == 0:
            tmp_data.append({
                'team_id': datum.team_id,
                'team_name': datum.team_name,
                'team_color_cd': datum.team_color_cd,
                'result': []
            })
            tmp_team_id.append(datum.team_id)

        if datum.team_id not in tmp_team_id:
            tmp_data.append({
                'team_id': datum.team_id,
                'team_name': datum.team_name,
                'team_color_cd': datum.team_color_cd,
                'result': [datum.deposit]
            })
            tmp_team_id.append(datum.team_id)
        else:
            for i, tmp in enumerate(tmp_data):
                if tmp['team_id'] == datum.team_id:
                    tmp_data[i]['result'].append(datum.deposit)

    return {
        'labels': sorted(list(set([datum.date for datum in result]))),
        # TODO::sqlで曜日指定したい
        # 'labels': sorted(list(set([datum.date for datum in result if datum.date.weekday() in [0, 2, 4]]))),
        'data': tmp_data
    }
