from tkinter import *
import feedparser
from PIL import Image, ImageTk
import pyowm
import datetime

xlarge_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18


icon_lookup = {
    '01d': "assets/Sun.png",  # clear sky day
    '01n': "assets/Moon.png",  # clear sky night
    '02d': "assets/PartlySunny.png",  # partly cloudy day
    '02n': "assets/PartlyMoon.png",
    '03d': "assets/Cloud.png",
    '03n': "assets/Cloud.png",
    '09d': "assets/Rain.png",  # rain day
    '09n': "assets/Rain.png",  # rain day
    '10d': "assets/Rain.png",  # rain day
    '10n': "assets/Rain.png",  # rain day
    '11d': "assets/Storm.png",  # thunderstorm
    '11n': "assets/Storm.png",  # thunderstorm
    '13d': "assets/Snow.png",  # snow day
    '13n': "assets/Snow.png",  # snow day
    '50d': "assets/Haze.png",  # fog day
    '50n': "assets/Haze.png",  # fog day
    'wind': "assets/Wind.png",  # wind
    'tornado': "assests/Tornado.png",    # tornado
    'hail': "assests/Hail.png"  # hail
}

class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        # initialize time label
        self.time1 = ''
        self.timeLbl = Label(self, font=('Helvetica', large_text_size), fg="white", bg="black")
        self.timeLbl.pack(side=TOP, anchor=E)
        # initialize day of week
        self.day_of_week1 = ''
        self.dayOWLbl = Label(self, text=self.day_of_week1, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.dayOWLbl.pack(side=TOP, anchor=E)
        # initialize date label
        self.date1 = ''
        self.dateLbl = Label(self, text=self.date1, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.dateLbl.pack(side=TOP, anchor=E)
        self.tick()

    def tick(self):

        time2 = datetime.datetime.now().time().strftime('%H:%M') #hour in 24h format
        today = datetime.date.today()
        date2 = today.strftime('%b %d, %Y')
        day_of_week2 = today.strftime('%A')

        # if time string has changed, update it
        if time2 != self.time1:
            self.time1 = time2
            self.timeLbl.config(text=time2)
        if day_of_week2 != self.day_of_week1:
            self.day_of_week1 = day_of_week2
            self.dayOWLbl.config(text=day_of_week2)
        if date2 != self.date1:
            self.date1 = date2
            self.dateLbl.config(text=date2)
        self.timeLbl.after(200, self.tick)

class Weather(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.temperature = ''
        self.forecast = ''
        self.location = ''
        self.currently = ''
        self.icon = ''
        self.degreeFrm = Frame(self, bg="black")
        self.degreeFrm.pack(side=TOP, anchor=W)
        self.temperatureLbl = Label(self.degreeFrm, font=('Helvetica', xlarge_text_size), fg="white", bg="black")
        self.temperatureLbl.pack(side=LEFT, anchor=N)
        self.iconLbl = Label(self.degreeFrm, bg="black")
        self.iconLbl.pack(side=LEFT, anchor=N, padx=20)
        self.currentlyLbl = Label(self, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.currentlyLbl.pack(side=TOP, anchor=W)
        self.forecastLbl = Label(self, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.forecastLbl.pack(side=TOP, anchor=W)
        self.locationLbl = Label(self, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.locationLbl.pack(side=TOP, anchor=W)
        self.get_weather()

    def get_weather(self):
        owm = pyowm.OWM('6892fc37f53067a561bbac518117974d')
        observation = owm.weather_at_place('luton,GB')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        temp = temp['temp']
        degree_sign = u'\N{DEGREE SIGN}'
        temperature2 = "%s%s" % (temp, degree_sign)
        currently2 = w.get_detailed_status()
        #forecast2 = weather_obj["hourly"]["summary"]
        icon_id = w.get_weather_icon_name()
        icon2 = None
        if icon_id in icon_lookup:
            icon2 = icon_lookup[icon_id]
        if icon2 is not None:
            if self.icon != icon2:
                self.icon = icon2
                image = Image.open(icon2)
                image = image.resize((100, 100), Image.ANTIALIAS)
                image = image.convert('RGB')
                photo = ImageTk.PhotoImage(image)
                self.iconLbl.config(image=photo)
                self.iconLbl.image = photo
        else:
            # remove image
            self.iconLbl.config(image='')
        if self.currently != currently2:
            self.currently = currently2
            self.currentlyLbl.config(text=currently2)
        # if self.forecast != forecast2:
        #     self.forecast = forecast2
        #     self.forecastLbl.config(text=forecast2)
        if self.temperature != temperature2:
            self.temperature = temperature2
            self.temperatureLbl.config(text=temperature2)
        self.after(60000, self.get_weather)

# class News:
#     def get_news():
#         ret_headlines = []
#         feed = feedparser.parse("https://news.google.com/news?ned=gb&output=rss")
#         for post in feed.entries[0:5]:
#             ret_headlines.append(post.title)
#         print(ret_headlines)

class News(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'News' # 'News' is more internationally generic
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.newsLbl.pack(side=TOP, anchor=W)
        self.headlinesContainer = Frame(self, bg="black")
        self.headlinesContainer.pack(side=TOP)
        self.get_headlines()

    def get_headlines(self):
        # remove all children
        for widget in self.headlinesContainer.winfo_children():
            widget.destroy()

        headlines_url = "https://news.google.com/news?ned=gb&output=rss"
        feed = feedparser.parse(headlines_url)

        for post in feed.entries[0:5]:
            headline = NewsHeadline(self.headlinesContainer, post.title)
            headline.pack(side=TOP, anchor=W)
        self.after(60000, self.get_headlines)


class NewsHeadline(Frame):
    def __init__(self, parent, event_name=""):
        Frame.__init__(self, parent, bg='black')

        image = Image.open("assets/Newspaper.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)

        self.iconLbl = Label(self, bg='black', image=photo)
        self.iconLbl.image = photo
        self.iconLbl.pack(side=LEFT, anchor=N)

        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.eventNameLbl.pack(side=LEFT, anchor=N)



class FullscreenWindow:
    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background='black')
        self.topFrame = Frame(self.tk, background = 'black')
        self.bottomFrame = Frame(self.tk, background = 'black')
        self.topFrame.pack(side = TOP, fill=BOTH, expand = YES)
        self.bottomFrame.pack(side = BOTTOM, fill=BOTH, expand = YES)
        self.state = False
        self.toggle_fullscreen()
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)


        # # weather
        # self.weather = Weather(self.topFrame)
        # self.weather.pack(side=LEFT, anchor=N, padx=100, pady=60)
        # # clock
        # self.clock = Clock(self.topFrame)
        # self.clock.pack(side=RIGHT, anchor=N, padx=100, pady=60)
        # # news
        # self.news = News(self.bottomFrame)
        # self.news.pack(side=LEFT, anchor=S, padx=100, pady=60)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"


w = FullscreenWindow()
#News.get_news()
w.tk.mainloop()