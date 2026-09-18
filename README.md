# Weather_API_chatbot
AI Weather Assistant
Project Overview

AI Weather Assistant is a Streamlit-based chatbot that provides real-time weather information for a city entered by the user. The application uses the Open-Meteo API to retrieve weather data and displays the results through a simple and interactive chat interface.

The application provides important weather details such as:

Temperature
Humidity
Wind Speed
Location
Features
Interactive chatbot interface
Search weather by city name
Real-time weather information
Temperature displayed in Celsius
Humidity percentage
Wind speed in km/h
Dark-themed user interface
Weather details displayed in separate sections
Uses Open-Meteo API
No API key required
Technologies Used
Python
Streamlit
Requests
Open-Meteo Weather API
Regular Expressions
Project Structure
AI-Weather-Assistant/
│
├── app.py
│
└── requirements.txt
How It Works

The user enters a weather-related question such as:

What is the temperature in Chennai?

The application extracts the city name from the question and sends a request to the Open-Meteo Geocoding API.

The location coordinates are then used to request current weather information from the Open-Meteo Weather API.

The retrieved information is displayed in the chatbot along with:

Temperature
Humidity
Wind Speed
Location
Example

User:

What is the temperature in Chennai?

Assistant:

The current temperature in Chennai, India is 30.5°C.
The humidity is 75%, and the wind speed is 11.0 km/h.

The application also displays the weather information in a separate Weather Details section.

Installation

Install the required Python libraries:

python -m pip install streamlit requests
Run the Application

Open the project folder in VS Code and run:

python -m streamlit run app.py

The application will open in your web browser.

API

This project uses Open-Meteo, a weather API that provides weather information without requiring an API key.

## Screenshot
<img width="632" height="413" alt="Screenshot 2026-09-16 223819" src="https://github.com/user-attachments/assets/474c7338-92d4-4f1c-937d-40b22b55f8f8" />

<img width="641" height="246" alt="Screenshot 2026-09-16 223832" src="https://github.com/user-attachments/assets/42cecebb-5ea6-4fc2-b89e-e24f82d02558" />



The application uses:

Open-Meteo Geocoding API to find city coordinates
Open-Meteo Forecast API to retrieve current weather data
Future Enhancements
Weather forecast for upcoming days
Rain prediction
Weather icons
Multiple language support
Voice-based weather queries
LLM-based natural language understanding
Weather charts and visualizations
Temperature unit selection
Conclusion

AI Weather Assistant provides a simple way to interact with weather information through a chatbot interface. It demonstrates the use of Python, Streamlit, API integration, and basic natural language processing in a practical application
