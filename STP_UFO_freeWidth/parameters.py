# This file was automatically created by FeynRules 1.6.11
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (February 23, 2011)
# Date: Mon 15 Sep 2014 21:33:43



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cLTW = Parameter(name = 'cLTW',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cLTW}',
                 lhablock = 'BSM',
                 lhacode = [ 1 ])

cRTW = Parameter(name = 'cRTW',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cRTW}',
                 lhablock = 'BSM',
                 lhacode = [ 2 ])

cLTZ = Parameter(name = 'cLTZ',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cLTZ}',
                 lhablock = 'BSM',
                 lhacode = [ 3 ])

cRTZ = Parameter(name = 'cRTZ',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cRTZ}',
                 lhablock = 'BSM',
                 lhacode = [ 4 ])

cLTh = Parameter(name = 'cLTh',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cLTh}',
                 lhablock = 'BSM',
                 lhacode = [ 5 ])

cRTh = Parameter(name = 'cRTh',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cRTh}',
                 lhablock = 'BSM',
                 lhacode = [ 6 ])

cLBW = Parameter(name = 'cLBW',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cLBW}',
                 lhablock = 'BSM',
                 lhacode = [ 7 ])

cRBW = Parameter(name = 'cRBW',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cRBW}',
                 lhablock = 'BSM',
                 lhacode = [ 8 ])

cLBZ = Parameter(name = 'cLBZ',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cLBZ}',
                 lhablock = 'BSM',
                 lhacode = [ 9 ])

cRBZ = Parameter(name = 'cRBZ',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cRBZ}',
                 lhablock = 'BSM',
                 lhacode = [ 10 ])

cLBh = Parameter(name = 'cLBh',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cLBh}',
                 lhablock = 'BSM',
                 lhacode = [ 11 ])

cRBh = Parameter(name = 'cRBh',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cRBh}',
                 lhablock = 'BSM',
                 lhacode = [ 12 ])

cLXW = Parameter(name = 'cLXW',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cLXW}',
                 lhablock = 'BSM',
                 lhacode = [ 13 ])

cRXW = Parameter(name = 'cRXW',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cRXW}',
                 lhablock = 'BSM',
                 lhacode = [ 14 ])

cLYW = Parameter(name = 'cLYW',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cLYW}',
                 lhablock = 'BSM',
                 lhacode = [ 15 ])

cRYW = Parameter(name = 'cRYW',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cRYW}',
                 lhablock = 'BSM',
                 lhacode = [ 16 ])

cLVW = Parameter(name = 'cLVW',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cLVW}',
                 lhablock = 'BSM',
                 lhacode = [ 17 ])

cRVW = Parameter(name = 'cRVW',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cRVW}',
                 lhablock = 'BSM',
                 lhacode = [ 18 ])

LAMBDA = Parameter(name = 'LAMBDA',
                   nature = 'external',
                   type = 'real',
                   value = 3000.,
                   texname = '\\Lambda',
                   lhablock = 'BSM',
                   lhacode = [ 19 ])

cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\text{aS}',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.0025499999999999997,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.67,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172.5,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.0005110000000000001,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.0005110000000000001,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.10566,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.0025499999999999997,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

Mtop = Parameter(name = 'Mtop',
                 nature = 'external',
                 type = 'real',
                 value = 172.5,
                 texname = '\\text{Mtop}',
                 lhablock = 'MASS',
                 lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

Mbot = Parameter(name = 'Mbot',
                 nature = 'external',
                 type = 'real',
                 value = 4.67,
                 texname = '\\text{Mbot}',
                 lhablock = 'MASS',
                 lhacode = [ 5 ])

MT23 = Parameter(name = 'MT23',
                 nature = 'external',
                 type = 'real',
                 value = 700,
                 texname = '\\text{MT23}',
                 lhablock = 'MASS',
                 lhacode = [ 8000001 ])

MB13 = Parameter(name = 'MB13',
                 nature = 'external',
                 type = 'real',
                 value = 700,
                 texname = '\\text{MB13}',
                 lhablock = 'MASS',
                 lhacode = [ 8000002 ])

MX53 = Parameter(name = 'MX53',
                 nature = 'external',
                 type = 'real',
                 value = 700,
                 texname = '\\text{MX53}',
                 lhablock = 'MASS',
                 lhacode = [ 8000003 ])

MY43 = Parameter(name = 'MY43',
                 nature = 'external',
                 type = 'real',
                 value = 700,
                 texname = '\\text{MY43}',
                 lhablock = 'MASS',
                 lhacode = [ 8000004 ])

MV83 = Parameter(name = 'MV83',
                 nature = 'external',
                 type = 'real',
                 value = 700,
                 texname = '\\text{MV83}',
                 lhablock = 'MASS',
                 lhacode = [ 8000005 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 80.399,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

Wtop = Parameter(name = 'Wtop',
                 nature = 'external',
                 type = 'real',
                 value = 1.50833649,
                 texname = '\\text{Wtop}',
                 lhablock = 'DECAY',
                 lhacode = [ 6 ])

WV83 = Parameter(name = 'WV83',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WV83}',
                 lhablock = 'DECAY',
                 lhacode = [ 8000005 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00575308848,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WB13 = Parameter(name = 'WB13',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WB13}',
                 lhablock = 'DECAY',
                 lhacode = [ 8000002 ])

WT23 = Parameter(name = 'WT23',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WT23}',
                 lhablock = 'DECAY',
                 lhacode = [ 8000001 ])

WX53 = Parameter(name = 'WX53',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WX53}',
                 lhablock = 'DECAY',
                 lhacode = [ 8000003 ])

WY43 = Parameter(name = 'WY43',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WY43}',
                 lhablock = 'DECAY',
                 lhacode = [ 8000004 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\text{aEW}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM11 = Parameter(name = 'CKM11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'cmath.cos(cabi)',
                  texname = '\\text{CKM11}')

CKM12 = Parameter(name = 'CKM12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'cmath.sin(cabi)',
                  texname = '\\text{CKM12}')

CKM13 = Parameter(name = 'CKM13',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{CKM13}')

CKM21 = Parameter(name = 'CKM21',
                  nature = 'internal',
                  type = 'complex',
                  value = '-cmath.sin(cabi)',
                  texname = '\\text{CKM21}')

CKM22 = Parameter(name = 'CKM22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'cmath.cos(cabi)',
                  texname = '\\text{CKM22}')

CKM23 = Parameter(name = 'CKM23',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{CKM23}')

CKM31 = Parameter(name = 'CKM31',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{CKM31}')

CKM32 = Parameter(name = 'CKM32',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{CKM32}')

CKM33 = Parameter(name = 'CKM33',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{CKM33}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = 'ee**2/(4.*Gf*MW**2*cmath.sqrt(2))',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

v = Parameter(name = 'v',
              nature = 'internal',
              type = 'real',
              value = '(2*MW*sw)/ee',
              texname = 'v')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*v**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/v',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/v',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/v',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/v',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/v',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/v',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/v',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/v',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/v',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*v**2)',
                texname = '\\mu')

