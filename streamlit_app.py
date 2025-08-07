<!DOCTYPE html>
<html>
<head>
    <title>🌟 Astrology Calculator</title>
    <style>
        body { font-family: Arial; background: linear-gradient(135deg, #667eea, #764ba2); margin: 0; padding: 20px; color: #333; min-height: 100vh; }
        .container { max-width: 900px; margin: 0 auto; }
        .header { background: linear-gradient(45deg, #ff6b6b, #feca57); color: white; padding: 30px; text-align: center; border-radius: 15px; margin-bottom: 20px; }
        .header h1 { margin: 0; font-size: 2.5em; }
        .alert { background: #ff6b6b; color: white; padding: 20px; text-align: center; border-radius: 10px; margin: 20px 0; animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.02); } }
        .section { background: rgba(255,255,255,0.9); padding: 20px; border-radius: 15px; margin: 20px 0; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
        .input-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 20px; }
        .input-group label { display: block; font-weight: bold; margin-bottom: 5px; }
        .input-group input { width: 100%; padding: 10px; border: 2px solid #ddd; border-radius: 5px; }
        .btn { background: #00c851; color: white; padding: 15px 30px; border: none; border-radius: 10px; cursor: pointer; font-size: 16px; font-weight: bold; }
        .btn:hover { background: #007e33; }
        .planet-row { padding: 10px; margin: 5px 0; border-radius: 5px; display: flex; justify-content: space-between; }
        .good { background: #d4edda; color: #155724; }
        .bad { background: #f8d7da; color: #721c24; }
        .neutral { background: #fff3cd; color: #856404; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌟 Astrology Calculator</h1>
            <p id="time"></p>
        </div>

        <div class="alert">
            <h3>⚠️ Mercury Retrograde Alert</h3>
            <p>Communications require caution until August 11, 2025</p>
        </div>

        <div class="section">
            <div class="input-grid">
                <div class="input-group">
                    <label>Name:</label>
                    <input type="text" id="name" value="Sample Person">
                </div>
                <div class="input-group">
                    <label>Birth Date:</label>
                    <input type="date" id="date" value="1990-01-01">
                </div>
                <div class="input-group">
                    <label>Birth Time:</label>
                    <input type="time" id="time" value="12:00">
                </div>
                <div class="input-group">
                    <label>Birth Place:</label>
                    <input type="text" id="place" value="Mumbai, India">
                </div>
            </div>
            <center><button class="btn" onclick="calc()">🔮 Calculate</button></center>
        </div>

        <div class="section" id="results" style="display:none;">
            <h3>📋 Personal Information</h3>
            <div id="personal"></div>
            
            <h3>🪐 Current Planetary Positions (Aug 7, 2025)</h3>
            <div id="planets"></div>
            
            <h3>📅 Upcoming Events</h3>
            <div class="planet-row good">
                <span><strong>Aug 11, 2025:</strong> Mercury Direct</span>
                <span>✅ Communication improves</span>
            </div>
            <div class="planet-row good">
                <span><strong>Aug 21, 2025:</strong> Venus enters Cancer</span>
                <span>✅ Family harmony</span>
            </div>
            <div class="planet-row bad">
                <span><strong>Sep 1, 2025:</strong> Saturn re-enters Pisces</span>
                <span>⚠️ Spiritual challenges</span>
            </div>
        </div>
    </div>

    <script>
        const data = [
            ['Sun ☉', '♋ Cancer', '20.76°', 'Ashlesha', 'good'],
            ['Moon ☽', '♐ Sagittarius', '24.88°', 'Purva Ashadha', 'good'],
            ['Mercury ☿', '♋ Cancer (R)', '10.93°', 'Pushya', 'bad'],
            ['Venus ♀', '♊ Gemini', '13.98°', 'Ardra', 'good'],
            ['Mars ♂', '♍ Virgo', '5.94°', 'Uttara Phalguni', 'neutral'],
            ['Jupiter ♃', '♊ Gemini', '18.81°', 'Ardra', 'good'],
            ['Saturn ♄', '♓ Pisces (R)', '7.20°', 'Uttara Bhadrapada', 'neutral'],
            ['Rahu ☊', '♒ Aquarius (R)', '25.73°', 'Purva Bhadrapada', 'neutral'],
            ['Ketu ☋', '♌ Leo (R)', '25.73°', 'Purva Phalguni', 'neutral']
        ];

        function updateTime() {
            document.getElementById('time').textContent = new Date().toLocaleString();
        }

        function calc() {
            const name = document.getElementById('name').value;
            const date = document.getElementById('date').value;
            const time = document.getElementById('time').value;
            const place = document.getElementById('place').value;

            document.getElementById('personal').innerHTML = `
                <div style="padding:10px; background:#f8f9fa; margin:5px 0; border-radius:5px;">
                    <strong>Name:</strong> ${name}<br>
                    <strong>Date:</strong> ${date}<br>
                    <strong>Time:</strong> ${time}<br>
                    <strong>Place:</strong> ${place}
                </div>
            `;

            let planetsHTML = '';
            data.forEach(planet => {
                const [name, sign, degree, nakshatra, status] = planet;
                const statusText = status === 'good' ? 'Favorable' : 
                                 status === 'bad' ? 'Challenging' : 'Neutral';
                planetsHTML += `
                    <div class="planet-row ${status}">
                        <span><strong>${name}</strong> in ${sign} (${degree}) - ${nakshatra}</span>
                        <span>${statusText}</span>
                    </div>
                `;
            });
            document.getElementById('planets').innerHTML = planetsHTML;

            document.getElementById('results').style.display = 'block';
            document.getElementById('results').scrollIntoView({ behavior: 'smooth' });
        }

        setInterval(updateTime, 1000);
        updateTime();
        
        // Auto-calculate after 2 seconds
        setTimeout(calc, 2000);
    </script>
</body>
</html>
