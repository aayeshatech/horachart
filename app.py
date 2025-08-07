from flask import Flask, render_template, request, jsonify
from datetime import datetime, date

app = Flask(__name__)

def get_planetary_positions():
    return [
        {'planet': 'Sun ☉', 'sign': '♋ Cancer', 'degree': '20.76', 'nakshatra': 'Ashlesha', 'lord': 'Mercury ☿', 'pada': 2, 'house': 4, 'status': 'good', 'motion': ''},
        {'planet': 'Moon ☽', 'sign': '♐ Sagittarius', 'degree': '24.88', 'nakshatra': 'Purva Ashadha', 'lord': 'Venus ♀', 'pada': 4, 'house': 9, 'status': 'good', 'motion': ''},
        {'planet': 'Mercury ☿', 'sign': '♋ Cancer', 'degree': '10.93', 'nakshatra': 'Pushya', 'lord': 'Saturn ♄', 'pada': 3, 'house': 4, 'status': 'bad', 'motion': 'Retrograde'},
        {'planet': 'Venus ♀', 'sign': '♊ Gemini', 'degree': '13.98', 'nakshatra': 'Ardra', 'lord': 'Rahu ☊', 'pada': 3, 'house': 3, 'status': 'good', 'motion': ''},
        {'planet': 'Mars ♂', 'sign': '♍ Virgo', 'degree': '5.94', 'nakshatra': 'Uttara Phalguni', 'lord': 'Sun ☉', 'pada': 3, 'house': 6, 'status': 'neutral', 'motion': ''},
        {'planet': 'Jupiter ♃', 'sign': '♊ Gemini', 'degree': '18.81', 'nakshatra': 'Ardra', 'lord': 'Rahu ☊', 'pada': 4, 'house': 3, 'status': 'good', 'motion': ''},
        {'planet': 'Saturn ♄', 'sign': '♓ Pisces', 'degree': '7.20', 'nakshatra': 'Uttara Bhadrapada', 'lord': 'Saturn ♄', 'pada': 2, 'house': 12, 'status': 'neutral', 'motion': 'Retrograde'},
        {'planet': 'Rahu ☊', 'sign': '♒ Aquarius', 'degree': '25.73', 'nakshatra': 'Purva Bhadrapada', 'lord': 'Jupiter ♃', 'pada': 2, 'house': 11, 'status': 'neutral', 'motion': 'Retrograde'},
        {'planet': 'Ketu ☋', 'sign': '♌ Leo', 'degree': '25.73', 'nakshatra': 'Purva Phalguni', 'lord': 'Venus ♀', 'pada': 4, 'house': 5, 'status': 'neutral', 'motion': 'Retrograde'}
    ]

def get_transits():
    return [
        {'planet': 'Sun ☉', 'sign': '♋ Cancer (20.76°)', 'house': 'Ashlesha Nakshatra', 'effect': 'Emotional depth & family focus', 'status': 'good'},
        {'planet': 'Moon ☽', 'sign': '♐ Sagittarius (24.88°)', 'house': 'Purva Ashadha', 'effect': 'Spiritual expansion & optimism', 'status': 'good'},
        {'planet': 'Mercury ☿', 'sign': '♋ Cancer (10.93°) ℞', 'house': 'Pushya Nakshatra', 'effect': 'Communication delays (Retrograde)', 'status': 'bad'},
        {'planet': 'Venus ♀', 'sign': '♊ Gemini (13.98°)', 'house': 'Ardra Nakshatra', 'effect': 'Social versatility & learning', 'status': 'good'},
        {'planet': 'Mars ♂', 'sign': '♍ Virgo (5.94°)', 'house': 'Uttara Phalguni', 'effect': 'Practical action & organization', 'status': 'good'},
        {'planet': 'Jupiter ♃', 'sign': '♊ Gemini (18.81°)', 'house': 'Ardra Nakshatra', 'effect': 'Knowledge expansion & teaching', 'status': 'good'},
        {'planet': 'Saturn ♄', 'sign': '♓ Pisces (7.2°) ℞', 'house': 'Uttara Bhadrapada', 'effect': 'Spiritual lessons (Retrograde)', 'status': 'neutral'},
        {'planet': 'Rahu ☊', 'sign': '♒ Aquarius (25.73°) ℞', 'house': 'Purva Bhadrapada', 'effect': 'Humanitarian focus', 'status': 'neutral'}
    ]

def calculate_dasha(birth_date):
    planets = ['Sun', 'Moon', 'Mars', 'Rahu', 'Jupiter', 'Saturn', 'Mercury', 'Ketu', 'Venus']
    years = [6, 10, 7, 18, 16, 19, 17, 7, 20]
    
    today = datetime.now()
    birth = datetime.strptime(birth_date, '%Y-%m-%d')
    age = (today - birth).days / 365.25
    
    total = 0
    for i, planet in enumerate(planets):
        if age >= total and age < total + years[i]:
            return {'current_dasha': planet, 'current_antardasha': planets[i % len(planets)]}
        total += years[i]
    
    return {'current_dasha': 'Sun', 'current_antardasha': 'Moon'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        name = data.get('name', 'Unknown')
        birth_date = data.get('date', str(date.today()))
        birth_time = data.get('time', '12:00')
        birth_place = data.get('place', 'Unknown')
        
        date_obj = datetime.strptime(birth_date, '%Y-%m-%d')
        weekday = date_obj.strftime('%A')
        
        result = {
            'personal_info': {
                'name': name, 'date': birth_date, 'time': birth_time, 
                'place': birth_place, 'weekday': weekday, 'tithi': 'Saptami', 'nakshatra': 'Rohini'
            },
            'planetary_positions': get_planetary_positions(),
            'current_transits': get_transits(),
            'dasha_info': calculate_dasha(birth_date),
            'upcoming_transits': [
                {'date': '2025-08-11', 'event': 'Mercury turns Direct', 'status': 'good'},
                {'date': '2025-08-17', 'event': 'Sun enters Leo', 'status': 'neutral'},
                {'date': '2025-08-21', 'event': 'Venus enters Cancer', 'status': 'good'}
            ]
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🌟 Astrology Calculator Starting...")
    app.run(debug=True, host='0.0.0.0', port=5000)
