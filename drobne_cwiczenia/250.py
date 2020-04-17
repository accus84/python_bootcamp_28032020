# a = [2, 4]        tak było oryginalnie - to jest źle
a = (2, 4)          # tak jest poprawnie
print("%d do kwadratu to %d" % a)

# Wskazowka (zakodowana w ROT13):
# Bcrengbe jlcryavravn jmbepn (bcrengbe %) zn qbfgnp qjn nethzragl:
# - m yrjrw zn olp ancvf
# - m cenjrw zn olp xebgxn (ab, rjraghnyavr fybjavx - nyr ghgnw gb avr zn manpmravn)
# Nethzrag m cenjrw avr zbmr olp yvfgn.

#import codecs
#codecs.encode(phrase, 'rot_13')
cleartxt = """Bcrengbe jlcryavravn jmbepn (bcrengbe %) zn qbfgnp qjn nethzragl:
- m yrjrw zn olp ancvf
- m cenjrw zn olp xebgxn (ab, rjraghnyavr fybjavx - nyr ghgnw gb avr zn manpmravn)
Nethzrag m cenjrw avr zbmr olp yvfgn.
"""
abc = "abcdefghijklmnopqrstuvwxyz"
secret = "".join([abc[(abc.find(c)+13)%26] for c in cleartxt])
print(secret)