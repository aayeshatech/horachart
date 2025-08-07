<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vedic Astrology Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .header {
            background: linear-gradient(45deg, #ff6b6b, #feca57);
            padding: 20px;
            text-align: center;
            border-radius: 15px;
            margin-bottom: 20px;
            color: white;
        }
        .input-section {
            background: rgba(255,255,255,0.95);
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
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
        }
        .input-group input {
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
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
        }
        .calculate-btn:hover {
            transform: translateY(-2px);
        }
        .results {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .result-panel {
            background: rgba(255,255,255,0.95);
            padding: 20px;
            border-radius: 15px;
        }
        .result-panel h3 {
            color: #2c3e50;
            margin-bottom: 15px;
            text-align: center;
        }
        .alert-box {
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
            color: white;
            padding: 15px;
            margin: 20px 0;
            border-radius: 10px;
            text-align: center;
        }
        .planetary-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: white;
            border-radius: 10px;
            overflow: hidden;
        }
        .planetary-table th {
            background: #2c3e50;
            color: white;
            padding: 12px;
            font-weight: bold;
        }
        .planetary-table td {
            padding: 10px;
            border-bottom: 1px solid #eee;
            text-align: center;
        }
        .status-good { color: #28a745; font-weight: bold; }
        .status-bad { color: #dc3545; font-weight: bold; }
        .status-neutral { color: #ffc107; font-weight: bold; }
        .transit-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }
        .transit-card {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #e9ecef;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌟 Vedic Astrology Calculator 🌟</h1>
            <p>Real-time Planetary Positions & Transit Analysis</p>
        </div>

        <div class="input-section">
            <div class="input-grid">
                <div class="input-group">
                    <label>👤 Name:</label>
                    <input type="text" id="name" placeholder="Enter your name">
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
            </div>
            <center>
                <button class="calculate-btn" onclick="calculateChart()">🔮 Calculate Chart</button>
            </center>
        </div>

        <div class="alert-box">
            <h3>⚠️ Current Transit Alert: Mercury Retrograde in Cancer</h3>
            <p>Be cautious with communications and family matters until August 11, 2025</p>
        </div>

        <div class="results">
            <div class="result-panel">
                <h3>📋 Personal Information</h3>
                <div id="personalInfo">
                    <p>Enter your details and click Calculate Chart</p>
                </div>
            </div>

            <div class="result-panel">
                <h3>⏰ Current Dasha Status</h3>
                <div id="dashaInfo">
                    <p>Dasha information will appear here</p>
                </div>
            </div>
        </div>

        <div class="result-panel">
            <h3>🚀 Current Planetary Transits (August 7, 2025)</h3>
            <div class="transit-grid" id="transitGrid">
                <!-- Transit cards will be populated here -->
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
                    <th>👑 Lord</th>
                    <th>📈 Status</th>
                </tr>
            </thead>
            <tbody id="planetaryData">
                <tr><td colspan="7">Click Calculate Chart to see planetary positions</td></tr>
            </tbody>
        </table>
    </div>

    <script>
        async function calculateChart() {
            const formData = {
                name: document.getElementById('name').value || 'Unknown',
                date: document.getElementById('date').value,
                time: document.getElementById('time').value,
                place: document.getElementById('place').value || 'Unknown'
            };

            try {
                const response = await fetch('/calculate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(formData)
                });

                const data = await response.json();
                
                updatePersonalInfo(data.personal_info);
                updateDashaInfo(data.dasha_info);
                updatePlanetaryData(data.planetary_positions);
                updateTransitData(data.current_transits);
                
            } catch (error) {
                alert('Error: ' + error.message);
            }
        }

        function updatePersonalInfo(info) {
            document.getElementById('personalInfo').innerHTML = `
                <p><strong>Name:</strong> ${info.name}</p>
                <p><strong>Date:</strong> ${info.date}</p>
                <p><strong>Time:</strong> ${info.time}</p>
                <p><strong>Place:</strong> ${info.place}</p>
                <p><strong>Weekday:</strong> ${info.weekday}</p>
                <p><strong>Tithi:</strong> ${info.tithi}</p>
            `;
        }

        function updateDashaInfo(dasha) {
            document.getElementById('dashaInfo').innerHTML = `
                <p><strong>Main Dasha:</strong> ${dasha.current_dasha}</p>
                <p><strong>Antardasha:</strong> ${dasha.current_antardasha}</p>
                <p><strong>Status:</strong> Currently Active</p>
            `;
        }

        function updatePlanetaryData(positions) {
            const tbody = document.getElementById('planetaryData');
            tbody.innerHTML = '';

            positions.forEach(pos => {
                const statusClass = `status-${pos.status}`;
                const motionText = pos.motion ? ` (${pos.motion})` : '';
                
                tbody.innerHTML += `
                    <tr>
                        <td><strong>${pos.planet}</strong></td>
                        <td>${pos.sign}${motionText}</td>
                        <td>${pos.degree}°</td>
                        <td>${pos.house}</td>
                        <td>${pos.nakshatra}</td>
                        <td>${pos.lord}</td>
                        <td class="${statusClass}">${pos.status.toUpperCase()}</td>
                    </tr>
                `;
            });
        }

        function updateTransitData(transits) {
            const grid = document.getElementById('transitGrid');
            grid.innerHTML = '';

            transits.forEach(transit => {
                const statusColor = transit.status === 'good' ? '#28a745' : 
                                  transit.status === 'bad' ? '#dc3545' : '#ffc107';
                
                grid.innerHTML += `
                    <div class="transit-card">
                        <h4 style="color: ${statusColor};">${transit.planet}</h4>
                        <p><strong>Sign:</strong> ${transit.sign}</p>
                        <p><strong>Effect:</strong> ${transit.effect}</p>
                    </div>
                `;
            });
        }

        // Auto-load on page load
        window.onload = function() {
            document.getElementById('date').value = new Date().toISOString().split('T')[0];
            calculateChart();
        };
    </script>
</body>
</html>
