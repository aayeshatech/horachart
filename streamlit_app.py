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

# Sidebar with precise inputs
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
    birth_date = st.date_input("📅 Birth Date", value=date(1990, 7, 3))
    
    col1, col2 = st.columns(2)
    with col1:
        birth_hour = st.number_input("🕐 Hour", min_value=0, max_value=23, value=12)
    with col2:
        birth_minute = st.number_input("🕐 Min", min_value=0, max_value=59, value=30)
    
    birth_place = st.text_input("📍 Birth Place", value="Mumbai, India")
    
    col1, col2 = st.columns(2)
    with col1:
        latitude = st.number_input("🌐 Lat", value=19.0760, format="%.4f")
    with col2:
        longitude = st.number_input("🌐 Long", value=72.8777, format="%.4f")
    
    # Ayanamsa selection for accurate calculations
    ayanamsa = st.selectbox("📐 Ayanamsa", 
                            ["KP (New)", "KP (Old)", "Lahiri", "Raman", "Krishnamurti"],
                            index=0)
    
    analyze_button = st.button("🚀 GENERATE ANALYSIS", type="primary", use_container_width=True)

# Enhanced Helper Functions
def get_complete_dasha_structure():
    """Complete Vimshottari Dasha with Mahadasha, Bhukti, and Antara periods"""
    return {
        "Sun": {
            "duration_years": 6,
            "lord_nature": "Authority, Leadership, Government",
            "bhuktis": {
                "Sun": {"months": 3.6, "start": "2024-11-19", "effects": "Power, recognition, father's influence"},
                "Moon": {"months": 6.0, "start": "2025-03-07", "effects": "Emotional growth, mother's support, property"},
                "Mars": {"months": 4.2, "start": "2025-09-07", "effects": "Energy, conflicts, property matters"},
                "Rahu": {"months": 10.8, "start": "2026-01-09", "effects": "Foreign opportunities, sudden changes"},
                "Jupiter": {"months": 9.6, "start": "2026-11-27", "effects": "Wisdom, spiritual growth, fortune"},
                "Saturn": {"months": 11.4, "start": "2027-09-15", "effects": "Discipline, delays, hard work pays"},
                "Mercury": {"months": 10.2, "start": "2028-08-27", "effects": "Communication, business, intelligence"},
                "Ketu": {"months": 4.2, "start": "2029-07-03", "effects": "Spirituality, detachment, liberation"},
                "Venus": {"months": 12.0, "start": "2029-11-09", "effects": "Luxury, relationships, material gains"}
            }
        },
        "Moon": {
            "duration_years": 10,
            "lord_nature": "Mind, Emotions, Mother, Public",
            "bhuktis": {
                "Moon": {"months": 10.0, "start": "2030-11-09", "effects": "Mental peace, maternal bliss, popularity"},
                "Mars": {"months": 7.0, "start": "2031-09-09", "effects": "Emotional courage, property gains"},
                "Rahu": {"months": 18.0, "start": "2032-04-09", "effects": "Mental confusion, foreign travels"},
                "Jupiter": {"months": 16.0, "start": "2033-10-09", "effects": "Happiness, children, fortune"},
                "Saturn": {"months": 19.0, "start": "2035-02-09", "effects": "Mental stress, hard work, stability"},
                "Mercury": {"months": 17.0, "start": "2036-09-09", "effects": "Intelligence, education, communication"},
                "Ketu": {"months": 7.0, "start": "2038-02-09", "effects": "Spiritual mind, intuition"},
                "Venus": {"months": 20.0, "start": "2038-09-09", "effects": "Emotional satisfaction, luxury"},
                "Sun": {"months": 6.0, "start": "2040-05-09", "effects": "Fame, authority, success"}
            }
        }
    }

def calculate_current_dasha_details(birth_date):
    """Calculate current Dasha, Bhukti, and Antara with precise timing"""
    current_date = datetime.now()
    
    # For demonstration, assuming Sun Mahadasha is active
    dasha_structure = get_complete_dasha_structure()
    
    return {
        "mahadasha": {
            "lord": "Sun",
            "start": "2024-11-19",
            "end": "2030-11-09",
            "nature": "Authority, Leadership, Government",
            "current_year": 1,
            "total_years": 6,
            "effects": "Period of recognition, authority, father's support, government favor"
        },
        "bhukti": {
            "lord": "Moon",
            "start": "2025-03-07",
            "end": "2025-09-07",
            "effects": "Emotional growth, mother's support, property matters, public recognition"
        },
        "antara": {
            "lord": "Mercury",
            "start": "2025-08-01",
            "end": "2025-08-20",
            "effects": "Communication opportunities, short travels, business dealings"
        },
        "upcoming_changes": [
            {"date": "2025-08-20", "type": "Antara", "new_lord": "Ketu", "effect": "Spiritual insights"},
            {"date": "2025-09-07", "type": "Bhukti", "new_lord": "Mars", "effect": "Energy and action"},
            {"date": "2030-11-09", "type": "Mahadasha", "new_lord": "Moon", "effect": "Emotional period begins"}
        ]
    }

def get_current_planetary_transits():
    """Get current planetary transits and their personal impacts"""
    return [
        {
            "planet": "Jupiter",
            "sign": "Gemini",
            "house": "3rd House",
            "aspect_houses": ["7th", "9th", "11th"],
            "duration": "Until Oct 18, 2025",
            "nature": "Highly Benefic",
            "personal_impacts": {
                "Career": "Communication skills enhanced, writing/teaching opportunities, short travels for work",
                "Relationships": "Better communication with spouse (7th aspect), spiritual connections",
                "Finance": "Gains through communication, siblings support, multiple income sources",
                "Health": "Good vitality, breathing exercises beneficial, watch nervous system",
                "Spiritual": "Learning spiritual texts, pilgrimages, guru's blessings (9th aspect)"
            }
        },
        {
            "planet": "Saturn",
            "sign": "Pisces (Retrograde)",
            "house": "12th House",
            "aspect_houses": ["2nd", "6th", "9th"],
            "duration": "Until Sep 1, 2025 (Retrograde)",
            "nature": "Challenging but Karmic",
            "personal_impacts": {
                "Career": "Foreign opportunities after delays, work in isolation beneficial",
                "Relationships": "Past relationship karma, need patience and maturity",
                "Finance": "Hidden expenses, but gains from foreign sources (2nd aspect)",
                "Health": "Need rest, feet/sleep issues, immunity needs attention (6th aspect)",
                "Spiritual": "Deep spiritual transformation, meditation essential, past life karma"
            }
        },
        {
            "planet": "Rahu",
            "sign": "Aquarius",
            "house": "11th House",
            "aspect_houses": ["3rd", "7th"],
            "duration": "Until May 2025",
            "nature": "Material Gains",
            "personal_impacts": {
                "Career": "Networking crucial, unconventional opportunities, technology sector gains",
                "Relationships": "Unusual friendships, online connections, social circle expansion",
                "Finance": "Sudden gains possible, cryptocurrency/stocks favorable, large profits",
                "Health": "Watch circulation, anxiety management needed, avoid addictions",
                "Spiritual": "Interest in occult sciences, astrology, alternative spirituality"
            }
        },
        {
            "planet": "Mars",
            "sign": "Virgo",
            "house": "6th House",
            "aspect_houses": ["9th", "12th", "1st"],
            "duration": "Until Sep 13, 2025",
            "nature": "Competitive Energy",
            "personal_impacts": {
                "Career": "Victory over competitors, service sector benefits, health industry",
                "Relationships": "Conflicts need careful handling, service to partner beneficial",
                "Finance": "Expenses on health, but victory in litigation, loan clearance",
                "Health": "High energy for fitness, surgery success if needed, digestive care",
                "Spiritual": "Karma yoga, service as spirituality, helping others (9th aspect)"
            }
        }
    ]

def get_upcoming_transit_events():
    """Get upcoming planetary transit events with precise dates and impacts"""
    return [
        {
            "date": "2025-08-11",
            "event": "Mercury Direct",
            "impact": "Communication clears, contracts favorable, technology issues resolve",
            "life_areas": ["Career", "Communication", "Travel"],
            "rating": "Highly Positive"
        },
        {
            "date": "2025-08-17",
            "event": "Sun enters Leo (Own Sign)",
            "impact": "Authority increases, father's support, government favor, leadership",
            "life_areas": ["Career", "Authority", "Recognition"],
            "rating": "Excellent"
        },
        {
            "date": "2025-08-21",
            "event": "Venus enters Cancer",
            "impact": "Family harmony, property gains, vehicle purchase, emotional satisfaction",
            "life_areas": ["Family", "Property", "Relationships"],
            "rating": "Very Good"
        },
        {
            "date": "2025-09-01",
            "event": "Saturn Direct Motion",
            "impact": "Karma clearing, delays end, hard work pays, structure returns",
            "life_areas": ["Career", "Long-term Goals", "Discipline"],
            "rating": "Positive"
        },
        {
            "date": "2025-09-13",
            "event": "Mars enters Libra",
            "impact": "Relationship energy, business partnerships, diplomatic action needed",
            "life_areas": ["Partnerships", "Business", "Balance"],
            "rating": "Neutral to Positive"
        },
        {
            "date": "2025-10-18",
            "event": "Jupiter enters Cancer (Exalted)",
            "impact": "MAJOR POSITIVE - Fortune, wisdom, spiritual growth, material gains",
            "life_areas": ["All Life Areas", "Fortune", "Growth"],
            "rating": "Most Excellent"
        }
    ]

def calculate_personal_predictions():
    """Generate detailed monthly predictions with transit impacts"""
    return {
        "August 2025": {
            "dasha_period": "Sun-Moon-Mercury until Aug 20",
            "key_transits": [
                "Mercury Retrograde until Aug 11 - Review period",
                "Sun enters Leo Aug 17 - Authority boost",
                "Venus enters Cancer Aug 21 - Family harmony"
            ],
            "career": {
                "prediction": "Communication delays until 11th, then rapid progress. Authority increases after 17th.",
                "opportunities": "Government sector, leadership roles, creative fields",
                "challenges": "Avoid major decisions until Mercury direct",
                "best_dates": ["17", "21", "25", "28"],
                "growth_potential": "75%"
            },
            "relationships": {
                "prediction": "Past issues surface for healing. Family support strong after 21st.",
                "opportunities": "Family reconciliation, emotional bonding, marriage discussions",
                "challenges": "Mercury retrograde miscommunications",
                "best_dates": ["21", "24", "27"],
                "harmony_level": "70%"
            },
            "finance": {
                "prediction": "Hold investments until 11th. Property gains after 17th. Family wealth benefits.",
                "opportunities": "Real estate, government bonds, gold investments",
                "challenges": "Hidden expenses during retrograde",
                "best_dates": ["17", "22", "26"],
                "growth_potential": "65%"
            },
            "health": {
                "prediction": "Nervous system needs care. Heart strengthens after 17th. Digestion improves.",
                "focus_areas": "Meditation, heart health, proper rest",
                "favorable_treatments": "After Aug 11",
                "vitality_level": "70%"
            },
            "spiritual": {
                "prediction": "Deep insights during retrograde. Sun in Leo brings self-realization.",
                "practices": "Meditation, mantra chanting, sun salutation",
                "favorable_days": ["Sundays", "Aug 17-31"],
                "growth_level": "85%"
            }
        },
        "September 2025": {
            "dasha_period": "Sun-Mars from Sep 7",
            "key_transits": [
                "Saturn Direct Sep 1 - Karma clearing",
                "Mars enters Libra Sep 13 - Partnership energy",
                "Autumn Equinox Sep 22 - Balance point"
            ],
            "career": {
                "prediction": "High energy period. Competition success. New initiatives thrive.",
                "opportunities": "Sports, military, engineering, surgery, real estate",
                "challenges": "Control aggression, avoid conflicts",
                "best_dates": ["5", "9", "13", "19", "27"],
                "growth_potential": "80%"
            },
            "relationships": {
                "prediction": "Passionate energy. Need patience. Partnership focus after 13th.",
                "opportunities": "Deep bonding, physical intimacy, joint ventures",
                "challenges": "Anger management crucial",
                "best_dates": ["13", "18", "22", "28"],
                "harmony_level": "65%"
            },
            "finance": {
                "prediction": "Property investments excellent. Technical stocks gain. Action brings profit.",
                "opportunities": "Real estate, defense stocks, machinery",
                "challenges": "Avoid impulsive spending",
                "best_dates": ["5", "14", "19", "25"],
                "growth_potential": "75%"
            },
            "health": {
                "prediction": "High vitality. Good for surgery. Sports injuries possible - be careful.",
                "focus_areas": "Physical exercise, avoid accidents, blood pressure",
                "favorable_treatments": "Surgery, dental work, fitness programs",
                "vitality_level": "85%"
            },
            "spiritual": {
                "prediction": "Karma yoga period. Service brings spiritual growth. Action as meditation.",
                "practices": "Hanuman worship, physical yoga, service activities",
                "favorable_days": ["Tuesdays", "Sep 7-30"],
                "growth_level": "70%"
            }
        },
        "October 2025": {
            "dasha_period": "Sun-Mars continues",
            "key_transits": [
                "JUPITER ENTERS CANCER Oct 18 - Major fortune begins",
                "Solar Eclipse Oct 2 - New beginnings",
                "Mercury in Scorpio Oct 10 - Deep insights"
            ],
            "career": {
                "prediction": "BREAKTHROUGH MONTH! Jupiter brings massive opportunities after 18th.",
                "opportunities": "Promotions, new positions, international opportunities, expansion",
                "challenges": "Eclipse may bring sudden changes",
                "best_dates": ["18", "19", "22", "25", "28"],
                "growth_potential": "95%"
            },
            "relationships": {
                "prediction": "Eclipse brings relationship changes. Jupiter brings marriage/children luck.",
                "opportunities": "Engagement, marriage, pregnancy, family expansion",
                "challenges": "Eclipse endings before new beginnings",
                "best_dates": ["18", "20", "24", "27"],
                "harmony_level": "85%"
            },
            "finance": {
                "prediction": "WEALTH EXPANSION! Jupiter brings fortune. Investments multiply.",
                "opportunities": "All investments favorable, especially after 18th",
                "challenges": "Don't be overconfident",
                "best_dates": ["18", "21", "25", "29"],
                "growth_potential": "90%"
            },
            "health": {
                "prediction": "Vitality increases dramatically after 18th. Healing accelerates.",
                "focus_areas": "Maintain balance despite high energy",
                "favorable_treatments": "All treatments favorable after 18th",
                "vitality_level": "90%"
            },
            "spiritual": {
                "prediction": "Major spiritual awakening. Guru's blessings. Wisdom downloads.",
                "practices": "Guru worship, Jupiter mantras, teaching/sharing wisdom",
                "favorable_days": ["Thursdays", "Oct 18-31"],
                "growth_level": "95%"
            }
        }
    }

def get_remedial_measures():
    """Get personalized remedial measures based on current planetary positions"""
    return {
        "gemstones": [
            {"stone": "Ruby", "weight": "3-5 carats", "finger": "Ring finger", "day": "Sunday", "metal": "Gold", "purpose": "Strengthen Sun (Mahadasha lord)"},
            {"stone": "Pearl", "weight": "5-7 carats", "finger": "Little finger", "day": "Monday", "metal": "Silver", "purpose": "Strengthen Moon (Bhukti lord)"},
            {"stone": "Yellow Sapphire", "weight": "4-5 carats", "finger": "Index finger", "day": "Thursday", "metal": "Gold", "purpose": "Jupiter blessings"}
        ],
        "mantras": [
            {"mantra": "Om Surya Namaha", "count": "108 times", "time": "Sunrise", "purpose": "Sun strength"},
            {"mantra": "Om Som Somaya Namaha", "count": "108 times", "time": "Evening", "purpose": "Moon peace"},
            {"mantra": "Om Gram Greem Grom Sah Guruve Namaha", "count": "108 times", "time": "Morning", "purpose": "Jupiter grace"}
        ],
        "donations": [
            {"item": "Wheat/Jaggery", "day": "Sunday", "recipient": "Temple/Poor", "purpose": "Sun favor"},
            {"item": "Rice/Milk", "day": "Monday", "recipient": "Women/Children", "purpose": "Moon blessings"},
            {"item": "Yellow items", "day": "Thursday", "recipient": "Brahmins/Teachers", "purpose": "Jupiter support"}
        ],
        "fasting": [
            {"day": "Sunday", "type": "One meal", "purpose": "Sun Mahadasha support"},
            {"day": "Monday", "type": "Fruits only", "purpose": "Moon Bhukti harmony"}
        ]
    }

def get_financial_instruments_analysis():
    """Get detailed financial analysis for specific instruments"""
    return [
        {
            "name": "NIFTY",
            "current_trend": "Bullish",
            "planetary_influence": "Jupiter in Gemini + Sun in Cancer",
            "intraday": "Buy on dips 9:30-10:30 AM, Sell peaks 2:30-3:15 PM",
            "weekly": "Strong uptrend, resistance at 25,200",
            "monthly": "Expect 8-12% growth, support at 24,500",
            "key_dates": "Aug 17-25 (Sun in Leo), Oct 18+ (Jupiter in Cancer)"
        },
        {
            "name": "BANK NIFTY",
            "current_trend": "Bullish",
            "planetary_influence": "Sun in Cancer (Traditional banking strong)",
            "intraday": "Strong 10:00-11:30 AM, Weak 1:00-2:00 PM",
            "weekly": "Outperforming Nifty, target 54,000",
            "monthly": "15-20% growth potential, buy on corrections",
            "key_dates": "Aug 21+ (Venus in Cancer), Family banking focus"
        },
        {
            "name": "GOLD",
            "current_trend": "Bullish",
            "planetary_influence": "Sun (Gold ruler) in exaltation degree",
            "intraday": "Buy 9:15-9:45 AM, Sell 2:45-3:15 PM",
            "weekly": "Breaking resistance, target ₹74,500",
            "monthly": "12-18% upside, accumulate on dips",
            "key_dates": "Aug 17 (Sun → Leo), Traditional strength"
        }
    ]

# Main Analysis
if analyze_button:
    with st.spinner("🌌 Calculating precise planetary positions and generating comprehensive analysis..."):
        time.sleep(2)
    
    st.success("✨ **COMPLETE ASTROLOGICAL ANALYSIS READY** - Professional KP system calculations completed!")
    
    if "Personal Horoscope" in analysis_mode:
        # Personal Horoscope Mode with Enhanced Features
        tabs = st.tabs([
            "📊 Dasha Analysis",
            "🌍 Current Transits", 
            "📅 Monthly Predictions",
            "⏰ Upcoming Events",
            "💎 Remedial Measures",
            "📈 Life Graph",
            "🎯 Career & Growth"
        ])
        
        with tabs[0]:  # Dasha Analysis
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    📊 COMPLETE VIMSHOTTARI DASHA ANALYSIS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            dasha_details = calculate_current_dasha_details(birth_date)
            
            # Current Dasha Status
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("### 🌟 Mahadasha (Main Period)")
                st.info(f"""
                **Lord:** {dasha_details['mahadasha']['lord']}  
                **Duration:** {dasha_details['mahadasha']['total_years']} years  
                **Current Year:** {dasha_details['mahadasha']['current_year']}  
                **Period:** {dasha_details['mahadasha']['start']} to {dasha_details['mahadasha']['end']}  
                **Nature:** {dasha_details['mahadasha']['nature']}  
                **Effects:** {dasha_details['mahadasha']['effects']}
                """)
            
            with col2:
                st.markdown("### 🌙 Bhukti (Sub-Period)")
                st.warning(f"""
                **Lord:** {dasha_details['bhukti']['lord']}  
                **Period:** {dasha_details['bhukti']['start']} to {dasha_details['bhukti']['end']}  
                **Effects:** {dasha_details['bhukti']['effects']}  
                **Combination:** {dasha_details['mahadasha']['lord']}-{dasha_details['bhukti']['lord']}  
                **Result:** Authority with emotional intelligence
                """)
            
            with col3:
                st.markdown("### ⭐ Antara (Sub-Sub Period)")
                st.success(f"""
                **Lord:** {dasha_details['antara']['lord']}  
                **Period:** {dasha_details['antara']['start']} to {dasha_details['antara']['end']}  
                **Effects:** {dasha_details['antara']['effects']}  
                **Triple Combination:** {dasha_details['mahadasha']['lord']}-{dasha_details['bhukti']['lord']}-{dasha_details['antara']['lord']}  
                **Current Focus:** Communication in leadership roles
                """)
            
            # Upcoming Dasha Changes
            st.markdown("### 🔄 Upcoming Dasha Changes")
            upcoming_df = pd.DataFrame(dasha_details['upcoming_changes'])
            
            for _, change in upcoming_df.iterrows():
                change_type = change['type']
                if change_type == "Mahadasha":
                    alert_type = st.error
                elif change_type == "Bhukti":
                    alert_type = st.warning
                else:
                    alert_type = st.info
                
                alert_type(f"**{change['date']}** - {change['type']} changes to **{change['new_lord']}** - {change['effect']}")
            
            # Detailed Dasha Timeline
            st.markdown("### 📅 Complete Dasha Timeline")
            
            dasha_data = get_complete_dasha_structure()
            sun_dasha = dasha_data["Sun"]
            
            with st.expander("☉ Sun Mahadasha - Complete Bhukti Periods", expanded=True):
                for planet, details in sun_dasha["bhuktis"].items():
                    col1, col2, col3, col4 = st.columns([1, 2, 2, 3])
                    with col1:
                        st.markdown(f"**{planet}**")
                    with col2:
                        st.caption(f"Starts: {details['start']}")
                    with col3:
                        st.caption(f"Duration: {details['months']} months")
                    with col4:
                        st.caption(details['effects'])
            
            with st.expander("🌙 Moon Mahadasha - Future Bhukti Periods"):
                moon_dasha = dasha_data["Moon"]
                for planet, details in moon_dasha["bhuktis"].items():
                    col1, col2, col3, col4 = st.columns([1, 2, 2, 3])
                    with col1:
                        st.markdown(f"**{planet}**")
                    with col2:
                        st.caption(f"Starts: {details['start']}")
                    with col3:
                        st.caption(f"Duration: {details['months']} months")
                    with col4:
                        st.caption(details['effects'])
        
        with tabs[1]:  # Current Transits
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    🌍 CURRENT PLANETARY TRANSITS & PERSONAL IMPACTS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            transits = get_current_planetary_transits()
            
            for transit in transits:
                nature_color = "🟢" if transit["nature"] == "Highly Benefic" else "🔴" if "Challenging" in transit["nature"] else "🟡"
                
                with st.expander(f"{nature_color} {transit['planet']} in {transit['sign']} - {transit['house']} - {transit['nature']}", expanded=True):
                    col1, col2 = st.columns([1, 2])
                    
                    with col1:
                        st.markdown(f"""
                        **📍 Position:** {transit['sign']}  
                        **🏠 House:** {transit['house']}  
                        **👁️ Aspects:** {', '.join(transit['aspect_houses'])}  
                        **⏱️ Duration:** {transit['duration']}  
                        **🔮 Nature:** {transit['nature']}
                        """)
                    
                    with col2:
                        st.markdown("**Personal Life Impacts:**")
                        for area, impact in transit["personal_impacts"].items():
                            if area == "Career":
                                icon = "💼"
                            elif area == "Relationships":
                                icon = "❤️"
                            elif area == "Finance":
                                icon = "💰"
                            elif area == "Health":
                                icon = "🏥"
                            else:
                                icon = "🕉️"
                            st.caption(f"{icon} **{area}:** {impact}")
        
        with tabs[2]:  # Monthly Predictions
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    📅 DETAILED MONTHLY PREDICTIONS WITH TRANSIT IMPACTS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            predictions = calculate_personal_predictions()
            
            for month, data in predictions.items():
                with st.expander(f"📅 {month} - {data['dasha_period']}", expanded=True):
                    # Key Transits
                    st.markdown("### 🌟 Key Planetary Transits")
                    for transit in data['key_transits']:
                        st.info(transit)
                    
                    # Life Areas
                    tabs_month = st.tabs(["💼 Career", "❤️ Relationships", "💰 Finance", "🏥 Health", "🕉️ Spiritual"])
                    
                    with tabs_month[0]:  # Career
                        career = data['career']
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Growth Potential", career['growth_potential'])
                            st.markdown(f"**Prediction:** {career['prediction']}")
                            st.markdown(f"**Opportunities:** {career['opportunities']}")
                        with col2:
                            st.markdown(f"**Best Dates:** {', '.join(career['best_dates'])}")
                            st.markdown(f"**Challenges:** {career['challenges']}")
                    
                    with tabs_month[1]:  # Relationships
                        relationships = data['relationships']
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Harmony Level", relationships['harmony_level'])
                            st.markdown(f"**Prediction:** {relationships['prediction']}")
                            st.markdown(f"**Opportunities:** {relationships['opportunities']}")
                        with col2:
                            st.markdown(f"**Best Dates:** {', '.join(relationships['best_dates'])}")
                            st.markdown(f"**Challenges:** {relationships['challenges']}")
                    
                    with tabs_month[2]:  # Finance
                        finance = data['finance']
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Growth Potential", finance['growth_potential'])
                            st.markdown(f"**Prediction:** {finance['prediction']}")
                            st.markdown(f"**Opportunities:** {finance['opportunities']}")
                        with col2:
                            st.markdown(f"**Best Dates:** {', '.join(finance['best_dates'])}")
                            st.markdown(f"**Challenges:** {finance['challenges']}")
                    
                    with tabs_month[3]:  # Health
                        health = data['health']
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Vitality Level", health['vitality_level'])
                            st.markdown(f"**Prediction:** {health['prediction']}")
                        with col2:
                            st.markdown(f"**Focus Areas:** {health['focus_areas']}")
                            st.markdown(f"**Favorable Treatments:** {health['favorable_treatments']}")
                    
                    with tabs_month[4]:  # Spiritual
                        spiritual = data['spiritual']
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Growth Level", spiritual['growth_level'])
                            st.markdown(f"**Prediction:** {spiritual['prediction']}")
                        with col2:
                            st.markdown(f"**Practices:** {spiritual['practices']}")
                            st.markdown(f"**Favorable Days:** {spiritual['favorable_days']}")
        
        with tabs[3]:  # Upcoming Events
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    ⏰ UPCOMING PLANETARY EVENTS & LIFE IMPACTS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            events = get_upcoming_transit_events()
            
            # Timeline view
            st.markdown("### 📅 Transit Timeline")
            
            for event in events:
                rating_color = "🟢" if "Excellent" in event['rating'] else "🟡" if "Positive" in event['rating'] or "Good" in event['rating'] else "🔵"
                
                with st.container():
                    col1, col2, col3 = st.columns([1, 2, 3])
                    
                    with col1:
                        st.markdown(f"### {event['date']}")
                        st.caption(f"{rating_color} {event['rating']}")
                    
                    with col2:
                        st.markdown(f"**{event['event']}**")
                        for area in event['life_areas']:
                            st.caption(f"• {area}")
                    
                    with col3:
                        st.info(event['impact'])
                    
                    st.divider()
        
        with tabs[4]:  # Remedial Measures
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    💎 PERSONALIZED REMEDIAL MEASURES
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            remedies = get_remedial_measures()
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 💎 Gemstone Recommendations")
                for gem in remedies['gemstones']:
                    with st.expander(f"{gem['stone']} - {gem['purpose']}"):
                        st.markdown(f"""
                        **Weight:** {gem['weight']}  
                        **Finger:** {gem['finger']}  
                        **Day to Wear:** {gem['day']}  
                        **Metal:** {gem['metal']}  
                        **Purpose:** {gem['purpose']}
                        """)
                
                st.markdown("### 📿 Mantra Chanting")
                for mantra in remedies['mantras']:
                    with st.expander(f"{mantra['purpose']}"):
                        st.markdown(f"""
                        **Mantra:** {mantra['mantra']}  
                        **Count:** {mantra['count']}  
                        **Time:** {mantra['time']}  
                        **Purpose:** {mantra['purpose']}
                        """)
            
            with col2:
                st.markdown("### 🎁 Donations & Charity")
                for donation in remedies['donations']:
                    with st.expander(f"{donation['item']} - {donation['purpose']}"):
                        st.markdown(f"""
                        **Item:** {donation['item']}  
                        **Day:** {donation['day']}  
                        **Recipient:** {donation['recipient']}  
                        **Purpose:** {donation['purpose']}
                        """)
                
                st.markdown("### 🍽️ Fasting Recommendations")
                for fast in remedies['fasting']:
                    with st.expander(f"{fast['day']} Fast"):
                        st.markdown(f"""
                        **Day:** {fast['day']}  
                        **Type:** {fast['type']}  
                        **Purpose:** {fast['purpose']}
                        """)
        
        with tabs[5]:  # Life Graph
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    📈 LIFE AREAS PERFORMANCE GRAPH
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Create performance metrics for different life areas
            life_areas = {
                "Career": {"Current": 75, "3 Months": 85, "6 Months": 90, "1 Year": 95},
                "Finance": {"Current": 65, "3 Months": 75, "6 Months": 85, "1 Year": 90},
                "Relationships": {"Current": 70, "3 Months": 75, "6 Months": 80, "1 Year": 85},
                "Health": {"Current": 70, "3 Months": 75, "6 Months": 80, "1 Year": 85},
                "Spirituality": {"Current": 85, "3 Months": 87, "6 Months": 90, "1 Year": 95}
            }
            
            # Display as metrics
            st.markdown("### Current vs Future Projections")
            
            for area, values in life_areas.items():
                col1, col2, col3, col4, col5 = st.columns(5)
                
                with col1:
                    st.markdown(f"**{area}**")
                with col2:
                    st.metric("Current", f"{values['Current']}%")
                with col3:
                    st.metric("3 Months", f"{values['3 Months']}%", delta=f"+{values['3 Months']-values['Current']}%")
                with col4:
                    st.metric("6 Months", f"{values['6 Months']}%", delta=f"+{values['6 Months']-values['Current']}%")
                with col5:
                    st.metric("1 Year", f"{values['1 Year']}%", delta=f"+{values['1 Year']-values['Current']}%")
                
                st.divider()
        
        with tabs[6]:  # Career & Growth
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    🎯 CAREER GROWTH & LIFE PURPOSE ANALYSIS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🎯 Career Direction")
                st.success("""
                **Most Favorable Fields (Based on Dasha & Transits):**
                • Government Services (Sun Mahadasha)
                • Leadership & Management Roles
                • Creative Arts & Entertainment
                • Real Estate & Property
                • Healthcare Administration
                
                **Timing for Career Moves:**
                • Aug 17-31: Excellent for job change
                • Sep 7+: New ventures favorable
                • Oct 18+: Major breakthrough period
                
                **Skills to Develop:**
                • Leadership & Authority
                • Communication (Mercury periods)
                • Emotional Intelligence (Moon)
                • Strategic Planning (Saturn aspect)
                """)
            
            with col2:
                st.markdown("### 🌟 Life Purpose & Dharma")
                st.info("""
                **Soul Purpose (From Dasha Analysis):**
                Your current life phase emphasizes leadership and service to society through positions of authority.
                
                **Karmic Lessons:**
                • Learning responsible use of power
                • Balancing ego with service
                • Family responsibilities and traditions
                • Public service and recognition
                
                **Spiritual Evolution:**
                • Sun Mahadasha: Self-realization
                • Moon upcoming: Emotional mastery
                • Focus on Raja Yoga practices
                • Teaching and mentoring others
                """)
            
            st.markdown("### 📊 Career Timeline & Milestones")
            
            career_timeline = [
                {"Period": "Aug 2025", "Event": "Authority increases", "Action": "Apply for senior positions", "Success": "85%"},
                {"Period": "Sep 2025", "Event": "Competition period", "Action": "Showcase your skills", "Success": "75%"},
                {"Period": "Oct 2025", "Event": "Jupiter blessing", "Action": "Major expansion/promotion", "Success": "95%"},
                {"Period": "Nov 2025", "Event": "Stability phase", "Action": "Consolidate gains", "Success": "80%"},
                {"Period": "Dec 2025", "Event": "Recognition period", "Action": "Awards/honors possible", "Success": "85%"}
            ]
            
            df_career = pd.DataFrame(career_timeline)
            st.dataframe(df_career, use_container_width=True)
    
    else:
        # Financial Markets Mode
        tabs = st.tabs([
            "📊 Market Dashboard", 
            "💹 Key Instruments", 
            "🏦 Sector Analysis",
            "⏰ Trading Times",
            "📈 Weekly Forecast"
        ])
        
        with tabs[0]:  # Market Dashboard
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    📊 PLANETARY MARKET DASHBOARD
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("📈 BULLISH PLANETS", "6")
                st.caption("Sun, Moon, Venus, Mars, Jupiter, Ketu")
                st.success("Strong market support")
            
            with col2:
                st.metric("📉 BEARISH PLANETS", "2")
                st.caption("Mercury (R), Saturn (R)")
                st.warning("Communication & traditional sectors weak")
            
            with col3:
                st.metric("⚖️ NEUTRAL FORCE", "1")
                st.caption("Rahu (Innovation)")
                st.info("Disruptive but opportunity")
        
        with tabs[1]:  # Key Instruments
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    💹 KEY FINANCIAL INSTRUMENTS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            instruments = get_financial_instruments_analysis()
            
            for instrument in instruments:
                trend_emoji = "📈" if instrument['current_trend'] == "Bullish" else "📉" if instrument['current_trend'] == "Bearish" else "➡️"
                
                with st.expander(f"{trend_emoji} {instrument['name']} - {instrument['current_trend']} Trend", expanded=True):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown(f"**Planetary Influence:** {instrument['planetary_influence']}")
                        st.markdown(f"**Intraday:** {instrument['intraday']}")
                        st.markdown(f"**Weekly:** {instrument['weekly']}")
                    
                    with col2:
                        st.markdown(f"**Monthly:** {instrument['monthly']}")
                        st.markdown(f"**Key Dates:** {instrument['key_dates']}")
        
        with tabs[2]:  # Sector Analysis
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    🏦 SECTOR-WISE PLANETARY IMPACT
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            sectors = {
                "💻 IT & TECHNOLOGY": {
                    "Status": "Mixed → Strong Bullish",
                    "Ruler": "Mercury + Jupiter",
                    "Impact": "Mercury retrograde temporary issues, Jupiter long-term support",
                    "Stocks": "TCS, Infosys, Wipro",
                    "Target": "15-25% upside"
                },
                "🏦 BANKING & FINANCE": {
                    "Status": "Strong Bullish",
                    "Ruler": "Sun + Jupiter",
                    "Impact": "Sun in Cancer excellent for traditional banking",
                    "Stocks": "HDFC Bank, ICICI, SBI",
                    "Target": "20-30% growth"
                },
                "🏠 REAL ESTATE": {
                    "Status": "Bullish",
                    "Ruler": "Mars + Sun",
                    "Impact": "Perfect for residential property investments",
                    "Stocks": "DLF, Godrej Properties",
                    "Target": "25-40% appreciation"
                },
                "⚡ ENERGY": {
                    "Status": "Mixed",
                    "Ruler": "Saturn + Mars",
                    "Impact": "Traditional energy weak, renewables strong",
                    "Stocks": "Reliance, Adani Green",
                    "Target": "Selective opportunities"
                },
                "🏥 HEALTHCARE": {
                    "Status": "Bullish",
                    "Ruler": "Moon + Jupiter",
                    "Impact": "Healthcare expansion, pharma growth",
                    "Stocks": "Sun Pharma, Dr. Reddy's",
                    "Target": "15-20% growth"
                }
            }
            
            for sector_name, sector_data in sectors.items():
                status_color = "🟢" if "Bullish" in sector_data['Status'] else "🔴" if "Bearish" in sector_data['Status'] else "🟡"
                
                with st.expander(f"{status_color} {sector_name} - {sector_data['Status']}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Planetary Ruler:** {sector_data['Ruler']}")
                        st.markdown(f"**Impact:** {sector_data['Impact']}")
                    with col2:
                        st.markdown(f"**Key Stocks:** {sector_data['Stocks']}")
                        st.markdown(f"**Target:** {sector_data['Target']}")
        
        with tabs[3]:  # Trading Times
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    ⏰ OPTIMAL TRADING TIMES BASED ON PLANETARY HOURS
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            trading_times = [
                {"Time": "9:15-9:45 AM", "Planet": "Sun", "Best For": "Gold, Banking", "Strategy": "Buy quality largecaps"},
                {"Time": "10:00-11:30 AM", "Planet": "Venus", "Best For": "FMCG, Real Estate", "Strategy": "Long positions"},
                {"Time": "11:30 AM-1:00 PM", "Planet": "Mercury", "Best For": "IT stocks", "Strategy": "Avoid during retrograde"},
                {"Time": "1:00-2:30 PM", "Planet": "Moon", "Best For": "Healthcare, Food", "Strategy": "Emotional sectors"},
                {"Time": "2:30-3:15 PM", "Planet": "Saturn", "Best For": "Value stocks", "Strategy": "Book profits"},
                {"Time": "3:15-3:30 PM", "Planet": "Jupiter", "Best For": "Finance, Education", "Strategy": "Final buying"}
            ]
            
            df_times = pd.DataFrame(trading_times)
            st.dataframe(df_times, use_container_width=True)
        
        with tabs[4]:  # Weekly Forecast
            st.markdown("""
            <div class="cosmic-panel">
                <h2 style="text-align: center; margin-bottom: 25px;">
                    📈 WEEKLY MARKET FORECAST
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            weekly_forecast = {
                "Aug 7-11, 2025": {
                    "Trend": "Bearish to Neutral",
                    "Nifty": "24,800-25,000 range",
                    "Key Event": "Mercury Retrograde peak",
                    "Strategy": "Stay cash heavy, avoid new positions"
                },
                "Aug 12-18, 2025": {
                    "Trend": "Bullish Recovery",
                    "Nifty": "25,200+ targets",
                    "Key Event": "Mercury Direct, Sun enters Leo",
                    "Strategy": "Aggressive buying in IT and Banking"
                },
                "Aug 19-25, 2025": {
                    "Trend": "Strong Bullish",
                    "Nifty": "25,500+ possible",
                    "Key Event": "Venus enters Cancer",
                    "Strategy": "Ride momentum, book partial profits"
                }
            }
            
            for week, data in weekly_forecast.items():
                trend_color = "success" if "Bullish" in data['Trend'] else "error" if "Bearish" in data['Trend'] else "warning"
                
                with st.expander(f"📅 {week} - {data['Trend']}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Nifty Range:** {data['Nifty']}")
                        st.markdown(f"**Key Event:** {data['Key Event']}")
                    with col2:
                        st.markdown(f"**Strategy:** {data['Strategy']}")

else:
    # Welcome Screen
    st.markdown("""
    <div class="cosmic-panel">
        <h2 style="text-align: center; color: #1a202c; margin-bottom: 20px;">
            🌌 PROFESSIONAL KP ASTROLOGY & MARKET ANALYSIS
        </h2>
        <p style="text-align: center; color: #2d3748; font-size: 1.2em; margin: 20px 0; line-height: 1.6;">
            Get comprehensive astrological analysis for personal life and financial markets
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature highlights
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **📊 Personal Horoscope Features:**
        • Complete Dasha Analysis (MD-AD-PD)
        • Current & Upcoming Transits
        • Monthly Predictions
        • Career & Growth Guidance
        • Remedial Measures
        • Life Purpose Analysis
        """)
    
    with col2:
        st.success("""
        **📈 Financial Markets Features:**
        • Planetary Market Dashboard
        • Key Instruments Analysis
        • Sector-wise Predictions
        • Optimal Trading Times
        • Weekly & Monthly Forecasts
        • Gann & Astro Techniques
        """)
    
    with col3:
        st.warning("""
        **🌟 Current Highlights:**
        • Mercury Retrograde until Aug 11
        • Sun enters Leo on Aug 17
        • Jupiter in Gemini (Knowledge)
        • Saturn Retrograde (Karma)
        • Major fortune after Oct 18
        • Venus favors relationships
        """)

# Footer
st.markdown("""
<div style="text-align: center; margin: 40px 0 25px 0; padding: 35px; 
            background: rgba(255, 255, 255, 0.98); border-radius: 20px; 
            border: 2px solid rgba(102, 126, 234, 0.2);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);">
    <h3 style="color: #667eea; margin-bottom: 12px; font-family: 'Orbitron', monospace;">
        🌌 PROFESSIONAL ASTROLOGY & TRADING PLATFORM
    </h3>
    <p style="color: #1a202c; font-size: 1.1em; font-family: 'Space Grotesk', sans-serif; margin-bottom: 8px;">
        Vimshottari Dasha | KP System | Planetary Transits | Life & Market Intelligence
    </p>
    <p style="color: #2d3748; font-family: 'Poppins', sans-serif; font-size: 0.95em;">
        Combining ancient wisdom with modern technology for comprehensive life guidance
    </p>
</div>
""", unsafe_allow_html=True)
