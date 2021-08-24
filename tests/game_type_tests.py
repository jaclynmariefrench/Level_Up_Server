import json
from levelupapi.models.event import Event
from levelupapi.models.game import Game
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import GameType, game_type


class GameTypeTests(APITestCase):
    def setUp(self):
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }

        response = self.client.post(url, data, format='json')
        self.token = response.data['token']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_create_game_type(self):
    #     url = '/gametypes'
    #     data = {
    #         "label": "Horror RPG"
    #     }

    #     self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #     self.assertEqual(response.data['label'], data['label'])


    def test_get_game_type(self):
        game_type = GameType()
        game_type.label = "Horror RPG"

        game_type.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.get(f'/gametypes/{game_type.id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['label'], game_type.label)
 

    # def test_update_game_type(self):
    #     game_type = GameType()
    #     game_type.label = "Horror RPG"
    #     game_type.save()

    #     data = {
    #         "label": "Horror RPG"
    #     }

    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
    #     response = self.client.put(f'/gametypes/{game_type.id}', data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #     response = self.client.get(f"/gametypes/{game_type.id}")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     self.assertEqual(response.data["label"], data['label'])

    # def test_delete_game_type(self):
    #     game_type = GameType()
    #     game_type.label = "Horror RPG"

    #     game_type.save()

    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
    #     response = self.client.delete(f'/gametypes/{game_type.id}')
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #     response = self.client.get(f"/gametypes/{game_type.id}")
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)