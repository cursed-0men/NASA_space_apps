import requests
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import time


api_key = 'API-KEY'

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data")
        return None


def printer(weather_data):
    """Structured report of weather conditions"""
    temperature = weather_data['main']['temp']  # in degrees Celsius
    cloud_cover = weather_data['clouds']['all']  # cloud cover percentage
    wind_speed = weather_data['wind']['speed']  # wind speed in m/s
    description = weather_data['weather'][0]['description']  # weather description
    lightning_risk = "thunderstorm" in description.lower()

    print("Weather Conditions")
    print("=" * 50)
    print(f"{'Condition':<20} | {'Normal'} | {'Live Condition'}")
    print("-" * 50)

    # Temperature
    expected_temp = "273.15 to 313.15 °C"
    temperature_status = f"{temperature:.2f} °C"
    temp_color = "\033[92m" if 273.15 < temperature < 313.15 else "\033[91m"
    print(f"{'Temperature':<20} | {expected_temp} | {temp_color}{temperature_status}\033[0m")

    # Cloud Cover
    expected_cloud = "<10%"
    cloud_color = "\033[92m" if cloud_cover < 10 else "\033[91m"
    print(f"{'Cloud Cover':<20} | {expected_cloud} | {cloud_color}{cloud_cover:.2f}%\033[0m")

    # Wind Speed
    expected_wind = "<9 m/s"
    wind_color = "\033[92m" if wind_speed < 9.0 else "\033[91m"
    print(f"{'Wind Speed':<20} | {expected_wind} | {wind_color}{wind_speed:.2f} m/s\033[0m")

    # Description (for clear sky)
    expected_description = "Clear Sky"
    skies = "rain" not in description.lower() and "drizzle" not in description.lower()
    desc_color = "\033[92m" if skies else "\033[91m"
    print(f"{'Description':<20} | {expected_description} | {desc_color}{description.title()}\033[0m")

    # Lightning Risk
    expected_lightning = "No Risk"
    storm = "thunderstorm" in description.lower()
    lightning_color = "\033[91m" if storm else "\033[92m"
    lightning_status = "True" if storm else "False"
    print(f"{'Lightning Risk':<20} | {expected_lightning} | {lightning_color}{lightning_status}\033[0m")
    print("=" * 50)


def is_suitable_for_rocket_launch(weather_data):
    """Determining if weather conditions are suitable for a rocket launch."""
    temperature = weather_data['main']['temp']  # in degrees Celsius
    cloud_cover = weather_data['clouds']['all']  # cloud cover percentage
    wind_speed = weather_data['wind']['speed']  # wind speed in m/s
    description = weather_data['weather'][0]['description']  # weather description
    lightning_risk = "thunderstorm" in description.lower()

    clear_skies = cloud_cover < 10
    low_wind_speed = wind_speed < 9.0
    moderate_temperature = 273.15 < temperature < 313.15
    dry_weather = "rain" not in description.lower()
    low_lightning_risk = not lightning_risk

    return (
        clear_skies and
        low_wind_speed and
        moderate_temperature and
        dry_weather and
        low_lightning_risk
    )


def get_suitable_time(current_time):
    """Suggesting the next suitable time for a rocket launch if current conditions are not ideal."""
    suitable_time = current_time + timedelta(minutes=15)  # Example: assume conditions improve in 15 minutes
    return suitable_time


def main():
    city = input("Enter city name: ")
    weather_data = get_weather_data(city)
    current_time = datetime.now()

    # Displaying the current weather conditions
    if weather_data:
        printer(weather_data)

        # Determine if it's suitable for a rocket launch
        if is_suitable_for_rocket_launch(weather_data):
            print("\033[92mIdeal conditions for a student rocket launch!\033[0m")
        else:
            next_suitable_time = get_suitable_time(current_time)
            print("\033[91mNot ideal conditions for a student rocket launch.\033[0m")
            print(f"\033[92mSuggested next suitable time: {next_suitable_time.strftime('%Y-%m-%d, %H:%M:%S')}\033[0m")

        # Asking the user if they want to continue with further analysis and plotting
        choice = input("Would you like to perform further analysis and plot data over time? (yes/no): ")

        if choice.lower() == "yes":
            data_list = []

            # Collect weather data every 10 seconds, 5 times
            for _ in range(5):
                weather_data = get_weather_data(city)

                if weather_data:
                    temperature = weather_data['main']['temp']
                    cloud_cover = weather_data['clouds']['all']
                    wind_speed = weather_data['wind']['speed']
                    description = weather_data['weather'][0]['description']

                    rocket_launch_suitable = is_suitable_for_rocket_launch(weather_data)
                    current_time = datetime.now()

                    data_list.append({
                        'Time': current_time,
                        'Temperature': temperature,
                        'Cloud Cover': cloud_cover,
                        'Wind Speed': wind_speed,
                        'Description': description,
                        'Rocket Launch Suitable': rocket_launch_suitable,
                    })

                    # Display weather info and suitability during the loop
                    printer(weather_data)

                else:
                    print("Error fetching weather data.")

                # Wait 10 sec  before the next fetch
                time.sleep(10)

            # Plot the weather factors and rocket launch suitability over time
            df = pd.DataFrame(data_list)

            plt.figure(figsize=(10, 6))
            plt.plot(df['Time'], df['Temperature'], '-o', label='Temperature (°C)', color='orange')
            plt.plot(df['Time'], df['Cloud Cover'], '-o', label='Cloud Cover (%)', color='gray')
            plt.plot(df['Time'], df['Wind Speed'], '-o', label='Wind Speed (m/s)', color='blue')
            plt.plot(df['Time'], df['Rocket Launch Suitable'], '-o', label='Rocket Launch Suitable', color='green')

            plt.xlabel("Time")
            plt.ylabel("Weather Data")
            plt.title("Weather Conditions Over Time")
            plt.legend()
            plt.show()

        else:
            print("Exiting the program. Have a great day!")

    else:
        print("Error fetching weather data. Exiting.")


if __name__ == "__main__":
    main()
