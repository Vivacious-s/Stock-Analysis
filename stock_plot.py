import matplotlib.pyplot as plt
import pandas as pd
df_tesla=pd.read_csv("Tesla_data.csv")
df_GME=pd.read_csv("GME_data.csv")

def plot_stock_data(df,title):
    plt.figure(figsize=(12,6))
    plt.plot(df['Close'])
    plt.fill_between(df.index, df['Close'], color='skyblue', alpha=0.5, label='Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price in USD')
    plt.title(f"{title} Closing Price Over Time")
    plt.legend()
    plt.tight_layout()
    plt.grid()
    plt.show()

plot_stock_data(df_tesla,"Tesla")
plot_stock_data(df_GME,"GameStop")