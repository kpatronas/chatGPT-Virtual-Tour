# chatGPT-Virtual-Tour
A toy application that uses chatgpt to extract information from device extracted longitudes and latitudes and provide a short tour of the place and a video from youtube
## How to run this
install all needed libraries from the py file, i feel to lazy at the moment to write a requirements.txt
then you need to provide your openai key to line 25 of the script
finally: 
```
chmod +x ./tour.py
./tour.py
```
if the script starts without errors open from your browser tour.html and press the tour me button. should ask for geolocation and soon after will pop a the chatgpt answer and a video

Note: geolocation from an ip other than localhost and 127.0.0.* requires https..
