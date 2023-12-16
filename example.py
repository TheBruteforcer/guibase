# Import module
from guibase import *
# Create 2 functions to set as Failure / Success actions
def Faliure(msg): # msg is required.
    print('Cannot Login / Signup.')
    print(msg)
def Success():
    print('Signed in successfully.')

guilogin(key = "! HTTP FIREBASE KEY !", title = "Sign in to complete", whensuccess=Success, whenfaliure=Faliure, lang = 'en')
guiregister(key = "! HTTP FIREBASE KEY !", title = "Sign up to complete", whensuccess=Success, whenfaliure=Faliure, lang = 'en')