class Jogo:
    def __init__(self, desenvolvedora, nome, preco, estoque, plataforma, publicadora):
        self._desenvolvedora = desenvolvedora
        self._nome = nome
        self._preco = preco
        self._estoque = estoque
        self._plataforma = plataforma
        self._publicadora = publicadora
    
    # Getters
    def get_desenvolvedora(self):
        return self._desenvolvedora
    
    def get_nome(self):
        return self._nome
    
    def get_preco(self):
        return self._preco
    
    def get_estoque(self):
        return self._estoque
    
    def get_plataforma(self):
        return self._plataforma
    
    def get_publicadora(self):
        return self._publicadora
    
    # Setters
    def set_desenvolvedora(self, desenvolvedora):
        self._desenvolvedora = desenvolvedora
    
    def set_nome(self, nome):
        self._nome = nome
    
    def set_preco(self, preco):
        self._preco = preco
    
    def set_estoque(self, estoque):
        self._estoque = estoque
    
    def set_plataforma(self, plataforma):
        self._plataforma = plataforma
    
    def set_publicadora(self, publicadora):
        self._publicadora = publicadora