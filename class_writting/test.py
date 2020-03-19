from music21 import *

note1 = note.Note("C4")
note1.duration.type = "half"
note2 = note.Note("F#4")
note3 = note.Note("B2")

stream1 = stream.Stream()
stream1.id = "some notes"
stream1.append(note1)
stream1.append(note2)
stream1.append(note3)

biggerStream = stream.Stream()
note2 = note.Note("D#5")
biggerStream.insert(0, note2)
biggerStream.append(stream1)
biggerStream.show("midi")
