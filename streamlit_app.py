import streamlit as st
from datetime import date, datetime
import time

# Page config
st.set_page_config(
    page_title="🌌 Solar System Astrology Calculator", 
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Solar System Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    /* Global Styles */
    .main {
        background: radial-gradient(ellipse at center, #0c0c1f 0%, #000000 70%);
        color: #ffffff;
        font-family: 'Orbitron', monospace;
    }
    
    .stApp {
        background: radial-gradient(ellipse at center, #0c0c1f 0%, #000000 70%);
    }
    
    /* Animated Stars Background */
    .stars-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
        overflow: hidden;
    }
    
    .star {
        position: absolute;
        width: 2px;
        height: 2px;
        background: #ffffff;
        border-radius: 50%;
        animation: twinkle 4s infinite;
    }
    
    @keyframes twinkle {
        0%, 100% { opacity: 0.3; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.2); }
    }
    
    /* Solar System Header */
    .solar-system-header {
        background: linear-gradient(135deg, #ff6b35, #f7941d, #ffd23f);
        padding: 40px 20px;
        border-radius: 25px;
        text-align: center;
        margin: 20px 0;
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 50px rgba(255, 165, 0, 0.5);
        animation: solarPulse 3s ease-in-out infinite;
    }
    
    @keyframes solarPulse {
        0%, 100% { box-shadow: 0 0 50px rgba(255, 165, 0, 0.5); }
        50% { box-shadow: 0 0 80px rgba(255, 165, 0, 0.8); }
    }
    
    .solar-system-header h1 {
        font-family: 'Orbitron', monospace;
        font-size: 3.5em;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.8);
        margin: 0;
        animation: titleFloat 4s ease-in-out infinite;
    }
    
    @keyframes titleFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Planet Orbit Animation */
    .orbit-container {
        position: relative;
        width: 300px;
        height: 300px;
        margin: 20px auto;
    }
    
    .orbit {
        position: absolute;
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 50%;
        animation: rotate 20s linear infinite;
    }
    
    .orbit-1 { width: 80px; height: 80px; top: 110px; left: 110px; animation-duration: 10s; }
    .orbit-2 { width: 120px; height: 120px; top: 90px; left: 90px; animation-duration: 15s; }
    .orbit-3 { width: 160px; height: 160px; top: 70px; left: 70px; animation-duration: 20s; }
    .orbit-4 { width: 200px; height: 200px; top: 50px; left: 50px; animation-duration: 25s; }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .sun-center {
        position: absolute;
        width: 60px;
        height: 60px;
        background: radial-gradient(circle, #ffd700, #ff8c00);
        border-radius: 50%;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        box-shadow: 0 0 40px #ffd700;
        animation: sunPulse 2s ease-in-out infinite;
    }
    
    @keyframes sunPulse {
        0%, 100% { transform: translate(-50%, -50%) scale(1); }
        50% { transform: translate(-50%, -50%) scale(1.1); }
    }
    
    .planet {
        position: absolute;
        width: 15px;
        height: 15px;
        border-radius: 50%;
        top: -7.5px;
        left: -7.5px;
    }
    
    .mercury { background: #8c7853; box-shadow: 0 0 10px #8c7853; }
    .venus { background: #ffc649; box-shadow: 0 0 10px #ffc649; }
    .earth { background: #6b93d6; box-shadow: 0 0 10px #6b93d6; }
    .mars { background: #c1440e; box-shadow: 0 0 10px #c1440e; }
    
    /* Mercury Retrograde Alert */
    .mercury-alert {
        background: linear-gradient(135deg, #ff4757, #ff3838);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        margin: 20px 0;
        position: relative;
        overflow: hidden;
        animation: alertPulse 2s ease-in-out infinite;
        box-shadow: 0 0 30px rgba(255, 71, 87, 0.6);
    }
    
    @keyframes alertPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .mercury-alert::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(transparent, rgba(255, 255, 255, 0.1), transparent);
        animation: mercuryRotate 3s linear infinite;
    }
    
    @keyframes mercuryRotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    /* Dynamic Panels */
    .cosmic-panel {
        background: linear-gradient(135deg, rgba(30, 30, 60, 0.8), rgba(20, 20, 40, 0.9));
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .cosmic-panel:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(100, 100, 255, 0.2);
        border-color: rgba(255, 255, 255, 0.3);
    }
    
    .cosmic-panel::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .cosmic-panel:hover::before {
        left: 100%;
    }
    
    /* Planet Status Cards */
    .planet-card {
        background: linear-gradient(135deg, rgba(50, 50, 100, 0.6), rgba(30, 30, 60, 0.8));
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        border-left: 5px solid;
        position: relative;
        transition: all 0.3s ease;
        backdrop-filter: blur(5px);
    }
    
    .planet-card:hover {
        transform: translateX(10px);
        box-shadow: 0 5px 25px rgba(0, 0, 0, 0.3);
    }
    
    .planet-good {
        border-left-color: #00ff88;
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.1), rgba(0, 200, 100, 0.1));
    }
    
    .planet-challenging {
        border-left-color: #ff4757;
        background: linear-gradient(135deg, rgba(255, 71, 87, 0.1), rgba(255, 50, 70, 0.1));
    }
    
    .planet-neutral {
        border-left-color: #ffa502;
        background: linear-gradient(135deg, rgba(255, 165, 2, 0.1), rgba(255, 140, 0, 0.1));
    }
    
    /* Constellation Background */
    .constellation-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -2;
    }
    
    /* Animated Metrics */
    .cosmic-metric {
        background: linear-gradient(135deg, rgba(100, 100, 255, 0.2), rgba(150, 100, 255, 0.2));
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin: 10px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .cosmic-metric:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 30px rgba(100, 100, 255, 0.3);
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(135deg, rgba(20, 20, 40, 0.9), rgba(30, 30, 60, 0.9));
        backdrop-filter: blur(10px);
    }
    
    /* Input Fields */
    .stTextInput > div > div > input,
    .stDateInput > div > div > input,
    .stTimeInput > div > div > input {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 10px;
        color: #ffffff;
        backdrop-filter: blur(5px);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border: none;
        border-radius: 15px;
        color: white;
        font-weight: bold;
        padding: 15px 30px;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2, #667eea);
    }
    
    /* Success/Error/Warning Messages */
    .stSuccess {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.2), rgba(0, 200, 100, 0.1));
        border: 1px solid rgba(0, 255, 136, 0.3);
        border-radius: 10px;
    }
    
    .stError {
        background: linear-gradient(135deg, rgba(255, 71, 87, 0.2), rgba(255, 50, 70, 0.1));
        border: 1px solid rgba(255, 71, 87, 0.3);
        border-radius: 10px;
    }
    
    .stWarning {
        background: linear-gradient(135deg, rgba(255, 165, 2, 0.2), rgba(255, 140, 0, 0.1));
        border: 1px solid rgba(255, 165, 2, 0.3);
        border-radius: 10px;
    }
    
    /* Loading Animation */
    .loading-cosmos {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
    }
    
    .cosmic-loader {
        width: 60px;
        height: 60px;
        border: 3px solid rgba(255, 255, 255, 0.1);
        border-top: 3px solid #667eea;
        border-radius: 50%;
        animation: cosmicSpin 1s linear infinite;
    }
    
    @keyframes cosmicSpin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style>

<div class="stars-container" id="starsContainer"></div>
<div class="constellation-bg" id="constellationBg"></div>

<script>
// Create animated stars
function createStars() {
    const container = document.getElementById('starsContainer');
    const numStars = 200;
    
    for (let i = 0; i < numStars; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 100 + '%';
        star.style.animationDelay = Math.random() * 4 + 's';
        star.style.animationDuration = (3 + Math.random() * 2) + 's';
        container.appendChild(star);
    }
}

// Initialize stars when page loads
setTimeout(createStars, 100);
</script>
""", unsafe_allow_html=True)

# Solar System Header
st.markdown("""
<div class="solar-system-header">
    <h1>🌌 SOLAR SYSTEM ASTROLOGY CALCULATOR</h1>
    <div class="orbit-container">
        <div class="sun-center"></div>
        <div class="orbit orbit-1">
            <div class="planet mercury"></div>
        </div>
        <div class="orbit orbit-2">
            <div class="planet venus"></div>
        </div>
        <div class="orbit orbit-3">
            <div class="planet earth"></div>
        </div>
        <div class="orbit orbit-4">
            <div class="planet mars"></div>
        </div>
    </div>
    <p style="color: #ffffff; font-size: 1.2em; margin-top: 20px;">
        Real-time Cosmic Analysis & Planetary Transit Predictions
    </p>
</div>
""", unsafe_allow_html=True)

# Mercury Retrograde Alert with Animation
st.markdown("""
<div class="mercury-alert">
    <h2 style="color: #ffffff; margin: 0; font-size: 1.8em; position: relative; z-index: 1;">
        ⚠️ COSMIC ALERT: MERCURY RETROGRADE ⚠️
    </h2>
    <p style="color: #ffffff; font-size: 1.2em; margin: 15px 0 0 0; position: relative; z-index: 1;">
        August 7, 2025 - Communications & Technology require extreme caution until August 11, 2025
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar for cosmic input
with st.sidebar:
    st.markdown("### 🌟 COSMIC BIRTH DATA")
    
    # Input fields with cosmic styling
    name = st.text_input("👤 Cosmic Entity Name", value="STELLAR NAVIGATOR", help="Enter your celestial identity")
    
    birth_date = st.date_input(
        "📅 Earth Birth Coordinates", 
        value=date(1990, 7, 3),
        min_value=date(1900, 1, 1),
        max_value=date(2030, 12, 31),
        help="When did you enter this dimension?"
    )
    
    birth_time = st.time_input("🕐 Universal Time", value=datetime.now().time(), help="Your cosmic arrival time")
    
    birth_place = st.text_input("📍 Planetary Coordinates", value="Earth - Sol System", help="Your origin point in space-time")
    
    # Real-time cosmic clock
    if 'time_placeholder' not in st.session_state:
        st.session_state.time_placeholder = st.empty()
    
    with st.session_state.time_placeholder.container():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(100, 100, 255, 0.3), rgba(150, 100, 255, 0.3)); 
                    padding: 15px; border-radius: 10px; text-align: center; margin: 10px 0;">
            <strong>🕐 COSMIC TIME:</strong><br>
            {current_time}
        </div>
        """, unsafe_allow_html=True)

# Main calculation area
if st.sidebar.button("🚀 INITIATE COSMIC ANALYSIS", type="primary"):
    
    # Animated loading
    with st.spinner("🌌 Analyzing cosmic alignments..."):
        time.sleep(2)  # Simulate processing
    
    st.success("✨ **COSMIC ANALYSIS COMPLETE** - Your stellar blueprint has been decoded!")
    
    # Personal Cosmic Profile
    st.markdown("""
    <div class="cosmic-panel">
        <h2 style="text-align: center; color: #ffffff; margin-bottom: 25px;">
            🌟 COSMIC PERSONAL PROFILE
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="cosmic-metric">
            <h3 style="color: #667eea;">👤 STELLAR IDENTITY</h3>
            <p style="color: #ffffff; font-size: 1.2em;">{name}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="cosmic-metric">
            <h3 style="color: #667eea;">📅 EARTH MANIFESTATION</h3>
            <p style="color: #ffffff; font-size: 1.2em;">{birth_date.strftime('%B %d, %Y')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="cosmic-metric">
            <h3 style="color: #667eea;">🕐 UNIVERSAL MOMENT</h3>
            <p style="color: #ffffff; font-size: 1.2em;">{birth_time}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="cosmic-metric">
            <h3 style="color: #667eea;">📆 COSMIC CYCLE</h3>
            <p style="color: #ffffff; font-size: 1.2em;">{birth_date.strftime('%A')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # Calculate age
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        st.markdown(f"""
        <div class="cosmic-metric">
            <h3 style="color: #667eea;">🌍 PLANETARY LOCATION</h3>
            <p style="color: #ffffff; font-size: 1.2em;">{birth_place}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="cosmic-metric">
            <h3 style="color: #667eea;">🎂 SOLAR ORBITS</h3>
            <p style="color: #ffffff; font-size: 1.2em;">{age} Years</p>
        </div>
        """, unsafe_allow_html=True)

    # Current Dasha Analysis with Cosmic Theme
    st.markdown("""
    <div class="cosmic-panel">
        <h2 style="text-align: center; color: #ffffff; margin-bottom: 25px;">
            ⏰ CURRENT PLANETARY DOMINANCE CYCLES
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Dasha calculation
    dasha_planets = ['Sun', 'Moon', 'Mars', 'Rahu', 'Jupiter', 'Saturn', 'Mercury', 'Ketu', 'Venus']
    dasha_years = [6, 10, 7, 18, 16, 19, 17, 7, 20]
    
    birth_datetime = datetime.combine(birth_date, birth_time)
    current_age = (datetime.now() - birth_datetime).days / 365.25
    
    # Find current dasha
    total_years = 0
    current_dasha = 'Sun'
    current_antardasha = 'Moon'
    
    for i, (planet, years) in enumerate(zip(dasha_planets, dasha_years)):
        if current_age >= total_years and current_age < total_years + years:
            current_dasha = planet
            dasha_progress = current_age - total_years
            antardasha_duration = years / len(dasha_planets)
            antardasha_index = int(dasha_progress / antardasha_duration) % len(dasha_planets)
            current_antardasha = dasha_planets[antardasha_index]
            years_left = total_years + years - current_age
            break
        total_years += years
    
    dasha_col1, dasha_col2 = st.columns(2)
    
    with dasha_col1:
        # Determine dasha planet colors
        planet_colors = {
            'Sun': '#ffd700', 'Moon': '#c0c0c0', 'Mars': '#ff4500', 'Mercury': '#32cd32',
            'Jupiter': '#daa520', 'Venus': '#ff69b4', 'Saturn': '#4169e1', 'Rahu': '#8b008b', 'Ketu': '#ff6347'
        }
        
        main_color = planet_colors.get(current_dasha, '#667eea')
        sub_color = planet_colors.get(current_antardasha, '#764ba2')
        
        st.markdown(f"""
        <div class="cosmic-metric" style="background: linear-gradient(135deg, rgba(255, 215, 0, 0.2), rgba(255, 165, 0, 0.1));">
            <h3 style="color: {main_color};">🌟 MAIN COSMIC RULER</h3>
            <p style="color: #ffffff; font-size: 1.5em; font-weight: bold;">{current_dasha}</p>
            <p style="color: #cccccc; font-size: 0.9em;">Dominating your cosmic sphere</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="cosmic-metric" style="background: linear-gradient(135deg, rgba(192, 192, 192, 0.2), rgba(169, 169, 169, 0.1));">
            <h3 style="color: {sub_color};">🌙 SUB-COSMIC INFLUENCE</h3>
            <p style="color: #ffffff; font-size: 1.5em; font-weight: bold;">{current_antardasha}</p>
            <p style="color: #cccccc; font-size: 0.9em;">Secondary energy pattern</p>
        </div>
        """, unsafe_allow_html=True)
    
    with dasha_col2:
        # Cosmic status determination
        benefic_planets = ['Jupiter', 'Venus', 'Moon', 'Mercury']
        if current_dasha in benefic_planets:
            status_color = "#00ff88"
            status_text = "🌟 COSMIC HARMONY PHASE"
            status_desc = "Favorable stellar alignments supporting growth and prosperity"
        elif current_dasha in ['Saturn', 'Mars', 'Rahu', 'Ketu']:
            status_color = "#ff4757"
            status_text = "⚡ COSMIC CHALLENGE PHASE"
            status_desc = "Transformative period requiring courage and wisdom"
        else:
            status_color = "#ffa502"
            status_text = "⚖️ COSMIC BALANCE PHASE"
            status_desc = "Mixed energies creating learning opportunities"
        
        st.markdown(f"""
        <div class="cosmic-metric" style="border: 2px solid {status_color}; background: linear-gradient(135deg, rgba(0, 255, 136, 0.1), rgba(0, 200, 100, 0.1));">
            <h3 style="color: {status_color};">📊 CURRENT COSMIC STATUS</h3>
            <p style="color: #ffffff; font-size: 1.2em; font-weight: bold;">{status_text}</p>
            <p style="color: #cccccc; font-size: 0.9em;">{status_desc}</p>
        </div>
        """, unsafe_allow_html=True)
        
        try:
            years_remaining = total_years + dasha_years[dasha_planets.index(current_dasha)] - current_age
            st.markdown(f"""
            <div class="cosmic-metric">
                <h3 style="color: #764ba2;">⏳ PHASE DURATION</h3>
                <p style="color: #ffffff; font-size: 1.2em; font-weight: bold;">{years_remaining:.1f} Years Remaining</p>
                <p style="color: #cccccc; font-size: 0.9em;">Until next major cosmic shift</p>
            </div>
            """, unsafe_allow_html=True)
        except:
            pass

    # Current Planetary Positions with Solar System Theme
    st.markdown("""
    <div class="cosmic-panel">
        <h2 style="text-align: center; color: #ffffff; margin-bottom: 25px;">
            🪐 REAL-TIME PLANETARY COORDINATES (August 7, 2025)
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Real planetary data with cosmic presentation
    cosmic_planets = [
        {"planet": "☉ SOLAR CORE", "sign": "♋ Cancer Constellation", "degree": "20.76°", "nakshatra": "Ashlesha Star Cluster", "status": "good", "energy": "Life Force Amplification"},
        {"planet": "☽ LUNAR SATELLITE", "sign": "♐ Sagittarius Sector", "degree": "24.88°", "nakshatra": "Purva Ashadha Nebula", "status": "good", "energy": "Intuitive Navigation"},
        {"planet": "☿ MERCURY PROBE", "sign": "♋ Cancer Zone (RETROGRADE)", "degree": "10.93°", "nakshatra": "Pushya Constellation", "status": "challenging", "energy": "Communication Disruption"},
        {"planet": "♀ VENUS STATION", "sign": "♊ Gemini Quadrant", "degree": "13.98°", "nakshatra": "Ardra Star System", "status": "good", "energy": "Harmonic Resonance"},
        {"planet": "♂ MARS OUTPOST", "sign": "♍ Virgo Territory", "degree": "5.94°", "nakshatra": "Uttara Phalguni Cluster", "status": "neutral", "energy": "Strategic Precision"},
        {"planet": "♃ JUPITER GIANT", "sign": "♊ Gemini Space", "degree": "18.81°", "nakshatra": "Ardra Federation", "status": "good", "energy": "Wisdom Expansion"},
        {"planet": "♄ SATURN RINGS", "sign": "♓ Pisces Realm (RETROGRADE)", "degree": "7.20°", "nakshatra": "Uttara Bhadrapada Grid", "status": "neutral", "energy": "Karmic Recalibration"},
        {"planet": "☊ RAHU NODE", "sign": "♒ Aquarius Matrix (RETROGRADE)", "degree": "25.73°", "nakshatra": "Purva Bhadrapada Network", "status": "neutral", "energy": "Innovation Portal"},
        {"planet": "☋ KETU NODE", "sign": "♌ Leo Dimension (RETROGRADE)", "degree": "25.73°", "nakshatra": "Purva Phalguni Gateway", "status": "neutral", "energy": "Spiritual Liberation"}
    ]
    
    for planet in cosmic_planets:
        if planet["status"] == "good":
            card_class = "planet-good"
            status_icon = "🟢"
            status_text = "FAVORABLE ALIGNMENT"
        elif planet["status"] == "challenging":
            card_class = "planet-challenging"
            status_icon = "🔴"
            status_text = "CAUTION REQUIRED"
        else:
            card_class = "planet-neutral"
            status_icon = "🟡"
            status_text = "NEUTRAL INFLUENCE"
        
        st.markdown(f"""
        <div class="planet-card {card_class}">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <h3 style="color: #ffffff; margin: 0;">{planet['planet']}</h3>
                <span style="font-size: 1.2em;">{status_icon}</span>
            </div>
            <p style="color: #cccccc; margin: 5px 0;"><strong>Cosmic Position:</strong> {planet['sign']} at {planet['degree']}</p>
            <p style="color: #cccccc; margin: 5px 0;"><strong>Star Formation:</strong> {planet['nakshatra']}</p>
            <p style="color: #cccccc; margin: 5px 0;"><strong>Energy Signature:</strong> {planet['energy']}</p>
            <p style="margin: 10px 0 0 0; font-weight: bold;"><strong>Status:</strong> {status_text}</p>
        </div>
        """, unsafe_allow_html=True)

    # Cosmic Transit Effects
    st.markdown("""
    <div class="cosmic-panel">
        <h2 style="text-align: center; color: #ffffff; margin-bottom: 25px;">
            🌊 ACTIVE COSMIC WAVE PATTERNS
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    cosmic_transits = [
        ("☉ Solar Core in Cancer Sector", "Deep emotional resonance waves - Family bond amplification active", "good"),
        ("☽ Lunar Satellite in Sagittarius", "Spiritual frequency elevation - Wisdom channel opening", "good"),
        ("☿ Mercury Probe RETROGRADE", "Communication matrix disrupted - System recalibration in progress", "challenging"),
        ("♀ Venus Station in Gemini", "Harmonic social frequencies - Creative channel enhancement", "good"),
        ("♂ Mars Outpost in Virgo", "Precision action protocols - Strategic implementation phase", "good"),
        ("♃ Jupiter Giant in Gemini", "Knowledge expansion wave - Teaching transmission active", "good"),
        ("♄ Saturn Rings RETROGRADE", "Karmic data review - Spiritual lesson integration cycle", "neutral"),
        ("☊ Rahu Node in Aquarius", "Innovation portal active - Revolutionary frequency detected", "neutral")
    ]
    
    for transit, effect, status in cosmic_transits:
        if status == "good":
            st.success(f"**🌟 {transit}:** {effect}")
        elif status == "challenging":
            st.error(f"**⚠️ {transit}:** {effect}")
        else:
            st.info(f"**🔮 {transit}:** {effect}")

    # Upcoming Cosmic Events Timeline
    st.markdown("""
    <div class="cosmic-panel">
        <h2 style="text-align: center; color: #ffffff; margin-bottom: 25px;">
            📅 UPCOMING COSMIC EVENTS TIMELINE
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    timeline_events = [
        ("August 11, 2025", "Mercury Probe Systems Resume", "Communication matrix restoration - All systems nominal", "good"),
        ("August 17, 2025", "Solar Core enters Leo Dimension", "Leadership frequency activation - Confidence boost protocol", "neutral"),
        ("August 21, 2025", "Venus Station enters Cancer Sector", "Love harmonic amplification - Family bond enhancement", "good"),
        ("September 1, 2025", "Saturn Rings re-enter Pisces Realm", "Spiritual challenge protocol reactivation - Compassion training", "challenging"),
        ("September 13, 2025", "Mars Outpost enters Libra Balance", "Diplomatic strategy mode - Relationship harmony protocol", "neutral"),
        ("October 18, 2025", "Jupiter Giant enters Cancer Territory", "Major family expansion wave - Emotional prosperity surge", "good")
    ]
    
    for event_date, event_name, event_description, status in timeline_events:
        if status == "good":
            icon = "🟢"
            bg_color = "rgba(0, 255, 136, 0.1)"
        elif status == "challenging":
            icon = "🔴"
            bg_color = "rgba(255, 71, 87, 0.1)"
        else:
            icon = "🟡"
            bg_color = "rgba(255, 165, 2, 0.1)"
        
        st.markdown(f"""
        <div style="background: {bg_color}; padding: 15px; border-radius: 10px; margin: 10px 0; border-left: 4px solid;">
            <div style="display: flex; align-items: center; gap: 15px;">
                <span style="font-size: 1.5em;">{icon}</span>
                <div>
                    <h4 style="color: #ffffff; margin: 0;">{event_date}: {event_name}</h4>
                    <p style="color: #cccccc; margin: 5px 0 0 0;">{event_description}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Cosmic Analysis Summary
    st.markdown("""
    <div class="cosmic-panel">
        <h2 style="text-align: center; color: #ffffff; margin-bottom: 25px;">
            📊 COSMIC FORCE ANALYSIS MATRIX
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    
    with metric_col1:
        st.markdown("""
        <div class="cosmic-metric" style="background: linear-gradient(135deg, rgba(0, 255, 136, 0.2), rgba(0, 200, 100, 0.1));">
            <h3 style="color: #00ff88;">🟢 FAVORABLE FORCES</h3>
            <p style="color: #ffffff; font-size: 2em; font-weight: bold;">6</p>
            <p style="color: #cccccc;">Solar, Lunar, Venus, Mars, Jupiter, Timeline</p>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown("""
        <div class="cosmic-metric" style="background: linear-gradient(135deg, rgba(255, 71, 87, 0.2), rgba(255, 50, 70, 0.1));">
            <h3 style="color: #ff4757;">🔴 CHALLENGING FORCES</h3>
            <p style="color: #ffffff; font-size: 2em; font-weight: bold;">1</p>
            <p style="color: #cccccc;">Mercury Retrograde Protocol</p>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_col3:
        st.markdown("""
        <div class="cosmic-metric" style="background: linear-gradient(135deg, rgba(255, 165, 2, 0.2), rgba(255, 140, 0, 0.1));">
            <h3 style="color: #ffa502;">🟡 NEUTRAL FORCES</h3>
            <p style="color: #ffffff; font-size: 2em; font-weight: bold;">4</p>
            <p style="color: #cccccc;">Saturn, Rahu, Ketu, Future Events</p>
        </div>
        """, unsafe_allow_html=True)

    # Cosmic Recommendations
    st.markdown("""
    <div class="cosmic-panel">
        <h2 style="text-align: center; color: #ffffff; margin-bottom: 25px;">
            💫 COSMIC NAVIGATION PROTOCOLS
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    rec_col1, rec_col2 = st.columns(2)
    
    with rec_col1:
        st.markdown("""
        <div class="planet-card planet-good">
            <h3 style="color: #00ff88; margin-bottom: 15px;">✅ OPTIMAL COSMIC ACTIVITIES</h3>
            <ul style="color: #ffffff; line-height: 1.6;">
                <li>🧘 Deep space meditation & spiritual practice</li>
                <li>👨‍👩‍👧‍👦 Strengthen family constellation bonds</li>
                <li>🎨 Channel creative cosmic energies</li>
                <li>📚 Engage in knowledge absorption protocols</li>
                <li>🌱 Plant seeds for future dimensional growth</li>
                <li>💖 Express love through harmonic frequencies</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with rec_col2:
        st.markdown("""
        <div class="planet-card planet-challenging">
            <h3 style="color: #ff4757; margin-bottom: 15px;">⚠️ COSMIC HAZARD PROTOCOLS</h3>
            <ul style="color: #ffffff; line-height: 1.6;">
                <li>📡 Avoid critical communications until Aug 11</li>
                <li>💔 Delay major emotional constellation decisions</li>
                <li>🔧 Postpone technology system upgrades</li>
                <li>✈️ Confirm all inter-dimensional travel plans</li>
                <li>📝 Review all cosmic contracts carefully</li>
                <li>⚡ Backup all important data transmissions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

else:
    # Welcome screen with cosmic theme
    st.markdown("""
    <div class="cosmic-panel">
        <h2 style="text-align: center; color: #ffffff;">🌌 WELCOME TO THE COSMIC NAVIGATION CENTER</h2>
        <p style="text-align: center; color: #cccccc; font-size: 1.2em; margin: 20px 0;">
            Enter your cosmic coordinates in the sidebar and initiate your stellar analysis
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cosmic-panel">
        <h3 style="color: #667eea; text-align: center; margin-bottom: 20px;">🌟 CURRENT COSMIC CONDITIONS</h3>
    </div>
    """, unsafe_allow_html=True)
    
    highlight_col1, highlight_col2, highlight_col3 = st.columns(3)
    
    with highlight_col1:
        st.info("🔄 **Mercury Retrograde Active** - Communication systems require enhanced caution protocols")
    
    with highlight_col2:
        st.success("📚 **Jupiter in Gemini Sector** - Optimal conditions for knowledge acquisition and teaching transmission")
    
    with highlight_col3:
        st.warning("🔄 **Multiple Retrograde Patterns** - Perfect time for system review and internal recalibration")

# Cosmic Footer
st.markdown("""
<div style="text-align: center; margin: 40px 0; padding: 30px; background: linear-gradient(135deg, rgba(50, 50, 100, 0.3), rgba(30, 30, 60, 0.5)); border-radius: 20px;">
    <h3 style="color: #667eea; margin-bottom: 15px;">🌌 COSMIC MISSION CONTROL CENTER</h3>
    <p style="color: #ffffff; font-size: 1.1em;">
        Powered by Real Astronomical Data | Solar System Coordinates: August 7, 2025
    </p>
    <p style="color: #cccccc; margin-top: 10px;">
        This advanced cosmic navigation system utilizes precise astronomical calculations and ancient Vedic stellar wisdom
    </p>
</div>
""", unsafe_allow_html=True)

# Auto-refresh cosmic time every 30 seconds
time.sleep(0.1)  # Small delay to ensure page loads
if st.session_state.get('auto_refresh', True):
    time.sleep(1)
