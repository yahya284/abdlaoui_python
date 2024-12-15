import os
from flask import Flask, request

app = Flask(__name__)

# Dossier pour sauvegarder les fichiers
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Aucun fichier trouvé', 400
    file = request.files['file']
    if file.filename == '':
        return 'Aucun fichier sélectionné', 400
    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)
    return 'Fichier reçu et sauvegardé', 200

if __name__ == '__main__':
    app.run(debug=True)
