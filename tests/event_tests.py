import json
from levelupapi.models import gamer
from levelupapi.models.gamer import Gamer
from levelupapi.models.event import Event
from levelupapi.models.game import Game
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import GameType


class EventTests(APITestCase):
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
        
        game_type = GameType()
        game_type.label = "Board Game"
        game_type.save()

        game = Game()
        game.game_type_id = 1
        game.skill_level = 5
        game.name = "Clue"
        game.maker = "Milton Bradley"
        game.number_of_players = 6
        game.description = "It's a fun game"
        game.gamer_id = 1

        game.save()

    def test_create_event(self):
        url = '/events'
        data = {
            "game_type_id": 1,
            "game_id": 1,
            "date": "2021-10-31",
            "time": "12:00:00",
            "description": "Clue event",
            "title": "Clue You"
        }

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['date'], data['date'])
        self.assertEqual(response.data['time'], data['time'])
        self.assertEqual(response.data['description'], data['description'])

    def test_get_event(self):
        event = Event()
        event.game_id = 1
        event.game_type_id = 1
        event.host_id = 1
        event.date = "2021-10-31"
        event.time = "12:00:00"
        event.description = "Clue event"
        event.title = "Clue You"

        event.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.get(f'/events/{event.id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['date'], event.date)
        self.assertEqual(response.data['time'], event.time)
        self.assertEqual(response.data['description'], event.description)

    def test_update_event(self):
        event = Event()
        event.game_id = 1
        event.game_type_id = 1
        event.host_id = 1
        event.date = "2021-10-31"
        event.time = "12:00:00"
        event.description = "Clue event"
        event.title = "Clue You"

        event.save()

        data = {
            "game_id": 1,
            "game_type_id": 1,
            "host_id": 1,
            "date": "2021-10-31",
            "time": "12:00:00",
            "description": "Clue event",
            "title": "Clue You"
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.put(f'/events/{event.id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f"/events/{event.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["date"], data['date'])
        self.assertEqual(response.data["time"], data['time'])
        self.assertEqual(response.data["description"], data['description'])

    def test_delete_event(self):
        event = Event()
        event.game_id = 1
        event.game_type_id = 1
        event.host_id = 1
        event.date = "2021-10-31"
        event.time = "12:00:00"
        event.description = "Clue event"
        event.title = "Clue You"

        event.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.delete(f'/events/{event.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f"/events/{event.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)