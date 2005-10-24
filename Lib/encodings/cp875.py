""" Python Character Mapping Codec generated from 'MAPPINGS/VENDORS/MICSFT/EBCDIC/CP875.TXT' with gencodec.py.

"""#"

import codecs

### Codec APIs

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):

        return codecs.charmap_encode(input,errors,encoding_map)

    def decode(self,input,errors='strict'):

        return codecs.charmap_decode(input,errors,decoding_table)
    
class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API

def getregentry():

    return (Codec().encode,Codec().decode,StreamReader,StreamWriter)


### Decoding Table

decoding_table = (
    u'\x00'	#  0x00 -> NULL
    u'\x01'	#  0x01 -> START OF HEADING
    u'\x02'	#  0x02 -> START OF TEXT
    u'\x03'	#  0x03 -> END OF TEXT
    u'\x9c'	#  0x04 -> CONTROL
    u'\t'	#  0x05 -> HORIZONTAL TABULATION
    u'\x86'	#  0x06 -> CONTROL
    u'\x7f'	#  0x07 -> DELETE
    u'\x97'	#  0x08 -> CONTROL
    u'\x8d'	#  0x09 -> CONTROL
    u'\x8e'	#  0x0a -> CONTROL
    u'\x0b'	#  0x0b -> VERTICAL TABULATION
    u'\x0c'	#  0x0c -> FORM FEED
    u'\r'	#  0x0d -> CARRIAGE RETURN
    u'\x0e'	#  0x0e -> SHIFT OUT
    u'\x0f'	#  0x0f -> SHIFT IN
    u'\x10'	#  0x10 -> DATA LINK ESCAPE
    u'\x11'	#  0x11 -> DEVICE CONTROL ONE
    u'\x12'	#  0x12 -> DEVICE CONTROL TWO
    u'\x13'	#  0x13 -> DEVICE CONTROL THREE
    u'\x9d'	#  0x14 -> CONTROL
    u'\x85'	#  0x15 -> CONTROL
    u'\x08'	#  0x16 -> BACKSPACE
    u'\x87'	#  0x17 -> CONTROL
    u'\x18'	#  0x18 -> CANCEL
    u'\x19'	#  0x19 -> END OF MEDIUM
    u'\x92'	#  0x1a -> CONTROL
    u'\x8f'	#  0x1b -> CONTROL
    u'\x1c'	#  0x1c -> FILE SEPARATOR
    u'\x1d'	#  0x1d -> GROUP SEPARATOR
    u'\x1e'	#  0x1e -> RECORD SEPARATOR
    u'\x1f'	#  0x1f -> UNIT SEPARATOR
    u'\x80'	#  0x20 -> CONTROL
    u'\x81'	#  0x21 -> CONTROL
    u'\x82'	#  0x22 -> CONTROL
    u'\x83'	#  0x23 -> CONTROL
    u'\x84'	#  0x24 -> CONTROL
    u'\n'	#  0x25 -> LINE FEED
    u'\x17'	#  0x26 -> END OF TRANSMISSION BLOCK
    u'\x1b'	#  0x27 -> ESCAPE
    u'\x88'	#  0x28 -> CONTROL
    u'\x89'	#  0x29 -> CONTROL
    u'\x8a'	#  0x2a -> CONTROL
    u'\x8b'	#  0x2b -> CONTROL
    u'\x8c'	#  0x2c -> CONTROL
    u'\x05'	#  0x2d -> ENQUIRY
    u'\x06'	#  0x2e -> ACKNOWLEDGE
    u'\x07'	#  0x2f -> BELL
    u'\x90'	#  0x30 -> CONTROL
    u'\x91'	#  0x31 -> CONTROL
    u'\x16'	#  0x32 -> SYNCHRONOUS IDLE
    u'\x93'	#  0x33 -> CONTROL
    u'\x94'	#  0x34 -> CONTROL
    u'\x95'	#  0x35 -> CONTROL
    u'\x96'	#  0x36 -> CONTROL
    u'\x04'	#  0x37 -> END OF TRANSMISSION
    u'\x98'	#  0x38 -> CONTROL
    u'\x99'	#  0x39 -> CONTROL
    u'\x9a'	#  0x3a -> CONTROL
    u'\x9b'	#  0x3b -> CONTROL
    u'\x14'	#  0x3c -> DEVICE CONTROL FOUR
    u'\x15'	#  0x3d -> NEGATIVE ACKNOWLEDGE
    u'\x9e'	#  0x3e -> CONTROL
    u'\x1a'	#  0x3f -> SUBSTITUTE
    u' '	#  0x40 -> SPACE
    u'\u0391'	#  0x41 -> GREEK CAPITAL LETTER ALPHA
    u'\u0392'	#  0x42 -> GREEK CAPITAL LETTER BETA
    u'\u0393'	#  0x43 -> GREEK CAPITAL LETTER GAMMA
    u'\u0394'	#  0x44 -> GREEK CAPITAL LETTER DELTA
    u'\u0395'	#  0x45 -> GREEK CAPITAL LETTER EPSILON
    u'\u0396'	#  0x46 -> GREEK CAPITAL LETTER ZETA
    u'\u0397'	#  0x47 -> GREEK CAPITAL LETTER ETA
    u'\u0398'	#  0x48 -> GREEK CAPITAL LETTER THETA
    u'\u0399'	#  0x49 -> GREEK CAPITAL LETTER IOTA
    u'['	#  0x4a -> LEFT SQUARE BRACKET
    u'.'	#  0x4b -> FULL STOP
    u'<'	#  0x4c -> LESS-THAN SIGN
    u'('	#  0x4d -> LEFT PARENTHESIS
    u'+'	#  0x4e -> PLUS SIGN
    u'!'	#  0x4f -> EXCLAMATION MARK
    u'&'	#  0x50 -> AMPERSAND
    u'\u039a'	#  0x51 -> GREEK CAPITAL LETTER KAPPA
    u'\u039b'	#  0x52 -> GREEK CAPITAL LETTER LAMDA
    u'\u039c'	#  0x53 -> GREEK CAPITAL LETTER MU
    u'\u039d'	#  0x54 -> GREEK CAPITAL LETTER NU
    u'\u039e'	#  0x55 -> GREEK CAPITAL LETTER XI
    u'\u039f'	#  0x56 -> GREEK CAPITAL LETTER OMICRON
    u'\u03a0'	#  0x57 -> GREEK CAPITAL LETTER PI
    u'\u03a1'	#  0x58 -> GREEK CAPITAL LETTER RHO
    u'\u03a3'	#  0x59 -> GREEK CAPITAL LETTER SIGMA
    u']'	#  0x5a -> RIGHT SQUARE BRACKET
    u'$'	#  0x5b -> DOLLAR SIGN
    u'*'	#  0x5c -> ASTERISK
    u')'	#  0x5d -> RIGHT PARENTHESIS
    u';'	#  0x5e -> SEMICOLON
    u'^'	#  0x5f -> CIRCUMFLEX ACCENT
    u'-'	#  0x60 -> HYPHEN-MINUS
    u'/'	#  0x61 -> SOLIDUS
    u'\u03a4'	#  0x62 -> GREEK CAPITAL LETTER TAU
    u'\u03a5'	#  0x63 -> GREEK CAPITAL LETTER UPSILON
    u'\u03a6'	#  0x64 -> GREEK CAPITAL LETTER PHI
    u'\u03a7'	#  0x65 -> GREEK CAPITAL LETTER CHI
    u'\u03a8'	#  0x66 -> GREEK CAPITAL LETTER PSI
    u'\u03a9'	#  0x67 -> GREEK CAPITAL LETTER OMEGA
    u'\u03aa'	#  0x68 -> GREEK CAPITAL LETTER IOTA WITH DIALYTIKA
    u'\u03ab'	#  0x69 -> GREEK CAPITAL LETTER UPSILON WITH DIALYTIKA
    u'|'	#  0x6a -> VERTICAL LINE
    u','	#  0x6b -> COMMA
    u'%'	#  0x6c -> PERCENT SIGN
    u'_'	#  0x6d -> LOW LINE
    u'>'	#  0x6e -> GREATER-THAN SIGN
    u'?'	#  0x6f -> QUESTION MARK
    u'\xa8'	#  0x70 -> DIAERESIS
    u'\u0386'	#  0x71 -> GREEK CAPITAL LETTER ALPHA WITH TONOS
    u'\u0388'	#  0x72 -> GREEK CAPITAL LETTER EPSILON WITH TONOS
    u'\u0389'	#  0x73 -> GREEK CAPITAL LETTER ETA WITH TONOS
    u'\xa0'	#  0x74 -> NO-BREAK SPACE
    u'\u038a'	#  0x75 -> GREEK CAPITAL LETTER IOTA WITH TONOS
    u'\u038c'	#  0x76 -> GREEK CAPITAL LETTER OMICRON WITH TONOS
    u'\u038e'	#  0x77 -> GREEK CAPITAL LETTER UPSILON WITH TONOS
    u'\u038f'	#  0x78 -> GREEK CAPITAL LETTER OMEGA WITH TONOS
    u'`'	#  0x79 -> GRAVE ACCENT
    u':'	#  0x7a -> COLON
    u'#'	#  0x7b -> NUMBER SIGN
    u'@'	#  0x7c -> COMMERCIAL AT
    u"'"	#  0x7d -> APOSTROPHE
    u'='	#  0x7e -> EQUALS SIGN
    u'"'	#  0x7f -> QUOTATION MARK
    u'\u0385'	#  0x80 -> GREEK DIALYTIKA TONOS
    u'a'	#  0x81 -> LATIN SMALL LETTER A
    u'b'	#  0x82 -> LATIN SMALL LETTER B
    u'c'	#  0x83 -> LATIN SMALL LETTER C
    u'd'	#  0x84 -> LATIN SMALL LETTER D
    u'e'	#  0x85 -> LATIN SMALL LETTER E
    u'f'	#  0x86 -> LATIN SMALL LETTER F
    u'g'	#  0x87 -> LATIN SMALL LETTER G
    u'h'	#  0x88 -> LATIN SMALL LETTER H
    u'i'	#  0x89 -> LATIN SMALL LETTER I
    u'\u03b1'	#  0x8a -> GREEK SMALL LETTER ALPHA
    u'\u03b2'	#  0x8b -> GREEK SMALL LETTER BETA
    u'\u03b3'	#  0x8c -> GREEK SMALL LETTER GAMMA
    u'\u03b4'	#  0x8d -> GREEK SMALL LETTER DELTA
    u'\u03b5'	#  0x8e -> GREEK SMALL LETTER EPSILON
    u'\u03b6'	#  0x8f -> GREEK SMALL LETTER ZETA
    u'\xb0'	#  0x90 -> DEGREE SIGN
    u'j'	#  0x91 -> LATIN SMALL LETTER J
    u'k'	#  0x92 -> LATIN SMALL LETTER K
    u'l'	#  0x93 -> LATIN SMALL LETTER L
    u'm'	#  0x94 -> LATIN SMALL LETTER M
    u'n'	#  0x95 -> LATIN SMALL LETTER N
    u'o'	#  0x96 -> LATIN SMALL LETTER O
    u'p'	#  0x97 -> LATIN SMALL LETTER P
    u'q'	#  0x98 -> LATIN SMALL LETTER Q
    u'r'	#  0x99 -> LATIN SMALL LETTER R
    u'\u03b7'	#  0x9a -> GREEK SMALL LETTER ETA
    u'\u03b8'	#  0x9b -> GREEK SMALL LETTER THETA
    u'\u03b9'	#  0x9c -> GREEK SMALL LETTER IOTA
    u'\u03ba'	#  0x9d -> GREEK SMALL LETTER KAPPA
    u'\u03bb'	#  0x9e -> GREEK SMALL LETTER LAMDA
    u'\u03bc'	#  0x9f -> GREEK SMALL LETTER MU
    u'\xb4'	#  0xa0 -> ACUTE ACCENT
    u'~'	#  0xa1 -> TILDE
    u's'	#  0xa2 -> LATIN SMALL LETTER S
    u't'	#  0xa3 -> LATIN SMALL LETTER T
    u'u'	#  0xa4 -> LATIN SMALL LETTER U
    u'v'	#  0xa5 -> LATIN SMALL LETTER V
    u'w'	#  0xa6 -> LATIN SMALL LETTER W
    u'x'	#  0xa7 -> LATIN SMALL LETTER X
    u'y'	#  0xa8 -> LATIN SMALL LETTER Y
    u'z'	#  0xa9 -> LATIN SMALL LETTER Z
    u'\u03bd'	#  0xaa -> GREEK SMALL LETTER NU
    u'\u03be'	#  0xab -> GREEK SMALL LETTER XI
    u'\u03bf'	#  0xac -> GREEK SMALL LETTER OMICRON
    u'\u03c0'	#  0xad -> GREEK SMALL LETTER PI
    u'\u03c1'	#  0xae -> GREEK SMALL LETTER RHO
    u'\u03c3'	#  0xaf -> GREEK SMALL LETTER SIGMA
    u'\xa3'	#  0xb0 -> POUND SIGN
    u'\u03ac'	#  0xb1 -> GREEK SMALL LETTER ALPHA WITH TONOS
    u'\u03ad'	#  0xb2 -> GREEK SMALL LETTER EPSILON WITH TONOS
    u'\u03ae'	#  0xb3 -> GREEK SMALL LETTER ETA WITH TONOS
    u'\u03ca'	#  0xb4 -> GREEK SMALL LETTER IOTA WITH DIALYTIKA
    u'\u03af'	#  0xb5 -> GREEK SMALL LETTER IOTA WITH TONOS
    u'\u03cc'	#  0xb6 -> GREEK SMALL LETTER OMICRON WITH TONOS
    u'\u03cd'	#  0xb7 -> GREEK SMALL LETTER UPSILON WITH TONOS
    u'\u03cb'	#  0xb8 -> GREEK SMALL LETTER UPSILON WITH DIALYTIKA
    u'\u03ce'	#  0xb9 -> GREEK SMALL LETTER OMEGA WITH TONOS
    u'\u03c2'	#  0xba -> GREEK SMALL LETTER FINAL SIGMA
    u'\u03c4'	#  0xbb -> GREEK SMALL LETTER TAU
    u'\u03c5'	#  0xbc -> GREEK SMALL LETTER UPSILON
    u'\u03c6'	#  0xbd -> GREEK SMALL LETTER PHI
    u'\u03c7'	#  0xbe -> GREEK SMALL LETTER CHI
    u'\u03c8'	#  0xbf -> GREEK SMALL LETTER PSI
    u'{'	#  0xc0 -> LEFT CURLY BRACKET
    u'A'	#  0xc1 -> LATIN CAPITAL LETTER A
    u'B'	#  0xc2 -> LATIN CAPITAL LETTER B
    u'C'	#  0xc3 -> LATIN CAPITAL LETTER C
    u'D'	#  0xc4 -> LATIN CAPITAL LETTER D
    u'E'	#  0xc5 -> LATIN CAPITAL LETTER E
    u'F'	#  0xc6 -> LATIN CAPITAL LETTER F
    u'G'	#  0xc7 -> LATIN CAPITAL LETTER G
    u'H'	#  0xc8 -> LATIN CAPITAL LETTER H
    u'I'	#  0xc9 -> LATIN CAPITAL LETTER I
    u'\xad'	#  0xca -> SOFT HYPHEN
    u'\u03c9'	#  0xcb -> GREEK SMALL LETTER OMEGA
    u'\u0390'	#  0xcc -> GREEK SMALL LETTER IOTA WITH DIALYTIKA AND TONOS
    u'\u03b0'	#  0xcd -> GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND TONOS
    u'\u2018'	#  0xce -> LEFT SINGLE QUOTATION MARK
    u'\u2015'	#  0xcf -> HORIZONTAL BAR
    u'}'	#  0xd0 -> RIGHT CURLY BRACKET
    u'J'	#  0xd1 -> LATIN CAPITAL LETTER J
    u'K'	#  0xd2 -> LATIN CAPITAL LETTER K
    u'L'	#  0xd3 -> LATIN CAPITAL LETTER L
    u'M'	#  0xd4 -> LATIN CAPITAL LETTER M
    u'N'	#  0xd5 -> LATIN CAPITAL LETTER N
    u'O'	#  0xd6 -> LATIN CAPITAL LETTER O
    u'P'	#  0xd7 -> LATIN CAPITAL LETTER P
    u'Q'	#  0xd8 -> LATIN CAPITAL LETTER Q
    u'R'	#  0xd9 -> LATIN CAPITAL LETTER R
    u'\xb1'	#  0xda -> PLUS-MINUS SIGN
    u'\xbd'	#  0xdb -> VULGAR FRACTION ONE HALF
    u'\x1a'	#  0xdc -> SUBSTITUTE
    u'\u0387'	#  0xdd -> GREEK ANO TELEIA
    u'\u2019'	#  0xde -> RIGHT SINGLE QUOTATION MARK
    u'\xa6'	#  0xdf -> BROKEN BAR
    u'\\'	#  0xe0 -> REVERSE SOLIDUS
    u'\x1a'	#  0xe1 -> SUBSTITUTE
    u'S'	#  0xe2 -> LATIN CAPITAL LETTER S
    u'T'	#  0xe3 -> LATIN CAPITAL LETTER T
    u'U'	#  0xe4 -> LATIN CAPITAL LETTER U
    u'V'	#  0xe5 -> LATIN CAPITAL LETTER V
    u'W'	#  0xe6 -> LATIN CAPITAL LETTER W
    u'X'	#  0xe7 -> LATIN CAPITAL LETTER X
    u'Y'	#  0xe8 -> LATIN CAPITAL LETTER Y
    u'Z'	#  0xe9 -> LATIN CAPITAL LETTER Z
    u'\xb2'	#  0xea -> SUPERSCRIPT TWO
    u'\xa7'	#  0xeb -> SECTION SIGN
    u'\x1a'	#  0xec -> SUBSTITUTE
    u'\x1a'	#  0xed -> SUBSTITUTE
    u'\xab'	#  0xee -> LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\xac'	#  0xef -> NOT SIGN
    u'0'	#  0xf0 -> DIGIT ZERO
    u'1'	#  0xf1 -> DIGIT ONE
    u'2'	#  0xf2 -> DIGIT TWO
    u'3'	#  0xf3 -> DIGIT THREE
    u'4'	#  0xf4 -> DIGIT FOUR
    u'5'	#  0xf5 -> DIGIT FIVE
    u'6'	#  0xf6 -> DIGIT SIX
    u'7'	#  0xf7 -> DIGIT SEVEN
    u'8'	#  0xf8 -> DIGIT EIGHT
    u'9'	#  0xf9 -> DIGIT NINE
    u'\xb3'	#  0xfa -> SUPERSCRIPT THREE
    u'\xa9'	#  0xfb -> COPYRIGHT SIGN
    u'\x1a'	#  0xfc -> SUBSTITUTE
    u'\x1a'	#  0xfd -> SUBSTITUTE
    u'\xbb'	#  0xfe -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\x9f'	#  0xff -> CONTROL
)

### Encoding Map

encoding_map = {
    0x0000: 0x00,	#  NULL
    0x0001: 0x01,	#  START OF HEADING
    0x0002: 0x02,	#  START OF TEXT
    0x0003: 0x03,	#  END OF TEXT
    0x0004: 0x37,	#  END OF TRANSMISSION
    0x0005: 0x2d,	#  ENQUIRY
    0x0006: 0x2e,	#  ACKNOWLEDGE
    0x0007: 0x2f,	#  BELL
    0x0008: 0x16,	#  BACKSPACE
    0x0009: 0x05,	#  HORIZONTAL TABULATION
    0x000a: 0x25,	#  LINE FEED
    0x000b: 0x0b,	#  VERTICAL TABULATION
    0x000c: 0x0c,	#  FORM FEED
    0x000d: 0x0d,	#  CARRIAGE RETURN
    0x000e: 0x0e,	#  SHIFT OUT
    0x000f: 0x0f,	#  SHIFT IN
    0x0010: 0x10,	#  DATA LINK ESCAPE
    0x0011: 0x11,	#  DEVICE CONTROL ONE
    0x0012: 0x12,	#  DEVICE CONTROL TWO
    0x0013: 0x13,	#  DEVICE CONTROL THREE
    0x0014: 0x3c,	#  DEVICE CONTROL FOUR
    0x0015: 0x3d,	#  NEGATIVE ACKNOWLEDGE
    0x0016: 0x32,	#  SYNCHRONOUS IDLE
    0x0017: 0x26,	#  END OF TRANSMISSION BLOCK
    0x0018: 0x18,	#  CANCEL
    0x0019: 0x19,	#  END OF MEDIUM
    0x001a: None,	#  SUBSTITUTE
    0x001b: 0x27,	#  ESCAPE
    0x001c: 0x1c,	#  FILE SEPARATOR
    0x001d: 0x1d,	#  GROUP SEPARATOR
    0x001e: 0x1e,	#  RECORD SEPARATOR
    0x001f: 0x1f,	#  UNIT SEPARATOR
    0x0020: 0x40,	#  SPACE
    0x0021: 0x4f,	#  EXCLAMATION MARK
    0x0022: 0x7f,	#  QUOTATION MARK
    0x0023: 0x7b,	#  NUMBER SIGN
    0x0024: 0x5b,	#  DOLLAR SIGN
    0x0025: 0x6c,	#  PERCENT SIGN
    0x0026: 0x50,	#  AMPERSAND
    0x0027: 0x7d,	#  APOSTROPHE
    0x0028: 0x4d,	#  LEFT PARENTHESIS
    0x0029: 0x5d,	#  RIGHT PARENTHESIS
    0x002a: 0x5c,	#  ASTERISK
    0x002b: 0x4e,	#  PLUS SIGN
    0x002c: 0x6b,	#  COMMA
    0x002d: 0x60,	#  HYPHEN-MINUS
    0x002e: 0x4b,	#  FULL STOP
    0x002f: 0x61,	#  SOLIDUS
    0x0030: 0xf0,	#  DIGIT ZERO
    0x0031: 0xf1,	#  DIGIT ONE
    0x0032: 0xf2,	#  DIGIT TWO
    0x0033: 0xf3,	#  DIGIT THREE
    0x0034: 0xf4,	#  DIGIT FOUR
    0x0035: 0xf5,	#  DIGIT FIVE
    0x0036: 0xf6,	#  DIGIT SIX
    0x0037: 0xf7,	#  DIGIT SEVEN
    0x0038: 0xf8,	#  DIGIT EIGHT
    0x0039: 0xf9,	#  DIGIT NINE
    0x003a: 0x7a,	#  COLON
    0x003b: 0x5e,	#  SEMICOLON
    0x003c: 0x4c,	#  LESS-THAN SIGN
    0x003d: 0x7e,	#  EQUALS SIGN
    0x003e: 0x6e,	#  GREATER-THAN SIGN
    0x003f: 0x6f,	#  QUESTION MARK
    0x0040: 0x7c,	#  COMMERCIAL AT
    0x0041: 0xc1,	#  LATIN CAPITAL LETTER A
    0x0042: 0xc2,	#  LATIN CAPITAL LETTER B
    0x0043: 0xc3,	#  LATIN CAPITAL LETTER C
    0x0044: 0xc4,	#  LATIN CAPITAL LETTER D
    0x0045: 0xc5,	#  LATIN CAPITAL LETTER E
    0x0046: 0xc6,	#  LATIN CAPITAL LETTER F
    0x0047: 0xc7,	#  LATIN CAPITAL LETTER G
    0x0048: 0xc8,	#  LATIN CAPITAL LETTER H
    0x0049: 0xc9,	#  LATIN CAPITAL LETTER I
    0x004a: 0xd1,	#  LATIN CAPITAL LETTER J
    0x004b: 0xd2,	#  LATIN CAPITAL LETTER K
    0x004c: 0xd3,	#  LATIN CAPITAL LETTER L
    0x004d: 0xd4,	#  LATIN CAPITAL LETTER M
    0x004e: 0xd5,	#  LATIN CAPITAL LETTER N
    0x004f: 0xd6,	#  LATIN CAPITAL LETTER O
    0x0050: 0xd7,	#  LATIN CAPITAL LETTER P
    0x0051: 0xd8,	#  LATIN CAPITAL LETTER Q
    0x0052: 0xd9,	#  LATIN CAPITAL LETTER R
    0x0053: 0xe2,	#  LATIN CAPITAL LETTER S
    0x0054: 0xe3,	#  LATIN CAPITAL LETTER T
    0x0055: 0xe4,	#  LATIN CAPITAL LETTER U
    0x0056: 0xe5,	#  LATIN CAPITAL LETTER V
    0x0057: 0xe6,	#  LATIN CAPITAL LETTER W
    0x0058: 0xe7,	#  LATIN CAPITAL LETTER X
    0x0059: 0xe8,	#  LATIN CAPITAL LETTER Y
    0x005a: 0xe9,	#  LATIN CAPITAL LETTER Z
    0x005b: 0x4a,	#  LEFT SQUARE BRACKET
    0x005c: 0xe0,	#  REVERSE SOLIDUS
    0x005d: 0x5a,	#  RIGHT SQUARE BRACKET
    0x005e: 0x5f,	#  CIRCUMFLEX ACCENT
    0x005f: 0x6d,	#  LOW LINE
    0x0060: 0x79,	#  GRAVE ACCENT
    0x0061: 0x81,	#  LATIN SMALL LETTER A
    0x0062: 0x82,	#  LATIN SMALL LETTER B
    0x0063: 0x83,	#  LATIN SMALL LETTER C
    0x0064: 0x84,	#  LATIN SMALL LETTER D
    0x0065: 0x85,	#  LATIN SMALL LETTER E
    0x0066: 0x86,	#  LATIN SMALL LETTER F
    0x0067: 0x87,	#  LATIN SMALL LETTER G
    0x0068: 0x88,	#  LATIN SMALL LETTER H
    0x0069: 0x89,	#  LATIN SMALL LETTER I
    0x006a: 0x91,	#  LATIN SMALL LETTER J
    0x006b: 0x92,	#  LATIN SMALL LETTER K
    0x006c: 0x93,	#  LATIN SMALL LETTER L
    0x006d: 0x94,	#  LATIN SMALL LETTER M
    0x006e: 0x95,	#  LATIN SMALL LETTER N
    0x006f: 0x96,	#  LATIN SMALL LETTER O
    0x0070: 0x97,	#  LATIN SMALL LETTER P
    0x0071: 0x98,	#  LATIN SMALL LETTER Q
    0x0072: 0x99,	#  LATIN SMALL LETTER R
    0x0073: 0xa2,	#  LATIN SMALL LETTER S
    0x0074: 0xa3,	#  LATIN SMALL LETTER T
    0x0075: 0xa4,	#  LATIN SMALL LETTER U
    0x0076: 0xa5,	#  LATIN SMALL LETTER V
    0x0077: 0xa6,	#  LATIN SMALL LETTER W
    0x0078: 0xa7,	#  LATIN SMALL LETTER X
    0x0079: 0xa8,	#  LATIN SMALL LETTER Y
    0x007a: 0xa9,	#  LATIN SMALL LETTER Z
    0x007b: 0xc0,	#  LEFT CURLY BRACKET
    0x007c: 0x6a,	#  VERTICAL LINE
    0x007d: 0xd0,	#  RIGHT CURLY BRACKET
    0x007e: 0xa1,	#  TILDE
    0x007f: 0x07,	#  DELETE
    0x0080: 0x20,	#  CONTROL
    0x0081: 0x21,	#  CONTROL
    0x0082: 0x22,	#  CONTROL
    0x0083: 0x23,	#  CONTROL
    0x0084: 0x24,	#  CONTROL
    0x0085: 0x15,	#  CONTROL
    0x0086: 0x06,	#  CONTROL
    0x0087: 0x17,	#  CONTROL
    0x0088: 0x28,	#  CONTROL
    0x0089: 0x29,	#  CONTROL
    0x008a: 0x2a,	#  CONTROL
    0x008b: 0x2b,	#  CONTROL
    0x008c: 0x2c,	#  CONTROL
    0x008d: 0x09,	#  CONTROL
    0x008e: 0x0a,	#  CONTROL
    0x008f: 0x1b,	#  CONTROL
    0x0090: 0x30,	#  CONTROL
    0x0091: 0x31,	#  CONTROL
    0x0092: 0x1a,	#  CONTROL
    0x0093: 0x33,	#  CONTROL
    0x0094: 0x34,	#  CONTROL
    0x0095: 0x35,	#  CONTROL
    0x0096: 0x36,	#  CONTROL
    0x0097: 0x08,	#  CONTROL
    0x0098: 0x38,	#  CONTROL
    0x0099: 0x39,	#  CONTROL
    0x009a: 0x3a,	#  CONTROL
    0x009b: 0x3b,	#  CONTROL
    0x009c: 0x04,	#  CONTROL
    0x009d: 0x14,	#  CONTROL
    0x009e: 0x3e,	#  CONTROL
    0x009f: 0xff,	#  CONTROL
    0x00a0: 0x74,	#  NO-BREAK SPACE
    0x00a3: 0xb0,	#  POUND SIGN
    0x00a6: 0xdf,	#  BROKEN BAR
    0x00a7: 0xeb,	#  SECTION SIGN
    0x00a8: 0x70,	#  DIAERESIS
    0x00a9: 0xfb,	#  COPYRIGHT SIGN
    0x00ab: 0xee,	#  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00ac: 0xef,	#  NOT SIGN
    0x00ad: 0xca,	#  SOFT HYPHEN
    0x00b0: 0x90,	#  DEGREE SIGN
    0x00b1: 0xda,	#  PLUS-MINUS SIGN
    0x00b2: 0xea,	#  SUPERSCRIPT TWO
    0x00b3: 0xfa,	#  SUPERSCRIPT THREE
    0x00b4: 0xa0,	#  ACUTE ACCENT
    0x00bb: 0xfe,	#  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00bd: 0xdb,	#  VULGAR FRACTION ONE HALF
    0x0385: 0x80,	#  GREEK DIALYTIKA TONOS
    0x0386: 0x71,	#  GREEK CAPITAL LETTER ALPHA WITH TONOS
    0x0387: 0xdd,	#  GREEK ANO TELEIA
    0x0388: 0x72,	#  GREEK CAPITAL LETTER EPSILON WITH TONOS
    0x0389: 0x73,	#  GREEK CAPITAL LETTER ETA WITH TONOS
    0x038a: 0x75,	#  GREEK CAPITAL LETTER IOTA WITH TONOS
    0x038c: 0x76,	#  GREEK CAPITAL LETTER OMICRON WITH TONOS
    0x038e: 0x77,	#  GREEK CAPITAL LETTER UPSILON WITH TONOS
    0x038f: 0x78,	#  GREEK CAPITAL LETTER OMEGA WITH TONOS
    0x0390: 0xcc,	#  GREEK SMALL LETTER IOTA WITH DIALYTIKA AND TONOS
    0x0391: 0x41,	#  GREEK CAPITAL LETTER ALPHA
    0x0392: 0x42,	#  GREEK CAPITAL LETTER BETA
    0x0393: 0x43,	#  GREEK CAPITAL LETTER GAMMA
    0x0394: 0x44,	#  GREEK CAPITAL LETTER DELTA
    0x0395: 0x45,	#  GREEK CAPITAL LETTER EPSILON
    0x0396: 0x46,	#  GREEK CAPITAL LETTER ZETA
    0x0397: 0x47,	#  GREEK CAPITAL LETTER ETA
    0x0398: 0x48,	#  GREEK CAPITAL LETTER THETA
    0x0399: 0x49,	#  GREEK CAPITAL LETTER IOTA
    0x039a: 0x51,	#  GREEK CAPITAL LETTER KAPPA
    0x039b: 0x52,	#  GREEK CAPITAL LETTER LAMDA
    0x039c: 0x53,	#  GREEK CAPITAL LETTER MU
    0x039d: 0x54,	#  GREEK CAPITAL LETTER NU
    0x039e: 0x55,	#  GREEK CAPITAL LETTER XI
    0x039f: 0x56,	#  GREEK CAPITAL LETTER OMICRON
    0x03a0: 0x57,	#  GREEK CAPITAL LETTER PI
    0x03a1: 0x58,	#  GREEK CAPITAL LETTER RHO
    0x03a3: 0x59,	#  GREEK CAPITAL LETTER SIGMA
    0x03a4: 0x62,	#  GREEK CAPITAL LETTER TAU
    0x03a5: 0x63,	#  GREEK CAPITAL LETTER UPSILON
    0x03a6: 0x64,	#  GREEK CAPITAL LETTER PHI
    0x03a7: 0x65,	#  GREEK CAPITAL LETTER CHI
    0x03a8: 0x66,	#  GREEK CAPITAL LETTER PSI
    0x03a9: 0x67,	#  GREEK CAPITAL LETTER OMEGA
    0x03aa: 0x68,	#  GREEK CAPITAL LETTER IOTA WITH DIALYTIKA
    0x03ab: 0x69,	#  GREEK CAPITAL LETTER UPSILON WITH DIALYTIKA
    0x03ac: 0xb1,	#  GREEK SMALL LETTER ALPHA WITH TONOS
    0x03ad: 0xb2,	#  GREEK SMALL LETTER EPSILON WITH TONOS
    0x03ae: 0xb3,	#  GREEK SMALL LETTER ETA WITH TONOS
    0x03af: 0xb5,	#  GREEK SMALL LETTER IOTA WITH TONOS
    0x03b0: 0xcd,	#  GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND TONOS
    0x03b1: 0x8a,	#  GREEK SMALL LETTER ALPHA
    0x03b2: 0x8b,	#  GREEK SMALL LETTER BETA
    0x03b3: 0x8c,	#  GREEK SMALL LETTER GAMMA
    0x03b4: 0x8d,	#  GREEK SMALL LETTER DELTA
    0x03b5: 0x8e,	#  GREEK SMALL LETTER EPSILON
    0x03b6: 0x8f,	#  GREEK SMALL LETTER ZETA
    0x03b7: 0x9a,	#  GREEK SMALL LETTER ETA
    0x03b8: 0x9b,	#  GREEK SMALL LETTER THETA
    0x03b9: 0x9c,	#  GREEK SMALL LETTER IOTA
    0x03ba: 0x9d,	#  GREEK SMALL LETTER KAPPA
    0x03bb: 0x9e,	#  GREEK SMALL LETTER LAMDA
    0x03bc: 0x9f,	#  GREEK SMALL LETTER MU
    0x03bd: 0xaa,	#  GREEK SMALL LETTER NU
    0x03be: 0xab,	#  GREEK SMALL LETTER XI
    0x03bf: 0xac,	#  GREEK SMALL LETTER OMICRON
    0x03c0: 0xad,	#  GREEK SMALL LETTER PI
    0x03c1: 0xae,	#  GREEK SMALL LETTER RHO
    0x03c2: 0xba,	#  GREEK SMALL LETTER FINAL SIGMA
    0x03c3: 0xaf,	#  GREEK SMALL LETTER SIGMA
    0x03c4: 0xbb,	#  GREEK SMALL LETTER TAU
    0x03c5: 0xbc,	#  GREEK SMALL LETTER UPSILON
    0x03c6: 0xbd,	#  GREEK SMALL LETTER PHI
    0x03c7: 0xbe,	#  GREEK SMALL LETTER CHI
    0x03c8: 0xbf,	#  GREEK SMALL LETTER PSI
    0x03c9: 0xcb,	#  GREEK SMALL LETTER OMEGA
    0x03ca: 0xb4,	#  GREEK SMALL LETTER IOTA WITH DIALYTIKA
    0x03cb: 0xb8,	#  GREEK SMALL LETTER UPSILON WITH DIALYTIKA
    0x03cc: 0xb6,	#  GREEK SMALL LETTER OMICRON WITH TONOS
    0x03cd: 0xb7,	#  GREEK SMALL LETTER UPSILON WITH TONOS
    0x03ce: 0xb9,	#  GREEK SMALL LETTER OMEGA WITH TONOS
    0x2015: 0xcf,	#  HORIZONTAL BAR
    0x2018: 0xce,	#  LEFT SINGLE QUOTATION MARK
    0x2019: 0xde,	#  RIGHT SINGLE QUOTATION MARK
}