def is_anagram(s, t):
  # Eğer iki dize farklı uzunlukta ise, anagram olamazlar
  if len(s) != len(t):
    return False
  
  # Her iki dizeyi de küçük harfe çevir
  s = s.lower()
  t = t.lower()

  # Her iki dize için harf sayısını sayan bir sözlük oluştur
  s_count = {}
  t_count = {}

  # s dizisindeki her harf için sayacı artır
  for c in s:
    if c in s_count:
      s_count[c] += 1
    else:
      s_count[c] = 1
  
  # t dizisindeki her harf için sayacı artır
  for c in t:
    if c in t_count:
      t_count[c] += 1
    else:
      t_count[c] = 1
  
  # Eğer iki sözlük eşit değilse, anagram değildir
  return s_count == t_count

# Kullanıcıdan iki dize girmesini iste
s = input("Birinci dizeyi giriniz: ")
t = input("İkinci dizeyi giriniz: ")

# Fonksiyonu çağır ve sonucu yazdır
print(is_anagram(s, t))
