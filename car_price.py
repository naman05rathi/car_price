import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_excel("car.xls")
print df.shape
print df.head()
df['Model_cat'] = pd.Categorical(df.Model).codes
dfx = df[['Model_cat', 'Mileage', 'Doors']]
dfy = df[['Price']]

dfx1 = sm.add_constant(dfx)
estimate = sm.OLS(dfy, dfx1).fit()

print estimate.summary()
print dfy.groupby(df.Doors).mean()

fig, ax = plt.subplots()
fig = sm.graphics.plot_fit(estimate, 0, ax=ax)
ax.set_ylabel("Price")
ax.set_xlabel("Car")
ax.set_title("Linear Regression")
plt.show()