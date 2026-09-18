# AI Weather Assistant

## Overview

AI Weather Assistant is a Streamlit-based weather chatbot that provides real-time weather information for different cities.

Users can enter a natural language weather query, and the application extracts the city name and retrieves current weather information using the Open-Meteo API.

## Features

- Interactive chatbot interface
- Search weather by city name
- Real-time weather information
- Temperature in Celsius
- Humidity information
- Wind speed information
- Location details
- Simple and user-friendly interface
- Dark-themed UI
- No API key required

## Technologies Used

- Python
- Streamlit
- Requests
- Open-Meteo API
- Regular Expressions

## How It Works

The application follows these steps:

1. The user enters a weather-related question.
2. The application identifies the city name from the question.
3. The Open-Meteo Geocoding API finds the location coordinates.
4. The Open-Meteo Weather API retrieves the current weather information.
5. The chatbot displays the weather details to the user.
6. The weather information is also displayed in the Weather Details section.

## Screenshot
<img width="632" height="413" alt="Screenshot 2026-09-16 223819" src="https://github.com/user-attachments/assets/be4bf484-2fd2-4373-891f-97239ea24a95" />

<img width="641" height="246" alt="Screenshot 2026-09-16 223832" src="https://github.com/user-attachments/assets/b55975d6-855b-4901-bd00-481792b92b43" />



## Example

User Query:

    What is the temperature in Chennai?

Chatbot Response:

    The current temperature in Chennai, India is 30.5°C.
    The humidity is 75%, and the wind speed is 11.0 km/h.

## Weather Details

The application displays:

- Temperature
- Humidity
- Wind Speed
- Location

## Project Structure

    AI-Weather-Assistant/
    │
    ├── app.py
    ├── requirements.txt
    └── README.md

## Installation

Clone the repository:

    git clone YOUR_GITHUB_REPOSITORY_URL

Move into the project folder:

    cd AI-Weather-Assistant

Install the required packages:

    python -m pip install -r requirements.txt

## Run the Application

Run the Streamlit application using:

    python -m streamlit run app.py

The application will open in the web browser.

## API

This project uses the Open-Meteo API to retrieve weather information.

The application uses the Open-Meteo Geocoding API to find the coordinates of a city and the Open-Meteo Forecast API to retrieve current weather data.

No API key is required for this project.

## Future Enhancements

- Weather forecast for upcoming days
- Rain prediction
- Weather icons
- Weather charts
- Voice-based weather queries
- Multiple language support
- LLM-based natural language understanding
- Location-based weather detection

## Conclusion

AI Weather Assistant demonstrates how Python, Streamlit, API integration, and natural language processing can be combined to create an interactive weather chatbot.
