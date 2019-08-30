with open("LOGINS", 'r') as file:
    LOGIN = file.readline()
    PASSWD = file.readline()

import vk_api


# True, if you want to like all the wall
# False, if you want to unlike all the wall
LIKE = True

# whom you want to like
USER_ID = '223304541'

vk_session = vk_api.VkApi(LOGIN, PASSWD)
vk_session.auth()

vk = vk_session.get_api()

lst = vk.wall.get(owner_id=USER_ID)['items']
qrs = []
for item in lst:
    qrs.append((item['from_id'], item['id']))

# print(qrs)

if LIKE:
    for item in qrs:
        vk.likes.add(owner_id=item[0], item_id=item[1], type='post')
        print('liked', item)
else:
    for item in qrs:
        vk.likes.delete(owner_id=item[0], item_id=item[1], type='post')
        print('unliked', item)
