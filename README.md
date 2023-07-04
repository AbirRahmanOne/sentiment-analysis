# installation process 

### Create a virtual environment to isolate our package dependencies locally
`python3.8 -m venv env`

### activate virtual env
`source env/bin/activate`

### for install dependency 
`pip install -r requirements.txt` 


#### for run the project 
### We're now ready to test the API we've built. Let's fire up the server from the command line.

`python manage.py migrate`
`python manage.py runserver`



# Api endpoint details

#### Method : POST 
`http://localhost:8000/sentiment-analysis/analyze/`






