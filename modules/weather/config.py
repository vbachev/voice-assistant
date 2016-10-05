buttonLabel = 'What\'s the weather?'

# weather API URL and credentials
apiURL = 'http://api.openweathermap.org/data/2.5/weather?APPID=229d854fb2e86c3fd138f93cc0d4b77a&type=like&q='

kelvin = 273.15 # temp measurement is provided in Kelvin so we need to subtract 273.15
location = 'Sofia'

temperatureMessage = 'Temperature in {0} is {1} degrees celsius.'
humidityMessage = 'Humidity is {0} percent.'
errorMessage = 'Sorry! No weather data available due to network error.'