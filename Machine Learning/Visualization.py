import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df1 = pd.read_csv('C:/Users/Arjun/Downloads/Dataset/Medical/Symptom.csv')
df2 = pd.read_csv('C:/Users/Arjun/Downloads/Dataset/Medical/Symptom Description.csv')
df3 = pd.read_csv('C:/Users/Arjun/Downloads/Dataset/Medical/Symptom Precaution.csv')
df4 = pd.read_csv('C:/Users/Arjun/Downloads/Dataset/Medical/Symptom Severity.csv')

sns.set()
vis1 = plt.hist(df4["weight"], color=sns.color_palette()[8])
plt.xlabel("Severity")
plt.ylabel("Count")
plt.show()

symptom = df1["Symptom_12"].value_counts()
vis2 = plt.pie(symptom, labels=symptom.index, startangle=100, counterclock=False)
plt.title("Symptom 12")
plt.show()

col = ['greenyellow', 'orchid', 'burlywood', 'salmon']
symptom = df1["Symptom_14"].value_counts()
vis3 = plt.pie(symptom, labels=symptom.index, startangle=90,
               counterclock=False, wedgeprops={'width': 0.4}, colors=col)
plt.title("Symptom 14")
plt.show()
