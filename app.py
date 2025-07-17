from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

@app.route('/stations', methods=['GET'])
def get_stations():
    stations = []
    with open('stations.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations.append({
                'name': row['이름'],
                'lat': float(row['위도']),
                'lng': float(row['경도']),
                'status': row['상태']
            })
    return jsonify(stations)

@app.route('/status')
def status():
    site = request.args.get('site')
    found_status = "데이터 없음"

    with open('stations.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['이름'] == site:
                found_status = row['상태']
                break

    return jsonify({"status": found_status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
