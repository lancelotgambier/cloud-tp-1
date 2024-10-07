# app = func.FunctionApp()

# @app.route(route="myHttpFunction", auth_level=func.AuthLevel.ANONYMOUS)
# def myHttpFunction(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )

# import azure.functions as func
# import logging

# app = func.FunctionApp()

# @app.route(route="myHttpFunction", auth_level=func.AuthLevel.ANONYMOUS)
# def myHttpFunction(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')
    
#     return func.HttpResponse("Hello, World!", status_code=200)



import azure.functions as func
from pymongo import MongoClient
import os
import logging
import json
from bson import json_util

# Initialize the function app
app = func.FunctionApp()

# Retrieve the MongoDB connection string from Azure application settings
MONGO_CONNECTION_STRING = os.environ.get("MONGO_CONNECTION_STRING")

# Verify if the connection string is properly retrieved
if not MONGO_CONNECTION_STRING:
    raise ValueError("MongoDB connection string is not defined.")

# Connect to MongoDB (outside the function to reuse the connection)
client = MongoClient(MONGO_CONNECTION_STRING)
db = client['mongo1']
collection = db['collection1']

@app.route(route="getDocuments", auth_level=func.AuthLevel.ANONYMOUS)
def get_documents(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Retrieve documents
        documents = list(collection.find())
        
        # Convert documents to JSON
        json_documents = json.dumps(documents, default=json_util.default)
        
        return func.HttpResponse(
            json_documents,
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        logging.error(f"Error retrieving documents: {e}")
        return func.HttpResponse(
            "Error retrieving documents",
            status_code=500
        )
