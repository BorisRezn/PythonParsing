from random import random

pack = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

a = len(pack)

dealer = []
gamer = []

def deal_card(cards):
    for n in range(cards):
        d = int(random()*a)
        new = pack[d]
        dealer.append(new)
        
    return(dealer)

def gam_card(cards2):
    for m in range(cards2):
        p = int(random()*a)
        newp = pack[p]
        gamer.append(newp)
    return(gamer)

print('Карты дилера ', deal_card(2))
print('Карты игрока ', gam_card(2))

def calc_sum(string):
    sm=0
    tuz=0
    for i in string:
        if i == 'A':
            tuz = tuz+1
        elif i == 'J' or i == 'Q' or i == 'K':
            sm = sm + 10
        else:
            sm = sm + int(i)

    if tuz > 0:
        if sm < 11:
            sm = sm + 11 + tuz - 1
        else:
            sm = sm + tuz
                                       
    return(sm)

print('Сумма дилера  ', calc_sum(dealer))
print('Сумма игрока  ', calc_sum(gamer))

ask=int(input('Еще карту? 1 - да, 2 - нет ', ))

while ask == 1:
    print(gam_card(1))
    print('Сумма игрока  ', calc_sum(gamer))
    if calc_sum(gamer) > 21:
        print('Перебор, вы проиграли')
        break
    elif calc_sum(gamer) == 21:
        print('Набрано 21, играет банк')
        break
    else:
        print('продолжаем игру')
        ask=int(input('Еще карту? 1 - да, 2 - нет ', ))
else:
    print('Ваша сумма %.f Играет банк ' %calc_sum(gamer))

if calc_sum(gamer) > 21:
    print("ИГРА ОКОНЧЕНА")
else:
    while calc_sum(dealer) < 17:
        print('Карты дилера ', deal_card(1))
        print('Сумма дилера  ', calc_sum(dealer))
        
    if calc_sum(dealer)> 21:
        print("У банка перебор! Вы выиграли!")
    elif calc_sum(dealer) == calc_sum(gamer):
        print('Ничья! Равное количество очков!')
    elif calc_sum(dealer) > calc_sum(gamer):
        print('Дилер выиграл')
    elif calc_sum(dealer) < calc_sum(gamer):
        print('Вы выиграли!!! Заберите деньги!')

  


