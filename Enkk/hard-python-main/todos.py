import requests
from prettytable import PrettyTable

# work on the users
url = "https://jsonplaceholder.typicode.com/users"
users = requests.get(url).json()

userid_to_name = {}
for user in users:
    userid_to_name[str(user["id"])] = user["username"]


# work on the todos
url = "https://jsonplaceholder.typicode.com/todos"
todos = requests.get(url).json()

users_todo = {}
for todo in todos:
    name = userid_to_name[str(todo["userId"])]
    if name in users_todo.keys():
        users_todo[name].append(todo)
    else:
        users_todo[name] = [todo]


# print todo e stato per ogni utente

for user, todos in users_todo.items():
    p = PrettyTable()
    p.field_names = [user, "TODO status"]
    p.add_row([user, ""])
    for todo in todos:
        p.add_row([todo["title"], todo["completed"]])
    print(p)
