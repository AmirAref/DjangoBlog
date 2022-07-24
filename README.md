# DjangoBlog
a weblog with the Django.  

<br>
 
# Installation Guide:  
### Virtual Environment :  
make a virtualenv
```bash
python3 -m venv venv
```
or 
```bash
virtualenv -p python3 venv
```
then activate the virtualenv  
```bash
source venv/bin/activate
```
### Requirements :  
install the requirements
```bash
pip install -r requirements.txt
```


### Configuration :  
copy the `.env-sample` to `.env` file
then put your personal config in the `.env` file like the sample.
```bash
cp .env-sample .env
``` 

### Run :  
finally run the server
```bash
./manage.py runserver
```
