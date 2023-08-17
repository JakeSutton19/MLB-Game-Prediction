#train.py



#Use to train model 



from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score

import pandas as pd 


#Read in file
print("Reading and cleaning data..")
file_string_1 = "data/TEAM_SEASONS/TOTAL_TEAM_SEASONS_2012-2022.csv"
df1 = pd.read_csv(file_string_1) 


df1["y-m-d"] = pd.to_datetime(df1["y-m-d"])
df1["opp_code"] = df1["Opp"].astype("category").cat.codes
df1["day_code"] = df1["y-m-d"].dt.dayofweek
df1["champ_lev_index"] = df1['champ_lev_index'].fillna('0')


print("Creating model..")
rf = RandomForestClassifier(n_estimators=500, min_samples_split=50, random_state=1)

train = df1[df1["y-m-d"] < '2022-01-01']
test = df1[df1["y-m-d"] > '2022-01-01']

predictors = ["opp_code", "is_day_game", "day_code","Rank", "champ_lev_index", "day_code"]

rf.fit(train[predictors], train["Outcome"])

preds = rf.predict(test[predictors])

error = accuracy_score(test["Outcome"], preds)


combined = pd.DataFrame(dict(actual=test["Outcome"], predicted=preds))

ct = pd.crosstab(index=combined["actual"], columns=combined["predicted"])

ps = precision_score(test["Outcome"], preds)

print(f"Model Resutls:")
print(f"---------------")
print(f"Error: {error}")
print(f"Precsion: {ps}\n")

print(ct)