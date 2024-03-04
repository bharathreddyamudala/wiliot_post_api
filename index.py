from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/v1/data-connection/endpoint/wiliot', methods=['POST'])
def process_data():
    input_data = request.json

    # Extract data from the input
    assetId = input_data.get('assetId', None)
    categoryId = input_data.get('categoryId', None)
    eventName = input_data.get('eventName', None)
    start = input_data.get('start', None)
    end = input_data.get('end', None)
    ownerId = input_data.get('ownerId', None)
    confidence = input_data.get('confidence', None)
    value = input_data.get('value', None)
    createdOn = input_data.get('createdOn', None)

    # Manipulate the data or perform any required operations
    output_data = {
        "assetId": assetId,
        "categoryId": categoryId,
        "eventName": eventName,
        "value": value,
        "confidence": confidence,
        "timestamp": createdOn,
        "status": "success"
    }

    response = record_data(output_data)
    return response


def record_data(data):
    # Record data logic
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')