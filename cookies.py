import pickle

s = """"""

cookies = []
for cookie_pair in s.split('; '):
    name, value = cookie_pair.split('=', 1)  # Split on the first "=" only
    cookies.append({'name': name, 'value': value})

# Step 2: Save cookies to a .pkl file
with open('cookies.pkl', 'wb') as file:
    pickle.dump(cookies, file)