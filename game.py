from classes import Weapon, Armour, Character, Room, Hero, Dungeon, Shop, Enemy


stick = Weapon("stick", 15, 5)
tooth = Weapon("tooth", 40, 15)
scort = Weapon("scort", 75, 30)
gun = Weapon("gun", 250, 75)
boss_club = Weapon("boss_club", 0, 160)
laser_gun = Weapon("laser_gun", 460, 180)
sword = Weapon("sword", 125, 50)
minigun = Weapon("minigun", 200, 60)
magic_stick = Weapon("magic_stick", 45, 30)
laser_scorts = Weapon('laser_scorts', 150, 85)

allwep = [stick, tooth, scort, gun, boss_club, laser_gun, sword, minigun, magic_stick]

no_armour = Armour("no_armour", 0, 0)
leatherArmour = Armour("leatherArmour", 50, 5)
ironArmour = Armour("iron armour", 150, 10)
diamond_armour = Armour("diamond_armour", 225, 150)
diamond_armour_x2 = Armour('diamond_armour_x2', 450, 300)
goldArmour = Armour("goldArmour", 250, 80)
magicarmour = Armour('magicarmour', 500, 600)

allar = [leatherArmour, ironArmour, diamond_armour, diamond_armour_x2, goldArmour, magicarmour]

goblin = Enemy("goblin", 320, scort, ironArmour, 60, 80)
giantСockroach = Enemy("giantСockroach", 550, minigun, goldArmour, 81, 140)
hero = Hero("clever Ivan", 100, stick, no_armour, 0, 0, 100)
dumb_Ivan = Enemy("dumb_Ivan", 20, stick, no_armour, 10, 10)
big_rat = Enemy("big_rat", 30, tooth, no_armour, 18, 20)
skelleton = Enemy("skelleton", 180, laser_gun, diamond_armour, 35, 50)
boss_skelleton = Enemy('boss_skelleton', 800, boss_club, diamond_armour_x2, 150, 200)
mouse = Enemy('mouse', 25, minigun, no_armour, 11, 50)
trader = Shop("Vilam", [sword, goldArmour, gun, laser_gun, minigun], 400, allwep, allar)

room_1 = Room(1, dumb_Ivan)
room_2 = Room(2, big_rat)
room_3 = Room(3, skelleton)
room_4 = Room(4, goblin)
room_5 = Room(5, mouse)
room_6 = Room(6, giantСockroach)
room_7 = Room(6, boss_skelleton)




rooms_d1 = [room_1, room_2, room_3]
dungeon_1 = Dungeon(rooms_d1, 'rat_dungeon')
dungeon_1.dungeon_manager(hero, trader)
rooms_d2 = [room_4, room_5, room_6, room_7]
dungeon_2 = Dungeon(rooms_d1, 'skelleton_dungeon')
dungeon_2.dungeon_manager(hero, trader)