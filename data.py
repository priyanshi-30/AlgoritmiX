import pandas as pd
import random
from datetime import datetime, timedelta

areas = [
"MG Road","Baner","Wakad","Shivaji Nagar","Kothrud","Hinjewadi",
"Aundh","Pimpri","Chinchwad","Viman Nagar","Hadapsar","Kharadi",
"Yerwada","Camp","Pashan"
]

street_light = ["good","moderate","poor"]
crowd = ["low","medium","high"]
crime_levels = ["low","medium","high"]
crime_types = ["none","theft","harassment","robbery","snatching"]

rows = []
start_time = datetime(2026,1,1)

for i in range(10000):

    area = random.choice(areas)
    latitude = round(random.uniform(18.45,18.65),6)
    longitude = round(random.uniform(73.70,73.95),6)

    light = random.choice(street_light)
    crowd_level = random.choice(crowd)
    crime = random.choice(crime_levels)

    nearby_shop = random.choice([True,False])
    open_businesses = random.randint(0,40)
    crime_reports = random.randint(0,8)

    crime_type = random.choice(crime_types)

    timestamp = start_time + timedelta(minutes=random.randint(0,500000))

    score = 100

    if light == "poor":
        score -= 20
    elif light == "moderate":
        score -= 10

    if crowd_level == "low":
        score -= 15

    if crime == "high":
        score -= 30
    elif crime == "medium":
        score -= 15

    score -= crime_reports * 3

    if not nearby_shop:
        score -= 8

    score = max(0,score)

    rows.append([
        area,"Pune",latitude,longitude,light,crowd_level,crime,
        nearby_shop,open_businesses,crime_reports,crime_type,
        timestamp.strftime("%Y-%m-%d %H:%M"),score
    ])

columns = [
"area_name","city","latitude","longitude","street_light","crowd",
"crime_area","nearby_shop","open_businesses","recent_crime_reports",
"crime_type","timestamp","safety_score"
]

df = pd.DataFrame(rows,columns=columns)

df.to_csv("safety_ai_dataset_10000_rows.csv",index=False)

print("Dataset created successfully!")