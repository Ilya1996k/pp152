# 19
# def f(a, p):
#     if a >= 627 and p == 3: return True
#     if a >= 627 and p == 2: return False
#     if a < 627 and p == 3: return False
#     if p % 2 == 0:
#         return f(a + 3, p + 1) or f(a + 4, p + 1) or f(a ** 2, p + 1)
#     else:
#         return f(a + 3, p + 1) and f(a + 4, p + 1) and f(a ** 2, p + 1)
#
#
# for s in range(1, 200):
#     if f(s, 1):
#         print(s)

# 20
# def f(a, p):
#     if a >= 627 and p == 4: return True
#     if a >= 627 and p == 3: return False
#     if a < 627 and p == 4: return False
#     if p % 2 != 0:
#         return f(a + 3, p + 1) or f(a + 4, p + 1) or f(a ** 2, p + 1)
#     else:
#         return f(a + 3, p + 1) and f(a + 4, p + 1) and f(a ** 2, p + 1)
#
#
# for s in range(1, 200):
#     if f(s, 1):
#         print(s)

# 21 (ВЫЧЕРКНУТЬ ЧИСЛА ИЗ 19)
# def f(a, p):
#     if a >= 627 and (p == 3 or p == 5): return True
#     if a >= 627 and (p == 2 or p == 4): return False
#     if a < 627 and p == 5: return False
#     if p % 2 == 0:
#         return f(a + 3, p + 1) or f(a + 4, p + 1) or f(a ** 2, p + 1)
#     else:
#         return f(a + 3, p + 1) and f(a + 4, p + 1) and f(a ** 2, p + 1)
#
#
# for s in range(1, 200):
#     if f(s, 1):
#         print(s)