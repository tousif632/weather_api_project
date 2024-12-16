from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = "1db8e45b230c29e267629252746d37ad"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return render_template('index.html', error="City parameter is required")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=1db8e45b230c29e267629252746d37ad&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }
        return render_template('index.html', weather=weather_info)
    else:
        return render_template('index.html', error="City not found or API error")

if __name__ == '__main__':
    app.run(debug=True)
