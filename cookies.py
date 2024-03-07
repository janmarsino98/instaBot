import pickle

s = """ig_did=0C826C21-17C3-444A-ABB7-EBABD37214D7; dpr=0.9375; mid=Zekh3AALAAFVjqFoU9zyszwZzKc8; datr=2yHpZQuBdabcRd3RrWGGKJ7r; ps_l=0; ps_n=0; ig_lang=en; csrftoken=3OvPNMgW0ufdhgYFSTCSGFcAyPfU48e0; ds_user_id=212321299; sessionid=212321299%3Ajva5bkJ7svoA0g%3A22%3AAYc5BA42eorfTDwBQSm69AdRUETo_02DQ7QyiNH_UA; shbid=11064\054212321299\0541741313768:01f7360643f154e64ef0d0221344faf0542d96d108ee54585dee0c83a96770f97f3857af; shbts=1709777768\054212321299\0541741313768:01f7ba14516b0b32067a3e0c505ce08f504fb4e32d995a0de4bf5a395a8c1ce50d703b33; rur=CCO\054212321299\0541741314190:01f73b174540ff4922aa5449f5c5e8a16dc858aebdecb773a8deb4e62f0a4e553d259f4e"""

cookies = []
for cookie_pair in s.split('; '):
    name, value = cookie_pair.split('=', 1)  # Split on the first "=" only
    cookies.append({'name': name, 'value': value})

# Step 2: Save cookies to a .pkl file
with open('cookies.pkl', 'wb') as file:
    pickle.dump(cookies, file)