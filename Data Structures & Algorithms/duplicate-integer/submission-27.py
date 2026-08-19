class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        seen = set()

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)


        return False   



# files = {}
# users = {}

# def upload(file_name, size):

#     if file_name in files:
#         return False
    
#     files[file_name] = size
#     return True

# def get(file_name):

#     if file_name not in files:
#         return None
#     return files.get(file_name)[0]

# def add_user(user_id, capacity):

#     if user_id in users:
#         return False
    
#     users[user_id] = capacity
#     return True

# def upload_by(user_id, file_name, size):
#     if user_id not in users or file_name in files or new_capacity < 0:
#         return False
    
#     new_cap = 0
#     cap = 0
#     if user_id in users:
#         cap = users.get(user_id) 
    
#     new_cap = cap - size
    
#     files[file_name] = (size, user_id)
#     users[user_id] = new_capacity
#     return new_capacity

# def merge_users(user_id_1, user_id_2):

#     if user_id_1 not in users or user_id_2 not in users or user_id_1 == user_id_2:
#         return False
    

#     users[user_id_1] += users[user_id_2]

#     for file_name, (size, owner) in files.items():
#         if owner == user_id_2:
#             files[file_name] = (size, user_id_1)  
        
#     if user_id_2 in users:
#         del users[user_id_2]
    
#     return users[users_id_1]

# def get_n_largest(prefix, n):

#     matches = []

#     for file_name, file_data in files.items():
#         sizes = file_data[0]
#         if file_name.startswith(prefix):
#             matches.append([file_name, sizes])
        
#     output = sorted(matches, key = lambda x :  (-x[1], x[0]))

#     res = []
#     for name, size in output[:n]:
#         res = [f"{name}({size})"]
#     return res

# testcases :

# print(upload("a.txt", 50)) # return True
# print(upload("ab.txt", 100)) # return True
# print(upload("abc.txt", 150)) # return True
# print(upload("abcd.txt", 250)) # return True

# print(get_n_largest(a, 3)) # returns ["abcd.txt(250)", "abc.txt(150)", "ab.txt(100)"]









