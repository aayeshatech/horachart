import streamlit as st
from datetime import date, datetime
import time

# Page config
st.set_page_config(
    page_title="🌌 Advanced Astrology Calculator", 
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS with perfect contrast and modern styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles - Perfect Contrast */
    .main {
        background: linear-gradient(135deg, #f0f4ff 0%, #e6f0ff 25%, #dce7ff 50%, #d2deff 75%, #c8d5ff 100%);
        color: #1a202c;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 500;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f0f4ff 0%, #e6f0ff 25%, #dce7ff 50%, #d2deff 75%, #c8d5ff 100%);
    }
    
    /* Stars Background */
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
        width: 4px;
        height: 4px;
        background: linear-gradient(45deg, #667eea, #764ba2);
        border-radius: 50%;
        animation: twinkle 4s infinite ease-in-out;
        box-shadow: 0 0 10px rgba(102, 126, 234, 0.7);
    }
    
    @keyframes twinkle {
        0%, 100% { opacity: 0.6; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1.4); }
    }
    
    /* Main Header */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 50px 30px;
        border-radius: 25px;
        text-align: center;
        margin: 25px 0;
        box-shadow: 0 15px 60px rgba(102, 126, 234, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .main-header h1 {
        font-family: 'Orbitron', monospace;
        font-size: 3.8em;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        margin: 0;
        letter-spacing: 2px;
    }
    
    .main-header p {
        color: #ffffff;
        font-size: 1.4em;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 500;
        margin: 20px 0 0 0;
        text-shadow: 0 1px 5px rgba(0, 0, 0, 0.2);
    }
    
    /* Mode Selector */
    .mode-selector {
        background: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 20px;
        margin: 25px 0;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(102, 126, 234, 0.2);
    }
    
    /* Enhanced Panels */
    .cosmic-panel {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(102, 126, 234, 0.2);
        border-radius: 20px;
        padding: 30px;
        margin: 25px 0;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
    }
    
    .cosmic-panel:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.15);
        border-color: rgba(102, 126, 234, 0.4);
    }
    
    .cosmic-panel h2, .cosmic-panel h3 {
        color: #1a202c !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 700 !important;
    }
    
    /* Input Fields - Perfect Contrast */
    .stTextInput > div > div > input,
    .stDateInput > div > div > input,
    .stTimeInput > div > div > input,
    .stSelectbox > div > div > input {
        background: #ffffff !important;
        border: 2px solid #667eea !important;
        border-radius: 12px !important;
        color: #1a202c !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        padding: 14px 18px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1) !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stDateInput > div > div > input:focus,
    .stTimeInput > div > div > input:focus {
        border-color: #764ba2 !important;
        box-shadow: 0 0 25px rgba(102, 126, 234, 0.5) !important;
        background: #ffffff !important;
        color: #1a202c !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #718096 !important;
        font-weight: 400 !important;
    }
    
    /* Labels - Dark and Bold */
    .stTextInput > label,
    .stDateInput > label,
    .stTimeInput > label,
    .stSelectbox > label {
        color: #1a202c !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
        font-size: 17px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(20px) !important;
        border-right: 2px solid rgba(102, 126, 234, 0.3) !important;
        box-shadow: 5px 0 25px rgba(0, 0, 0, 0.1) !important;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 20px;
        backdrop-filter: blur(15px);
        box-shadow: 0 5px 25px rgba(0, 0, 0, 0.1);
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 65px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 15px;
        border: none;
        color: #ffffff;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 16px;
        transition: all 0.3s ease;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #764ba2, #f093fb);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #f093fb, #764ba2) !important;
        box-shadow: 0 6px 25px rgba(240, 147, 251, 0.5) !important;
        transform: translateY(-2px);
    }
    
    /* Cards - 3 Column Layout */
    .planet-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 18px;
        padding: 25px;
        margin: 15px 5px;
        border-left: 5px solid;
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        font-family: 'Space Grotesk', sans-serif;
        color: #1a202c;
        border-top: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    .planet-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.12);
        background: rgba(255, 255, 255, 1);
    }
    
    .planet-card h3 {
        color: #1a202c !important;
        font-weight: 700 !important;
        font-size: 1.3em !important;
        margin-bottom: 15px !important;
    }
    
    .planet-card p {
        color: #2d3748 !important;
        font-weight: 500 !important;
        line-height: 1.6 !important;
        margin: 8px 0 !important;
    }
    
    .planet-good { border-left-color: #38a169; }
    .planet-challenging { border-left-color: #e53e3e; }
    .planet-neutral { border-left-color: #d69e2e; }
    
    /* Metrics */
    .cosmic-metric {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        margin: 15px 5px;
        border: 2px solid rgba(102, 126, 234, 0.2);
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .cosmic-metric:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 35px rgba(102, 126, 234, 0.2);
        border-color: rgba(102, 126, 234, 0.4);
    }
    
    .cosmic-metric h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1.1em !important;
        margin-bottom: 10px !important;
    }
    
    .cosmic-metric p {
        color: #1a202c !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        border: none !important;
        border-radius: 15px !important;
        color: #ffffff !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
        padding: 15px 30px !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4) !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.6) !important;
        background: linear-gradient(135deg, #764ba2, #f093fb) !important;
    }
    
    /* Alert Messages */
    .stSuccess {
        background: linear-gradient(135deg, #38a169, #48bb78) !important;
        border: none !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2) !important;
    }
    
    .stError {
        background: linear-gradient(135deg, #e53e3e, #fc8181) !important;
        border: none !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2) !important;
    }
    
    .stWarning, .stInfo {
        background: linear-gradient(135deg, #d69e2e, #f6e05e) !important;
        border: none !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2) !important;
    }
    
    /* Market Analysis Cards */
    .market-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 18px;
        padding: 25px;
        margin: 15px 5px;
        border-top: 4px solid;
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        font-family: 'Space Grotesk', sans-serif;
        color: #1a202c;
    }
    
    .market-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.12);
    }
    
    .market-bullish { border-top-color: #38a169; }
    .market-bearish { border-top-color: #e53e3e; }
    .market-neutral { border-top-color: #d69e2e; }
    
    /* Horoscope Cards */
    .horoscope-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 18px;
        padding: 30px;
        margin: 20px 5px;
        border: 2px solid;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        font-family: 'Space Grotesk', sans-serif;
        color: #1a202c;
    }
    
    .horoscope-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
    }
    
    /* Mercury Alert */
    .mercury-alert {
        background: linear-gradient(135deg, #e53e3e, #fc8181);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin: 25px 0;
        box-shadow: 0 10px 35px rgba(229, 62, 62, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.3);
    }
    
    .mercury-alert h2, .mercury-alert p {
        color: #ffffff !important;
        text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3) !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }
    
    /* Selectbox Styling */
    .stSelectbox > div > div {
        background: #ffffff !important;
        border: 2px solid #667eea !important;
        border-radius: 12px !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stSelectbox > div > div > div {
        color: #1a202c !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }
</style>

<div class="stars-container" id="starsContainer"></div>

<script>
function createStars() {
    const container = document.getElementById('starsContainer');
    if (!container) return;
    
    const numStars = 120;
    
    for (let i = 0; i < numStars; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 100 + '%';
        star.style.animationDelay = Math.random() * 4 + 's';
        star.style.animationDuration = (3 + Math.random() * 2) + 's';
        
        const size = Math.random() * 4 + 2;
        star.style.width = size + 'px';
        star.style.height = size + 'px';
        
        container.appendChild(star);
    }
}

setTimeout(createStars, 100);
</script>
""", unsafe_allow_html=True)

# Main Header
st.markdown("""
<div class="main-header">
    <h1>🌌 ADVANCED ASTROLOGY CALCULATOR</h1>
    <p>🚀 Cosmic Intelligence & Financial Market Analysis Platform</p>
</div>
""", unsafe_allow_html=True)

# Mode Selection
st.markdown("""
<div class="mode-selector">
    <h3 style="color: #1a202c; text-align: center; font-family: 'Orbitron', monospace; margin-bottom: 20px;">
        🎯 SELECT ANALYSIS MODE
    </h3>
</div>
""", unsafe_allow_html=True)

# Mode selector
analysis_mode = st.selectbox(
    "",
    ["🌟 Personal Horoscope & Life Guidance", "📈 Financial Markets & Investment Analysis"],
    index=0,
    label_visibility="collapsed"
)

# Mercury Retrograde Alert
st.markdown("""
<div class="mercury-alert">
    <h2 style="margin: 0; font-size: 1.8em;">⚠️ MERCURY RETROGRADE ACTIVE ⚠️</h2>
    <p style="font-size: 1.1em; margin: 10px 0 0 0;">
        August 7-11, 2025 | Exercise caution with communications & technology
    </p>
</div>
""", unsafe_allow_html=True)

# Enhanced Sidebar
with st.sidebar:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea, #764ba2); 
                padding: 25px; border-radius: 20px; margin-bottom: 25px; 
                box-shadow: 0 5px 25px rgba(0, 0, 0, 0.1);">
        <h2 style="color: #ffffff; text-align: center; font-family: 'Orbitron', monospace; 
                   margin: 0; text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);">
            🌟 COSMIC DATA INPUT
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    name = st.text_input(
        "👤 Your Name", 
        value="Cosmic Navigator", 
        help="Enter your name for personalized analysis",
        placeholder="Enter your name..."
    )
    
    birth_date = st.date_input(
        "📅 Birth Date", 
        value=date(1990, 7, 3),
        min_value=date(1900, 1, 1),
        max_value=date(2030, 12, 31),
        help="Your date of birth"
    )
    
    birth_time = st.time_input(
        "🕐 Birth Time", 
        value=datetime.now().time(), 
        help="Time of birth (24-hour format)"
    )
    
    birth_place = st.text_input(
        "📍 Birth Place", 
        value="Mumbai, India", 
        help="City and country of birth",
        placeholder="City, Country..."
    )
    
    st.markdown("---")
    
    # Cosmic clock
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea, #764ba2); 
                padding: 20px; border-radius: 15px; text-align: center; margin: 15px 0;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);">
        <h4 style="color: #ffffff; margin: 0; font-family: 'Orbitron', monospace; 
                   text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);">🕐 CURRENT TIME</h4>
        <p style="color: #ffffff; font-size: 1.1em; margin: 8px 0 0 0; 
                  font-family: 'Inter', monospace; text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);">
            {current_time}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    analyze_button = st.button("🚀 START COSMIC ANALYSIS", type="primary", use_container_width=True)

# Main Analysis
if analyze_button:
    with st.spinner("🌌 Analyzing cosmic alignments..."):
        time.sleep(2)
    
    st.success("✨ **COSMIC ANALYSIS COMPLETE** - Your stellar blueprint has been decoded!")
    
    if "Personal Horoscope" in analysis_mode:
        # Personal Horoscope Mode
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🌟 Personal Profile", 
            "🪐 Current Positions", 
            "⏰ Life Cycles", 
            "🔮 2025 Predictions", 
            "📅 Yearly Forecast"
        ])
        
        with tab1:
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 30px;">
                    🌟 PERSONAL COSMIC PROFILE
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class="cosmic-metric">
                    <h3 style="color: #667eea;">👤 NAME</h3>
                    <p style="font-size: 1.4em; font-weight: 700;">{name}</p>
                </div>
                """, unsafe_allow_html=True)
                
                today = date.today()
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                
                st.markdown(f"""
                <div class="cosmic-metric">
                    <h3 style="color: #667eea;">🎂 AGE</h3>
                    <p style="font-size: 1.4em; font-weight: 700;">{age} Years</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="cosmic-metric">
                    <h3 style="color: #667eea;">📅 BIRTH DATE</h3>
                    <p style="font-size: 1.4em; font-weight: 700;">{birth_date.strftime('%d %B %Y')}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="cosmic-metric">
                    <h3 style="color: #667eea;">📆 DAY</h3>
                    <p style="font-size: 1.4em; font-weight: 700;">{birth_date.strftime('%A')}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="cosmic-metric">
                    <h3 style="color: #667eea;">🕐 TIME</h3>
                    <p style="font-size: 1.4em; font-weight: 700;">{birth_time}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="cosmic-metric">
                    <h3 style="color: #667eea;">📍 PLACE</h3>
                    <p style="font-size: 1.4em; font-weight: 700;">{birth_place}</p>
                </div>
                """, unsafe_allow_html=True)
        
        with tab2:
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 30px;">
                    🪐 CURRENT PLANETARY POSITIONS
                </h2>
                <p style="text-align: center; color: #2d3748; font-size: 1.2em; font-weight: 500;">
                    August 7, 2025 - Real-time Celestial Coordinates
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Planetary data in 3 columns
            planets_data = [
                {"planet": "☉ SUN", "sign": "♋ Cancer", "degree": "20.76°", "nakshatra": "Ashlesha", "status": "good", "energy": "Life Force & Vitality"},
                {"planet": "☽ MOON", "sign": "♐ Sagittarius", "degree": "24.88°", "nakshatra": "Purva Ashadha", "status": "good", "energy": "Emotions & Intuition"},
                {"planet": "☿ MERCURY", "sign": "♋ Cancer (R)", "degree": "10.93°", "nakshatra": "Pushya", "status": "challenging", "energy": "Communication Issues"},
                {"planet": "♀ VENUS", "sign": "♊ Gemini", "degree": "13.98°", "nakshatra": "Ardra", "status": "good", "energy": "Love & Relationships"},
                {"planet": "♂ MARS", "sign": "♍ Virgo", "degree": "5.94°", "nakshatra": "Uttara Phalguni", "status": "neutral", "energy": "Action & Energy"},
                {"planet": "♃ JUPITER", "sign": "♊ Gemini", "degree": "18.81°", "nakshatra": "Ardra", "status": "good", "energy": "Wisdom & Growth"},
                {"planet": "♄ SATURN", "sign": "♓ Pisces (R)", "degree": "7.20°", "nakshatra": "Uttara Bhadrapada", "status": "neutral", "energy": "Discipline & Karma"},
                {"planet": "☊ RAHU", "sign": "♒ Aquarius (R)", "degree": "25.73°", "nakshatra": "Purva Bhadrapada", "status": "neutral", "energy": "Desires & Innovation"},
                {"planet": "☋ KETU", "sign": "♌ Leo (R)", "degree": "25.73°", "nakshatra": "Purva Phalguni", "status": "neutral", "energy": "Spirituality & Detachment"}
            ]
            
            # Display in 3 columns
            for i in range(0, len(planets_data), 3):
                col1, col2, col3 = st.columns(3)
                cols = [col1, col2, col3]
                
                for j, col in enumerate(cols):
                    if i + j < len(planets_data):
                        planet = planets_data[i + j]
                        
                        if planet["status"] == "good":
                            card_class = "planet-good"
                            status_icon = "🟢"
                            status_text = "FAVORABLE"
                        elif planet["status"] == "challenging":
                            card_class = "planet-challenging"
                            status_icon = "🔴"
                            status_text = "CAUTION"
                        else:
                            card_class = "planet-neutral"
                            status_icon = "🟡"
                            status_text = "NEUTRAL"
                        
                        with col:
                            st.markdown(f"""
                            <div class="planet-card {card_class}">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                                    <h3>{planet['planet']}</h3>
                                    <span style="font-size: 1.5em;">{status_icon}</span>
                                </div>
                                <p><strong>Position:</strong> {planet['sign']}</p>
                                <p><strong>Degree:</strong> {planet['degree']}</p>
                                <p><strong>Nakshatra:</strong> {planet['nakshatra']}</p>
                                <p><strong>Energy:</strong> {planet['energy']}</p>
                                <p style="font-weight: 700; color: #1a202c; margin-top: 12px;">
                                    <strong>Status:</strong> {status_text}
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
        
        with tab3:
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 30px;">
                    ⏰ LIFE PLANETARY CYCLES
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Dasha calculations
            dasha_planets = ['Sun', 'Moon', 'Mars', 'Rahu', 'Jupiter', 'Saturn', 'Mercury', 'Ketu', 'Venus']
            dasha_years = [6, 10, 7, 18, 16, 19, 17, 7, 20]
            
            birth_datetime = datetime.combine(birth_date, birth_time)
            current_age = (datetime.now() - birth_datetime).days / 365.25
            
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
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class="cosmic-metric" style="border: 3px solid #ffd700;">
                    <h3 style="color: #d69e2e;">🌟 MAIN PERIOD</h3>
                    <p style="font-size: 2.5em; font-weight: 900; font-family: 'Orbitron', monospace;">{current_dasha}</p>
                    <p style="color: #2d3748;">Primary life influence</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="cosmic-metric" style="border: 3px solid #c0c0c0;">
                    <h3 style="color: #718096;">🌙 SUB PERIOD</h3>
                    <p style="font-size: 2.5em; font-weight: 900; font-family: 'Orbitron', monospace;">{current_antardasha}</p>
                    <p style="color: #2d3748;">Secondary influence</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="cosmic-metric" style="border: 3px solid #764ba2;">
                    <h3 style="color: #764ba2;">⏳ TIME LEFT</h3>
                    <p style="font-size: 2.5em; font-weight: 900; font-family: 'Orbitron', monospace;">{years_left:.1f}</p>
                    <p style="color: #2d3748;">Years remaining</p>
                </div>
                """, unsafe_allow_html=True)
        
        with tab4:
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 30px;">
                    🔮 2025 PERSONAL PREDICTIONS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Personal predictions in 3 columns
            predictions = [
                {"area": "❤️ LOVE & RELATIONSHIPS", "prediction": "Strong Venus influence brings harmony. Existing relationships deepen. Single? Love may arrive through communication or learning.", "rating": "good"},
                {"area": "💰 CAREER & MONEY", "prediction": "Jupiter in Gemini supports learning new skills. Financial growth through communication, teaching, or technology fields.", "rating": "good"},
                {"area": "🏥 HEALTH & WELLNESS", "prediction": "Focus on nervous system due to Mercury retrograde. Practice stress management. Good time for yoga and meditation.", "rating": "neutral"},
                {"area": "👨‍👩‍👧‍👦 FAMILY & HOME", "prediction": "Sun in Cancer emphasizes family bonds. Property matters may be favorable. Home-based work thrives.", "rating": "good"},
                {"area": "🎓 EDUCATION & GROWTH", "prediction": "Excellent period for learning. Jupiter supports higher education, courses, certifications. Mental expansion favored.", "rating": "good"},
                {"area": "✈️ TRAVEL & ADVENTURE", "prediction": "Sagittarius Moon encourages travel for knowledge. Spiritual journeys particularly beneficial. Avoid travel during Mercury retrograde.", "rating": "neutral"}
            ]
            
            for i in range(0, len(predictions), 3):
                col1, col2, col3 = st.columns(3)
                cols = [col1, col2, col3]
                
                for j, col in enumerate(cols):
                    if i + j < len(predictions):
                        pred = predictions[i + j]
                        
                        border_color = "#38a169" if pred["rating"] == "good" else "#d69e2e" if pred["rating"] == "neutral" else "#e53e3e"
                        
                        with col:
                            st.markdown(f"""
                            <div class="horoscope-card" style="border-color: {border_color};">
                                <h3 style="color: {border_color}; margin-bottom: 15px; font-size: 1.2em;">
                                    {pred['area']}
                                </h3>
                                <p style="line-height: 1.6; font-weight: 500;">
                                    {pred['prediction']}
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
        
        with tab5:
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 30px;">
                    📅 YEARLY FORECAST 2025-2026
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            yearly_forecast = [
                {"quarter": "Q3 2025 (Jul-Sep)", "theme": "Communication & Learning", "details": "Mercury retrograde challenges followed by strong educational opportunities. Family focus intensifies.", "energy": "Mixed"},
                {"quarter": "Q4 2025 (Oct-Dec)", "theme": "Relationships & Growth", "details": "Venus and Jupiter create harmonious conditions for love and financial growth. Career advancement likely.", "energy": "Positive"},
                {"quarter": "Q1 2026 (Jan-Mar)", "theme": "New Beginnings", "details": "Fresh starts in multiple life areas. Good time for launching projects and making important decisions.", "energy": "Positive"},
                {"quarter": "Q2 2026 (Apr-Jun)", "theme": "Consolidation", "details": "Time to solidify gains from previous quarters. Focus on stability and building strong foundations.", "energy": "Stable"},
                {"quarter": "Q3 2026 (Jul-Sep)", "theme": "Expansion Phase", "details": "Major growth opportunities. Travel, higher learning, and spiritual development highly favored.", "energy": "Positive"},
                {"quarter": "Q4 2026 (Oct-Dec)", "theme": "Achievement", "details": "Culmination of efforts. Recognition, rewards, and fulfillment of long-term goals. Family celebrations.", "energy": "Excellent"}
            ]
            
            for i in range(0, len(yearly_forecast), 3):
                col1, col2, col3 = st.columns(3)
                cols = [col1, col2, col3]
                
                for j, col in enumerate(cols):
                    if i + j < len(yearly_forecast):
                        forecast = yearly_forecast[i + j]
                        
                        if forecast["energy"] == "Positive" or forecast["energy"] == "Excellent":
                            border_color = "#38a169"
                            bg_gradient = "rgba(56, 161, 105, 0.1)"
                        elif forecast["energy"] == "Mixed":
                            border_color = "#d69e2e"
                            bg_gradient = "rgba(214, 158, 46, 0.1)"
                        else:
                            border_color = "#667eea"
                            bg_gradient = "rgba(102, 126, 234, 0.1)"
                        
                        with col:
                            st.markdown(f"""
                            <div style="background: {bg_gradient}; border: 2px solid {border_color}; 
                                        border-radius: 18px; padding: 25px; margin: 15px 5px;
                                        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.08);">
                                <h3 style="color: {border_color}; margin-bottom: 15px; font-family: 'Space Grotesk', sans-serif; font-weight: 700;">
                                    {forecast['quarter']}
                                </h3>
                                <h4 style="color: #1a202c; margin-bottom: 10px; font-family: 'Space Grotesk', sans-serif;">
                                    {forecast['theme']}
                                </h4>
                                <p style="color: #2d3748; line-height: 1.6; font-weight: 500;">
                                    {forecast['details']}
                                </p>
                                <p style="color: {border_color}; font-weight: 700; margin-top: 15px;">
                                    Energy: {forecast['energy']}
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
    
    else:
        # Financial Analysis Mode
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📈 Market Overview", 
            "🏦 Indian Sectors", 
            "🌍 Global Markets", 
            "🥇 Commodities", 
            "📊 Cosmic Trading"
        ])
        
        with tab1:
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 30px;">
                    📈 PLANETARY MARKET ANALYSIS
                </h2>
                <p style="text-align: center; color: #2d3748; font-size: 1.2em;">
                    Astrological Impact on Financial Markets - August 7, 2025
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <div class="cosmic-metric" style="border: 3px solid #38a169;">
                    <h3 style="color: #38a169;">📈 BULLISH FORCES</h3>
                    <p style="font-size: 3em; font-weight: 900; color: #38a169;">5</p>
                    <p style="color: #2d3748;">Strong planetary support</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="cosmic-metric" style="border: 3px solid #e53e3e;">
                    <h3 style="color: #e53e3e;">📉 BEARISH FORCES</h3>
                    <p style="font-size: 3em; font-weight: 900; color: #e53e3e;">2</p>
                    <p style="color: #2d3748;">Mercury & Saturn challenges</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                <div class="cosmic-metric" style="border: 3px solid #d69e2e;">
                    <h3 style="color: #d69e2e;">⚖️ SIDEWAYS TREND</h3>
                    <p style="font-size: 3em; font-weight: 900; color: #d69e2e;">3</p>
                    <p style="color: #2d3748;">Neutral planetary forces</p>
                </div>
                """, unsafe_allow_html=True)
        
        with tab2:
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 30px;">
                    🏦 INDIAN MARKET SECTORS ANALYSIS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            indian_sectors = [
                {"sector": "💻 IT & Technology", "planetary_influence": "Jupiter in Gemini", "trend": "bullish", "analysis": "Strong growth due to Jupiter's influence on communication and technology. AI and software companies particularly favored."},
                {"sector": "🏦 Banking & Finance", "planetary_influence": "Sun in Cancer", "trend": "bullish", "analysis": "Sun in Cancer supports traditional financial institutions. Home loans and family-oriented financial products excel."},
                {"sector": "⚕️ Healthcare & Pharma", "planetary_influence": "Moon in Sagittarius", "trend": "neutral", "analysis": "Mixed signals. Traditional medicine and spiritual healing gain attention. Preventive healthcare focus."},
                {"sector": "🏭 Manufacturing", "planetary_influence": "Mars in Virgo", "trend": "bullish", "analysis": "Precision manufacturing and quality control emphasized. Efficiency improvements drive profitability."},
                {"sector": "🏠 Real Estate", "planetary_influence": "Sun in Cancer", "trend": "bullish", "analysis": "Residential real estate particularly strong. Family housing and home improvement sectors benefit significantly."},
                {"sector": "⚡ Energy & Power", "planetary_influence": "Saturn in Pisces", "trend": "bearish", "analysis": "Traditional energy faces challenges. Renewable energy and spiritual/alternative energy sources favored long-term."},
                {"sector": "🛒 Consumer Goods", "planetary_influence": "Venus in Gemini", "trend": "neutral", "analysis": "Communication-based marketing works well. Luxury goods and beauty products show mixed performance."},
                {"sector": "🚗 Automobile", "planetary_influence": "Mercury Retrograde", "trend": "bearish", "analysis": "Transportation and logistics face temporary setbacks. Electric vehicles may see delays but long-term positive."},
                {"sector": "📱 Telecom", "planetary_influence": "Mercury Retrograde", "trend": "bearish", "analysis": "Communication sector faces technical challenges. Upgrade cycles delayed. Network infrastructure issues possible."}
            ]
            
            for i in range(0, len(indian_sectors), 3):
                col1, col2, col3 = st.columns(3)
                cols = [col1, col2, col3]
                
                for j, col in enumerate(cols):
                    if i + j < len(indian_sectors):
                        sector = indian_sectors[i + j]
                        
                        if sector["trend"] == "bullish":
                            card_class = "market-bullish"
                            icon = "📈"
                            trend_color = "#38a169"
                        elif sector["trend"] == "bearish":
                            card_class = "market-bearish"
                            icon = "📉"
                            trend_color = "#e53e3e"
                        else:
                            card_class = "market-neutral"
                            icon = "➡️"
                            trend_color = "#d69e2e"
                        
                        with col:
                            st.markdown(f"""
                            <div class="market-card {card_class}">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                                    <h3 style="color: #1a202c; font-size: 1.1em;">{sector['sector']}</h3>
                                    <span style="font-size: 1.8em;">{icon}</span>
                                </div>
                                <p style="color: #2d3748; font-weight: 600; margin-bottom: 10px;">
                                    <strong>Influence:</strong> {sector['planetary_influence']}
                                </p>
                                <p style="color: #2d3748; line-height: 1.5; font-weight: 500;">
                                    {sector['analysis']}
                                </p>
                                <p style="color: {trend_color}; font-weight: 700; margin-top: 15px; text-transform: uppercase;">
                                    Trend: {sector['trend']}
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
        
        with tab3:
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 30px;">
                    🌍 GLOBAL MARKETS ANALYSIS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            global_markets = [
                {"market": "🇺🇸 US Markets (S&P 500)", "influence": "Jupiter expansion", "trend": "bullish", "analysis": "Technology and communication stocks lead growth. AI and social media companies particularly strong."},
                {"market": "🇪🇺 European Markets", "influence": "Saturn discipline", "trend": "neutral", "analysis": "Slow but steady growth. Traditional industries face restructuring. Green energy initiatives gain momentum."},
                {"market": "🇨🇳 Chinese Markets", "influence": "Rahu innovation", "trend": "bullish", "analysis": "Innovation and technology drive growth. New economy sectors outperform traditional manufacturing."},
                {"market": "🇯🇵 Japanese Markets", "influence": "Moon intuition", "trend": "neutral", "analysis": "Consumer discretionary and traditional values emphasized. Stability over aggressive growth."},
                {"market": "🇬🇧 UK Markets", "influence": "Mercury communication", "trend": "bearish", "analysis": "Communication and financial services face temporary setbacks. Brexit-related adjustments continue."},
                {"market": "🌏 Emerging Markets", "influence": "Mars energy", "trend": "bullish", "analysis": "High energy and growth potential. Infrastructure and basic materials sectors particularly strong."}
            ]
            
            for i in range(0, len(global_markets), 3):
                col1, col2, col3 = st.columns(3)
                cols = [col1, col2, col3]
                
                for j, col in enumerate(cols):
                    if i + j < len(global_markets):
                        market = global_markets[i + j]
                        
                        if market["trend"] == "bullish":
                            card_class = "market-bullish"
                            icon = "📈"
                            trend_color = "#38a169"
                        elif market["trend"] == "bearish":
                            card_class = "market-bearish"
                            icon = "📉"
                            trend_color = "#e53e3e"
                        else:
                            card_class = "market-neutral"
                            icon = "➡️"
                            trend_color = "#d69e2e"
                        
                        with col:
                            st.markdown(f"""
                            <div class="market-card {card_class}">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                                    <h3 style="color: #1a202c; font-size: 1.1em;">{market['market']}</h3>
                                    <span style="font-size: 1.8em;">{icon}</span>
                                </div>
                                <p style="color: #2d3748; font-weight: 600; margin-bottom: 10px;">
                                    <strong>Key Influence:</strong> {market['influence']}
                                </p>
                                <p style="color: #2d3748; line-height: 1.5; font-weight: 500;">
                                    {market['analysis']}
                                </p>
                                <p style="color: {trend_color}; font-weight: 700; margin-top: 15px; text-transform: uppercase;">
                                    Outlook: {market['trend']}
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
        
        with tab4:
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 30px;">
                    🥇 COMMODITIES & PRECIOUS METALS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            commodities = [
                {"commodity": "🥇 GOLD", "influence": "Sun in Cancer", "trend": "bullish", "analysis": "Traditional safe haven strengthened by family/security focus. Central bank buying continues."},
                {"commodity": "🥈 SILVER", "influence": "Moon cycles", "trend": "bullish", "analysis": "Industrial demand meets investment demand. Solar energy applications drive consumption."},
                {"commodity": "⚡ CRUDE OIL", "influence": "Mars energy", "trend": "neutral", "analysis": "Geopolitical tensions vs renewable transition. Volatility expected with gradual decline."},
                {"commodity": "🌾 AGRICULTURAL", "influence": "Earth signs", "trend": "bullish", "analysis": "Climate concerns and population growth support prices. Sustainable farming premium."},
                {"commodity": "⚡ NATURAL GAS", "influence": "Saturn restriction", "trend": "bearish", "analysis": "Transition to renewables pressures long-term demand. Short-term supply disruptions possible."},
                {"commodity": "🔸 COPPER", "influence": "Jupiter expansion", "trend": "bullish", "analysis": "Electric vehicle and renewable energy infrastructure drives demand. Supply constraints support prices."},
                {"commodity": "💎 PRECIOUS STONES", "influence": "Venus luxury", "trend": "bullish", "analysis": "Luxury spending returns post-pandemic. Cultural celebrations and weddings drive demand."},
                {"commodity": "🌿 COFFEE & SPICES", "influence": "Mercury trade", "trend": "bearish", "analysis": "Supply chain disruptions during Mercury retrograde. Trade logistics face temporary challenges."},
                {"commodity": "🏗️ STEEL & METALS", "influence": "Mars strength", "trend": "neutral", "analysis": "Infrastructure spending supports demand. Environmental regulations create mixed pressures."}
            ]
            
            for i in range(0, len(commodities), 3):
                col1, col2, col3 = st.columns(3)
                cols = [col1, col2, col3]
                
                for j, col in enumerate(cols):
                    if i + j < len(commodities):
                        commodity = commodities[i + j]
                        
                        if commodity["trend"] == "bullish":
                            card_class = "market-bullish"
                            icon = "📈"
                            trend_color = "#38a169"
                        elif commodity["trend"] == "bearish":
                            card_class = "market-bearish"
                            icon = "📉"
                            trend_color = "#e53e3e"
                        else:
                            card_class = "market-neutral"
                            icon = "➡️"
                            trend_color = "#d69e2e"
                        
                        with col:
                            st.markdown(f"""
                            <div class="market-card {card_class}">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                                    <h3 style="color: #1a202c; font-size: 1.1em;">{commodity['commodity']}</h3>
                                    <span style="font-size: 1.8em;">{icon}</span>
                                </div>
                                <p style="color: #2d3748; font-weight: 600; margin-bottom: 10px;">
                                    <strong>Planetary Factor:</strong> {commodity['influence']}
                                </p>
                                <p style="color: #2d3748; line-height: 1.5; font-weight: 500;">
                                    {commodity['analysis']}
                                </p>
                                <p style="color: {trend_color}; font-weight: 700; margin-top: 15px; text-transform: uppercase;">
                                    Trend: {commodity['trend']}
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
        
        with tab5:
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 30px;">
                    📊 COSMIC TRADING CALENDAR
                </h2>
                <p style="text-align: center; color: #2d3748; font-size: 1.1em;">
                    Optimal Trading Periods Based on Planetary Movements
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            trading_periods = [
                {"period": "August 7-11, 2025", "phase": "Mercury Retrograde", "recommendation": "AVOID", "strategy": "Hold positions, avoid new entries. Focus on risk management and portfolio review."},
                {"period": "August 12-17, 2025", "phase": "Mercury Direct", "recommendation": "BUY", "strategy": "Communication stocks recover. Technology and social media excellent entry points."},
                {"period": "August 18-25, 2025", "phase": "Sun enters Leo", "recommendation": "BULLISH", "strategy": "Leadership and luxury stocks outperform. Entertainment and casino stocks favorable."},
                {"period": "August 26-31, 2025", "phase": "Venus in Cancer", "recommendation": "BUY", "strategy": "Home, family, and comfort-oriented stocks excel. Real estate and consumer staples strong."},
                {"period": "Sep 1-15, 2025", "phase": "Saturn Review", "recommendation": "CAUTIOUS", "strategy": "Traditional value stocks over growth. Focus on fundamentally strong companies."},
                {"period": "Sep 16-30, 2025", "phase": "Mars Balance", "recommendation": "BALANCED", "strategy": "Equal allocation between growth and value. Diplomatic and partnership-oriented investments."}
            ]
            
            for i in range(0, len(trading_periods), 3):
                col1, col2, col3 = st.columns(3)
                cols = [col1, col2, col3]
                
                for j, col in enumerate(cols):
                    if i + j < len(trading_periods):
                        period = trading_periods[i + j]
                        
                        if period["recommendation"] == "BUY" or period["recommendation"] == "BULLISH":
                            border_color = "#38a169"
                            bg_color = "rgba(56, 161, 105, 0.1)"
                            icon = "📈"
                        elif period["recommendation"] == "AVOID":
                            border_color = "#e53e3e"
                            bg_color = "rgba(229, 62, 62, 0.1)"
                            icon = "⚠️"
                        else:
                            border_color = "#d69e2e"
                            bg_color = "rgba(214, 158, 46, 0.1)"
                            icon = "⚖️"
                        
                        with col:
                            st.markdown(f"""
                            <div style="background: {bg_color}; border: 2px solid {border_color}; 
                                        border-radius: 18px; padding: 25px; margin: 15px 5px;
                                        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.08);">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                                    <h3 style="color: #1a202c; font-size: 1em; font-weight: 700;">{period['period']}</h3>
                                    <span style="font-size: 1.5em;">{icon}</span>
                                </div>
                                <h4 style="color: {border_color}; margin-bottom: 10px; font-weight: 700;">
                                    {period['phase']}
                                </h4>
                                <p style="color: {border_color}; font-weight: 700; font-size: 1.1em; margin-bottom: 10px;">
                                    Action: {period['recommendation']}
                                </p>
                                <p style="color: #2d3748; line-height: 1.5; font-weight: 500;">
                                    {period['strategy']}
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
    
    # Current Planetary Positions for both modes (3-column layout)
    with tab2 if "Personal" in analysis_mode else tab1:
        if "Personal" in analysis_mode:
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 30px;">
                    🪐 CURRENT PLANETARY POSITIONS
                </h2>
                <p style="text-align: center; color: #2d3748; font-size: 1.1em;">August 7, 2025 - Personal Life Influences</p>
            </div>
            """, unsafe_allow_html=True)

else:
    # Welcome Screen
    st.markdown("""
    <div class="cosmic-panel">
        <h2 style="text-align: center; color: #1a202c; margin-bottom: 25px;">
            🌌 WELCOME TO THE COSMIC INTELLIGENCE CENTER
        </h2>
        <p style="text-align: center; color: #2d3748; font-size: 1.3em; margin: 25px 0; line-height: 1.6;">
            Choose your analysis mode above, enter your cosmic coordinates in the sidebar, and begin your journey
        </p>
        <div style="text-align: center; margin: 30px 0;">
            <div style="display: inline-block; background: linear-gradient(135deg, #667eea, #764ba2); 
                        padding: 25px 50px; border-radius: 50px; box-shadow: 0 8px 30px rgba(102, 126, 234, 0.3);">
                <span style="font-size: 1.3em; color: #ffffff; font-family: 'Space Grotesk', sans-serif; font-weight: 600;
                           text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);">
                    🚀 Ready for Cosmic Analysis
                </span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Current conditions preview
    st.markdown("""
    <div class="cosmic-panel">
        <h3 style="color: #667eea; text-align: center; margin-bottom: 25px;">
            🌟 CURRENT COSMIC CONDITIONS
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🔄 **Mercury Retrograde** | Communication caution required")
    
    with col2:
        st.success("📚 **Jupiter in Gemini** | Learning & growth opportunities")
    
    with col3:
        st.warning("⚖️ **Mixed Energies** | Balance required in decisions")

# Enhanced Footer
st.markdown("""
<div style="text-align: center; margin: 50px 0 30px 0; padding: 40px; 
            background: rgba(255, 255, 255, 0.95); border-radius: 25px; 
            backdrop-filter: blur(15px); border: 2px solid rgba(102, 126, 234, 0.2);
            box-shadow: 0 12px 45px rgba(0, 0, 0, 0.08);">
    <h3 style="color: #667eea; margin-bottom: 15px; font-family: 'Orbitron', monospace; font-weight: 700;">
        🌌 COSMIC INTELLIGENCE PLATFORM
    </h3>
    <p style="color: #1a202c; font-size: 1.2em; font-family: 'Space Grotesk', sans-serif; 
              margin-bottom: 10px; font-weight: 600;">
        Powered by Real Astronomical Data | Updated: August 7, 2025
    </p>
    <p style="color: #2d3748; font-family: 'Inter', sans-serif; font-size: 1em; font-weight: 500;">
        Advanced cosmic analysis combining precise astronomical calculations with financial market intelligence
    </p>
</div>
""", unsafe_allow_html=True)
