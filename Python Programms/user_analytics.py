num_users = int(input('Enter number of users: '))
user_analytics = {'username': [], 'age': [], 'email': []}
user_list = []

for i in range(num_users):
    username = input("Enter username: ")
    age = int(input("Enter user age: "))
    email = input("Enter user email: ")
    user_analytics['username'].append(username)
    user_analytics['age'].append(age)
    user_analytics['email'].append(email)
    user_dict = {'username' : username, 'age' : age, 'email' : email}
    user_list.append((i + 1, user_dict))

print(user_list)
print(user_analytics)