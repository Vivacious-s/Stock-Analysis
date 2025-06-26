import requests
from bs4 import BeautifulSoup
import pandas as pd
def revenue_from_web(url,company):
    headers = {"User-Agent": "Mozilla/5.0"}
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')
    tables=soup.find_all('table')
    revenue_data=[]
    for table in tables:
        if f"{company} Quarterly Revenue" in table.text:
            rows=table.find_all("tr")
            for row in rows:
                cols=row.find_all('td')
                if len(cols)==2:
                    date=cols[0].text.strip()
                    revenue=cols[1].text.strip().replace(",","")
                    revenue_data.append((date,revenue))
                    df=pd.DataFrame(revenue_data,columns=["Date","Revenue"])
                    df.to_csv(f"{company}_revenue.csv",index=False)

revenue_from_web("https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue","GameStop")
revenue_from_web("https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue","Tesla")

