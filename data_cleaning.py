import pandas as pd
df_GME=pd.read_csv("GME_data.csv")
df_GME_revenue=pd.read_csv("GameStop_revenue.csv")
df_Tesla=pd.read_csv("Tesla_data.csv")
df_Tesla_revenue=pd.read_csv("Tesla_revenue.csv")

df_GME_revenue['Date']=pd.to_datetime(df_GME_revenue['Date'],utc=True)
df_GME['Date']=pd.to_datetime(df_GME['Date'],utc=True)
df_Tesla_revenue['Date']=pd.to_datetime(df_Tesla_revenue['Date'],utc=True)
df_Tesla['Date']=pd.to_datetime(df_Tesla['Date'],utc=True)

df_Tesla_revenue["Revenue"]=df_Tesla_revenue['Revenue'].str.replace('$','').str.replace(',','')
df_Tesla_revenue['Revenue']=pd.to_numeric(df_Tesla_revenue['Revenue'])

df_GME_revenue['Revenue']=df_GME_revenue['Revenue'].str.replace('$','').str.replace(',','')
df_GME_revenue['Revenue']=pd.to_numeric(df_GME_revenue['Revenue'])



print(df_Tesla_revenue.info())
print(df_GME_revenue.info())


'''tesla_merged = pd.merge_asof(
    df_Tesla.sort_values('Date'),
    df_Tesla_revenue.sort_values('Date'),
    on='Date',
    direction='backward'
    )

gme_merged=pd.merge_asof(
    df_GME.sort_values('Date'),
    df_GME_revenue.sort_values('Date'),
    on='Date',
    direction="backward"
)

tesla_merged.to_csv("Tesla_merged.csv",index=False)
gme_merged.to_csv("gme_merged.csv",index=False)



# Load your merged Tesla and GME data
tesla_df = pd.read_csv("tesla_merged.csv")
gme_df = pd.read_csv("gme_merged.csv")

# Add company identifier
tesla_df["Company"] = "Tesla"
gme_df["Company"] = "GameStop"

# Concatenate both
combined_df = pd.concat([tesla_df, gme_df], ignore_index=True)

# Save to new CSV
combined_df.to_csv("combined_stock_data.csv", index=False)'''


