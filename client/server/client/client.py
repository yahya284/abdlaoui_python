import requests

def send_file(file_path):
    """Envoie un fichier audio ou vidéo au serveur."""
    url = 'http://127.0.0.1:5000/upload'
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (file_path, file, 'application/octet-stream')}
            response = requests.post(url, files=files)
            if response.status_code == 200:
                print(response.json())
            else:
                print(f"Erreur : {response.status_code} - {response.json()}")
    except FileNotFoundError:
        print(f"Fichier non trouvé : {file_path}")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == '__main__':
    # Spécifiez le chemin de l'audio ou de la vidéo à envoyer
    file_path = 'C:\\Users\\pcexp\\Desktop\\summer_24\\1.mp4'  # Exemple de chemin à remplacer
    send_file(file_path)
