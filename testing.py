# para corrigir o problema do ttk.meter
from PIL import Image
Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import psutil
import time
import threading

def update_system_info():
    while True:
        info_disco = psutil.disk_usage('/')
        info_ram = psutil.virtual_memory()
        
        meter_memory.configure(amountused=info_disco.used / (1024**3))
        meter_memory.configure(amounttotal=info_disco.total / (1024**3))
        
        meter_ram.configure(amountused=info_ram.used / (1024**3))
        meter_ram.configure(amounttotal=info_ram.total / (1024**3))
        
        time.sleep(1)

app = ttk.Window(themename="cosmo")
app.geometry("400x300")
app.resizable(width=False, height=False)

# Cria um frame centralizado
frame = ttk.Frame(app)
frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# Configura o layout da grid para expandir o frame central
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# Cria Meters para memória e disco no frame
meter_memory = ttk.Meter(frame, subtext="Disco", textright="GB", bootstyle="info", metertype="full")
meter_memory.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

meter_ram = ttk.Meter(frame, subtext="RAM", textright="GB", bootstyle="info", metertype="full")
meter_ram.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# Configura o layout da grid para centralizar os meters no frame
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Inicia a thread para atualizar os dados do sistema
update_thread = threading.Thread(target=update_system_info, daemon=True)
update_thread.start()

app.mainloop()
