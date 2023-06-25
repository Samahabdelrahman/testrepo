!pip install yfinance==0.1.67
!mamba install bs4==4.10.0 -y

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

#Question1
Tesla = yf.Ticker('TSLA')
tesla_data = Tesla.history(period='max')
tesla_data.reset_index(inplace=True)
tesla_data.head(5)

#Question2
import requests
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(URL)
html_data = response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')

import pandas as pd
tesla_revenue = pd.DataFrame(columns=['Date', 'Revenue'])
for row in soup.find('tbody').find_all('tr'):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text
    
    tesla_revenue = tesla_revenue.append({"Date": date, "Revenue": revenue}, ignore_index=True)

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].replace(",", "").replace("$", "")

tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue.tail()

#Question3
GameStop = yf.Ticker("GME")
gme_data = GameStop.history(period='max')
gme_data.reset_index(inplace=True)
gme_data.head(5)

#Question4
import requests
URL = ' https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
response = requests.get(URL)
html_data = response.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')
import pandas as pd
gme_revenue = pd.DataFrame(columns=['Date', 'Revenue'])
for row in soup.find('tbody').find_all('tr'):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text
    gme_revenue = gme_revenue.append({'Date': date, "Revenue": revenue}, ignore_index=True)
gme_revenue["Revenue"] = gme_revenue["Revenue"].replace(",", "").replace("$", "")
gme_revenue.tail()

#Question5
make_graph(tesla_data, tesla_revenue, 'Tesla')

#Question6
make_graph(gme_data, gme_revenue, 'GameStop')
