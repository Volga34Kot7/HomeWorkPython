# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

predicate = [True, False]
for x in predicate:
    for y in predicate:
        for z in predicate:
            res = not (x or y or z) == (not x) and (not y) and (not z)
            print('X=', x, 'Y=', 'Z=', z, ':' '¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z' '=', res)