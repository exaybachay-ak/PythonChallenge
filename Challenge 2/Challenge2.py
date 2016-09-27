# found answer here: http://www.tutorialspoint.com/python/string_maketrans.htm

# transform text by 2 characters to solve
# evaluate character - if a - z, transform, else go to next character
#import re
import string
from string import maketrans

intab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
outtab = "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB"
trantab = maketrans(intab, outtab)

bla = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

print (bla.translate(trantab))

# answer is ocr.html

### CODE BELOW DOESNT WORK -- TRIED IT BUT WAS FOR DIFFERENT PYTHON VERSION

#def make_rot_n(n):
# lc = string.lowercase
# trans = string.maketrans(lc, lc[n:] + lc[:n])
# return lambda s: string.translate(s, trans)

#rot2 = make_rot_n(2)

#rot2(Paragraph)

#def rotChars():
#	#bla = " ".join(re.findall("[a-zA-Z]+", Paragraph))
#	#print bla
#	bla = string.lowercase
#	trans = string.maketrans(bla, bla[13:] + bla[:13])
#	print trans
#	return lambda s: string.translate(s, trans)
	
#rotChars()

#rot13 = bla.maketrans(
#    b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
#    b"cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB")
#b"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj".translate(rot13)