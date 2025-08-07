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

# Enhanced CSS with lighter theme and better fonts
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;500;600&display=swap');
    
    /* Global Styles - Lighter Cosmic Theme */
    .main {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 25%, #0f3460 50%, #533483 75%, #7209b7 100%);
        color: #ffffff;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 25%, #0f3460 50%, #533483 75%, #7209b7 100%);
    }
    
    /* Enhanced Stars Background */
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
        width: 3px;
        height: 3px;
        background: linear-gradient(45deg, #ffffff, #e6f3ff);
        border-radius: 50%;
        animation: twinkle 3s infinite ease-in-out;
        box-shadow: 0 0 6px rgba(255, 255, 255, 0.8);
    }
    
    @keyframes twinkle {
        0%, 100% { opacity: 0.4; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1.2); }
    }
    
    /* Cosmic Header */
    .cosmic-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 40px 20px;
        border-radius: 25px;
        text-align: center;
        margin: 20px 0;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 50px rgba(102, 126, 234, 0.4);
        animation: headerGlow 4s ease-in-out infinite;
    }
    
    @keyframes headerGlow {
        0%, 100% { box-shadow: 0 10px 50px rgba(102, 126, 234, 0.4); }
        50% { box-shadow: 0 15px 60px rgba(118, 75, 162, 0.6); }
    }
    
    .cosmic-header h1 {
        font-family: 'Orbitron', monospace;
        font-size: 3.5em;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 0 0 30px rgba(255, 255, 255, 0.9);
        margin: 0;
        animation: titleFloat 5s ease-in-out infinite;
    }
    
    @keyframes titleFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
    }
    
    /* Enhanced Planet Animation */
    .solar-system {
        position: relative;
        width: 350px;
        height: 350px;
        margin: 30px auto;
    }
    
    .orbit {
        position: absolute;
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        animation: rotate linear infinite;
    }
    
    .orbit-1 { width: 100px; height: 100px; top: 125px; left: 125px; animation-duration: 8s; }
    .orbit-2 { width: 150px; height: 150px; top: 100px; left: 100px; animation-duration: 12s; }
    .orbit-3 { width: 200px; height: 200px; top: 75px; left: 75px; animation-duration: 16s; }
    .orbit-4 { width: 250px; height: 250px; top: 50px; left: 50px; animation-duration: 20s; }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .sun-center {
        position: absolute;
        width: 80px;
        height: 80px;
        background: radial-gradient(circle, #ffd700, #ff8c00, #ff6b35);
        border-radius: 50%;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        box-shadow: 0 0 50px #ffd700, inset 0 0 20px rgba(255, 255, 255, 0.3);
        animation: sunPulse 3s ease-in-out infinite;
    }
    
    @keyframes sunPulse {
        0%, 100% { transform: translate(-50%, -50%) scale(1); }
        50% { transform: translate(-50%, -50%) scale(1.15); }
    }
    
    .planet {
        position: absolute;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        top: -9px;
        left: -9px;
        box-shadow: 0 0 15px;
    }
    
    .mercury { background: linear-gradient(45deg, #8c7853, #b8a082); box-shadow: 0 0 15px #8c7853; }
    .venus { background: linear-gradient(45deg, #ffc649, #ffab00); box-shadow: 0 0 15px #ffc649; }
    .earth { background: linear-gradient(45deg, #6b93d6, #4a90e2); box-shadow: 0 0 15px #6b93d6; }
    .mars { background: linear-gradient(45deg, #c1440e, #e74c3c); box-shadow: 0 0 15px #c1440e; }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.3), rgba(118, 75, 162, 0.3));
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: #ffffff;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        backdrop-filter: blur(5px);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.5), rgba(118, 75, 162, 0.5));
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.3);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        box-shadow: 0 5px 25px rgba(102, 126, 234, 0.5);
        transform: translateY(-2px);
    }
    
    /* Enhanced Input Fields with Better Fonts */
    .stTextInput > div > div > input,
    .stDateInput > div > div > input,
    .stTimeInput > div > div > input,
    .stSelectbox > div > div > input {
        background: rgba(255, 255, 255, 0.15) !important;
        border: 2px solid rgba(102, 126, 234, 0.4) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        padding: 12px 16px !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stDateInput > div > div > input:focus,
    .stTimeInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.5) !important;
        background: rgba(255, 255, 255, 0.2) !important;
    }
    
    /* Input Labels */
    .stTextInput > label,
    .stDateInput > label,
    .stTimeInput > label,
    .stSelectbox > label {
        color: #ffffff !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.3) !important;
    }
    
    /* Enhanced Panels */
    .cosmic-panel {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 30px;
        margin: 25px 0;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .cosmic-panel:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.2);
        border-color: rgba(255, 255, 255, 0.4);
    }
    
    /* Mercury Alert - Less Intense */
    .mercury-alert {
        background: linear-gradient(135deg, rgba(255, 107, 107, 0.8), rgba(255, 71, 87, 0.6));
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        margin: 20px 0;
        animation: gentleAlert 3s ease-in-out infinite;
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.3);
        backdrop-filter: blur(10px);
    }
    
    @keyframes gentleAlert {
        0%, 100% { transform: scale(1); box-shadow: 0 10px 30px rgba(255, 107, 107, 0.3); }
        50% { transform: scale(1.01); box-shadow: 0 12px 35px rgba(255, 107, 107, 0.4); }
    }
    
    /* Planet Cards */
    .planet-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.12), rgba(255, 255, 255, 0.08));
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        border-left: 4px solid;
        position: relative;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        font-family: 'Space Grotesk', sans-serif;
    }
    
    .planet-card:hover {
        transform: translateX(8px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.18), rgba(255, 255, 255, 0.12));
    }
    
    .planet-good {
        border-left-color: #00d4aa;
        background: linear-gradient(135deg, rgba(0, 212, 170, 0.15), rgba(0, 200, 160, 0.1));
    }
    
    .planet-challenging {
        border-left-color: #ff6b6b;
        background: linear-gradient(135deg, rgba(255, 107, 107, 0.15), rgba(255, 80, 80, 0.1));
    }
    
    .planet-neutral {
        border-left-color: #feca57;
        background: linear-gradient(135deg, rgba(254, 202, 87, 0.15), rgba(255, 165, 2, 0.1));
    }
    
    /* Metrics */
    .cosmic-metric {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.12), rgba(255, 255, 255, 0.08));
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        margin: 15px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
    }
    
    .cosmic-metric:hover {
        transform: scale(1.03);
        box-shadow: 0 10px 35px rgba(102, 126, 234, 0.25);
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.18), rgba(255, 255, 255, 0.12));
    }
    
    /* Sidebar Enhancement */
    .css-1d391kg {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05)) !important;
        backdrop-filter: blur(15px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    
    /* Enhanced Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        border: none !important;
        border-radius: 15px !important;
        color: white !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        padding: 15px 30px !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4) !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.6) !important;
        background: linear-gradient(135deg, #764ba2, #f093fb) !important;
    }
    
    /* Success/Error/Info Messages */
    .stSuccess {
        background: linear-gradient(135deg, rgba(0, 212, 170, 0.15), rgba(0, 200, 160, 0.1)) !important;
        border: 1px solid rgba(0, 212, 170, 0.4) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .stError {
        background: linear-gradient(135deg, rgba(255, 107, 107, 0.15), rgba(255, 80, 80, 0.1)) !important;
        border: 1px solid rgba(255, 107, 107, 0.4) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .stWarning, .stInfo {
        background: linear-gradient(135deg, rgba(254, 202, 87, 0.15), rgba(255, 165, 2, 0.1)) !important;
        border: 1px solid rgba(254, 202, 87, 0.4) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Tab Content Styling */
    .stTabs [data-baseweb="tab-panel"] {
        padding-top: 30px;
    }
    
    /* Loading Animation */
    .cosmic-loader {
        width: 60px;
        height: 60px;
        border: 3px solid rgba(255, 255, 255, 0.2);
        border-top: 3px solid #667eea;
        border-radius: 50%;
        animation: cosmicSpin 1.2s linear infinite;
        margin: 0 auto;
    }
    
    @keyframes cosmicSpin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Constellation Lines */
    .constellation-line {
        position: absolute;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        animation: constellationGlow 4s ease-in-out infinite;
    }
    
    @keyframes constellationGlow {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.8; }
    }
</style>

<div class="stars-container" id="starsContainer"></div>

<script>
// Enhanced star creation
function createStars() {
    const container = document.getElementById('starsContainer');
    if (!container) return;
    
    const numStars = 150;
    
    for (let i = 0; i < numStars; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 100 + '%';
        star.style.animationDelay = Math.random() * 3 + 's';
        star.style.animationDuration = (2 + Math.random() * 2) + 's';
        
        // Varying star sizes
        const size = Math.random() * 3 + 1;
        star.style.width = size + 'px';
        star.style.height = size + 'px';
        
        container.appendChild(star);
    }
}

// Initialize stars
setTimeout(createStars, 100);
</script>
""", unsafe_allow_html=True)

# Enhanced Header
st.markdown("""
<div class="cosmic-header">
    <h1>🌌 ASTROLOGY NAVIGATION CENTER</h1>
    <div class="solar-system">
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
    <p style="color: #ffffff; font-size: 1.3em; margin-top: 25px; font-family: 'Space Grotesk', sans-serif;">
        🚀 Advanced Cosmic Intelligence & Planetary Analysis System
    </p>
</div>
""", unsafe_allow_html=True)

# Mercury Retrograde Alert (Softer)
st.markdown("""
<div class="mercury-alert">
    <h2 style="color: #ffffff; margin: 0; font-size: 1.8em; font-family: 'Space Grotesk', sans-serif;">
        ⚠️ MERCURY RETROGRADE ACTIVE ⚠️
    </h2>
    <p style="color: #ffffff; font-size: 1.1em; margin: 10px 0 0 0;">
        August 7-11, 2025 | Exercise caution with communications & technology
    </p>
</div>
""", unsafe_allow_html=True)

# Enhanced Sidebar with Better Input Styling
with st.sidebar:
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05)); 
                padding: 25px; border-radius: 20px; margin-bottom: 20px; backdrop-filter: blur(10px);">
        <h2 style="color: #ffffff; text-align: center; font-family: 'Orbitron', monospace; margin-bottom: 20px;">
            🌟 COSMIC COORDINATES
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced input fields
    name = st.text_input(
        "👤 Stellar Identity", 
        value="Cosmic Navigator", 
        help="Enter your celestial name",
        placeholder="Your cosmic identity..."
    )
    
    birth_date = st.date_input(
        "📅 Earth Manifestation Date", 
        value=date(1990, 7, 3),
        min_value=date(1900, 1, 1),
        max_value=date(2030, 12, 31),
        help="When did you enter this dimension?"
    )
    
    birth_time = st.time_input(
        "🕐 Universal Time", 
        value=datetime.now().time(), 
        help="Your cosmic arrival moment"
    )
    
    birth_place = st.text_input(
        "📍 Planetary Location", 
        value="Earth, Sol System", 
        help="Your origin coordinates",
        placeholder="City, Country..."
    )
    
    st.markdown("---")
    
    # Real-time cosmic clock
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2)); 
                padding: 20px; border-radius: 15px; text-align: center; margin: 15px 0; backdrop-filter: blur(10px);">
        <h4 style="color: #ffffff; margin: 0; font-family: 'Orbitron', monospace;">🕐 COSMIC TIME</h4>
        <p style="color: #ffffff; font-size: 1.1em; margin: 8px 0 0 0; font-family: 'Inter', monospace;">
            {current_time}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced Analysis Button
    analyze_button = st.button("🚀 INITIATE COSMIC ANALYSIS", type="primary", use_container_width=True)

# Main content with enhanced tabs
if analyze_button:
    with st.spinner("🌌 Analyzing cosmic alignments..."):
        time.sleep(2)
    
    st.success("✨ **COSMIC ANALYSIS COMPLETE** - Your stellar blueprint has been decoded!")
    
    # Create enhanced tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🌟 Personal Profile", 
        "🪐 Current Positions", 
        "⏰ Planetary Cycles", 
        "🌊 Cosmic Transits", 
        "📅 Future Events"
    ])
    
    with tab1:
        st.markdown("""
        <div class="cosmic-panel">
            <h2 style="text-align: center; color: #ffffff; margin-bottom: 30px; font-family: 'Orbitron', monospace;">
                🌟 STELLAR IDENTITY MATRIX
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="cosmic-metric">
                <h3 style="color: #667eea; font-family: 'Space Grotesk', sans-serif;">👤 COSMIC NAME</h3>
                <p style="color: #ffffff; font-size: 1.3em; font-weight: 600;">{name}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="cosmic-metric">
                <h3 style="color: #667eea; font-family: 'Space Grotesk', sans-serif;">📅 BIRTH MATRIX</h3>
                <p style="color: #ffffff; font-size: 1.3em; font-weight: 600;">{birth_date.strftime('%B %d, %Y')}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="cosmic-metric">
                <h3 style="color: #667eea; font-family: 'Space Grotesk', sans-serif;">🕐 TIME PORTAL</h3>
                <p style="color: #ffffff; font-size: 1.3em; font-weight: 600;">{birth_time}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="cosmic-metric">
                <h3 style="color: #667eea; font-family: 'Space Grotesk', sans-serif;">📆 WEEKLY CYCLE</h3>
                <p style="color: #ffffff; font-size: 1.3em; font-weight: 600;">{birth_date.strftime('%A')}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            today = date.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            
            st.markdown(f"""
            <div class="cosmic-metric">
                <h3 style="color: #667eea; font-family: 'Space Grotesk', sans-serif;">🌍 COORDINATES</h3>
                <p style="color: #ffffff; font-size: 1.3em; font-weight: 600;">{birth_place}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="cosmic-metric">
                <h3 style="color: #667eea; font-family: 'Space Grotesk', sans-serif;">🎂 SOLAR ORBITS</h3>
                <p style="color: #ffffff; font-size: 1.3em; font-weight: 600;">{age} Years</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="cosmic-panel">
            <h2 style="text-align: center; color: #ffffff; margin-bottom: 30px; font-family: 'Orbitron', monospace;">
                🪐 REAL-TIME PLANETARY COORDINATES
            </h2>
            <p style="text-align: center; color: #cccccc; font-size: 1.1em;">August 7, 2025 - Current Celestial Positions</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Planetary positions data
        cosmic_planets = [
            {"planet": "☉ SOLAR CORE", "sign": "♋ Cancer", "degree": "20.76°", "nakshatra": "Ashlesha", "status": "good", "energy": "Life Force Amplification"},
            {"planet": "☽ LUNAR SATELLITE", "sign": "♐ Sagittarius", "degree": "24.88°", "nakshatra": "Purva Ashadha", "status": "good", "energy": "Intuitive Navigation"},
            {"planet": "☿ MERCURY PROBE", "sign": "♋ Cancer (R)", "degree": "10.93°", "nakshatra": "Pushya", "status": "challenging", "energy": "Communication Disruption"},
            {"planet": "♀ VENUS STATION", "sign": "♊ Gemini", "degree": "13.98°", "nakshatra": "Ardra", "status": "good", "energy": "Harmonic Resonance"},
            {"planet": "♂ MARS OUTPOST", "sign": "♍ Virgo", "degree": "5.94°", "nakshatra": "Uttara Phalguni", "status": "neutral", "energy": "Strategic Precision"},
            {"planet": "♃ JUPITER GIANT", "sign": "♊ Gemini", "degree": "18.81°", "nakshatra": "Ardra", "status": "good", "energy": "Wisdom Expansion"},
            {"planet": "♄ SATURN RINGS", "sign": "♓ Pisces (R)", "degree": "7.20°", "nakshatra": "Uttara Bhadrapada", "status": "neutral", "energy": "Karmic Recalibration"},
            {"planet": "☊ RAHU NODE", "sign": "♒ Aquarius (R)", "degree": "25.73°", "nakshatra": "Purva Bhadrapada", "status": "neutral", "energy": "Innovation Portal"},
            {"planet": "☋ KETU NODE", "sign": "♌ Leo (R)", "degree": "25.73°", "nakshatra": "Purva Phalguni", "status": "neutral", "energy": "Spiritual Liberation"}
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
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                    <h3 style="color: #ffffff; margin: 0; font-family: 'Space Grotesk', sans-serif;">{planet['planet']}</h3>
                    <span style="font-size: 1.4em;">{status_icon}</span>
                </div>
                <p style="color: #e0e0e0; margin: 8px 0; font-family: 'Inter', sans-serif;"><strong>Position:</strong> {planet['sign']} at {planet['degree']}</p>
                <p style="color: #e0e0e0; margin: 8px 0; font-family: 'Inter', sans-serif;"><strong>Star Formation:</strong> {planet['nakshatra']}</p>
                <p style="color: #e0e0e0; margin: 8px 0; font-family: 'Inter', sans-serif;"><strong>Energy:</strong> {planet['energy']}</p>
                <p style="margin: 12px 0 0 0; font-weight: 600; color: #ffffff;"><strong>Status:</strong> {status_text}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="cosmic-panel">
            <h2 style="text-align: center; color: #ffffff; margin-bottom: 30px; font-family: 'Orbitron', monospace;">
                ⏰ PLANETARY DOMINANCE CYCLES
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced Dasha calculation
        dasha_planets = ['Sun', 'Moon', 'Mars', 'Rahu', 'Jupiter', 'Saturn', 'Mercury', 'Ketu', 'Venus']
        dasha_years = [6, 10, 7, 18, 16, 19, 17, 7, 20]
        
        birth_datetime = datetime.combine(birth_date, birth_time)
        current_age = (datetime.now() - birth_datetime).days / 365.25
        
        # Find current dasha
        total_years = 0
        current_dasha = 'Sun'
        current_antardasha = 'Moon'
        years_left = 0
        
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
        
        col1, col2 = st.columns(2)
        
        with col1:
            planet_colors = {
                'Sun': '#ffd700', 'Moon': '#c0c0c0', 'Mars': '#ff6b6b', 'Mercury': '#48dbfb',
                'Jupiter': '#f39c12', 'Venus': '#ff9ff3', 'Saturn': '#3742fa', 'Rahu': '#8c7ae6', 'Ketu': '#ff7675'
            }
            
            main_color = planet_colors.get(current_dasha, '#667eea')
            sub_color = planet_colors.get(current_antardasha, '#764ba2')
            
            st.markdown(f"""
            <div class="cosmic-metric" style="border: 2px solid {main_color};">
                <h3 style="color: {main_color}; font-family: 'Space Grotesk', sans-serif;">🌟 MAIN RULER</h3>
                <p style="color: #ffffff; font-size: 2.2em; font-weight: bold; font-family: 'Orbitron', monospace;">{current_dasha}</p>
                <p style="color: #e0e0e0; font-size: 1em;">Primary cosmic influence</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="cosmic-metric" style="border: 2px solid {sub_color};">
                <h3 style="color: {sub_color}; font-family: 'Space Grotesk', sans-serif;">🌙 SUB RULER</h3>
                <p style="color: #ffffff; font-size: 2.2em; font-weight: bold; font-family: 'Orbitron', monospace;">{current_antardasha}</p>
                <p style="color: #e0e0e0; font-size: 1em;">Secondary energy pattern</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Enhanced status determination
            benefic_planets = ['Jupiter', 'Venus', 'Moon', 'Mercury']
            if current_dasha in benefic_planets:
                status_color = "#00d4aa"
                status_text = "🌟 HARMONY PHASE"
                status_desc = "Favorable alignments supporting growth and prosperity"
            elif current_dasha in ['Saturn', 'Mars', 'Rahu', 'Ketu']:
                status_color = "#ff6b6b"
                status_text = "⚡ CHALLENGE PHASE"
                status_desc = "Transformative period requiring wisdom and patience"
            else:
                status_color = "#feca57"
                status_text = "⚖️ BALANCE PHASE"
                status_desc = "Mixed energies creating learning opportunities"
            
            st.markdown(f"""
            <div class="cosmic-metric" style="border: 2px solid {status_color};">
                <h3 style="color: {status_color}; font-family: 'Space Grotesk', sans-serif;">📊 CURRENT STATUS</h3>
                <p style="color: #ffffff; font-size: 1.4em; font-weight: bold;">{status_text}</p>
                <p style="color: #e0e0e0; font-size: 0.95em; line-height: 1.4;">{status_desc}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="cosmic-metric">
                <h3 style="color: #764ba2; font-family: 'Space Grotesk', sans-serif;">⏳ TIME REMAINING</h3>
                <p style="color: #ffffff; font-size: 2em; font-weight: bold; font-family: 'Orbitron', monospace;">{years_left:.1f}</p>
                <p style="color: #e0e0e0; font-size: 1em;">Years until cosmic shift</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("""
        <div class="cosmic-panel">
            <h2 style="text-align: center; color: #ffffff; margin-bottom: 30px; font-family: 'Orbitron', monospace;">
                🌊 ACTIVE COSMIC WAVE PATTERNS
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        cosmic_transits = [
            ("☉ Solar Core in Cancer", "Deep emotional resonance - Family bond amplification", "good"),
            ("☽ Lunar Satellite in Sagittarius", "Spiritual elevation - Wisdom channel opening", "good"),
            ("☿ Mercury Probe RETROGRADE", "Communication disruption - System recalibration", "challenging"),
            ("♀ Venus Station in Gemini", "Social harmony - Creative enhancement", "good"),
            ("♂ Mars Outpost in Virgo", "Precision protocols - Strategic implementation", "good"),
            ("♃ Jupiter Giant in Gemini", "Knowledge expansion - Teaching transmission", "good"),
            ("♄ Saturn Rings RETROGRADE", "Karmic review - Spiritual integration", "neutral"),
            ("☊ Rahu Node in Aquarius", "Innovation portal - Revolutionary frequency", "neutral")
        ]
        
        for transit, effect, status in cosmic_transits:
            if status == "good":
                st.success(f"**🌟 {transit}:** {effect}")
            elif status == "challenging":
                st.error(f"**⚠️ {transit}:** {effect}")
            else:
                st.info(f"**🔮 {transit}:** {effect}")
    
    with tab5:
        st.markdown("""
        <div class="cosmic-panel">
            <h2 style="text-align: center; color: #ffffff; margin-bottom: 30px; font-family: 'Orbitron', monospace;">
                📅 COSMIC EVENTS TIMELINE
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        timeline_events = [
            ("August 11, 2025", "Mercury Systems Resume", "Communication restoration", "good"),
            ("August 17, 2025", "Solar Core → Leo", "Leadership activation", "neutral"),
            ("August 21, 2025", "Venus → Cancer", "Love amplification", "good"),
            ("September 1, 2025", "Saturn → Pisces", "Spiritual challenges", "challenging"),
            ("September 13, 2025", "Mars → Libra", "Diplomatic protocols", "neutral"),
            ("October 18, 2025", "Jupiter → Cancer", "Family prosperity surge", "good")
        ]
        
        for event_date, event_name, event_description, status in timeline_events:
            if status == "good":
                icon = "🟢"
                bg_color = "rgba(0, 212, 170, 0.15)"
                border_color = "#00d4aa"
            elif status == "challenging":
                icon = "🔴"
                bg_color = "rgba(255, 107, 107, 0.15)"
                border_color = "#ff6b6b"
            else:
                icon = "🟡"
                bg_color = "rgba(254, 202, 87, 0.15)"
                border_color = "#feca57"
            
            st.markdown(f"""
            <div style="background: {bg_color}; padding: 20px; border-radius: 15px; margin: 15px 0; 
                        border-left: 4px solid {border_color}; backdrop-filter: blur(10px);">
                <div style="display: flex; align-items: center; gap: 20px;">
                    <span style="font-size: 2em;">{icon}</span>
                    <div>
                        <h4 style="color: #ffffff; margin: 0; font-family: 'Space Grotesk', sans-serif; font-weight: 600;">
                            {event_date}: {event_name}
                        </h4>
                        <p style="color: #e0e0e0; margin: 8px 0 0 0; font-family: 'Inter', sans-serif;">
                            {event_description}
                        </p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="cosmic-panel">
            <h2 style="text-align: center; color: #ffffff; margin-bottom: 30px; font-family: 'Orbitron', monospace;">
                📊 COSMIC FORCE ANALYSIS
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        
        with metric_col1:
            st.markdown("""
            <div class="cosmic-metric" style="background: linear-gradient(135deg, rgba(0, 212, 170, 0.2), rgba(0, 200, 160, 0.1)); border: 2px solid #00d4aa;">
                <h3 style="color: #00d4aa; font-family: 'Space Grotesk', sans-serif;">🟢 FAVORABLE</h3>
                <p style="color: #ffffff; font-size: 3em; font-weight: bold; font-family: 'Orbitron', monospace;">6</p>
                <p style="color: #e0e0e0; font-size: 0.9em;">Positive cosmic forces</p>
            </div>
            """, unsafe_allow_html=True)
        
        with metric_col2:
            st.markdown("""
            <div class="cosmic-metric" style="background: linear-gradient(135deg, rgba(255, 107, 107, 0.2), rgba(255, 80, 80, 0.1)); border: 2px solid #ff6b6b;">
                <h3 style="color: #ff6b6b; font-family: 'Space Grotesk', sans-serif;">🔴 CHALLENGING</h3>
                <p style="color: #ffffff; font-size: 3em; font-weight: bold; font-family: 'Orbitron', monospace;">1</p>
                <p style="color: #e0e0e0; font-size: 0.9em;">Mercury retrograde only</p>
            </div>
            """, unsafe_allow_html=True)
        
        with metric_col3:
            st.markdown("""
            <div class="cosmic-metric" style="background: linear-gradient(135deg, rgba(254, 202, 87, 0.2), rgba(255, 165, 2, 0.1)); border: 2px solid #feca57;">
                <h3 style="color: #feca57; font-family: 'Space Grotesk', sans-serif;">🟡 NEUTRAL</h3>
                <p style="color: #ffffff; font-size: 3em; font-weight: bold; font-family: 'Orbitron', monospace;">4</p>
                <p style="color: #e0e0e0; font-size: 0.9em;">Balanced influences</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Recommendations
        st.markdown("---")
        
        rec_col1, rec_col2 = st.columns(2)
        
        with rec_col1:
            st.markdown("""
            <div class="planet-card planet-good">
                <h3 style="color: #00d4aa; margin-bottom: 20px; font-family: 'Space Grotesk', sans-serif;">✅ OPTIMAL ACTIVITIES</h3>
                <div style="color: #ffffff; line-height: 1.8; font-family: 'Inter', sans-serif;">
                    <p>🧘 <strong>Spiritual Practice:</strong> Meditation & inner exploration</p>
                    <p>👨‍👩‍👧‍👦 <strong>Family Bonds:</strong> Strengthen relationships & connections</p>
                    <p>🎨 <strong>Creative Work:</strong> Channel artistic energies</p>
                    <p>📚 <strong>Learning:</strong> Acquire new knowledge & skills</p>
                    <p>🌱 <strong>Growth:</strong> Plant seeds for future success</p>
                    <p>💖 <strong>Love Expression:</strong> Share positive energy</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with rec_col2:
            st.markdown("""
            <div class="planet-card planet-challenging">
                <h3 style="color: #ff6b6b; margin-bottom: 20px; font-family: 'Space Grotesk', sans-serif;">⚠️ CAUTION PROTOCOLS</h3>
                <div style="color: #ffffff; line-height: 1.8; font-family: 'Inter', sans-serif;">
                    <p>📡 <strong>Communications:</strong> Double-check all messages</p>
                    <p>💔 <strong>Major Decisions:</strong> Delay until August 12+</p>
                    <p>🔧 <strong>Technology:</strong> Backup data, avoid upgrades</p>
                    <p>✈️ <strong>Travel Plans:</strong> Confirm all arrangements</p>
                    <p>📝 <strong>Contracts:</strong> Review carefully before signing</p>
                    <p>⚡ <strong>Electronics:</strong> Expect potential glitches</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

else:
    # Enhanced Welcome Screen
    st.markdown("""
    <div class="cosmic-panel">
        <h2 style="text-align: center; color: #ffffff; font-family: 'Orbitron', monospace; margin-bottom: 20px;">
            🌌 WELCOME TO THE COSMIC INTELLIGENCE CENTER
        </h2>
        <p style="text-align: center; color: #e0e0e0; font-size: 1.3em; margin: 25px 0; font-family: 'Space Grotesk', sans-serif; line-height: 1.6;">
            Enter your cosmic coordinates in the sidebar and initiate your comprehensive stellar analysis
        </p>
        <div style="text-align: center; margin: 30px 0;">
            <div style="display: inline-block; background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2)); 
                        padding: 20px 40px; border-radius: 50px; border: 2px solid rgba(255, 255, 255, 0.3);">
                <span style="font-size: 1.2em; color: #ffffff; font-family: 'Space Grotesk', sans-serif;">
                    🚀 Ready for cosmic navigation
                </span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Current cosmic highlights
    st.markdown("""
    <div class="cosmic-panel">
        <h3 style="color: #667eea; text-align: center; margin-bottom: 25px; font-family: 'Space Grotesk', sans-serif;">
            🌟 CURRENT COSMIC CONDITIONS
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🔄 **Mercury Retrograde Active** | Communication systems require enhanced protocols")
    
    with col2:
        st.success("📚 **Jupiter in Gemini** | Optimal conditions for knowledge expansion")
    
    with col3:
        st.warning("🔄 **Multiple Retrogrades** | Perfect time for review & recalibration")

# Enhanced Footer
st.markdown("""
<div style="text-align: center; margin: 50px 0 30px 0; padding: 35px; 
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05)); 
            border-radius: 25px; backdrop-filter: blur(15px); border: 1px solid rgba(255, 255, 255, 0.2);">
    <h3 style="color: #667eea; margin-bottom: 15px; font-family: 'Orbitron', monospace;">
        🌌 COSMIC MISSION CONTROL
    </h3>
    <p style="color: #ffffff; font-size: 1.1em; font-family: 'Space Grotesk', sans-serif; margin-bottom: 10px;">
        Powered by Real Astronomical Data | Solar System Coordinates: August 7, 2025
    </p>
    <p style="color: #e0e0e0; font-family: 'Inter', sans-serif; font-size: 0.95em;">
        Advanced cosmic navigation utilizing precise astronomical calculations & ancient Vedic wisdom
    </p>
</div>
""", unsafe_allow_html=True)
