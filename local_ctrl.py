import requests

headers = {"Content-Type": "application/json", "Authorization": "Bearer luxafor"}

color_data = {
    "on": "#FFFFFF",
    "off": "#000000",
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
    "cyan": "#00FFFF",
    "magenta": "#FF00FF",
}

pattern_data = {
    "trafic_lights": "1",
    "police": "5",
    "random_1": "2",
    "random_2": "3",
    "random_3": "4",
    "random_4": "6",
    "random_5": "7",
    "ranbow": "8",
    "red_flash": "101",
    "green_flash": "102",
    "white_flash": "104",
    "yellow_flash": "105",
    "magenta_flash": "106",
    "cyan_flash": "107",
    "sea": "201",
    "white_wave": "202",
    "synthetic": "203",
}

requests.post("http://127.0.0.1:5383/color", headers=headers, json={"color": "#FFFF00"})

requests.post("http://127.0.0.1:5383/brightness", headers=headers, json={"brightness": 0})
requests.post("http://127.0.0.1:5383/pattern/play", headers=headers, json={"id": 5})
requests.post("http://127.0.0.1:5383/pattern/play", headers=headers, json={"id": pattern_data["trafic_lights"]})

requests.post("http://127.0.0.1:5383/brightness/increase", headers=headers, json={"step": 10})
requests.post("http://127.0.0.1:5383/brightness/decrease", headers=headers, json={"step": 10})