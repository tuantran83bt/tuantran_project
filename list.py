'''
List trong Python được định nghĩa là 1 dạng danh sách các phần tử \
chứa trong nó. bap gồm giá trị và vị trí chứa nó, vị trí là index\
và vị trí đầu tiên từ số 0 tiến tới và vị trí cuối cùng là -1 đếm \
lùi. List được định dạng bằng dấu ngoặc vuông []. \
Bên dưới là các hàm xữ lý list.
'''
list_1 = [1, 2, "3", True, None]# Create list chứa các dạng kiểu dữ liệu 
list_2 = list()# tạo 1 empty list_2
list_3 =[]# tạo 1 empty list-3
len(list_1)# Hàm len kiểm tra độ dài của list
list_1[2]# Lấy giá trị phần tử trong list bằng index vị trí
list_1[3] # lấy giá trị ở vị trí thứ 2, 3 trong list
list_1.index("3")# Tìm vị trí phần tử nằm ở đâu
list_1.count(2)# Đếm có bao nhiêu số 2 trong list
"Hàm for dùng để lấy tất cả giá trị trong list"
for item in list_1:
    print(item)# Hàm for để lấy ra hết các giá trị trong list
for vitri, giatri in enumerate(list_1, start=1): 
# (Hàm enumerate dùng để lấy cả vị trí và giá trị trong list_1
# tham số start =1 để thay thế vị trí đầu tiên là 1
    print(f"thứ tự {vitri} và giá trị là {giatri}")
    # in ra dạng f - string
    print('Thứ tự %s và giá trị là %s'% (vitri, giatri))
    # In ra dạng % biến
    print("Thứ tự {} và giá trị là {}".format(vitri, giatri))
    # In ra định dạng format
"Cắt dữ liệu trong list (Slicing) [start : end : step]"
new_list = [0,1,2,3,4,5,6]
new_list[3:]# start: bắt đầu từ vị trí số 1 <=> start 3 in ra [3,4,5,6]
new_list[:2]# end: Kết thúc từ vị trí số 2 <=> end 2, in ra [1,2]
new_list [-1]# truy cập vị trí cuối cùng trong list
new_list[::] # lấy toàn bộ các phần tử trong list ra
new_list[::2]# step: Bỏ qua (nhảy cóc) theo vi trí phần tử trong list
new_list[::-1]# đảo lại các phần tử trong list in ra [6,5,4,3,2,1]
"Các hàm thêm vào phần tử trong  list"
new_list*2 # nhân đôi các phần tử trong list[1,2,3,4,5,6,1,2,3,4,5,6]
new_list +[7,"End"]# Thêm phần tử vào list mới và không thây đổi list cũ
new_list.append(7)# Thêm 1 phần tử vào list ở vị trí cuối cùng
new_list.extend([8,9,10])# thêm nhiều phần tử vào list vị trí cuối
new_list.insert(0,"Bắt đầu")# thêm phần tử vào vị trí định sẵn trong list
"Xóa phần tử trong list"
new_list.pop()# xóa phần tử cuối cùng trong list
new_list.pop(1) # xóa phần tử ở vị trí số 1 trong list
new_list.remove(6)# (xóa giá trị đầu tiên trong list, <=> xóa số 6 trong list
# ví dụ trong list có nhiều số 6 thì chỉ xóa số 6 đầu tiên trong list
del new_list[0]# Hàm del xóa vị trí phần tử chỉ định
"Sắp xếp các phần tử trong list và giữ nguyên list cũ"
new_list.sort()# Sắp xếp các phần tử theo giá trị tăng dần
new_list.sort(reverse=True)# sắp xếp theo thứ tự giảm dần
new_list.reverse()# Đảo thứ tự trong list
"Sắp xếp các phần tử trong list và tạo list mới"
print(sorted(new_list))# Tạo ra 1 list mới có giá trị phần tử tăng dần
print(list(reversed(new_list)))# tạo ra list mới có giá trị đảo ngược với list cũ
"Tìm số lớn nhất trong list(dành cho số)"
print(max(new_list))# tìm số lớn nhất
print(min(new_list))# Tìm số nhỏ nhất
print(sum(new_list))# Tổng tất cả các số trong list

print(new_list)
"End..."









