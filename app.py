import streamlit as st
import requests
import re

st.set_page_config(
    page_title="Weather Chatbot",
    layout="centered"
)

st.markdown("""
<style>

.main-title {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 25px;
}

.weather-box {
    background-color: #191d24;
    padding: 25px;
    border-radius: 14px;
    margin-top: 25px;
    border: 1px solid #262b35;
}

.weather-title {
    font-size: 30px;
    font-weight: 600;
    margin-bottom: 25px;
}

.metric-box {
    background-color: #191d24;
    padding: 15px;
    border-radius: 12px;
}

.metric-label {
    font-size: 16px;
    color: #dddddd;
}

.metric-value {
    font-size: 34px;
    font-weight: 500;
    margin-top: 8px;
}

.location-text {
    color: #aaaaaa;
    font-size: 16px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">AI Weather Assistant</div>',
    unsafe_allow_html=True
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "weather_data" not in st.session_state:
    st.session_state.weather_data = None

def extract_city(text):

    text = text.strip()

    patterns = [
        r"temperature in (.+)",
        r"weather in (.+)",
        r"weather of (.+)",
        r"weather at (.+)",
        r"forecast for (.+)",
        r"temperature at (.+)",
        r"temperature of (.+)",
        r"how hot is (.+)",
        r"what is the weather in (.+)",
        r"what is the temperature in (.+)"
    ]

    text_lower = text.lower()

    for pattern in patterns:

        match = re.search(pattern, text_lower)

        if match:

            city = match.group(1)

            city = city.strip(" ?.,!")

            return city

    return None

def get_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        return None

    data = response.json()

    if "results" not in data:
        return None

    result = data["results"][0]

    return {
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "city": result["name"],
        "country": result.get("country", "")
    }

def get_weather(city):

    location = get_coordinates(city)

    if location is None:
        return None

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "auto"
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        return None

    data = response.json()

    current = data["current"]

    return {
        "city": location["city"],
        "country": location["country"],
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"]
    }

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

user_input = st.chat_input(
    "Ask about the weather..."
)


if user_input:

    # Add user message

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    city = extract_city(user_input)

    if city is None:

        answer = (
            "Please mention a city name. "
            "For example: What is the temperature in Chennai?"
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        with st.chat_message("assistant"):
            st.write(answer)

    else:

        weather = get_weather(city)

        if weather is None:

            answer = f"Sorry, I couldn't find the city: {city}"

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

            with st.chat_message("assistant"):
                st.write(answer)

        else:

            answer = (
                f"The current temperature in "
                f"{weather['city']}, {weather['country']} is "
                f"{weather['temperature']}°C. "
                f"The humidity is {weather['humidity']}%, "
                f"and the wind speed is "
                f"{weather['wind_speed']} km/h."
            )

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

            with st.chat_message("assistant"):
                st.write(answer)

            st.session_state.weather_data = weather

if st.session_state.weather_data:

    weather = st.session_state.weather_data

    st.markdown("---")

    st.markdown(
        '<div class="weather-title"> Weather Details</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-label">Temperature</div>
                <div class="metric-value">
                    {weather['temperature']}°C
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-label">Humidity</div>
                <div class="metric-value">
                    {weather['humidity']}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-label">Wind Speed</div>
                <div class="metric-value">
                    {weather['wind_speed']} km/h
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div class="location-text">
             Location: {weather['city']}, {weather['country']}
        </div>
        """,
        unsafe_allow_html=True
    )