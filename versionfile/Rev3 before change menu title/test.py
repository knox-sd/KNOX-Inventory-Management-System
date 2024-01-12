from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Qatar')
        
def update_clock(self):
        raw_TS = datetime.now(IST)
        date_now = raw_TS.strftime("%d %b %Y")
        time_now = raw_TS.strftime("%H:%M:%S %p")
        label_date.config(text = date_now)
        self.root.self.lbl_clock.config(text = time_now)
        self.lbl_clock.after(1000, update_clock)
update_clock()
