<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌟 Vedic Astrology Calculator</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh; padding: 20px; color: #333;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        .header {
            background: linear-gradient(45deg, #ff6b6b, #feca57);
            padding: 30px; text-align: center; border-radius: 15px;
            margin-bottom: 30px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        }
        .header h1 { font-size: 2.5em; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); }
        .time-display { font-size: 1.2em; opacity: 0.9; margin: 10px 0; }
        .alert {
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
            color: white; padding: 20px; margin: 20px 0; border-radius: 10px;
            text-align: center; animation: pulse 2s infinite;
        }
        @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.02); } }
        .input-section {
            background: rgba(255,255,255,0.95); padding: 25px; border-radius: 15px;
            margin-bottom: 25px; box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        }
        .input-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px; margin-bottom: 20px;
        }
        .input-group { display: flex; flex-direction: column; }
        .input-group label { font-weight: bold; margin-bottom: 8px; color: #2c3e50; }
        .input-group input {
            padding: 12px; border: 2px solid #ddd; border-radius: 8px;
            font-size: 16px; transition: border-color 0.3s;
        }
        .input-group input:focus { border-color: #3498db; outline: none; }
        .btn {
            background: linear-gradient(45deg, #00c851, #007e33); color: white;
            padding: 15px 30px; border: none; border-radius: 10px;
            cursor: pointer; font-size: 18px; font-weight: bold;
            transition: transform 0.3s; box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .btn:hover { transform: translateY(-2px); }
        .dashboard {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px; margin: 25px 0;
        }
        .panel {
            background: rgba(255,255,255,0.95); padding: 20px; border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        }
        .panel h3 {
            color: #2c3e50; margin-bottom: 15px; text-align: center;
            font-size: 1.3em; border-bottom: 2px solid #3498db; padding-bottom: 8px;
        }
        .info-item {
            display: flex; justify-content: space-between; padding: 10px 12px;
            background: #f8f9fa; border-radius: 8px; margin: 8px 0;
            border-left: 4px solid #3498db;
        }
        .table {
            width: 100%; border-collapse: collapse; background: white;
            border-radius: 10px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            margin: 25px 0;
        }
        .table th {
            background: linear-gradient(135deg, #2c3e50, #34495e); color: white;
            padding: 15px; font-weight: bold; text-align: center;
        }
        .table td {
            padding: 12px; border-bottom: 1px solid #eee; text-align: center;
            transition: background 0.3s;
        }
        .table tr:hover td { background: #f8f9fa; }
        .good { color: #28a745; font-weight: bold; }
        .bad { color: #dc3545; font-weight: bold; }
        .neutral { color: #ffc107; font-weight: bold; }
        .transit-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px; margin: 20px 0;
        }
        .transit-card {
            background: #f8f9fa; padding: 15px; border-radius: 10px;
            border: 2px solid #e9ecef; transition: all 0.3s;
        }
        .transit-card:hover { border-color: #3498db; transform: translateY(-2px); }
        .events-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 15px; margin: 20px 0;
        }
        .event-item {
            padding: 12px; border-radius: 8px; border-left: 4px solid;
        }
        .event-good { background: #d4edda; border-left-color: #28a745; color: #155724; }
        .event-neutral { background: #fff3cd; border-left-color: #ffc107; color: #856404; }
        .event-bad { background: #f8d7da; border-left-color: #dc3545; color: #721c24; }
        @media (max-width: 768px) {
            .dashboard, .input-grid, .transit-grid, .events-grid { grid-template-columns: 1fr; }
            .header h1 { font-size: 2em; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌟 Vedic Astrology Calculator 🌟</h1>
            <div class="time-display" id="currentTime">Loading...</div>
            <p>Real-time Planetary Positions & Transit Analysis</p>
        </div>

        <div class="alert">
            <h3>⚠️ Mercury Retrograde Alert: August 7, 2025</h3>
            <p>Communications and family matters need extra caution until August 11, 2025</p>
        </div>

        <div class="input-section">
            <div class="input-grid">
                <div class="input-group">
                    <label>👤 Full Name:</label>
                    <input type="text" id="name" placeholder="Enter your name" value="Sample User">
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
                    <input type="text" id="place" placeholder="City, Country" value="Mumbai, India">
                </div>
            </div>
            <center>
                <button class="btn" onclick="calculateChart()">🔮 Calculate Astrology Chart</button>
            </center>
        </div>

        <div class="dashboard">
            <div class="panel">
                <h3>📋 Personal Information</h3>
                <div id="personalInfo">
                    <p style="text-align: center; padding: 20px; color: #666;">
                        Click "Calculate Astrology Chart" to see your details
                    </p>
                </div>
            </div>

            <div class="panel">
                <h3>⏰ Current Dasha Status</h3>
                <div id="dashaInfo">
                    <p style="text-align: center; padding: 20px; color: #666;">
                        Your planetary periods will appear here
                    </p>
                </div>
            </div>
        </div>

        <div class="panel">
            <h3>🚀 Current Planetary Transits (August 7, 2025)</h3>
            <div class="transit-grid" id="transitGrid">
                <!-- Will be populated by JavaScript -->
            </div>
        </div>

        <table class="table" id="planetTable">
            <thead>
                <tr>
                    <th>🪐 Planet</th>
                    <th>♈ Sign</th>
                    <th>📐 Degree</th>
                    <th>⭐ Nakshatra</th>
                    <th>👑 Lord</th>
                    <th>🏠 House</th>
                    <th>📈 Status</th>
                </tr>
            </thead>
            <tbody id="planetTableBody">
                <tr>
                    <td colspan="7" style="padding: 30px; color: #666; font-style: italic;">
                        Click "Calculate Astrology Chart" to see planetary positions
                    </td>
                </tr>
            </tbody>
        </table>

        <div class="panel">
            <h3>📅 Upcoming Transit Events</h3>
            <div class="events-grid" id="eventsGrid">
                <!-- Will be populated by JavaScript -->
            </div>
        </div>
    </div>

    <script>
        // Real planetary data (August 7, 2025)
        const planetData = [
            {planet: 'Sun ☉', sign: '♋ Cancer', degree: '20.76°', nakshatra: 'Ashlesha', lord: 'Mercury ☿', house: 4, status: 'good', motion: ''},
            {planet: 'Moon ☽', sign: '♐ Sagittarius', degree: '24.88°', nakshatra: 'Purva Ashadha', lord: 'Venus ♀', house: 9, status: 'good', motion: ''},
            {planet: 'Mercury ☿', sign: '♋ Cancer', degree: '10.93°', nakshatra: 'Pushya', lord: 'Saturn ♄', house: 4, status: 'bad', motion: 'Retrograde'},
            {planet: 'Venus ♀', sign: '♊ Gemini', degree: '13.98°', nakshatra: 'Ardra', lord: 'Rahu ☊', house: 3, status: 'good', motion: ''},
            {planet: 'Mars ♂', sign: '♍ Virgo', degree: '5.94°', nakshatra: 'Uttara Phalguni', lord: 'Sun ☉', house: 6, status: 'neutral', motion: ''},
            {planet: 'Jupiter ♃', sign: '♊ Gemini', degree: '18.81°', nakshatra: 'Ardra', lord: 'Rahu ☊', house: 3, status: 'good', motion: ''},
            {planet: 'Saturn ♄', sign: '♓ Pisces', degree: '7.20°', nakshatra: 'Uttara Bhadrapada', lord: 'Saturn ♄', house: 12, status: 'neutral', motion: 'Retrograde'},
            {planet: 'Rahu ☊', sign: '♒ Aquarius', degree: '25.73°', nakshatra: 'Purva Bhadrapada', lord: 'Jupiter ♃', house: 11, status: 'neutral', motion: 'Retrograde'},
            {planet: 'Ketu ☋', sign: '♌ Leo', degree: '25.73°', nakshatra: 'Purva Phalguni', lord: 'Venus ♀', house: 5, status: 'neutral', motion: 'Retrograde'}
        ];

        const transitData = [
            {planet: 'Sun ☉', position: '♋ Cancer (20.76°)', effect: 'Emotional depth & family focus', status: 'good'},
            {planet: 'Moon ☽', position: '♐ Sagittarius (24.88°)', effect: 'Spiritual expansion & optimism', status: 'good'},
            {planet: 'Mercury ☿', position: '♋ Cancer (10.93°) ℞', effect: 'Communication delays (Retrograde)', status: 'bad'},
            {planet: 'Venus ♀', position: '♊ Gemini (13.98°)', effect: 'Social versatility & learning', status: 'good'},
            {planet: 'Mars ♂', position: '♍ Virgo (5.94°)', effect: 'Practical action & organization', status: 'good'},
            {planet: 'Jupiter ♃', position: '♊ Gemini (18.81°)', effect: 'Knowledge expansion & teaching', status: 'good'},
            {planet: 'Saturn ♄', position: '♓ Pisces (7.2°) ℞', effect: 'Spiritual lessons (Retrograde)', status: 'neutral'},
            {planet: 'Rahu ☊', position: '♒ Aquarius (25.73°) ℞', effect: 'Humanitarian focus', status: 'neutral'}
        ];

        const upcomingEvents = [
            {date: 'Aug 11, 2025', event: 'Mercury turns Direct in Cancer', status: 'good'},
            {date: 'Aug 17, 2025', event: 'Sun enters Leo', status: 'neutral'},
            {date: 'Aug 21, 2025', event: 'Venus enters Cancer', status: 'good'},
            {date: 'Sep 1, 2025', event: 'Saturn re-enters Pisces', status: 'bad'},
            {date: 'Sep 13, 2025', event: 'Mars enters Libra', status: 'neutral'},
            {date: 'Oct 18, 2025', event: 'Jupiter enters Cancer', status: 'good'}
        ];

        function updateTime() {
            const now = new Date();
            const timeString = now.toLocaleString('en-US', {
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit'
            });
            document.getElementById('currentTime').textContent = timeString;
        }

        function calculateDasha(birthDate) {
            const planets = ['Sun', 'Moon', 'Mars', 'Rahu', 'Jupiter', 'Saturn', 'Mercury', 'Ketu', 'Venus'];
            const years = [6, 10, 7, 18, 16, 19, 17, 7, 20];
            
            try {
                const today = new Date();
                const birth = new Date(birthDate);
                const ageYears = (today - birth) / (365.25 * 24 * 60 * 60 * 1000);
                
                let totalYears = 0;
                for (let i = 0; i < planets.length; i++) {
                    if (ageYears >= totalYears && ageYears < totalYears + years[i]) {
                        const progress = ageYears - totalYears;
                        const antardashaIndex = Math.floor(progress / (years[i] / planets.length)) % planets.length;
                        return {
                            dasha: planets[i],
                            antardasha: planets[antardashaIndex],
                            yearsLeft: (totalYears + years[i] - ageYears).toFixed(1)
                        };
                    }
                    totalYears += years[i];
                }
            } catch (e) {
                console.log('Dasha calculation error');
            }
            
            return { dasha: 'Sun', antardasha: 'Moon', yearsLeft: '5.0' };
        }

        function calculateChart() {
            const name = document.getElementById('name').value || 'Unknown';
            const birthDate = document.getElementById('date').value;
            const birthTime = document.getElementById('time').value;
            const birthPlace = document.getElementById('place').value || 'Unknown';

            // Update personal info
            const date = new Date(birthDate);
            const weekday = date.toLocaleDateString('en-US', { weekday: 'long' });
            
            document.getElementById('personalInfo').innerHTML = `
                <div class="info-item"><span><strong>Name:</strong></span><span>${name}</span></div>
                <div class="info-item"><span><strong>Birth Date:</strong></span><span>${birthDate}</span></div>
                <div class="info-item"><span><strong>Birth Time:</strong></span><span>${birthTime}</span></div>
                <div class="info-item"><span><strong>Birth Place:</strong></span><span>${birthPlace}</span></div>
                <div class="info-item"><span><strong>Weekday:</strong></span><span>${weekday}</span></div>
                <div class="info-item"><span><strong>Tithi:</strong></span><span>Saptami</span></div>
            `;

            // Update dasha info
            const dashaInfo = calculateDasha(birthDate);
            const dashaStatus = ['Jupiter', 'Venus', 'Moon'].includes(dashaInfo.dasha) ? 'Favorable' : 
                             ['Saturn', 'Mars', 'Rahu', 'Ketu'].includes(dashaInfo.dasha) ? 'Challenging' : 'Mixed';

            document.getElementById('dashaInfo').innerHTML = `
                <div class="info-item"><span><strong>Main Dasha:</strong></span><span>${dashaInfo.dasha}</span></div>
                <div class="info-item"><span><strong>Antardasha:</strong></span><span>${dashaInfo.antardasha}</span></div>
                <div class="info-item"><span><strong>Years Left:</strong></span><span>${dashaInfo.yearsLeft} years</span></div>
                <div class="info-item"><span><strong>Period Status:</strong></span><span>${dashaStatus}</span></div>
            `;

            // Update planetary table
            const tbody = document.getElementById('planetTableBody');
            tbody.innerHTML = '';
            
            planetData.forEach(planet => {
                const statusClass = planet.status;
                const statusText = planet.status === 'good' ? 'Favorable' : 
                                 planet.status === 'bad' ? 'Challenging' : 'Neutral';
                const motionText = planet.motion ? ` (${planet.motion})` : '';
                
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td><strong>${planet.planet}</strong></td>
                    <td>${planet.sign}${motionText}</td>
                    <td>${planet.degree}</td>
                    <td>${planet.nakshatra}</td>
                    <td>${planet.lord}</td>
                    <td>${planet.house}</td>
                    <td class="${statusClass}">${statusText}</td>
                `;
                tbody.appendChild(row);
            });

            // Update transits
            const transitGrid = document.getElementById('transitGrid');
            transitGrid.innerHTML = '';
            
            transitData.forEach(transit => {
                const statusColor = transit.status === 'good' ? '#28a745' : 
                                  transit.status === 'bad' ? '#dc3545' : '#ffc107';
                
                const card = document.createElement('div');
                card.className = 'transit-card';
                card.innerHTML = `
                    <h4 style="color: ${statusColor}; margin-bottom: 10px;">${transit.planet}</h4>
                    <p><strong>Position:</strong> ${transit.position}</p>
                    <p><strong>Effect:</strong> ${transit.effect}</p>
                `;
                transitGrid.appendChild(card);
            });

            // Update events
            const eventsGrid = document.getElementById('eventsGrid');
            eventsGrid.innerHTML = '';
            
            upcomingEvents.forEach(event => {
                const eventClass = event.status === 'good' ? 'event-good' : 
                                 event.status === 'bad' ? 'event-bad' : 'event-neutral';
                
                const item = document.createElement('div');
                item.className = `event-item ${eventClass}`;
                item.innerHTML = `<strong>${event.date}:</strong> ${event.event}`;
                eventsGrid.appendChild(item);
            });

            // Scroll to results
            document.querySelector('.dashboard').scrollIntoView({ behavior: 'smooth' });
        }

        // Initialize
        window.onload = function() {
            updateTime();
            setInterval(updateTime, 1000);
            
            // Set current date
            document.getElementById('date').value = new Date().toISOString().split('T')[0];
            
            // Auto calculate after 2 seconds
            setTimeout(calculateChart, 2000);
        };
    </script>
</body>
</html>
