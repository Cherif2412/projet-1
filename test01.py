import pyautogui
import time

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
time.sleep(15)  # Augmenter si nécessaire pour permettre à Word de se lancer complètement
pyautogui.press('enter')

# Coller le texte ou l'image capturée dans Word
pyautogui.hotkey('ctrl', 'v')
