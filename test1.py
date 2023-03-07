import json
import pandas as pd
import requests
import time

#Create Empty DataFrame To Append To
wine_cols = ['Winery','Wine','Rating','Review_Count','Region','SubRegion']
wine_df = pd.DataFrame(columns=wine_cols)

#Loop
for x in range(1,10):
    print("Started the attempt #", x)
    r = requests.get(
        "https://www.vivino.com/api/explore/explore",
        params = {
            "currency_code":"USD",
            "min_rating":"1",
            "order_by":"price",
            "order":"asc",
            "page": 4,
            "wine_type_ids[]":"1"
        },
        headers= {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
        }
    )
    print("Debugging the output:")
    # print(r.json())
    results = [
        (
        t["vintage"]["wine"]["winery"]["name"], 
        f'{t["vintage"]["wine"]["name"]} {t["vintage"]["year"]}',
        t["vintage"]["statistics"]["ratings_average"],
        t["vintage"]["statistics"]["ratings_count"],
        t["vintage"]["wine"]["region"]["country"]["name"],
        t["vintage"]["wine"]["region"]["name"]
        )
        for t in r.json()["explore_vintage"]["matches"]
    ]
    temp_df = pd.DataFrame(results,columns=wine_cols)
    wine_df = wine_df.append(temp_df, ignore_index=True)
    print("Shape of wine_df after the attempt #", x)
    print(wine_df.shape)
    print("Finished the attempt #", x)
