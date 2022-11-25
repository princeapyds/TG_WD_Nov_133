import seaborn as sns
tip = sns.load_dataset('tips')
tip.info()
tip = sns.pointplot(x='time',y='total_bill',data=tip)