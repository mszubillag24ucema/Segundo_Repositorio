from flask import Flask, request, jsonify
from db_management.statistics_load import load_statistics, save_statistics
import statistics

app = Flask(__name__)
data_user = load_statistics()


@app.route('/api/prometheus/statistics', methods=['POST']) # agregar al archivo statistics.csv la info del día
def statistics():

    body = request.json
    date = body['date']
    dna = body['dna']
    blod = body['blod_sugar_level']
    emotions = body['emotion_level']
    data = {'date': date, 'dna': dna, 'blod_sugar_level': blod, 'emotion_level': emotions}
    return save_statistics(data)


@app.route('/api/prometheus/statistics', methods=['GET']) # consultar la info guardada en statistics.csv
def information():
    return jsonify([data.serialize() for data in data_user])


@app.route('/api/prometheus/reports', methods=['GET']) # consultar los pormedios de blod y emotions de un día
def reports():
    report_date = request.args.get['report_date', ""]
    blod = []
    emotion = []
    info = {}
    try:
        for data in data_user:
            if data.date == report_date:
                blod.append(data.blod_sugar_level)
                emotion.append(data.emotion_level)
        info['avg_blod_sugar_level'] = statistics.mean(blod)
        info['avg_emotion_level'] = statistics.mean(emotion)
        return jsonify(info)
    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code="ERROR",
            error_description="Bad request",
            error_body=missing_param
        ), 400


if __name__ == '__main__':
    app.run()
