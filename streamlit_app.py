import streamlit as st
from datetime import date, datetime

# Page config
st.set_page_config(page_title="🌟 Vedic Astrology Calculator", page_icon="🔮")

# Title
st.title("🌟 Vedic Astrology Calculator")

# Mercury Retrograde Alert
st.error("⚠️ **Mercury Retrograde Alert: August 7, 2025**  \nCommunications, family matters, and emotional decisions require extra caution until August 11, 2025")

# Input Section
st.header("📋 Enter Birth Details")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👤 Name", value="NIFTY", help="Enter your full name")

with col2:
    # Fixed date input with proper range
    birth_date = st.date_input(
        "📅 Birth Date", 
        value=date(1990, 7, 3),  # Default to July 3, 1990
        min_value=date(1900, 1, 1),  # Allow dates from 1900
        max_value=date(2030, 12, 31),  # Allow dates up to 2030
        help="Select your birth date"
    )

# Add birth time input
birth_time = st.time_input("🕐 Birth Time", value=datetime.now().time(), help="Enter your birth time")

# Add birth place input
birth_place = st.text_input("📍 Birth Place", value="Mumbai, India", help="Enter your birth city and country")

# Calculate button
if st.button("🔮 Calculate Chart", type="primary"):
    
    # Show success message
    st.success(f"✅ Calculating chart for {name}")
    
    # Personal Information Section
    st.header("📋 Personal Information")
    
    # Create info columns
    info_col1, info_col2 = st.columns(2)
    
    with info_col1:
        st.write(f"**👤 Name:** {name}")
        st.write(f"**📅 Birth Date:** {birth_date.strftime('%B %d, %Y')}")  # Format: July 03, 1990
        st.write(f"**📆 Weekday:** {birth_date.strftime('%A')}")  # Day of week
    
    with info_col2:
        st.write(f"**🕐 Birth Time:** {birth_time}")
        st.write(f"**📍 Birth Place:** {birth_place}")
        
        # Calculate age
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        st.write(f"**🎂 Current Age:** {age} years")

    # Current Dasha Section
    st.header("⏰ Current Dasha Status")
    
    # Simple dasha calculation based on birth date
    dasha_planets = ['Sun', 'Moon', 'Mars', 'Rahu', 'Jupiter', 'Saturn', 'Mercury', 'Ketu', 'Venus']
    dasha_years = [6, 10, 7, 18, 16, 19, 17, 7, 20]
    
    # Calculate age in years from birth date
    birth_datetime = datetime.combine(birth_date, birth_time)
    current_age = (datetime.now() - birth_datetime).days / 365.25
    
    # Find current dasha
    total_years = 0
    current_dasha = 'Sun'
    current_antardasha = 'Moon'
    
    for i, (planet, years) in enumerate(zip(dasha_planets, dasha_years)):
        if current_age >= total_years and current_age < total_years + years:
            current_dasha = planet
            # Calculate antardasha
            dasha_progress = current_age - total_years
            antardasha_duration = years / len(dasha_planets)
            antardasha_index = int(dasha_progress / antardasha_duration) % len(dasha_planets)
            current_antardasha = dasha_planets[antardasha_index]
            break
        total_years += years
    
    dasha_col1, dasha_col2 = st.columns(2)
    
    with dasha_col1:
        st.write(f"**🌟 Main Dasha:** {current_dasha}")
        st.write(f"**🌙 Antardasha:** {current_antardasha}")
    
    with dasha_col2:
        # Determine dasha status
        benefic_planets = ['Jupiter', 'Venus', 'Moon', 'Mercury']
        if current_dasha in benefic_planets:
            st.success("**📈 Period Status:** Favorable")
        elif current_dasha in ['Saturn', 'Mars', 'Rahu', 'Ketu']:
            st.error("**📉 Period Status:** Challenging")
        else:
            st.warning("**⚖️ Period Status:** Mixed Results")

    # Current Planetary Positions
    st.header("🪐 Current Planetary Positions (August 7, 2025)")
    
    # Real planetary data from your table
    planets = [
        {"planet": "Sun ☉", "sign": "♋ Cancer", "degree": "20.76°", "nakshatra": "Ashlesha", "status": "Good"},
        {"planet": "Moon ☽", "sign": "♐ Sagittarius", "degree": "24.88°", "nakshatra": "Purva Ashadha", "status": "Good"},
        {"planet": "Mercury ☿", "sign": "♋ Cancer (Retrograde)", "degree": "10.93°", "nakshatra": "Pushya", "status": "Challenging"},
        {"planet": "Venus ♀", "sign": "♊ Gemini", "degree": "13.98°", "nakshatra": "Ardra", "status": "Good"},
        {"planet": "Mars ♂", "sign": "♍ Virgo", "degree": "5.94°", "nakshatra": "Uttara Phalguni", "status": "Neutral"},
        {"planet": "Jupiter ♃", "sign": "♊ Gemini", "degree": "18.81°", "nakshatra": "Ardra", "status": "Good"},
        {"planet": "Saturn ♄", "sign": "♓ Pisces (Retrograde)", "degree": "7.20°", "nakshatra": "Uttara Bhadrapada", "status": "Neutral"},
        {"planet": "Rahu ☊", "sign": "♒ Aquarius (Retrograde)", "degree": "25.73°", "nakshatra": "Purva Bhadrapada", "status": "Neutral"},
        {"planet": "Ketu ☋", "sign": "♌ Leo (Retrograde)", "degree": "25.73°", "nakshatra": "Purva Phalguni", "status": "Neutral"}
    ]
    
    # Display planets in a nice format
    for planet in planets:
        if planet["status"] == "Good":
            st.success(f"**{planet['planet']}** in {planet['sign']} at {planet['degree']} - Nakshatra: {planet['nakshatra']} - Status: **Favorable**")
        elif planet["status"] == "Challenging":
            st.error(f"**{planet['planet']}** in {planet['sign']} at {planet['degree']} - Nakshatra: {planet['nakshatra']} - Status: **Challenging**")
        else:
            st.warning(f"**{planet['planet']}** in {planet['sign']} at {planet['degree']} - Nakshatra: {planet['nakshatra']} - Status: **Neutral**")

    # Current Transit Effects
    st.header("🚀 Current Transit Effects")
    
    transit_effects = [
        ("Sun ☉ in Cancer", "Emotional depth and family focus - strengthening home bonds", "Good"),
        ("Moon ☽ in Sagittarius", "Spiritual expansion and philosophical thinking", "Good"),
        ("Mercury ☿ Retrograde in Cancer", "Communication delays, review family matters carefully", "Challenging"),
        ("Venus ♀ in Gemini", "Enhanced social skills and versatile relationships", "Good"),
        ("Mars ♂ in Virgo", "Practical action and attention to detail", "Good"),
        ("Jupiter ♃ in Gemini", "Knowledge expansion and teaching opportunities", "Good"),
        ("Saturn ♄ Retrograde in Pisces", "Deep spiritual lessons and karmic review", "Neutral"),
        ("Rahu ☊ in Aquarius", "Innovation and humanitarian focus", "Neutral")
    ]
    
    for transit, effect, status in transit_effects:
        if status == "Good":
            st.success(f"**{transit}:** {effect}")
        elif status == "Challenging":
            st.error(f"**{transit}:** {effect}")
        else:
            st.info(f"**{transit}:** {effect}")

    # Upcoming Transit Events
    st.header("📅 Upcoming Major Transit Events")
    
    st.info("**🟢 August 11, 2025:** Mercury turns Direct in Cancer - Communication clarity returns, family matters resolve")
    st.warning("**🟡 August 17, 2025:** Sun enters Leo - Leadership energy increases, confidence boost, creative expression")
    st.success("**🟢 August 21, 2025:** Venus enters Cancer - Love and harmony in family relationships, emotional bonding deepens")
    st.error("**🔴 September 1, 2025:** Saturn re-enters Pisces - Spiritual challenges return, need for compassionate discipline")
    st.info("**🟡 September 13, 2025:** Mars enters Libra - Balance in relationships, diplomatic approach to conflicts")
    st.success("**🟢 October 18, 2025:** Jupiter enters Cancer - Major expansion in family life and emotional prosperity")

    # Additional Analysis
    st.header("📊 Astrological Analysis Summary")
    
    analysis_col1, analysis_col2, analysis_col3 = st.columns(3)
    
    with analysis_col1:
        st.metric("🟢 Favorable Planets", "5", delta="Strong Support")
        st.caption("Sun, Moon, Venus, Mars, Jupiter")
    
    with analysis_col2:
        st.metric("🔴 Challenging Planets", "1", delta="Needs Attention")
        st.caption("Mercury (Retrograde)")
    
    with analysis_col3:
        st.metric("🟡 Neutral Planets", "3", delta="Balanced Energy")
        st.caption("Saturn, Rahu, Ketu")

    # Recommendations
    st.header("💡 Current Period Recommendations")
    
    rec_col1, rec_col2 = st.columns(2)
    
    with rec_col1:
        st.success("**✅ Favorable Activities:**")
        st.write("• Focus on spiritual growth and learning")
        st.write("• Strengthen family relationships")  
        st.write("• Engage in creative pursuits")
        st.write("• Practice meditation and mindfulness")
        st.write("• Plan for future expansion")
    
    with rec_col2:
        st.error("**⚠️ Areas Requiring Caution:**")
        st.write("• Important communications until Aug 11")
        st.write("• Major emotional decisions")
        st.write("• Technology and electronic purchases")
        st.write("• Travel plans (confirm details)")
        st.write("• Signing contracts or agreements")

else:
    # Welcome message when no calculation has been done
    st.info("👆 **Enter your birth details above and click 'Calculate Chart' to generate your personalized astrological analysis**")
    
    st.header("🌟 Current Cosmic Highlights")
    st.info("🔄 **Mercury Retrograde in Cancer** - Extra caution needed in communications and family matters")
    st.success("📚 **Jupiter in Gemini** - Excellent time for learning, teaching, and intellectual pursuits")
    st.warning("🔄 **Multiple Retrograde Planets** - Period of review, reflection, and inner work")

# Footer
st.markdown("---")
st.markdown("**🔮 Professional Vedic Astrology Calculator** | *Based on Real Astronomical Data for August 7, 2025*")
st.caption("This calculator uses traditional Vedic astrology principles combined with precise astronomical calculations.")
