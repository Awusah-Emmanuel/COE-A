current_users = ['alice', 'bob', 'charlie', 'dave', 'eve']
new_users = ['alice', 'bob', 'carol', 'dave', 'eve']

for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"The username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")

        