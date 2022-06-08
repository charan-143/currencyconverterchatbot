from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/',methods=["POST"])
def index():
  data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency'][
        'currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    cf = fetch_conversion_factor(source_currency, target_currency)
    final_amount = amount * cf
    final_amount = round(final_amount, 2)
    response = {
        'fulfillmentText':"{} {} is {} {}".format(amount, source_currency, final_amount,target_currency)
    }
    return jsonify(response)
    weather = ""
    geo_city = data['queryResult']['parameters']["geo-city"]
    
    response = {
        'fulfillmentText':"weather in {} {}".format(geo_city,weather)
    }

def fetch_conversion_factor(source, target):

    url = "https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey=b5d6b8ead1b89dd6e693".format(
        source, target)

    response = requests.get(url)
    response = response.json()

    return response['{}_{}'.format(source, target)]




if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
