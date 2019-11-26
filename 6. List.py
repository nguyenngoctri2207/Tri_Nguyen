#Để khai báo một list trong Python thì chúng ta sử dụng cặp dấu [] và bên trong là các giá trị của list.
name = ["Nguyễn Ngọc Trí","Lê Văn Hải","Lê Văn Đức"]
# list được đánh dấu bắt đầu từ 0 theo chiều từ trái sang phải và từ -1 theo chiều từ phải qua trái.
print(name[0])
print(name[1])
print(name[2])
#hoặc
print(name[-3])	
print(name[-2])
print(name[-1])
# in ra một phần của list
print(name[0:3])
#Sửa đổi và xóa bỏ giá trị phần tử trong list.
#update
name[0]=2222222222
print(name)
#delete
del name[0:1] # xóa 1 giá trị
print(name)
#List lồng nhau.
dateofbirth = [22,7,1996]
mylist=[dateofbirth,name[0]] 
print(mylist)



