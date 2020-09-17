nick_file = open ('nick.txt', 'r')
print(nick_file.readline())
cnt=1
nick_file.close
# nick_file.write("\nHello\n")
# print(nick_file.read())
# nick_file.close
# numbers = [1,2,3]
# for i in range(len(numbers)):
#     num = numbers[i]
#     nick_file.write('{}\n'.format(num))

#     nick_file = open('nick.text', 'w')
#     nick_file.write('nick')
#     nick_file.close()
new_file = open('new_file.txt')
file_items = new_file.readlines()\
for i in range(len(file_items)):
    each_item = file_items[i]
    print('Before: {}'.format(each_item))
    print(each_item[0:-1])



