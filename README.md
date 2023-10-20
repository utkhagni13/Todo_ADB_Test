# Adbrew Test!

# Instructions Followed [IMPORTANT]

1. All React code was implemented using [React hooks](https://reactjs.org/docs/hooks-intro.html), not using traditional stateful React components and component lifecycle method.
2. Django's model, serializers or SQLite DB were not used. All data was retrieved from a mongo instance. Reffered to the `db` instance which was already present in `views.py`.
3. Followed and integrated the Docker setup after making few corrections.
4. Applied all the basic concepts of React Hooks/Mongo/Docker.
5. Created a New Repo instead of forking and making a PR, as instructed.
6. Completed the assessment with full understaning of the code and ready for live walkthrough.
7. Error handling, abstractions, well-maintained code architecture and modularity of code was kept in mind while working.

# Tasks Completed

After running localhost:3000, the following 2 things would appear:

1. A form with a TODO description textbox and a submit button. On this form submission, the app interacts with the Django backend (POST http://localhost:8000) and creates a TODO in MongoDB.
2. A list with hardcoded TODOs. This was changed to reflect TODOs in the backend (GET http://localhost:8000).
   When the form is submitted, the TODO list should refreshes again and fetch latest list of TODOs from MongoDB

# Structure

This repository includes code for a Docker setup with 3 containers:

-   App: This is the React dev server and runs on http://localhost:3000. The code for this resides in src/app directory.
-   API: This is the backend container that run a Django instance on http://localhost:8000.
-   Mongo: This is a DB instance running on port 27017. Django views already have code written to connect to this instance of Mongo.

# Setup

1. Clone this repository

```
git clone https://github.com/utkhagni13/Todo-ADB-test.git
```

2. Change into the cloned directory and set the environment variable for the code path. Replace `path_to_repository` appropriately.

```
export ADBREW_CODEBASE_PATH="{path_to_repository}/test/src"
```

3. Build the container.

```
docker-compose build
```

4. Once the build is completed, start the containers:

```
docker-compose up -d
```

5. Once complete, `docker ps` should output something like this:

```
CONTAINER ID   IMAGE               COMMAND                  CREATED         STATUS         PORTS                      NAMES
e445be7efa61   adbrew_test_api     "bash -c 'cd /src/re…"   3 minutes ago   Up 2 seconds   0.0.0.0:8000->8000/tcp     api
0fd203f12d8a   adbrew_test_app     "bash -c 'cd /src/ap…"   4 minutes ago   Up 3 minutes   0.0.0.0:3000->3000/tcp     app
884cb9296791   adbrew_test_mongo   "/usr/bin/mongod --b…"   4 minutes ago   Up 3 minutes   0.0.0.0:27017->27017/tcp   mongo
```

6. Check that http://localhost:3000 and http://localhost:8000 are started.
