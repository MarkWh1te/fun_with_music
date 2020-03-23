from music21 import stream, note


# names = ["C1", "C3", "C5"]
names = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
s = stream.Stream()
for name in names:
    s.append(note.Note(name))

s.show("midi")

# names = ["C#1", "C#3", "C#5"]
# s = stream.Stream()
# for name in names:
#     s.append(note.Note(name))


# s.show("midi")
