Partly Cloudy
=======

A seriously lightweight Python wrapper for the littleBits cloud API.


### Installation
If you've got pip installed, just run `pip install partlycloudy`.

###How to use
* Import the module. `import partlycloudy as cloud`
* Create a Bit object. `bit = cloud.Bit(access_token, device_id)`
* Send output to your bit. `bit.output(power_from_1_to_100, duration_in_milliseconds)`
* Get input from your bit. `print bit.input()`
* Make awesome stuff.
