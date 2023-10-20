from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pymongo import MongoClient
import os

mongo_uri = os.getenv("DATABASE_URL")
client = MongoClient(mongo_uri)
db = client[os.getenv("DATABASE_NAME")]
collection = db[os.getenv("COLLECTION_NAME")]

class TodoListView(APIView):
    def get(self, request):
        # Implement this method - return all todo items from db instance above.
        try:
            # fetch the list of todos
            data = collection.find()
            todos = [
                {
                    '_id': str(obj.get('_id')),  # Convert ObjectId to string
                    'title': obj.get('title'),
                }
                for obj in data
            ]
            if (todos.__len__):
                return Response({"data": todos, "error": None}, status=status.HTTP_200_OK)
            else:
                return Response({"data": None, "error": "No Data Found"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"data": None, "error": Exception}, status=status.HTTP_400_BAD_REQUEST)


class TodoListAdd(APIView):
    def post(self, request):
        # Implement this method - accept a todo item in a mongo collection, persist it using db instance above.
        try:
            # get the todo's title
            title = request.data["title"]

            # check if the todo already exists in the lists
            existing_task = collection.find_one({'title': title})
            if existing_task:
                return Response({"data": None, "error": "Already Exists"}, status=status.HTTP_409_CONFLICT)

            # insert the todo in the list
            data = collection.insert_one({'title': title})
            if data:
                result = {
                    '_id': str(data.inserted_id),
                    'title': title,
                }
                return Response({"data": result, "error": None}, status=status.HTTP_200_OK)
            else:
                return Response({"data": None, "error": "Database Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({"data": None, "error": Exception}, status=status.HTTP_400_BAD_REQUEST)
