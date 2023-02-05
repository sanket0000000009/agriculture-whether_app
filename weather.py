import tkinter as tk
import requests
import time
import random

def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    api1 = "https://api.ambeedata.com/latest/by-city?city="+city+"&x-api-key=13d68e42ce7c19f2e2ff4792c51c2f40b0239084d0396609ccdee1f20d259427"
    json_data1=requests.get(api1).json()
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
   # soid_status=json_data1['stations']['aqiInfo']['pollutant']
    soil_status = json_data1['stations'][0]['aqiInfo']['category']
    soil_CO = json_data1['stations'][0]['aqiInfo']['pollutant']
    soil_CO1 = json_data1['stations'][0]['aqiInfo']['concentration']
    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset + "\n" + "soil catagory:" + str(soil_status) + "\n" + "soil pollutant:" + str(soil_CO) + "\n" + "soil concentration:" + str(soil_CO1)
    label1.config(text = final_info)
    label2.config(text = final_data)
mycolor = '#%02x%02x%02x' % (225, 225, 0)  # set your favourite rgb color
mycolor2 = '#40E0D0'  # or use hex if you prefer
canvas = tk.Tk()
canvas.configure(bg=mycolor)
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()