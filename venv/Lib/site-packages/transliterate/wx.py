## -*- coding: utf-8 -*-
# (C) 2020 முத்து அண்ணாமலை
# https://en.wikipedia.org/wiki/WX_notation
# Ref: https://github.com/irshadbhat/indic-wx-converter/blob/7ce1ac54b9df5ac8beed71c73e2e8b80b2eca65d/wxconv/wx.py#L2562
from collections import OrderedDict

from tamil.utf8 import uyirmei_letters, splitMeiUyir

_uyir = (
    ("அ", "A"),
    ("ஆ", ("A")),
    ("இ", "I"),
    ("ஈ", ("II")),
    ("உ", "U"),
    ("ஊ", ("UU")),
    ("எ", "E"),
    ("ஏ", ("EY")),
    ("ஐ", "AI"),
    ("ஒ", "O"),
    ("ஓ", ("OW")),
    ("ஔ", "AU"),
)
_aytham = (("ஃ", "H"),)
_mei = (
    ("க்", ("K")),
    ("ங்", "NG"),
    ("ச்", "CH"),
    ("ஜ்", "JA"),
    ("ஞ்", "nY"),
    ("ட்", ("d", "t")),
    ("ண்", "NAA"),
    ("த்", ("dh", "dt")),
    ("ந்", "N"),
    ("ன்", "NA"),
    ("ப்", ("b", "bh", "p")),
    ("ம்", "m"),
    ("ய்", "y"),
    ("ர்", "r"),
    ("ற்", "R"),
    ("ல்", "l"),
    ("ள்", "L"),
    ("ழ்", ("z", "zh")),
    ("வ்", ("v", "w")),
    ("ஷ்", "sh"),
    ("ஸ்", "s"),
    ("ஹ்", "h"),
    ("ஃப்", "f"),
)


class Transliteration:
    """
    ITRANS encoding formats.
    """

    table = OrderedDict()  # {}


def _options(_ref, _sym):
    _v = []
    for _k, _v in _ref:
        if _k == _sym:
            break
    return _v


for ta_map in [_uyir, _mei, _aytham]:
    for obj in ta_map:
        ta, en = obj[0], obj[1]
        if not isinstance(en, (list, tuple)):
            en = list(en)
        for e in en:
            Transliteration.table[e] = ta

# mix of consonants and compound - uyirmei - letters
for vc in uyirmei_letters:
    c, v = splitMeiUyir(vc)
    for vo in _options(_uyir, v):
        for co in _options(_mei, c):
            if not Transliteration.table.get(co + vo, None):
                Transliteration.table[co + vo] = vc

from pprint import pprint

pprint(Transliteration.table)
print(len(Transliteration.table))
