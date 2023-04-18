def situation_now(day, month, temperature):
    print(f'Сегодня {day} {month}. На улице {temperature} градусов.')
    if temperature < 0:
        print('Холодно, лучше остаться дома')


if __name__ == '__main__':
    day = 21
    month = 10
    temperature = -5
    situation_now(day, month, temperature)
