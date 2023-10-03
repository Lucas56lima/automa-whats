from tkinter import *
from tkinter import filedialog
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
from tkinter import messagebox



def envia_mensagem(diretorio,texto_inserido):

    mensagem = texto_inserido.get('1.0',END)

    contatos_df = pd.read_excel(str(diretorio))
    contatos_df.head()

    navegador = webdriver.Chrome()
    navegador.get("https://web.whatsapp.com/")

    while len(navegador.find_elements(By.ID,"side")) < 1:
        time.sleep(1)
    
    for i, valida in enumerate(contatos_df['já enviado']):
        if valida != "v":
            pessoa = contatos_df.loc[i,'nome']
            numero = contatos_df.loc[i,'numero']      
        
            mensagem_inserida = urllib.parse.quote(f"{pessoa} , {mensagem}")
            link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem_inserida}"
            navegador.get(link)
        else:
            messagebox.showwarning(message="Mensagem já enviada para contatos selecionados.")
    
        while len(navegador.find_elements(By.ID,"side")) < 1:
            time.sleep(5)
                               
        navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER)   
        time.sleep(10)

        

    messagebox.showinfo(message="Mensagem enviada! ")         



janela = Tk()
janela.geometry('500x300')
janela.configure(background="#FFFAFA")
janela.title("Automação Whatsapp")
texto = Label(janela, text="Arquivo selecionado: ",anchor='w')
texto.place(x=10,y=30,width=150,height=20)
# texto.grid(column=0, row=0, padx=0, pady=0)

upload_arquivo = filedialog.askopenfilename()

local_arquivo = Label(janela, text= upload_arquivo,anchor='w')
local_arquivo.place(x=10,y=80,width=300,height=20)

texto_mensagem = Label(janela,text='Insira uma mensagem: ',anchor='w')
texto_mensagem.place(x=10,y=120,width=150,height=20)

inserir_mensagem = Text(janela)
inserir_mensagem.place(x=10,y=150,width=300,height=100) 


botao = Button(janela,default='normal', text="Enviar mensagem", command=lambda: envia_mensagem(upload_arquivo,inserir_mensagem))
botao.place(x=10,y=230,width=120,height=30)



janela.mainloop()


   
    