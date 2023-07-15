import os
from instagrapi import Client
from dotenv import load_dotenv


class InstagramParserAPI:

    def __init__(self, username: str,
                 password: str):
        self.cl = Client()
        self.cl.login(username=username, password=password)

    def get_photos(self,
                   username: str,
                   max_count: int) -> dict[str, list[str]]:
        user = self.cl.user_info_by_username(username)
        medias = self.cl.user_medias(user_id=int(user.pk),
                                     amount=max_count)

        return {'urls': [f"https://instagram.com/p/{media.code}" for media in medias]}


load_dotenv()
instagramParserAPI = InstagramParserAPI(os.environ['API_USERNAME'],
                                        os.environ['API_PASSWORD'])
