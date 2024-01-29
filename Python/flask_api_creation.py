from flask import Flask, request, jsonify
import csv

app = Flask(__name__)
@app.route('/home')
def home():
    return jsonify({'success': True})
@app.route('/2023summary/<int:daynum>')
def retrieve_day_report(daynum):
    with open('./bin/practice_data_2023.csv') as file:
        csv_reader = csv.reader(file)
        day_summary = []
        for line in csv_reader:
            day_summary.append(line)
        print(day_summary)
        response = {}
        if 0 < daynum < len(day_summary):
            response['day'] = daynum
            response['temperature'] = float(day_summary[daynum][1])
            response['temperature_unit'] = 'C'
            response['humidity'] = float(day_summary[daynum][2])
            response['humidity_unit'] = '%'
            response['wind'] = float(day_summary[daynum][3])
            response['wind_unit'] = 'Km/h'
        else:
            response['error'] = f'Day {daynum} is not found in summary'
    return jsonify(response), 200
if __name__ == "__main__":
    app.run(debug=True)
