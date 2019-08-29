import requests, json
from bs4 import BeautifulSoup
import MySQLdb
from sqlalchemy import create_engine
import pandas as pd

class movie_crawling:

    def __init__(self, start_page=1, last_page=20):
        self.start_page = start_page
        self.last_page = last_page

    def movie_crawling(self):
        df = pd.DataFrame(columns=['movie','name'])

        for i in range(self.start_page, self.last_page+1):
            response = requests.get("https://movie.naver.com/movie/point/af/list.nhn?&page={}".format(i))
            dom = BeautifulSoup(response.content, "html.parser")
            datas = dom.select("#old_content  .list_netizen  tbody tr")
            for data in datas:
                point = data.select_one(".point").text
                title = data.select_one(".title .movie").text
                user = data.select_one(".num .author").text
                df = df.append({'movie': title, 'name':user,'point':point}, ignore_index=True)

        return df

    def main_crawling(self):
        frames = []
        for page in range(10):
            frames.append(self.movie_crawling(page*100 + 1, (page+1)*100))
        result_df = pd.concat(frames)
        return result_df


    def send_slack(self, msg='crawling_done!!', channel="#james", username="bot" ):
        webhook_URL = "https://hooks.slack.com/services/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"
        # 페이로드 생성
        payload = {
            "channel": channel,
            "username": username,
            "icon_emoji": ":test:",
            "text": msg,
        }

        # 전송
        response = requests.post(
            webhook_URL,
            data = json.dumps(payload),
        )


    def df_to_sql(self, df):
        db = MySQLdb.connect(
            "54.180.116.159", # IP (Mysql 서버)
            "root", # Mysql 사용자 계정
            "1234", # password inits
            "world", # 데이터 베이스 이름
            charset='utf8'# 문자 인코딩 방식
        )
        engine = create_engine("mysql://root:1234@54.180.116.159/world?charset=utf8")
        df.to_sql(name="movie", con=engine, if_exists="append")
        db.commit()

    def main(self):
        df = self.movie_crawling()
        self.df_to_sql(df)
        self.send_slack()
        return df



movie = movie_crawling()
movie.main()
