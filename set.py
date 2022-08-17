# Set
#   Değiştirilebilir.
#   Sırasız + Eşsizdir.
#   Kapsayıcıdır.
set1 = set([1, 3, 5])
set2 = set([1, 2, 3])
# set1'de olup set2'de olmayanlar.
print(set1.difference(set2))
# set2'de olup set1'de olmayanlar.
print(set2.difference(set1))
# Matematiksel ifadelerle birlikte kullanabiliriz. Difference için "-" kullanılır.
print(set1 - set2)
# İki kümede de birbirlerine göre olmayanlar = symmetric_difference()
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))
# İki kümenin kesişimi = intersection()
print(set1.intersection(set2))
print(set2.intersection(set1))
# Matematiksel ifadelerle birlikte kullabiliriz. Kesişim için "&" kullanılır.
print(set1 & set2)
# İki kümenin birleşimi = union()
print(set1.union(set2))
# İki kümenin kesişimi boş mu? = isdisjoint() - True/False çıktısı gelir.
set3 = set([7, 8 ,9])
set4 = set([5, 6, 7, 8, 9, 10])
print(set3.isdisjoint(set4))
# Bir küme diğer kümenin alt kümesi mi? = issubset()
print(set3.issubset(set4))
print(set4.issubset(set3))
# Bir küme diğer kümeyi kapsıyor mu? = issuperset()
print(set4.issuperset(set3))
print(set3.issuperset(set4))
