Steps on how to run the system

1. First activate the virtual environment "casestudy"
  run `scripts\activate` from the casestudy directory

2. Run `python app.py` to start the Flask app from the project directory

3. Visit the url of the running flask app to test functionality
   `http://127.0.0.1:5000`

    4. since the secret key is already generated there will be no need to run the backend and test python files

    5. if you would like to use a new secret key:
    run `python backend.py`
    then `python test.py` if not generated
    finally `python app.py`


