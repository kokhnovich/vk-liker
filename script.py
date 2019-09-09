# whom you want to like
USER_ID = '-22079806'


# True, if you want to like all the wall
# False, if you want to unlike all the wall
LIKE = True


# time between likes
# in seconds
TIMEOUT = 0.5

with open("LOGINS", 'r') as file:
    LOGIN = file.readline()
    PASSWD = file.readline()


import vk_api


def captcha_handler(captcha):
    """ При возникновении капчи вызывается эта функция и ей передается объект
        капчи. Через метод get_url можно получить ссылку на изображение.
        Через метод try_again можно попытаться отправить запрос с кодом капчи
    """

    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)



vk_session = vk_api.VkApi(LOGIN, PASSWD, captcha_handler=captcha_handler)
vk_session.auth()

vk = vk_session.get_api()

lst = vk.wall.get(owner_id=USER_ID)['items']
qrs = []
for item in lst:
    qrs.append((item['from_id'], item['id']))

print(qrs)

from time import sleep

if LIKE:
    for item in qrs:
        if str(item[0]) == str(USER_ID):
            vk.likes.add(owner_id=item[0], item_id=item[1], type='post')
            print('liked', item)
            sleep(0.05)
else:
    for item in qrs:
        if str(item[0]) == str(USER_ID):
            vk.likes.delete(owner_id=item[0], item_id=item[1], type='post')
            print('unliked', item)
            sleep(0.05)
