import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

# Load the dataset
file_path = "Daily_Public_Transport_Passenger_Journeys_by_Service_Type_20241028.csv"
data = pd.read_csv(file_path)

# Convert 'Date' column to datetime format and set as index
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
data.set_index('Date', inplace=True)

# Fill missing values in 'Other' with the median
data['Other'].fillna(data['Other'].median(), inplace=True)

# Aggregate data by day to handle any duplicate dates
data = data.resample('D').sum()

##Insights# Function to provide and explain insights
def display_insights(data):
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    # 1. Overall Passenger Distribution
    service_columns = ['Local Route', 'Light Rail', 'Peak Service', 'Rapid Route', 'School', 'Other']
    total_passengers = data[service_columns].sum().sort_values(ascending=False)
    # Explanation
    print("\nInsight 1: Overall Passenger Distribution")
    print("The total number of passengers for each service type has been visualized. "
          "It can be observed that 'Rapid Route' services have the highest total passenger count, "
          "indicating it is the most popular service type. Services like 'School' and 'Other' "
          "have significantly lower usage. This insight can help in understanding which services "
          "need more resources or attention.")
    print(total_passengers)
    
    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=total_passengers.index, y=total_passengers.values, palette="viridis")
    plt.title("Total Passengers by Service Type")
    plt.ylabel("Total Number of Passengers")
    plt.xticks(rotation=45)
    plt.show()
    
    
    #2. Descriptive Statistics for Each Service Type
    summary_stats = data[service_columns].describe().T
    print("\nInsight 2: Descriptive Statistics")
    print("The table below shows key statistics (mean, min, max) for each service type, "
          "giving a clear view of average usage and variability. This can be useful to identify "
          "patterns and outliers in daily passenger counts across different services.")
    print(summary_stats[['mean', 'min', 'max']])
    

    plt.figure(figsize=(12, 8))
    for col in service_columns:
        sns.lineplot(x=data.index, y=data[col], label=col)
    plt.title("Passenger Trends Over Time by Service Type")
    plt.xlabel("Date")
    plt.ylabel("Number of Passengers")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()      

    # 3. Correlation Between Service Types
    print("\nInsight 3: Correlation Between Service Types")
    print("The correlation matrix shows relationships between different service types. High correlations could "
          "indicate that certain services are used interchangeably or are affected by similar factors. For example, "
          "'Local Route' and 'Peak Service' might have a high correlation, suggesting they serve overlapping commuter needs.")
    correlation_matrix = data[service_columns].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix Between Service Types")
    plt.show()
    
    
    # 4. Outlier Detection
    outliers = summary_stats[summary_stats['max'] > (summary_stats['mean'] + 3 * summary_stats['std'])]
    print("\nInsight 4: Outlier Detection")
    print("Outliers have been identified based on passenger counts exceeding three standard deviations from the mean.")
    print("These outliers may indicate unusual events, such as special events or disruptions, that caused significant "
          "deviations from normal service usage.")
    print(outliers[['mean', 'max', 'std']])

# Call the function to display insights
display_insights(data)



