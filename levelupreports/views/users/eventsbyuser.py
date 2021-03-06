from levelupapi.models.event import Event
import sqlite3
from django.shortcuts import render
from levelupapi.models import Game
from levelupreports.views import Connection
from datetime import datetime

def events_by_user(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute(
                """
                select g.id as user_id,
                u.first_name || " " || u.last_name as full_name,
                e.id,
                e.date,
                e.time,
                e.title,
                e.description,
                e.host_id,
                gm.name as game_name
                from levelupapi_event e
                join levelupapi_eventgamer eg
                on e.id = eg.event_id
                join levelupapi_gamer g
                on g.id = eg.gamer_id
                join auth_user u
                on u.id = g.user_id
                join levelupapi_game gm
                on e.game_id = gm.id
                """
            )

            dataset = db_cursor.fetchall()

            events_by_user = {}

            for row in dataset:
                # Crete a Event instance and set its properties
                event = Event()
                event.date = row["date"]
                event.time = row["time"]
                event.title = row["title"]
                event.host_id = row["host_id"]
                event.game_name = row["game_name"]
                event.description = row["description"]

                # Store the user's id
                uid = row["user_id"]

                # If the user's id is already a key in the dictionary...
                if uid in events_by_user:

                    # Add the current game to the `games` list for it
                    events_by_user[uid]['events'].append(event)

                else:
                    # Otherwise, create the key and dictionary value
                    events_by_user[uid] = {}
                    events_by_user[uid]["id"] = uid
                    events_by_user[uid]["full_name"] = row["full_name"]
                    events_by_user[uid]["events"] = [event]


    events = events_by_user.values()
    template = "users/list_with_events.html"
    context = { "user_with_events": events }
    return render(request, template, context)
