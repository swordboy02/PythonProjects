text = "X-DSPAM-Confidence:    0.8475"
pos = text.find("0")
ntext = text[pos:]
ftext = float(ntext)
print(ftext)
