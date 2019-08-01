from dotenv import dotenv_values
import requests
import datetime as dt
import pandas as pd


def get_the_beginning(date):
    return dt.datetime(year=date.year, month=date.month, day=date.day, hour=0)


def get_timestamp(date):
    return int(date.timestamp())


def get_count_of_query_in_vk(query, access_token, start_time, end_time):
    '''https://vk.com/dev/newsfeed.search'''

    method_name = 'newsfeed.search'
    params = {
        'access_token': access_token,
        'v': 5.101,
        'q': query,
        'start_time': start_time,
        'end_time': end_time
    }

    response = requests.get('https://api.vk.com/method/{}'.format(method_name), params=params)
    response.raise_for_status()

    return response.json()['response']['total_count']


def get_stat_from_vk(query, days_count, access_token):
    today = get_the_beginning(dt.datetime.now())

    dates = [today - dt.timedelta(days=days) for days in range(days_count + 1)]

    counts = []
    for date in dates:
        end_time = get_timestamp(date)
        start_time = get_timestamp(date - dt.timedelta(days=1))

        total_count = get_count_of_query_in_vk(query, access_token, start_time, end_time)

        counts.append(total_count)
    return {'dates': dates, 'counts': counts}


if __name__ == '__main__':
    dotenv_dict = dotenv_values()
    access_token = dotenv_dict['access_token']

    days_count = 30
    query = 'vc.ru'

    stat_data = get_stat_from_vk(query, days_count, access_token)

    df = pd.DataFrame(stat_data)
    print(df)

    df.to_csv('stat.csv')  # сохранить в csv
