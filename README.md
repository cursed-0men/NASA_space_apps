# NASA_space_apps
This is a web-app project made by team Cypher that participated in the 2023 NASA SpaceApps Challenges

# Introduction:
The provided codebase consists of three components aimed at facilitating the assessment of weather conditions for potential rocket launches. The Python script interacts with the OpenWeatherMap API to retrieve weather data for a specified city and assesses whether the conditions are suitable for a launch. On the other hand, the HTML files serve as user interfaces for viewing weather information and launch suitability on both a textual interface and an interactive world map.

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
HTML Code 1 :
Purpose: The HTML code provides user interfaces for inputting a city name and displaying weather information relevant to rocket launches.
Components:
Input Field: Allows users to enter the name of the city.
Weather Information: Displays temperature, cloud cover, wind speed, sky condition, and lightning risk.
Launch Suitability Message: Indicates whether conditions are suitable for a rocket launch.
Next Launch Time: Displays the expected suitable launch time.
Best Launch Time: Shows the best launch time for the next 4 days.
Styling with CSS: Enhances the visual appearance and layout of the interface.

HTML Code 2 :
Purpose: The HTML code creates an interactive world map where users can select cities to view weather forecasts and assess launch suitability.
Components:
Leaflet Map: Displays a world map allowing users to click on cities.
Weather Forecast Display: Shows detailed weather forecast information for selected cities.
Custom Markers: Indicates launch suitability with custom markers on the map.
Weather Forecast Table: Presents a table with detailed weather forecast data.
Styling with CSS: Enhances the visual appearance and layout of the map and weather information.

# Resources
1. OpenWeatherMap API: Provides real-time weather data for cities worldwide.
2. Leaflet.js Library: Enables the creation of interactive and customizable maps in web applications.
3. API Key: Required for authentication and access to OpenWeatherMap API services.

# Group Members
1> Deep Sangani
2> Dhyey Savaliya
3> Harsh Dhimmar
4> Saurav Sawant
5> Harsh Patel
6> Miqdad Ali











