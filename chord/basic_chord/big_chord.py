# https://en.wikipedia.org/wiki/Major_chord
from music21 import stream, note, chord


def main():
    s = stream.Stream()

    # names = ["C4", "E4", "G4"]

    # names = ["C#4", "F4", "G#4"]

    # names = ["D4", "F#4", "A4"]

    names = ["E4", "G#4", "B"]

    for name in names:
        s.append(note.Note(name))

    s.show("midi")

    c = chord.Chord(names)
    c.duration.type = "half"
    c.quarterLength
    c.show("midi")


if __name__ == "__main__":
    main()
