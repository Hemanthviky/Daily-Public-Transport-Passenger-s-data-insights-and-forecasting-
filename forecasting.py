import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error


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


# Function to forecast, plot, and provide detailed explanations
def forecast_and_plot(data, service_name):
    # Split the data into training (all but last 7 days) and testing (last 7 days)
    train = data[service_name].iloc[:-7]
    test = data[service_name].iloc[-7:]
    
    # Fit SARIMA model
    model = SARIMAX(train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 7))
    model_fit = model.fit(disp=False)
    
    # Forecast for the next 7 days
    forecast = model_fit.forecast(steps=7)
    
    # Calculate Root Mean Square Error (RMSE)
    error = np.sqrt(mean_squared_error(test, forecast))
    
    # Create a plot comparing actual and forecast
    plt.figure(figsize=(10, 6))
    plt.plot(train.index[-14:], train[-14:], label="Training Data", color="blue")
    plt.plot(test.index, test, label="Actual (Last 7 Days)", color="orange")
    plt.plot(forecast.index, forecast, label="Forecast (Next 7 Days)", linestyle='--', color="green")
    plt.title(f"Actual vs Forecast for {service_name}")
    plt.xlabel("Date")
    plt.ylabel("Number of Passengers")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()
    
    # Detailed Explanation and Forecast Values
    print(f"\nInsight: Forecasting for {service_name}")
    print(f"RMSE (Root Mean Square Error): {error:.2f}")
    print("The graph above compares actual passenger data from the last 7 days with the forecasted values for the next 7 days. "
          "The solid orange line represents the actual data, while the green dashed line shows the forecast. "
          "The goal is to observe how well the forecast aligns with actual patterns. A lower RMSE indicates better performance.")
    
    print("\nForecasted Values for the Next 7 Days:")
    forecast_df = pd.DataFrame({
        "Date": forecast.index,
        "Forecasted Passengers": forecast.values
    })
    print(forecast_df)
    
    return forecast

# Apply the function to each service type and visualize results
for service in ['Local Route', 'Light Rail', 'Peak Service', 'Rapid Route', 'School']:
    forecast_and_plot(data, service)


