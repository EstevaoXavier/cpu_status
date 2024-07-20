import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def main():
    app = ttk.Window(themename="cosmo")
    app.title("Horizontal Widgets Example")
    app.geometry("400x100")

    # Frame para organizar os widgets horizontalmente
    frame = ttk.Frame(app)
    frame.grid(row=0, column=0, padx=10, pady=10)

    # Widgets horizontais
    label1 = ttk.Label(frame, text="Label 1", bootstyle="success", font=("Helvetica", 12))
    label1.grid(row=0, column=0, padx=5)

    label2 = ttk.Label(frame, text="Label 2", bootstyle="info", font=("Helvetica", 12))
    label2.grid(row=0, column=1, padx=5)

    button = ttk.Button(frame, text="Button", bootstyle="primary")
    button.grid(row=1, column=2, padx=5)

    app.mainloop()

if __name__ == "__main__":
    main()
