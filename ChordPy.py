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
		transText = simpledialog.askstring("ChordPy", "Transpose (+/- #s, comma separated): ")
		if transText == "" or transText == None:
			transText = 0
			transValues = [0]
			break	
		else:
			try:		
				transValues = transText.split(",")
				transValues = list(map(int, transValues))
				break
			except ValueError:
				messagebox.showinfo(title="ChordPy", message="Invalid transposition.")
				#print("Invalid transposition.")		

	for trans in transValues:
		f = open(filename, "r", encoding='utf-8')
		outFilename = filename[:len(filename)-4]+"_transposed"+str(trans)+".txt"
		out = open(outFilename, "w+", encoding='utf-8')

		for line in f:
			outputChords = ""
			outputLyrics = ""
			inBracket = False
			for i in range(len(line)):
				if line[i] == '[':
					inBracket = True
					outputChords = outputChords + " "*(max(0, len(outputLyrics.encode('gbk'))-len(outputChords.encode('gbk'))))
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

	messagebox.showinfo(title="ChordPy", message=("Transposed " + ", ".join(map(str, transValues)) + " steps."))