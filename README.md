# ChordPy!
A Pyton script that takes ChordPro files (especially from [WorshipTogether.com](http://www.worshiptogether.com/)) and converts them to a readable plaintext format.  Output file is in same location as input.

**To download the program for Windows, [go here and click "View Raw"](https://github.com/tkoft/ChordPy/tree/master/dist/ChordPy.exe).**

![Download free ChordPro file from WorshipTogether](https://github.com/tkoft/ChordPy/blob/master/img/tut1.png?raw=true)
![First dialog when you run the program](https://github.com/tkoft/ChordPy/blob/master/img/tut2.png)
![Pick literally any integer](https://github.com/tkoft/ChordPy/blob/master/img/tut3.png)
![Voila!](https://github.com/tkoft/ChordPy/blob/master/img/tut4.png)

My usual workflow for making chordsheets is:
* download ChordPro file from [WorshipTogether](http://www.worshiptogether.com/) (*free!*)
* find the transposed key I like
* transpose and convert using ChordPy
* copy output text to MS Word and make pretty for printing (two columns, 0.5 margins is the only right way to do this obviously). 

I use PyInstaller to make this Python script into a `.exe` executable.  The program only uses `tkinter` simple GUI dialogs.  Run `make.bat` to compile ChordPro.py into an executable.   

**God Bless!  Have fun worshipping!**
