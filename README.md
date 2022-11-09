# unemployment-report
For Homework


Make sure that all your "app" is lower case
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
### Email Sending

Run the email service to send an example email and see if everything is working:

```sh
python -m app.email_service
```

Send the unemployment report via email:

```sh
python -m app.unemployment_email
```

Send the stocks report via email:

```sh
python -m app.stocks_email

# or in production mode:
APP_ENV="production" DEFAULT_SYMBOL="GOOGL" python -m app.stocks_email
```

## Testing

Run tests:

```sh
pytest
```