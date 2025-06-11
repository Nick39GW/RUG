import streamlit as st
import requests

# Title and description
st.title("People in Space Right Now")
st.markdown("This app shows how many people are currently in space and who they are, using data from Open Notify API.")

# Fetch astronaut data
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
data = response.json()

# Display total number and names
st.subheader(f"Total Astronauts in Space: {data['number']}")
names = [person["name"] for person in data["people"]]
st.write("### Names of Astronauts:")
st.write(names)



st.title("Current Location of the ISS")
st.markdown("The map below shows the real-time location of the International Space Station.")

# Fetch ISS location
iss_url = "http://api.open-notify.org/iss-now.json"
iss_response = requests.get(iss_url)
iss_data = iss_response.json()

# Get coordinates
lat = float(iss_data["iss_position"]["latitude"])
lon = float(iss_data["iss_position"]["longitude"])

# Create DataFrame for the map
import pandas as pd
location_df = pd.DataFrame({"latitude": [lat], "longitude": [lon]})

# Show map
st.map(location_df)
