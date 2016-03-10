import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox

scale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
def transpose(note, step):
	noteNum = scale.index(note)
	noteNum = (noteNum+step) % 12
	return scale[noteNum]

root = tk.Tk()
root.withdraw()
filename = filedialog.askopenfilename(title="ChordPy: Chose ChordPro .txt File")
if filename != "":
	while True:	
		trans = simpledialog.askstring("ChordPy", "Transpose (+/- #): ")
		if trans == "" or trans == None:
			trans = 0
			break	
		else:
			try:		
				trans = int(trans)%12
				break
			except ValueError:
				messagebox.showinfo(title="ChordPy", message="Invalid transposition.")
				#print("Invalid transposition.")		

	f = open(filename, "r")
	outFilename = filename[:len(filename)-4]+"_transposed"+str(trans)+".txt"
	out = open(outFilename, "w+")

	for line in f:
		outputChords = ""
		outputLyrics = ""
		inBracket = False
		for i in range(len(line)):
			if line[i] == '[':
				inBracket = True
				outputChords = outputChords + " "*(i-len(outputChords))
			elif inBracket and line[i] == ']':
				inBracket = False
			elif inBracket and line[i] =='#':
				pass
			elif inBracket and str.isupper(line[i]):
				if line[i+1] == '#':
					outputChords += transpose(line[i]+"#", trans)
				else:
					outputChords += transpose(line[i], trans)
			elif inBracket:
				#DONT TRANSPOSE AND PUT IN OUTPUTCHORDS
				outputChords = outputChords + line[i]
			else:
				outputLyrics = outputLyrics + line[i]
		if not str.strip(outputChords) == "":
			out.write(outputChords+"\n")
		out.write(outputLyrics)

	f.close()
	out.close()

	messagebox.showinfo(title="ChordPy", message=("Transposed " + str(trans) + " steps to " + outFilename))