# NASA Space Apps
This is a web-app project made by team Cypher that participated in the 2023 NASA SpaceApps Challenges

# Introduction:
The provided codebase consists of three components aimed at facilitating the assessment of weather conditions for potential rocket launches. The Python script interacts with the OpenWeatherMap API to retrieve weather data for a specified city and assesses whether the conditions are suitable for a launch. On the other hand, the HTML files serve as user interfaces for viewing weather information and launch suitability on both a textual interface and an interactive world map.
# Modules
Requests
Matplotlib
Pandas
datetime
time

# Functions:
1. get_weather_data(city) : 
Fetches weather data from the OpenWeatherMap API for the specified city. 
Returns the weather data as a JSON object or None if there is an error.

Parameters: city (str): The name of the city to fetch weather data for.
Returns: Dictionary containing weather data or None in case of error.

2.  printer(weather_data) : 
Prints a structured report of weather conditions in a tabular format. 
Highlights key weather attributes such as temperature, cloud cover, wind speed, weather 
description, and lightning risk. 
Uses color-coded output to indicate suitability.

Parameters: weather_data (dict): The weather data to display.

3. is_suitable_for_rocket_launch(weather_data)
Determines whether the weather conditions are suitable for a rocket launch based on 
defined criteria, including temperature range, cloud cover percentage, wind speed, and weather description.

Parameters: weather_data (dict): The weather data to analyze.
Returns: Boolean value indicating suitability for rocket launch.

4. get_suitable_time(current_time)
Suggests the next suitable time for a rocket launch if the current 
conditions are not ideal. In this example, it assumes the conditions 
may improve in 15 minutes.

Parameters: current_time (datetime): The current time.
Returns: datetime indicating the next suggested suitable time.

5. 5. main()
Main function of the program. Asks the user for a city name and fetches the current weather data. 
It then displays the weather conditions and evaluates suitability for a rocket launch. 
If the conditions are not ideal, it suggests the next suitable time. The user is asked if they 
want to continue with further analysis and plotting. If agreed, the program collects weather data every 
10sec(any time) for five iterations and plots the weather factors over time.


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
