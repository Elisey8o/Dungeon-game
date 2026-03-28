from random import randint, choice
import time

class Weapon:
    def __init__(self, name, cost, damage):
        self.name = name
        self.cost = cost
        self.damage = damage
    def __str__(self):
        return f'{self.name}, cost: {self.cost}, damage: {self.damage}'

class Armour:
    def __init__(self, name, cost, defence):
        self.name = name
        self.cost = cost
        self.defence = defence
    def __str__(self):
        return f'{self.name}, cost: {self.cost}, defence: {self.defence}'

class Character:
    def __init__(self, name, hp, weapon, armour):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armour = armour

    def is_alive(self):
        if self.hp < 1:
            return False
        else:
            return True

class Enemy(Character):
    def __init__(self, name, hp, weapon, armour, scoreP, money):
        super().__init__(name, hp, weapon, armour)
        self.scoreP = scoreP
        self.money = money

class Hero(Character):
    def __init__(self, name, hp, weapon, armour, ballance, score, max_hp):
        super().__init__(name, hp, weapon, armour)
        self.ballance = ballance
        self.score = score
        self.inventory = []
        self.max_hp = max_hp
    
    def show_hero_inventory(self):
        print('Your inventory:')
        for i in range(len(self.inventory)):
            print(f'{i + 1}. {self.inventory[i].name}')
        print(f'Your ballance: {self.ballance}')

    def hp_hill(hp, ballance):
        pass

    def inventory_manager(self):
        self.show_hero_inventory()
        while True:
            answer = input("What do you want? (a - change item, x - exit): ")
            if answer == 'a':
                self.change_item()
            if answer == 'x':
                print('Loading...')
                time.sleep(randint(1, 4))
                break
            else:
                pass

    def change_item(self):
        self.show_hero_inventory()
        answer = input(f'Print item number from 1 to {len(self.inventory)} or x (exit): ')
        
        if answer == 'x':
            print('Loading...')
            time.sleep(randint(1, 4))
            return
        
        elif isinstance(self.inventory[int(answer) - 1], Weapon):
            self.inventory.append(self.weapon)
            self.weapon = self.inventory[int(answer) - 1]

        elif isinstance(self.inventory[int(answer) - 1], Armour):
            self.inventory.append(self.armour)
            self.armour = self.inventory[int(answer) - 1]

        
class Room:
    def __init__(self, id, enemy):
        self.id = id
        self.enemy = enemy

    def enter_room(self, hero):
        print(f"You are entered the room {self.id}. There is enemy {self.enemy.name}.")
        self.start_fight(hero)

    def start_fight(self, hero):
        while self.enemy.is_alive():    
            action = input(f"Choose your action: a - attac, s - drink potion (cost: 150, hill: 70 HP, your ballance: {hero.ballance}): ")
            if action == "a":
                self.enemy.hp = self.enemy.hp - hero.weapon.damage
                print(f"You dealt {hero.weapon.damage} damage to an enemy slime.{self.enemy.name} has {self.enemy.hp} HP left.")
            elif action == "s":
                if hero.ballance >= 120 and hero.hp < hero.max_hp:
                    hero.hp += 70
                    hero.ballance -= 120
                    if hero.hp > hero.max_hp:
                        hero.hp = hero.max_hp
                    print(f'Your HP is {hero.hp}, your ballance is {hero.ballance}.')
                else:
                    print('NO! You dont need it!')
            else:
                print('Sorry, you are input incorrect action. Try again!')
            hero.hp = hero.hp - self.enemy.weapon.damage
            print(f"{self.enemy.name} dealt {self.enemy.weapon.damage} damage to you. You have {hero.hp} HP left.")

            if not hero.is_alive():
                answer = 0
                print(f'You are dead and {self.enemy.name} has {self.enemy.hp} hp left.')
                while not answer == 'x' or not answer == 'z':
                    answer = input("Continue for 100 HP? (cost 750 coins) z -yes, x - no: ")
                    if answer == 'z':
                        if hero.ballance >= 750:
                            hero.hp = 100
                            print('Your HP: 100')

                        else:
                            print('You are dead!')
                            break
                            
                    if answer == "x":
                        print("You are dead!")
                        break
                    else:
                        print('Sorry, you are input incorrect action. Try again!')
                
                if not hero.is_alive():
                    break

        if self.enemy.hp < 1:
            print(f"You are won and you have {hero.hp} hp left.")

    def get_loot(self, hero):
        loot_procent = randint(1, 100)
        if loot_procent >= 1 and  loot_procent <= 33:
            hero.inventory.extend([self.enemy.armour, self.enemy.weapon])
            hero.show_hero_inventory()

        elif loot_procent >= 34 and loot_procent <= 66:
            money = randint(round(self.enemy.money / 2), self.enemy.money * 2)
            hero.ballance += money
            hero.show_hero_inventory()
            print(f"You are get money({money}).")
        
        elif loot_procent >= 67 and loot_procent <= 99:
            hero.hp += 15
            print(f"You're HP: {hero.hp}.")

        elif loot_procent == 100:
            money = randint(round(self.enemy.money / 2), self.enemy.money * 2)
            money *= 10
            hero.ballance += money
            print('You are get lucky blok!')
            print('Loading...')
            time.sleep(randint(1, 4))
            hero.show_hero_inventory()
            print(f"You're get money({money}).")


class Dungeon:
    def __init__(self, rooms, name):
        self.rooms = rooms
        self.counter = 0
        self.name = name

    def dungeon_manager(self, hero, trader):
        print(f'You have entered the {self.name}.')
        while True:
            choose = input('Choose your action: m - shop, n - inventory, b - next room: ')
            if choose == 'm':
                print('Loading...')
                time.sleep(randint(1, 4))
                trader.trader_manager(hero)
            elif choose == 'n':
                print('Loading...')
                time.sleep(randint(1, 4))
                hero.inventory_manager()
            elif choose == 'b':
                print('Loading...')
                time.sleep(randint(1, 4))
                self.next_room(hero)
                if not hero.is_alive():
                    break
                self.rooms[self.counter - 1].get_loot(hero)    
                if self.counter == len(self.rooms):
                    print(f'You competed {self.name}.')
                    time.sleep(randint(1, 4))
                    break
            else:
                print('Sorry, you are input incorrect action. Try again!')

    def next_room(self, hero):
        self.rooms[self.counter].enter_room(hero)
        self.counter += 1



class Shop:
    def __init__(self, name, inventory, money, allar, allwep):
        self.name = name
        self.trader_inventory = inventory
        self.money = money
        self.allar = allar
        self.allwep = allwep
        self.discount = 1
        self.df17 = 0
        self.ga = 0
        self.n = 0

    def trader_manager(self, hero):
        print(f"You have entered the {self.name}'s shop. Your ballance is {hero.ballance}.")
        while True:
            choose = input('Choose your action: o - buy, p - sell, l - exit, k - buy discount (cost 450, discount; -10%): ')
            if choose == 'o':
                self.buy_item(hero)
            elif choose == 'p':
                self.sell_item(hero)
            elif choose == 'l':
                print('Loading...')
                time.sleep(randint(1, 4))
                break
            elif choose == 'f':
                self.show_trader_inventory()
            elif choose == 'k':
                self.get_discount()

            if choose =='w':
                print('Loading...')
                time.sleep(randint(1, 4))
                self.codes(hero)
                
            else:
                print('Sorry, you are input incorrect action. Try again!')
    
    def buy_item(self, hero: Hero):
        self.show_trader_inventory()
        print("...And you may buy potion (cost: 100, hill: 80 HP) (a) and chest (cost: 450 and random thing (money, HP, weapon, armour)) (s).")
        print('(l - exit).')
        choose = int(input(f'Print your choose: number from 1 to {len(self.trader_inventory)}: '))
        if choose < len(self.trader_inventory) + 1 and choose > 0:
            if hero.ballance >= self.trader_inventory[choose - 1].cost:
                item = self.trader_inventory.pop(choose - 1)
                hero.ballance = hero.ballance - item.cost*self.discount
                self.money = self.money + item.cost
                hero.inventory.append(item)
                hero.show_hero_inventory()

            else:
                print("Sorry, you don't have enough money.")
        elif choose == 'a':
            if hero.ballance >= self.trader_inventory[choose - 1].cost:
                hero.ballance = hero.ballance - 100
                hero.hp = hero.hp + 80

            else:
                print("Sorry, you don't have enough money.")
        
        elif choose == 's':
            self.chest_manager()
        elif choose =='l':
            return
        else:
            print('No! Try again')

    def sell_item(self, hero): 
        hero.show_hero_inventory()
        choose = int(input(f'Print your choose: number from 1 to {len(hero.inventory)}: '))
        if choose < len(hero.inventory) + 1 and choose > 0:
            if self.money >= hero.inventory[choose - 1].cost:
                item = hero.inventory.pop(choose - 1)
                hero.ballance += item.cost
                self.money -= item.cost
                self.trader_inventory.append(item)

            else:
                print('TRADER: Sorry, I dont have money for this purchase.')
            
        else:
            print('No! True again')

    def show_trader_inventory(self):
        for i in range(len(self.trader_inventory)):
            print(f'{i + 1}. {self.trader_inventory[i]}')

    def chest_manager(self, hero):
        proc = randint(1, 4)
        if proc == 1:
            gC = randint(500, 990)
            hero.ballance += gC
            print(f'Congratulations! You get {gC} money!')
        elif proc == 2:
            gC = randint(40, 99)
            hero.hp += gC
            print(f'Congratulations! You get {gC} hp!')
            if hero.hp > hero.max_hp:
                hero.hp = hero.max_hp
        elif proc == 3:
            gC = choice(self.allar)
            hero.inventory.append(gC)
            print(f'Congratulations! You get {gC}!')
        elif proc == 4:
            gC = choice(self.allwep)
            hero.inventory.append(gC)
            print(f'Congratulations! You get {gC}!')

    def codes(self, hero):
        choose = input('You are entered to secret room. Print codes: ')
        if choose == 'Dark wolf 17':
            if self.df17 == 0:
                hero.ballance += 170
                print('YOU GET 170 MONEY!')
                self.df17 = 1
            else:
                print('NO!')
                time.sleep(0.5)
                print('NO!')
                time.sleep(0.2)
                print('NO!')
                time.sleep(0.2)
                print('NO!')
                time.sleep(0.1)
                print('NO!')
                time.sleep(0.1)
                print('NO!')
                print('NO!')
                print('NO! I WONT GIVE YOU 170$ AGAIN!')
        elif choose == 'Gold armour':
            goldArmour = Armour("goldArmour", 250, 80)
            if self.ga == 0:
                hero.inventory.append(goldArmour)
                print('YOU GET GOLD ARMOUR!')
                self.ga = 1
            else:
                print('NO!')
                time.sleep(0.5)
                print('NO!')
                time.sleep(0.2)
                print('NO!')
                time.sleep(0.2)
                print('NO!')
                time.sleep(0.1)
                print('NO!')
                time.sleep(0.1)
                print('NO!')
                print('NO!')
                print('NO! I WONT GIVE YOU GOLD ARMOUR AGAIN!')
        elif choose == 'NFC':
            if choose == 'Dark wolf 17':
                if self.df17 == 0:
                    self.discount = round((self.discount - 0.1), 1)
                    ds = round((1 - self.discount) * 100)
                    print(f'YOU GET DISCOUNT... NOW YOUR DISCOUNT IS {ds}%!')
                    self.df17 = 1
                else:
                    print('NO!')
                    time.sleep(0.5)
                    print('NO!')
                    time.sleep(0.2)
                    print('NO!')
                    time.sleep(0.2)
                    print('NO!')
                    time.sleep(0.1)
                    print('NO!')
                    time.sleep(0.1)
                    print('NO!')
                    print('NO!')
                    print('NO! I WONT GIVE YOU DISCOUNT AGAIN!')
        else:
            print('INCORRECT! GO OUT!')
            return


    def get_discount(self, hero):
        if not self.discount == 0.1:
            if hero.ballance >= 450:
                self.discount = round((self.discount - 0.1), 1)
                ds = round((1 - self.discount) * 100)
                print(f'You get discount! Now your discount is {ds}%.')
                hero.ballance -= 450
            else:
                print("Sorry, you don't have enough money.")
        else:
            print('You have max discount.')