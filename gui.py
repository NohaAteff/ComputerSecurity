from tkinter import *
from tkinter import ttk,messagebox
import ttkbootstrap as tb
import ceasar
import mono
import playfair
import rsa
import main as des
import viginere
# import RC4 
# import Row_transposition as row
# themename='numanalysis'
window = tb.Window()
window.title('Computer Security')
font =(10)
# fontObj = tb.font=(10)
ciphertextLabel = Label(window,text='cipher Text:',font=(8))
cipherEntry = tb.Entry(window,width=45,font=font)
plaintextLabel = Label(window,text='Plain Text:',font=(8))
plainEntry = tb.Entry(window,width=45,bootstyle='dark',font=(8))
plainlabel = Label(window,text ='Plain Text',font=(10))
plainlabel.grid(row=1,column=1)
ptEntry = tb.Entry(window, width=45, bootstyle='dark',font=(8))
ptEntry.grid(row=1,column=2,columnspan=2,padx=10)
keylabel = Label(window,text ='Key',font=(10))
keyEntry = tb.Entry(window, width=45, bootstyle='dark',font=(8))
p = Label(window,text='p',font=(10))
q = Label(window,text='q',font=(10))
c = Label(window,text='c',font=(10))
pEntry = tb.Entry(window,width=35, bootstyle='dark')
qEntry = tb.Entry(window,width=35, bootstyle='dark')
cEntry = tb.Entry(window,width=35, bootstyle='dark')
line = Label(window,text='-------------------------------------------------',font=(12))
def selected(event):
    keyEntry.delete(0,'end')
    # if chooseMethod.get() == 'Ceasar Cipher' or chooseMethod.get() == "MonoAlphabetic cipher" or chooseMethod.get() == 'Play fair cipher' or chooseMethod.get() == 'Polyalphabetic (viginere)' or chooseMethod.get() == 'Row Transposition' or chooseMethod.get() == 'RC4':
    #     keylabel.grid(row=5,column=1)
    #     keyEntry.grid(row=5,column=2,columnspan=2)
    if chooseMethod.get() == 'RSA':
        keylabel.destroy()
        keyEntry.destroy()
        p.grid(row=6,column=1)
        q.grid(row=7,column=1)
        c.grid(row=8,column=1)
        pEntry.grid(row=6, column=2, columnspan=2)
        qEntry.grid(row=7, column=2, columnspan=2)
        cEntry.grid(row=8, column=2, columnspan=2)
    elif chooseMethod.get() == 'DES':
        pass
    else:
        keylabel.grid(row=5,column=1)
        keyEntry.grid(row=5,column=2,columnspan=2)
def encrypt():
    line.grid(row=7,column=2,columnspan=3,padx=10,pady=10)
    cipherEntry.delete(0,'end')
    try:
        if chooseMethod.get() == 'Ceasar Cipher':
            a = ceasar.caesar_cipher(ptEntry.get(),int(keyEntry.get()))
            ciphertextLabel.grid(row=8,column=1,padx=(10,0),pady=10)
            cipherEntry.grid(row=8,column=3,padx=(0,150),pady=10)
            cipherEntry.insert(0,a)
        elif chooseMethod.get() == 'MonoAlphabetic cipher':
            print(keyEntry.get())
            a = mono.monoalphabetic_encrypt(ptEntry.get(),str(keyEntry.get()))
            ciphertextLabel.grid(row=8,column=1,padx=(10,0),pady=10)
            cipherEntry.grid(row=8,column=3,padx=(0,150),pady=10)
            cipherEntry.insert(0,a)
        elif chooseMethod.get() == 'Play fair cipher':
            a = playfair.encryptByPlayfairCipher(ptEntry.get(),keyEntry.get())
            ciphertextLabel.grid(row=8,column=1,padx=(10,0),pady=10)
            cipherEntry.grid(row=8,column=3,padx=(0,150),pady=10)
            cipherEntry.insert(0,a)
        elif chooseMethod.get() == 'RSA':
            a = rsa.rsa_encrypt(int(pEntry.get()),int(qEntry.get()),int(cEntry.get()))
            ciphertextLabel.grid(row=8,column=1,padx=(10,0),pady=10)
            cipherEntry.grid(row=8,column=3,padx=(0,150),pady=10)
            cipherEntry.insert(0,a)
        elif chooseMethod.get() == 'DES':
            a,_ = des.encryption(ptEntry.get())
            print(a)
        elif chooseMethod.get() == 'Polyalphabetic (viginere)':
            a = viginere.vigenere_encrypt(ptEntry.get(),keyEntry.get())
            print(a)
            ciphertextLabel.grid(row=8,column=1,padx=(10,0),pady=10)
            cipherEntry.grid(row=8,column=3,padx=(0,150),pady=10)
            cipherEntry.insert(0,a)
        elif chooseMethod.get() == 'Row Transposition':
            pass
            # a = row.row_transposition_encrypt(ptEntry.get(),int(keyEntry.get()))
            # print(a)
        elif chooseMethod.get() == 'RC4':
            pass
            # a = RC4.rc4_encrypt(ptEntry.get(),int(keyEntry.get()))
            # print(a)
    except EXCEPTION as e:
        print(e)
        messagebox.showerror(window,title= 'Exception', message=e)
def decrypt():
    cipherEntry.delete(0,'end')
    # ciphertextLabel.destroy()
    plainEntry.delete(0,'end')
    line.grid(row=7,column=2,columnspan=3,padx=10,pady=10)

    try:
        if chooseMethod.get() == 'Ceasar Cipher':
            a = ceasar.caesar_decipher(ptEntry.get(),int(keyEntry.get()))
            plaintextLabel.grid(row=8,column=1,padx=(10,0),pady=10)
            cipherEntry.grid(row=8,column=3,padx=(0,150),pady=10)
            cipherEntry.insert(0,a)
                
        elif chooseMethod.get() == 'MonoAlphabetic cipher':
            print(keyEntry.get())
            a = mono.monoalphabetic_decrypt(ptEntry.get(),str(keyEntry.get()))
            print(a)
            plaintextLabel.grid(row=8,column=1,padx=(10,0),pady=10)
            cipherEntry.grid(row=8,column=3,padx=(0,150),pady=10)
            cipherEntry.insert(0,a)
        # elif chooseMethod.get() == 'Play fair cipher':
        #     a = playfair.(ptEntry.get(),keyEntry.get())
        #     print(a)
        elif chooseMethod.get() == 'RSA':
            a = rsa.rsa_decrypt(int(pEntry.get()),int(qEntry.get()),int(cEntry.get()))
            print(a)
        elif chooseMethod.get() == 'DES':
            a,_ = des.decryption(ptEntry.get())
            print(a)
        elif chooseMethod.get() == 'Polyalphabetic (viginere)':
            a = viginere.vigenere_decrypt(ptEntry.get(),keyEntry.get())
            print(a)
        elif chooseMethod.get() == 'Row Transposition':
            pass
            # a = row.row_transposition_decrypt(ptEntry.get(),int(keyEntry.get()))
            # print(a)
        elif chooseMethod.get() == 'RC4':
            pass
            # a = RC4.rc4_decrypt(ptEntry.get(),(keyEntry.get()))
            # print(a)
    except EXCEPTION as e:
        print(e)
        messagebox.showerror(e)
options = ['Ceasar Cipher', 'MonoAlphabetic cipher', 'Polyalphabetic (viginere)','Play fair cipher','Row Transposition','RSA','DES','RC4']
chooseMethod = tb.Combobox(window, values=options,width=30)
chooseMethod.bind("<<ComboboxSelected>>",selected)

chooseMethod.grid(row=3,column=2,columnspan=3,padx=10,pady=10)
buttonenc = tb.Button(window,text='encrypt',bootstyle='primary outline',command=encrypt).grid(row=6,column=2,padx=(75,0),pady=10)
buttondec =tb.Button(window,text='Decrypt',bootstyle='warning outline',command=decrypt).grid(row=6,column=3,padx=(0,100),pady=10)
window.mainloop()