mist
=======

A seriously lightweight Python wrapper for the littleBits cloud API.


### Installation
If you've got pip installed, just run `pip install mist`.

###How to use
* Import `mist`.
* Create a Bit object. `bit = mist.Bit(access_token, device_id)`
* Send output to your bit. `bit.output(power_from_1_to_100, duration_in_milliseconds)`
* Make awesome stuff.
