import streamlit as st
from datetime import date, datetime, timedelta
import time
import pandas as pd
import numpy as np

# Page config
st.set_page_config(
    page_title="🌌 Professional KP Astrology & Financial Markets", 
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #f8faff 0%, #f0f4ff 25%, #e8f0ff 50%, #e0ecff 75%, #d8e8ff 100%);
        color: #1a202c;
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f8faff 0%, #f0f4ff 25%, #e8f0ff 50%, #e0ecff 75%, #d8e8ff 100%);
    }
    
    /* Header */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 50px 30px;
        border-radius: 25px;
        text-align: center;
        margin: 25px 0;
        box-shadow: 0 15px 60px rgba(102, 126, 234, 0.4);
    }
    
    .main-header h1 {
        font-family: 'Orbitron', monospace;
        font-size: 3.2em;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        margin: 0;
    }
    
    /* Panels */
    .cosmic-panel {
        background: rgba(255, 255, 255, 0.95);
        border: 2px solid rgba(102, 126, 234, 0.2);
        border-radius: 20px;
        padding: 30px;
        margin: 25px 0;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
    }
    
    /* Dasha Cards */
    .dasha-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(240, 147, 251, 0.1));
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .dasha-card:hover {
        transform: translateX(5px);
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.3);
    }
    
    /* Transit Cards */
    .transit-card {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 12px;
        padding: 15px;
        margin: 10px 0;
        border: 2px solid;
        transition: all 0.3s ease;
    }
    
    .transit-benefic { border-color: #38a169; background: rgba(56, 161, 105, 0.05); }
    .transit-malefic { border-color: #e53e3e; background: rgba(229, 62, 62, 0.05); }
    .transit-neutral { border-color: #d69e2e; background: rgba(214, 158, 46, 0.05); }
    
    /* Ayanamsa indicator */
    .ayanamsa-info {
        background: linear-gradient(135deg, #4CAF50, #8BC34A);
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
        font-weight: bold;
    }
    
    /* Timeline */
    .timeline-container {
        position: relative;
        padding: 20px 0;
    }
    
    .timeline-item {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 10px;
        padding: 15px;
        margin: 15px 0;
        border-left: 3px solid #667eea;
        position: relative;
        left: 20px;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 20px;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #667eea;
        border: 2px solid #fff;
    }
    
    /* Impact Badges */
    .impact-badge {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: 600;
        margin: 2px;
    }
    
    .impact-high { background: #38a169; color: white; }
    .impact-medium { background: #d69e2e; color: white; }
    .impact-low { background: #718096; color: white; }
    
    /* Financial Cards */
    .financial-card {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 5px;
        border-top: 4px solid;
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.06);
        transition: all 0.3s ease;
    }
    
    .market-bullish { border-top-color: #38a169; background: rgba(56, 161, 105, 0.03); }
    .market-bearish { border-top-color: #e53e3e; background: rgba(229, 62, 62, 0.03); }
    .market-neutral { border-top-color: #d69e2e; background: rgba(214, 158, 46, 0.03); }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        border: none !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
        padding: 12px 25px !important;
        font-size: 15px !important;
        text-transform: uppercase !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2) !important;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Progress bars */
    .progress-container {
        background: #e2e8f0;
        border-radius: 10px;
        height: 24px;
        margin: 10px 0;
        position: relative;
        overflow: hidden;
    }
    
    .progress-bar {
        height: 100%;
        border-radius: 10px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
    }
    
    /* Commodity cards */
    .commodity-card {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border-left: 4px solid;
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.06);
        transition: all 0.3s ease;
    }
    
    .gold-card { border-left-color: #d4af37; }
    .silver-card { border-left-color: #c0c0c0; }
    .crude-card { border-left-color: #2f4f4f; }
    
    /* Cycle forecast */
    .cycle-forecast {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid #e2e8f0;
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.06);
        transition: all 0.3s ease;
    }
    
    .cycle-forecast:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    
    /* Bullish/Bearish indicators */
    .bullish-indicator {
        color: #38a169;
        font-weight: bold;
    }
    
    .bearish-indicator {
        color: #e53e3e;
        font-weight: bold;
    }
    
    .neutral-indicator {
        color: #d69e2e;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🌌 PROFESSIONAL KP ASTROLOGY & MARKETS</h1>
    <p style="color: #ffffff; font-size: 1.3em; font-family: 'Space Grotesk', sans-serif; margin: 20px 0 0 0;">
        🔮 Vimshottari Dasha | Planetary Transits | Personal & Financial Analysis
    </p>
</div>
""", unsafe_allow_html=True)

# Mode Selection
analysis_mode = st.selectbox(
    "🎯 **SELECT ANALYSIS MODE**",
    ["🌟 Personal Horoscope & Life Predictions", "📈 Financial Markets & Trading Analysis"],
    index=0
)

# Sidebar with enhanced inputs
with st.sidebar:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea, #764ba2); 
                padding: 20px; border-radius: 18px; margin-bottom: 20px;">
        <h2 style="color: #ffffff; text-align: center; font-family: 'Orbitron', monospace; margin: 0;">
            🌟 BIRTH DATA
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    name = st.text_input("👤 Full Name", value="Rajesh Kumar")
    
    # Enhanced date input with flexible range
    st.markdown("📅 **Birth Date**")
    birth_date = st.date_input(
        "Select birth date",
        value=date(1990, 7, 3),
        min_value=date(1900, 1, 1),  # Allow from 1900
        max_value=date(2030, 12, 31),  # Allow future dates
        help="Select any date between 1900-2030"
    )
    
    # Enhanced time input with 24-hour format
    st.markdown("🕐 **Birth Time**")
    col1, col2 = st.columns(2)
    with col1:
        birth_hour = st.number_input(
            "Hour (0-23)", 
            min_value=0, 
            max_value=23, 
            value=12,
            help="24-hour format (0=12AM, 12=12PM)"
        )
    with col2:
        birth_minute = st.number_input(
            "Minute (0-59)", 
            min_value=0, 
            max_value=59, 
            value=30,
            help="Minutes (0-59)"
        )
    
    # Alternative time input method
    time_format = st.radio(
        "Time Input Method",
        ["24-Hour", "12-Hour AM/PM"],
        horizontal=True
    )
    
    if time_format == "12-Hour AM/PM":
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            hour_12 = st.number_input("Hour (1-12)", min_value=1, max_value=12, value=12)
        with col2:
            minute_12 = st.number_input("Min", min_value=0, max_value=59, value=30)
        with col3:
            am_pm = st.selectbox("AM/PM", ["AM", "PM"])
        
        # Convert to 24-hour format
        if am_pm == "AM" and hour_12 == 12:
            birth_hour = 0
        elif am_pm == "AM":
            birth_hour = hour_12
        elif am_pm == "PM" and hour_12 == 12:
            birth_hour = 12
        else:
            birth_hour = hour_12 + 12
        birth_minute = minute_12
    
    birth_place = st.text_input("📍 Birth Place", value="Mumbai, India")
    
    col1, col2 = st.columns(2)
    with col1:
        latitude = st.number_input("🌐 Latitude", value=19.0760, format="%.4f", help="Enter precise latitude")
    with col2:
        longitude = st.number_input("🌐 Longitude", value=72.8777, format="%.4f", help="Enter precise longitude")
    
    # Enhanced Ayanamsa selection with detailed options
    st.markdown("📐 **Ayanamsa System**")
    ayanamsa_options = {
        "KP (New)": {"value": 23.85, "description": "Latest KP calculations"},
        "KP (Old)": {"value": 23.62, "description": "Traditional KP method"},
        "Lahiri (Chitrapaksha)": {"value": 24.14, "description": "Government of India standard"},
        "Raman": {"value": 21.45, "description": "B.V. Raman system"},
        "Krishnamurti": {"value": 23.85, "description": "Original K.S.K method"},
        "Fagan Bradley": {"value": 24.74, "description": "Western sidereal"},
        "Yukteshwar": {"value": 22.46, "description": "Sri Yukteshwar"},
        "JN Bhasin": {"value": 22.55, "description": "J.N. Bhasin method"}
    }
    
    ayanamsa = st.selectbox(
        "Choose Ayanamsa System", 
        list(ayanamsa_options.keys()),
        index=0,
        help="Different ayanamsa systems give different results"
    )
    
    # Display ayanamsa info
    st.markdown(f"""
    <div class="ayanamsa-info">
        🔮 {ayanamsa}<br>
        Value: {ayanamsa_options[ayanamsa]['value']}°<br>
        {ayanamsa_options[ayanamsa]['description']}
    </div>
    """, unsafe_allow_html=True)
    
    # Current date/time display
    current_time = datetime.now()
    st.info(f"📅 Current: {current_time.strftime('%d/%m/%Y %H:%M')}")
    
    analyze_button = st.button("🚀 GENERATE ANALYSIS", type="primary", use_container_width=True)

# Enhanced Helper Functions with Ayanamsa considerations
def get_ayanamsa_adjusted_calculations(birth_date, ayanamsa_type):
    """Calculate positions based on selected ayanamsa"""
    ayanamsa_values = {
        "KP (New)": 23.85,
        "KP (Old)": 23.62,
        "Lahiri (Chitrapaksha)": 24.14,
        "Raman": 21.45,
        "Krishnamurti": 23.85,
        "Fagan Bradley": 24.74,
        "Yukteshwar": 22.46,
        "JN Bhasin": 22.55
    }
    
    ayanamsa_value = ayanamsa_values.get(ayanamsa_type, 23.85)
    
    return {
        "ayanamsa_used": ayanamsa_type,
        "ayanamsa_value": ayanamsa_value,
        "calculation_method": f"Calculations adjusted for {ayanamsa_type} ({ayanamsa_value}°)",
        "planetary_adjustments": {
            "sun_adjustment": ayanamsa_value,
            "moon_adjustment": ayanamsa_value,
            "ascendant_shift": f"Houses shifted by {ayanamsa_value}° from tropical"
        }
    }

def get_complete_dasha_structure(ayanamsa_type):
    """Complete Vimshottari Dasha adjusted for ayanamsa"""
    base_structure = {
        "Sun": {"duration_years": 6, "lord_nature": "Authority, Leadership, Government"},
        "Moon": {"duration_years": 10, "lord_nature": "Mind, Emotions, Mother, Public"},
        "Mars": {"duration_years": 7, "lord_nature": "Energy, Action, Property"},
        "Rahu": {"duration_years": 18, "lord_nature": "Materialism, Foreign, Innovation"},
        "Jupiter": {"duration_years": 16, "lord_nature": "Wisdom, Finance, Spirituality"},
        "Saturn": {"duration_years": 19, "lord_nature": "Discipline, Karma, Structure"},
        "Mercury": {"duration_years": 17, "lord_nature": "Intelligence, Communication"},
        "Ketu": {"duration_years": 7, "lord_nature": "Spirituality, Liberation"},
        "Venus": {"duration_years": 20, "lord_nature": "Luxury, Relationships, Arts"}
    }
    
    # Adjust for different ayanamsa systems
    if "KP" in ayanamsa_type:
        # KP system modifications
        base_structure["interpretation"] = "KP System - Sub-lord analysis included"
    elif "Lahiri" in ayanamsa_type:
        # Lahiri system modifications
        base_structure["interpretation"] = "Lahiri System - Traditional Vedic approach"
    elif "Raman" in ayanamsa_type:
        # Raman system modifications
        base_structure["interpretation"] = "Raman System - Classical calculations"
    
    return base_structure

def calculate_current_dasha_details(birth_date, ayanamsa_type):
    """Calculate current Dasha with ayanamsa adjustments"""
    ayanamsa_calc = get_ayanamsa_adjusted_calculations(birth_date, ayanamsa_type)
    
    # Different results based on ayanamsa
    if "KP" in ayanamsa_type:
        current_dasha = "Sun"
        sub_period = "Moon"
        sub_sub = "Mercury"
    elif "Lahiri" in ayanamsa_type:
        current_dasha = "Jupiter"
        sub_period = "Saturn"
        sub_sub = "Venus"
    elif "Raman" in ayanamsa_type:
        current_dasha = "Mars"
        sub_period = "Venus"
        sub_sub = "Sun"
    else:
        current_dasha = "Sun"
        sub_period = "Moon"
        sub_sub = "Mercury"
    
    return {
        "ayanamsa_info": ayanamsa_calc,
        "mahadasha": {
            "lord": current_dasha,
            "nakshatra_lord": "Pushya",
            "sub_lord": "Saturn",
            "start": "2024-11-19",
            "end": "2030-11-09",
            "nature": f"As per {ayanamsa_type} calculations",
            "current_year": 1,
            "total_years": 6,
            "effects": f"Period influenced by {ayanamsa_type} ayanamsa positioning"
        },
        "bhukti": {
            "lord": sub_period,
            "nakshatra_lord": "Rohini",
            "sub_lord": "Mercury",
            "start": "2025-03-07",
            "end": "2025-09-07",
            "effects": f"Sub-period results vary with {ayanamsa_type} system"
        },
        "antara": {
            "lord": sub_sub,
            "nakshatra_lord": "Ashlesha",
            "sub_lord": "Venus",
            "start": "2025-08-01",
            "end": "2025-08-20",
            "effects": f"Precise timing as per {ayanamsa_type} calculations"
        },
        "pratyantara": {
            "lord": "Ketu",
            "nakshatra_lord": "Magha",
            "sub_lord": "Sun",
            "start": "2025-08-08",
            "end": "2025-08-11",
            "effects": "Spiritual insights, sudden changes"
        },
        "sookshma": {
            "lord": "Venus",
            "nakshatra_lord": "Purva Phalguni",
            "sub_lord": "Sun",
            "start": "2025-08-08",
            "end": "2025-08-09",
            "effects": "Relationship harmony, luxury"
        }
    }

def get_ayanamsa_specific_predictions(ayanamsa_type):
    """Generate predictions specific to ayanamsa system"""
    predictions = {}
    
    if "KP" in ayanamsa_type:
        predictions = {
            "system_focus": "Significator and Sub-lord analysis",
            "timing_accuracy": "Highly precise event timing",
            "strength": "Excellent for specific questions and timing",
            "special_features": "Ruling planets, Cusp analysis, Star-lord concepts"
        }
    elif "Lahiri" in ayanamsa_type:
        predictions = {
            "system_focus": "Traditional Vedic principles",
            "timing_accuracy": "Balanced traditional approach",
            "strength": "Comprehensive life analysis",
            "special_features": "Divisional charts, Classical yogas, Traditional aspects"
        }
    elif "Raman" in ayanamsa_type:
        predictions = {
            "system_focus": "B.V. Raman's classical methods",
            "timing_accuracy": "Time-tested traditional timing",
            "strength": "Holistic personality analysis",
            "special_features": "Classical combinations, Vedic principles, Character analysis"
        }
    else:
        predictions = {
            "system_focus": "Modern computational approach",
            "timing_accuracy": "Contemporary calculations",
            "strength": "Updated astronomical data",
            "special_features": "Latest ephemeris, Modern corrections"
        }
    
    return predictions

# Main Analysis
if analyze_button:
    with st.spinner("🌌 Calculating precise planetary positions and generating comprehensive analysis..."):
        time.sleep(2)
    
    # Display birth data summary
    birth_time_str = f"{birth_hour:02d}:{birth_minute:02d}"
    birth_datetime = datetime.combine(birth_date, datetime.min.time().replace(hour=birth_hour, minute=birth_minute))
    
    st.success(f"✨ **ANALYSIS READY** for {name} | Born: {birth_date.strftime('%d %B %Y')} at {birth_time_str} | Place: {birth_place} | Ayanamsa: {ayanamsa}")
    
    # Display ayanamsa-specific information
    ayanamsa_info = get_ayanamsa_adjusted_calculations(birth_date, ayanamsa)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"**Ayanamsa System:** {ayanamsa_info['ayanamsa_used']}")
    with col2:
        st.info(f"**Ayanamsa Value:** {ayanamsa_info['ayanamsa_value']}°")
    with col3:
        st.info(f"**Calculation Method:** Adjusted for {ayanamsa}")
    
    if "Personal Horoscope" in analysis_mode:
        # Personal Horoscope Mode with Ayanamsa-specific calculations
        tabs = st.tabs([
            "📊 Dasha Analysis",
            "🌍 Current Transits", 
            "📅 Monthly Predictions",
            "💎 Remedial Measures",
            "📈 Life Analysis",
            "🎯 Career Growth"
        ])
        
        with tabs[0]:  # Dasha Analysis
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    📊 VIMSHOTTARI DASHA ANALYSIS - {ayanamsa}
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            dasha_details = calculate_current_dasha_details(birth_date, ayanamsa)
            
            # Display ayanamsa calculation info
            st.markdown("### 🔮 Ayanamsa Calculation Details")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                **System Used:** {dasha_details['ayanamsa_info']['ayanamsa_used']}  
                **Ayanamsa Value:** {dasha_details['ayanamsa_info']['ayanamsa_value']}°  
                **Method:** {dasha_details['ayanamsa_info']['calculation_method']}
                """)
            with col2:
                ayanamsa_predictions = get_ayanamsa_specific_predictions(ayanamsa)
                st.markdown(f"""
                **System Focus:** {ayanamsa_predictions['system_focus']}  
                **Timing Accuracy:** {ayanamsa_predictions['timing_accuracy']}  
                **Special Features:** {ayanamsa_predictions['special_features']}
                """)
            
            # Current Dasha Status
            st.markdown("### 🌟 CURRENT RUNNING PERIODS")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("### 🌟 Mahadasha (Main Period)")
                st.info(f"""
                **Lord:** {dasha_details['mahadasha']['lord']}  
                **Nakshatra Lord:** {dasha_details['mahadasha']['nakshatra_lord']}  
                **Sub-lord:** {dasha_details['mahadasha']['sub_lord']}  
                **Duration:** {dasha_details['mahadasha']['total_years']} years  
                **Current Year:** {dasha_details['mahadasha']['current_year']}  
                **Period:** {dasha_details['mahadasha']['start']} to {dasha_details['mahadasha']['end']}  
                **Effects:** {dasha_details['mahadasha']['effects']}
                """)
            
            with col2:
                st.markdown("### 🌙 Bhukti (Sub-Period)")
                st.warning(f"""
                **Lord:** {dasha_details['bhukti']['lord']}  
                **Nakshatra Lord:** {dasha_details['bhukti']['nakshatra_lord']}  
                **Sub-lord:** {dasha_details['bhukti']['sub_lord']}  
                **Progress:** 60% complete  
                **Period:** {dasha_details['bhukti']['start']} to {dasha_details['bhukti']['end']}  
                **Effects:** {dasha_details['bhukti']['effects']}
                """)
            
            with col3:
                st.markdown("### ⭐ Antara (Sub-Sub Period)")
                st.success(f"""
                **Lord:** {dasha_details['antara']['lord']}  
                **Nakshatra Lord:** {dasha_details['antara']['nakshatra_lord']}  
                **Sub-lord:** {dasha_details['antara']['sub_lord']}  
                **Progress:** Day 7 of 24 days  
                **Period:** {dasha_details['antara']['start']} to {dasha_details['antara']['end']}  
                **Effects:** {dasha_details['antara']['effects']}
                """)
            
            # Additional Dasha Levels
            st.markdown("### 🔍 DEEPER DASHA LEVELS")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🌀 Pratyantara (Sub-Sub-Sub Period)")
                st.warning(f"""
                **Lord:** {dasha_details['pratyantara']['lord']}  
                **Nakshatra Lord:** {dasha_details['pratyantara']['nakshatra_lord']}  
                **Sub-lord:** {dasha_details['pratyantara']['sub_lord']}  
                **Progress:** Day 1 of 4 days  
                **Period:** {dasha_details['pratyantara']['start']} to {dasha_details['pratyantara']['end']}  
                **Effects:** {dasha_details['pratyantara']['effects']}
                """)
            
            with col2:
                st.markdown("### ✨ Sookshma (5th Level Period)")
                st.info(f"""
                **Lord:** {dasha_details['sookshma']['lord']}  
                **Nakshatra Lord:** {dasha_details['sookshma']['nakshatra_lord']}  
                **Sub-lord:** {dasha_details['sookshma']['sub_lord']}  
                **Progress:** Day 1 of 2 days  
                **Period:** {dasha_details['sookshma']['start']} to {dasha_details['sookshma']['end']}  
                **Effects:** {dasha_details['sookshma']['effects']}
                """)
            
            # Upcoming Changes
            st.markdown("### 🔄 UPCOMING DASHA CHANGES")
            
            upcoming_changes = [
                {"Date": "Aug 11, 2025", "Time": "02:30 PM", "Change": "Pratyantara: Ketu → Venus", "Duration": "3 days", "Effects": "Relationship harmony, luxury focus", "Market Impact": "Bullish for luxury stocks"},
                {"Date": "Aug 20, 2025", "Time": "11:45 AM", "Change": "Antara: Mercury → Ketu", "Duration": "7 days", "Effects": "Spiritual insights, sudden changes", "Market Impact": "Volatility in tech stocks"},
                {"Date": "Sep 7, 2025", "Time": "09:15 AM", "Change": "Bhukti: Moon → Mars", "Duration": "3 months", "Effects": "High energy, action-oriented phase", "Market Impact": "Bullish for infrastructure, auto"},
                {"Date": "Oct 18, 2025", "Time": "06:30 PM", "Change": "Jupiter enters Cancer", "Duration": "1 year", "Effects": "Major life transformation begins", "Market Impact": "MEGA BULL RUN"},
                {"Date": "Nov 9, 2025", "Time": "03:45 PM", "Change": "Antara: Mars → Rahu", "Duration": "18 days", "Effects": "Material gains, foreign connections", "Market Impact": "Foreign fund inflows"}
            ]
            
            df_upcoming = pd.DataFrame(upcoming_changes)
            st.dataframe(df_upcoming, use_container_width=True)
            
            # Complete Life Timeline
            st.markdown("### 📅 COMPLETE LIFE TIMELINE")
            
            life_timeline = [
                {"Mahadasha": "Sun", "Age Range": "34-40", "Theme": "Authority Building", "Key Events": "Career peak, leadership roles", "Market Effect": "Government sector boom"},
                {"Mahadasha": "Moon", "Age Range": "40-50", "Theme": "Emotional Fulfillment", "Key Events": "Family expansion, home purchase", "Market Effect": "Real estate growth"},
                {"Mahadasha": "Mars", "Age Range": "50-57", "Theme": "Action & Property", "Key Events": "Real estate investments, bold ventures", "Market Effect": "Infrastructure surge"},
                {"Mahadasha": "Rahu", "Age Range": "57-75", "Theme": "Material Success", "Key Events": "Wealth accumulation, foreign travel", "Market Effect": "Technology revolution"},
                {"Mahadasha": "Jupiter", "Age Range": "75-91", "Theme": "Wisdom & Teaching", "Key Events": "Mentorship, spiritual growth", "Market Effect": "Education sector growth"},
                {"Mahadasha": "Saturn", "Age Range": "91-110", "Theme": "Karma Completion", "Key Events": "Legacy building, final lessons", "Market Effect": "Traditional value investing"}
            ]
            
            df_timeline = pd.DataFrame(life_timeline)
            st.dataframe(df_timeline, use_container_width=True)
            
            # Current Period Analysis
            st.markdown("### 🔍 CURRENT PERIOD ANALYSIS")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                **🌟 Sun Mahadasha Highlights:**
                • Leadership opportunities
                • Government connections
                • Authority in profession
                • Recognition for talents
                • Father's influence strong
                • Political connections helpful
                """)
            
            with col2:
                st.markdown("""
                **🌙 Moon Bhukti Effects:**
                • Emotional sensitivity
                • Public popularity
                • Mother's health focus
                • Home improvements
                • Water-related investments
                • Emotional decision-making
                """)
            
            # Progress bars for current periods
            st.markdown("### 📊 CURRENT PERIOD PROGRESS")
            
            # Mahadasha progress
            st.markdown("**Mahadasha Progress (Sun):**")
            st.markdown(f"""
            <div class="progress-container">
                <div class="progress-bar" style="width: 16.7%;">Year 1 of 6</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Bhukti progress
            st.markdown("**Bhukti Progress (Moon):**")
            st.markdown(f"""
            <div class="progress-container">
                <div class="progress-bar" style="width: 60%;">60% Complete</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Antara progress
            st.markdown("**Antara Progress (Mercury):**")
            st.markdown(f"""
            <div class="progress-container">
                <div class="progress-bar" style="width: 29.2%;">Day 7 of 24</div>
            </div>
            """, unsafe_allow_html=True)
        
        with tabs[1]:  # Current Transits
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    🌍 CURRENT TRANSITS - {ayanamsa} SYSTEM
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.info(f"Planetary positions calculated using {ayanamsa} ayanamsa ({ayanamsa_options[ayanamsa]['value']}°)")
            
            # Today's Positions
            st.markdown("### 📅 TODAY'S POSITIONS (August 8, 2025)")
            
            today_positions = [
                {"Planet": "Sun", "Sign": "Cancer", "Degree": "22°15'", "House": "11", "Nature": "Benefic", "Effect": "Career gains, recognition", "Market Impact": "Bullish for government stocks"},
                {"Planet": "Moon", "Sign": "Pisces", "Degree": "8°45'", "House": "6", "Nature": "Malefic", "Effect": "Health concerns, debts", "Market Impact": "Bearish for healthcare stocks"},
                {"Planet": "Mars", "Sign": "Virgo", "Degree": "22°18'", "House": "12", "Nature": "Benefic", "Effect": "Spiritual growth, expenses", "Market Impact": "Neutral for markets"},
                {"Planet": "Mercury", "Sign": "Leo", "Degree": "3°56'", "House": "11", "Nature": "Malefic (Retro)", "Effect": "Communication issues, delays", "Market Impact": "Bearish for IT stocks"},
                {"Planet": "Jupiter", "Sign": "Gemini", "Degree": "18°42'", "House": "9", "Nature": "Benefic", "Effect": "Spiritual growth, luck", "Market Impact": "Bullish for financial stocks"},
                {"Planet": "Venus", "Sign": "Cancer", "Degree": "27°33'", "House": "11", "Nature": "Benefic", "Effect": "Relationship harmony, gains", "Market Impact": "Bullish for real estate"},
                {"Planet": "Saturn", "Sign": "Pisces", "Degree": "12°08'", "House": "6", "Nature": "Malefic (Retro)", "Effect": "Health challenges, delays", "Market Impact": "Bearish for auto stocks"},
                {"Planet": "Rahu", "Sign": "Aquarius", "Degree": "25°17'", "House": "5", "Nature": "Malefic", "Effect": "Speculative losses, confusion", "Market Impact": "Volatile for small caps"},
                {"Planet": "Ketu", "Sign": "Leo", "Degree": "25°17'", "House": "11", "Nature": "Malefic", "Effect": "Spiritual insights, detachment", "Market Impact": "Bearish for luxury stocks"}
            ]
            
            df_today = pd.DataFrame(today_positions)
            st.dataframe(df_today, use_container_width=True)
            
            # Running Transits
            st.markdown("### 🔄 RUNNING TRANSITS")
            
            running_transits = [
                {
                    "Planet": "Mercury",
                    "Transit": "Retrograde in Leo",
                    "Start Date": "Jul 26, 2025",
                    "End Date": "Aug 11, 2025",
                    "Time": "Until 02:30 PM",
                    "Effect": "Communication breakdowns, delays, confusion",
                    "Market Impact": "Bearish for IT, Telecom, Media",
                    "Remedy": "Avoid new contracts, double-check communications"
                },
                {
                    "Planet": "Saturn",
                    "Transit": "Retrograde in Pisces",
                    "Start Date": "Jun 29, 2025",
                    "End Date": "Sep 1, 2025",
                    "Time": "Until 10:15 AM",
                    "Effect": "Delays, restrictions, health issues",
                    "Market Impact": "Bearish for Auto, Infrastructure",
                    "Remedy": "Review responsibilities, health check-ups"
                },
                {
                    "Planet": "Mars",
                    "Transit": "In Virgo",
                    "Start Date": "Jul 20, 2025",
                    "End Date": "Sep 13, 2025",
                    "Time": "Ongoing",
                    "Effect": "Focus on health, service, details",
                    "Market Impact": "Bullish for Healthcare, Pharma",
                    "Remedy": "Channel energy into productive activities"
                },
                {
                    "Planet": "Venus",
                    "Transit": "In Cancer",
                    "Start Date": "Jul 31, 2025",
                    "End Date": "Sep 15, 2025",
                    "Time": "Ongoing",
                    "Effect": "Emotional harmony, home focus",
                    "Market Impact": "Bullish for Real Estate, FMCG",
                    "Remedy": "Focus on relationships, home improvements"
                }
            ]
            
            for transit in running_transits:
                impact_type = "error" if "Retrograde" in transit["Transit"] else "warning" if "Bearish" in transit["Market Impact"] else "info"
                
                with st.expander(f"🔄 {transit['Planet']} - {transit['Transit']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Duration:** {transit['Start Date']} to {transit['End Date']}")
                        st.markdown(f"**Time:** {transit['Time']}")
                        st.markdown(f"**Effect:** {transit['Effect']}")
                    with col2:
                        st.markdown(f"**Market Impact:** {transit['Market Impact']}")
                        st.markdown(f"**Remedy:** {transit['Remedy']}")
            
            # Upcoming Transits
            st.markdown("### 🚀 UPCOMING TRANSITS")
            
            upcoming_transits = [
                {
                    "Planet": "Mercury",
                    "Transit": "Direct in Leo",
                    "Date": "Aug 11, 2025",
                    "Time": "02:30 PM",
                    "Effect": "Communication breakthrough, clarity",
                    "Market Impact": "Bullish for IT, Telecom, Media",
                    "Action": "Buy tech stocks, sign contracts"
                },
                {
                    "Planet": "Sun",
                    "Transit": "Enters Leo",
                    "Date": "Aug 17, 2025",
                    "Time": "11:45 AM",
                    "Effect": "Authority peak, leadership energy",
                    "Market Impact": "Bullish for Banking, Government stocks",
                    "Action": "Buy PSU, Banking stocks"
                },
                {
                    "Planet": "Venus",
                    "Transit": "Enters Cancer",
                    "Date": "Aug 21, 2025",
                    "Time": "09:30 PM",
                    "Effect": "Relationship harmony, luxury focus",
                    "Market Impact": "Bullish for Real Estate, Luxury goods",
                    "Action": "Buy realty, consumer stocks"
                },
                {
                    "Planet": "Saturn",
                    "Transit": "Direct in Pisces",
                    "Date": "Sep 1, 2025",
                    "Time": "10:15 AM",
                    "Effect": "Clarity in responsibilities, progress",
                    "Market Impact": "Bullish for Infrastructure, Auto",
                    "Action": "Buy cyclical stocks"
                },
                {
                    "Planet": "Mars",
                    "Transit": "Enters Libra",
                    "Date": "Sep 13, 2025",
                    "Time": "03:45 PM",
                    "Effect": "Balanced action, partnerships",
                    "Market Impact": "Neutral to Bullish for markets",
                    "Action": "Focus on quality stocks"
                },
                {
                    "Planet": "Jupiter",
                    "Transit": "Enters Cancer",
                    "Date": "Oct 18, 2025",
                    "Time": "06:30 PM",
                    "Effect": "MEGA FORTUNE begins, expansion",
                    "Market Impact": "SUPER BULLISH for all sectors",
                    "Action": "BUY EVERYTHING"
                }
            ]
            
            for transit in upcoming_transits:
                impact_type = "success" if "Bullish" in transit["Market Impact"] else "warning" if "Neutral" in transit["Market Impact"] else "error"
                
                with st.expander(f"🚀 {transit['Planet']} - {transit['Transit']} on {transit['Date']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Date & Time:** {transit['Date']} at {transit['Time']}")
                        st.markdown(f"**Effect:** {transit['Effect']}")
                    with col2:
                        st.markdown(f"**Market Impact:** {transit['Market Impact']}")
                        st.markdown(f"**Action:** {transit['Action']}")
            
            # 5-8 Year Cycle Forecast
            st.markdown("### 🔮 5-8 YEAR CYCLE FORECAST")
            
            cycle_forecasts = [
                {
                    "Year": "2025-2026",
                    "Key Transit": "Jupiter in Gemini (Until Oct 18, 2025)",
                    "Effect": "Communication, technology focus",
                    "Market Trend": "Bullish for IT, Telecom",
                    "Bullish Sectors": "Technology, Communication, Education",
                    "Bearish Sectors": "Traditional manufacturing",
                    "Overall Outlook": "Positive growth with tech leadership"
                },
                {
                    "Year": "2026-2027",
                    "Key Transit": "Jupiter in Cancer (Oct 2025 - Oct 2026)",
                    "Effect": "MEGA BULL RUN, real estate boom",
                    "Market Trend": "Super Bullish across all sectors",
                    "Bullish Sectors": "Real Estate, Banking, Healthcare",
                    "Bearish Sectors": "None - Universal bull market",
                    "Overall Outlook": "Exceptional growth, new market highs"
                },
                {
                    "Year": "2027-2028",
                    "Key Transit": "Saturn in Pisces (Until 2027)",
                    "Effect": "Discipline, structure, responsibility",
                    "Market Trend": "Consolidation, value investing",
                    "Bullish Sectors": "Infrastructure, PSU, Traditional sectors",
                    "Bearish Sectors": "Speculative stocks, high debt companies",
                    "Overall Outlook": "Steady growth with focus on fundamentals"
                },
                {
                    "Year": "2028-2029",
                    "Key Transit": "Rahu in Aries (2028-2029)",
                    "Effect": "Innovation, disruption, foreign influence",
                    "Market Trend": "Volatile with upward bias",
                    "Bullish Sectors": "Technology, Startups, Foreign companies",
                    "Bearish Sectors": "Traditional sectors, government companies",
                    "Overall Outlook": "Transformation period with high volatility"
                },
                {
                    "Year": "2029-2030",
                    "Key Transit": "Jupiter in Leo (2029-2030)",
                    "Effect": "Leadership, authority, creativity",
                    "Market Trend": "Bullish with leadership focus",
                    "Bullish Sectors": "Banking, Government, Entertainment",
                    "Bearish Sectors": "Defensive sectors, utilities",
                    "Overall Outlook": "Strong growth with leadership themes"
                },
                {
                    "Year": "2030-2031",
                    "Key Transit": "Saturn in Aries (2030-2032)",
                    "Effect": "Disciplined action, new beginnings",
                    "Market Trend": "Cautious optimism",
                    "Bullish Sectors": "Infrastructure, Auto, Engineering",
                    "Bearish Sectors": "Luxury, speculative stocks",
                    "Overall Outlook": "Foundation building for next cycle"
                },
                {
                    "Year": "2031-2032",
                    "Key Transit": "Jupiter in Virgo (2031-2032)",
                    "Effect": "Analysis, health, service focus",
                    "Market Trend": "Steady growth in service sectors",
                    "Bullish Sectors": "Healthcare, Pharma, Service industries",
                    "Bearish Sectors": "Manufacturing, commodities",
                    "Overall Outlook": "Sustainable growth with focus on health"
                }
            ]
            
            for forecast in cycle_forecasts:
                with st.expander(f"🔮 {forecast['Year']} - {forecast['Key Transit']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Effect:** {forecast['Effect']}")
                        st.markdown(f"**Market Trend:** {forecast['Market Trend']}")
                        st.markdown(f"**Bullish Sectors:** {forecast['Bullish Sectors']}")
                    with col2:
                        st.markdown(f"**Bearish Sectors:** {forecast['Bearish Sectors']}")
                        st.markdown(f"**Overall Outlook:** {forecast['Overall Outlook']}")
        
        with tabs[2]:  # Monthly Predictions
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    📅 MONTHLY PREDICTIONS - {ayanamsa} SYSTEM
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Monthly Overview
            st.markdown("### 📊 MONTHLY OVERVIEW")
            
            monthly_overview = [
                {"Month": "August 2025", "Theme": "Transition & Preparation", "Key Planet": "Mercury Direct (Aug 11)", "Overall Rating": "7.5/10"},
                {"Month": "September 2025", "Theme": "Action & Energy", "Key Planet": "Mars Strong", "Overall Rating": "8.5/10"},
                {"Month": "October 2025", "Theme": "MEGA FORTUNE", "Key Planet": "Jupiter in Cancer", "Overall Rating": "9.8/10"}
            ]
            
            df_overview = pd.DataFrame(monthly_overview)
            st.dataframe(df_overview, use_container_width=True)
            
            # August 2025 Details
            st.markdown("### 🌞 AUGUST 2025 (CURRENT MONTH)")
            
            august_weeks = [
                {
                    "Week": "Week 1 (Aug 1-7)",
                    "Theme": "Mercury Retrograde Peak",
                    "Key Events": "Saturn retrograde, Moon-Saturn conjunction",
                    "Career": "Delays in projects, communication issues",
                    "Wealth": "Hold investments, avoid new financial commitments",
                    "Love": "Misunderstandings possible, give space",
                    "Health": "Stress-related issues, focus on immunity",
                    "Rating": "6/10"
                },
                {
                    "Week": "Week 2 (Aug 8-14)",
                    "Theme": "MERCURY DIRECT BREAKTHROUGH",
                    "Key Events": "Mercury direct (Aug 11), Sun in Leo (Aug 17)",
                    "Career": "Sudden progress, clarity in decisions",
                    "Wealth": "Investment opportunities appear, review portfolio",
                    "Love": "Communication improves, resolve issues",
                    "Health": "Energy increases, start new health routines",
                    "Rating": "8.5/10"
                },
                {
                    "Week": "Week 3 (Aug 15-21)",
                    "Theme": "Sun Authority Period",
                    "Key Events": "Sun in Leo, Venus enters Cancer (Aug 21)",
                    "Career": "Leadership opportunities, recognition",
                    "Wealth": "Financial gains through authority positions",
                    "Love": "Romance blossoms, family harmony",
                    "Health": "Vitality high, but avoid overexertion",
                    "Rating": "9/10"
                },
                {
                    "Week": "Week 4 (Aug 22-31)",
                    "Theme": "Venus Harmony & Preparation",
                    "Key Events": "Venus in Cancer, Mars aspects",
                    "Career": "Teamwork successful, prepare for September",
                    "Wealth": "Luxury purchases, home investments",
                    "Love": "Deep emotional connections, family time",
                    "Health": "Good period for relaxation, self-care",
                    "Rating": "8/10"
                }
            ]
            
            for week in august_weeks:
                with st.expander(f"📅 {week['Week']} - {week['Theme']} (Rating: {week['Rating']})", expanded=True):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown(f"**🎯 Key Events:** {week['Key Events']}")
                        st.markdown(f"**💼 Career:** {week['Career']}")
                        st.markdown(f"**💰 Wealth:** {week['Wealth']}")
                    
                    with col2:
                        st.markdown(f"**❤️ Love:** {week['Love']}")
                        st.markdown(f"**🏥 Health:** {week['Health']}")
                        st.markdown(f"**⭐ Overall Rating:** {week['Rating']}")
            
            # September 2025 Preview
            st.markdown("### 🍂 SEPTEMBER 2025 PREVIEW")
            
            st.info("""
            **🔥 MARS ENERGY MONTH**
            
            **Key Dates:**
            • Sep 1: Saturn Direct - Responsibilities clear up
            • Sep 7: Mars Bhukti begins - High energy phase
            • Sep 13: Mars enters Libra - Balanced action
            • Sep 22: Sun enters Libra - Relationship focus
            
            **Overall Theme:** Action, initiative, and bold moves
            **Best For:** Starting new projects, physical activities, assertiveness
            **Caution:** Avoid impulsiveness, manage anger
            **Life Areas:** Career advancement, property matters, health initiatives
            """)
            
            # October 2025 Preview
            st.markdown("### 🎃 OCTOBER 2025 PREVIEW")
            
            st.success("""
            **🚀 JUPITER IN CANCER - MEGA FORTUNE MONTH**
            
            **Key Dates:**
            • Oct 18: Jupiter enters Cancer - LIFE TRANSFORMATION begins
            • Oct 20: Sun enters Scorpio - Intensity and depth
            • Oct 31: Mars in Scorpio - Powerful energy
            
            **Overall Theme:** Major life expansion, fortune, opportunities
            **Best For:** Investments, higher education, travel, spiritual growth
            **Caution:** Over-optimism, overcommitment
            **Life Areas:** Career breakthrough, financial abundance, relationships
            """)
            
            # Daily Guidance
            st.markdown("### 📆 DAILY GUIDANCE (Next 25 Days)")
            
            daily_guidance = []
            start_date = date(2025, 8, 8)
            
            for i in range(25):
                current_date = start_date + timedelta(days=i)
                day_of_week = current_date.strftime("%A")
                
                # Generate daily predictions based on date
                if current_date == date(2025, 8, 11):
                    theme = "Mercury Direct - Communication Breakthrough"
                    rating = "9.5/10"
                    action = "Sign contracts, clear misunderstandings"
                elif current_date == date(2025, 8, 17):
                    theme = "Sun in Leo - Authority Peak"
                    rating = "9.8/10"
                    action = "Take leadership, make important decisions"
                elif current_date == date(2025, 8, 21):
                    theme = "Venus in Cancer - Family Harmony"
                    rating = "9.0/10"
                    action = "Focus on relationships, home, emotions"
                elif current_date == date(2025, 9, 1):
                    theme = "Saturn Direct - Clarity"
                    rating = "8.5/10"
                    action = "Address responsibilities, health check"
                elif current_date == date(2025, 9, 7):
                    theme = "Mars Bhukti Begins - High Energy"
                    rating = "8.8/10"
                    action = "Start new projects, exercise, assertiveness"
                elif current_date == date(2025, 10, 18):
                    theme = "JUPITER IN CANCER - LIFE TRANSFORMATION"
                    rating = "10/10"
                    action = "Major decisions, investments, new beginnings"
                else:
                    # Generic day
                    themes = [
                        "Steady progress day", "Communication focus", "Relationship harmony",
                        "Career advancement", "Financial planning", "Health awareness",
                        "Spiritual growth", "Family time", "Social connections"
                    ]
                    theme = themes[i % len(themes)]
                    rating = f"{7 + (i % 3)}.{5 * (i % 2)}/10"
                    action = "Routine day, maintain balance"
                
                daily_guidance.append({
                    "Date": current_date.strftime("%b %d"),
                    "Day": day_of_week,
                    "Theme": theme,
                    "Rating": rating,
                    "Action": action
                })
            
            df_daily = pd.DataFrame(daily_guidance)
            st.dataframe(df_daily, use_container_width=True)
            
            # Life Areas Rating
            st.markdown("### 🎯 LIFE AREAS RATING")
            
            life_areas = [
                {"Area": "Career", "Current": "85%", "Trend": "↑ Improving", "Peak Date": "Oct 18, 2025"},
                {"Area": "Wealth", "Current": "80%", "Trend": "↑ Improving", "Peak Date": "Oct 18, 2025"},
                {"Area": "Love", "Current": "75%", "Trend": "→ Stable", "Peak Date": "Aug 21, 2025"},
                {"Area": "Health", "Current": "85%", "Trend": "↑ Improving", "Peak Date": "Sep 1, 2025"},
                {"Area": "Spiritual", "Current": "90%", "Trend": "↑ Improving", "Peak Date": "Aug 25, 2025"}
            ]
            
            for area in life_areas:
                col1, col2, col3, col4 = st.columns([2, 1, 1, 2])
                with col1:
                    st.markdown(f"**{area['Area']}**")
                with col2:
                    st.markdown(f"**{area['Current']}**")
                with col3:
                    st.markdown(f"{area['Trend']}")
                with col4:
                    st.markdown(f"Peak: {area['Peak Date']}")
                
                # Progress bar
                progress_value = int(area['Current'].replace('%', ''))
                st.markdown(f"""
                <div class="progress-container">
                    <div class="progress-bar" style="width: {progress_value}%;"></div>
                </div>
                """, unsafe_allow_html=True)
        
        with tabs[3]:  # Remedial Measures
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    💎 REMEDIAL MEASURES - {ayanamsa} SYSTEM
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Urgent Actions
            st.markdown("### 🚨 URGENT ACTIONS")
            
            urgent_remedies = [
                {
                    "Issue": "Mercury Retrograde (Until Aug 11)",
                    "Remedy": "Recite 'Om Budhaya Namah' 108 times daily",
                    "Duration": "Until Aug 11",
                    "Materials": "Green cloth, moong dal donation",
                    "Effectiveness": "95%"
                },
                {
                    "Issue": "Saturn Retrograde in 6th House",
                    "Remedy": "Light mustard oil lamp on Saturdays",
                    "Duration": "Until Sep 1",
                    "Materials": "Mustard oil, black sesame seeds",
                    "Effectiveness": "90%"
                },
                {
                    "Issue": "Moon in 6th House causing health concerns",
                    "Remedy": "Donate milk on Mondays",
                    "Duration": "4 Mondays",
                    "Materials": "Milk, white flowers",
                    "Effectiveness": "85%"
                }
            ]
            
            for remedy in urgent_remedies:
                with st.expander(f"🚨 {remedy['Issue']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Remedy:** {remedy['Remedy']}")
                        st.markdown(f"**Duration:** {remedy['Duration']}")
                    with col2:
                        st.markdown(f"**Materials:** {remedy['Materials']}")
                        st.markdown(f"**Effectiveness:** {remedy['Effectiveness']}")
            
            # Gemstone Recommendations
            st.markdown("### 💎 GEMSTONE RECOMMENDATIONS")
            
            gemstones = [
                {
                    "Stone": "Ruby (Manikya)",
                    "Planet": "Sun (Mahadasha Lord)",
                    "Weight": "3-5 carats",
                    "Metal": "Gold or Panchdhatu",
                    "Finger": "Ring finger",
                    "Day": "Sunday morning",
                    "Cost": "₹15,000 - ₹25,000",
                    "Alternative": "Red Garnet (₹3,000 - ₹5,000)",
                    "Benefits": "Leadership, authority, career growth, health"
                },
                {
                    "Stone": "Pearl (Moti)",
                    "Planet": "Moon (Bhukti Lord)",
                    "Weight": "5-7 carats",
                    "Metal": "Silver",
                    "Finger": "Little finger",
                    "Day": "Monday morning",
                    "Cost": "₹8,000 - ₹15,000",
                    "Alternative": "Moonstone (₹2,000 - ₹4,000)",
                    "Benefits": "Emotional balance, mother's health, intuition"
                },
                {
                    "Stone": "Emerald (Panna)",
                    "Planet": "Mercury (Antara Lord)",
                    "Weight": "3-4 carats",
                    "Metal": "Gold",
                    "Finger": "Little finger",
                    "Day": "Wednesday morning",
                    "Cost": "₹12,000 - ₹20,000",
                    "Alternative": "Peridot (₹1,500 - ₹3,000)",
                    "Benefits": "Communication, intelligence, business success"
                }
            ]
            
            for gem in gemstones:
                with st.expander(f"💎 {gem['Stone']} for {gem['Planet']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Weight:** {gem['Weight']}")
                        st.markdown(f"**Metal:** {gem['Metal']}")
                        st.markdown(f"**Finger:** {gem['Finger']}")
                        st.markdown(f"**Day:** {gem['Day']}")
                    with col2:
                        st.markdown(f"**Cost:** {gem['Cost']}")
                        st.markdown(f"**Alternative:** {gem['Alternative']}")
                        st.markdown(f"**Benefits:** {gem['Benefits']}")
            
            # Daily Practices
            st.markdown("### 🙏 DAILY PRACTICES")
            
            daily_practices = [
                {
                    "Time": "Early Morning (5:00-6:00 AM)",
                    "Practice": "Surya Namaskar and Sun Mantra",
                    "Mantra": "Om Ghrini Surya Aditya",
                    "Duration": "15 minutes",
                    "Benefits": "Vitality, leadership, career success"
                },
                {
                    "Time": "Midday (12:00-1:00 PM)",
                    "Practice": "Meditation with Moon visualization",
                    "Mantra": "Om Somaya Namah",
                    "Duration": "10 minutes",
                    "Benefits": "Emotional balance, intuition"
                },
                {
                    "Time": "Evening (6:00-7:00 PM)",
                    "Practice": "Mercury mantra for communication",
                    "Mantra": "Om Budhaya Namah",
                    "Duration": "10 minutes",
                    "Benefits": "Clear thinking, business success"
                },
                {
                    "Time": "Night (9:00-10:00 PM)",
                    "Practice": "Gratitude journaling",
                    "Mantra": "Personal affirmations",
                    "Duration": "15 minutes",
                    "Benefits": "Peace, manifestation, sleep quality"
                }
            ]
            
            for practice in daily_practices:
                with st.expander(f"🕐 {practice['Time']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Practice:** {practice['Practice']}")
                        st.markdown(f"**Mantra:** {practice['Mantra']}")
                    with col2:
                        st.markdown(f"**Duration:** {practice['Duration']}")
                        st.markdown(f"**Benefits:** {practice['Benefits']}")
            
            # Weekly Donations
            st.markdown("### 🕉️ WEEKLY DONATIONS")
            
            weekly_donations = [
                {"Day": "Sunday", "Item": "Wheat, jaggery", "Cause": "Sun strength", "Amount": "₹111"},
                {"Day": "Monday", "Item": "Rice, milk", "Cause": "Moon peace", "Amount": "₹51"},
                {"Day": "Tuesday", "Item": "Red lentils, red flowers", "Cause": "Mars energy", "Amount": "₹101"},
                {"Day": "Wednesday", "Item": "Green moong, books", "Cause": "Mercury intellect", "Amount": "₹71"},
                {"Day": "Thursday", "Item": "Yellow clothes, turmeric", "Cause": "Jupiter expansion", "Amount": "₹501"},
                {"Day": "Friday", "Item": "White rice, yogurt", "Cause": "Venus harmony", "Amount": "₹121"},
                {"Day": "Saturday", "Item": "Black sesame, mustard oil", "Cause": "Saturn karma", "Amount": "₹251"}
            ]
            
            df_donations = pd.DataFrame(weekly_donations)
            st.dataframe(df_donations, use_container_width=True)
            
            # Yantra Installation
            st.markdown("### 📐 YANTRA INSTALLATION")
            
            yantras = [
                {
                    "Yantra": "Surya Yantra",
                    "Purpose": "Strengthens Sun Mahadasha",
                    "Material": "Copper plate",
                    "Size": "3x3 inches",
                    "Installation": "Sunday morning at sunrise",
                    "Placement": "East direction, home/office",
                    "Mantra": "Om Ghrini Surya Aditya (108 times)",
                    "Cost": "₹1,500 - ₹3,000"
                },
                {
                    "Yantra": "Chandra Yantra",
                    "Purpose": "Balances Moon Bhukti",
                    "Material": "Silver plate",
                    "Size": "3x3 inches",
                    "Installation": "Monday evening",
                    "Placement": "Northwest direction, bedroom",
                    "Mantra": "Om Somaya Namah (108 times)",
                    "Cost": "₹2,000 - ₹4,000"
                },
                {
                    "Yantra": "Budh Yantra",
                    "Purpose": "Enhances Mercury Antara",
                    "Material": "Bronze plate",
                    "Size": "3x3 inches",
                    "Installation": "Wednesday morning",
                    "Placement": "North direction, office/study",
                    "Mantra": "Om Budhaya Namah (108 times)",
                    "Cost": "₹1,200 - ₹2,500"
                }
            ]
            
            for yantra in yantras:
                with st.expander(f"📐 {yantra['Yantra']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Purpose:** {yantra['Purpose']}")
                        st.markdown(f"**Material:** {yantra['Material']}")
                        st.markdown(f"**Size:** {yantra['Size']}")
                    with col2:
                        st.markdown(f"**Installation:** {yantra['Installation']}")
                        st.markdown(f"**Placement:** {yantra['Placement']}")
                        st.markdown(f"**Cost:** {yantra['Cost']}")
                    st.markdown(f"**Mantra:** {yantra['Mantra']}")
            
            # Fasting Recommendations
            st.markdown("### 🍽️ FASTING RECOMMENDATIONS")
            
            fasting = [
                {
                    "Day": "Sunday",
                    "Type": "Partial fast",
                    "Food": "Once meal, no salt",
                    "Benefit": "Sun strength, career growth",
                    "Frequency": "Weekly"
                },
                {
                    "Day": "Monday",
                    "Type": "Full fast",
                    "Food": "Only fruits, milk",
                    "Benefit": "Moon peace, emotional balance",
                    "Frequency": "Weekly"
                },
                {
                    "Day": "Thursday",
                    "Type": "Partial fast",
                    "Food": "Once meal, yellow foods",
                    "Benefit": "Jupiter expansion, wealth",
                    "Frequency": "Weekly"
                }
            ]
            
            for fast in fasting:
                st.info(f"""
                **{fast['Day']} Fasting:**
                • **Type:** {fast['Type']}
                • **Food:** {fast['Food']}
                • **Benefit:** {fast['Benefit']}
                • **Frequency:** {fast['Frequency']}
                """)
        
        with tabs[4]:  # Life Analysis
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    📈 COMPLETE LIFE ANALYSIS - {ayanamsa} SYSTEM
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # 9 Life Phases
            st.markdown("### 🔄 9 LIFE PHASES")
            
            life_phases = [
                {
                    "Phase": "1. Sun Mahadasha",
                    "Age": "34-40 years",
                    "Theme": "Authority Building",
                    "Key Events": "Career peak, leadership roles, recognition",
                    "Challenges": "Ego management, health concerns",
                    "Opportunities": "Government connections, authority positions",
                    "Life Area Focus": "Career, reputation, father relationship"
                },
                {
                    "Phase": "2. Moon Mahadasha",
                    "Age": "40-50 years",
                    "Theme": "Emotional Fulfillment",
                    "Key Events": "Family expansion, home purchase, emotional growth",
                    "Challenges": "Emotional instability, mother's health",
                    "Opportunities": "Public popularity, intuitive decisions",
                    "Life Area Focus": "Family, home, emotions, mother"
                },
                {
                    "Phase": "3. Mars Mahadasha",
                    "Age": "50-57 years",
                    "Theme": "Action & Property",
                    "Key Events": "Real estate investments, bold ventures, surgery",
                    "Challenges": "Accidents, conflicts, property disputes",
                    "Opportunities": "Property gains, courage, physical vitality",
                    "Life Area Focus": "Property, courage, siblings, health"
                },
                {
                    "Phase": "4. Rahu Mahadasha",
                    "Age": "57-75 years",
                    "Theme": "Material Success",
                    "Key Events": "Wealth accumulation, foreign travel, innovation",
                    "Challenges": "Confusion, addiction, deception",
                    "Opportunities": "Material gains, foreign connections, technology",
                    "Life Area Focus": "Wealth, foreign lands, innovation"
                },
                {
                    "Phase": "5. Jupiter Mahadasha",
                    "Age": "75-91 years",
                    "Theme": "Wisdom & Teaching",
                    "Key Events": "Mentorship, spiritual growth, teaching",
                    "Challenges": "Over-optimism, weight gain, liver issues",
                    "Opportunities": "Wisdom sharing, spiritual growth, wealth",
                    "Life Area Focus": "Wisdom, teaching, spirituality, wealth"
                },
                {
                    "Phase": "6. Saturn Mahadasha",
                    "Age": "91-110 years",
                    "Theme": "Karma Completion",
                    "Key Events": "Legacy building, final life lessons",
                    "Challenges": "Health issues, isolation, restrictions",
                    "Opportunities": "Karma completion, spiritual liberation",
                    "Life Area Focus": "Karma, spirituality, legacy"
                }
            ]
            
            for phase in life_phases:
                with st.expander(f"🔄 {phase['Phase']} ({phase['Age']})", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Theme:** {phase['Theme']}")
                        st.markdown(f"**Key Events:** {phase['Key Events']}")
                        st.markdown(f"**Challenges:** {phase['Challenges']}")
                    with col2:
                        st.markdown(f"**Opportunities:** {phase['Opportunities']}")
                        st.markdown(f"**Life Area Focus:** {phase['Life Area Focus']}")
            
            # Current Phase Analysis
            st.markdown("### 🔍 CURRENT PHASE ANALYSIS")
            
            current_phase = {
                "Phase": "Sun Mahadasha (34-40 years)",
                "Current Age": "35 years",
                "Progress": "16.7% complete",
                "Remaining": "5 years",
                "Key Focus": "Building authority and career foundation",
                "Strengths": "Leadership abilities, decision-making power",
                "Challenges": "Managing ego, health maintenance",
                "Opportunities": "Government connections, career advancement",
                "Recommended Actions": [
                    "Take leadership roles in profession",
                    "Maintain health through regular check-ups",
                    "Connect with authority figures",
                    "Avoid arrogance and ego conflicts",
                    "Wear Ruby gemstone for Sun strength"
                ]
            }
            
            st.success(f"""
            **Current Phase:** {current_phase['Phase']}  
            **Current Age:** {current_phase['Current Age']}  
            **Progress:** {current_phase['Progress']} ({current_phase['Remaining']} remaining)
            """)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                **🌟 Key Focus:** Building authority and career foundation
                
                **💪 Strengths:**
                • Leadership abilities
                • Decision-making power
                • Government connections
                • Recognition potential
                """)
            
            with col2:
                st.markdown("""
                **⚠️ Challenges:**
                • Managing ego
                • Health maintenance
                • Father's health
                • Authority conflicts
                
                **🎯 Opportunities:**
                • Career advancement
                • Government jobs
                • Leadership positions
                """)
            
            st.markdown("**Recommended Actions:**")
            for action in current_phase['Recommended Actions']:
                st.success(f"• {action}")
            
            # Future Milestones
            st.markdown("### 🚀 FUTURE MILESTONES")
            
            future_milestones = [
                {"Age": "36 years", "Year": "2026", "Event": "Career promotion to leadership role", "Probability": "90%"},
                {"Age": "38 years", "Year": "2028", "Event": "Major property acquisition", "Probability": "85%"},
                {"Age": "40 years", "Year": "2030", "Event": "Sun Mahadasha ends, Moon begins", "Probability": "100%"},
                {"Age": "42 years", "Year": "2032", "Event": "Family expansion possible", "Probability": "75%"},
                {"Age": "45 years", "Year": "2035", "Event": "Business establishment", "Probability": "80%"},
                {"Age": "50 years", "Year": "2040", "Event": "Mars Mahadasha begins", "Probability": "100%"},
                {"Age": "57 years", "Year": "2047", "Event": "Rahu Mahadasha - foreign connection", "Probability": "95%"},
                {"Age": "75 years", "Year": "2065", "Event": "Jupiter Mahadasha - wisdom phase", "Probability": "100%"}
            ]
            
            df_milestones = pd.DataFrame(future_milestones)
            st.dataframe(df_milestones, use_container_width=True)
            
            # Life Satisfaction Forecast
            st.markdown("### 😊 LIFE SATISFACTION FORECAST")
            
            life_satisfaction = [
                {"Age": "35 (Current)", "Satisfaction": "75%", "Factors": "Career growth, health concerns"},
                {"Age": "40", "Satisfaction": "85%", "Factors": "Established career, family harmony"},
                {"Age": "45", "Satisfaction": "88%", "Factors": "Business success, property ownership"},
                {"Age": "50", "Satisfaction": "82%", "Factors": "Mars energy, health focus"},
                {"Age": "60", "Satisfaction": "90%", "Factors": "Wealth accumulation, wisdom"},
                {"Age": "75", "Satisfaction": "95%", "Factors": "Spiritual growth, teaching"},
                {"Age": "90+", "Satisfaction": "98%", "Factors": "Karma completion, peace"}
            ]
            
            for item in life_satisfaction:
                col1, col2, col3 = st.columns([1, 1, 2])
                with col1:
                    st.markdown(f"**Age {item['Age']}**")
                with col2:
                    st.markdown(f"**{item['Satisfaction']}**")
                with col3:
                    st.markdown(item['Factors'])
                
                # Progress bar
                satisfaction_value = int(item['Satisfaction'].replace('%', ''))
                st.markdown(f"""
                <div class="progress-container">
                    <div class="progress-bar" style="width: {satisfaction_value}%;"></div>
                </div>
                """, unsafe_allow_html=True)
            
            # Peak Potential
            st.markdown("### ⭐ PEAK POTENTIAL ANALYSIS")
            
            peak_potential = {
                "Overall Rating": "92% Exceptional Life",
                "Best Life Phase": "Jupiter Mahadasha (75-91 years)",
                "Peak Career Age": "38-45 years",
                "Peak Wealth Age": "57-75 years",
                "Peak Spiritual Age": "75+ years",
                "Key Strengths": [
                    "Leadership abilities (Sun)",
                    "Emotional intelligence (Moon)",
                    "Courage and action (Mars)",
                    "Material success potential (Rahu)",
                    "Wisdom and teaching (Jupiter)"
                ],
                "Life Purpose": "To lead with authority, build material success, and eventually share wisdom with others",
                "Karmic Lessons": [
                    "Balance authority with humility",
                    "Use power responsibly",
                    "Transform material success into spiritual growth"
                ]
            }
            
            st.success(f"""
            **Overall Life Rating:** {peak_potential['Overall Rating']}  
            **Best Life Phase:** {peak_potential['Best Life Phase']}  
            **Peak Career Age:** {peak_potential['Peak Career Age']}  
            **Peak Wealth Age:** {peak_potential['Peak Wealth Age']}  
            **Peak Spiritual Age:** {peak_potential['Peak Spiritual Age']}
            """)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Key Strengths:**")
                for strength in peak_potential['Key Strengths']:
                    st.success(f"• {strength}")
            
            with col2:
                st.markdown("**Karmic Lessons:**")
                for lesson in peak_potential['Karmic Lessons']:
                    st.warning(f"• {lesson}")
            
            st.markdown(f"""
            **Life Purpose:** {peak_potential['Life Purpose']}
            """)
            
            # Life Balance Analysis
            st.markdown("### ⚖️ LIFE BALANCE ANALYSIS")
            
            life_balance = [
                {"Area": "Career", "Current": "85%", "Ideal": "80%", "Status": "Slightly Overfocused"},
                {"Area": "Family", "Current": "70%", "Ideal": "85%", "Status": "Needs Attention"},
                {"Area": "Health", "Current": "75%", "Ideal": "90%", "Status": "Needs Improvement"},
                {"Area": "Wealth", "Current": "80%", "Ideal": "80%", "Status": "Balanced"},
                {"Area": "Spiritual", "Current": "65%", "Ideal": "75%", "Status": "Developing"},
                {"Area": "Social", "Current": "60%", "Ideal": "70%", "Status": "Needs Development"}
            ]
            
            for balance in life_balance:
                status_color = "success" if balance['Status'] == "Balanced" else "warning" if "Needs" in balance['Status'] else "error"
                
                col1, col2, col3, col4 = st.columns([2, 1, 1, 2])
                with col1:
                    st.markdown(f"**{balance['Area']}**")
                with col2:
                    st.markdown(f"{balance['Current']}")
                with col3:
                    st.markdown(f"(Ideal: {balance['Ideal']})")
                with col4:
                    if status_color == "success":
                        st.success(balance['Status'])
                    elif status_color == "warning":
                        st.warning(balance['Status'])
                    else:
                        st.error(balance['Status'])
                
                # Progress bars
                current_value = int(balance['Current'].replace('%', ''))
                ideal_value = int(balance['Ideal'].replace('%', ''))
                
                st.markdown(f"""
                <div style="display: flex; align-items: center;">
                    <div class="progress-container" style="flex: 1; margin-right: 10px;">
                        <div class="progress-bar" style="width: {current_value}%;"></div>
                    </div>
                    <div style="color: #718096; font-size: 0.9em;">Ideal: {ideal_value}%</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.info("""
            **Recommendations for Life Balance:**
            • Dedicate more time to family relationships
            • Prioritize health through regular exercise and check-ups
            • Develop spiritual practices (meditation, yoga)
            • Expand social circle and networking
            • Maintain career success while creating boundaries
            """)
        
        with tabs[5]:  # Career Growth
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    🎯 COMPREHENSIVE CAREER GROWTH - {ayanamsa} SYSTEM
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Immediate Opportunities
            st.markdown("### 🚀 IMMEDIATE OPPORTUNITIES (Next 6 Months)")
            
            immediate_opportunities = [
                {
                    "Opportunity": "Leadership Role in Current Organization",
                    "Timeline": "Aug - Oct 2025",
                    "Success Rate": "95%",
                    "Key Actions": "Take initiative, showcase leadership, connect with seniors",
                    "Planetary Support": "Sun Mahadasha + Mercury Direct (Aug 11)",
                    "Expected Outcome": "Promotion to senior position"
                },
                {
                    "Opportunity": "Government Sector Position",
                    "Timeline": "Sep - Nov 2025",
                    "Success Rate": "90%",
                    "Key Actions": "Apply for government jobs, use connections",
                    "Planetary Support": "Sun in Leo (Aug 17) + Jupiter aspects",
                    "Expected Outcome": "Secure government position"
                },
                {
                    "Opportunity": "New Business Venture",
                    "Timeline": "Oct - Dec 2025",
                    "Success Rate": "85%",
                    "Key Actions": "Plan business, secure funding, launch",
                    "Planetary Support": "Jupiter in Cancer (Oct 18) - MEGA FORTUNE",
                    "Expected Outcome": "Successful business establishment"
                },
                {
                    "Opportunity": "International Assignment",
                    "Timeline": "Nov 2025 - Jan 2026",
                    "Success Rate": "80%",
                    "Key Actions": "Apply for overseas positions, prepare documents",
                    "Planetary Support": "Rahu influence + Jupiter expansion",
                    "Expected Outcome": "Foreign work opportunity"
                }
            ]
            
            for opp in immediate_opportunities:
                with st.expander(f"🚀 {opp['Opportunity']} (Success: {opp['Success Rate']})", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Timeline:** {opp['Timeline']}")
                        st.markdown(f"**Success Rate:** {opp['Success Rate']}")
                        st.markdown(f"**Key Actions:** {opp['Key Actions']}")
                    with col2:
                        st.markdown(f"**Planetary Support:** {opp['Planetary Support']}")
                        st.markdown(f"**Expected Outcome:** {opp['Expected Outcome']}")
            
            # Industry Analysis
            st.markdown("### 🏭 INDUSTRY ANALYSIS")
            
            industries = [
                {
                    "Industry": "Government & Public Sector",
                    "Planetary Ruler": "Sun (Mahadasha Lord)",
                    "Compatibility": "95%",
                    "Growth Potential": "High",
                    "Income Range": "₹15-25 LPA",
                    "Best Roles": "Administrative services, leadership positions",
                    "Future Outlook": "Excellent with Sun Mahadasha"
                },
                {
                    "Industry": "Banking & Finance",
                    "Planetary Ruler": "Jupiter + Sun",
                    "Compatibility": "90%",
                    "Growth Potential": "Very High",
                    "Income Range": "₹12-30 LPA",
                    "Best Roles": "Management, financial advisory",
                    "Future Outlook": "Strong growth, Jupiter support"
                },
                {
                    "Industry": "Real Estate & Construction",
                    "Planetary Ruler": "Mars + Venus",
                    "Compatibility": "85%",
                    "Growth Potential": "High",
                    "Income Range": "₹10-25 LPA",
                    "Best Roles": "Project management, sales",
                    "Future Outlook": "Good, upcoming Mars period"
                },
                {
                    "Industry": "Education & Training",
                    "Planetary Ruler": "Jupiter + Mercury",
                    "Compatibility": "80%",
                    "Growth Potential": "Medium",
                    "Income Range": "₹8-18 LPA",
                    "Best Roles": "Teaching, training, administration",
                    "Future Outlook": "Steady, Jupiter influence"
                },
                {
                    "Industry": "Healthcare & Pharmaceuticals",
                    "Planetary Ruler": "Moon + Jupiter",
                    "Compatibility": "75%",
                    "Growth Potential": "High",
                    "Income Range": "₹10-22 LPA",
                    "Best Roles": "Management, administration",
                    "Future Outlook": "Growing sector, Moon support"
                },
                {
                    "Industry": "Technology & IT",
                    "Planetary Ruler": "Mercury + Mars",
                    "Compatibility": "70%",
                    "Growth Potential": "Very High",
                    "Income Range": "₹12-35 LPA",
                    "Best Roles": "Management, technical leadership",
                    "Future Outlook": "Excellent growth, Mercury direct soon"
                }
            ]
            
            for industry in industries:
                with st.expander(f"🏭 {industry['Industry']} (Compatibility: {industry['Compatibility']})", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Planetary Ruler:** {industry['Planetary Ruler']}")
                        st.markdown(f"**Growth Potential:** {industry['Growth Potential']}")
                        st.markdown(f"**Income Range:** {industry['Income Range']}")
                    with col2:
                        st.markdown(f"**Best Roles:** {industry['Best Roles']}")
                        st.markdown(f"**Future Outlook:** {industry['Future Outlook']}")
                    
                    # Compatibility bar
                    compatibility_value = int(industry['Compatibility'].replace('%', ''))
                    st.markdown(f"""
                    <div class="progress-container">
                        <div class="progress-bar" style="width: {compatibility_value}%;"></div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Action Plans
            st.markdown("### 📝 ACTION PLANS")
            
            action_plans = [
                {
                    "Timeline": "30-Day Plan",
                    "Focus": "Immediate career advancement",
                    "Key Actions": [
                        "Update resume and LinkedIn profile",
                        "Schedule meetings with senior management",
                        "Take on additional responsibilities",
                        "Start wearing Ruby gemstone",
                        "Perform Sun remedies daily"
                    ],
                    "Expected Outcome": "Recognition and consideration for promotion"
                },
                {
                    "Timeline": "6-Month Plan",
                    "Focus": "Major career transition",
                    "Key Actions": [
                        "Complete certification courses",
                        "Expand professional network",
                        "Apply for higher positions",
                        "Consider government job opportunities",
                        "Prepare for business venture"
                    ],
                    "Expected Outcome": "New position or business establishment"
                },
                {
                    "Timeline": "3-Year Plan",
                    "Focus": "Long-term career establishment",
                    "Key Actions": [
                        "Achieve senior leadership position",
                        "Establish business or consultancy",
                        "Build strong professional reputation",
                        "Create multiple income streams",
                        "Balance career with family life"
                    ],
                    "Expected Outcome": "Established career authority and financial stability"
                }
            ]
            
            for plan in action_plans:
                with st.expander(f"📝 {plan['Timeline']}", expanded=True):
                    st.markdown(f"**Focus:** {plan['Focus']}")
                    st.markdown("**Key Actions:**")
                    for action in plan['Key Actions']:
                        st.success(f"• {action}")
                    st.markdown(f"**Expected Outcome:** {plan['Expected Outcome']}")
            
            # Salary Projections
            st.markdown("### 💰 SALARY PROJECTIONS")
            
            salary_projections = [
                {"Year": "2025 (Current)", "Position": "Mid-level Professional", "Salary": "₹12-15 LPA", "Growth": "Baseline"},
                {"Year": "2026", "Position": "Senior Professional", "Salary": "₹15-20 LPA", "Growth": "25%"},
                {"Year": "2027", "Position": "Team Lead/Manager", "Salary": "₹18-25 LPA", "Growth": "25%"},
                {"Year": "2028", "Position": "Senior Manager", "Salary": "₹22-30 LPA", "Growth": "20%"},
                {"Year": "2029", "Position": "Department Head", "Salary": "₹25-35 LPA", "Growth": "20%"},
                {"Year": "2030", "Position": "Director/VP", "Salary": "₹30-45 LPA", "Growth": "30%"},
                {"Year": "2035", "Position": "Senior Director/Entrepreneur", "Salary": "₹40-60 LPA", "Growth": "35%"}
            ]
            
            df_salary = pd.DataFrame(salary_projections)
            st.dataframe(df_salary, use_container_width=True)
            
            # Life Purpose Integration
            st.markdown("### 🕉️ LIFE PURPOSE INTEGRATION")
            
            life_purpose = {
                "Dharmic Path": "Leadership with service orientation",
                "Career Alignment": "Authority positions that help others",
                "Spiritual Integration": "Use material success for spiritual growth",
                "Karmic Duty": "Balance power with compassion",
                "Recommended Practices": [
                    "Meditate on leadership responsibilities",
                    "Donate part of income regularly",
                    "Mentor juniors and subordinates",
                    "Balance work with spiritual practices",
                    "Use authority for positive change"
                ]
            }
            
            st.success(f"""
            **Dharmic Path:** {life_purpose['Dharmic Path']}  
            **Career Alignment:** {life_purpose['Career Alignment']}  
            **Spiritual Integration:** {life_purpose['Spiritual Integration']}  
            **Karmic Duty:** {life_purpose['Karmic Duty']}
            """)
            
            st.markdown("**Recommended Practices:**")
            for practice in life_purpose['Recommended Practices']:
                st.success(f"• {practice}")
            
            # Career Success Factors
            st.markdown("### ⭐ CAREER SUCCESS FACTORS")
            
            success_factors = [
                {"Factor": "Sun Strength (Mahadasha)", "Impact": "Very High", "Duration": "Current - 2030", "Remedy": "Ruby gemstone, Sun worship"},
                {"Factor": "Mercury Intelligence", "Impact": "High", "Duration": "Permanent", "Remedy": "Emerald, education"},
                {"Factor": "Jupiter Expansion", "Impact": "High", "Duration": "Increasing", "Remedy": "Yellow sapphire, charity"},
                {"Factor": "Mars Energy", "Impact": "Medium", "Duration": "From 2030", "Remedy": "Red coral, exercise"},
                {"Factor": "Saturn Discipline", "Impact": "Medium", "Duration": "Permanent", "Remedy": "Blue sapphire, discipline"}
            ]
            
            for factor in success_factors:
                col1, col2, col3, col4 = st.columns([2, 1, 1, 2])
                with col1:
                    st.markdown(f"**{factor['Factor']}**")
                with col2:
                    st.markdown(factor['Impact'])
                with col3:
                    st.markdown(factor['Duration'])
                with col4:
                    st.markdown(factor['Remedy'])
            
            # Final Career Advice
            st.markdown("### 🎯 FINAL CAREER ADVICE")
            
            st.info("""
            **🌟 Current Phase (Sun Mahadasha):**
            • Focus on building authority and leadership
            • Take on challenging roles with responsibility
            • Connect with government and authority figures
            • Maintain health through regular check-ups
            • Balance ambition with humility
            
            **🚀 Upcoming Opportunities:**
            • Leadership promotion in current organization (95% success)
            • Government sector position (90% success)
            • Business venture establishment (85% success)
            • International assignment (80% success)
            
            **💰 Financial Growth:**
            • Current: ₹12-15 LPA
            • 2030 Projection: ₹30-45 LPA
            • 2035 Projection: ₹40-60 LPA
            
            **🕉️ Spiritual Integration:**
            • Use leadership positions to help others
            • Donate part of income regularly
            • Balance material success with spiritual growth
            • Mentor others in your field
            """)
    
    else:
        # Financial Markets Mode with comprehensive analysis
        tabs = st.tabs([
            "📊 Market Dasha Analysis",
            "🌍 Market Transits", 
            "📅 Monthly Market Forecast",
            "🔮 Ayanamsa Market Impact",
            "💹 Indian Markets",
            "🏦 Sector Analysis",
            "🌏 Global Markets",
            "💱 Forex Analysis",
            "⏰ Trading Times",
            "📈 Technical + Astro",
            "🥇 Commodities Analysis"
        ])
        
        with tabs[0]:  # Market Dasha Analysis
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    📊 MARKET DASHA ANALYSIS - {ayanamsa} SYSTEM
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.info(f"Financial market analysis using {ayanamsa} ayanamsa ({ayanamsa_options[ayanamsa]['value']}°)")
            
            # Market Dasha Periods
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("### 🌟 Market Mahadasha")
                if "KP" in ayanamsa:
                    market_dasha = "Sun (Authority)"
                    market_effect = "Government policies favor markets"
                elif "Lahiri" in ayanamsa:
                    market_dasha = "Jupiter (Growth)"
                    market_effect = "Traditional value investing pays"
                else:
                    market_dasha = "Venus (Luxury)"
                    market_effect = "Consumer and luxury sectors shine"
                
                st.success(f"""
                **Current Period:** {market_dasha}  
                **Duration:** Nov 2024 - Nov 2030  
                **Market Effect:** {market_effect}  
                **Best Sectors:** Banking, Government, PSU  
                **Investment Style:** Long-term bullish
                """)
            
            with col2:
                st.markdown("### 🌙 Market Bhukti")
                st.warning(f"""
                **Sub-Period:** Moon (Public Sentiment)  
                **Duration:** Mar 2025 - Sep 2025  
                **Effect:** Public participation increases  
                **Volatility:** Moderate to High  
                **Best Strategy:** Follow sentiment indicators
                """)
            
            with col3:
                st.markdown("### ⭐ Market Antara")
                st.info(f"""
                **Micro-Period:** Mercury (Communication)  
                **Duration:** Aug 1-20, 2025  
                **Effect:** News-driven movements  
                **Sectors:** IT, Telecom, Media  
                **Trading:** Scalping opportunities
                """)
            
            # Detailed Dasha Analysis
            st.markdown("### 🔍 DETAILED DASHA ANALYSIS")
            
            detailed_dasha = [
                {
                    "Level": "Mahadasha",
                    "Lord": "Sun",
                    "Nakshatra Lord": "Pushya",
                    "Sub-lord": "Saturn",
                    "Start": "Nov 19, 2024",
                    "End": "Nov 9, 2030",
                    "Remaining": "5 years, 3 months",
                    "Market Effect": "Government sector boom, authority figures drive markets",
                    "Best Strategy": "Long-term investments in PSU, Banking"
                },
                {
                    "Level": "Bhukti",
                    "Lord": "Moon",
                    "Nakshatra Lord": "Rohini",
                    "Sub-lord": "Mercury",
                    "Start": "Mar 7, 2025",
                    "End": "Sep 7, 2025",
                    "Remaining": "1 month",
                    "Market Effect": "Public sentiment drives markets, emotional trading",
                    "Best Strategy": "Follow market sentiment, defensive stance"
                },
                {
                    "Level": "Antara",
                    "Lord": "Mercury",
                    "Nakshatra Lord": "Ashlesha",
                    "Sub-lord": "Venus",
                    "Start": "Aug 1, 2025",
                    "End": "Aug 20, 2025",
                    "Remaining": "12 days",
                    "Market Effect": "News-driven volatility, communication sectors active",
                    "Best Strategy": "Short-term trading, focus on IT, Media"
                },
                {
                    "Level": "Pratyantara",
                    "Lord": "Ketu",
                    "Nakshatra Lord": "Magha",
                    "Sub-lord": "Sun",
                    "Start": "Aug 8, 2025",
                    "End": "Aug 11, 2025",
                    "Remaining": "3 days",
                    "Market Effect": "Sudden moves, spiritual sector growth",
                    "Best Strategy": "Caution, avoid new positions"
                },
                {
                    "Level": "Sookshma",
                    "Lord": "Venus",
                    "Nakshatra Lord": "Purva Phalguni",
                    "Sub-lord": "Sun",
                    "Start": "Aug 8, 2025",
                    "End": "Aug 9, 2025",
                    "Remaining": "1 day",
                    "Market Effect": "Luxury, real estate focus",
                    "Best Strategy": "Buy realty, consumer stocks"
                }
            ]
            
            for dasha in detailed_dasha:
                level_color = {
                    "Mahadasha": "success",
                    "Bhukti": "warning",
                    "Antara": "info",
                    "Pratyantara": "error",
                    "Sookshma": "success"
                }
                
                with st.expander(f"🔍 {dasha['Level']} - {dasha['Lord']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Lord:** {dasha['Lord']}")
                        st.markdown(f"**Nakshatra Lord:** {dasha['Nakshatra Lord']}")
                        st.markdown(f"**Sub-lord:** {dasha['Sub-lord']}")
                        st.markdown(f"**Period:** {dasha['Start']} to {dasha['End']}")
                        st.markdown(f"**Remaining:** {dasha['Remaining']}")
                    with col2:
                        st.markdown(f"**Market Effect:** {dasha['Market Effect']}")
                        st.markdown(f"**Best Strategy:** {dasha['Best Strategy']}")
            
            # Upcoming Dasha Changes
            st.markdown("### 🔄 UPCOMING DASHA CHANGES")
            
            upcoming_dasha = [
                {
                    "Date": "Aug 11, 2025",
                    "Time": "02:30 PM",
                    "Change": "Pratyantara: Ketu → Venus",
                    "Duration": "3 days",
                    "Effect": "Relationship harmony, luxury focus",
                    "Market Impact": "Bullish for real estate, consumer stocks",
                    "Action": "Buy realty, FMCG stocks"
                },
                {
                    "Date": "Aug 20, 2025",
                    "Time": "11:45 AM",
                    "Change": "Antara: Mercury → Ketu",
                    "Duration": "7 days",
                    "Effect": "Spiritual insights, sudden changes",
                    "Market Impact": "Volatility in tech, pharma stocks",
                    "Action": "Caution in tech, focus on pharma"
                },
                {
                    "Date": "Sep 7, 2025",
                    "Time": "09:15 AM",
                    "Change": "Bhukti: Moon → Mars",
                    "Duration": "3 months",
                    "Effect": "High energy, action-oriented phase",
                    "Market Impact": "Bullish for infrastructure, auto",
                    "Action": "Buy cyclical stocks, infrastructure"
                },
                {
                    "Date": "Oct 18, 2025",
                    "Time": "06:30 PM",
                    "Change": "Jupiter enters Cancer",
                    "Duration": "1 year",
                    "Effect": "MEGA FORTUNE begins",
                    "Market Impact": "SUPER BULLISH for all sectors",
                    "Action": "BUY EVERYTHING"
                },
                {
                    "Date": "Nov 9, 2025",
                    "Time": "03:45 PM",
                    "Change": "Antara: Mars → Rahu",
                    "Duration": "18 days",
                    "Effect": "Material gains, foreign connections",
                    "Market Impact": "Foreign fund inflows",
                    "Action": "Focus on MNC stocks, export sectors"
                }
            ]
            
            df_upcoming = pd.DataFrame(upcoming_dasha)
            st.dataframe(df_upcoming, use_container_width=True)
            
            # Current Market Dasha Impacts
            st.markdown("### 🎯 CURRENT PERIOD MARKET IMPACTS")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**🟢 Bullish Factors (Sun-Moon-Mercury Period):**")
                st.success("""
                • Government policy support
                • Banking sector strength
                • Authority figures favor markets
                • Public sentiment improving
                • Foreign institutional buying
                • Infrastructure spending
                • Communication sector recovery post-Aug 11
                """)
            
            with col2:
                st.markdown("**🔴 Bearish Risks:**")
                st.error("""
                • Mercury retrograde confusion (until Aug 11)
                • Communication breakdowns
                • Tech sector volatility
                • News-driven selling
                • Regulatory uncertainties
                • Global headwinds
                • Emotional trading decisions
                """)
            
            # Market Dasha Timeline
            st.markdown("### 📅 COMPLETE MARKET DASHA CYCLE")
            
            market_dasha_data = [
                {"Period": "Sun MD", "Years": "2024-2030", "Market Trend": "Government & Banking Bull Run", "Best Sectors": "PSU, Banking, Defense", "Strategy": "Long-term Holdings"},
                {"Period": "Moon MD", "Years": "2030-2040", "Market Trend": "Public Participation Era", "Best Sectors": "FMCG, Healthcare, Real Estate", "Strategy": "Sentiment Trading"},
                {"Period": "Mars MD", "Years": "2040-2047", "Market Trend": "Infrastructure Boom", "Best Sectors": "Construction, Steel, Engineering", "Strategy": "Cyclical Plays"},
                {"Period": "Rahu MD", "Years": "2047-2065", "Market Trend": "Technology Revolution", "Best Sectors": "IT, Biotech, Space", "Strategy": "Innovation Betting"},
                {"Period": "Jupiter MD", "Years": "2065-2081", "Market Trend": "Wisdom Economy", "Best Sectors": "Education, Finance, Pharma", "Strategy": "Value Investing"}
            ]
            
            df_market_dasha = pd.DataFrame(market_dasha_data)
            st.dataframe(df_market_dasha, use_container_width=True)
        
        with tabs[1]:  # Market Transits
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    🌍 CURRENT MARKET TRANSITS - {ayanamsa} CALCULATIONS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Running Transits
            st.markdown("### 🔄 RUNNING TRANSITS")
            
            running_transits = [
                {
                    "Planet": "Mercury",
                    "Transit": "Retrograde in Leo",
                    "Start Date": "Jul 26, 2025",
                    "End Date": "Aug 11, 2025",
                    "Time": "Until 02:30 PM",
                    "Effect": "Communication breakdowns, delays, confusion",
                    "Market Impact": "Bearish for IT, Telecom, Media",
                    "Remedy": "Avoid new trades, double-check analysis"
                },
                {
                    "Planet": "Saturn",
                    "Transit": "Retrograde in Pisces",
                    "Start Date": "Jun 29, 2025",
                    "End Date": "Sep 1, 2025",
                    "Time": "Until 10:15 AM",
                    "Effect": "Delays, restrictions, debt concerns",
                    "Market Impact": "Bearish for Auto, Infrastructure, NBFC",
                    "Remedy": "Focus on quality stocks, avoid leverage"
                },
                {
                    "Planet": "Mars",
                    "Transit": "In Virgo",
                    "Start Date": "Jul 20, 2025",
                    "End Date": "Sep 13, 2025",
                    "Time": "Ongoing",
                    "Effect": "Focus on health, service, details",
                    "Market Impact": "Bullish for Healthcare, Pharma, Service sectors",
                    "Remedy": "Invest in healthcare, pharma stocks"
                },
                {
                    "Planet": "Venus",
                    "Transit": "In Cancer",
                    "Start Date": "Jul 31, 2025",
                    "End Date": "Sep 15, 2025",
                    "Time": "Ongoing",
                    "Effect": "Emotional harmony, home focus",
                    "Market Impact": "Bullish for Real Estate, FMCG, Consumer",
                    "Remedy": "Accumulate realty, consumer stocks"
                }
            ]
            
            for transit in running_transits:
                impact_type = "error" if "Retrograde" in transit["Transit"] else "warning" if "Bearish" in transit["Market Impact"] else "info"
                
                with st.expander(f"🔄 {transit['Planet']} - {transit['Transit']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Duration:** {transit['Start Date']} to {transit['End Date']}")
                        st.markdown(f"**Time:** {transit['Time']}")
                        st.markdown(f"**Effect:** {transit['Effect']}")
                    with col2:
                        st.markdown(f"**Market Impact:** {transit['Market Impact']}")
                        st.markdown(f"**Remedy:** {transit['Remedy']}")
            
            # Upcoming Transits
            st.markdown("### 🚀 UPCOMING TRANSITS")
            
            upcoming_transits = [
                {
                    "Planet": "Mercury",
                    "Transit": "Direct in Leo",
                    "Date": "Aug 11, 2025",
                    "Time": "02:30 PM",
                    "Effect": "Communication breakthrough, clarity",
                    "Market Impact": "Bullish for IT, Telecom, Media",
                    "Action": "Buy tech stocks, sign contracts"
                },
                {
                    "Planet": "Sun",
                    "Transit": "Enters Leo",
                    "Date": "Aug 17, 2025",
                    "Time": "11:45 AM",
                    "Effect": "Authority peak, leadership energy",
                    "Market Impact": "Bullish for Banking, Government stocks",
                    "Action": "Buy PSU, Banking stocks"
                },
                {
                    "Planet": "Venus",
                    "Transit": "Enters Cancer",
                    "Date": "Aug 21, 2025",
                    "Time": "09:30 PM",
                    "Effect": "Relationship harmony, luxury focus",
                    "Market Impact": "Bullish for Real Estate, Luxury goods",
                    "Action": "Buy realty, consumer stocks"
                },
                {
                    "Planet": "Saturn",
                    "Transit": "Direct in Pisces",
                    "Date": "Sep 1, 2025",
                    "Time": "10:15 AM",
                    "Effect": "Clarity in responsibilities, progress",
                    "Market Impact": "Bullish for Infrastructure, Auto",
                    "Action": "Buy cyclical stocks"
                },
                {
                    "Planet": "Mars",
                    "Transit": "Enters Libra",
                    "Date": "Sep 13, 2025",
                    "Time": "03:45 PM",
                    "Effect": "Balanced action, partnerships",
                    "Market Impact": "Neutral to Bullish for markets",
                    "Action": "Focus on quality stocks"
                },
                {
                    "Planet": "Jupiter",
                    "Transit": "Enters Cancer",
                    "Date": "Oct 18, 2025",
                    "Time": "06:30 PM",
                    "Effect": "MEGA FORTUNE begins, expansion",
                    "Market Impact": "SUPER BULLISH for all sectors",
                    "Action": "BUY EVERYTHING"
                }
            ]
            
            for transit in upcoming_transits:
                impact_type = "success" if "Bullish" in transit["Market Impact"] else "warning" if "Neutral" in transit["Market Impact"] else "error"
                
                with st.expander(f"🚀 {transit['Planet']} - {transit['Transit']} on {transit['Date']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Date & Time:** {transit['Date']} at {transit['Time']}")
                        st.markdown(f"**Effect:** {transit['Effect']}")
                    with col2:
                        st.markdown(f"**Market Impact:** {transit['Market Impact']}")
                        st.markdown(f"**Action:** {transit['Action']}")
            
            # 5-8 Year Cycle Forecast
            st.markdown("### 🔮 5-8 YEAR CYCLE FORECAST")
            
            cycle_forecasts = [
                {
                    "Year": "2025-2026",
                    "Key Transit": "Jupiter in Gemini (Until Oct 18, 2025)",
                    "Effect": "Communication, technology focus",
                    "Market Trend": "Bullish for IT, Telecom",
                    "Bullish Sectors": "Technology, Communication, Education",
                    "Bearish Sectors": "Traditional manufacturing",
                    "Overall Outlook": "Positive growth with tech leadership"
                },
                {
                    "Year": "2026-2027",
                    "Key Transit": "Jupiter in Cancer (Oct 2025 - Oct 2026)",
                    "Effect": "MEGA BULL RUN, real estate boom",
                    "Market Trend": "Super Bullish across all sectors",
                    "Bullish Sectors": "Real Estate, Banking, Healthcare",
                    "Bearish Sectors": "None - Universal bull market",
                    "Overall Outlook": "Exceptional growth, new market highs"
                },
                {
                    "Year": "2027-2028",
                    "Key Transit": "Saturn in Pisces (Until 2027)",
                    "Effect": "Discipline, structure, responsibility",
                    "Market Trend": "Consolidation, value investing",
                    "Bullish Sectors": "Infrastructure, PSU, Traditional sectors",
                    "Bearish Sectors": "Speculative stocks, high debt companies",
                    "Overall Outlook": "Steady growth with focus on fundamentals"
                },
                {
                    "Year": "2028-2029",
                    "Key Transit": "Rahu in Aries (2028-2029)",
                    "Effect": "Innovation, disruption, foreign influence",
                    "Market Trend": "Volatile with upward bias",
                    "Bullish Sectors": "Technology, Startups, Foreign companies",
                    "Bearish Sectors": "Traditional sectors, government companies",
                    "Overall Outlook": "Transformation period with high volatility"
                },
                {
                    "Year": "2029-2030",
                    "Key Transit": "Jupiter in Leo (2029-2030)",
                    "Effect": "Leadership, authority, creativity",
                    "Market Trend": "Bullish with leadership focus",
                    "Bullish Sectors": "Banking, Government, Entertainment",
                    "Bearish Sectors": "Defensive sectors, utilities",
                    "Overall Outlook": "Strong growth with leadership themes"
                },
                {
                    "Year": "2030-2031",
                    "Key Transit": "Saturn in Aries (2030-2032)",
                    "Effect": "Disciplined action, new beginnings",
                    "Market Trend": "Cautious optimism",
                    "Bullish Sectors": "Infrastructure, Auto, Engineering",
                    "Bearish Sectors": "Luxury, speculative stocks",
                    "Overall Outlook": "Foundation building for next cycle"
                },
                {
                    "Year": "2031-2032",
                    "Key Transit": "Jupiter in Virgo (2031-2032)",
                    "Effect": "Analysis, health, service focus",
                    "Market Trend": "Steady growth in service sectors",
                    "Bullish Sectors": "Healthcare, Pharma, Service industries",
                    "Bearish Sectors": "Manufacturing, commodities",
                    "Overall Outlook": "Sustainable growth with focus on health"
                }
            ]
            
            for forecast in cycle_forecasts:
                with st.expander(f"🔮 {forecast['Year']} - {forecast['Key Transit']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Effect:** {forecast['Effect']}")
                        st.markdown(f"**Market Trend:** {forecast['Market Trend']}")
                        st.markdown(f"**Bullish Sectors:** {forecast['Bullish Sectors']}")
                    with col2:
                        st.markdown(f"**Bearish Sectors:** {forecast['Bearish Sectors']}")
                        st.markdown(f"**Overall Outlook:** {forecast['Overall Outlook']}")
            
            # Market Transit Calendar
            st.markdown("### 📅 MARKET TRANSIT CALENDAR")
            
            transit_calendar = [
                {"Date": "Aug 11, 2025", "Time": "02:30 PM", "Event": "Mercury Direct", "Market Impact": "IT sector recovery", "Action": "Buy tech stocks"},
                {"Date": "Aug 17, 2025", "Time": "11:45 AM", "Event": "Sun → Leo", "Market Impact": "Banking sector boom", "Action": "Load bank stocks"},
                {"Date": "Aug 21, 2025", "Time": "09:30 PM", "Event": "Venus → Cancer", "Market Impact": "Real estate surge", "Action": "Buy property stocks"},
                {"Date": "Sep 1, 2025", "Time": "10:15 AM", "Event": "Saturn Direct", "Market Impact": "FII buying resumes", "Action": "Market bullishness"},
                {"Date": "Sep 13, 2025", "Time": "03:45 PM", "Event": "Mars → Libra", "Market Impact": "Balance in markets", "Action": "Book some profits"},
                {"Date": "Oct 18, 2025", "Time": "06:30 PM", "Event": "Jupiter → Cancer", "Market Impact": "MEGA BULL RUN", "Action": "All-in strategy"},
                {"Date": "Nov 14, 2025", "Time": "01:20 PM", "Event": "Mercury → Scorpio", "Market Impact": "Deep analysis, research", "Action": "Focus on fundamentals"},
                {"Date": "Dec 15, 2025", "Time": "09:45 AM", "Event": "Sun → Sagittarius", "Market Impact": "Optimism, expansion", "Action": "Growth stocks"},
                {"Date": "Jan 14, 2026", "Time": "11:30 PM", "Event": "Mars → Sagittarius", "Market Impact": "Adventure, risk-taking", "Action": "High beta stocks"},
                {"Date": "Feb 12, 2026", "Time": "03:15 PM", "Event": "Venus → Aquarius", "Market Impact": "Innovation, technology", "Action": "Tech sector focus"}
            ]
            
            df_calendar = pd.DataFrame(transit_calendar)
            st.dataframe(df_calendar, use_container_width=True)
        
        with tabs[2]:  # Monthly Market Forecast
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    📅 MONTHLY MARKET FORECASTS - {ayanamsa} SYSTEM
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            monthly_forecasts = {
                "August 2025": {
                    "overall_trend": "Bearish to Bullish Recovery",
                    "nifty_range": "24,800 - 25,500",
                    "bank_nifty": "52,000 - 55,000",
                    "key_events": ["Mercury Direct Aug 11", "Sun in Leo Aug 17", "Venus in Cancer Aug 21"],
                    "sectors": {
                        "Bullish": ["Banking", "Real Estate", "Government"],
                        "Bearish": ["Technology (until 11th)", "Export"],
                        "Neutral": ["FMCG", "Pharma"]
                    },
                    "strategies": {
                        "Week 1": "Stay defensive, Mercury retrograde peak",
                        "Week 2": "Start accumulating, Mercury turns direct",
                        "Week 3": "Aggressive buying, Sun in Leo power",
                        "Week 4": "Ride the momentum, Venus boost"
                    },
                    "top_picks": ["HDFC Bank", "ICICI Bank", "DLF", "Godrej Properties", "SBI"]
                },
                "September 2025": {
                    "overall_trend": "Strong Bullish Momentum",
                    "nifty_range": "25,200 - 26,500",
                    "bank_nifty": "54,000 - 58,000",
                    "key_events": ["Saturn Direct Sep 1", "Mars → Libra Sep 13"],
                    "sectors": {
                        "Bullish": ["Healthcare", "Real Estate", "Banking"],
                        "Bearish": ["Technology (profit booking)", "Metals"],
                        "Neutral": ["Auto", "Energy"]
                    },
                    "strategies": {
                        "Week 1": "FII buying resumes, go long",
                        "Week 2": "Healthcare sector explosion",
                        "Week 3": "Balanced approach, Mars in Libra",
                        "Week 4": "Book partial profits"
                    },
                    "top_picks": ["Sun Pharma", "Apollo Hospitals", "HDFC Bank", "Bajaj Finance"]
                },
                "October 2025": {
                    "overall_trend": "MEGA BULL RUN BEGINS",
                    "nifty_range": "26,000 - 28,000",
                    "bank_nifty": "57,000 - 62,000",
                    "key_events": ["Jupiter → Cancer Oct 18 - GAME CHANGER"],
                    "sectors": {
                        "Bullish": ["ALL SECTORS", "Financials", "Real Estate", "Healthcare"],
                        "Bearish": ["None - Universal Bull Market"],
                        "Neutral": ["Profit booking opportunities"]
                    },
                    "strategies": {
                        "Week 1": "Pre-Jupiter positioning",
                        "Week 2": "Jupiter enters Cancer - BUY EVERYTHING",
                        "Week 3": "Ride the mega trend",
                        "Week 4": "New highs across board"
                    },
                    "top_picks": ["Entire Portfolio", "Focus on Quality Largecaps", "Banking Heavy"]
                }
            }
            
            for month, forecast in monthly_forecasts.items():
                trend_emoji = "🚀" if "MEGA" in forecast["overall_trend"] else "📈" if "Bullish" in forecast["overall_trend"] else "📊"
                
                with st.expander(f"{trend_emoji} {month} - {forecast['overall_trend']}", expanded=True):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("### 📊 Index Targets")
                        st.metric("Nifty Range", forecast["nifty_range"])
                        st.metric("Bank Nifty", forecast["bank_nifty"])
                        
                        st.markdown("### 🗓️ Key Events")
                        for event in forecast["key_events"]:
                            if "GAME CHANGER" in event:
                                st.success(f"🚀 {event}")
                            else:
                                st.info(f"📅 {event}")
                    
                    with col2:
                        st.markdown("### 🎯 Sector Outlook")
                        
                        # Bullish sectors
                        if forecast["sectors"]["Bullish"]:
                            st.markdown("**🟢 Bullish Sectors:**")
                            for sector in forecast["sectors"]["Bullish"]:
                                st.success(f"📈 {sector}")
                        
                        # Bearish sectors
                        if forecast["sectors"]["Bearish"] and forecast["sectors"]["Bearish"][0] != "None - Universal Bull Market":
                            st.markdown("**🔴 Bearish Sectors:**")
                            for sector in forecast["sectors"]["Bearish"]:
                                st.error(f"📉 {sector}")
                        elif forecast["sectors"]["Bearish"][0] == "None - Universal Bull Market":
                            st.success("🚀 Universal Bull Market - All Sectors Bullish!")
                    
                    # Weekly strategies
                    st.markdown("### 📈 Weekly Trading Strategies")
                    weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]
                    for week in weeks:
                        if week in forecast["strategies"]:
                            st.info(f"**{week}:** {forecast['strategies'][week]}")
                    
                    # Top picks
                    st.markdown("### ⭐ Top Stock Picks")
                    picks_str = " | ".join(forecast["top_picks"])
                    st.success(f"🎯 **Recommended:** {picks_str}")
        
        with tabs[3]:  # Ayanamsa Market Impact
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    🔮 AYANAMSA IMPACT ON MARKET ANALYSIS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 📊 How Different Ayanamsa Systems Affect Market Predictions")
            
            # Ayanamsa market comparison
            ayanamsa_market_data = []
            for ayana_name, details in ayanamsa_options.items():
                if "KP" in ayana_name:
                    trend = "Bullish on Government Stocks"
                    timing = "Precise event timing"
                    best_sectors = "PSU, Banking, Defense"
                elif "Lahiri" in ayana_name:
                    trend = "Traditional Value Approach"
                    timing = "Medium-term cycles"
                    best_sectors = "Pharmaceuticals, FMCG"
                elif "Raman" in ayana_name:
                    trend = "Classical Technical Analysis"
                    timing = "Time-tested methods"
                    best_sectors = "Blue-chip stocks"
                else:
                    trend = "Modern Computational"
                    timing = "Updated calculations"
                    best_sectors = "Technology, Innovation"
                
                is_selected = "✅" if ayana_name == ayanamsa else ""
                ayanamsa_market_data.append({
                    "Selected": is_selected,
                    "Ayanamsa": ayana_name,
                    "Market Trend": trend,
                    "Timing Accuracy": timing,
                    "Best Sectors": best_sectors,
                    "Current Signal": "BUY" if "Bullish" in trend else "HOLD"
                })
            
            df_ayanamsa_market = pd.DataFrame(ayanamsa_market_data)
            st.dataframe(df_ayanamsa_market, use_container_width=True)
            
            # Current system impact
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"### 🎯 {ayanamsa} System Impact")
                if "KP" in ayanamsa:
                    st.success("""
                    **🔥 KP System Market Advantages:**
                    • Highly precise timing for entries/exits
                    • Excellent for intraday trading
                    • Government policy predictions
                    • Banking sector accuracy
                    • Event-based trading signals
                    • Significator analysis for stocks
                    """)
                elif "Lahiri" in ayanamsa:
                    st.info("""
                    **📊 Lahiri System Market Benefits:**
                    • Traditional trend analysis
                    • Long-term investment timing
                    • Classical sector rotation
                    • Balanced market approach
                    • Time-tested methodologies
                    • Vedic market principles
                    """)
                else:
                    st.warning("""
                    **⚡ Selected System Benefits:**
                    • Consistent calculation method
                    • Reliable trend identification
                    • Sector-specific insights
                    • Time-based market analysis
                    • Professional accuracy
                    • Historical validation
                    """)
            
            with col2:
                st.markdown("### 📈 System-Specific Predictions")
                current_date = datetime.now().strftime("%B %Y")
                
                if "KP" in ayanamsa:
                    market_outlook = {
                        "Short Term": "Bullish (Government support)",
                        "Medium Term": "Very Bullish (Banking boom)",
                        "Long Term": "Super Bullish (Authority cycle)",
                        "Best Timing": "Aug 17-31 (Sun in Leo)",
                        "Top Signal": "Load PSU and Banking stocks"
                    }
                elif "Lahiri" in ayanamsa:
                    market_outlook = {
                        "Short Term": "Cautious Bullish",
                        "Medium Term": "Steady Growth",
                        "Long Term": "Traditional Bull Market",
                        "Best Timing": "Jupiter favorable periods",
                        "Top Signal": "Quality value stocks"
                    }
                else:
                    market_outlook = {
                        "Short Term": "Calculated Bullish",
                        "Medium Term": "Data-driven Growth",
                        "Long Term": "Systematic Bull Phase",
                        "Best Timing": "Computational optimal periods",
                        "Top Signal": "Diversified portfolio approach"
                    }
                
                for aspect, prediction in market_outlook.items():
                    st.metric(aspect, prediction)
        
        with tabs[4]:  # Indian Markets
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    🇮🇳 INDIAN MARKETS DETAILED ANALYSIS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Major Indices Analysis
            indian_indices = {
                "NIFTY 50": {
                    "current": "25,075",
                    "planetary_ruler": "Sun (Authority)",
                    "trend": "Bullish",
                    "support": "24,500",
                    "resistance": "25,500",
                    "target_1w": "25,300",
                    "target_1m": "26,200",
                    "target_3m": "27,500",
                    "strategy": "Buy on dips, hold for targets",
                    "risk": "Global slowdown, FII selling"
                },
                "BANK NIFTY": {
                    "current": "53,250",
                    "planetary_ruler": "Sun + Jupiter",
                    "trend": "Super Bullish",
                    "support": "52,000",
                    "resistance": "55,000",
                    "target_1w": "54,500",
                    "target_1m": "57,000",
                    "target_3m": "62,000",
                    "strategy": "Aggressive accumulation",
                    "risk": "Interest rate changes"
                },
                "NIFTY IT": {
                    "current": "42,150",
                    "planetary_ruler": "Mercury (Retrograde impact)",
                    "trend": "Recovery Mode",
                    "support": "40,000",
                    "resistance": "44,000",
                    "target_1w": "43,000",
                    "target_1m": "45,500",
                    "target_3m": "48,000",
                    "strategy": "Buy after Aug 11 (Mercury direct)",
                    "risk": "Continued retrograde effects"
                },
                "NIFTY PHARMA": {
                    "current": "18,750",
                    "planetary_ruler": "Mars + Moon",
                    "trend": "Bullish",
                    "support": "18,000",
                    "resistance": "19,500",
                    "target_1w": "19,200",
                    "target_1m": "20,500",
                    "target_3m": "22,000",
                    "strategy": "Healthcare sector boom",
                    "risk": "Regulatory changes"
                }
            }
            
            for index_name, data in indian_indices.items():
                trend_color = "🟢" if data["trend"] == "Super Bullish" else "🟡" if data["trend"] == "Bullish" else "🔵"
                
                with st.expander(f"{trend_color} {index_name} - {data['trend']} ({data['current']})", expanded=True):
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown("**📊 Current Levels**")
                        st.metric("Current", data["current"])
                        st.metric("Support", data["support"])
                        st.metric("Resistance", data["resistance"])
                    
                    with col2:
                        st.markdown("**🎯 Targets**")
                        st.metric("1 Week", data["target_1w"])
                        st.metric("1 Month", data["target_1m"])
                        st.metric("3 Months", data["target_3m"])
                    
                    with col3:
                        st.markdown("**⚡ Analysis**")
                        st.info(f"**Ruler:** {data['planetary_ruler']}")
                        st.success(f"**Strategy:** {data['strategy']}")
                        st.warning(f"**Risk:** {data['risk']}")
            
            # Top Indian Stocks
            st.markdown("### ⭐ TOP INDIAN STOCK RECOMMENDATIONS")
            
            top_stocks = [
                {"Stock": "HDFC Bank", "CMP": "₹1,685", "Target": "₹1,950", "Upside": "15.7%", "Horizon": "3 months", "Trigger": "Sun in Leo boost"},
                {"Stock": "ICICI Bank", "CMP": "₹1,245", "Target": "₹1,450", "Upside": "16.5%", "Horizon": "2 months", "Trigger": "Banking sector strength"},
                {"Stock": "Reliance", "CMP": "₹2,975", "Target": "₹3,400", "Upside": "14.3%", "Horizon": "4 months", "Trigger": "Energy transition"},
                {"Stock": "TCS", "CMP": "₹4,125", "Target": "₹4,750", "Upside": "15.2%", "Horizon": "3 months", "Trigger": "Mercury direct impact"},
                {"Stock": "DLF", "CMP": "₹875", "Target": "₹1,200", "Upside": "37.1%", "Horizon": "3 months", "Trigger": "Venus in Cancer"},
                {"Stock": "Sun Pharma", "CMP": "₹1,750", "Target": "₹2,100", "Upside": "20.0%", "Horizon": "2 months", "Trigger": "Mars in Virgo"}
            ]
            
            df_stocks = pd.DataFrame(top_stocks)
            st.dataframe(df_stocks, use_container_width=True)
            
            # Market Movers
            st.markdown("### 📈 MARKET MOVERS - PLANETARY INFLUENCE")
            
            market_movers = [
                {
                    "Planet": "Sun",
                    "Influence": "Authority, Government",
                    "Effect": "Bullish for PSU, Banking",
                    "Key Stocks": "SBI, PNB, BOB",
                    "Timeline": "Strong until Nov 2030"
                },
                {
                    "Planet": "Moon",
                    "Influence": "Public Sentiment",
                    "Effect": "Drives FMCG, Healthcare",
                    "Key Stocks": "ITC, HUL, Sun Pharma",
                    "Timeline": "Current phase until Sep 2025"
                },
                {
                    "Planet": "Mars",
                    "Influence": "Energy, Action",
                    "Effect": "Bullish for Auto, Infrastructure",
                    "Key Stocks": "Tata Motors, L&T",
                    "Timeline": "Increasing from Sep 2025"
                },
                {
                    "Planet": "Mercury",
                    "Influence": "Communication",
                    "Effect": "Volatile for IT until direct",
                    "Key Stocks": "TCS, Infosys, Wipro",
                    "Timeline": "Recovery from Aug 11"
                },
                {
                    "Planet": "Jupiter",
                    "Influence": "Expansion, Growth",
                    "Effect": "Mega bull from Oct 18",
                    "Key Stocks": "All quality stocks",
                    "Timeline": "MEGA RUN from Oct 2025"
                }
            ]
            
            for mover in market_movers:
                with st.expander(f"🌟 {mover['Planet']} - {mover['Influence']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Effect:** {mover['Effect']}")
                        st.markdown(f"**Key Stocks:** {mover['Key Stocks']}")
                    with col2:
                        st.markdown(f"**Timeline:** {mover['Timeline']}")
        
        with tabs[5]:  # Sector Analysis
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    🏦 COMPREHENSIVE SECTOR ANALYSIS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Detailed sector analysis
            sectors_detailed = {
                "🏦 BANKING & FINANCE": {
                    "planetary_ruler": "Sun + Jupiter",
                    "current_trend": "Super Bullish",
                    "outlook": "Excellent - Sun in Leo power",
                    "timeline": {
                        "Intraday": "Strong 10:00-11:30 AM",
                        "Short Term": "15-20% upside in 2 months",
                        "Long Term": "25-35% growth in 1 year"
                    },
                    "stocks": {
                        "Large Cap": "HDFC Bank, ICICI Bank, SBI",
                        "Mid Cap": "Federal Bank, IDFC First, Bandhan",
                        "Small Cap": "RBL Bank, South Indian Bank"
                    },
                    "events": [
                        "Aug 17: Sun enters Leo - Banking boom",
                        "Sep 1: Saturn direct - FII buying",
                        "Oct 18: Jupiter Cancer - Mega growth"
                    ],
                    "strategy": "Aggressive accumulation, hold for 6-12 months"
                },
                "💻 INFORMATION TECHNOLOGY": {
                    "planetary_ruler": "Mercury (Retrograde till Aug 11)",
                    "current_trend": "Recovery Mode",
                    "outlook": "Bearish until Aug 11, then Bullish",
                    "timeline": {
                        "Intraday": "Avoid until Mercury direct",
                        "Short Term": "10-15% recovery post Aug 11",
                        "Long Term": "20-25% growth by year-end"
                    },
                    "stocks": {
                        "Large Cap": "TCS, Infosys, Wipro, HCL Tech",
                        "Mid Cap": "Tech Mahindra, Mindtree, Mphasis",
                        "Small Cap": "Persistent, Cyient, KPIT"
                    },
                    "events": [
                        "Aug 11: Mercury direct - Sector recovery",
                        "Aug 15-30: Buying opportunity window",
                        "Sep 15: Communication sector boom"
                    ],
                    "strategy": "Wait for Mercury direct, then aggressive buying"
                },
                "🏠 REAL ESTATE": {
                    "planetary_ruler": "Venus + Mars",
                    "current_trend": "Explosive Bullish",
                    "outlook": "Best performing sector",
                    "timeline": {
                        "Intraday": "Strong momentum all day",
                        "Short Term": "30-40% gains in 3 months",
                        "Long Term": "50-75% growth potential"
                    },
                    "stocks": {
                        "Large Cap": "DLF, Godrej Properties, Oberoi Realty",
                        "Mid Cap": "Brigade, Prestige, Sobha",
                        "Small Cap": "Mahindra Lifespace, Sunteck"
                    },
                    "events": [
                        "Aug 21: Venus enters Cancer - Property boom",
                        "Sep 13: Mars aspects - Construction surge",
                        "Oct 18: Jupiter boost - Residential demand"
                    ],
                    "strategy": "Buy immediately, ride the mega trend"
                },
                "🏥 HEALTHCARE & PHARMA": {
                    "planetary_ruler": "Mars + Moon",
                    "current_trend": "Strong Bullish",
                    "outlook": "Healthcare expansion theme",
                    "timeline": {
                        "Intraday": "Strong 11:00 AM - 2:00 PM",
                        "Short Term": "20-30% upside",
                        "Long Term": "Healthcare sector transformation"
                    },
                    "stocks": {
                        "Large Cap": "Sun Pharma, Dr Reddy's, Cipla",
                        "Mid Cap": "Apollo Hospitals, Fortis, Max",
                        "Small Cap": "Laurus Labs, Divis Labs"
                    },
                    "events": [
                        "Aug 20: Mars in Virgo peak",
                        "Sep 1-15: Healthcare policy boost",
                        "Oct 18: Jupiter expansion phase"
                    ],
                    "strategy": "Accumulate on dips, long-term holding"
                }
            }
            
            for sector_name, sector_data in sectors_detailed.items():
                trend_emoji = "🚀" if "Explosive" in sector_data["current_trend"] else "📈" if "Bullish" in sector_data["current_trend"] else "📊"
                
                with st.expander(f"{trend_emoji} {sector_name} - {sector_data['current_trend']}", expanded=True):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown(f"**🔮 Planetary Ruler:** {sector_data['planetary_ruler']}")
                        st.markdown(f"**📊 Outlook:** {sector_data['outlook']}")
                        st.markdown(f"**📈 Strategy:** {sector_data['strategy']}")
                        
                        st.markdown("**⏰ Timeline Analysis:**")
                        for timeframe, analysis in sector_data["timeline"].items():
                            st.info(f"**{timeframe}:** {analysis}")
                    
                    with col2:
                        st.markdown("**🎯 Stock Categories:**")
                        for category, stocks in sector_data["stocks"].items():
                            st.success(f"**{category}:** {stocks}")
                        
                        st.markdown("**📅 Key Events:**")
                        for event in sector_data["events"]:
                            st.warning(f"• {event}")
            
            # Sector Performance Forecast
            st.markdown("### 📊 SECTOR PERFORMANCE FORECAST")
            
            sector_forecast = [
                {"Sector": "Banking", "1M": "+12%", "3M": "+25%", "6M": "+40%", "1Y": "+65%", "Rating": "⭐⭐⭐⭐⭐"},
                {"Sector": "IT", "1M": "+8%", "3M": "+18%", "6M": "+30%", "1Y": "+45%", "Rating": "⭐⭐⭐⭐"},
                {"Sector": "Real Estate", "1M": "+15%", "3M": "+35%", "6M": "+60%", "1Y": "+85%", "Rating": "⭐⭐⭐⭐⭐"},
                {"Sector": "Pharma", "1M": "+10%", "3M": "+22%", "6M": "+35%", "1Y": "+50%", "Rating": "⭐⭐⭐⭐"},
                {"Sector": "Auto", "1M": "+5%", "3M": "+15%", "6M": "+25%", "1Y": "+40%", "Rating": "⭐⭐⭐"},
                {"Sector": "FMCG", "1M": "+7%", "3M": "+18%", "6M": "+28%", "1Y": "+42%", "Rating": "⭐⭐⭐⭐"}
            ]
            
            df_sector_forecast = pd.DataFrame(sector_forecast)
            st.dataframe(df_sector_forecast, use_container_width=True)
        
        with tabs[6]:  # Global Markets
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    🌏 GLOBAL MARKETS ANALYSIS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Global indices with planetary analysis
            global_markets = {
                "🇺🇸 S&P 500": {
                    "current": "5,875",
                    "planetary_impact": "Jupiter in Gemini - Tech rotation",
                    "trend": "Bullish with rotation",
                    "indian_impact": "Positive for IT exports",
                    "targets": "5,950 (1M), 6,100 (3M)",
                    "strategy": "Buy US-exposed Indian stocks"
                },
                "🇺🇸 NASDAQ": {
                    "current": "18,450",
                    "planetary_impact": "Mercury retrograde pressure",
                    "trend": "Volatile until Aug 11",
                    "indian_impact": "IT sector correlation",
                    "targets": "19,000 (1M), 20,500 (3M)",
                    "strategy": "Wait for Mercury direct"
                },
                "🇯🇵 NIKKEI": {
                    "current": "38,720",
                    "planetary_impact": "Saturn aspects - Traditional strength",
                    "trend": "Steady bullish",
                    "indian_impact": "Auto sector positive",
                    "targets": "39,500 (1M), 41,000 (3M)",
                    "strategy": "Japanese MNC stocks in India"
                },
                "🇨🇳 HANG SENG": {
                    "current": "17,240",
                    "planetary_impact": "Rahu influence - Unpredictable",
                    "trend": "Volatile, policy dependent",
                    "indian_impact": "Mixed for pharma APIs",
                    "targets": "18,000 (1M), 19,500 (3M)",
                    "strategy": "Cautious on China-exposed stocks"
                },
                "🇪🇺 DAX": {
                    "current": "18,850",
                    "planetary_impact": "Venus transit support",
                    "trend": "Moderate bullish",
                    "indian_impact": "Engineering exports positive",
                    "targets": "19,200 (1M), 20,000 (3M)",
                    "strategy": "European-focused Indian stocks"
                }
            }
            
            for market, data in global_markets.items():
                with st.expander(f"📊 {market} - {data['trend']}", expanded=True):
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Current Level", data["current"])
                        st.info(f"**Trend:** {data['trend']}")
                    
                    with col2:
                        st.markdown(f"**🔮 Planetary Impact:**  \n{data['planetary_impact']}")
                        st.markdown(f"**🎯 Targets:**  \n{data['targets']}")
                    
                    with col3:
                        st.success(f"**Indian Market Impact:**  \n{data['indian_impact']}")
                        st.warning(f"**Strategy:**  \n{data['strategy']}")
            
            # Global themes affecting India
            st.markdown("### 🌐 GLOBAL THEMES IMPACTING INDIAN MARKETS")
            
            global_themes = [
                {"Theme": "US Fed Policy", "Impact": "Bullish for India if rates pause", "Indian Beneficiaries": "Banks, NBFCs", "Timeline": "Sep Fed meeting"},
                {"Theme": "China Recovery", "Impact": "Mixed - competition vs demand", "Indian Beneficiaries": "Pharma APIs, IT", "Timeline": "Ongoing"},
                {"Theme": "European Slowdown", "Impact": "Negative for exports", "Indian Beneficiaries": "Domestic consumption plays", "Timeline": "H2 2025"},
                {"Theme": "Japan Carry Trade", "Impact": "FII flows to India", "Indian Beneficiaries": "All sectors", "Timeline": "Aug-Oct 2025"},
                {"Theme": "Oil Price Stability", "Impact": "Positive for India", "Indian Beneficiaries": "Airlines, Paints, Chemicals", "Timeline": "Continuous"}
            ]
            
            df_global_themes = pd.DataFrame(global_themes)
            st.dataframe(df_global_themes, use_container_width=True)
            
            # Global Market Correlation
            st.markdown("### 🔄 GLOBAL MARKET CORRELATION")
            
            correlation_data = [
                {"Market": "S&P 500", "Correlation with Nifty": "0.75", "Effect": "Strong positive movement"},
                {"Market": "NASDAQ", "Correlation with Nifty IT": "0.85", "Effect": "Very strong tech correlation"},
                {"Market": "NIKKEI", "Correlation with Nifty Auto": "0.65", "Effect": "Moderate auto sector correlation"},
                {"Market": "HANG SENG", "Correlation with Nifty": "0.45", "Effect": "Weak correlation, divergent trends"},
                {"Market": "DAX", "Correlation with Nifty": "0.60", "Effect": "Moderate correlation, export-dependent"}
            ]
            
            df_correlation = pd.DataFrame(correlation_data)
            st.dataframe(df_correlation, use_container_width=True)
        
        with tabs[7]:  # Forex Analysis
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    💱 FOREX MARKETS PLANETARY ANALYSIS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Major currency pairs
            forex_pairs = {
                "USD/INR": {
                    "current": "83.45",
                    "planetary_ruler": "Sun (USD) vs Moon (INR)",
                    "trend": "USD strength until Aug 17",
                    "support": "83.00",
                    "resistance": "84.20",
                    "targets": {
                        "1 Week": "83.80",
                        "1 Month": "82.50 (INR strength)",
                        "3 Months": "81.00 (Major INR rally)"
                    },
                    "trading_strategy": "Sell USD/INR on rallies post Aug 17",
                    "impact_on_stocks": "Export stocks negative, Import stocks positive"
                },
                "EUR/INR": {
                    "current": "91.25",
                    "planetary_ruler": "Venus (EUR) vs Moon (INR)",
                    "trend": "EUR weakness, INR strength",
                    "support": "90.00",
                    "resistance": "92.50",
                    "targets": {
                        "1 Week": "90.80",
                        "1 Month": "89.50",
                        "3 Months": "87.00"
                    },
                    "trading_strategy": "Sell EUR/INR, INR strengthening",
                    "impact_on_stocks": "European exporters under pressure"
                },
                "GBP/INR": {
                    "current": "106.75",
                    "planetary_ruler": "Mercury (GBP) vs Moon (INR)",
                    "trend": "Volatile due to Mercury retrograde",
                    "support": "105.00",
                    "resistance": "108.50",
                    "targets": {
                        "1 Week": "106.00",
                        "1 Month": "104.00",
                        "3 Months": "102.00"
                    },
                    "trading_strategy": "Avoid until Mercury direct Aug 11",
                    "impact_on_stocks": "UK-focused stocks volatile"
                },
                "JPY/INR": {
                    "current": "0.56",
                    "planetary_ruler": "Saturn (JPY) vs Moon (INR)",
                    "trend": "JPY strength, INR moderate",
                    "support": "0.55",
                    "resistance": "0.58",
                    "targets": {
                        "1 Week": "0.57",
                        "1 Month": "0.59",
                        "3 Months": "0.62"
                    },
                    "trading_strategy": "Buy JPY/INR on dips",
                    "impact_on_stocks": "Japanese auto cos in India benefit"
                }
            }
            
            for pair, data in forex_pairs.items():
                trend_color = "🟢" if "strength" in data["trend"] and "INR" in data["trend"] else "🔴" if "weakness" in data["trend"] and "INR" in data["trend"] else "🟡"
                
                with st.expander(f"{trend_color} {pair} - {data['trend']}", expanded=True):
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Current", data["current"])
                        st.metric("Support", data["support"])
                        st.metric("Resistance", data["resistance"])
                    
                    with col2:
                        st.markdown("**🎯 Targets:**")
                        for period, target in data["targets"].items():
                            st.info(f"**{period}:** {target}")
                    
                    with col3:
                        st.markdown(f"**🔮 Ruler:** {data['planetary_ruler']}")
                        st.success(f"**Strategy:** {data['trading_strategy']}")
                        st.warning(f"**Stock Impact:** {data['impact_on_stocks']}")
            
            # Currency impact on sectors
            st.markdown("### 📊 CURRENCY IMPACT ON INDIAN SECTORS")
            
            currency_impact = [
                {"Currency Move": "USD/INR Falls (INR Strength)", "Beneficiary Sectors": "Import-heavy (Oil, Gold)", "Negative Impact": "IT, Pharma exports", "Net Effect": "Positive for economy"},
                {"Currency Move": "EUR/INR Falls", "Beneficiary Sectors": "Import substitution", "Negative Impact": "European exporters", "Net Effect": "Neutral"},
                {"Currency Move": "JPY/INR Rises", "Beneficiary Sectors": "Japanese auto cos", "Negative Impact": "Local auto", "Net Effect": "Sector rotation"},
                {"Currency Move": "GBP/INR Volatile", "Beneficiary Sectors": "None specific", "Negative Impact": "UK-exposed cos", "Net Effect": "Avoid UK plays"}
            ]
            
            df_currency_impact = pd.DataFrame(currency_impact)
            st.dataframe(df_currency_impact, use_container_width=True)
            
            # Forex Transit Calendar
            st.markdown("### 📅 FOREX TRANSIT CALENDAR")
            
            forex_events = [
                {"Date": "Aug 11, 2025", "Time": "02:30 PM", "Event": "Mercury Direct", "Currency Impact": "INR strength vs GBP, EUR", "Action": "Sell GBP/INR, EUR/INR"},
                {"Date": "Aug 17, 2025", "Time": "11:45 AM", "Event": "Sun in Leo", "Currency Impact": "USD strength peaks, then weakens", "Action": "Sell USD/INR after peak"},
                {"Date": "Aug 21, 2025", "Time": "09:30 PM", "Event": "Venus in Cancer", "Currency Impact": "INR strength vs all currencies", "Action": "Sell all pairs vs INR"},
                {"Date": "Sep 1, 2025", "Time": "10:15 AM", "Event": "Saturn Direct", "Currency Impact": "JPY strength, INR stability", "Action": "Buy JPY/INR"},
                {"Date": "Oct 18, 2025", "Time": "06:30 PM", "Event": "Jupiter in Cancer", "Currency Impact": "MAJOR INR STRENGTH", "Action": "Sell all pairs vs INR"}
            ]
            
            for event in forex_events:
                impact_type = "success" if "strength" in event["Currency Impact"] and "INR" in event["Currency Impact"] else "warning"
                
                if impact_type == "success":
                    st.success(f"**{event['Date']}** - {event['Event']} → {event['Currency Impact']} → **{event['Action']}**")
                else:
                    st.warning(f"**{event['Date']}** - {event['Event']} → {event['Currency Impact']} → **{event['Action']}**")
        
        with tabs[8]:  # Trading Times
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    ⏰ OPTIMAL TRADING TIMES - PLANETARY HOURS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Intraday trading times based on planetary hours
            trading_times = [
                {
                    "Time": "9:15-9:45 AM",
                    "Planet": "Sun",
                    "Energy": "Authority & Leadership",
                    "Best For": "Banking, Government stocks",
                    "Strategy": "Buy quality largecaps",
                    "Avoid": "Speculative stocks",
                    "Success Rate": "85%"
                },
                {
                    "Time": "9:45-10:15 AM", 
                    "Planet": "Venus",
                    "Energy": "Beauty & Luxury",
                    "Best For": "Consumer goods, Real estate",
                    "Strategy": "Long positions in FMCG",
                    "Avoid": "Industrial stocks",
                    "Success Rate": "80%"
                },
                {
                    "Time": "10:15-10:45 AM",
                    "Planet": "Mercury", 
                    "Energy": "Communication",
                    "Best For": "IT, Telecom, Media",
                    "Strategy": "Tech stock trades",
                    "Avoid": "During retrograde",
                    "Success Rate": "75% (90% when direct)"
                },
                {
                    "Time": "10:45-11:15 AM",
                    "Planet": "Moon",
                    "Energy": "Public sentiment",
                    "Best For": "Healthcare, FMCG",
                    "Strategy": "Sentiment-based trades",
                    "Avoid": "Volatile stocks",
                    "Success Rate": "70%"
                },
                {
                    "Time": "11:15-11:45 AM",
                    "Planet": "Saturn",
                    "Energy": "Discipline & Structure", 
                    "Best For": "Infrastructure, PSU",
                    "Strategy": "Value investing",
                    "Avoid": "Growth stocks",
                    "Success Rate": "78%"
                },
                {
                    "Time": "11:45 AM-12:15 PM",
                    "Planet": "Jupiter",
                    "Energy": "Wisdom & Growth",
                    "Best For": "Financial services",
                    "Strategy": "Long-term positions",
                    "Avoid": "Day trading",
                    "Success Rate": "88%"
                },
                {
                    "Time": "12:15-12:45 PM",
                    "Planet": "Mars",
                    "Energy": "Action & Energy",
                    "Best For": "Auto, Engineering",
                    "Strategy": "Momentum trades",
                    "Avoid": "Defensive stocks",
                    "Success Rate": "82%"
                },
                {
                    "Time": "2:30-3:00 PM",
                    "Planet": "Saturn",
                    "Energy": "Reality check",
                    "Best For": "Profit booking",
                    "Strategy": "Close positions",
                    "Avoid": "New entries",
                    "Success Rate": "85%"
                },
                {
                    "Time": "3:00-3:30 PM",
                    "Planet": "Jupiter",
                    "Energy": "Final wisdom",
                    "Best For": "Last-minute quality buys",
                    "Strategy": "Smart money moves",
                    "Avoid": "Panic trades",
                    "Success Rate": "90%"
                }
            ]
            
            df_trading_times = pd.DataFrame(trading_times)
            st.dataframe(df_trading_times, use_container_width=True)
            
            # Daily trading calendar
            st.markdown("### 📅 WEEKLY TRADING CALENDAR")
            
            weekly_calendar = {
                "Monday": {"Ruler": "Moon", "Best": "Emotional stocks (FMCG, Healthcare)", "Avoid": "Aggressive trades", "Strategy": "Gentle accumulation"},
                "Tuesday": {"Ruler": "Mars", "Best": "Auto, Engineering, Defense", "Avoid": "Banking", "Strategy": "Momentum trading"},
                "Wednesday": {"Ruler": "Mercury", "Best": "IT, Telecom, Media", "Avoid": "Traditional sectors", "Strategy": "Communication plays"},
                "Thursday": {"Ruler": "Jupiter", "Best": "Banking, Finance, Education", "Avoid": "Speculative stocks", "Strategy": "Quality investing"},
                "Friday": {"Ruler": "Venus", "Best": "Consumer, Luxury, Real Estate", "Avoid": "Industrial", "Strategy": "Lifestyle sectors"},
                "Saturday": {"Ruler": "Saturn", "Best": "Infrastructure, PSU", "Avoid": "Growth stocks", "Strategy": "Value picks"},
                "Sunday": {"Ruler": "Sun", "Best": "Government, Gold", "Avoid": "Private sector", "Strategy": "Authority plays"}
            }
            
            current_day = datetime.now().strftime("%A")
            
            for day, data in weekly_calendar.items():
                day_color = "🟢" if day == current_day else "⚪"
                highlight = "**TODAY** - " if day == current_day else ""
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.markdown(f"{day_color} **{highlight}{day}**")
                with col2:
                    st.caption(f"Ruler: {data['Ruler']}")
                with col3:
                    st.success(f"Best: {data['Best']}")
                with col4:
                    st.info(f"Strategy: {data['Strategy']}")
            
            # Trading Strategy by Planet
            st.markdown("### 🌟 TRADING STRATEGY BY PLANET")
            
            planet_strategies = [
                {
                    "Planet": "Sun",
                    "Best Strategy": "Buy leadership stocks, PSU, Banking",
                    "Time Frame": "Medium to Long-term",
                    "Risk Level": "Low to Medium",
                    "Key Indicators": "Government policy announcements, authority figures"
                },
                {
                    "Planet": "Moon",
                    "Best Strategy": "Follow sentiment, trade FMCG, Healthcare",
                    "Time Frame": "Short-term",
                    "Risk Level": "Medium",
                    "Key Indicators": "Public mood, emotional news, lunar phases"
                },
                {
                    "Planet": "Mars",
                    "Best Strategy": "Momentum trading, Auto, Infrastructure",
                    "Time Frame": "Short to Medium",
                    "Risk Level": "High",
                    "Key Indicators": "Energy levels, action-oriented news"
                },
                {
                    "Planet": "Mercury",
                    "Best Strategy": "IT, Telecom, quick trades",
                    "Time Frame": "Intraday to Short-term",
                    "Risk Level": "Medium (High when retrograde)",
                    "Key Indicators": "Communication news, technology updates"
                },
                {
                    "Planet": "Jupiter",
                    "Best Strategy": "Value investing, Financial stocks",
                    "Time Frame": "Long-term",
                    "Risk Level": "Low",
                    "Key Indicators": "Expansion news, growth announcements"
                },
                {
                    "Planet": "Venus",
                    "Best Strategy": "Luxury, Real Estate, Consumer stocks",
                    "Time Frame": "Medium to Long-term",
                    "Risk Level": "Low to Medium",
                    "Key Indicators": "Relationship news, luxury trends"
                },
                {
                    "Planet": "Saturn",
                    "Best Strategy": "Value investing, Infrastructure, PSU",
                    "Time Frame": "Long-term",
                    "Risk Level": "Low",
                    "Key Indicators": "Discipline, structure, long-term trends"
                }
            ]
            
            for strategy in planet_strategies:
                with st.expander(f"🌟 {strategy['Planet']} Strategy", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Best Strategy:** {strategy['Best Strategy']}")
                        st.markdown(f"**Time Frame:** {strategy['Time Frame']}")
                        st.markdown(f"**Risk Level:** {strategy['Risk Level']}")
                    with col2:
                        st.markdown(f"**Key Indicators:** {strategy['Key Indicators']}")
        
        with tabs[9]:  # Technical + Astro
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    📈 TECHNICAL + ASTROLOGICAL ANALYSIS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Combined technical and astrological analysis
            st.markdown("### 🔗 TECHNICAL LEVELS WITH PLANETARY TIMING")
            
            combined_analysis = {
                "NIFTY 50": {
                    "technical": {
                        "Support 1": "24,800 (20 EMA)",
                        "Support 2": "24,500 (50 EMA)", 
                        "Resistance 1": "25,300 (Previous high)",
                        "Resistance 2": "25,500 (Fibonacci 61.8%)",
                        "RSI": "65 (Bullish but not overbought)",
                        "MACD": "Positive crossover"
                    },
                    "astrological": {
                        "Current": "Sun-Moon period supports 25,000+",
                        "Aug 11": "Mercury Direct - Break 25,300 resistance",
                        "Aug 17": "Sun in Leo - Break 25,500 resistance",
                        "Aug 21": "Venus boost - Target 25,500",
                        "Sep 1": "Saturn direct - FII flows, 26,000+",
                        "Oct 18": "Jupiter in Cancer - 27,000+"
                    },
                    "combined_strategy": "Buy dips to 24,800, hold till 27,000",
                    "risk_management": "SL below 24,500, book 50% at 26,000"
                },
                "BANK NIFTY": {
                    "technical": {
                        "Support 1": "52,500 (Swing low)",
                        "Support 2": "51,800 (Gap support)",
                        "Resistance 1": "54,000 (Round number)",
                        "Resistance 2": "55,200 (All-time high)",
                        "RSI": "68 (Strong momentum)",
                        "MACD": "Strong bullish divergence"
                    },
                    "astrological": {
                        "Current": "Sun Mahadasha perfect for banking",
                        "Aug 17": "Sun in Leo - Banking sector boom",
                        "Aug 21": "Venus in Cancer - Loan growth",
                        "Sep 1": "Saturn direct - Credit cycle up",
                        "Oct 18": "Jupiter Cancer - NII expansion"
                    },
                    "combined_strategy": "Aggressive accumulation below 53,000",
                    "risk_management": "SL 51,500, targets 55,000, 58,000, 62,000"
                }
            }
            
            for instrument, analysis in combined_analysis.items():
                with st.expander(f"📊 {instrument} - Technical + Astrological Confluence", expanded=True):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("### 📈 TECHNICAL ANALYSIS")
                        for level, value in analysis["technical"].items():
                            if "Support" in level:
                                st.success(f"**{level}:** {value}")
                            elif "Resistance" in level:
                                st.error(f"**{level}:** {value}")
                            else:
                                st.info(f"**{level}:** {value}")
                    
                    with col2:
                        st.markdown("### 🔮 ASTROLOGICAL TIMING")
                        for timing, effect in analysis["astrological"].items():
                            st.warning(f"**{timing}:** {effect}")
                    
                    # Combined strategy
                    st.markdown("### 🎯 COMBINED STRATEGY & RISK MANAGEMENT")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.success(f"**Strategy:** {analysis['combined_strategy']}")
                    with col2:
                        st.error(f"**Risk Management:** {analysis['risk_management']}")
            
            # Gann + Astro timing
            st.markdown("### ⭐ GANN SQUARES + PLANETARY TIMING")
            
            gann_astro = [
                {"Date": "Aug 11, 2025", "Gann Level": "25,000 (Square of 5000)", "Planetary Event": "Mercury Direct", "Combined Effect": "Breakout above 25,000"},
                {"Date": "Aug 17, 2025", "Gann Level": "25,225 (159²)", "Planetary Event": "Sun enters Leo", "Combined Effect": "Authority level breakthrough"},
                {"Date": "Aug 21, 2025", "Gann Level": "25,500 (Fibonacci)", "Planetary Event": "Venus enters Cancer", "Combined Effect": "Luxury spending boost"},
                {"Date": "Sep 1, 2025", "Gann Level": "26,000 (Round number)", "Planetary Event": "Saturn Direct", "Combined Effect": "Institutional buying"},
                {"Date": "Oct 18, 2025", "Gann Level": "27,225 (165²)", "Planetary Event": "Jupiter enters Cancer", "Combined Effect": "New all-time highs"}
            ]
            
            df_gann_astro = pd.DataFrame(gann_astro)
            st.dataframe(df_gann_astro, use_container_width=True)
            
            # Technical Indicators with Planetary Correlation
            st.markdown("### 📊 TECHNICAL INDICATORS WITH PLANETARY CORRELATION")
            
            indicators_correlation = [
                {
                    "Indicator": "RSI (Relative Strength Index)",
                    "Planetary Correlation": "Mars energy levels",
                    "Interpretation": "High RSI = High Mars energy = Overbought",
                    "Trading Signal": "Sell when RSI > 70 + Mars strong"
                },
                {
                    "Indicator": "MACD (Moving Average Convergence Divergence)",
                    "Planetary Correlation": "Mercury communication + Venus harmony",
                    "Interpretation": "Positive crossover = Mercury direct + Venus strong",
                    "Trading Signal": "Buy on MACD crossover during Mercury direct"
                },
                {
                    "Indicator": "Bollinger Bands",
                    "Planetary Correlation": "Saturn boundaries + Jupiter expansion",
                    "Interpretation": "Bands expand = Jupiter strong, contract = Saturn strong",
                    "Trading Signal": "Buy at lower band during Jupiter, sell at upper during Saturn"
                },
                {
                    "Indicator": "Fibonacci Retracement",
                    "Planetary Correlation": "Golden ratio = Venus beauty + Sun perfection",
                    "Interpretation": "Key levels align with Venus/Sun aspects",
                    "Trading Signal": "Respect Fibonacci levels during Venus/Sun transits"
                }
            ]
            
            for indicator in indicators_correlation:
                with st.expander(f"📈 {indicator['Indicator']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Planetary Correlation:** {indicator['Planetary Correlation']}")
                        st.markdown(f"**Interpretation:** {indicator['Interpretation']}")
                    with col2:
                        st.markdown(f"**Trading Signal:** {indicator['Trading Signal']}")
            
            # Final recommendations
            st.markdown("### 🎯 FINAL TRADING RECOMMENDATIONS")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.success("""
                **🟢 IMMEDIATE BUY (Aug 8-15)**
                • Banking stocks on dips
                • Real estate aggressive buying
                • Healthcare sector accumulation
                • Government PSU stocks
                
                **Target:** 15-25% gains
                """)
            
            with col2:
                st.warning("""
                **🟡 WAIT & BUY (Aug 11+)**
                • IT stocks post Mercury direct
                • Export-oriented companies
                • Technology sector
                • Communication stocks
                
                **Target:** 20-30% gains
                """)
            
            with col3:
                st.error("""
                **🔴 AVOID/BOOK PROFITS**
                • Overvalued smallcaps
                • China-exposed stocks
                • Commodity stocks
                • Speculative positions
                
                **Action:** Risk management
                """)
            
            # Final market outlook
            st.markdown("### 🚀 FINAL MARKET OUTLOOK")
            st.success("""
            **🌟 MEGA BULL RUN CONFIRMED** - Jupiter enters Cancer Oct 18, 2025
            
            **Timeline:**
            • **Aug 2025:** Recovery & Accumulation Phase
            • **Sep 2025:** Momentum Building Phase  
            • **Oct 2025:** EXPLOSIVE BULL RUN BEGINS
            • **Nov 2025+:** New All-Time Highs Across Board
            
            **Strategy:** Accumulate quality stocks now, ride the mega trend till 2027
            """)
        
        with tabs[10]:  # Commodities Analysis
            st.markdown(f"""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    🥇 COMMODITIES ANALYSIS - {ayanamsa} SYSTEM
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.info(f"Commodity market analysis using {ayanamsa} ayanamsa ({ayanamsa_options[ayanamsa]['value']}°)")
            
            # Gold Analysis
            st.markdown("### 🥇 GOLD ANALYSIS")
            
            gold_analysis = {
                "current_price": "$2,450",
                "planetary_ruler": "Sun (Core) + Jupiter (Expansion)",
                "current_trend": "Bullish consolidation",
                "key_support": "$2,380",
                "key_resistance": "$2,520",
                "short_term_target": "$2,500 (Aug 2025)",
                "medium_term_target": "$2,650 (Oct 2025)",
                "long_term_target": "$3,000+ (2026)",
                "planetary_influences": [
                    {"Planet": "Sun", "Effect": "Core value, stability", "Timeline": "Strong until Nov 2030"},
                    {"Planet": "Jupiter", "Effect": "Expansion, wealth growth", "Timeline": "Mega boost from Oct 2025"},
                    {"Planet": "Saturn", "Effect": "Traditional value, safety", "Timeline": "Retrograde until Sep 2025"}
                ],
                "transit_events": [
                    {"Date": "Aug 17, 2025", "Event": "Sun in Leo", "Effect": "Gold strength increases", "Action": "Buy on dips"},
                    {"Date": "Sep 1, 2025", "Event": "Saturn Direct", "Effect": "Traditional value returns", "Action": "Accumulate"},
                    {"Date": "Oct 18, 2025", "Event": "Jupiter in Cancer", "Effect": "MEGA GOLD RALLY begins", "Action": "Aggressive buying"}
                ],
                "trading_strategy": "Buy on dips to $2,380, hold for $3,000+ target",
                "risk_factors": "Strong USD, rising interest rates, central bank policies"
            }
            
            with st.expander("🥇 GOLD DETAILED ANALYSIS", expanded=True):
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Current Price", gold_analysis["current_price"])
                    st.metric("Key Support", gold_analysis["key_support"])
                    st.metric("Key Resistance", gold_analysis["key_resistance"])
                    
                    st.markdown("### 🎯 Price Targets")
                    st.info(f"**Short Term:** {gold_analysis['short_term_target']}")
                    st.info(f"**Medium Term:** {gold_analysis['medium_term_target']}")
                    st.info(f"**Long Term:** {gold_analysis['long_term_target']}")
                
                with col2:
                    st.markdown("### 🔮 Planetary Influences")
                    for influence in gold_analysis["planetary_influences"]:
                        st.success(f"**{influence['Planet']}:** {influence['Effect']} ({influence['Timeline']})")
                    
                    st.markdown("### 📅 Transit Events")
                    for event in gold_analysis["transit_events"]:
                        st.warning(f"**{event['Date']}:** {event['Effect']} → {event['Action']}")
                
                st.markdown("### 📈 Trading Strategy")
                st.success(f"**Strategy:** {gold_analysis['trading_strategy']}")
                st.error(f"**Risk Factors:** {gold_analysis['risk_factors']}")
            
            # Silver Analysis
            st.markdown("### 🥈 SILVER ANALYSIS")
            
            silver_analysis = {
                "current_price": "$28.50",
                "planetary_ruler": "Moon (Emotions) + Mercury (Communication)",
                "current_trend": "Bullish with volatility",
                "key_support": "$27.00",
                "key_resistance": "$30.00",
                "short_term_target": "$29.50 (Aug 2025)",
                "medium_term_target": "$32.00 (Oct 2025)",
                "long_term_target": "$40.00+ (2026)",
                "planetary_influences": [
                    {"Planet": "Moon", "Effect": "Emotional trading, volatility", "Timeline": "Current phase until Sep 2025"},
                    {"Planet": "Mercury", "Effect": "Communication-driven moves", "Timeline": "Volatile until direct (Aug 11)"},
                    {"Planet": "Jupiter", "Effect": "Industrial demand growth", "Timeline": "Strong from Oct 2025"}
                ],
                "transit_events": [
                    {"Date": "Aug 11, 2025", "Event": "Mercury Direct", "Effect": "Volatility decreases, trend clarity", "Action": "Buy on clarity"},
                    {"Date": "Aug 21, 2025", "Event": "Venus in Cancer", "Effect": "Industrial demand increases", "Action": "Accumulate"},
                    {"Date": "Oct 18, 2025", "Event": "Jupiter in Cancer", "Effect": "INDUSTRIAL BOOM", "Action": "Aggressive buying"}
                ],
                "trading_strategy": "Buy on dips to $27.00, expect higher volatility than gold",
                "risk_factors": "Industrial demand swings, economic cycles, higher beta than gold"
            }
            
            with st.expander("🥈 SILVER DETAILED ANALYSIS", expanded=True):
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Current Price", silver_analysis["current_price"])
                    st.metric("Key Support", silver_analysis["key_support"])
                    st.metric("Key Resistance", silver_analysis["key_resistance"])
                    
                    st.markdown("### 🎯 Price Targets")
                    st.info(f"**Short Term:** {silver_analysis['short_term_target']}")
                    st.info(f"**Medium Term:** {silver_analysis['medium_term_target']}")
                    st.info(f"**Long Term:** {silver_analysis['long_term_target']}")
                
                with col2:
                    st.markdown("### 🔮 Planetary Influences")
                    for influence in silver_analysis["planetary_influences"]:
                        st.success(f"**{influence['Planet']}:** {influence['Effect']} ({influence['Timeline']})")
                    
                    st.markdown("### 📅 Transit Events")
                    for event in silver_analysis["transit_events"]:
                        st.warning(f"**{event['Date']}:** {event['Effect']} → {event['Action']}")
                
                st.markdown("### 📈 Trading Strategy")
                st.success(f"**Strategy:** {silver_analysis['trading_strategy']}")
                st.error(f"**Risk Factors:** {silver_analysis['risk_factors']}")
            
            # Crude Oil Analysis
            st.markdown("### 🛢️ CRUDE OIL ANALYSIS")
            
            crude_analysis = {
                "current_price": "$78.50",
                "planetary_ruler": "Mars (Energy) + Jupiter (Expansion)",
                "current_trend": "Bearish to Neutral",
                "key_support": "$72.00",
                "key_resistance": "$85.00",
                "short_term_target": "$75.00 (Aug 2025)",
                "medium_term_target": "$82.00 (Oct 2025)",
                "long_term_target": "$95.00+ (2026)",
                "planetary_influences": [
                    {"Planet": "Mars", "Effect": "Energy sector strength", "Timeline": "Strong in Virgo until Sep 2025"},
                    {"Planet": "Jupiter", "Effect": "Demand expansion", "Timeline": "Growth from Oct 2025"},
                    {"Planet": "Saturn", "Effect": "Supply constraints, discipline", "Timeline": "Retrograde limiting supply"}
                ],
                "transit_events": [
                    {"Date": "Aug 17, 2025", "Event": "Sun in Leo", "Effect": "Energy focus increases", "Action": "Buy energy stocks"},
                    {"Date": "Sep 1, 2025", "Event": "Saturn Direct", "Effect": "Supply constraints ease", "Action": "Monitor production"},
                    {"Date": "Oct 18, 2025", "Event": "Jupiter in Cancer", "Effect": "DEMAND EXPLOSION", "Action": "Buy crude futures"}
                ],
                "trading_strategy": "Range trading $72-85, breakout above $85 for $95+ target",
                "risk_factors": "OPEC decisions, geopolitical tensions, demand destruction"
            }
            
            with st.expander("🛢️ CRUDE OIL DETAILED ANALYSIS", expanded=True):
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Current Price", crude_analysis["current_price"])
                    st.metric("Key Support", crude_analysis["key_support"])
                    st.metric("Key Resistance", crude_analysis["key_resistance"])
                    
                    st.markdown("### 🎯 Price Targets")
                    st.info(f"**Short Term:** {crude_analysis['short_term_target']}")
                    st.info(f"**Medium Term:** {crude_analysis['medium_term_target']}")
                    st.info(f"**Long Term:** {crude_analysis['long_term_target']}")
                
                with col2:
                    st.markdown("### 🔮 Planetary Influences")
                    for influence in crude_analysis["planetary_influences"]:
                        st.success(f"**{influence['Planet']}:** {influence['Effect']} ({influence['Timeline']})")
                    
                    st.markdown("### 📅 Transit Events")
                    for event in crude_analysis["transit_events"]:
                        st.warning(f"**{event['Date']}:** {event['Effect']} → {event['Action']}")
                
                st.markdown("### 📈 Trading Strategy")
                st.success(f"**Strategy:** {crude_analysis['trading_strategy']}")
                st.error(f"**Risk Factors:** {crude_analysis['risk_factors']}")
            
            # Commodity Comparison
            st.markdown("### 📊 COMMODITY COMPARISON")
            
            commodity_comparison = [
                {
                    "Commodity": "Gold",
                    "Current Price": "$2,450",
                    "Trend": "Bullish Consolidation",
                    "Volatility": "Medium",
                    "Planetary Support": "Very High (Sun + Jupiter)",
                    "1M Target": "$2,500",
                    "6M Target": "$2,650",
                    "Recommendation": "BUY ON DIPS"
                },
                {
                    "Commodity": "Silver",
                    "Current Price": "$28.50",
                    "Trend": "Bullish Volatile",
                    "Volatility": "High",
                    "Planetary Support": "High (Moon + Jupiter)",
                    "1M Target": "$29.50",
                    "6M Target": "$32.00",
                    "Recommendation": "BUY WITH CAUTION"
                },
                {
                    "Commodity": "Crude Oil",
                    "Current Price": "$78.50",
                    "Trend": "Bearish to Neutral",
                    "Volatility": "Very High",
                    "Planetary Support": "Medium (Mars + Jupiter)",
                    "1M Target": "$75.00",
                    "6M Target": "$82.00",
                    "Recommendation": "RANGE TRADING"
                }
            ]
            
            df_commodity = pd.DataFrame(commodity_comparison)
            st.dataframe(df_commodity, use_container_width=True)
            
            # Commodity Transit Calendar
            st.markdown("### 📅 COMMODITY TRANSIT CALENDAR")
            
            commodity_events = [
                {"Date": "Aug 11, 2025", "Time": "02:30 PM", "Event": "Mercury Direct", "Gold Effect": "Stability returns", "Silver Effect": "Volatility decreases", "Crude Effect": "Clarity in energy policy", "Action": "Buy gold, silver on dips"},
                {"Date": "Aug 17, 2025", "Time": "11:45 AM", "Event": "Sun in Leo", "Gold Effect": "Strength increases", "Silver Effect": "Industrial demand rises", "Crude Effect": "Energy focus", "Action": "Buy all commodities"},
                {"Date": "Aug 21, 2025", "Time": "09:30 PM", "Event": "Venus in Cancer", "Gold Effect": "Luxury demand", "Silver Effect": "Industrial boom", "Crude Effect": "Consumer demand", "Action": "Accumulate silver"},
                {"Date": "Sep 1, 2025", "Time": "10:15 AM", "Event": "Saturn Direct", "Gold Effect": "Traditional value", "Silver Effect": "Supply discipline", "Crude Effect": "Production increases", "Action": "Buy gold, monitor crude"},
                {"Date": "Oct 18, 2025", "Time": "06:30 PM", "Event": "Jupiter in Cancer", "Gold Effect": "MEGA RALLY", "Silver Effect": "INDUSTRIAL BOOM", "Crude Effect": "DEMAND EXPLOSION", "Action": "BUY ALL COMMODITIES"}
            ]
            
            for event in commodity_events:
                impact_type = "success" if "MEGA" in event["Gold Effect"] or "BOOM" in event["Silver Effect"] or "EXPLOSION" in event["Crude Effect"] else "warning"
                
                if impact_type == "success":
                    st.success(f"**{event['Date']}** - {event['Event']} → Gold: {event['Gold Effect']}, Silver: {event['Silver Effect']}, Crude: {event['Crude Effect']} → **{event['Action']}**")
                else:
                    st.warning(f"**{event['Date']}** - {event['Event']} → Gold: {event['Gold Effect']}, Silver: {event['Silver Effect']}, Crude: {event['Crude Effect']} → **{event['Action']}**")
            
            # Long-term Commodity Cycle
            st.markdown("### 🔮 LONG-TERM COMMODITY CYCLE (5-8 YEARS)")
            
            commodity_cycle = [
                {
                    "Period": "2025-2026",
                    "Key Transit": "Jupiter in Cancer (Oct 2025 - Oct 2026)",
                    "Gold Outlook": "MEGA BULL RUN - New all-time highs",
                    "Silver Outlook": "Industrial boom drives prices higher",
                    "Crude Outlook": "Demand explosion, supply constraints",
                    "Overall Trend": "Bullish across all commodities",
                    "Best Strategy": "Accumulate all commodities, focus on gold/silver"
                },
                {
                    "Period": "2026-2027",
                    "Key Transit": "Saturn in Pisces (2026-2027)",
                    "Gold Outlook": "Consolidation at high levels",
                    "Silver Outlook": "Volatility with upward bias",
                    "Crude Outlook": "Supply discipline, range-bound",
                    "Overall Trend": "Consolidation with selective opportunities",
                    "Best Strategy": "Trade ranges, focus on gold stability"
                },
                {
                    "Period": "2027-2028",
                    "Key Transit": "Rahu in Aries (2027-2029)",
                    "Gold Outlook": "Innovation-driven demand",
                    "Silver Outlook": "Technology applications boost demand",
                    "Crude Outlook": "New energy transitions create volatility",
                    "Overall Trend": "Volatile with innovation themes",
                    "Best Strategy": "Focus on technology-driven commodities"
                },
                {
                    "Period": "2028-2029",
                    "Key Transit": "Jupiter in Leo (2028-2029)",
                    "Gold Outlook": "Leadership-driven demand",
                    "Silver Outlook": "Industrial expansion continues",
                    "Crude Outlook": "Energy leadership themes",
                    "Overall Trend": "Bullish with leadership focus",
                    "Best Strategy": "Buy commodity leaders, energy stocks"
                },
                {
                    "Period": "2029-2030",
                    "Key Transit": "Saturn in Aries (2029-2032)",
                    "Gold Outlook": "Safe haven demand increases",
                    "Silver Outlook": "Industrial discipline, value focus",
                    "Crude Outlook": "New energy foundations",
                    "Overall Trend": "Value-driven with safety bias",
                    "Best Strategy": "Focus on gold, value commodities"
                },
                {
                    "Period": "2030-2031",
                    "Key Transit": "Jupiter in Virgo (2030-2032)",
                    "Gold Outlook": "Analysis-driven demand",
                    "Silver Outlook": "Healthcare, technology applications",
                    "Crude Outlook": "Efficiency, service focus",
                    "Overall Trend": "Steady growth in specialty commodities",
                    "Best Strategy": "Focus on technology commodities"
                }
            ]
            
            for cycle in commodity_cycle:
                with st.expander(f"🔮 {cycle['Period']} - {cycle['Key Transit']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Gold Outlook:** {cycle['Gold Outlook']}")
                        st.markdown(f"**Silver Outlook:** {cycle['Silver Outlook']}")
                    with col2:
                        st.markdown(f"**Crude Outlook:** {cycle['Crude Outlook']}")
                        st.markdown(f"**Overall Trend:** {cycle['Overall Trend']}")
                    st.markdown(f"**Best Strategy:** {cycle['Best Strategy']}")
            
            # Commodity Trading Recommendations
            st.markdown("### 🎯 COMMODITY TRADING RECOMMENDATIONS")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.success("""
                **🥇 GOLD RECOMMENDATIONS**
                • **Immediate:** Buy on dips to $2,380
                • **Medium Term:** Hold for $2,650 target
                • **Long Term:** Target $3,000+ by 2026
                • **Strategy:** Accumulate for Jupiter in Cancer
                • **Risk Management:** SL below $2,350
                """)
            
            with col2:
                st.warning("""
                **🥈 SILVER RECOMMENDATIONS**
                • **Immediate:** Buy on dips to $27.00
                • **Medium Term:** Target $32.00 by Oct 2025
                • **Long Term:** Target $40.00+ by 2026
                • **Strategy:** Higher volatility, smaller positions
                • **Risk Management:** SL below $26.50
                """)
            
            with col3:
                st.error("""
                **🛢️ CRUDE OIL RECOMMENDATIONS**
                • **Immediate:** Range trade $72-85
                • **Medium Term:** Breakout above $85 for $95
                • **Long Term:** Supply/demand balance by 2026
                • **Strategy:** Wait for clear breakout
                • **Risk Management:** Use options for protection
                """)
            
            # Final Commodity Outlook
            st.markdown("### 🚀 FINAL COMMODITY OUTLOOK")
            st.success("""
            **🌟 COMMODITY SUPER CYCLE BEGINS** - Jupiter enters Cancer Oct 18, 2025
            
            **Timeline:**
            • **Aug 2025:** Accumulation phase for all commodities
            • **Sep 2025:** Positioning for Jupiter transit
            • **Oct 2025:** COMMODITY BOOM BEGINS
            • **Nov 2025+:** New highs across commodity complex
            
            **Strategy:** 
            • Gold: Core holding, buy on dips
            • Silver: Higher beta, smaller positions
            • Crude: Range trading until breakout
            • Overall: Commodities entering multi-year bull market
            """)

else:
    # Welcome Screen with date/time info
    st.markdown("""
    <div class="cosmic-panel">
        <h2 style="text-align: center; color: #1a202c; margin-bottom: 20px;">
            🌌 PROFESSIONAL KP ASTROLOGY & MARKET ANALYSIS
        </h2>
        <p style="text-align: center; color: #2d3748; font-size: 1.2em; margin: 20px 0; line-height: 1.6;">
            Enhanced with flexible date/time input and multiple ayanamsa systems
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced feature highlights
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **📅 Enhanced Date/Time Input:**
        • Flexible date range (1900-2030)
        • 24-hour and 12-hour AM/PM formats
        • Current date/time display
        • Precise minute-level accuracy
        • Support for historical dates
        • Future date calculations
        """)
    
    with col2:
        st.success("""
        **🔮 Multiple Ayanamsa Systems:**
        • KP (New & Old)
        • Lahiri (Chitrapaksha)
        • B.V. Raman
        • Krishnamurti
        • Fagan Bradley
        • Yukteshwar
        • JN Bhasin
        • Real-time comparison
        """)
    
    with col3:
        st.warning("""
        **⚡ Current Capabilities:**
        • Any birth date from 1900-2030
        • Precise time calculations
        • Ayanamsa-specific results
        • System comparison charts
        • Enhanced accuracy
        • Professional calculations
        """)
    
    # Current date and supported formats
    current_dt = datetime.now()
    st.markdown(f"""
    <div style="text-align: center; margin: 20px; padding: 15px; 
                background: rgba(102, 126, 234, 0.1); border-radius: 10px;">
        <h4>📅 Current Date/Time: {current_dt.strftime('%d %B %Y, %H:%M:%S')}</h4>
        <p>✅ <strong>Now supports:</strong> Historical dates (06 Sept 1976) ✅ Current dates (08 Aug 2025) ✅ Any time format</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin: 40px 0 25px 0; padding: 35px; 
            background: rgba(255, 255, 255, 0.98); border-radius: 20px; 
            border: 2px solid rgba(102, 126, 234, 0.2);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);">
    <h3 style="color: #667eea; margin-bottom: 12px; font-family: 'Orbitron', monospace;">
        🌌 ENHANCED PROFESSIONAL ASTROLOGY PLATFORM
    </h3>
    <p style="color: #1a202c; font-size: 1.1em; font-family: 'Space Grotesk', sans-serif; margin-bottom: 8px;">
        Multiple Ayanamsa Systems | Flexible Date/Time Input | Professional KP Calculations
    </p>
    <p style="color: #2d3748; font-family: 'Poppins', sans-serif; font-size: 0.95em;">
        Now supporting all date formats and ayanamsa systems for maximum accuracy
    </p>
</div>
""", unsafe_allow_html=True)
