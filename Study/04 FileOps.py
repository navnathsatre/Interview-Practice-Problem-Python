'''
with open(filename,mode) as fh:
    pass
mode:
r: reading file if not error will be there read(), readline(), readlines()

w: open for write if not it will create (overwrite) write(), writelines()

a same as write but it will not remove pre data

r+

w+

rb

wb
'''
# with open("day.txt",'r') as fo:
#     # print(fo.read()) # read all content
#     # print(fo.readline(3), end='') #readline(no. of char)
#     # print(fo.readlines()) # o/p : list of elements
#     for day in fo.readlines()[1:6]:
#         print(day[:3].upper(),end=')

# with open(r'D:\data\tech.txt') as fo:
#     pass

# with open('tech.txt', 'w') as fh:
#     # fh.write(("Data Analytics"))
#     # fh.write(("Data Analytics", "PowerBI")) # error
#     fh.writelines(['Data Analytics\n','PowerBI'])

# with open('tech.txt', 'a') as fh:
#     fh.writelines(['\nMySql\n','R'])

# with open('day.txt','r+') as fh:
#     print(fh.read())
#     fh.writelines(['AI','ML\n','DL'])

# with open('day.txt','w+') as fh:
#     fh.writelines(['Pune\n','Mumbai\n','Hyderabad'])
#     fh.seek(0,0)
#     print(fh.read())

# with open('day.txt') as rf:
#     with open('city.txt', 'a') as wf:
#         data = rf.readlines()
#         wf.writelines(data[:2])
#         wf.writelines(['Cochi\n','konkatta\n'])
#         wf.writelines(data[2:])

# with open(r'C:\User\puppy.jpg','r') as pp: # image data so error
#     print(pp.read())

# with open(r'C:\User\puppy.jpg','rb') as pp:
#     print(pp.read())

with open(r'C:\User\puppy.jpg','rb') as pp:
    with open(r'C:\User\puppy.jpg','wb') as p :
        print(p.raad())

