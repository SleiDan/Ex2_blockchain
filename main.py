def from_hex_to_le(num, counter):
    while num[counter] == '0':
        counter = counter - 2
    ans = num[:counter + 1]
    if counter % 2 == 0:
        return ans + '0'
    else:
        return ans


print('Введите hex для конвертации: ')
num = input()
print('Кол-во байтов:')
length = len(num[2:]) // 2
print(length)
print('Конвертация из hex в little-endian:')
l_e = int(from_hex_to_le(num, len(num) - 1), 16)
print(l_e)
print('Конвертация из hex в big-endian:')
b_e = int(num, 16)
print(b_e)
print('Конвертация из little-endian в hex:')
hex_l_e = hex(l_e) + '0' * (2 * (length - len(str(l_e)) + 2))
print(hex_l_e)
print('Конвертация из big-endian в hex:')
hex_b_e = hex(b_e)
print(hex_b_e)