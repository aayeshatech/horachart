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
                <div class="info-grid" id="personalInfo">
                    <!-- Personal info will be populated here -->
                </div>
            </div>

            <div class="info-panel">
                <h3>⏰ Current Transit Status</h3>
                <div class="info-grid" id="transitStatus">
                    <!-- Transit status will be populated here -->
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
                <div class="current-period" id="currentPeriod">
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

        async function calculateChart() {
            const formData = {
                name: document.getElementById('name').value || 'Unknown Person',
                date: document.getElementById('date').value,
                time: document.getElementById('time').value,
                place: document.getElementById('place').value || 'Unknown Location',
                latitude: document.getElementById('latitude').value,
                longitude: document.getElementById('longitude').value
            };

            try {
                const response = await fetch('/calculate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData)
                });

                const data = await response.json();
                
                updatePersonalInfo(data.personal_info);
                updatePlanetaryData(data.planetary_positions);
                updateTransitData(data.current_transits);
                updateDashaInfo(data.dasha_info);
                updateCharts();
                
            } catch (error) {
                console.error('Error calculating chart:', error);
                alert('Error calculating chart. Please try again.');
            }
        }

        function updatePersonalInfo(info) {
            const container = document.getElementById('personalInfo');
            container.innerHTML = `
                <div class="info-item"><span><strong>Name:</strong></span><span>${info.name}</span></div>
                <div class="info-item"><span><strong>Date:</strong></span><span>${info.date}</span></div>
                <div class="info-item"><span><strong>Time:</strong></span><span>${info.time}</span></div>
                <div class="info-item"><span><strong>Place:</strong></span><span>${info.place}</span></div>
                <div class="info-item"><span><strong>Weekday:</strong></span><span>${info.weekday}</span></div>
                <div class="info-item"><span><strong>Tithi:</strong></span><span>${info.tithi}</span></div>
                <div class="info-item"><span><strong>Nakshatra:</strong></span><span>${info.nakshatra}</span></div>
            `;
        }

        function updatePlanetaryData(positions) {
            const tbody = document.getElementById('planetaryData');
            tbody.innerHTML = '';

            positions.forEach(pos => {
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

        function updateTransitData(transits) {
            const grid = document.getElementById('transitGrid');
            grid.innerHTML = '';

            transits.forEach(transit => {
                const card = document.createElement('div');
                card.className = 'transit-card';
                
                let statusColor = '#6c757d';
                if (transit.status === 'good') statusColor = '#28a745';
                if (transit.status === 'bad') statusColor = '#dc3545';
                
                card.innerHTML = `
                    <h4 style="color: ${statusColor}; margin-bottom: 10px;">${transit.planet}</h4>
                    <p><strong>Current Sign:</strong> ${transit.sign}</p>
                    <p><strong>Nakshatra:</strong> ${transit.house}</p>
                    <p><strong>Effect:</strong> ${transit.effect}</p>
                `;
                
                grid.appendChild(card);
            });
        }

        function updateDashaInfo(dashaInfo) {
            const currentPeriodInfo = document.getElementById('currentPeriodInfo');
            currentPeriodInfo.innerHTML = `
                <strong>Main Dasha:</strong> ${dashaInfo.current_dasha}<br>
                <strong>Antardasha:</strong> ${dashaInfo.current_antardasha}<br>
                <strong>Status:</strong> Currently running period
            `;
        }

        function updateCharts() {
            createChart('rashiChart');
            createChart('navamshaChart');
        }

        function createChart(chartId) {
            const chart = document.getElementById(chartId);
            chart.innerHTML = '';

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
            
            document.getElementById('date').value = new Date().toISOString().split('T')[0];
        };
    </script>
</body>
</html>
