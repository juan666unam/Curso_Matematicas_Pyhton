from tkinter import Tk, Label, Entry


# Diccionario
inventario = {"CPU" : 50, "Monitor" : 70 , 
                  "Mouse" : 100, "Teclado" : 40, "Webcam" : 20,
                  "USB" : 120, "Laptop" : 43}


# Creo la ventana
ventana = Tk()
ventana.title("Inventario")
ventana.eval('tk::PlaceWindow . center')

#Creo los elementos a poner en la ventana 
texto = Label(ventana,  font=('Helvetica 15 bold'), text = "Tipo de Producto: ")
entrada = Entry(ventana, font=('Helvetica 15 bold'),background='#ffa533', width=30)
score = Label(ventana,font=('Helvetica 15 bold'),text='')


# Pongo los elementos en la ventana
texto.pack(side = 'left', padx=(20,5), pady=10)
entrada.pack(side='left', padx=(2,20), pady=10)
score.pack(side='bottom', padx= (0,10),pady=(100,5))

# Toma el dato de la entrada después de dar enter
# e imprime el nombre en consola
def mi_entrada(event):
    producto = entrada.get()
    resultado = inventario.get(producto, -1)
    if resultado != -1:
        score.configure(text = "Existencia: "+ str(resultado))
    else:
        score.configure(text = "Ingresa un nombre de producto válido")    

# Enlaza el recuadro de entrada con dar Return    
entrada.bind('<Return>', mi_entrada)

ventana.mainloop()