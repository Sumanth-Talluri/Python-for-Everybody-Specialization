str = 'X-DSPAM-Confidence:0.8475'

pos = str.find(':')
newstr = str[pos+1:]
print(float(newstr))
