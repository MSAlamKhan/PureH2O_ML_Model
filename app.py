from flask import Flask, request, redirect
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import prediction

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class Test(Resource):
    def get(self):
        return 'Welcome to, Test App API!'

    def post(self):
        try:
            value = request.get_json()
            if(value):
                return {'Post Values': value}, 201

            return {"error":"Invalid format."}

        except Exception as error:
            return {'error': error}

class GetPredictionOutput(Resource):
    def get(self):
        return {"error":"Invalid Method."}

    def post(self):
        # try:
            data = request.get_json()
            print("DAATAA",data["data"],)
            predict = prediction.predict_mpg(data["data"])
            predictOutput = predict
            return {'Sales Prediction':predictOutput[0]},200

        # except Exception as error:
        #     return {'error': error}

api.add_resource(Test,'/')
api.add_resource(GetPredictionOutput,'/getPredictionOutput')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='ec2-51-21-127-105.eu-north-1.compute.amazonaws.com', port=port)