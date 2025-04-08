# 19)
# Harf yoki pastki chiziq (_) bilan boshlanishi kerak.
# Keyingi belgilar harf, raqam, yoki pastki chiziq (_) bo‘lishi mumkin.
# Python'ning ajratilgan (reserved) so‘zlari identifikator bo‘la olmaydi (masalan, if, for, class va h.k.).

def indefikator(satr):
  if not satr:
    return False
  if not (satr[0].isalpha() or satr[0]=='_'):
    return False
  for a in satr[1:]:
    if not (a.isalnum() or a=='_'):
      return False
  return True
print(indefikator('my-name'))
