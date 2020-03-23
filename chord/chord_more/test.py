from music21 import *

cMinor = chord.Chord(["C4", "G4", "E-5"])

cMinor.duration.type = "half"
cMinor.quarterLength

# cMinor.show("midi")

cMinor.show()
cMajor.show()

