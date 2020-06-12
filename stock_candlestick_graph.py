# finance.naver.com crawling
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express
import plotly.graph_objects
from bs4 import BeautifulSoup

if __name__ == '__main__':
    samsung_url = 'https://finance.naver.com/item/sise_day.nhn?code=005935'
    df = pd.DataFrame()
    for page in range(1, 21):
        jusik_df = pd.read_html(f'{samsung_url}&page={page}', header=0)[0]
        df = df.append(jusik_df)

    df = df.rename(
        columns={'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})
    df['date'] = pd.to_datetime(df['date'], format='%Y.%m.%d', errors='raise')
    df = df.dropna()
    df = df.sort_values(by='date', ascending=True)
    tail = df.tail(60)

    # fig = go.Figure(data=go.Scatter(x=head['날짜'], y=head['시가']))
    # offline.plot(figure_or_data={
    #     'data': go.Scatter(x=head['날짜'], y=head['시가']),
    #     'type': 'line'
    # })
    # plotly.express.line(x=tail['날짜'], y=tail['시가']).show()
    plotly.offline.plot(figure_or_data={
        'data': plotly.graph_objects.Candlestick(
            close=df['close'], high=df['high'], open=df['open'], low=df['low'], x=df['date'])
    })