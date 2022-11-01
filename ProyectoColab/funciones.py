class funciones:
    #Funcion que recibe una lista de numeros y regresa la cantidad de pares
    #Asignado a: FRIDA SOFIA ORTIZ SILVA
    def funcionContarPares(self, lista):

        num_pares = []
        cont = 0
        for n in lista:
            if n % 2 == 0:
                cont = cont + 1
        return cont

    #Funcion que recibe una lista de numeros y regresa la cantidad de negativos
    #Asignado a: GALVAN DE LA RIVA MIGUEL ANGEL
    def funcionContarNegativos(self, lista):

        count = len(list(filter(lambda x: (x < 0), lista)))
        return count

        #Funcion que recibe una palabra y regresa la palabra inversa en mayusculas
    #Asignado a: HERNANDEZ MARTINEZ DAVID
    def funcionInversaMayus(self, palabra):
        resultado= ''
        for c in range(len(palabra) -1, -1, -1):
            resultado += palabra[c]
        return resultado.upper()

    #Funcion que recibe una palabra y regresa la cantidad de vocales
    #Asignado a: HERNANDEZ RAMIREZ DIEGO FRANCISCO
    def funcionVocales(self, palabra):
        voc = 0
        for c in palabra:
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
                voc = voc + 1
        return voc
    #Funcion que recibe una nombre completo y regresa las iniciales
    #Asignado a: HERNANDEZ SEGURA LUIS ENRIQUE
    def funcionIniciales(self, nombre):
        prueba = nombre.split(" ")
        # prueba= np.array(nombre.split(" "))
        inicialesNombre = ""
        for x in prueba:
            inicialesNombre = inicialesNombre + x[0]
        return inicialesNombre

    #Funcion que recibe una lista de numeros y regresa verdadero si esta ordenada o falso si no
    #Asignado a: HERNANDEZ TINOCO LUZ ELIZABETH
    def funcionEsOrden(self, lista):
        pass

    #Funcion que recibe una lista de numeros y regresa verdadero si hay duplicados o falso si no
    #Asignado a: MARTINEZ PUENTE DANIEL ALEJANDRO
    def funcionHayDuplicados(self, lista):
        dup = [x for i, x in enumerate(lista) if i != lista.index(x)]
        if dup.__len__() > 0:
            return True
        else:
            return False

    #Funcion que recibe una lista de elemento y regresa en una lista el tipo de dato, usar la funcion type()
    #Asignado a: RODRIGUEZ CERDA JOSE ALFREDO
    def funcionListaTipos(self, lista):
        try:
            for l in lista:
                a = lista[0]
                b = lista[1]
                c = lista[2]
                d = lista[3]
            array = [type(a), type(b), type(c), type(d)]
            return array
        except:
            for l in lista:
                a = lista[0]
                b = lista[1]
            array = [type(a), type(b)]
            return array
    #Funcion que recibe un valor y si no esta dentro del rango lo ajusta a los limites
    #Asignado a: RODRIGUEZ GAYTAN JAIME ABRAHAM
    def funcionAjustar(self, valor, inferior, superior):
        if (valor >= inferior and valor <= superior):
            print("El valor dado esta dentro del rango")
        else:
            print("El valor dado no esta dentro del rango y se ha ajustado al limite")
            valor = inferior
        return valor

    #Funcion que recibe una lista de numeros y regresa en una lista los negativos, neutros y positivos
    #Asignado a: ROJAS LÓPEZ ALEJANDRO JOSUE
    def funcionListaClasificados(self, lista):
        pos = 0
        neu = 0
        neg = 0
        for num in lista:
            if num < 0:
                neg += 1

            elif num == 0:
                neu +=1

            else:
                pos +=1
        array = [neg, neu, pos]
        return array
    #Funcion que recibe una lista de numeros y regresa en una lista de cada numero multiplicado por un Multiplicando
    #Asignado a: SALAZAR SUAREZ ISRAEL
    def funcionListaMultiplos(self, lista, multiplicando):
        pass

    #Funcion que recibe dos listas de numeros y regresa en una lista combinada de manera intercalada
    #Asignado a: VILLALPANDO ALDERETE CELESTE GRISEL
    def funcionCombinarListas(self, lista1, lista2):
        ListaFinal = []
        Tam1 = len(lista1)
        Tam2 = len(lista2)

        if Tam1 >= Tam2:
            TamMax = Tam1
        else:
            TamMax = Tam2

        for i in range(0, TamMax):
            if i < Tam1:
                ListaFinal.append(lista1[i])
            if i < Tam2:
                ListaFinal.append(lista2[i])
        return ListaFinal
        print(ListaFinal)



