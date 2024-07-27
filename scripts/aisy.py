# def can_partition(classrooms, c, group_size):
#     if c == 0:
#         return False
#     dp = [False] * (group_size + 1)
#     dp[0] = True
    
#     for size in classrooms:
#         for j in range(group_size, size - 1, -1):
#             dp[j] = dp[j] or dp[j - size]
    
#     return dp[group_size]

# def can_distribute_chocolates(classrooms):
#     total_students = sum(classrooms)
    
#     # Check if total_students is divisible by 3
#     if total_students % 3 != 0:
#         return "Ohoo"
    
#     group_size = total_students // 3
    
#     # We need to check if we can partition the classrooms into 3 groups each of size group_size
#     if can_partition(classrooms, len(classrooms), group_size) and \
#        can_partition(classrooms, len(classrooms), group_size) and \
#        can_partition(classrooms, len(classrooms), group_size):
#         return "Yahoo"
    
#     return "Ohoo"

# # # Read input
# # c = int(input())
# # classrooms = [int(input()) for _ in range(c)]

# classrooms=[3,2,3,1]
# # Print the result
# print(can_distribute_chocolates(classrooms))

def can_partition(classrooms, target, k, memo):
    if k == 0:
        return target == 0
    if target == 0:
        return can_partition(classrooms, sum(classrooms) // 3, k - 1, memo)
    if (tuple(classrooms), target, k) in memo:
        return memo[(tuple(classrooms), target, k)]
    
    for i in range(len(classrooms)):
        if classrooms[i] <= target:
            new_classrooms = classrooms[:i] + classrooms[i+1:]
            if can_partition(new_classrooms, target - classrooms[i], k, memo):
                memo[(tuple(classrooms), target, k)] = True
                return True
    
    memo[(tuple(classrooms), target, k)] = False
    return False

def chocolate(classrooms):
    total_students = sum(classrooms)
    
    # Check if total_students is divisible by 3
    if total_students % 3 != 0:
        return "Ohoo"
    
    group_size = total_students // 3
    memo = {}
    
    if can_partition(classrooms, group_size, 3, memo):
        return "Yahoo"
    
    return "Ohoo"

# # Example usage
# c = int(input())
# classrooms = [int(input()) for _ in range(c)]
classrooms=[3,2,3,1]
print(chocolate(classrooms))
