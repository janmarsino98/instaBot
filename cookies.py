import pickle

s = """mid=Ze7J3wALAAGawu2MaBxjm_sc23iE; ig_did=0C826C21-17C3-444A-ABB7-EBABD37214D7; ps_l=0; ps_n=0; dpr=1.125; datr=4MnuZU9aIjg_m90UpJn2b5gF; csrftoken=mD98bho1B0AxoDpJHCVOEivU5PkLmyrk; ds_user_id=212321299; sessionid=212321299%3AXDi6mGUeJgFnCj%3A23%3AAYfQ9_3rHNnMfmZLX6pHtwbk06gO3z9KLKZ0631Xfg; shbid="11064\054212321299\0541741684350:01f7d37bc536588d9f529f94498f2545ba9c1d5a5be527e09fdd1a971fb4d0f54fa9499c"; shbts="1710148350\054212321299\0541741684350:01f7a8d2baf4b481dd6ed005192c871329afccbf68ece5c575daf03e2934cfc0a3306877"; rur="PRN\054212321299\0541741684372:01f7b3ad2a9fa8369cdbf91536bc6711782b599f54360af7f2fc0fc3e8f1ea23ea5a0c45"""
cookies = []
for cookie_pair in s.split('; '):
    name, value = cookie_pair.split('=', 1)  # Split on the first "=" only
    cookies.append({'name': name, 'value': value})

# Step 2: Save cookies to a .pkl file
with open('cookies.pkl', 'wb') as file:
    pickle.dump(cookies, file)