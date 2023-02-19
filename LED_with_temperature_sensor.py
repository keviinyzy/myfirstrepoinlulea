#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import glob
import time
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


host_name = '192.168.0.102'  # IP Address of Raspberry Pi
host_port = 8000


def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(18, GPIO.OUT)


def getTemperature():
    temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
    return temp
    
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

class MyServer(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        print(os.getcwd())
        html = '''
           <html>
           <body 
            style="width:960px; margin: 20px auto;">
           <h1>Welcome to my Raspberry Pi</h1>
           <div>
           <img src="img/Hermes.png" alt="Hermes" />
           </div>
           <section class="vh-100">
  <div class="container py-5 h-100">

    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-md-8 col-lg-6 col-xl-4">

        <h3 class="mb-4 pb-2 fw-normal">Check the weather forecast</h3>

        <div class="input-group rounded mb-3">
          <input type="search" class="form-control rounded" placeholder="City" aria-label="Search"
            aria-describedby="search-addon" />
          <a href="#!" type="button">
            <span class="input-group-text border-0 fw-bold" id="search-addon">
              Check!
            </span>
          </a>
        </div>

        <div class="mb-4 pb-2">
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1"
              value="option1" checked />
            <label class="form-check-label" for="inlineRadio1">Celsius</label>
          </div>

          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2"
              value="option2" />
            <label class="form-check-label" for="inlineRadio2">Farenheit</label>
          </div>
        </div>

        <div class="card shadow-0 border">
          <div class="card-body p-4">

            <h4 class="mb-1 sfw-normal">New York, US</h4>
            <p class="mb-2">Current temperature: <strong>5.42°C</strong></p>
            <p>Feels like: <strong>4.37°C</strong></p>
            <p>Max: <strong>6.11°C</strong>, Min: <strong>3.89°C</strong></p>

            <div class="d-flex flex-row align-items-center">
              <p class="mb-0 me-4">Scattered Clouds</p>
              <i class="fas fa-cloud fa-3x" style="color: #eee;"></i>
            </div>

          </div>
        </div>

      </div>
    </div>

  </div>
</section>
           <p>The temperature is {:.1f} degrees celsius and {:.1f} degrees farenheit </p>
           <form action="/" method="POST">
               Turn LED :
               <input type="submit" name="submit" value="On">
               <input type="submit" name="submit" value="Off">
           </form>
           
           </body>
           </html>
        '''.format(read_temp()[0], read_temp()[1])
        temp = getTemperature()
        self.do_HEAD()
        self.wfile.write(html.format(temp[5:]).encode("utf-8"))

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        post_data = post_data.split("=")[1]

        setupGPIO()

        if post_data == 'On':
            GPIO.output(18, GPIO.HIGH)
        else:
            GPIO.output(18, GPIO.LOW)

        print("LED is {}".format(post_data))
        self._redirect('/')  # Redirect back to the root url


# # # # # Main # # # # #

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
