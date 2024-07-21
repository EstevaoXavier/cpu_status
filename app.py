# para corrigir o problema do ttk.meter
from PIL import Image
Image.CUBIC = Image.BICUBIC
# importações
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import psutil
import platform

def fazer_analise():
        info_disco = psutil.disk_usage('/')
        info_ram = psutil.virtual_memory()

        meter_memory.configure(amountused = f'{info_disco.used / (1024**3):.2f}')
        meter_ram.configure(amountused = f'{info_ram.used / (1024**3):.2f}')
        print('Memorias Visualizadas')
        print(psutil.sensors_battery)
        
#definição do app
app = ttk.Window(themename="cosmo")
app.title("CPU STATUS")
app.geometry("400x240")
frame = ttk.Frame(app)
frame.grid(row=0, column=0, padx=66, pady=10)
app.resizable(width=False, height=False)


#  Métrica do Disco
info_disco = psutil.disk_usage('/')
label_memoria = ttk.Label(app, text='Disco e RAM')

meter_memory = ttk.Meter(
    frame,
    metersize=120,
    padding=0,
    amountused=0,
    amounttotal= f"{info_disco.total / (1024**3):.2f}",
    metertype="full",
    textright="GB",
    subtext=f"Máximo: {info_disco.total / (1024**3):.2f}GB",
    subtextfont= f"-size 6",
    textfont="-size 11 -weight bold",
    interactive=False,
    bootstyle='primary',
)

# Métrica da RAM
info_ram = psutil.virtual_memory()
meter_ram = ttk.Meter(
    frame,
    metersize=120,
    padding=20,
    amountused=0,
    amounttotal= f"{info_ram.total / (1024**3):.2f}",
    metertype="full",
    textright="RAM",
    subtext=f"Máximo: {info_ram.total / (1024**3):.2f}GB",
    subtextfont= f"-size 6",
    textfont="-size 11 -weight bold",
    interactive=False,
    bootstyle="info",
)

# Janela
label_memoria.grid(row=0, column=0, padx=0, pady=0, sticky='n')

meter_memory.grid(row=1, column=0, padx=0, pady=10, sticky='w')
meter_ram.grid(row=1, column=1, padx=0, pady=10, sticky='e')

button_att = ttk.Button(app, text="ATUALIZAR", command=fazer_analise)
button_att.grid(row=2, column=0, padx=0, pady=5, sticky="ew")

app.mainloop()