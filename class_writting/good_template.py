from music21 import *


def part2stream(part):
    s = stream.Stream()
    for p in part:
        if p == "-":
            s.append(note.Rest())
        else:
            s.append(note.Note(p))
    return s


def combine_stream(streams):
    big_s = stream.Stream()
    for s in streams:
        big_s.append(s)
    return big_s


# part1 = [""]
# stream1.id = "some notes"
# stream1.append(note1)
# stream1.append(note2)
# stream1.append(note3)

# biggerStream = stream.Stream()
# note2 = note.Note("D#5")
# biggerStream.insert(0, note2)
# biggerStream.append(stream1)


def main():
    part1 = ["E4", "G4", "C4", "-"]
    part2 = ["D4", "E4", "A3", "-"]
    part3 = ["C4", "D4", "E4", "G4"]
    part4 = ["D4", "-", "-", "-"]
    s = combine_stream(
        [
            part2stream(part1),
            part2stream(part2),
            part2stream(part3),
            part2stream(part4),
        ]
    )
    s.show("midi")


if __name__ == "__main__":
    main()
