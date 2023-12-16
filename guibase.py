from tkinter import *
from tkinter import messagebox
from openvpn_api import *
import requests
def guilogin(key, title, whensuccess, whenfaliure, lang='en', theme ='dark'):
    app = Tk()
    app.resizable(0,0)
    app.geometry('350x500')
    app.title(title)
    if theme == 'dark':
        app.config(background='#092635')
        if lang == 'ar':
            mainlabel = Label(app , text = "تـسـجـيـل الـدخـول" , font=('Cairo Medium', 30), bg ='#092635', fg='White')
            mainlabel.pack(pady=37)
            emaillabel = Label(app, text = 'البـريد الإلكـتروني' , background='#092635', foreground= 'White', font = ('Cairo Medium' , 12))
            emaillabel.pack(anchor = 'e' , padx = 30, pady = (0,3))
            emailentry = Entry(app, width=30, font = ('Cairo Medium', 12))
            emailentry.pack(padx = (10,0))
            passwordlabel = Label(app, text = 'كلمة المرور' , background='#092635', foreground= 'White', font = ('Cairo Medium' , 12))
            passwordlabel.pack(anchor = 'e' , padx = 30, pady = (15,3))
            passwordentry = Entry(app, width=30, font = ('Cairo Medium', 12))
            passwordentry.pack(padx = (10,0))
        elif lang == 'en':
            mainlabel = Label(app , text = "Login" , font=('Cairo Medium', 35), bg ='#092635', fg='White')
            mainlabel.pack(pady=37)
            emaillabel = Label(app, text = 'Email' , background='#092635', foreground= 'White', font = ('Cairo Medium' , 12))
            emaillabel.pack(anchor = 'w' , padx = 30, pady = (0,3))
            emailentry = Entry(app, width=30, font = ('Cairo Medium', 12))
            emailentry.pack(padx = (10,0))
            passwordlabel = Label(app, text = 'Password' , background='#092635', foreground= 'White', font = ('Cairo Medium' , 12))
            passwordlabel.pack(anchor = 'w' , padx = 30, pady = (15,3))
            passwordentry = Entry(app, width=30, font = ('Cairo Medium', 12))
            passwordentry.pack(padx = (10,0))
        else:
            print(f'Unknown language choice {lang} - You Can Use ( "ar" / "en" )')
    elif theme == 'light':
        app.config(background='#EBF3E8')
        if lang == 'ar':
            mainlabel = Label(app , text = "تـسـجـيـل الـدخـول" , font=('Cairo Medium', 30), bg ='#EBF3E8', fg='Black')
            mainlabel.pack(pady=37)
            emaillabel = Label(app, text = 'البـريد الإلكـتروني' , background='#EBF3E8', foreground= 'Black', font = ('Cairo Medium' , 12))
            emaillabel.pack(anchor = 'e' , padx = 30, pady = (0,3))
            emailentry = Entry(app, width=30, font = ('Cairo Medium', 12), background='#E4E4D0')
            emailentry.pack(padx = (10,0))
            passwordlabel = Label(app, text = 'كلمة المرور' , background='#EBF3E8', foreground= 'black', font = ('Cairo Medium' , 12))
            passwordlabel.pack(anchor = 'e' , padx = 30, pady = (15,3))
            passwordentry = Entry(app, width=30, font = ('Cairo Medium', 12), background='#E4E4D0')
            passwordentry.pack(padx = (10,0))
        elif lang == 'en':
            mainlabel = Label(app , text = "Login" , font=('Cairo Medium', 35), bg ='#EBF3E8', fg='Black')
            mainlabel.pack(pady=37)
            emaillabel = Label(app, text = 'Email' , background='#EBF3E8', foreground= 'black', font = ('Cairo Medium' , 12))
            emaillabel.pack(anchor = 'w' , padx = 30, pady = (0,3))
            emailentry = Entry(app, width=30, font = ('Cairo Medium', 12), background='#E4E4D0')
            emailentry.pack(padx = (10,0))
            passwordlabel = Label(app, text = 'Password' , background='#EBF3E8', foreground= 'black', font = ('Cairo Medium' , 12))
            passwordlabel.pack(anchor = 'w' , padx = 30, pady = (15,3))
            passwordentry = Entry(app, width=30, font = ('Cairo Medium', 12), background='#E4E4D0')
            passwordentry.pack(padx = (10,0))
        else:
            print(f'Unknown language choice {lang} - You Can Use ( "ar" / "en" )')
    def sigin():
            signinpaylod = {
                'email' : emailentry.get(),
                'password' : passwordentry.get(),
                'returnSecureToken' : 'false'
            }
            signinresponse = (requests.post(f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={key}', data= signinpaylod)).json()
            if 'error' in signinresponse:
                a = signinresponse
                whenfaliure(a)
            elif 'registered' in signinresponse:
                a = "DONE"
                whensuccess()
            else:
                a = f'UNEXPECTED ERROR - "{signinresponse}"'
    sign = Button(app, command=sigin, text="Sign In", height=15, width=30,font=('Cairo Medium', 15), background='#1B4242', foreground = 'White').pack(pady=50, padx=50)
    app.mainloop()


#############################################################################


def guiregister(key, title, whensuccess, whenfaliure, lang='en', theme = 'dark'):
    app = Tk()
    app.resizable(0,0)
    app.geometry('350x500')
    app.title(title)
    if theme == 'dark':
        app.config(background='#092635')
        if lang == 'ar':
            mainlabel = Label(app , text = "تـسـجـيـل الإشـتـراك" , font=('Cairo Medium', 30), bg ='#092635', fg='White')
            mainlabel.pack(pady=37)
            emaillabel = Label(app, text = 'البـريد الإلكـتروني' , background='#092635', foreground= 'White', font = ('Cairo Medium' , 12))
            emaillabel.pack(anchor = 'e' , padx = 30, pady = (0,3))
            emailentry = Entry(app, width=30, font = ('Cairo Medium', 12))
            emailentry.pack(padx = (10,0))
            passwordlabel = Label(app, text = 'كلمة المرور' , background='#092635', foreground= 'White', font = ('Cairo Medium' , 12))
            passwordlabel.pack(anchor = 'e' , padx = 30, pady = (15,3))
            passwordentry = Entry(app, width=30, font = ('Cairo Medium', 12))
            passwordentry.pack(padx = (10,0))
        elif lang == 'en':
            mainlabel = Label(app , text = "Register" , font=('Cairo Medium', 35), bg ='#092635', fg='White')
            mainlabel.pack(pady=37)
            emaillabel = Label(app, text = 'Email' , background='#092635', foreground= 'White', font = ('Cairo Medium' , 12))
            emaillabel.pack(anchor = 'w' , padx = 30, pady = (0,3))
            emailentry = Entry(app, width=30, font = ('Cairo Medium', 12))
            emailentry.pack(padx = (10,0))
            passwordlabel = Label(app, text = 'Password' , background='#092635', foreground= 'White', font = ('Cairo Medium' , 12))
            passwordlabel.pack(anchor = 'w' , padx = 30, pady = (15,3))
            passwordentry = Entry(app, width=30, font = ('Cairo Medium', 12))
            passwordentry.pack(padx = (10,0))
        else:
            print(f'Unknown language choice {lang} - You Can Use ( "ar" / "en" )')
    elif theme == 'light':
        app.config(background='#EBF3E8')
        if lang == 'ar':
            mainlabel = Label(app , text = "تـسـجـيـل الـدخـول" , font=('Cairo Medium', 30), bg ='#EBF3E8', fg='Black')
            mainlabel.pack(pady=37)
            emaillabel = Label(app, text = 'البـريد الإلكـتروني' , background='#EBF3E8', foreground= 'Black', font = ('Cairo Medium' , 12))
            emaillabel.pack(anchor = 'e' , padx = 30, pady = (0,3))
            emailentry = Entry(app, width=30, font = ('Cairo Medium', 12), background='#E4E4D0')
            emailentry.pack(padx = (10,0))
            passwordlabel = Label(app, text = 'كلمة المرور' , background='#EBF3E8', foreground= 'black', font = ('Cairo Medium' , 12))
            passwordlabel.pack(anchor = 'e' , padx = 30, pady = (15,3))
            passwordentry = Entry(app, width=30, font = ('Cairo Medium', 12), background='#E4E4D0')
            passwordentry.pack(padx = (10,0))
        elif lang == 'en':
            mainlabel = Label(app , text = "Login" , font=('Cairo Medium', 35), bg ='#EBF3E8', fg='Black')
            mainlabel.pack(pady=37)
            emaillabel = Label(app, text = 'Email' , background='#EBF3E8', foreground= 'black', font = ('Cairo Medium' , 12))
            emaillabel.pack(anchor = 'w' , padx = 30, pady = (0,3))
            emailentry = Entry(app, width=30, font = ('Cairo Medium', 12), background='#E4E4D0')
            emailentry.pack(padx = (10,0))
            passwordlabel = Label(app, text = 'Password' , background='#EBF3E8', foreground= 'black', font = ('Cairo Medium' , 12))
            passwordlabel.pack(anchor = 'w' , padx = 30, pady = (15,3))
            passwordentry = Entry(app, width=30, font = ('Cairo Medium', 12), background='#E4E4D0')
            passwordentry.pack(padx = (10,0))
        else:
            print(f'Unknown language choice {lang} - You Can Use ( "ar" / "en" )')
    def sigin():
            signinpaylod = {
                'email' : emailentry.get(),
                'password' : passwordentry.get(),
                'returnSecureToken' : 'false'
            }
            signinresponse = (requests.post(f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={key}', data= signinpaylod)).json()
            if 'error' in signinresponse:
                a = signinresponse
                whenfaliure(a)
            elif 'email' in signinresponse:
                whensuccess()
            else:
                a = f'UNEXPECTED ERROR - "{signinresponse}"'
    sign = Button(app, command=sigin, text="Sign Up", height=15, width=30,font=('Cairo Medium', 15), background='#1B4242', foreground = 'White').pack(pady=50, padx=50)
    app.mainloop()