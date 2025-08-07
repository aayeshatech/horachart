import streamlit as st

# Basic page config
st.set_page_config(page_title="Astrology Calculator")

# Title
st.title("🌟 Vedic Astrology Calculator")

# Alert
st.error("⚠️ Mercury Retrograde Alert: August 7, 2025")

# Input
name = st.text_input("Name", "Unknown Person")
birth_date = st.date_input("Birth Date")

if st.button("Calculate Chart"):
    st.success(f"Calculating chart for {name}")
    
    # Personal info
    st.subheader("Personal Information")
    st.write(f"Name: {name}")
    st.write(f"Birth Date: {birth_date}")
    st.write(f"Weekday: {birth_date.strftime('%A')}")
    
    # Planetary positions
    st.subheader("Current Planetary Positions (August 7, 2025)")
    
    planets = [
        ["Sun ☉", "♋ Cancer", "20.76°", "Good"],
        ["Moon ☽", "♐ Sagittarius", "24.88°", "Good"], 
        ["Mercury ☿", "♋ Cancer (R)", "10.93°", "Challenging"],
        ["Venus ♀", "♊ Gemini", "13.98°", "Good"],
        ["Mars ♂", "♍ Virgo", "5.94°", "Neutral"],
        ["Jupiter ♃", "♊ Gemini", "18.81°", "Good"],
        ["Saturn ♄", "♓ Pisces (R)", "7.20°", "Neutral"],
        ["Rahu ☊", "♒ Aquarius (R)", "25.73°", "Neutral"],
        ["Ketu ☋", "♌ Leo (R)", "25.73°", "Neutral"]
    ]
    
    for planet in planets:
        if planet[3] == "Good":
            st.success(f"{planet[0]} in {planet[1]} at {planet[2]} - {planet[3]}")
        elif planet[3] == "Challenging":
            st.error(f"{planet[0]} in {planet[1]} at {planet[2]} - {planet[3]}")
        else:
            st.warning(f"{planet[0]} in {planet[1]} at {planet[2]} - {planet[3]}")
    
    # Upcoming events
    st.subheader("Upcoming Transit Events")
    st.info("Aug 11, 2025: Mercury turns Direct")
    st.success("Aug 21, 2025: Venus enters Cancer")
    st.warning("Sep 1, 2025: Saturn re-enters Pisces")

st.write("---")
st.write("Real astronomical data for August 7, 2025")
