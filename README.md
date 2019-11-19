# CS5700- Networking Fundamentals Final Project    

This project goes over how to set up your own Rasberry Pi as a cloud server and wireless access point.   
We use the commands laid out in the setup_raspi to setup the raspbi. These instructions go over DHCP, NAT translation, Static IP addressing, and wireless access point set up.     
Then the code laid out in the src directory is a small Django web application that utilizes Bootstrap to allow a user to upload files directly onto the RasberryPi, making the RasbpPi a fully functioning Web Server that serves HTTP requests to the user to display HTML pages and other media. 


| Hardware   | Software      | 
| -------------- |:---------:| 
| Ethernet Cable | PuTTY     |
| Rasberry Pi    | Etcher    |
| MicroSD card   |           |
| Micro USB cable|


### I. Seting up the Rasberry Pi, headlessly. 
In order to set up a Rasberry Pi to be able to work on it, an operating system must be installed.   
There are a variety of [OS](https://www.fossmint.com/operating-systems-for-raspberry-pi/) that can be used to interact with your Rasberry Pi, but we ended up using the one mentioned in the article, [Rasbpian Jessie Lite](http://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2016-09-28/), because of its small size and because we were not in need of a GUI. 

The following project is inspired by following [article](https://learn.adafruit.com/digital-free-library/).
