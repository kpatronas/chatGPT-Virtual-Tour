# chatGPT-Virtual-Tour
A toy application that uses chatgpt to extract information from device extracted longitudes and latitudes and provide a short tour of the place and a video from youtube
## How to run this
install all needed libraries from the py file, i feel to lazy at the moment to write a requirements.txt

Important: then you need to provide your openai key to line 25 of the script

finally: 
```
chmod +x ./tour.py
./tour.py
```
if the script starts without errors open from your browser tour.html and press the tour me button. should ask for geolocation and soon after will pop a the chatgpt answer and a video

Note: geolocation rights from a browser using an ip other than 127.0.0.* or localhost requires https..
