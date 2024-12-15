import os
from flask import Flask, request

# Initialisation de l'application Flask
app = Flask(__name__)

# Chemin de stockage des fichiers
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)  # Crée le dossier 'uploads' s'il n'existe pas

@app.route('/upload', methods=['POST'])
def upload_file():
    """Endpoint pour recevoir les fichiers audio/vidéo."""
    if 'file' not in request.files:
        return {'message': 'Aucun fichier trouvé dans la requête'}, 400
    
    file = request.files['file']
    if file.filename == '':
        return {'message': 'Aucun fichier sélectionné'}, 400
    
    # Enregistrement du fichier dans le dossier 'uploads'
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return {'message': f'Fichier {file.filename} téléchargé avec succès !'}, 200

if __name__ == '__main__':
    print("Le serveur Flask démarre...")
    app.run(host='0.0.0.0', port=5000, debug=True)
