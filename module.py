def mail(a):
  ch=a.find('@gmail.com')
  return True if a[ch:ch+10] == "@gmail.com" else False
