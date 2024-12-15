import tkinter as tk
from tkinter import filedialog, messagebox
import requests

def send_file():
    # Ouvre une boîte de dialogue pour sélectionner le fichier
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3"), ("Video Files", "*.mp4")])
    if file_path:
        if file_path.endswith(('.mp3', '.mp4')):
            with open(file_path, 'rb') as file:
                files = {'file': file}
                url = "http://127.0.0.1:5000/upload"
                response = requests.post(url, files=files)
                if response.status_code == 200:
                    messagebox.showinfo("Succès", "Fichier envoyé avec succès.")
                else:
                    messagebox.showerror("Erreur", "Erreur lors de l'envoi du fichier.")
        else:
            messagebox.showerror("Erreur", "Seuls les fichiers audio (mp3) et vidéo (mp4) sont autorisés.")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Envoyer un fichier")

# Ajouter un bouton pour sélectionner et envoyer le fichier
button = tk.Button(root, text="Choisir un fichier", command=send_file)
button.pack(pady=20)

# Lancer l'application Tkinter
root.mainloop()
