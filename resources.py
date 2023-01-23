import cv2 as cv
import pygame


def scale_images(square_size):
    dim = (square_size, square_size)

    for t in textures:
        img = cv.imread(t[0])
        img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        tile_mapper[t[1]] = img

    for e in entities:
        img = pygame.image.load(e[0]).convert_alpha()
        img = pygame.transform.scale(img, dim)
        entity_mapper[e[1]] = img


textures = [
    ("assets/textures/rock_tileable.png", "Rock"),
    ("assets/textures/wood_planks_tileable.png", "Wood"),
    ("assets/textures/moss_tileable.png", "Moss"),
    ("assets/textures/stone_bricks_tileable.png", "Stone bricks"),
    ("assets/textures/smooth_stone_tileable.png", "Smooth stone"),
    ("assets/textures/dark_smooth_stone_tileable.png", "Dark smooth stone"),
    ("assets/textures/dark_smooth_stone_with_puddle_tileable.png", "Dark smooth stone with puddle"),
    ("assets/textures/Cobblestone.jpg", "Cobblestone"),
    ("assets/textures/Grass_Marsh.jpg", "Grass marsh"),
    ("assets/textures/Rectangular_Tiles.jpg", "Rectangular tiles"),
    ("assets/textures/Rock_Ground_01.jpg", "Rock ground A"),
    ("assets/textures/Rock_Ground_02.jpg", "Rock ground B"),
    ("assets/textures/Rock_Texture_01.jpg", "Rock texture A"),
    ("assets/textures/Rock_Texture_02.jpg", "Rock texture B"),
    ("assets/textures/Rock_Tiles_Mossy.jpg", "Rock tiles mossy"),
    ("assets/textures/Square_Cobblestone.jpg", "Square cobblestone")
]
entities = [
    ("assets/entities/player.png", "Player spawn point", 1),
    ("assets/entities/rock.png", "Rock", 2),
    ("assets/entities/hole.png", "Hole", 3)
]

tile_mapper = dict()
entity_mapper = dict()
