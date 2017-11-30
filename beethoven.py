from pyknon.genmidi import Midi
from pyknon.music import NoteSeq
from pyknon.music import Note
from pyknon.music import Rest

a = NoteSeq("R8 G8 G8 G8")
b = NoteSeq("R8 F8 F8 F8")
c = NoteSeq([Note(3, dur=1)])
d = NoteSeq([Note(2, dur=1)])
e = NoteSeq("R8 Ab8 Ab8 Ab8")
f = NoteSeq("R8 Eb8'' Eb8'' Eb8''")
g = NoteSeq([Note(7, dur=0.75)])
h = NoteSeq([Note(0, dur=1)])
i = NoteSeq("G8 G8 G8 G8")
j = NoteSeq([Note(0, dur=0.5)])
k = NoteSeq([Note(7, dur=0.5)])

track3 = NoteSeq([Note(0, octave=6, dur=1)])
track4 = NoteSeq([Note(3, dur=1), Note(3, dur=1)])

bass = NoteSeq("G8,, G8,, G8,,")
bass2 = NoteSeq([Note(3, octave=3, dur=1)])

notes1 = a + c + b + d + a + e + f + h + j + Rest(dur=0.5)
notes2 = Rest(dur=4.0) + k + g + i
notes3 = Rest(dur=4.5) + track3
notes4 = Rest(dur=3.5) + track4
notes5 = Rest(dur=0.125) + bass + bass2 + Rest(dur=0.125) + bass + bass2

midi = Midi(number_tracks=5, tempo=108)
midi.seq_notes(notes1, track=0)
midi.seq_notes(notes2, track=1)
midi.seq_notes(notes3, track=2)
midi.seq_notes(notes4, track=3)
midi.seq_notes(notes5, track=4)
midi.write("fifth11.mid")

