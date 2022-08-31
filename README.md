# Bitly URL shortener
This command line application is a api client implementation whose purpose is to short links and count clicks on them. The application makes requests to bitly.com
##
before start you have to:
 - register on bitly.com
 - get personal token
 - create .env file on project directory
 - make a record formatted as "TOKEN=YUORTOKEN"
## for install: 
```
git clone https://github.com/SergeyPostnikov/api2
pip install -r requirements.txt

```
## to shorten links:
```
python url_shortener.py <your link>
```
## to count visits on links:
```
python url_shortener.py <your shorten link>
```
