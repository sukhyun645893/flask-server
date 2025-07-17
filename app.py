from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/status')
def status():
    site = request.args.get('site')
    fake_status_data = {
        "대전탑립동1": "정상 작동 중",
        "대전탑립동2": "점검 필요"
    }
    return jsonify({"status": fake_status_data.get(site, "데이터 없음")})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
