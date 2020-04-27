# essential-quotes

essentialQuotes is a project designed to capture outpouring of community support from tweets and web posts and display them on RGB matrices by Klinstifen

My basic purpose is to analyze which, why and how things are used in this project along with the code...

Hardware components

* 4 Adafruit 64x32 RGB Matrix
* 1 Adafruit 5V 10A Power Supply
* 1 Adafruit RGB Matrix Bonnet
* 12 Machine Screw, M3
* 4 Machine Screw, M2.5
* 1 Raspberry Pi 3 Model B
* 1 Flash Memory Card, SD Card
* 1 Adafruit Heat Shrink

Software apps and online services

* Autodesk Fusion 360

Hand tools and fabrication machines

* Multitool, Screwdriver
* 3D Printer (generic)	
* Soldering iron (generic)
* Wire Stripper / Cutter, Full Flush


EssentialQuotes is a project designed to capture outpouring of community support from tweets and simple messages. Received messages are displayed on a chain of 64x32 RGB matrices.

Prerequisites

* Raspberry Pi with Internet access
* PSQL database
* Twitter App
This assumes you have the aforementioned prerequisites and does not go into too much detail regarding their setup. 

Hardware Instructions
It starts like many projects, with a Raspberry Pi (3 to be specific). The project uses four 64x32 RGB matrices chained together, to display the messages to community members.

We begin by fastening two matrices together using a 3D printed bracket and four M3x6mm screws.

Fasten the remaining two matrices together to form one long matrix!

Connect each of the ribbon cables. Pay attention to the notch on the ribbon cable - when correctly seated the red wire should be at the top (the RPi is at the bottom).

Now, connect the power cable. Pay attention to the VCCGNDmarkingsbelow the power cable sockets. The red wire connects to VCC and the black wire connects to GND.

Connect the loose end of the power cable to the terminal block on the Adafruit RGB Matrix Bonnet. Makesurethe cables are plugged all the way into the terminal block and tightly secured.

Plug the power supply into the Adafruit RGB Matrix Bonnet and login to the RPi,

Now that the hardware setup is complete it's time to shift to software.

Software Instructions

Clone the essentialQuote repo withe the following command:

git clone --recursive https://github.com/techahoynyc/essentialQuotes

Create the config.ini with the following format:

[twitter]

TW_NAME = <your twitter screen name>
  
TW_HASH = <your designed hash tag including hash symbol>
  
APP_KEY = <your twitter app API Key>
  
APP_SECRET = <your twitter app API Secret> 
  
ACCESS_TOKEN = <your twitter app Access Token>
  
ACCESS_SECRET = <your twitter app Access Secret>
  
[sql]

HOST = <your PSQL DB hostname>
  
DB = <your PSQL DB name>
  
PORT = 5432 <or your custom PSQL DB port>
  
UN = <your PSQL DB username>
  
PW = <your PSQL DB user's password>

[general]

DEFAULT_MSG = <your default message or instructions>
  
Add showQuotes.py to /etc/rc.local so it will run on boot:

# run essentialQuotes
cd /home/pi/essentialQuotes && sudo python3 showQuotes.py &

Modify cron so getTweet.py runs every five minutes:

*/5 * * * * /usr/local/bin/python3 /home/pi/essentialQuotes/getTweet.py &

Reboot and make sure the code launched successfully.

If nothing appears on the matrices you can verify the code is running by using this command:

ps -aux | grep python

Hardware Installation

Mount the sign in a window or inside on a wall - we chose a window.

Tell everyone about your sign and help spread positive messages to community members!

Helpful Resources
* QRCode Generator - https://www.the-qrcode-generator.com/
* Twitter API Docs - https://developer.twitter.com/en/docs/basics/getting-started
