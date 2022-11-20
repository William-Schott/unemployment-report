# unemployment-report
For Homework

##Setup 

Create and activate a virtual envoronment
cd ~/Desktop/unemployment-report
conda create -n unemployment-env python=3.8
conda activate unemployment-env

pip install -r requirements.txt

#Configuration
obtain a api key from alpha vantage https://www.alphavantage.co/support/#api-key
and store that in the env file



##Usage
'''sh
python app/my_script.py
python app/unemployment.py
API Key: PCBWXAJKUC99DFN6

comand to run 
#python app/unemployment.py
python -m app.unemployment

run stocks report:

'''sh
#python -app/stock.py
python -m app.stocks
'''sh

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```
