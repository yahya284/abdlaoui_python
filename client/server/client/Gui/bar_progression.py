import tkinter as tk
from tkinter import filedialog
import requests
from tqdm import tqdm

def send_file():
    # Ouvre une boîte de dialogue pour sélectionner le fichier
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3"), ("Video Files", "*.mp4")])
    if file_path:
        with open(file_path, 'rb') as file:
            files = {'file': file}
            url = "http://127.0.0.1:5000/upload"
            
            # Utiliser tqdm pour suivre la progression
            with tqdm(total=len(file.read()), unit='B', unit_scale=True) as pbar:
                response = requests.post(url, files=files, stream=True)
                if response.status_code == 200:
                    print("Fichier envoyé avec succès.")
                else:
                    print("Erreur lors de l'envoi du fichier.")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Envoyer un fichier")

# Ajouter un bouton pour sélectionner et envoyer le fichier
button = tk.Button(root, text="Choisir un fichier", command=send_file)
button.pack(pady=20)

# Lancer l'application Tkinter
root.mainloop()
