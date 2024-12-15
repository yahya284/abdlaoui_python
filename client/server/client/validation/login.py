import tkinter as tk
from tkinter import filedialog, messagebox
import requests

# Fonction de connexion simple
def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "password":  # Exemple de vérification
        messagebox.showinfo("Connexion", "Connexion réussie !")
        root.withdraw()  # Masquer la fenêtre de connexion
        send_file_window()  # Ouvrir la fenêtre pour envoyer le fichier
    else:
        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

def send_file_window():
    file_window = tk.Tk()
    file_window.title("Envoyer un fichier")

    def send_file():
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3"), ("Video Files", "*.mp4")])
        if file_path:
            with open(file_path, 'rb') as file:
                files = {'file': file}
                url = "http://127.0.0.1:5000/upload"
                response = requests.post(url, files=files)
                if response.status_code == 200:
                    messagebox.showinfo("Succès", "Fichier envoyé avec succès.")
                else:
                    messagebox.showerror("Erreur", "Erreur lors de l'envoi du fichier.")

    button = tk.Button(file_window, text="Choisir un fichier", command=send_file)
    button.pack(pady=20)
    file_window.mainloop()

# Créer la fenêtre de connexion
root = tk.Tk()
root.title("Connexion")

label_username = tk.Label(root, text="Nom d'utilisateur")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Mot de passe")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

login_button = tk.Button(root, text="Se connecter", command=login)
login_button.pack(pady=20)

root.mainloop()
