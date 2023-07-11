




bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

import random
#Создаём колоду карт
suits = ['Черви', 'Бубны','Черви', 'Бубны']
ranks = ['2','3','4' ,'5', '6',  '7', '8', '9', '10','Валет', 'Дама', 'Король', 'Туз']
values = {'2': 2,'3': 3,'4': 4 ,'5': 5, '6':6,  '7':7, '8':8, '9': 9, '10': 10,'Валет': 10, 'Дама': 10, 'Король': 10, 'Туз': 11}

#Класс карты для показа
class Card:
    def __init__(self, suit, rank, values):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} {self.suit}"

#Класс колоды карт для показа
class Deck():
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

#Перетасовка
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()

#Представления руки игрока или дилера
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Туз':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces - = 1

#Отображения карт на руке дилера или игрока (функция)
def show_hand(hand):
    for card in hand.cards:
        print(card)

def show_partial_hand(hand):
    print("Скрытая карта")
    for card in hand.cards[1:]:
        print(card)

#Функция для игры
def play_blackjack():
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()

    #Раздача карт
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    #Покзывает карты на руках игроках и дилера
    show_partial_hand(dealer_hand)
    print("Ваши карты:")
    show_hand(player_hand)


    #Ход игрока
    while True:
        choice = input("Желаете взять ещё карту?(да/нет):")
        if choice.lower() == 'да':

            player_hand.add_card(deck.deal_card())
            player_hand.adjust_for_ace()
            show_hand(player_hand)
            if player_hand.value > 21:
                print("Перебор! К сожалению вы проиграли. Ничего, в следующий раз вы обязтельно одержите победу.")
                return
        else:
            break
    
    #Ход дилер 
    show_hand(dealer_hand)
    while dealer_hand.value < 17:
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.adjust_for_ace()
        show_hand(dealer_hand)
    
    #Определение победителя
    if dealer_hand.value > 21:
        print("Дилер перебрал! Вы победили.")
    elif dealer_hand.value > player_hand.value:
        print("Дилер выиграл.")
    elif dealer_hand.value < player_hand.value:
        print("Вы победили. Поздравляем!")
    else:
        print("Ничья.")

#Запуск игры
play_blackjack()


