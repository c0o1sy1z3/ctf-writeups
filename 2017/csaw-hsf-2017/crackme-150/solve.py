fuck=[-103,
-109,
-98,
-104,
-124,
-103,
-109,
-102,
-104,
-96,
-103,
-109,
-102,
-104,
-96,
-104,
-112,
-96,
-98,
-120,
-98,
-122,
-96,
-99,
-106,
-117,
-103,
-109,
-106,
-113,
-96,
-110,
-102,
-96,
-98,
-111,
-112,
-117,
-105,
-102,
-115,
-96,
-101,
0x9E,
0x86,
0x82]
s = ''
for x in fuck:
    if x < 0:
        x += 0x100
    s += chr(~x & 0xFF)
print s
