class chess:
    def _init_(self):
        self.board = Board()
        self.color = 
        self.turn = 


    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col,

        if self._turn_ == "Blanco":
            self._turn_ == "Negro":
        else:    


class board:
    def _init_(self):
        self._posittions_ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self._posittions_.append(col) 
        self._posittions_[0][0] = torre ("Negra")
        self._posittions_[0][7] = torre ("Negra")
        self._posittions_[7][7] = torre ("Blanca")
        self._posittions_[7][0] = torre ("Blanca")   

class torre():
    def _init_(self, color):
        self.__color = color 

class peon():
     def _init_(self, color):
        self.__color = color