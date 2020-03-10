import urllib.request
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import PIL.Image
import PIL.ImageTk
from tkinter import Label
import io

root = tk.Tk()


raw_data = urllib.request.urlopen(r"https://maps.googleapis.com/maps/api/staticmap?size=600x400&path=enc%3Ayws{HvcqAAc@?EKs@ORkA|BfBtCL^FX_@f@q@|@eCzCk@h@i@^aAj@a@TCDKn@Gf@]pDWbCq@lG_@tCi@dDo@lD_AfFiC|OqA|H_BpKqDfWcAvIK~@g@fGeAbMi@nIyAnRQbCQjDGvACdG?x@H`ELv@RbBBDDLBZA^ERMTc@lBSt@KjBUlEItBMtOC|F@rDFrC\xF^zE`@|EF`@PdEDjCEbHEjBIbCGZ[zGq@dOMpDAdC?`CPhJ`@|AB@FJF\C`@OTIDKAIEEEw@rA}@nA]Vg@Fu@DaBN&key=YOUR_API_KEY").read()
#print(raw_data)
im = PIL.Image.open(io.BytesIO(raw_data))
image = PIL.ImageTk.PhotoImage(im)
label1 = Label(root, image=image)
label1.grid()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
