import requests

url = "http://107.23.160.88:5000/car_price_predict"

try:
    r = requests.post(url, json = {"symboling": 2,"normalized-losses": 164,"wheel-base": 99.8,"make": "audi","fuel-type": "gas","aspiration": "std","num-of-doors": "four","body-style": "sedan","drive-wheels": "fwd","engine-location": "front","length": 176.60,"width": 66.20,"height": 54.30,"curb-weight": 2337,"engine-type": "ohc","num-of-cylinders": "four","engine-size": 109, "fuel-system": "mpfi","bore": 3.19,"stroke": 3.40,"compression-ratio": 10,"horsepower": 102,"peak-rpm": 5500,"city-mpg": 24,"highway-mpg": 30})
    print(r.text)
    if r.text == "[12815.2]":
        print("Test successful")
        exit(0)
    else:
        print("Test failed")
        exit(1)    
except Exception as e:
    print("Test failed")
    print("The exception is: ", e)
    exit(1)

