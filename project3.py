a = bytearray((12, 8, 25, 2))
print("Creating Bytearray")
print(a)

print("\nAccessing Elements:", a[1])

a[1] = 3
print("\nAfter Modifying")
print(a)

a.append(30)
print("\nAfter Adding Elements")
print(a)