import subprocess
import os

def ouvrir_word():
    try:
        # Chemin vers l'application Word (pour Windows)
        word_path = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
        
        # Vérifie si le chemin existe
        if os.path.exists(word_path):
            # Ouvre l'application Word
            subprocess.Popen([word_path])
            print("Microsoft Word est ouvert avec succès.")
        else:
            print("Le chemin spécifié pour Word n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    ouvrir_word()
