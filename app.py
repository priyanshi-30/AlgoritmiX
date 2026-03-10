import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
import random
import speech_recognition as sr

st.set_page_config(page_title="AI Safety Route App", layout="wide")

st.title("🛡 AI Personal Safety & Route Finder")

# OpenStreetMap Geocoder
geolocator = Nominatim(user_agent="safety_app")

# Sidebar navigation
st.sidebar.title("Navigation")
menu = st.sidebar.selectbox(
    "Select Feature",
    ["Safest Route Finder", "Voice Distress Detection"]
)

# Session state (prevents blinking)
if "route_data" not in st.session_state:
    st.session_state.route_data = None


# ==============================
# SAFETY SCORE (WEIGHTAGE MODEL)
# ==============================

def calculate_safety():

    crime_rate = random.randint(1,10)
    lighting = random.randint(1,10)
    activity = random.randint(1,10)

    score = (lighting*0.35) + ((10-crime_rate)*0.40) + (activity*0.25)

    return round(score,2), crime_rate, lighting, activity


# ==============================
# SAFEST ROUTE FINDER
# ==============================

if menu == "Safest Route Finder":

    st.header("🗺 Find Safest Route")

    source = st.text_input("Enter Source Area")
    destination = st.text_input("Enter Destination Area")

    if st.button("Find Route"):

        with st.spinner("Finding location..."):

            try:

                # Add India for better search accuracy
                src = geolocator.geocode(source + ", India", timeout=10)
                dst = geolocator.geocode(destination + ", India", timeout=10)

                if src is None:
                    st.error("Source location not found. Try adding city name.")
                    st.stop()

                if dst is None:
                    st.error("Destination location not found. Try adding city name.")
                    st.stop()

                start_lat = src.latitude
                start_lon = src.longitude

                dest_lat = dst.latitude
                dest_lon = dst.longitude

                safety_score, crime, light, activity = calculate_safety()

                st.session_state.route_data = {
                    "start":[start_lat,start_lon],
                    "end":[dest_lat,dest_lon],
                    "score":safety_score,
                    "crime":crime,
                    "light":light,
                    "activity":activity
                }

            except Exception as e:
                st.error("Error finding location")
                st.write(e)


# ==============================
# DISPLAY MAP AND RESULT
# ==============================

if st.session_state.route_data:

    data = st.session_state.route_data

    st.subheader(f"Safety Score: {data['score']} / 10")

    if data["score"] > 7:
        st.success("Safe Route")
    elif data["score"] > 4:
        st.warning("Moderate Risk")
    else:
        st.error("Unsafe Route")

    # Create map
    m = folium.Map(location=data["start"], zoom_start=13)

    # Source marker
    folium.Marker(
        data["start"],
        tooltip="Source",
        icon=folium.Icon(color="green")
    ).add_to(m)

    # Destination marker
    folium.Marker(
        data["end"],
        tooltip="Destination",
        icon=folium.Icon(color="red")
    ).add_to(m)

    # Route line
    folium.PolyLine(
        [data["start"], data["end"]],
        color="blue",
        weight=5
    ).add_to(m)

    st_folium(m, width=900, height=500)

    st.write("### Safety Factors")
    st.write("Crime Rate:", data["crime"])
    st.write("Street Lighting:", data["light"])
    st.write("Area Activity:", data["activity"])


# ==============================
# VOICE DISTRESS DETECTION
# ==============================

if menu == "Voice Distress Detection":

    st.header("🎤 Voice Distress Detection")

    st.write("Say words like **help**, **save me**, or **emergency**")

    if st.button("Start Listening"):

        recognizer = sr.Recognizer()

        try:

            with sr.Microphone() as source:

                st.info("Listening...")
                audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio)

            st.write("Detected Speech:", text)

            if "help" in text.lower() or "save me" in text.lower() or "emergency" in text.lower():

                st.error("🚨 DISTRESS DETECTED")
                st.write("SOS Alert Triggered")

            else:
                st.success("No distress detected")

        except:
            st.warning("Could not recognize speech")