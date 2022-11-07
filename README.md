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