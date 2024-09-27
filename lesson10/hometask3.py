import pandas as pd
import seaborn as sns
import matplotlob.pyplot as plt

df = pd.read_csv('data,csv')

sns.scatterplot(x='salary', y='bonus', size='years_at_company', data=df)

plt.title('Salary vs Bonus with Years at Company')

plt.xlabel('Salary')
plt.ylabel('Bonus')

plt.show()
