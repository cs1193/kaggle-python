spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)


print(type(spam_amount))

print(type(19.95))

print(5 / 2)

print(6 / 2)

print(5 // 2)

print(6 // 2)

# PEMDAS

print(8 - 3 + 2)

print(-3 + 4 * 2)

# Order of operations

hat_height_cm = 25
my_height_cm = 190

total_height_meters = hat_height_cm + my_height_cm / 100
print("Wrong Height in meters = ", total_height_meters)

total_height_meters_mod = (hat_height_cm + my_height_cm) / 100;
print("Height in meters = ", total_height_meters_mod)

# Builtin functions
print(min(1, 2, 3))
print(max(1, 2, 3))

print(abs(32))
print(abs(-32))

print(float(10))
print(int(3.33))
print(int('807') + 1)