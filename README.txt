# NASA_space_apps
This is a web-app project made by team Cypher that participated in the 2023 NASA SpaceApps Challenges

# Introduction:
This Python script utilizes the OpenWeatherMap API to fetch real-time weather data for a specified city. It assesses various weather parameters including temperature, cloud cover, wind speed, and lightning risk to determine whether conditions are suitable for a student rocket launch. The script provides insights into current weather conditions and informs users about the feasibility of conducting a rocket launch based on the analyzed data.

# Functions:

get_weather_data(city)

1. Description: Retrieves weather data for a specified city from the OpenWeatherMap API.
Parameters:
city (str): Name of the city for which weather data is requested.
Returns:
Weather data in JSON format if the request is successful.
printer(weather_data)

2. Description: Prints the weather data in a formatted table.
Parameters:
weather_data (dict): Weather data obtained from the OpenWeatherMap API.
is_suitable_for_rocket_launch(weather_data)

3. Description: Determines if weather conditions are suitable for a rocket launch based on the provided data.
Parameters:
weather_data (dict): Weather data obtained from the OpenWeatherMap API.
Returns:
True if conditions are suitable for a rocket launch, otherwise False.

4. main()
Description: Main function to execute the script. Prompts the user for a city name, retrieves weather data, and checks if conditions are suitable for a rocket launch.

# WEB PLATFORM
1. The HTML document presents a web-based tool for checking weather conditions suitable for a rocket launch. Here's an overview of its components:

2. Particle Animation Background:

Utilizes the Particle JS library to create an animated background resembling space particles.
Main Content Container:

Contains the user interface elements and displays weather-related information.
City Input and Button:

Allows users to input the name of a city and fetch weather data for that location.
Error Message Display:

Displays error messages if there are any issues fetching weather data.
Weather Conditions Table:

Presents a table showing various weather parameters such as temperature, cloud cover, wind speed, and sky condition.
Launch Suitability Message:

Indicates whether weather conditions are suitable for a rocket launch based on the analyzed data.
Next Launch Time Display:

Shows the estimated next suitable launch time, calculated as one hour from the current time.
Best Launch Time Display:

Provides information on the best launch time for the next four days, based on simulated weather scores.
JavaScript Code:

Handles fetching weather data, updating the UI with weather information, and controlling the particle animation.
This HTML file serves as the frontend component of the rocket launch weather checking tool, offering a user-friendly interface for accessing and analyzing weather data.

# Group Memebers
1> Deep Sangani
2> Dhyey Savaliya
3> Harsh Dhimmar
4> Saurav Sawant
5> Harsh Patel
6> Miqdad Ali











