import hashlib


class Requsts:

    def parse(self, data):
        users = []
        metod = data.split(' ')[0]
        if metod == 'POST':
            temp_data = data.split('\n')[-1]
            temp_users = temp_data.split('&')
            for item in temp_users:
                users.append(item.split('=')[1])
            users[1] = '@'.join(users[1].split('%40'))
        path = data.split(' ')[1]
        if len(users) == 3:
            pass_user = users[2]
            users[2] = hashlib.md5(pass_user.encode('utf-8')).hexdigest()
        req = [path, metod]
        return req, users
