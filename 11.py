from enum import Enum
from struct import unpack_from, calcsize


class Types(Enum):
    float = "f"
    uint64 = "Q"
    uint32 = "I"
    uint16 = "H"
    uint8 = "B"
    int64 = "q"
    int32 = "i"
    int16 = "h"
    int8 = "b"
    char = "c"
    double = "d"


class BinaryReader:
    def __init__(self, offset, source):
        self.offset = offset
        self.source = source

    def read(self, pattern):
        pattern = '>' + pattern.value
        result = unpack_from(pattern, self.source, self.offset)
        self.offset += calcsize(pattern)
        return result[0]


def a(reader: BinaryReader):
    a1 = reader.read(Types.uint8)
    a2 = masser_a2(reader.read(Types.uint32), reader.read(Types.uint16), reader.source)
    a3 = reader.read(Types.int64)
    a4 = (reader.read(Types.char) + reader.read(Types.char) +
          reader.read(Types.char) + reader.read(Types.char) +
          reader.read(Types.char) + reader.read(Types.char) +
          reader.read(Types.char) + reader.read(Types.char)). \
        decode("ascii")
    a5 = reader.read(Types.int16)
    a6 = masser_a6(reader.read(Types.uint32), reader.read(Types.uint16), reader.source)
    a7 = d(reader)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5 = a5, A6 = a6, A7 = a7)


def b(reader: BinaryReader):
    b1 = reader.read(Types.int16)
    b2 = c(reader.read(Types.uint32), reader.source)
    return dict(B1=b1, B2=b2)


def c(offset, source):
    reader = BinaryReader(offset, source)
    c1 = reader.read(Types.float)
    c2 = reader.read(Types.uint16)
    return dict(C1=c1, C2=c2)


def d(reader: BinaryReader):
    d1 = reader.read(Types.uint64)
    d2 = reader.read(Types.uint64)
    d3 = masser_d3(8, reader)
    d4 = reader.read(Types.float)
    d5 = reader.read(Types.double)
    d6 = reader.read(Types.int16)
    d7 = reader.read(Types.int32)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6, D7=d7)


def masser_a2(size, offset, source):
    reader = BinaryReader(offset, source)
    rez = []
    while reader.offset < offset + size * 6:
        rez.append(b(reader))
    return rez


def masser_a6(size, offset, source):
    reader = BinaryReader(offset, source)
    rez = ''
    while reader.offset < offset + size:
        rez += str(reader.read(Types.char).decode("ascii"))
    return rez


def masser_d3(size, reader: BinaryReader):
    offset = reader.offset
    rez = []
    while reader.offset < offset + size * 8:
        rez.append(reader.read(Types.uint64))
    return rez


def main(source):
    reader = BinaryReader(offset=4, source=source)
    return a(reader)


print(main(b'JOKUI\x00\x00\x00\x04\x00\x9d\xa9}\x02y\xc5\xe9\xd0olguypyxh\xd4'
    b'\xa7\x00\x00\x00\x03\x00\xb5\xcf?\xee\x8c\x11\x8fd\xcd\xbd-`\xeb~\xb5\xe1U`'
    b'u@0\xfa\x0b+P\xe5O\xbcD\xad(\xc9\xac@\x98P\xcf\xc7|@\xcf\x97^_p\xec'
    b'5\x1f\x0b3\xba\r\x15\x1bvi\x13\xfb\xd7T\x0c\x15\x93\x1c\xbc|\xbac\xbfg'
    b'\xbdg\x14\xeb\x8b\x8cM\xfd\xabz\x99>\xde;\xec?\xbfj[\xcc\xa3G0.\xcdn\xba\xda'
    b"\xf6?9\x00\x9e\x0b\x1c\xbe\x9f\xbe\x15v\xdc>\xcf?\x1e\xcb\xe7?w'\xf4\xa5"
    b']k\xe3\x00\x00\x00\x85\xa7\xff\x00\x00\x00\x8bK*\x00\x00\x00\x91['
    b'X\x00\x00\x00\x97ipk'))