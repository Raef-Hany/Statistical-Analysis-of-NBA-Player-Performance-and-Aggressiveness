import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
df = pd.read_csv('nba_data.csv')

# Descriptive statistics
summary = df.describe()

# Visualizations
plt.figure(figsize=(10, 8))
sns.histplot(df['Age'], kde=True)
plt.title('Distribution of Player Ages')
plt.show()

plt.figure(figsize=(10, 8))
sns.histplot(df['PTS'], kde=True)
plt.title('Distribution of Points per Game')
plt.xlabel('Points per Game for each Player')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 8))
sns.histplot(df['Pos'], kde=True)
plt.title('Distribution of the Positions')
plt.xlabel('Positions')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 8))
sns.histplot(df['PF'], kde=True)
plt.title('Distribution of the fouls committed by each player')
plt.xlabel('Number of fouls')
plt.ylabel('Number of Players')
plt.show()

plt.figure(figsize=(10, 8))
sns.histplot(df['GS'], kde=True)
plt.title('Distribution of the player that starts the game')
plt.xlabel('number of games started')
plt.ylabel('Number of Players')
plt.show()