# Raspberry bike speedmeter




## Startup

Connect the rpi into your local network, then access via ssh:
``` ssh pi@192.168.1.254 ```

Enter in the project directory:

``` cd rpi-bike-speedmeter ```

And start the software:

``` sudo python speedmeter.py ```

Access to the speedmeter via HTTP get request:

``` http://192.168.1.254:6061 ```
