<h1 id="toc_0">E7029E</h1>

<h2 id="toc_1">Week 1</h2>

<h3 id="toc_2">16 Jan</h3>

<p>Met Up with Jan to discuss on the scope of the Project. The basic fundamental of Internet Of Things (IOT) was explained in detail and STM32L4S5 Discovery Kit was handed to us. The first task was to establish a connection within a local network such that the STM32 LED could be controlled by a browser that is connected within the same network as STM32.</p>

<h3 id="toc_3">17 - 19 Jan</h3>

<p>Since Tera Term was not supported by Mac, I had to install PuTTY. To install PuTTY, the following code was inserted into the terminal.</p>

<blockquote>
<p>sudo port install putty</p>
</blockquote>

<p>Before a PuTTY terminal was opened, there are serveral parameters that had to be set on the PuTTY. Changing the connection to Serial with a speed of 115200. Identification of the port is needed and the command would be</p>

<blockquote>
<p>ls /dev/tty.usb*</p>
</blockquote>

<p>Upon setting the correct parameters, SSID and Password are entered in the terminal for connection to the network. A IP address would then be displayed onto the terminal, with this IP address. The LED lightbulb on the STM32 could be controlled locally in the network.</p>

<h3 id="toc_4">19-22 Jan</h3>

<p>Since we have sucefussfully set up the connection locally we would then proceed to pass the data to an device that is not connected locally. Amazon Web Service (AWS) is a platform where data can be sent through SM32 via MQTT publish/subscribe. An AWS account was created to create a &quot;thing&quot; so that we could have a Certificate key and a private key. In the video guide, MBed online compiler was used to compile and build the program into SM32. Mbed online compiler was discontinued last year and the alternative would be KEIL studio online compiler. However, as I am using a MBP without an USB port and KEIL studio does not support a USB to Type C adapter. I downloaded Mbed studio and there was an example of code to connect to AWS. Unfortunately, connection was not established even after data like aws endpoint, certificate key, private key and ssid was entered. Further troubleshooting are to be done.</p>

<h2 id="toc_5">Week 2</h2>

<h3 id="toc_6">23 Jan</h3>

<p>Since I got stucked for the connection with MQTT using Mbed. There is another alternative method     to get connected to the AWS. There is a function pack for IoT sensor node with telemetry and device control applications for AWS cloud provided by the official stm website. It provides a detailed step-by-step guide to establish the connection.</p>

<p>Before I could move onto the next step, the previous program have to be removed from STM32. Unlike any previous board that I have previously used (reset could be done by holding the reset button). I found a way that a factory reset could be done through STMCubeProgrammer. After following though the guide from STM website we were able establish a connection between STM32 and STM Telemetry to display real time data.</p>

<h3 id="toc_7">24-25 Jan</h3>

<p>Attempted to establish a connection link between FreeRTOS with AWS IoT. https://docs.aws.amazon.com/freertos/latest/userguide/freertos-prereqs.html#freertos-configure
Problem faced:</p>

<ol>
<li>Unable to import freertos from github to Mbed studio due to libiary issues</li>
<li>Tried to import freertos from github to STMIDE with the aid of the guide to change the setting in IDE and still unable to establish connection.</li>
</ol>

<h3 id="toc_8">26-27 Jan</h3>

<p>Familiasation with the STMIDE interface, tried out blinky to set GPIO pin 5 to blink within a specific time interval.</p>

<h2 id="toc_9">Week 3</h2>

<h3 id="toc_10">30 Jan</h3>

<p>Get familiar with Raspberry Pi and set up a connection between the raspberry pi and laptop using VNC viewer.</p>

<h3 id="toc_11">31-1 Feb</h3>

<p>Install node red into Raspberry Pi, using a node, we were able to display the temperature onto the node-red dashboard.</p>

<h3 id="toc_12">2-3 Feb</h3>

<p>Using node-red mqtt to publish a topic and configuring the mqtt to aws by inserting the certificate, private key and CA root into the setting. Then using AWS to subscribe to a topic. We will then inject data into mqtt to AWS.</p>

<h3 id="toc_13">4-5 Feb</h3>

<p>In order to store data, we would need a database. We have found out that mySQL offers this service. Downloaded XAMPP to run a SQL database.</p>

<p>In the SQL database, we have set up a table of infomation to be received from node-red. Currently we are still trying to establish a connection between SQL node in node-red to MySQL databse.</p>

<h2 id="toc_14">Week 4</h2>

<h3 id="toc_15">6-7 Feb</h3>

<p>Met up with Jan on Monday morning to discuss on how we could implement temperature sensor with the Raspberry Pi. We were given a temperature sensor, resistor, breadbaord and wires for the connection between the sensor and Raspberry Pi. The connection steps are as follows:</p>

<ol>
<li> First, connect the 3v3 pin from the Pi to the positive rail and a ground pin to the ground rail on the breadboard.</li>
<li> Now place the temperaturesensor onto the breadboard.</li>
<li>Place a 4.7k resistor between the positive lead and the output lead of the sensor.</li>
<li> Place a wire from the positive lead to the positive 3v3 rail.</li>
<li> Place a wire from the output lead back to pin #4 (Pin #7 if using physical numbering) of the Raspberry Pi.</li>
<li>Place a wire from the ground lead to the ground rail.</li>
</ol>

<p>After the hardware has been set up, we will now proceed to the software portion. In the terminal,</p>

<blockquote>
<p>sudo nano /boot/config.txt</p>
</blockquote>

<p>Add dtoverlay=w1-gpio into the file under audio then we will save it then following by rebooting the Raspberry Pi</p>

<blockquote>
<p>sudo reboot</p>
</blockquote>

<p>After the Raspberry Pi has been rebooted, we will ensure that the correct modules are loaded by</p>

<blockquote>
<p>sudo modprobe w1-gpio
sudo modprobe w1-therm</p>
</blockquote>

<p>We will then change the devices directory and use ls to see the folders and files in the directory</p>

<blockquote>
<p>cd /sys/bus/w1/devices</p>

<p>ls</p>
</blockquote>

<p>We will then change the numbering after cd to the ls command. While in the directory, we will run</p>

<blockquote>
<p>Cat w1_slave</p>
</blockquote>

<p>With the command above it will include data but it might be hard for user to read.</p>

<p>We will then clone the python script from github by</p>

<blockquote>
<p>git clone https://github.com/pimylifeup/temperature_sensor.git</p>
</blockquote>

<p>By opening up the directory and running the python script we would be able to retrive and display real time temperature in the terminal.</p>

<h3 id="toc_16">8-9 Feb</h3>

<p>In order to control receive information/data that is not within a local network, we will set up a flask. A flask is a web applcation framework written in Python. When the python script has been executed we could access the webpage simply by entering the ip address of the Raspberry Pi into the web browser.</p>

<p>In this portion, we have set up a hardware connection such that the positive of the LED is connected to the pin 18 of the Raspberry Pi. We would be able to control the Raspberry Pi GIPO via HTTP webserver. The project that we clone is</p>

<blockquote>
<p>https://github.com/davidrazmadzeExtra/RaspberryPi<em>HTTP</em>LED</p>
</blockquote>

<p>By changing the ip address in the python code, and starting the flask, we would be able to control the LED via pin 18 in the web browser.</p>

<h3 id="toc_17">10-11 Feb</h3>

<p>As we can display the real time value temperature from the temperature sensor to the terminal, we will now attempt to pass the temperature value to the webpage. Hence by modication of the webserver flask code and temperature sensor code, we were able to display the temperature and control the LED on the web browser.</p>

<h2 id="toc_18">Week 5</h2>

<h3 id="toc_19">14 Feb</h3>

<p>Understanding the concept of how GIT works. Learning how to push files from the command terminal to the GIT Repository.</p>

<p>We will cd into our foler then</p>

<blockquote>
<p>git init</p>
</blockquote>

<p>To add repository</p>

<blockquote>
<p>git remote add origin https://github.com/keviinyzy/myfirstrepoinlulea.git</p>
</blockquote>

<p>To check the status of the git we will use, by running this command we will get current status of the git</p>

<blockquote>
<p>git status</p>
</blockquote>

<p>Usually a new file added will be displayed untraced in the display terminal. So we have to add the file to be added before commiting it to git</p>

<blockquote>
<p>git add <file name></p>
</blockquote>

<p>Upon adding the file the git is now ready to be commited. The commit message will be displayed in the git website for the description of the file</p>

<blockquote>
<p>git commit -m &#39;<commit message>&#39;</p>
</blockquote>

<p>Once it is commited the file is ready to be pushed to the repository. After running the command, enter the credentials of your git account</p>

<blockquote>
<p>git push origin master</p>
</blockquote>

<h3 id="toc_20">15 Feb</h3>

<p>Attempt to control the servo motor via the webserver. A servo motor consist of three wires. 5V power, signal and ground. We will connect the signal to pin 11. A servo motor works by sendind Pulse Width Modulation (PWN) through the signal wire.
By using a code we found online. we were able to control the servo motor by sliding the slider in the webpage.</p>

<h3 id="toc_21">16 Feb - 17 Feb</h3>

<p>Attempted to incorporate the servo motor code with the existing code that we worked on so that the user could control LED, servo motor and view the temperature at the same time.</p>

<h3 id="toc_22">18 Feb</h3>

<p>Improving on the UI on the webserver by adding background colours, changing fonts size, types of buttons to beautify the webpage.</p>
