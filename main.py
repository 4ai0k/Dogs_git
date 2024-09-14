from dogs import Thoroughbred

if __name__ == '__main__':
    dog_1 = Thoroughbred('Шарик', '10 лет', 'коричневый', 'дворовая')
    dog_2 = Thoroughbred('Арчи', '5 лет', 'черный', 'немецкая овчарка')

    print(dog_1.dark())
    print(dog_1.go_to_dog_show(), '\n')
    print(dog_2.dark())
    print(dog_2.go_to_dog_show())
