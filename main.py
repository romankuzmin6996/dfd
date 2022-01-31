def reverseWords(teksts: str):
  sar1 = teksts.split()
  if len(sar1)>1:
    sar1.reverse()
    teksts=""
    for elements in sar1:
      teksts+=elements
  else:
    teksts = "Parak iss teikums!"
  return teksts

a = reverseWords("")
print(a)