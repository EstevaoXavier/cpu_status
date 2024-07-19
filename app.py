#para corrigir o problema do ttk.meter
from PIL import Image
Image.CUBIC = Image.BICUBIC
#importações
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#definição do app
app = ttk.Window(themename="cosmo")
app.title("CPU STATUS")
app.geometry("800x400")

meter = ttk.Meter(
    metersize=80,
    padding=30,
    amountused=0,
    amounttotal= f"2000",
    metertype="semi",
    subtext="miles per hour",
    subtextfont= f"-size 6",
    textfont="-size 11 -weight bold",
    interactive=True,
)
meter.pack()

meter.configure(amountused = 70)

meter.configure(subtext="loading...")

app.mainloop()