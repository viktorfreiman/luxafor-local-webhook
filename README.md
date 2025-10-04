# Luxafor Local Webhook

Luxafor is very open to open source from want I can read on their website.

Link to their developer page
https://luxafor.helpscoutdocs.com/category/5-software-integrations

I have emailed Luxafor's support for the api that the streamdeck plugin is using but I have not got a response from them about the local api. I took Wireshark for the rescue and now we have the full api. It's faster and works completely offline. Uses the offical software from Luxafor which makes it easy to install via offical stores for locked-down systems. There is no need to sign-up or use their online webhook if data privacy is a concern.

Something is off with sending the http from curl vs python. From curl I get error 301 but with python it just works.

The local_ctrl.py is not a working python file for controlling it. It's just the bare python code you need to kickstart your code to making work.

Pay attention to the right types being used. Luxafor's software does not handle invalid request and will crash if it receives any.

setup.png shows how to set it up

Good luck and just make a issue if there is anything
