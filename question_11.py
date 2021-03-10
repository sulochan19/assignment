# 11. Create a variable, filename. Assuming that it has a three-letter
# extension, and using slice operations, find the extension. For
# README.txt, the extension should be txt. Write code using slice
# operations that will give the name without the extension. Does your
# code work on filenames of arbitrary length?

file_name='README.txt'
list=list(file_name)
index=list.index('.')
sliced=slice(index+1,len(file_name))
print(file_name[sliced])

name_sliced=slice(0,index)
print(file_name[name_sliced])

#yes the code works for arbitrary length