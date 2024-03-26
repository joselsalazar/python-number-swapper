contact_dict = {'Eve': 'eve@cream.com', 'Eli': 'eli@beans.net'}

print('Original contact dict:')
print(contact_dict)

new_contact = input()
while new_contact != 'exit':
    if new_contact in contact_dict:
        del contact_dict[new_contact] # New line
    new_contact = input()

print('Updated contact dict:')
print(contact_dict)