from pogoda import get_location_id, get_location_weather, location_name

import tkinter
root = tkinter.Tk()

woeid = get_location_id(location_name)
show = get_location_weather(woeid)

a_label = tkinter.Label(master=root, text=show)
a_label.pack()
root.mainloop()

#odpala się przez pogoda_gui.py <miejscowość> - defaultowo miescowość to Warsaw