Partly Cloudy
=============

A ridiculously lightweight wrapper for the cloudBit API.


Installation
------------

Installing Partly Cloudy is really easy - just run

`$ pip install partlycloudy`

in a terminal.

Tutorial
--------

Partly Cloudy makes interfacing with your cloudBit really easy.

Import Partly Cloudy.

`>>> import partlycloudy as cloud`

Create a Bit object.

`>>> bit = cloud.Bit(YOUR_ACCESS_TOKEN, YOUR_DEVICE_ID)`

To send output from your bit, call

`>>> bit.output(power_from_1_to_100, duration_in_ms)`

Getting input is a little bit different. If you want realtime input, use the `bit.stream()` generator.

```
for pct in bit.stream():
  print pct # input, on a scale of 1 to 100
```

This is considered 'best practice'. If you need a single value for input, use `bit.input()`.

Contribute
----------
Ideas? Bugs? Bug fixes? Great!

- Issue Tracker: http://github.com/technoboy10/partly-cloudy/issues
- Source Code: http://github.com/technoboy10/partly-cloudy

License
-------
Partly Cloudy is licensed under the MIT license.
