import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("./UCB_psp_e4_20200111a_ADAPTEnsemble2pt5Rs.csv",index_col=0)
plt.scatter(df['lon'],df['lat'])
