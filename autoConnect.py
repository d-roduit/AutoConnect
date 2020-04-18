from InternetBot import *
from tkinter import *
from credentials import credentials


def showSuccessMessage():
    labelStatut['text'] = 'Program ran successfully'

def connect(site, username, password):
    driver = InternetBot()
    driver.connectOn(site, username = username, password = password)
    showSuccessMessage()

window = Tk()

window.title('AutoConnect by Droduit')
window.iconbitmap(r'.\\autoConnect.ico')
window.geometry("250x200")

button1 = Button(window, text = 'Facebook', command = lambda: connect('facebook', username = credentials['facebook']['username'], password = credentials['facebook']['password']), pady = 5, padx = 5)
button2 = Button(window, text = 'Instagram', command = lambda: connect('instagram', username = credentials['instagram']['username'], password = credentials['instagram']['password']), pady = 5, padx = 5)

button1.pack(padx = 10, pady = 10)
button2.pack(padx = 10, pady = 10)

labelStatut = Label(window, text = 'Aucun action n\'a encore été lancée')
labelStatut.pack(pady = 2)

window.mainloop()
