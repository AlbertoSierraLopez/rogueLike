#!/usr/bin/env python3
import tcod

from engine import Engine
from input_handlers import EventHandler
from entity import Entity
from game_map import GameMap


def main():
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    keep_running = True

    tileset = tcod.tileset.load_tilesheet("data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {player, npc}

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True

    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while keep_running:

            engine.render(root_console, context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == '__main__':
    main()
