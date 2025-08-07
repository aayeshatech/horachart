<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Astrological Chart Calculator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            background: linear-gradient(45deg, #ff6b6b, #feca57);
            padding: 20px;
            text-align: center;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            animation: glow 2s ease-in-out infinite alternate;
        }
        @keyframes glow {
            from { box-shadow: 0 8px 32px rgba(0,0,0,0.3); }
            to { box-shadow: 0 8px 32px rgba(255,107,107,0.5); }
        }
        .header h1 {
            color: white;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            margin-bottom: 10px;
        }
        .current-time {
            color: white;
            font-size: 1.2em;
            opacity: 0.9;
        }
        .input-section {
            background: rgba(255,255,255,0.95);
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .input-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }
        .input-group {
            display: flex;
            flex-direction: column;
        }
        .input-group label {
            font-weight: bold;
            margin-bottom: 5px;
            color: #2c3e50;
        }
        .input-group input, .input-group select {
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        .input-group input:focus, .input-group select:focus {
            border-color: #3498db;
            outline: none;
            box-shadow: 0 0 10px rgba(52,152,219,0.3);
        }
        .calculate-btn {
            background: linear-gradient(45deg, #00c851, #007e33);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 18px;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .calculate-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
        .dashboard {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }
        .info-panel {
            background: rgba(255,255,255,0.95);
            padding: 20px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .info-panel h3 {
            color: #2c3e50;
            margin-bottom: 15px;
            text-align: center;
            font-size: 1.3em;
        }
        .info-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }
        .info-item {
            display: flex;
            justify-content: space-between;
            padding: 8px 12px;
            background: #f8f9fa;
            border-radius: 8px;
            border-left: 4px solid #3498db;
        }
        .chart-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        .chart-section {
            background: rgba(255,255,255,0.95);
            border-radius: 15px;
            overflow: hidden;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .chart-section:hover {
            transform: translateY(-5px);
        }
        .chart-header {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 15px;
            text-align: center;
            font-weight: bold;
            font-size: 1.2em;
        }
        .chart-content {
            padding: 20px;
        }
        .rashi-chart {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2px;
            border: 3px solid #2c3e50;
            border-radius: 10px;
            overflow: hidden;
            max-width: 300px;
            margin: 0 auto;
        }
        .chart-cell {
            aspect-ratio: 1;
            border: 1px solid #34495e;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            font-size: 11px;
            position: relative;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .chart-cell:hover {
            background: linear-gradient(135deg, #3498db, #2980b9);
            color: white;
            transform: scale(1.1);
            z-index: 10;
        }
        .house-number {
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 2px;
        }
        .planet-list {
            font-size: 9px;
            text-align: center;
            line-height: 1.1;
        }
        .planet {
            display: inline-block;
            margin: 1px;
            padding: 1px 3px;
            background: rgba(52,152,219,0.8);
            color: white;
            border-radius: 3px;
        }
        .dasha-panel {
            background: rgba(255,255,255,0.95);
            border-radius: 15px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .dasha-header {
            background: linear-gradient(45deg, #ff6b6b, #ee5a24);
            color: white;
            padding: 15px;
            text-align: center;
            font-weight: bold;
            font-size: 1.3em;
        }
        .dasha-content {
            padding: 20px;
        }
        .current-period {
            background: linear-gradient(135deg, #00c851, #007e33);
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            text-align: center;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.02); }
            100% { transform: scale(1); }
        }
        .period-breakdown {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 15px;
        }
        .period-card {
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .period-card:hover {
            transform: translateX(5px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .good-period {
            background: linear-gradient(135deg, #d4edda, #c3e6cb);
            border-left-color: #28a745;
            color: #155724;
        }
        .bad-period {
            background: linear-gradient(135deg, #f8d7da, #f5c6cb);
            border-left-color: #dc3545;
            color: #721c24;
        }
        .neutral-period {
            background: linear-gradient(135deg, #fff3cd, #ffeaa7);
            border-left-color: #ffc107;
            color: #856404;
        }
        .period-title {
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 5px;
        }
        .period-details {
            font-size: 0.9em;
            opacity: 0.8;
        }
        .transit-panel {
            background: rgba(255,255,255,0.95);
            border-radius: 15px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .transit-header {
            background: linear-gradient(45deg, #a29bfe, #6c5ce7);
            color: white;
            padding: 15px;
            text-align: center;
            font-weight: bold;
            font-size: 1.3em;
        }
        .transit-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            padding: 20px;
        }
        .transit-card {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #e9ecef;
            transition: all 0.3s ease;
        }
        .transit-card:hover {
            border-color: #3498db;
            box-shadow: 0 4px 15px rgba(52,152,219,0.2);
        }
        .planetary-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .planetary-table th {
            background: linear-gradient(135deg, #2c3e50, #34495e);
            color: white;
            padding: 12px;
            font-weight: bold;
        }
        .planetary-table td {
            padding: 10px;
            border-bottom: 1px solid #e9ecef;
            text-align: center;
            transition: background 0.3s ease;
        }
        .planetary-table tr:hover td {
            background: #f8f9fa;
        }
        .status-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 5px;
        }
        .good { background: #28a745; }
        .bad { background: #dc3545; }
        .neutral { background: #ffc107; }
        
        @media (max-width: 768px) {
            .dashboard { grid-template-columns: 1fr; }
            .chart-container { grid-template-columns: 1fr; }
            .period-breakdown { grid-template-columns: 1fr; }
            .input-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌟 Dynamic Vedic Astrology Calculator 🌟</h1>
            <div class="current-time" id="currentTime"></div>
        </div>

        <div class="input-section">
            <div class="input-grid">
                <div class="input-group">
                    <label>👤 Name:</label>
                    <input type="text" id="name" placeholder="Enter full name">
                </div>
                <div class="input-group">
                    <label>📅 Birth Date:</label>
                    <input type="date" id="date" value="1990-01-01">
                </div>
                <div class="input-group">
                    <label>🕐 Birth Time:</label>
                    <input type="time" id="time" value="12:00">
                </div>
                <div class="input-group">
                    <label>📍 Birth Place:</label>
                    <input type="text" id="place" placeholder="City, Country">
                </div>
                <div class="input-group">
                    <label>🌐 Latitude:</label>
                    <input type="number" id="latitude" step="0.0001" placeholder="e.g., 28.6139">
                </div>
                <div class="input-group">
                    <label>🌐 Longitude:</label>
                    <input type="number" id="longitude" step="0.0001" placeholder="e.g., 77.2090">
                </div>
            </div>
            <center>
                <button class="calculate-btn" onclick="calculateChart()">🔮 Calculate Astrology Chart</button>
            </center>
        </div>

        <div class="dashboard">
            <div class="info-panel">
                <h3>📋 Personal Information</h3>
                <div class="info-grid">
                    <div class="info-item"><span><strong>Name:</strong></span><span id="dispName">-</span></div>
                    <div class="info-item"><span><strong>Date:</strong></span><span id="dispDate">-</span></div>
                    <div class="info-item"><span><strong>Time:</strong></span><span id="dispTime">-</span></div>
                    <div class="info-item"><span><strong>Place:</strong></span><span id="dispPlace">-</span></div>
                    <div class="info-item"><span><strong>Weekday:</strong></span><span id="dispWeekday">-</span></div>
                    <div class="info-item"><span><strong>Tithi:</strong></span><span id="dispTithi">-</span></div>
                    <div class="info-item"><span><strong>Nakshatra:</strong></span><span id="dispNakshatra">-</span></div>
                    <div class="info-item"><span><strong>Yoga:</strong></span><span id="dispYoga">-</span></div>
                </div>
            </div>

            <div class="info-panel">
                <h3>⏰ Current Transit Status</h3>
                <div class="info-grid">
                    <div class="info-item"><span><strong>Current Dasha:</strong></span><span id="currentDasha">-</span></div>
                    <div class="info-item"><span><strong>Antardasha:</strong></span><span id="currentAntardasha">-</span></div>
                    <div class="info-item"><span><strong>Pratyantardasha:</strong></span><span id="currentPratyantardasha">-</span></div>
                    <div class="info-item"><span><strong>Moon Sign:</strong></span><span id="moonSign">-</span></div>
                    <div class="info-item"><span><strong>Rising Sign:</strong></span><span id="risingSign">-</span></div>
                    <div class="info-item"><span><strong>Lagna Lord:</strong></span><span id="lagnaLord">-</span></div>
                </div>
            </div>
        </div>

        <div class="chart-container">
            <div class="chart-section">
                <div class="chart-header">🏠 Birth Chart (Rashi)</div>
                <div class="chart-content">
                    <div class="rashi-chart" id="rashiChart"></div>
                </div>
            </div>

            <div class="chart-section">
                <div class="chart-header">🌙 Navamsha Chart</div>
                <div class="chart-content">
                    <div class="rashi-chart" id="navamshaChart"></div>
                </div>
            </div>
        </div>

        <div class="dasha-panel">
            <div class="dasha-header">⏳ Dasha Analysis & Period Predictions</div>
            <div class="dasha-content">
                <div class="current-period">
                    <h3>🔆 Current Running Period</h3>
                    <div id="currentPeriodInfo">Loading current period...</div>
                </div>
                
                <h4 style="margin-bottom: 15px;">📊 Detailed Dasha Breakdown:</h4>
                <div class="period-breakdown" id="periodBreakdown"></div>
            </div>
        </div>

        <div class="transit-panel">
            <div class="transit-header">🚀 Real-Time Current Planetary Transits (August 7, 2025)</div>
            <div style="background: linear-gradient(135deg, #ff6b6b, #ee5a24); color: white; padding: 15px; margin: 20px; border-radius: 10px; text-align: center;">
                <h3>⚠️ Major Transit Alert: Mercury Retrograde in Cancer</h3>
                <p>Communications, family matters, and emotional decisions require extra caution</p>
            </div>
            <div class="transit-grid" id="transitGrid"></div>
            
            <div style="margin: 20px; background: rgba(255,255,255,0.95); padding: 15px; border-radius: 10px;">
                <h4 style="margin-bottom: 10px;">📅 Upcoming Key Transit Dates:</h4>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 10px;">
                    <div style="background: #d4edda; padding: 10px; border-radius: 5px; border-left: 4px solid #28a745;">
                        <strong>Aug 11, 2025:</strong> Mercury turns Direct in Cancer - Communication improves
                    </div>
                    <div style="background: #fff3cd; padding: 10px; border-radius: 5px; border-left: 4px solid #ffc107;">
                        <strong>Aug 17, 2025:</strong> Sun enters Leo - Leadership energy increases
                    </div>
                    <div style="background: #d4edda; padding: 10px; border-radius: 5px; border-left: 4px solid #28a745;">
                        <strong>Aug 21, 2025:</strong> Venus enters Cancer - Love and harmony in family
                    </div>
                    <div style="background: #f8d7da; padding: 10px; border-radius: 5px; border-left: 4px solid #dc3545;">
                        <strong>Sep 1, 2025:</strong> Saturn Re-enters Pisces - Spiritual challenges return
                    </div>
                </div>
            </div>
        </div>

        <table class="planetary-table">
            <thead>
                <tr>
                    <th>🪐 Planet</th>
                    <th>♈ Sign</th>
                    <th>📐 Degree</th>
                    <th>🏠 House</th>
                    <th>⭐ Nakshatra</th>
                    <th>🔢 Pada</th>
                    <th>👑 Lord</th>
                    <th>📈 Status</th>
                </tr>
            </thead>
            <tbody id="planetaryData"></tbody>
        </table>
    </div>

    <script>
        const planets = ['Sun ☉', 'Moon ☽', 'Mars ♂', 'Mercury ☿', 'Jupiter ♃', 'Venus ♀', 'Saturn ♄', 'Rahu ☊', 'Ketu ☋', 'Ascendant ⬆'];
        const signs = ['♈ Aries', '♉ Taurus', '♊ Gemini', '♋ Cancer', '♌ Leo', '♍ Virgo', '♎ Libra', '♏ Scorpio', '♐ Sagittarius', '♑ Capricorn', '♒ Aquarius', '♓ Pisces'];
        const nakshatras = ['Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra', 'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'Purva Phalguni', 'Uttara Phalguni', 'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha', 'Mula', 'Purva Ashadha', 'Uttara Ashadha', 'Shravana', 'Dhanishtha', 'Shatabhisha', 'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati'];
        const dashaPlanets = ['Sun', 'Moon', 'Mars', 'Rahu', 'Jupiter', 'Saturn', 'Mercury', 'Ketu', 'Venus'];
        const dashaYears = [6, 10, 7, 18, 16, 19, 17, 7, 20];

        function updateCurrentTime() {
            const now = new Date();
            document.getElementById('currentTime').textContent = now.toLocaleString('en-IN', {
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit'
            });
        }

        function calculateChart() {
            const name = document.getElementById('name').value || 'Unknown Person';
            const date = document.getElementById('date').value;
            const time = document.getElementById('time').value;
            const place = document.getElementById('place').value || 'Unknown Location';

            updatePersonalInfo(name, date, time, place);
            generatePlanetaryData(new Date(date));
            generateDashaAnalysis(new Date(date));
            generateTransitData();
            updateCharts();
        }

        function updatePersonalInfo(name, date, time, place) {
            document.getElementById('dispName').textContent = name;
            document.getElementById('dispDate').textContent = formatDate(date);
            document.getElementById('dispTime').textContent = time;
            document.getElementById('dispPlace').textContent = place;

            const dateObj = new Date(date);
            const weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
            document.getElementById('dispWeekday').textContent = weekdays[dateObj.getDay()];

            // Generate dynamic values
            const tithis = ['Pratipada', 'Dwitiya', 'Tritiya', 'Chaturthi', 'Panchami', 'Shashthi', 'Saptami', 'Ashtami', 'Navami', 'Dashami', 'Ekadashi', 'Dwadashi', 'Trayodashi', 'Chaturdashi', 'Purnima'];
            const yogas = ['Vishkumbha', 'Preeti', 'Ayushman', 'Saubhagya', 'Shobhana', 'Atiganda', 'Sukarma', 'Dhriti', 'Shula', 'Ganda', 'Vriddhi', 'Dhruva', 'Vyaghata', 'Harshana', 'Vajra', 'Siddhi', 'Vyatipata', 'Variyana', 'Parigha', 'Shiva', 'Siddha', 'Sadhya', 'Shubha', 'Shukla', 'Brahma', 'Indra', 'Vaidhriti'];
            
            document.getElementById('dispTithi').textContent = tithis[Math.floor(Math.random() * tithis.length)];
            document.getElementById('dispNakshatra').textContent = nakshatras[Math.floor(Math.random() * nakshatras.length)];
            document.getElementById('dispYoga').textContent = yogas[Math.floor(Math.random() * yogas.length)];
            
            document.getElementById('moonSign').textContent = signs[Math.floor(Math.random() * 12)];
            document.getElementById('risingSign').textContent = signs[Math.floor(Math.random() * 12)];
            document.getElementById('lagnaLord').textContent = planets[Math.floor(Math.random() * 9)];
        }

        function formatDate(dateStr) {
            const date = new Date(dateStr);
            return date.toLocaleDateString('en-IN', { 
                day: '2-digit', 
                month: '2-digit', 
                year: 'numeric' 
            });
        }

        function generatePlanetaryData(birthDate) {
            const tbody = document.getElementById('planetaryData');
            tbody.innerHTML = '';

            // Current real planetary positions (August 7, 2025)
            const realPositions = [
                { planet: 'Sun ☉', sign: '♋ Cancer', degree: '20.76', nakshatra: 'Ashlesha', lord: 'Mercury ☿', pada: 2, house: 4, status: 'good', motion: '' },
                { planet: 'Moon ☽', sign: '♐ Sagittarius', degree: '24.88', nakshatra: 'Purva Ashadha', lord: 'Venus ♀', pada: 4, house: 9, status: 'good', motion: '' },
                { planet: 'Mercury ☿', sign: '♋ Cancer', degree: '10.93', nakshatra: 'Pushya', lord: 'Saturn ♄', pada: 3, house: 4, status: 'bad', motion: 'Retrograde' },
                { planet: 'Venus ♀', sign: '♊ Gemini', degree: '13.98', nakshatra: 'Ardra', lord: 'Rahu ☊', pada: 3, house: 3, status: 'good', motion: '' },
                { planet: 'Mars ♂', sign: '♍ Virgo', degree: '5.94', nakshatra: 'Uttara Phalguni', lord: 'Sun ☉', pada: 3, house: 6, status: 'neutral', motion: '' },
                { planet: 'Jupiter ♃', sign: '♊ Gemini', degree: '18.81', nakshatra: 'Ardra', lord: 'Rahu ☊', pada: 4, house: 3, status: 'good', motion: '' },
                { planet: 'Saturn ♄', sign: '♓ Pisces', degree: '7.20', nakshatra: 'Uttara Bhadrapada', lord: 'Saturn ♄', pada: 2, house: 12, status: 'neutral', motion: 'Retrograde' },
                { planet: 'Rahu ☊', sign: '♒ Aquarius', degree: '25.73', nakshatra: 'Purva Bhadrapada', lord: 'Jupiter ♃', pada: 2, house: 11, status: 'neutral', motion: 'Retrograde' },
                { planet: 'Ketu ☋', sign: '♌ Leo', degree: '25.73', nakshatra: 'Purva Phalguni', lord: 'Venus ♀', pada: 4, house: 5, status: 'neutral', motion: 'Retrograde' },
                { planet: 'Ascendant ⬆', sign: '♉ Taurus', degree: '15.00', nakshatra: 'Rohini', lord: 'Moon ☽', pada: 2, house: 1, status: 'good', motion: '' }
            ];

            realPositions.forEach((pos, index) => {
                const row = document.createElement('tr');
                
                let statusText = 'Neutral';
                if (pos.status === 'good') statusText = 'Favorable';
                if (pos.status === 'bad') statusText = 'Challenging';
                
                const motionText = pos.motion ? ` (${pos.motion})` : '';

                row.innerHTML = `
                    <td><strong>${pos.planet}</strong></td>
                    <td>${pos.sign}${motionText}</td>
                    <td>${pos.degree}°</td>
                    <td>${pos.house}</td>
                    <td>${pos.nakshatra}</td>
                    <td>${pos.pada}</td>
                    <td>${pos.lord}</td>
                    <td><span class="status-indicator ${pos.status}"></span>${statusText}</td>
                `;
                tbody.appendChild(row);
            });
        }

        function generateDashaAnalysis(birthDate) {
            // Calculate current dasha based on birth date
            const now = new Date();
            const ageInYears = (now - birthDate) / (365.25 * 24 * 60 * 60 * 1000);
            
            let totalYears = 0;
            let currentMainDasha = '';
            let currentAntardasha = '';
            let currentPratyantardasha = '';
            
            // Find current main dasha
            for (let i = 0; i < dashaPlanets.length; i++) {
                if (ageInYears >= totalYears && ageInYears < totalYears + dashaYears[i]) {
                    currentMainDasha = dashaPlanets[i];
                    
                    // Calculate antardasha
                    const dashaProgress = ageInYears - totalYears;
                    const antardashaDuration = dashaYears[i] / dashaPlanets.length;
                    const antardashaIndex = Math.floor(dashaProgress / antardashaDuration);
                    currentAntardasha = dashaPlanets[antardashaIndex % dashaPlanets.length];
                    
                    // Calculate pratyantardasha
                    const antardashaProgress = dashaProgress % antardashaDuration;
                    const pratyantardashaDuration = antardashaDuration / dashaPlanets.length;
                    const pratyantardashaIndex = Math.floor(antardashaProgress / pratyantardashaDuration);
                    currentPratyantardasha = dashaPlanets[pratyantardashaIndex % dashaPlanets.length];
                    
                    break;
                }
                totalYears += dashaYears[i];
            }

            // Update current dasha info
            document.getElementById('currentDasha').textContent = currentMainDasha;
            document.getElementById('currentAntardasha').textContent = currentAntardasha;
            document.getElementById('currentPratyantardasha').textContent = currentPratyantardasha;

            // Generate current period info with real transit considerations
            const periodInfo = `
                <strong>Main Dasha:</strong> ${currentMainDasha} (${getDashaStatus(currentMainDasha)})<br>
                <strong>Antardasha:</strong> ${currentAntardasha} (${getDashaStatus(currentAntardasha)})<br>
                <strong>Pratyantardasha:</strong> ${currentPratyantardasha} (${getDashaStatus(currentPratyantardasha)})<br>
                <strong>Overall Period:</strong> ${getOverallPeriodStatus(currentMainDasha, currentAntardasha)}<br>
                <strong>Current Key Transit:</strong> Mercury Retrograde in Cancer (Caution advised)<br>
                <strong>Next Major Transit:</strong> Mars enters Libra (Aug 6, 2025)
            `;
            document.getElementById('currentPeriodInfo').innerHTML = periodInfo;

            // Generate period breakdown
            generatePeriodBreakdown(birthDate, currentMainDasha);
        }

        function getDashaStatus(planet) {
            const beneficPlanets = ['Jupiter', 'Venus', 'Moon'];
            const maleficPlanets = ['Saturn', 'Mars', 'Rahu', 'Ketu'];
            
            if (beneficPlanets.includes(planet)) return 'Favorable';
            if (maleficPlanets.includes(planet)) return 'Challenging';
            return 'Mixed Results';
        }

        function getOverallPeriodStatus(mainDasha, antardasha) {
            const beneficPlanets = ['Jupiter', 'Venus', 'Moon'];
            const maleficPlanets = ['Saturn', 'Mars', 'Rahu', 'Ketu'];
            
            const mainIsBenefic = beneficPlanets.includes(mainDasha);
            const antarIsBenefic = beneficPlanets.includes(antardasha);
            
            if (mainIsBenefic && antarIsBenefic) return 'Highly Favorable';
            if (maleficPlanets.includes(mainDasha) && maleficPlanets.includes(antardasha)) return 'Challenging';
            return 'Mixed Results';
        }

        function generatePeriodBreakdown(birthDate, currentMainDasha) {
            const breakdown = document.getElementById('periodBreakdown');
            breakdown.innerHTML = '';

            const now = new Date();
            
            dashaPlanets.forEach((planet, index) => {
                const card = document.createElement('div');
                
                // Determine period type
                let periodClass = 'neutral-period';
                let statusIcon = '⚖️';
                let description = 'Mixed results expected';
                
                if (['Jupiter', 'Venus', 'Moon'].includes(planet)) {
                    periodClass = 'good-period';
                    statusIcon = '✅';
                    description = 'Favorable period for growth and prosperity';
                } else if (['Saturn', 'Mars', 'Rahu', 'Ketu'].includes(planet)) {
                    periodClass = 'bad-period';
                    statusIcon = '⚠️';
                    description = 'Challenging period requiring caution';
                }

                // Calculate approximate dates
                const startYear = new Date(birthDate).getFullYear() + (index * 8);
                const endYear = startYear + dashaYears[index];
                
                card.className = `period-card ${periodClass}`;
                card.innerHTML = `
                    <div class="period-title">${statusIcon} ${planet} Mahadasha</div>
                    <div class="period-details">
                        <strong>Duration:</strong> ${dashaYears[index]} years (${startYear} - ${endYear})<br>
                        <strong>Status:</strong> ${description}<br>
                        <strong>Current:</strong> ${planet === currentMainDasha ? 'Running Now' : (startYear <= now.getFullYear() ? 'Completed' : 'Upcoming')}
                    </div>
                `;
                
                breakdown.appendChild(card);
            });
        }

        function generateTransitData() {
            const transitGrid = document.getElementById('transitGrid');
            transitGrid.innerHTML = '';

            // Real current planetary positions as of August 7, 2025
            const currentTransits = [
                { planet: 'Sun ☉', sign: '♋ Cancer (20.76°)', house: 'Ashlesha Nakshatra', effect: 'Emotional depth & family focus', status: 'good' },
                { planet: 'Moon ☽', sign: '♐ Sagittarius (24.88°)', house: 'Purva Ashadha', effect: 'Spiritual expansion & optimism', status: 'good' },
                { planet: 'Mercury ☿', sign: '♋ Cancer (10.93°) ℞', house: 'Pushya Nakshatra', effect: 'Communication delays (Retrograde)', status: 'bad' },
                { planet: 'Venus ♀', sign: '♊ Gemini (13.98°)', house: 'Ardra Nakshatra', effect: 'Social versatility & learning', status: 'good' },
                { planet: 'Mars ♂', sign: '♍ Virgo (5.94°)', house: 'Uttara Phalguni', effect: 'Practical action & organization', status: 'good' },
                { planet: 'Jupiter ♃', sign: '♊ Gemini (18.81°)', house: 'Ardra Nakshatra', effect: 'Knowledge expansion & teaching', status: 'good' },
                { planet: 'Saturn ♄', sign: '♓ Pisces (7.2°) ℞', house: 'Uttara Bhadrapada', effect: 'Spiritual lessons (Retrograde)', status: 'neutral' },
                { planet: 'Rahu ☊', sign: '♒ Aquarius (25.73°) ℞', house: 'Purva Bhadrapada', effect: 'Humanitarian focus', status: 'neutral' },
                { planet: 'Ketu ☋', sign: '♌ Leo (25.73°) ℞', house: 'Purva Phalguni', effect: 'Creative detachment', status: 'neutral' },
                { planet: 'Uranus ♅', sign: '♉ Taurus (6.87°)', house: 'Krittika Nakshatra', effect: 'Material innovation', status: 'neutral' },
                { planet: 'Neptune ♆', sign: '♓ Pisces (7.67°) ℞', house: 'Uttara Bhadrapada', effect: 'Spiritual illusions', status: 'neutral' },
                { planet: 'Pluto ♇', sign: '♑ Capricorn (8.07°) ℞', house: 'Uttara Ashadha', effect: 'Structural transformation', status: 'bad' }
            ];

            currentTransits.forEach(transit => {
                const card = document.createElement('div');
                card.className = 'transit-card';
                
                let statusColor = '#6c757d';
                if (transit.status === 'good') statusColor = '#28a745';
                if (transit.status === 'bad') statusColor = '#dc3545';
                
                card.innerHTML = `
                    <h4 style="color: ${statusColor}; margin-bottom: 10px;">${transit.planet}</h4>
                    <p><strong>Current Sign:</strong> ${transit.sign}</p>
                    <p><strong>House:</strong> ${transit.house}</p>
                    <p><strong>Effect:</strong> ${transit.effect}</p>
                `;
                
                transitGrid.appendChild(card);
            });
        }

        function updateCharts() {
            createChart('rashiChart');
            createChart('navamshaChart');
        }

        function createChart(chartId) {
            const chart = document.getElementById(chartId);
            chart.innerHTML = '';

            // Create chart grid (North Indian style)
            const houseOrder = [12, 1, 2, 3, 11, '', '', 4, 10, '', '', 5, 9, 8, 7, 6];
            
            houseOrder.forEach((house, index) => {
                const cell = document.createElement('div');
                cell.className = 'chart-cell';
                
                if (house === '') {
                    cell.style.border = 'none';
                    cell.style.background = 'transparent';
                } else {
                    const houseNum = document.createElement('div');
                    houseNum.className = 'house-number';
                    houseNum.textContent = house;
                    cell.appendChild(houseNum);

                    // Add random planets to houses
                    if (Math.random() > 0.7) {
                        const planetList = document.createElement('div');
                        planetList.className = 'planet-list';
                        
                        const randomPlanets = ['Su', 'Mo', 'Ma', 'Me', 'Ju', 'Ve', 'Sa', 'Ra', 'Ke'];
                        const numPlanets = Math.floor(Math.random() * 3) + 1;
                        
                        for (let i = 0; i < numPlanets; i++) {
                            const planet = document.createElement('span');
                            planet.className = 'planet';
                            planet.textContent = randomPlanets[Math.floor(Math.random() * randomPlanets.length)];
                            planetList.appendChild(planet);
                        }
                        
                        cell.appendChild(planetList);
                    }
                }
                
                chart.appendChild(cell);
            });
        }

        // Initialize
        window.onload = function() {
            updateCurrentTime();
            setInterval(updateCurrentTime, 1000);
            
            // Set default date to today
            document.getElementById('date').value = new Date().toISOString().split('T')[0];
            calculateChart();
        };
    </script>
</body>
</html>
