# para corrigir o problema do ttk.meter
from PIL import Image
Image.CUBIC = Image.BICUBIC
# importações
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import psutil

def verificar_temperatura():
    try:
        # Obtém as temperaturas dos sensores
        temps = psutil.sensors_temperatures()
        
        # Verifica se há sensores de temperatura disponíveis
        if not temps:
            print("Nenhum sensor de temperatura disponível.")
        else:
            # Itera sobre os sensores encontrados
            for name, entries in temps.items():
                print(f"Sensores de {name}:")
                for entry in entries:
                    print(f"  {entry.label or name}: {entry.current}°C (high={entry.high}°C, critical={entry.critical}°C)")
    except AttributeError:
        # Caso a funcionalidade não seja suportada pelo sistema
        print("A funcionalidade de sensores de temperatura não é suportada no seu sistema.")

#definição do app
app = ttk.Window(themename="cosmo")
app.title("CPU STATUS")
app.geometry("400x700")
frame = ttk.Frame(app)
frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")


info_disco = psutil.disk_usage('/')

label_memoria = ttk.Label(app, text='Disco e RAM')

meter_memory = ttk.Meter(
    frame,
    metersize=120,
    padding=20,
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

label_memoria.grid(row=0, column=0, padx=5, pady=5, sticky='n')

meter_memory.grid(row=1, column=0, padx=5, pady=5, sticky='n')
meter_memory.configure(amountused = f'{info_disco.used / (1024**3):.2f}')

meter_ram.grid(row=1, column=1, padx=5, pady=5, sticky='n')
meter_ram.configure(amountused = f'{info_ram.used / (1024**3):.2f}')

# Separador
separator = ttk.Separator(app, orient='horizontal',)
separator.grid(row=3, column=0, padx=5, pady=5, sticky='n',)



app.mainloop()