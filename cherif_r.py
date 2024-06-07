import pyautogui
import time

# Attendre un moment pour te laisser le temps de basculer sur le bon écran si nécessaire
time.sleep(2)

# Simuler la pression des touches Windows + R
pyautogui.hotkey('win', 'r')

# Attendre un court instant pour s'assurer que la boîte de dialogue "Exécuter" est ouverte
time.sleep(1)

# Taper "cmd" dans la boîte de dialogue "Exécuter"
pyautogui.write('cmd')

# Simuler la pression de la touche "Entrée"
pyautogui.press('enter')

# Attendre un moment pour s'assurer que l'invite de commande est ouverte
time.sleep(2)

# Taper la commande dans l'invite de commande netsh wlan>show profile
pyautogui.write('netsh wlan show profile')

# Simuler la pression de la touche "Entrée"
pyautogui.press('enter')

# Attendre un court instant pour s'assurer que la commande s'est exécutée
time.sleep(1)

# Sélectionner tout le texte dans l'invite de commande
pyautogui.hotkey('ctrl', 'a')

# Copier le texte sélectionné
pyautogui.hotkey('ctrl', 'c')

# Attendre un court instant pour s'assurer que le texte est copié
time.sleep(1)

# Fermer l'invite de commande
pyautogui.hotkey('alt', 'f4')

# Attendre un court instant pour s'assurer que l'invite de commande est fermée
time.sleep(2)

# Simuler la pression des touches Windows + R pour ouvrir la boîte de dialogue "Exécuter" à nouveau
pyautogui.hotkey('win', 'r')

# Attendre un court instant pour s'assurer que la boîte de dialogue "Exécuter" est ouverte
time.sleep(1)

# Taper "winword" pour ouvrir Microsoft Word
pyautogui.write('winword')
pyautogui.press('enter')

# Attendre un moment pour que Microsoft Word s'ouvre
time.sleep(5)

# Simuler la pression de la touche "Entrée" pour créer un nouveau document vierge
pyautogui.press('enter')

# Attendre que Microsoft Word s'ouvre
time.sleep(5)  # Ajuster ce délai si nécessaire

# Coller le texte dans Word
pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
pyautogui.hotkey('alt', 'f4')

import pyautogui
import time

# Attendre un moment pour te laisser le temps de basculer sur le bon écran si nécessaire
time.sleep(2)

# Appuyer sur la flèche droite une fois
pyautogui.press('right')

# Simuler la pression de la touche "Entrée"
pyautogui.press('enter')

# Attendre un moment pour te laisser le temps de basculer sur le bon écran si nécessaire
time.sleep(2)

# Simuler la pression des touches Windows + R pour ouvrir la boîte de dialogue "Exécuter"
pyautogui.hotkey('win', 'r')

# Attendre un court instant pour s'assurer que la boîte de dialogue "Exécuter" est ouverte
time.sleep(1)

# Taper le nom de l'application "photos" pour l'application Photos
pyautogui.write('chrome')

# Simuler la pression de la touche "Entrée" pour lancer l'application
pyautogui.press('enter')

time.sleep(2)
pyautogui.write('octomiro')
pyautogui.press('enter')
time.sleep(10)


# Simuler la pression des touches Windows pour ouvrir la camera"Exécuter"
pyautogui.hotkey('win')

# Attendre un court instant pour s'assurer que la boîte de dialogue "Exécuter" est ouverte
time.sleep(2)

# Taper le nom de l'application "photos" pour l'application Photos
pyautogui.write("camera")
time.sleep(2)
pyautogui.press('enter')
time.sleep(10)


# Simuler la combinaison de touches 'Win + Shift + S' pour capturer une partie de l'écran
pyautogui.hotkey('printscreen')

# Attendre quelques secondes pour que l'utilisateur fasse la capture d'écran
time.sleep(5)

# Simuler 'Win + R' pour ouvrir la boîte de dialogue "Exécuter"
pyautogui.hotkey('win', 'r')
time.sleep(2)

# Taper 'winword' pour ouvrir Microsoft Word
pyautogui.write('winword')
time.sleep(2)
pyautogui.press('enter')

# Attendre que Microsoft Word s'ouvre
time.sleep(10)  # Augmenter si nécessaire pour permettre à Word de se lancer complètement
pyautogui.press('enter')

# Coller le texte ou l'image capturée dans Word
pyautogui.hotkey('ctrl', 'v')







