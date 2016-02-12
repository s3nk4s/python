# convert dec to hex with leading zeros
def makeHex(d):
    return "{0:#0{1}x}".format(d,6).split('x')[1]
    
# pad integer with 4 leading zeros    
def padNumber(i):
    return "%04d" % (i,)
    
# create column of hex characters for binary input
FILTER=''.join([(len(repr(chr(x)))==3) and chr(x) or '.' for x in range(256)])
def hexDump(src, length=16):
    N=0; result=''
    while src:
       s,src = src[:length],src[length:]
       hexa = ' '.join(["%02X"%ord(x) for x in s])
       s = s.translate(FILTER)
       result += "%04X   %-*s   %s\n" % (N, length*3, hexa, s)
       N+=length
    return '\n' + result
