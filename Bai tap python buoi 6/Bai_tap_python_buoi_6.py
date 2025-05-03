
#Tuple
#1
# numbers = (10, 100, 24, 40, 100)
# print("Phan tu thu 3:", numbers[2])

#2
# tuple_data = (1, 2, 3)
# a, b, c = tuple_data
# print(a, b, c)

#3
# original_tuple = (1, 2, 3)
# them_phan_tu = 4
# updated_tuple = original_tuple + (them_phan_tu,)
# print(updated_tuple)

#4
# my_tuple = (1, 2, 3, 4, 5, 6)
# chi_so = my_tuple.index(6)
# print("Chi so cua phan tu 6:", chi_so)

#5
# from collections import Counter

# my_tuple = (10, 10, 2, 3, 4, 10)
# counter = Counter(my_tuple)
# repeated_items = [item for item, count in counter.items() if count > 1]

# print("Cac phan tu lap lai:", repeated_items)

#Set
#1
# numbers = {10, 2, 3, 7,6}
# print("Gia tri lon nhat:", max(numbers))
# print("Gia tri nho nhat:", min(numbers))

#2
# my_set = {5, 10, 25, 100, 44}
# value = 25

# if value in my_set:
#     print(value, "co trong set.")
# else:
#     print(value, "khong co trong set.")

#3
# set1 = {1, 10, 15}
# set2 = {10, 22, 55}

# if set1.isdisjoint(set2):
#     print("Khong co phan tu chung.")
# else:
#     print("Co phan tu chung")

#4
# from collections import Counter

# string_list = ["apple", "banana", "apple", "orange", "banana", "kiwi", "apple"]
# tu_duy_nhat = set(string_list)
# word_count = Counter(string_list)

# print("Tu duy nhat:", tu_duy_nhat)
# print("So lan xuat hien:")
# for word in tu_duy_nhat:
#     print(f"{word}: {word_count[word]}")

#5
# set_a = {10, 11, 12, 13, 14}
# set_b = {14, 15, 16, 17, 18}

# missing_in_b = set_a - set_b
# missing_in_a = set_b - set_a

# print("Cac so co trong A nhung khong trong B:", missing_in_b)
# print("Cac so co trong B nhung khong trong A:", missing_in_a)

#Dict
#1
# keys = ['dish', 'price', 'available']
# values = ['Bun bo', 45000, True]
# result = dict(zip(keys, values))
# print("Dictionary:", result)

#2
# student_info = {'name': 'Han', 'age': 20}
# diem = {'toan': 7, 'tieng anh': 8}
# merged = student_info.copy()
# merged.update(diem)
# print("Merged dictionary:", merged)

#3
# sample_dict = {
#   "class": {
#     "student": {
#       "name": "Han",
#       "marks": {
#         "english": 7,
#         "history": 8
#       }
#     }
#   }
# }
# print("Gia tri cua 'history':", sample_dict["class"]["student"]["marks"]["history"])

#4
# employees = ['Phuong', 'Thanh']
# defaults = {"designation": "Giao vien", "salary": 7000000}
# dict_with_defaults = dict.fromkeys(employees, defaults)
# print(dict_with_defaults)

#5
# sample_dict = {
#     "ten": "Thanh",
#     "tuoi": 20,
#     "thu lao": 2000,
#     "que quan": "Ninh Thuan"
# }
# keys = ["ten", "thu lao"]
# new_dict = {k: sample_dict[k] for k in keys}
# print( new_dict)

#6
# sample_dict = {
#      "ten": "Thanh",
#      "tuoi": 20,
#     "thu lao": 2000,
#     "que quan": "Ninh Thuan"
# }
# keys_to_remove = ["ten", "thu lao"]
# for k in keys_to_remove:
#     sample_dict.pop(k, None)
# print( sample_dict)

#7
# sample_dict = {'ten': 'Han', 'tuoi': '20', 'nghe nghiep': 'sinh vien'}
# value_to_check = '20'
# exists = value_to_check in sample_dict.values()
# print(exists)

#8
# sample_dict = {'ten': 'Han', 'tuoi': 20}
# sample_dict['ho_va_ten'] = sample_dict.pop('ten')
# print( sample_dict)

#9
# sample_dict = {'Hoa': 2, 'Anh': 5, 'Toan': 10}
# min_key = min(sample_dict, key=sample_dict.get)
# print(min_key)

#10
# sample_dict = {
#     'pho': {'ten': 'Pho bo', 'gia': 40000},
#     'bun_bo': {'ten': 'Bun bo', 'gia': 45000}
# }

# sample_dict['pho']['gia'] = 50000

# print(sample_dict)

#11
# paragraph = "Apple"
# char_count = {}
# for char in paragraph:
#     if char != " ":
#         char_count[char] = char_count.get(char, 0) + 1
# print(char_count)

#12
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# N = 10
# primes = [x for x in range(2, N) if is_prime(x)]
# prime_dict = {i+1: p for i, p in enumerate(primes)}
# print(prime_dict)

# Restructuring the company data
employees = {
    1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
    1002: {"name": "Bob", "department": "Sales", "salary": 50000},
    1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
    1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
    1005: {"name": "Eve", "department": "Sales", "salary": 55000}
}

dept_employees = {}

for emp_id, info in employees.items():
    dept = info["department"]
    if dept not in dept_employees:
        dept_employees[dept] = {}
    dept_employees[dept][emp_id] = {
        "name": info["name"],
        "salary": info["salary"]
    }

print(dept_employees)








