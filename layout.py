
import tkinter
import Analisacnpj
from sqlalchemy import TEXT
current_arquivo=[None]

root=tkinter.Tk()
root.resizable=False
TopFrame=tkinter.Frame(root, width=100)
TopText=tkinter.Label(TopFrame, text='ANALISA CNPJ')
TopText.pack()
TopFrame.pack(side='top')
MidFrame=tkinter.Frame(root)
MidTopFrame=tkinter.Frame(MidFrame)
MidTopFrameLabel=tkinter.Label(MidTopFrame, text='DIGITE O NOME DA PLANILHA')
MidtopFrameInput=tkinter.Entry(MidTopFrame, width=15)
MidTopFrameLabel.pack(side=tkinter.LEFT)
MidtopFrameInput.pack(side=tkinter.LEFT)
MidDownFrame=tkinter.Frame(MidFrame)
ResultFrame=tkinter.Frame(root)
label_aviso=tkinter.Label(MidDownFrame, text='PLANILHA JÁ ABERTA')
MidDownFrameButton=tkinter.Button(MidDownFrame, text='Buscar', command=lambda: Analisacnpj.analisa(MidtopFrameInput.get(), ResultFrame))
ResultFrame.pack(side='bottom')
MidDownFrameButton.pack()
MidTopFrame.pack()
MidDownFrame.pack()
MidFrame.pack()


root.mainloop()