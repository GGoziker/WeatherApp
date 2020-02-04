# Runs on Python 2.7
# https://www.youtube.com/watch?v=D8-snVfekto

import Tkinter as tk
import requests # Need this to make API calls

HEIGHT = 500
WIDTH = 600


def get_weather(city):
    print('Test function!\n', city)
    url = 'http://api.openweathermap.org/data/2.5/weather'
    weatherAppAPIKey = 'df900fb9451d18079febbee3db064d87'
    params = {'APPID':weatherAppAPIKey, 'q':city, 'units':'imperial',}

    response = requests.get(url, params=params)
    weatherJson = response.json()
    label['text'] = ('City: %s\nWeather: %s\ntemp: %s\nFeels like: %s\n'
                     % (city,
                        weatherJson['weather'][0]['description'],
                        weatherJson['main']['temp'],
                        weatherJson['main']['feels_like']))

root = tk.Tk()

# Set size of window
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Top frame: search bar
top_frame = tk.Frame(root, bg='#bab3ff', bd=5)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(top_frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(top_frame, text='Get Weather', font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

# Bottom frame: display box
bottom_frame = tk.Frame(root, bg='#bab3ff', bd=5)
bottom_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(bottom_frame, text="", )
label.place(relwidth=1, relheight=1)

root.mainloop()