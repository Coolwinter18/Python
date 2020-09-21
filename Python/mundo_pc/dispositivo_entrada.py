class DispositivoEntrada:
    
    def __init__(self, marca, tipo_entrada):
        #Atributos de tipo protected (accesibles desde una subclase)
        self._marca = marca
        self._tipo_entrada = tipo_entrada