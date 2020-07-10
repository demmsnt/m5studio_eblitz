import fortnitepy
import json
import os


email = 'eblitz.test1@gmail.com'
password = 'Ebl1tztest1'

# device_id = '25a36bcdfaf4494780a3ffabc8f5b430'
# account_id = 'd546a40182474da8a2aeefd3504adff9'
# secret = 'ZSURPLZQLZ6G4RCFG5YYTNLQFGKZOXLF'


# email = 'eblitz.test2@gmail.com'
# password = 'Ebl1tztest2'

# device_id = 'aa9fa72523724c5b91110ae8bb98f78e'
# account_id = 'd5750d40f25c4e1caf78a4b65f56f198'
# secret = 'TIZ5MSTXXRHASWBTKUTS3DHF6K6SIUPP'

filename = 'device_auths.json'

class MyClient(fortnitepy.Client):
    # Auth with: email, password
    def __init__(self):
        device_auth_details = self.get_device_auth_details().get(email, {})
        super().__init__(
            auth=fortnitepy.AdvancedAuth(
                email=email,
                password=password,
                prompt_authorization_code=True,
                delete_existing_device_auths=True,
                **device_auth_details
            )
        )

    # Auth with: device_id, account_id, secret
    # def __init__(self):
    #     device_auth_details = self.get_device_auth_details().get(email, {device_id: device_id, account_id: account_id, secret: secret})
    #     super().__init__(
    #         auth=fortnitepy.AdvancedAuth(
    #             **device_auth_details
    #         )
    #     )

    def get_device_auth_details(self):
        if os.path.isfile(filename):
            with open(filename, 'r') as fp:
                return json.load(fp)
        return {}

    def store_device_auth_details(self, email, details):
        existing = self.get_device_auth_details()
        existing[email] = details

        with open(filename, 'w') as fp:
            json.dump(existing, fp)

    async def event_device_auth_generate(self, details, email):
        self.store_device_auth_details(email, details)

    async def event_ready(self):
        print('----------------')
        print('Client ready as')
        print(self.user.display_name)
        print(self.user.id)
        print(dir(self.user))
        print('----------------')

    async def event_friend_request(self, request):
        await request.accept()

    async def event_friend_message(self, message):
        print('Received message from {0.author.display_name} | Content: "{0.content}"'.format(message))
        await message.reply('Thanks for your message!')


client = MyClient()
client.run()