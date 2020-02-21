#''' This is the date and time script, bock will pull from this '''

import datetime

class Date_Time():

    def get_date_time(self):
        time_now = datetime.datetime.now().time().strftime('%H:%M')  # hour in 24h format
        today = datetime.date.today()
        date = today.strftime('%B %d, %Y')
        day_of_week = today.strftime('%A')
        date_dict = {
            'time': time_now,
            'date': date,
            'day': day_of_week
        }
        return date_dict