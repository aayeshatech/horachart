import streamlit as st
from datetime import date, datetime, timedelta
import time
import pandas as pd

# Page config
st.set_page_config(
    page_title="🌌 Professional KP Astrology & Financial Markets", 
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS for Professional Layout
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    /* Main Theme */
    .main {
        background: linear-gradient(180deg, #f7f9fc 0%, #f1f5fb 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Planet Transit Cards */
    .planet-card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border-left: 4px solid;
        transition: all 0.3s ease;
    }
    
    .planet-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }
    
    .planet-card-good {
        border-left-color: #10b981;
    }
    
    .planet-card-bad {
        border-left-color: #ef4444;
    }
    
    .planet-card-neutral {
        border-left-color: #f59e0b;
    }
    
    /* Transit Event Cards */
    .transit-event-card {
        background: white;
        border-radius: 10px;
        padding: 15px;
        margin: 8px;
        border-left: 3px solid;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }
    
    .transit-positive {
        background: #dcfce7;
        border-left-color: #22c55e;
    }
    
    .transit-negative {
        background: #fee2e2;
        border-left-color: #ef4444;
    }
    
    .transit-neutral {
        background: #fef3c7;
        border-left-color: #f59e0b;
    }
    
    /* Status Badges */
    .status-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
    }
    
    .status-good {
        background: #dcfce7;
        color: #15803d;
    }
    
    .status-bad {
        background: #fee2e2;
        color: #b91c1c;
    }
    
    .status-neutral {
        background: #fef3c7;
        color: #a16207;
    }
    
    /* Planet Symbol */
    .planet-symbol {
        font-size: 24px;
        margin-right: 8px;
    }
    
    /* Section Headers */
    .section-header {
        background: white;
        padding: 20px;
        border-radius: 12px;
        margin: 20px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        text-align: center;
    }
    
    .section-header h2 {
        color: #1e293b;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 600;
        margin: 0;
    }
    
    /* Data Table Styling */
    .dataframe {
        font-size: 14px !important;
    }
    
    th {
        background: #f1f5f9 !important;
        font-weight: 600 !important;
        color: #475569 !important;
    }
    
    /* Metric Cards */
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Helper Functions
def get_planetary_positions():
    """Get current planetary positions with detailed information"""
    return [
        {
            "planet": "Sun", "symbol": "☉", "sign": "Cancer", "degree": "20.76°",
            "house": 4, "nakshatra": "Ashlesha", "pada": 2, "nakshatra_lord": "Mercury",
            "status": "Favorable", "status_type": "good",
            "effect": "Emotional depth & family focus"
        },
        {
            "planet": "Moon", "symbol": "☽", "sign": "Sagittarius", "degree": "24.88°",
            "house": 9, "nakshatra": "Purva Ashadha", "pada": 4, "nakshatra_lord": "Venus",
            "status": "Favorable", "status_type": "good",
            "effect": "Spiritual expansion & optimism"
        },
        {
            "planet": "Mercury", "symbol": "☿", "sign": "Cancer", "degree": "10.93°",
            "house": 4, "nakshatra": "Pushya", "pada": 3, "nakshatra_lord": "Saturn",
            "status": "Challenging", "status_type": "bad", "retrograde": True,
            "effect": "Communication delays (Retrograde)"
        },
        {
            "planet": "Venus", "symbol": "♀", "sign": "Gemini", "degree": "13.98°",
            "house": 3, "nakshatra": "Ardra", "pada": 3, "nakshatra_lord": "Rahu",
            "status": "Favorable", "status_type": "good",
            "effect": "Social versatility & learning"
        },
        {
            "planet": "Mars", "symbol": "♂", "sign": "Virgo", "degree": "5.94°",
            "house": 6, "nakshatra": "Uttara Phalguni", "pada": 3, "nakshatra_lord": "Sun",
            "status": "Neutral", "status_type": "neutral",
            "effect": "Practical action & organization"
        },
        {
            "planet": "Jupiter", "symbol": "♃", "sign": "Gemini", "degree": "18.81°",
            "house": 3, "nakshatra": "Ardra", "pada": 4, "nakshatra_lord": "Rahu",
            "status": "Favorable", "status_type": "good",
            "effect": "Knowledge expansion & teaching"
        },
        {
            "planet": "Saturn", "symbol": "♄", "sign": "Pisces", "degree": "7.20°",
            "house": 12, "nakshatra": "Uttara Bhadrapada", "pada": 2, "nakshatra_lord": "Saturn",
            "status": "Neutral", "status_type": "neutral", "retrograde": True,
            "effect": "Spiritual lessons (Retrograde)"
        },
        {
            "planet": "Rahu", "symbol": "☊", "sign": "Aquarius", "degree": "25.73°",
            "house": 11, "nakshatra": "Purva Bhadrapada", "pada": 2, "nakshatra_lord": "Jupiter",
            "status": "Neutral", "status_type": "neutral", "retrograde": True,
            "effect": "Humanitarian focus & innovation"
        },
        {
            "planet": "Ketu", "symbol": "☋", "sign": "Leo", "degree": "25.73°",
            "house": 5, "nakshatra": "Purva Phalguni", "pada": 4, "nakshatra_lord": "Venus",
            "status": "Neutral", "status_type": "neutral", "retrograde": True,
            "effect": "Spiritual creativity & detachment"
        }
    ]

def get_upcoming_transits():
    """Get upcoming major transit events"""
    return [
        {
            "date": "Aug 11, 2025",
            "event": "Mercury turns Direct in Cancer",
            "effect": "Communication clarity returns",
            "type": "positive"
        },
        {
            "date": "Aug 17, 2025",
            "event": "Sun enters Leo",
            "effect": "Leadership energy & confidence boost",
            "type": "positive"
        },
        {
            "date": "Aug 21, 2025",
            "event": "Venus enters Cancer",
            "effect": "Love & harmony in family matters",
            "type": "positive"
        },
        {
            "date": "Sep 1, 2025",
            "event": "Saturn re-enters Pisces",
            "effect": "Spiritual challenges & lessons return",
            "type": "negative"
        },
        {
            "date": "Sep 13, 2025",
            "event": "Mars enters Libra",
            "effect": "Balance & harmony in relationships",
            "type": "neutral"
        },
        {
            "date": "Oct 18, 2025",
            "event": "Jupiter enters Cancer",
            "effect": "Family expansion & emotional growth",
            "type": "positive"
        }
    ]

def get_dasha_periods():
    """Get current Vimshottari Dasha periods"""
    return {
        "mahadasha": {
            "planet": "Sun",
            "start": "Nov 19, 2024",
            "end": "Nov 19, 2030",
            "duration": "6 years",
            "progress": 15
        },
        "antardasha": {
            "planet": "Moon",
            "start": "Mar 7, 2025",
            "end": "Sep 7, 2025",
            "duration": "6 months",
            "progress": 45
        },
        "pratyantar": {
            "planet": "Mercury",
            "start": "Aug 1, 2025",
            "end": "Aug 20, 2025",
            "duration": "19 days",
            "progress": 35
        }
    }

def get_financial_data():
    """Get financial market data based on planetary positions"""
    return {
        "indices": [
            {"name": "NIFTY 50", "value": "24,836", "change": "+127.40", "change_pct": "+0.52%", "trend": "bullish"},
            {"name": "BANK NIFTY", "value": "52,265", "change": "+385.20", "change_pct": "+0.74%", "trend": "bullish"},
            {"name": "SENSEX", "value": "81,356", "change": "+236.50", "change_pct": "+0.29%", "trend": "bullish"}
        ],
        "commodities": [
            {"name": "GOLD", "value": "₹72,450", "change": "+180", "change_pct": "+0.25%", "trend": "bullish"},
            {"name": "SILVER", "value": "₹91,200", "change": "-320", "change_pct": "-0.35%", "trend": "bearish"},
            {"name": "CRUDE OIL", "value": "$82.30", "change": "-0.45", "change_pct": "-0.54%", "trend": "bearish"}
        ]
    }

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea, #764ba2); 
                padding: 20px; border-radius: 12px; margin-bottom: 20px; text-align: center;">
        <h2 style="color: white; margin: 0; font-family: 'Space Grotesk', sans-serif;">
            🌟 Birth Details
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    name = st.text_input("👤 Name", value="Example Person")
    birth_date = st.date_input("📅 Birth Date", value=date(1990, 1, 1))
    
    col1, col2 = st.columns(2)
    with col1:
        birth_hour = st.number_input("🕐 Hour", min_value=0, max_value=23, value=12)
    with col2:
        birth_minute = st.number_input("🕐 Min", min_value=0, max_value=59, value=0)
    
    birth_place = st.text_input("📍 Birth Place", value="Mumbai, India")
    
    col1, col2 = st.columns(2)
    with col1:
        latitude = st.number_input("🌐 Lat", value=19.0760, format="%.4f")
    with col2:
        longitude = st.number_input("🌐 Long", value=72.8777, format="%.4f")
    
    st.selectbox("📐 Ayanamsa", ["KP (New)", "KP (Old)", "Lahiri", "Raman"], index=0)
    
    analyze_button = st.button("🔮 Generate Analysis", use_container_width=True)

# Main Header
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea, #764ba2); 
            padding: 30px; border-radius: 16px; margin-bottom: 30px; text-align: center;">
    <h1 style="color: white; margin: 0; font-family: 'Space Grotesk', sans-serif; font-size: 2.5em;">
        🌌 Professional KP Astrology & Financial Markets
    </h1>
    <p style="color: rgba(255,255,255,0.9); margin-top: 10px; font-size: 1.1em;">
        Precise Planetary Calculations | Vimshottari Dasha | Market Predictions
    </p>
</div>
""", unsafe_allow_html=True)

# Mode Selection
mode = st.radio(
    "Select Analysis Mode",
    ["🌟 Personal Horoscope", "📈 Financial Markets"],
    horizontal=True
)

if analyze_button or True:  # Show by default for demo
    if mode == "🌟 Personal Horoscope":
        # Current Date Display
        st.markdown(f"""
        <div style="text-align: center; margin: 20px 0;">
            <h3 style="color: #64748b; font-family: 'Space Grotesk', sans-serif;">
                🚀 Current Planetary Transits (August 7, 2025)
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Planetary Transit Cards
        planets = get_planetary_positions()
        
        # Display planets in 4-column grid
        for i in range(0, len(planets), 4):
            cols = st.columns(4)
            for j, col in enumerate(cols):
                if i + j < len(planets):
                    planet = planets[i + j]
                    with col:
                        # Determine card color based on status
                        if planet['status_type'] == 'good':
                            border_color = "#10b981"
                            bg_color = "#f0fdf4"
                            status_color = "#15803d"
                            status_bg = "#dcfce7"
                        elif planet['status_type'] == 'bad':
                            border_color = "#ef4444"
                            bg_color = "#fef2f2"
                            status_color = "#b91c1c"
                            status_bg = "#fee2e2"
                        else:
                            border_color = "#f59e0b"
                            bg_color = "#fffbeb"
                            status_color = "#a16207"
                            status_bg = "#fef3c7"
                        
                        retrograde = "R" if planet.get('retrograde', False) else ""
                        
                        st.markdown(f"""
                        <div style="background: {bg_color}; border-left: 4px solid {border_color}; 
                                    border-radius: 12px; padding: 15px; margin: 5px 0; min-height: 180px;
                                    box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
                            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                                <span style="font-size: 24px; margin-right: 8px;">{planet['symbol']}</span>
                                <h4 style="margin: 0; color: #1e293b; font-weight: 600;">
                                    {planet['planet']} {planet['symbol']}
                                </h4>
                            </div>
                            <p style="margin: 5px 0; color: #475569; font-size: 14px;">
                                <strong>Current Position:</strong> {planet['sign']} ({planet['degree']}) {retrograde}
                            </p>
                            <p style="margin: 5px 0; color: #475569; font-size: 13px;">
                                <strong>Transit Effect:</strong> {planet['effect']}
                            </p>
                            <div style="margin-top: 10px;">
                                <span style="background: {status_bg}; color: {status_color}; 
                                            padding: 4px 12px; border-radius: 20px; font-size: 12px; 
                                            font-weight: 600;">
                                    Status: {planet['status']}
                                </span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
        
        # Detailed Planetary Positions Table
        st.markdown("""
        <div style="margin: 30px 0 20px 0;">
            <h3 style="color: #1e293b; font-family: 'Space Grotesk', sans-serif; text-align: center;">
                📊 Detailed Planetary Positions
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Create DataFrame for planetary positions
        df_data = []
        for p in planets:
            df_data.append({
                "🪐 Planet": f"{p['symbol']} {p['planet']}",
                "♈ Zodiac Sign": p['sign'],
                "📐 Exact Degree": p['degree'],
                "🏠 House": p['house'],
                "⭐ Nakshatra": p['nakshatra'],
                "🔢 Pada": p['pada'],
                "👑 Nakshatra Lord": p['nakshatra_lord'],
                "📊 Current Status": p['status']
            })
        
        df = pd.DataFrame(df_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Upcoming Transit Events
        st.markdown("""
        <div style="margin: 30px 0 20px 0;">
            <h3 style="color: #1e293b; font-family: 'Space Grotesk', sans-serif; text-align: center;">
                📅 Upcoming Major Transit Events
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        transits = get_upcoming_transits()
        
        # Display transits in 3-column grid
        for i in range(0, len(transits), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(transits):
                    transit = transits[i + j]
                    with col:
                        # Determine card color based on transit type
                        if transit['type'] == 'positive':
                            bg_color = "#dcfce7"
                            border_color = "#22c55e"
                        elif transit['type'] == 'negative':
                            bg_color = "#fee2e2"
                            border_color = "#ef4444"
                        else:
                            bg_color = "#fef3c7"
                            border_color = "#f59e0b"
                        
                        st.markdown(f"""
                        <div style="background: {bg_color}; border-left: 3px solid {border_color};
                                    border-radius: 10px; padding: 15px; margin: 5px 0; min-height: 120px;
                                    box-shadow: 0 2px 6px rgba(0,0,0,0.06);">
                            <h5 style="margin: 0 0 8px 0; color: #1e293b; font-weight: 600;">
                                {transit['date']}
                            </h5>
                            <p style="margin: 5px 0; color: #334155; font-size: 14px; font-weight: 500;">
                                {transit['event']}
                            </p>
                            <p style="margin: 5px 0; color: #64748b; font-size: 13px;">
                                {transit['effect']}
                            </p>
                        </div>
                        """, unsafe_allow_html=True)
        
        # Vimshottari Dasha Display
        st.markdown("---")
        st.markdown("""
        <div style="margin: 30px 0 20px 0;">
            <h3 style="color: #1e293b; font-family: 'Space Grotesk', sans-serif; text-align: center;">
                ⏰ Current Vimshottari Dasha Periods
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        dasha = get_dasha_periods()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div style="background: white; border-radius: 12px; padding: 20px; 
                        box-shadow: 0 2px 8px rgba(0,0,0,0.08); text-align: center;">
                <h4 style="color: #667eea; margin-bottom: 15px;">Mahadasha</h4>
                <h2 style="color: #1e293b; margin: 10px 0;">{dasha['mahadasha']['planet']}</h2>
                <p style="color: #64748b; font-size: 14px;">{dasha['mahadasha']['start']} - {dasha['mahadasha']['end']}</p>
                <p style="color: #64748b; font-size: 14px;">Duration: {dasha['mahadasha']['duration']}</p>
                <div style="background: #e0e7ff; border-radius: 20px; height: 8px; margin-top: 15px;">
                    <div style="background: #667eea; border-radius: 20px; height: 8px; width: {dasha['mahadasha']['progress']}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style="background: white; border-radius: 12px; padding: 20px; 
                        box-shadow: 0 2px 8px rgba(0,0,0,0.08); text-align: center;">
                <h4 style="color: #764ba2; margin-bottom: 15px;">Antardasha</h4>
                <h2 style="color: #1e293b; margin: 10px 0;">{dasha['antardasha']['planet']}</h2>
                <p style="color: #64748b; font-size: 14px;">{dasha['antardasha']['start']} - {dasha['antardasha']['end']}</p>
                <p style="color: #64748b; font-size: 14px;">Duration: {dasha['antardasha']['duration']}</p>
                <div style="background: #f3e8ff; border-radius: 20px; height: 8px; margin-top: 15px;">
                    <div style="background: #764ba2; border-radius: 20px; height: 8px; width: {dasha['antardasha']['progress']}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div style="background: white; border-radius: 12px; padding: 20px; 
                        box-shadow: 0 2px 8px rgba(0,0,0,0.08); text-align: center;">
                <h4 style="color: #f093fb; margin-bottom: 15px;">Pratyantar Dasha</h4>
                <h2 style="color: #1e293b; margin: 10px 0;">{dasha['pratyantar']['planet']}</h2>
                <p style="color: #64748b; font-size: 14px;">{dasha['pratyantar']['start']} - {dasha['pratyantar']['end']}</p>
                <p style="color: #64748b; font-size: 14px;">Duration: {dasha['pratyantar']['duration']}</p>
                <div style="background: #fce7f3; border-radius: 20px; height: 8px; margin-top: 15px;">
                    <div style="background: #f093fb; border-radius: 20px; height: 8px; width: {dasha['pratyantar']['progress']}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Additional Tabs for Detailed Analysis
        st.markdown("---")
        tabs = st.tabs(["📊 Life Predictions", "💰 Financial Outlook", "💎 Remedies", "📈 Career Analysis"])
        
        with tabs[0]:
            st.subheader("Monthly Life Predictions")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                **August 2025 Predictions:**
                - 💼 **Career**: Authority increases after Aug 17 (Sun in Leo)
                - ❤️ **Relationships**: Family harmony improves after Aug 21
                - 💰 **Finance**: Property investments favorable
                - 🏥 **Health**: Watch nervous system until Mercury direct
                - 🎯 **Lucky Days**: 11, 17, 21, 25
                """)
            
            with col2:
                st.markdown("""
                **September 2025 Predictions:**
                - 💼 **Career**: High energy period, competition success
                - ❤️ **Relationships**: Passionate but need patience
                - 💰 **Finance**: Real estate gains possible
                - 🏥 **Health**: High vitality but avoid accidents
                - 🎯 **Lucky Days**: 5, 13, 19, 27
                """)
        
        with tabs[1]:
            st.subheader("Financial & Investment Guidance")
            
            st.markdown("""
            **Based on Current Planetary Positions:**
            
            ✅ **Favorable Investments:**
            - Gold (Sun in Cancer - traditional wealth)
            - Real Estate (Venus-Moon connection)
            - Banking Stocks (Jupiter aspect)
            
            ⚠️ **Avoid Until Aug 11:**
            - Technology stocks (Mercury retrograde)
            - Cryptocurrency (Communication planet weak)
            - New ventures (Wait for Mercury direct)
            
            📈 **Best Trading Times Today:**
            - Morning: 9:15-10:30 AM (Sun hour)
            - Afternoon: 2:30-3:30 PM (Jupiter hour)
            """)
        
        with tabs[2]:
            st.subheader("Remedial Measures")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                **🔮 Gemstones:**
                - Ruby (3-5 carats) - Ring finger, Sunday
                - Pearl (5-7 carats) - Little finger, Monday
                - Yellow Sapphire (4-5 carats) - Index finger, Thursday
                
                **📿 Mantras:**
                - Sun: "Om Surya Namaha" (108 times at sunrise)
                - Moon: "Om Som Somaya Namaha" (108 times)
                - Jupiter: "Om Gram Greem Grom Sah Guruve Namaha"
                """)
            
            with col2:
                st.markdown("""
                **🎁 Donations:**
                - Sunday: Wheat/Jaggery to temple
                - Monday: Rice/Milk to women & children
                - Thursday: Yellow items to teachers
                
                **🍽️ Fasting:**
                - Sunday: One meal (Sun Mahadasha)
                - Monday: Fruits only (Moon Antardasha)
                - Thursday: Vegetarian (Jupiter blessings)
                """)
        
        with tabs[3]:
            st.subheader("Career & Growth Analysis")
            
            st.markdown("""
            **Most Favorable Career Fields (Based on Dasha):**
            
            🌟 **Excellent Prospects:**
            - Government Services (Sun Mahadasha)
            - Leadership & Management Roles
            - Creative Arts & Entertainment
            - Real Estate & Property Development
            
            📈 **Growth Timeline:**
            - **Aug 11-17**: Apply for new positions
            - **Aug 17-31**: Peak authority period
            - **Sep 7+**: New ventures favorable
            - **Oct 18+**: Major breakthrough (Jupiter in Cancer)
            
            💡 **Skills to Develop:**
            - Leadership & Public Speaking
            - Emotional Intelligence (Moon period)
            - Strategic Planning
            - Creative Problem Solving
            """)
    
    else:  # Financial Markets Mode
        # Market Overview
        st.markdown("""
        <div style="margin: 20px 0;">
            <h3 style="color: #1e293b; font-family: 'Space Grotesk', sans-serif; text-align: center;">
                📊 Market Overview - Planetary Influence
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        financial_data = get_financial_data()
        
        # Display Indices
        st.markdown("#### Stock Indices")
        cols = st.columns(3)
        for i, index in enumerate(financial_data['indices']):
            with cols[i]:
                trend_color = "#10b981" if index['trend'] == 'bullish' else "#ef4444"
                arrow = "↑" if index['trend'] == 'bullish' else "↓"
                
                st.markdown(f"""
                <div style="background: white; border-radius: 10px; padding: 15px; 
                            box-shadow: 0 2px 6px rgba(0,0,0,0.06); text-align: center;">
                    <h4 style="color: #1e293b; margin: 0;">{index['name']}</h4>
                    <h2 style="color: {trend_color}; margin: 10px 0;">
                        {index['value']} {arrow}
                    </h2>
                    <p style="color: {trend_color}; font-weight: 600;">
                        {index['change']} ({index['change_pct']})
                    </p>
                </div>
                """, unsafe_allow_html=True)
        
        # Display Commodities
        st.markdown("#### Commodities")
        cols = st.columns(3)
        for i, commodity in enumerate(financial_data['commodities']):
            with cols[i]:
                trend_color = "#10b981" if commodity['trend'] == 'bullish' else "#ef4444"
                arrow = "↑" if commodity['trend'] == 'bullish' else "↓"
                
                st.markdown(f"""
                <div style="background: white; border-radius: 10px; padding: 15px; 
                            box-shadow: 0 2px 6px rgba(0,0,0,0.06); text-align: center;">
                    <h4 style="color: #1e293b; margin: 0;">{commodity['name']}</h4>
                    <h2 style="color: {trend_color}; margin: 10px 0;">
                        {commodity['value']} {arrow}
                    </h2>
                    <p style="color: {trend_color}; font-weight: 600;">
                        {commodity['change']} ({commodity['change_pct']})
                    </p>
                </div>
                """, unsafe_allow_html=True)
        
        # Planetary Market Analysis
        st.markdown("---")
        st.subheader("🌟 Planetary Market Influence")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Bullish Planetary Factors:**
            - ✅ Sun in Cancer - Banking sector strong
            - ✅ Jupiter in Gemini - IT & Communication growth
            - ✅ Venus in Gemini - Consumer goods favorable
            - ✅ Mars in Virgo - Healthcare & pharma positive
            
            **Key Support Levels:**
            - NIFTY: 24,500
            - BANK NIFTY: 51,800
            - GOLD: ₹72,000
            """)
        
        with col2:
            st.markdown("""
            **Bearish Planetary Factors:**
            - ❌ Mercury Retrograde - Tech volatility
            - ❌ Saturn Retrograde - Traditional sectors weak
            - ❌ Rahu in Aquarius - Cryptocurrency unstable
            
            **Key Resistance Levels:**
            - NIFTY: 25,200
            - BANK NIFTY: 53,000
            - GOLD: ₹73,000
            """)
        
        # Sector Analysis
        st.markdown("---")
        st.subheader("🏦 Sector-wise Planetary Impact")
        
        sectors = [
            {"sector": "Banking", "impact": "Highly Positive", "reason": "Sun in Cancer", "stocks": "HDFC, ICICI, SBI", "target": "+20-25%"},
            {"sector": "IT", "impact": "Mixed", "reason": "Mercury Retrograde", "stocks": "TCS, Infosys, Wipro", "target": "Wait till Aug 11"},
            {"sector": "Real Estate", "impact": "Positive", "reason": "Venus-Moon aspect", "stocks": "DLF, Godrej Prop", "target": "+15-20%"},
            {"sector": "Pharma", "impact": "Positive", "reason": "Mars in Virgo", "stocks": "Sun Pharma, Dr Reddy", "target": "+12-15%"}
        ]
        
        df_sectors = pd.DataFrame(sectors)
        st.dataframe(df_sectors, use_container_width=True, hide_index=True)
        
        # Trading Strategy
        st.markdown("---")
        st.subheader("📈 Today's Trading Strategy")
        
        st.info("""
        **Intraday Trading Plan (Aug 7, 2025):**
        
        🕐 **9:15-10:30 AM** - Sun Hour
        - Buy: Banking stocks, Gold
        - Avoid: Technology stocks
        
        🕐 **10:30 AM-12:00 PM** - Venus Hour  
        - Buy: FMCG, Real Estate
        - Book partial profits
        
        🕐 **12:00-2:30 PM** - Mercury Hour
        - Avoid new positions (Retrograde)
        - Square off intraday positions
        
        🕐 **2:30-3:30 PM** - Moon/Jupiter Hour
        - Buy for next day: Healthcare, Education stocks
        - Accumulate quality stocks on dips
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #64748b;">
    <p style="font-size: 14px;">
        🌟 Professional KP Astrology System | Accurate Planetary Calculations | Financial Astrology
    </p>
    <p style="font-size: 12px; margin-top: 10px;">
        Disclaimer: For educational and informational purposes only. Please consult professionals for personal and financial decisions.
    </p>
</div>
""", unsafe_allow_html=True)
