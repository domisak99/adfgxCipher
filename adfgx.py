import sys
import random
import math
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, uic
 
qtCreatorFile = "adfgx.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class PlayFair(QMainWindow, Ui_MainWindow):


    def Create_table_ADFGX(self):
        abcd = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
        conversion_array = [[0] * 5 for x in range(5)]
        subs_key=self.subs_klic.toPlainText()
        subs_key = subs_key.upper();
        subs_key = subs_key.replace('W', 'V')
        subs_key = subs_key.replace(' ', '')
        abc=''.join(random.sample(abcd,len(abcd)))
        for x in range(5):
            for y in range(5):
                if len(subs_key):
                    conversion_array[x][y] = subs_key[0]
                    abc = abc.replace(subs_key[0], '')
                    subs_key = subs_key.replace(subs_key[0], '', -1)
                else:
                    conversion_array[x][y] = abc[0]
                    abc = abc[1:]

        self.vypis_tabulky.setColumnCount(5)
        self.vypis_tabulky.setRowCount(5)
        tab=""
        for i in range(5):
            for j in range(5):
                self.vypis_tabulky.setItem(i, j, QTableWidgetItem((conversion_array[i][j])))
                length=len(tab)
                tab=tab[:length]+conversion_array[i][j]

        self.tab_text.setText(tab)

        return conversion_array

    def Create_table_ADFGVX(self):
        abcd = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        conversion_array = [[0] * 6 for x in range(6)]
        subs_key=self.subs_klic.toPlainText()
        subs_key = subs_key.upper();
        subs_key = subs_key.replace(' ', '')
        abc=''.join(random.sample(abcd,len(abcd)))
        for x in range(6):
            for y in range(6):
                if len(subs_key):
                    conversion_array[x][y] = subs_key[0]
                    abc = abc.replace(subs_key[0], '')
                    subs_key = subs_key.replace(subs_key[0], '', -1)
                else:
                    conversion_array[x][y] = abc[0]
                    abc = abc[1:]

        self.vypis_tabulky.setColumnCount(6)
        self.vypis_tabulky.setRowCount(6)
        tab=""
        for i in range(6):
            for j in range(6):
                self.vypis_tabulky.setItem(i, j, QTableWidgetItem((conversion_array[i][j])))
                length=len(tab)
                tab=tab[:length]+conversion_array[i][j]

        self.tab_text.setText(tab)
        
        return conversion_array

    def Create_dectable_ADFGX(self):
        abc = self.tab_text.toPlainText()
        conversion_array = [[0] * 5 for x in range(5)]
        for x in range(5):
            for y in range(5):
                conversion_array[x][y] = abc[0]
                abc = abc[1:]

        self.vypis_tabulky.setColumnCount(5)
        self.vypis_tabulky.setRowCount(5)
        tab=""
        for i in range(5):
            for j in range(5):
                self.vypis_tabulky.setItem(i, j, QTableWidgetItem((conversion_array[i][j])))
                length=len(tab)
                tab=tab[:length]+conversion_array[i][j]

        self.tab_text.setText(tab)

        return conversion_array

    def Create_dectable_ADFGVX(self):
        abc = self.tab_text.toPlainText()
        conversion_array = [[0] * 6 for x in range(6)]
        for x in range(6):
            for y in range(6):
                conversion_array[x][y] = abc[0]
                abc = abc[1:]

        self.vypis_tabulky.setColumnCount(6)
        self.vypis_tabulky.setRowCount(6)
        tab=""
        for i in range(6):
            for j in range(6):
                self.vypis_tabulky.setItem(i, j, QTableWidgetItem((conversion_array[i][j])))
                length=len(tab)
                tab=tab[:length]+conversion_array[i][j]

        self.tab_text.setText(tab)
        
        return conversion_array

    def encrypt_ADFGX(self):
        adfgx = ["A", "D", "F", "G", "X"]
        conversion_array=self.Create_table_ADFGX()
        perm_key=self.perm_klic.toPlainText()
        perm_key=perm_key.upper()
        message=self.vstup.toPlainText()
        message=message.upper()                           
        message=message.replace("W", "V")            
        message = message.replace(" ", "XMEZERAX")

        

        if message.isalnum()==False:
            self.vystup.setText("Byli zadany nepovolene znaky (Povolene jsou pouze A..Z a 1..9)")
            return
        
        message = message.replace("Ě", "E")
        message = message.replace("Š", "S")
        message = message.replace("Č", "C")
        message = message.replace("Ř", "R")
        message = message.replace("Ž", "Z")
        message = message.replace("Ý", "Y")
        message = message.replace("Á", "A")
        message = message.replace("Í", "I")
        message = message.replace("É", "E")
        message = message.replace("Ť", "T")
        message = message.replace("Ď", "D")
        message = message.replace("Ň", "N")
        message = message.replace("Ú", "U")
        message = message.replace("Ů", "U")

        message = message.replace("0", "PBA")
        message = message.replace("1", "BFB")
        message = message.replace("2", "CDC")
        message = message.replace("3", "DCD")
        message = message.replace("4", "YUE")
        message = message.replace("5", "EGF")
        message = message.replace("6", "GHG")
        message = message.replace("7", "HGH")
        message = message.replace("8", "RJI")
        message = message.replace("9", "JIJ")
        encrypt_message=""

        #Prevod z pismen na AD,FG atd..
        for i in range(len(message)):
            ch=''
            a=''
            b=''
            ch=message[i]
            Fchar=self.FindPosition(conversion_array, ch, 5)
            a=adfgx[Fchar[0]]
            b=adfgx[Fchar[1]]
            str1=a+b
            length=len(encrypt_message)
            encrypt_message = encrypt_message[:length]+str1

        #vytvoreni poli a definovani velikosti    
        length_array=math.ceil(len(encrypt_message)/len(perm_key))
        trans_array = [[0] * len(perm_key) for x in range(length_array)]
        end_array = [[0] * len(perm_key) for x in range(length_array)]
        length_y=len(perm_key)

        #vlozeni zakodovane zpravy do pole
        for x in range(length_array):
            for y in range(length_y):
                if len(encrypt_message):
                    trans_array[x][y] = encrypt_message[0]
                    encrypt_message=encrypt_message[1:]
                else:
                    continue


        end_message=''

        #serazeni slova podle abecedy (vrati cisla)
        word=self.sortind(perm_key)

        #prehazeni sloupcu v tabulce
        for y in range(length_y):
            for x in range(length_array):
                if(trans_array[x][y]==0):
                    continue
                else:
                    seq=word[y];
                    end_array[x][seq]=trans_array[x][y]

                    
        #Vlozeni listu do stringu a pridani mezery
        for y in range(length_y):
            for x in range(length_array):
                if(end_array[x][y]==0):
                    continue
                else:
                    length=len(end_message)
                    end_message=end_message[:length]+end_array[x][y]
            length2=len(end_message)
            end_message=end_message[:length2]+ " "

        
        #vypis    
        self.vystup.setText(str(end_message))
        #self.vystup.setText(message)

    def encrypt_ADFGVX(self):
        adfgx = ["A", "D", "F", "G", "V", "X"]
        conversion_array=self.Create_table_ADFGVX()
        perm_key=self.perm_klic.toPlainText()
        perm_key=perm_key.upper()
        message=self.vstup.toPlainText()
        message=message.upper()                           
        message=message.replace("W", "V")            

        message = message.replace(" ", "XMEZERAX")

        if message.isalnum()==False:
            self.vystup.setText("Byli zadany nepovolene znaky (Povolene jsou pouze A..Z a 1..9)")
            return
        
        message = message.replace("Ě", "E")
        message = message.replace("Š", "S")
        message = message.replace("Č", "C")
        message = message.replace("Ř", "R")
        message = message.replace("Ž", "Z")
        message = message.replace("Ý", "Y")
        message = message.replace("Á", "A")
        message = message.replace("Í", "I")
        message = message.replace("É", "E")
        message = message.replace("Ť", "T")
        message = message.replace("Ď", "D")
        message = message.replace("Ň", "N")
        message = message.replace("Ú", "U")
        message = message.replace("Ů", "U")

        message = message.replace("0", "PBA")
        message = message.replace("1", "BFB")
        message = message.replace("2", "CDC")
        message = message.replace("3", "DCD")
        message = message.replace("4", "YUE")
        message = message.replace("5", "EGF")
        message = message.replace("6", "GHG")
        message = message.replace("7", "HGH")
        message = message.replace("8", "RJI")
        message = message.replace("9", "JIJ")
        encrypt_message=""

        #Prevod z pismen na AD,FG atd..
        for i in range(len(message)):
            ch=''
            a=''
            b=''
            ch=message[i]
            Fchar=self.FindPosition(conversion_array, ch, 6)
            a=adfgx[Fchar[0]]
            b=adfgx[Fchar[1]]
            str1=a+b
            length=len(encrypt_message)
            encrypt_message = encrypt_message[:length]+str1


        #vytvoreni poli a definovani velikosti    
        length_array=math.ceil(len(encrypt_message)/len(perm_key))
        trans_array = [[0] * len(perm_key) for x in range(length_array)]
        end_array = [[0] * len(perm_key) for x in range(length_array)]
        length_y=len(perm_key)

        #vlozeni zakodovane zpravy do pole
        for x in range(length_array):
            for y in range(length_y):
                if len(encrypt_message):
                    trans_array[x][y] = encrypt_message[0]
                    encrypt_message=encrypt_message[1:]
                else:
                    continue


        end_message=''

        #serazeni slova podle abecedy (vrati cisla)
        word=self.sortind(perm_key)

        #prehazeni sloupcu v tabulce
        for y in range(length_y):
            for x in range(length_array):
                if(trans_array[x][y]==0):
                    continue
                else:
                    seq=word[y];
                    end_array[x][seq]=trans_array[x][y]

                    
        #Vlozeni listu do stringu a pridani mezery
        for y in range(length_y):
            for x in range(length_array):
                if(end_array[x][y]==0):
                    continue
                else:
                    length=len(end_message)
                    end_message=end_message[:length]+end_array[x][y]
            length2=len(end_message)
            end_message=end_message[:length2]+ " "

        
        #vypis    
        self.vystup.setText(str(end_message))
        #self.vystup.setText(message)

    def decrypt_ADFGX(self):
        adfgx = ["A", "D", "F", "G", "X"]
        conversion_array=self.Create_dectable_ADFGX()
        perm_key=self.perm_klic.toPlainText()
        perm_key=perm_key.upper()
        encrypt_message=self.vstup.toPlainText()
        encrypt_message=encrypt_message.upper()
        encrypt_message = encrypt_message.replace(" ", "_") 

        length_y=len(perm_key)
        length_array=math.ceil(len(encrypt_message)/len(perm_key))

        input_array = [[0] * length_y for x in range(length_array)]
        trans_array = [[0] * length_y for x in range(length_array)]
        op=encrypt_message[0]

        #vlozeni stringu do pole !!!!!!!
        for y in range(length_y):
           for x in range(length_array):
                if (encrypt_message[0]=="_"):
                    encrypt_message=encrypt_message[1:]
                    break
                else:
                    if len(encrypt_message):
                        input_array[x][y] = encrypt_message[0]
                        encrypt_message=encrypt_message[1:]
                    else:
                        continue
                
        word=self.sortind(perm_key)

        #prehozeni sloupcu v poli
        for y in range(length_y):
            for x in range(length_array):
                seq=word[y];
                trans_array[x][y]=input_array[x][seq]


        #vlozeni sifrz do stringu
        en_message=""
        for x in range(length_array):
            for y in range(length_y):
                if(trans_array[x][y]==0):
                    continue
                else:
                    length=len(en_message)
                    en_message=en_message[:length]+trans_array[x][y]

        end_message=""

        #zmena AD,FG atd.. na pismena
        for i in range(1,len(en_message),2):
            ch=''
            a=''
            b=''
            a=adfgx.index(en_message[i-1])
            b=adfgx.index(en_message[i])
            ch=conversion_array[a][b]
            length=len(end_message)
            end_message=end_message[:length]+ch

        end_message = end_message.replace("XMEZERAX", " ")
        end_message = end_message.replace("PBA", "0")
        end_message = end_message.replace("BFB", "1")
        end_message = end_message.replace("CDC", "2")
        end_message = end_message.replace("DCD", "3")
        end_message = end_message.replace("YUE", "4")
        end_message = end_message.replace("EGF", "5")
        end_message = end_message.replace("GHG", "6")
        end_message = end_message.replace("HGH", "7")
        end_message = end_message.replace("RJI", "8")
        end_message = end_message.replace("JIJ", "9")
        
        self.vystup.setText(str(end_message))

    def decrypt_ADFGVX(self):
        adfgx = ["A", "D", "F", "G", "V", "X"]
        conversion_array=self.Create_dectable_ADFGVX()
        perm_key=self.perm_klic.toPlainText()
        perm_key=perm_key.upper()
        encrypt_message=self.vstup.toPlainText()
        encrypt_message=encrypt_message.upper()
        encrypt_message = encrypt_message.replace(" ", "_") 

        length_y=len(perm_key)
        length_array=math.ceil(len(encrypt_message)/len(perm_key))

        input_array = [[0] * length_y for x in range(length_array)]
        trans_array = [[0] * length_y for x in range(length_array)]
        op=encrypt_message[0]

        #vlozeni stringu do pole !!!!!!!
        for y in range(length_y):
           for x in range(length_array):
                if (encrypt_message[0]=="_"):
                    encrypt_message=encrypt_message[1:]
                    break
                else:
                    if len(encrypt_message):
                        input_array[x][y] = encrypt_message[0]
                        encrypt_message=encrypt_message[1:]
                    else:
                        continue
                
        word=self.sortind(perm_key)

        #prehozeni sloupcu v poli
        for y in range(length_y):
            for x in range(length_array):
                seq=word[y];
                trans_array[x][y]=input_array[x][seq]


        #vlozeni sifrz do stringu
        en_message=""
        for x in range(length_array):
            for y in range(length_y):
                if(trans_array[x][y]==0):
                    continue
                else:
                    length=len(en_message)
                    en_message=en_message[:length]+trans_array[x][y]

        end_message=""

        #zmena AD,FG atd.. na pismena
        for i in range(1,len(en_message),2):
            ch=''
            a=''
            b=''
            a=adfgx.index(en_message[i-1])
            b=adfgx.index(en_message[i])
            ch=conversion_array[a][b]
            length=len(end_message)
            end_message=end_message[:length]+ch

        end_message = end_message.replace("XMEZERAX", " ")
        end_message = end_message.replace("PBA", "0")
        end_message = end_message.replace("BFB", "1")
        end_message = end_message.replace("CDC", "2")
        end_message = end_message.replace("DCD", "3")
        end_message = end_message.replace("YUE", "4")
        end_message = end_message.replace("EGF", "5")
        end_message = end_message.replace("GHG", "6")
        end_message = end_message.replace("HGH", "7")
        end_message = end_message.replace("RJI", "8")
        end_message = end_message.replace("JIJ", "9")
        
        self.vystup.setText(str(end_message))
            
    def FindPosition(self, table, ch, size):
        for x in range(size):
            for y in range(size):
                if table[x][y] == ch:
                    return [x, y]
        return [x, y]

    def sortind(self,word):
        t1 = [(word[i],i) for i in range(len(word))]
        t2 = [(k[1],i) for i,k in enumerate(sorted(t1))]
        return [q[1] for q in sorted(t2)]

    def select(self):
        self.vstup.clear()
        self.vystup.clear()
        self.perm_klic.clear()
        self.tab_text.clear()
        self.subs_klic.clear()
        content=self.vyber.currentIndex()
        if content == 1 :
            self.T_sifrovat.clicked.connect(self.encrypt_ADFGVX)
            self.T_desifrovat.clicked.connect(self.decrypt_ADFGVX)
        else:
            self.T_sifrovat.clicked.connect(self.encrypt_ADFGX)
            self.T_desifrovat.clicked.connect(self.decrypt_ADFGX)

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.zmena.clicked.connect(self.select)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayFair()
    window.show()
    sys.exit(app.exec_()) 
