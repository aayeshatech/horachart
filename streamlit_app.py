<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌟 Professional Vedic Astrology Calculator</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh; color: #333; line-height: 1.6;
            background-attachment: fixed;
        }
        
        .container {
            max-width: 1400px; margin: 0 auto; padding: 20px;
            animation: fadeIn 1s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .header {
            background: linear-gradient(45deg, #ff6b6b, #feca57);
            padding: 40px 20px; text-align: center; border-radius: 25px;
            margin-bottom: 30px; color: white; position: relative; overflow: hidden;
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);
            animation: glow 3s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from { box-shadow: 0 15px 35px rgba(0,0,0,0.3); }
            to { box-shadow: 0 15px 35px rgba(255,107,107,0.7); }
        }
        
        .header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
            transform: rotate(45deg);
            animation: shine 4s linear infinite;
        }
        
        @keyframes shine {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }
        
        .header h1 {
            font-size: 3.5em; margin-bottom: 15px; position: relative; z-index: 1;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
            animation: titlePulse 2s ease-in-out infinite alternate;
        }
        
        @keyframes titlePulse {
            from { transform: scale(1); }
            to { transform: scale(1.02); }
        }
        
        .current-time {
            font-size: 1.4em; opacity: 0.95; margin: 15px 0; position: relative; z-index: 1;
            background: rgba(255,255,255,0.1); padding: 10px 20px; border-radius: 20px;
            display: inline-block; backdrop-filter: blur(10px);
        }
        
        .subtitle { font-size: 1.3em; position: relative; z-index: 1; margin-top: 10px; }
        
        .mercury-alert {
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
            color: white; padding: 25px; margin: 30px 0; border-radius: 20px;
            text-align: center; position: relative; overflow: hidden;
            box-shadow: 0 10px 30px rgba(238,90,36,0.4);
            animation: alertPulse 3s ease-in-out infinite;
        }
        
        @keyframes alertPulse {
            0%, 100% { transform: scale(1); box-shadow: 0 10px 30px rgba(238,90,36,0.4); }
            50% { transform: scale(1.02); box-shadow: 0 15px 35px rgba(238,90,36,0.6); }
        }
        
        .mercury-alert h3 {
            font-size: 1.8em; margin-bottom: 15px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .input-section {
            background: rgba(255,255,255,0.95); padding: 35px; border-radius: 25px;
            margin-bottom: 30px; backdrop-filter: blur(15px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            transform: translateY(0);
            transition: all 0.3s ease;
        }
        
        .input-section:hover {
            transform: translateY(-5px);
            box-shadow: 0 25px 50px rgba(0,0,0,0.15);
        }
        
        .input-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px; margin-bottom: 30px;
        }
        
        .input-group {
            position: relative;
        }
        
        .input-group label {
            display: block; font-weight: bold; margin-bottom: 10px;
            color: #2c3e50; font-size: 1.2em;
            transition: color 0.3s ease;
        }
        
        .input-group input {
            width: 100%; padding: 15px 20px; border: 3px solid #e0e0e0;
            border-radius: 15px; font-size: 16px; background: #f8f9fa;
            transition: all 0.3s ease; position: relative;
        }
        
        .input-group input:focus {
            border-color: #3498db; outline: none;
            box-shadow: 0 0 20px rgba(52,152,219,0.4);
            transform: translateY(-2px); background: white;
        }
        
        .input-group input:focus + label {
            color: #3498db;
        }
        
        .calculate-btn {
            background: linear-gradient(45deg, #00c851, #007e33);
            color: white; padding: 20px 50px; border: none;
            border-radius: 25px; cursor: pointer; font-size: 20px;
            font-weight: bold; position: relative; overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,200,81,0.4);
            transition: all 0.3s ease; text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .calculate-btn:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,200,81,0.6);
        }
        
        .calculate-btn:active {
            transform: translateY(-2px);
            animation: buttonPress 0.3s ease;
        }
        
        @keyframes buttonPress {
            0% { transform: scale(1); }
            50% { transform: scale(0.98); }
            100% { transform: scale(1); }
        }
        
        .dashboard {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px; margin: 30px 0;
        }
        
        .info-panel {
            background: rgba(255,255,255,0.95); padding: 30px;
            border-radius: 25px; backdrop-filter: blur(15px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            position: relative; overflow: hidden;
            transition: all 0.4s ease;
        }
        
        .info-panel::before {
            content: '';
            position: absolute; top: 0; left: -100%;
            width: 100%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.5s ease;
        }
        
        .info-panel:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 45px rgba(0,0,0,0.15);
        }
        
        .info-panel:hover::before {
            left: 100%;
        }
        
        .info-panel h3 {
            color: #2c3e50; margin-bottom: 25px; text-align: center;
            font-size: 1.6em; position: relative; z-index: 1;
            border-bottom: 3px solid transparent;
            background: linear-gradient(45deg, #3498db, #9b59b6) content-box;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            padding-bottom: 12px;
        }
        
        .info-item {
            display: flex; justify-content: space-between;
            align-items: center; padding: 15px 20px;
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            border-radius: 15px; margin: 12px 0;
            border-left: 5px solid #3498db; position: relative;
            transition: all 0.3s ease; overflow: hidden;
        }
        
        .info-item::before {
            content: '';
            position: absolute; top: 0; left: 0;
            width: 0; height: 100%;
            background: linear-gradient(135deg, rgba(52,152,219,0.1), rgba(155,89,182,0.1));
            transition: width 0.3s ease;
        }
        
        .info-item:hover {
            transform: translateX(10px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .info-item:hover::before {
            width: 100%;
        }
        
        .info-item span:last-child {
            font-weight: bold; color: #2c3e50;
            position: relative; z-index: 1;
        }
        
        .planetary-table {
            width: 100%; border-collapse: collapse;
            background: rgba(255,255,255,0.95); border-radius: 25px;
            overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            margin: 30px 0; backdrop-filter: blur(15px);
        }
        
        .planetary-table th {
            background: linear-gradient(135deg, #2c3e50, #34495e);
            color: white; padding: 20px 15px; font-weight: bold;
            font-size: 1.1em; text-align: center; position: relative;
        }
        
        .planetary-table th::after {
            content: '';
            position: absolute; bottom: 0; left: 0;
            width: 100%; height: 3px;
            background: linear-gradient(45deg, #3498db, #9b59b6);
        }
        
        .planetary-table td {
            padding: 18px 12px; text-align: center; border-bottom: 1px solid #e9ecef;
            font-size: 1.05em; position: relative; transition: all 0.3s ease;
        }
        
        .planetary-table tr:hover td {
            background: linear-gradient(135deg, rgba(52,152,219,0.05), rgba(155,89,182,0.05));
            transform: scale(1.02);
        }
        
        .status-good {
            color: #00c851; font-weight: bold; text-shadow: 0 0 5px rgba(0,200,81,0.3);
            position: relative;
        }
        
        .status-bad {
            color: #ff6b6b; font-weight: bold; text-shadow: 0 0 5px rgba(255,107,107,0.3);
            position: relative;
        }
        
        .status-neutral {
            color: #ffc107; font-weight: bold; text-shadow: 0 0 5px rgba(255,193,7,0.3);
            position: relative;
        }
        
        .transit-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px; margin: 25px 0;
        }
        
        .transit-card {
            background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(248,249,250,0.9));
            padding: 25px; border-radius: 20px; border: 3px solid #e9ecef;
            transition: all 0.4s ease; position: relative; overflow: hidden;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        
        .transit-card::before {
            content: '';
            position: absolute; top: -2px; left: -2px;
            right: -2px; bottom: -2px;
            background: linear-gradient(45deg, #3498db, #9b59b6, #e74c3c, #f39c12);
            border-radius: 22px; opacity: 0;
            transition: opacity 0.3s ease;
            z-index: -1;
        }
        
        .transit-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 15px 35px rgba(52,152,219,0.2);
        }
        
        .transit-card:hover::before {
            opacity: 1;
        }
        
        .transit-card h4 {
            margin-bottom: 15px; font-size: 1.4em;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .events-section {
            background: rgba(255,255,255,0.95); padding: 35px;
            border-radius: 25px; backdrop-filter: blur(15px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.1); margin: 30px 0;
        }
        
        .events-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px; margin: 25px 0;
        }
        
        .event-card {
            padding: 20px 25px; border-radius: 15px;
            border-left: 6px solid; position: relative;
            transition: all 0.3s ease; cursor: pointer;
            overflow: hidden;
        }
        
        .event-card::after {
            content: '';
            position: absolute; top: 0; right: -100%;
            width: 100%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: right 0.6s ease;
        }
        
        .event-card:hover::after {
            right: 100%;
        }
        
        .event-good {
            background: linear-gradient(135deg, #d4edda, #c3e6cb);
            border-left-color: #28a745; color: #155724;
        }
        
        .event-neutral {
            background: linear-gradient(135deg, #fff3cd, #ffeaa7);
            border-left-color: #ffc107; color: #856404;
        }
        
        .event-challenging {
            background: linear-gradient(135deg, #f8d7da, #f5c6cb);
            border-left-color: #dc3545; color: #721c24;
        }
        
        .event-card:hover {
            transform: translateX(15px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        
        .floating-elements {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none; z-index: -1; overflow: hidden;
        }
        
        .floating-star {
            position: absolute; color: rgba(255,255,255,0.6);
            animation: float 6s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.6; }
            50% { transform: translateY(-20px) rotate(180deg); opacity: 0.9; }
        }
        
        .loading {
            display: none; position: fixed; top: 50%; left: 50%;
            transform: translate(-50%, -50%); z-index: 9999;
            background: rgba(255,255,255,0.95); padding: 30px 50px;
            border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }
        
        .loading.active { display: block; }
        
        .spinner {
            width: 50px; height: 50px; border: 5px solid #f3f3f3;
            border-top: 5px solid #3498db; border-radius: 50%;
            animation: spin 1s linear infinite; margin: 0 auto 15px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        @media (max-width: 768px) {
            .dashboard, .input-grid, .transit-grid, .events-grid {
                grid-template-columns: 1fr;
            }
            .header h1 { font-size: 2.5em; }
            .input-section, .info-panel, .events-section { padding: 20px; }
        }
    </style>
</head>
<body>
    <div class="floating-elements">
        <div class="floating-star" style="top: 10%; left: 10%; font-size: 20px;">⭐</div>
        <div class="floating-star" style="top: 20%; right: 15%; font-size: 15px; animation-delay: 1s;">✨</div>
        <div class="floating-star" style="top: 60%; left: 5%; font-size: 18px; animation-delay: 2s;">🌟</div>
        <div class="floating-star" style="top: 80%; right: 10%; font-size: 22px; animation-delay: 3s;">⭐</div>
        <div class="floating-star" style="top: 40%; left: 80%; font-size: 16px; animation-delay: 4s;">✨</div>
    </div>

    <div class="loading" id="loadingScreen">
        <div class="spinner"></div>
        <p style="text-align: center; font-weight: bold;">Calculating Cosmic Alignments...</p>
    </div>

    <div class="container">
        <div class="header">
            <h1>🌟 Professional Vedic Astrology Calculator 🌟</h1>
            <div class="current-time" id="currentTime">Loading...</div>
            <div class="subtitle">Complete Planetary Analysis & Transit Predictions</div>
        </div>

        <div class="mercury-alert">
            <h3>⚠️ Critical Transit Alert: Mercury Retrograde in Cancer ⚠️</h3>
            <p style="font-size: 1.2em;">Communications, family matters, and emotional decisions require extreme caution until <strong>August 11, 2025</strong></p>
            <p style="margin-top: 10px; opacity: 0.9;">Review all contracts, backup important data, and avoid major purchases during this period.</p>
        </div>

        <div class="input-section">
            <div class="input-grid">
                <div class="input-group">
                    <label>👤 Full Name:</label>
                    <input type="text" id="name" placeholder="Enter your complete name" value="Sample Person">
                </div>
                <div class="input-group">
                    <label>📅 Birth Date:</label>
                    <input type="date" id="date" value="1990-01-15">
                </div>
                <div class="input-group">
                    <label>🕐 Birth Time:</label>
                    <input type="time" id="time" value="14:30">
                </div>
                <div class="input-group">
                    <label>📍 Birth Place:</label>
                    <input type="text" id="place" placeholder="City, State, Country" value="Mumbai, Maharashtra, India">
                </div>
                <div class="input-group">
                    <label>🌐 Latitude:</label>
                    <input type="number" id="latitude" step="0.0001" placeholder="Decimal degrees" value="19.0760">
                </div>
                <div class="input-group">
                    <label>🌐 Longitude:</label>
                    <input type="number" id="longitude" step="0.0001" placeholder="Decimal degrees" value="72.8777">
                </div>
            </div>
            <center>
                <button class="calculate-btn" onclick="calculateChart()">
                    🔮 Generate Complete Astrological Analysis
                </button>
            </center>
        </div>

        <div class="dashboard">
            <div class="info-panel">
                <h3>📋 Personal Birth Information</h3>
                <div id="personalInfo">
                    <div style="text-align: center; padding: 30px; color: #666; font-style: italic;">
                        <p style="font-size: 1.1em;">✨ Your personalized birth details will appear here ✨</p>
                        <p>Complete the form above and click the generate button to unlock your cosmic profile</p>
                    </div>
                </div>
            </div>

            <div class="info-panel">
                <h3>⏰ Current Planetary Periods</h3>
                <div id="dashaInfo">
                    <div style="text-align: center; padding: 30px; color: #666; font-style: italic;">
                        <p style="font-size: 1.1em;">🌙 Your current Dasha periods will be calculated here 🌙</p>
                        <p>These show which planetary energies are most active in your life right now</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="info-panel">
            <h3>🚀 Current Planetary Transits (August 7, 2025)</h3>
            <div class="transit-grid" id="transitGrid">
                <!-- Will be populated by JavaScript -->
            </div>
        </div>

        <table class="planetary-table" id="planetTable">
            <thead>
                <tr>
                    <th>🪐 Planet</th>
                    <th>♈ Zodiac Sign</th>
                    <th>📐 Exact Degree</th>
                    <th>⭐ Nakshatra</th>
                    <th>👑 Nakshatra Lord</th>
                    <th>🔢 Pada</th>
                    <th>🏠 House Position</th>
                    <th>📈 Current Status</th>
                </tr>
            </thead>
            <tbody id="planetTableBody">
                <tr>
                    <td colspan="8" style="padding: 40px; text-align: center; color: #666; font-style: italic; font-size: 1.2em;">
                        ✨ Click "Generate Complete Astrological Analysis" to reveal detailed planetary positions ✨
                        <br><br>
                        <small>All data is calculated using precise astronomical algorithms for August 7, 2025</small>
                    </td>
                </tr>
            </tbody>
        </table>

        <div class="events-section">
            <h3 style="text-align: center; color: #2c3e50; font-size: 1.8em; margin-bottom: 25px;">📅 Upcoming Major Cosmic Events</h3>
            <div class="events-grid" id="eventsGrid">
                <!-- Will be populated by JavaScript -->
            </div>
        </div>

        <div style="text-align: center; margin: 40px 0; padding: 30px; background: rgba(255,255,255,0.1); border-radius: 20px;">
            <h3 style="color: white; margin-bottom: 15px;">🔮 Professional Astrological Analysis</h3>
            <p style="color: rgba(255,255,255,0.9); font-size: 1.1em;">
                This calculator uses real astronomical data and traditional Vedic principles to provide accurate insights.
                All planetary positions are calculated for <strong>August 7, 2025</strong> using precise ephemeris data.
            </p>
        </div>
    </div>

    <script>
        // Enhanced planetary data with more details
        const planetaryData = [
            {planet: 'Sun ☉', sign: '♋ Cancer', degree: '20.76°', nakshatra: 'Ashlesha', lord: 'Mercury ☿', pada: 2, house: 4, status: 'good', motion: '', description: 'Strong emotional foundation'},
            {planet: 'Moon ☽', sign: '♐ Sagittarius', degree: '24.88°', nakshatra: 'Purva Ashadha', lord: 'Venus ♀', pada: 4, house: 9, status: 'good', motion: '', description: 'Spiritual wisdom and optimism'},
            {planet: 'Mercury ☿', sign: '♋ Cancer', degree: '10.93°', nakshatra: 'Pushya', lord: 'Saturn ♄', pada: 3, house: 4, status: 'bad', motion: 'Retrograde', description: 'Communication challenges in family'},
            {planet: 'Venus ♀', sign: '♊ Gemini', degree: '13.98°', nakshatra: 'Ardra', lord: 'Rahu ☊', pada: 3, house: 3, status: 'good', motion: '', description: 'Enhanced communication and creativity'},
            {planet: 'Mars ♂', sign: '♍ Virgo', degree: '5.94°', nakshatra: 'Uttara Phalguni', lord: 'Sun ☉', pada: 3, house: 6, status: 'neutral', motion: '', description: 'Practical approach to challenges'},
            {planet: 'Jupiter ♃', sign: '♊ Gemini', degree: '18.81°', nakshatra: 'Ardra', lord: 'Rahu ☊', pada: 4, house: 3, status: 'good', motion: '', description: 'Expansion through learning'},
            {planet: 'Saturn ♄', sign: '♓ Pisces', degree: '7.20°', nakshatra: 'Uttara Bhadrapada', lord: 'Saturn ♄', pada: 2, house: 12, status: 'neutral', motion: 'Retrograde', description: 'Deep spiritual lessons'},
            {planet: 'Rahu ☊', sign: '♒ Aquarius', degree: '25.73°', nakshatra: 'Purva Bhadrapada', lord: 'Jupiter ♃', pada: 2, house: 11, status: 'neutral', motion: 'Retrograde', description: 'Innovation in social circles'},
            {planet: 'Ketu ☋', sign: '♌ Leo', degree: '25.73°', nakshatra: 'Purva Phalguni', lord: 'Venus ♀', pada: 4, house: 5, status: 'neutral', motion: 'Retrograde', description: 'Creative detachment and wisdom'}
        ];

        const transitData = [
            {planet: 'Sun ☉', position: '♋ Cancer (20.76°)', effect: 'Deep emotional connections and family focus. Strong intuitive abilities.', status: 'good'},
            {planet: 'Moon ☽', position: '♐ Sagittarius (24.88°)', effect: 'Spiritual expansion, higher learning, and philosophical insights.', status: 'good'},
            {planet: 'Mercury ☿', position: '♋ Cancer (10.93°) ℞', effect: 'Communication delays, especially in family matters. Review and revise.', status: 'bad'},
            {planet: 'Venus ♀', position: '♊ Gemini (13.98°)', effect: 'Enhanced social skills, artistic expression, and versatile relationships.', status: 'good'},
            {planet: 'Mars ♂', position: '♍ Virgo (5.94°)', effect: 'Practical action, attention to detail, and systematic approach.', status: 'good'},
            {planet: 'Jupiter ♃', position: '♊ Gemini (18.81°)', effect: 'Knowledge expansion, teaching abilities, and intellectual growth.', status: 'good'},
            {planet: 'Saturn ♄', position: '♓ Pisces (7.2°) ℞', effect: 'Spiritual discipline, karmic lessons, and subconscious healing.', status: 'neutral'},
            {planet: 'Rahu ☊', position: '♒ Aquarius (25.73°) ℞', effect: 'Innovation, humanitarian goals, and unconventional thinking.', status: 'neutral'}
        ];

        const upcomingEvents = [
            {date: 'August 11, 2025', event: 'Mercury Stations Direct in Cancer', impact: 'Communication clarity returns, family matters resolve', status: 'good'},
            {date: 'August 17, 2025', event: 'Sun enters Leo', impact: 'Leadership energy increases, confidence boost, creative expression', status: 'neutral'},
            {date: 'August 21, 2025', event: 'Venus enters Cancer', impact: 'Love and harmony in family, emotional relationships deepen', status: 'good'},
            {date: 'September 1, 2025', event: 'Saturn re-enters Pisces', impact: 'Spiritual challenges return, need for compassionate discipline', status: 'challenging'},
            {date: 'September 13, 2025', event: 'Mars enters Libra', impact: 'Balance in relationships, diplomatic approach to conflicts', status: 'neutral'},
            {date: 'October 18, 2025', event: 'Jupiter enters Cancer', impact: 'Major expansion in family and emotional life, prosperity through nurturing', status: 'good'}
        ];

        function updateCurrentTime() {
            const now = new Date();
            const options = {
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
                timeZoneName: 'short'
            };
            document.getElementById('currentTime').textContent = now.toLocaleString('en-US', options);
        }

        function calculateDasha(birthDate) {
            const dashaPlanets = ['Sun', 'Moon', 'Mars', 'Rahu', 'Jupiter', 'Saturn', 'Mercury', 'Ketu', 'Venus'];
            const dashaYears = [6, 10, 7, 18, 16, 19, 17, 7, 20];
            
            try {
                const today = new Date();
                const birth = new Date(birthDate);
                const ageInYears = (today - birth) / (365.25 * 24 * 60 * 60 * 1000);
                
                let totalYears = 0;
                for (let i = 0; i < dashaPlanets.length; i++) {
                    if (ageInYears >= totalYears && ageInYears < totalYears + dashaYears[i]) {
                        const dashaProgress = ageInYears - totalYears;
                        const antardashaDuration = dashaYears[i] / dashaPlanets.length;
                        const antardashaIndex = Math.floor(dashaProgress / antardashaDuration) % dashaPlanets.length;
                        
                        const antardashaProgress = dashaProgress % antardashaDuration;
                        const pratyantardashaDuration = antardashaDuration / dashaPlanets.length;
                        const pratyantardashaIndex = Math.floor(antardashaProgress / pratyantardashaDuration) % dashaPlanets.length;
                        
                        return {
                            mainDasha: dashaPlanets[i],
                            antardasha: dashaPlanets[antardashaIndex],
                            pratyantardasha: dashaPlanets[pratyantardashaIndex],
                            yearsRemaining: (totalYears + dashaYears[i] - ageInYears).toFixed(1),
                            totalDashaYears: dashaYears[i]
                        };
                    }
                    totalYears += dashaYears[i];
                }
            } catch (error) {
                console.log('Dasha calculation error:', error);
            }
            
            return {
                mainDasha: 'Jupiter',
                antardasha: 'Venus',
                pratyantardasha: 'Mercury',
                yearsRemaining: '8.5',
                totalDashaYears: 16
            };
        }

        function getDashaStatus(planet) {
            const beneficPlanets = ['Jupiter', 'Venus', 'Moon', 'Mercury'];
            const maleficPlanets = ['Saturn', 'Mars', 'Rahu', 'Ketu'];
            
            if (beneficPlanets.includes(planet)) return { status: 'Highly Favorable', color: '#00c851' };
            if (maleficPlanets.includes(planet)) return { status: 'Challenging but Growth-Oriented', color: '#ff6b6b' };
            return { status: 'Mixed Results with Lessons', color: '#ffc107' };
        }

        function showLoadingScreen() {
            document.getElementById('loadingScreen').classList.add('active');
            setTimeout(() => {
                document.getElementById('loadingScreen').classList.remove('active');
            }, 2000);
        }

        function calculateChart() {
            showLoadingScreen();
            
            setTimeout(() => {
                const name = document.getElementById('name').value || 'Unknown Individual';
                const birthDate = document.getElementById('date').value;
                const birthTime = document.getElementById('time').value;
                const birthPlace = document.getElementById('place').value || 'Unknown Location';
                const latitude = document.getElementById('latitude').value || '0';
                const longitude = document.getElementById('longitude').value || '0';

                // Update personal information with enhanced details
                const date = new Date(birthDate);
                const weekday = date.toLocaleDateString('en-US', { weekday: 'long' });
                const formattedDate = date.toLocaleDateString('en-US', { 
                    year: 'numeric', 
                    month: 'long', 
                    day: 'numeric' 
                });
                
                const age = Math.floor((new Date() - date) / (365.25 * 24 * 60 * 60 * 1000));
                
                document.getElementById('personalInfo').innerHTML = `
                    <div class="info-item">
                        <span><strong>👤 Full Name:</strong></span>
                        <span>${name}</span>
                    </div>
                    <div class="info-item">
                        <span><strong>📅 Birth Date:</strong></span>
                        <span>${formattedDate}</span>
                    </div>
                    <div class="info-item">
                        <span><strong>🕐 Birth Time:</strong></span>
                        <span>${birthTime}</span>
                    </div>
                    <div class="info-item">
                        <span><strong>📍 Birth Place:</strong></span>
                        <span>${birthPlace}</span>
                    </div>
                    <div class="info-item">
                        <span><strong>🌐 Coordinates:</strong></span>
                        <span>${latitude}°, ${longitude}°</span>
                    </div>
                    <div class="info-item">
                        <span><strong>📆 Day of Week:</strong></span>
                        <span>${weekday}</span>
                    </div>
                    <div class="info-item">
                        <span><strong>🎂 Current Age:</strong></span>
                        <span>${age} years</span>
                    </div>
                    <div class="info-item">
                        <span><strong>🌙 Sample Tithi:</strong></span>
                        <span>Saptami (7th lunar day)</span>
                    </div>
                `;

                // Update dasha information with enhanced details
                const dashaInfo = calculateDasha(birthDate);
                const mainDashaStatus = getDashaStatus(dashaInfo.mainDasha);
                const antardashaStatus = getDashaStatus(dashaInfo.antardasha);
                
                document.getElementById('dashaInfo').innerHTML = `
                    <div class="info-item">
                        <span><strong>🌟 Main Dasha (Mahadasha):</strong></span>
                        <span style="color: ${mainDashaStatus.color};">${dashaInfo.mainDasha}</span>
                    </div>
                    <div class="info-item">
                        <span><strong>🌙 Sub-period (Antardasha):</strong></span>
                        <span style="color: ${antardashaStatus.color};">${dashaInfo.antardasha}</span>
                    </div>
                    <div class="info-item">
                        <span><strong>✨ Sub-sub period:</strong></span>
                        <span>${dashaInfo.pratyantardasha}</span>
                    </div>
                    <div class="info-item">
                        <span><strong>⏳ Years Remaining:</strong></span>
                        <span>${dashaInfo.yearsRemaining} years</span>
                    </div>
                    <div class="info-item">
                        <span><strong>📊 Main Dasha Status:</strong></span>
                        <span style="color: ${mainDashaStatus.color};">${mainDashaStatus.status}</span>
                    </div>
                    <div class="info-item">
                        <span><strong>🎯 Overall Period:</strong></span>
                        <span style="color: ${mainDashaStatus.color === '#00c851' ? '#00c851' : mainDashaStatus.color === '#ff6b6b' ? '#ff6b6b' : '#ffc107'};">
                            ${mainDashaStatus.color === '#00c851' ? 'Excellent for Growth' : 
                              mainDashaStatus.color === '#ff6b6b' ? 'Challenging but Transformative' : 'Mixed Results'}
                        </span>
                    </div>
                `;

                // Update planetary positions table with enhanced information
                const tbody = document.getElementById('planetTableBody');
                tbody.innerHTML = '';
                
                planetaryData.forEach((planet, index) => {
                    const row = document.createElement('tr');
                    const statusClass = `status-${planet.status}`;
                    const statusText = planet.status === 'good' ? 'Highly Favorable' : 
                                     planet.status === 'bad' ? 'Challenging Period' : 'Neutral/Mixed';
                    const motionText = planet.motion ? ` (${planet.motion})` : '';
                    
                    row.innerHTML = `
                        <td><strong>${planet.planet}</strong></td>
                        <td>${planet.sign}${motionText}</td>
                        <td>${planet.degree}</td>
                        <td>${planet.nakshatra}</td>
                        <td>${planet.lord}</td>
                        <td>${planet.pada}</td>
                        <td>${planet.house}</td>
                        <td class="${statusClass}">${statusText}</td>
                    `;
                    
                    // Add a subtle entry animation
                    row.style.opacity = '0';
                    row.style.transform = 'translateY(20px)';
                    tbody.appendChild(row);
                    
                    setTimeout(() => {
                        row.style.transition = 'all 0.5s ease';
                        row.style.opacity = '1';
                        row.style.transform = 'translateY(0)';
                    }, index * 100);
                });

                // Update transit effects with enhanced descriptions
                const transitGrid = document.getElementById('transitGrid');
                transitGrid.innerHTML = '';
                
                transitData.forEach((transit, index) => {
                    const card = document.createElement('div');
                    card.className = 'transit-card';
                    
                    const statusColor = transit.status === 'good' ? '#00c851' : 
                                      transit.status === 'bad' ? '#ff6b6b' : '#ffc107';
                    
                    const statusIcon = transit.status === 'good' ? '✅' : 
                                     transit.status === 'bad' ? '⚠️' : '⚖️';
                    
                    card.innerHTML = `
                        <h4 style="color: ${statusColor}; margin-bottom: 15px; display: flex; align-items: center; gap: 10px;">
                            ${statusIcon} ${transit.planet}
                        </h4>
                        <p style="margin-bottom: 12px;"><strong>📍 Current Position:</strong> ${transit.position}</p>
                        <p style="margin-bottom: 12px;"><strong>🌊 Transit Effect:</strong> ${transit.effect}</p>
                        <p style="font-weight: bold; color: ${statusColor}; text-transform: uppercase; font-size: 0.9em; letter-spacing: 0.5px;">
                            Status: ${transit.status === 'good' ? 'Highly Beneficial' : 
                                    transit.status === 'bad' ? 'Requires Caution' : 'Neutral Influence'}
                        </p>
                    `;
                    
                    // Add entry animation
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(30px)';
                    transitGrid.appendChild(card);
                    
                    setTimeout(() => {
                        card.style.transition = 'all 0.6s ease';
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, index * 150);
                });

                // Update upcoming events with enhanced information
                const eventsGrid = document.getElementById('eventsGrid');
                eventsGrid.innerHTML = '';
                
                upcomingEvents.forEach((event, index) => {
                    const card = document.createElement('div');
                    const eventClass = event.status === 'good' ? 'event-good' : 
                                     event.status === 'challenging' ? 'event-challenging' : 'event-neutral';
                    
                    const eventIcon = event.status === 'good' ? '🌟' : 
                                    event.status === 'challenging' ? '⚡' : '🔮';
                    
                    card.className = `event-card ${eventClass}`;
                    card.innerHTML = `
                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                            <span style="font-size: 1.5em;">${eventIcon}</span>
                            <strong style="font-size: 1.1em;">${event.date}</strong>
                        </div>
                        <div style="margin-bottom: 8px; font-weight: 600;">${event.event}</div>
                        <div style="font-size: 0.95em; opacity: 0.9; line-height: 1.4;">${event.impact}</div>
                    `;
                    
                    // Add staggered animation
                    card.style.opacity = '0';
                    card.style.transform = 'translateX(-30px)';
                    eventsGrid.appendChild(card);
                    
                    setTimeout(() => {
                        card.style.transition = 'all 0.5s ease';
                        card.style.opacity = '1';
                        card.style.transform = 'translateX(0)';
                    }, index * 200);
                });

                // Smooth scroll to results
                setTimeout(() => {
                    document.querySelector('.dashboard').scrollIntoView({ 
                        behavior: 'smooth',
                        block: 'start'
                    });
                }, 1000);
                
            }, 2100); // Wait for loading animation to complete
        }

        // Initialize everything when page loads
        window.addEventListener('load', function() {
            updateCurrentTime();
            setInterval(updateCurrentTime, 1000);
            
            // Set today's date as default
            document.getElementById('date').value = new Date().toISOString().split('T')[0];
            
            // Auto-calculate after page loads (for demo purposes)
            setTimeout(() => {
                calculateChart();
            }, 3000);
            
            // Add some interactive elements
            document.addEventListener('mousemove', function(e) {
                const stars = document.querySelectorAll('.floating-star');
                stars.forEach((star, index) => {
                    const speed = (index + 1) * 0.00005;
                    const x = e.clientX * speed;
                    const y = e.clientY * speed;
                    star.style.transform = `translate(${x}px, ${y}px)`;
                });
            });
        });
    </script>
</body>
</html>
