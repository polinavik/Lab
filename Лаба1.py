class Auto:
    count=0
    def __init__(self, color, brand, power, drive_unit):
        self.color = color
        self.brand = brand
        self.power = power
        self.drive_unit = drive_unit
        Auto.count += 1
    def __str__(self):
        return f"color: {self.color}, brand: {self.brand},power: {self.power},drive_unit: {self.drive_unit}"
class CarManager:
    def read_data(self, file_name):
        autos = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                color, brand, power, drive_unit = line.strip().split(',')
                auto = Auto(color,brand,power,drive_unit)
                autos.append(auto)
        return autos

    def write_data(self, file_name, autos):
        with open(file_name, 'w') as file:
            for auto in autos:
                file.write(f"{auto.color},{auto.brand},{auto.power},{auto.drive_unit}\n")
        print("Данные были записаны в файл.")

    def choose_file(self):
        file_name = input("Введите имя файла 'Data1' или 'Data2': ")
        return file_name


car_manager = CarManager()
autos = []
def main():
    while True:
        print("\n1. Добавить автомобиль")
        print("2. Удалить автомобиль")
        print("3. Редактировать автомобиль")
        print("4. Поиск автомобиля")
        print("5. Отобразить параметр автомобиля")
        print("6. Отобразить все автомобили")
        print("7. Показать количество автомобилей")
        print("8. Перемещение")
        print("9. Выбор файла для записи в этот файл")
        print("10. Выбор файла для чтения")
        print("11. Выбор файла для записи данных из файла в список авто")
        print("0.Выйти")
        
        variant = input("Введите выбор: ")

        try:
            variant = int(variant)

        except ValueError:
            print("Неверный выбор")
            continue
        if variant == 1:
            count1=int(input("Количество экзмепляром,которые вы хотите добавить: "))
            for i in range(1,count1+1):
                color = str(input("Введите цвет автомобиля: "))
                brand = str(input("Введите марку автомобиля: "))
                power = int(input("Введите мощность автомобиля: "))
                drive_unit = str(input("Введите привод автомобиля: "))
                auto = Auto(color, brand, power, drive_unit)
                autos.append(auto)
                print("Автомобиль добавлен в список")
        elif variant == 2:
            if not autos:
                print("Список автомобилей пуст")
                return
            count2=int(input("Количество экзмепляром,которые вы хотите удалить: "))
            while count2>0:
                for index, auto in enumerate(autos):
                    print(f"Индекс: {index}, Автомобиль: {auto.__dict__}")
                index = int(input("Введите индекс удаляемого автомобиля: "))
                if index < 0 or index >= len(autos):
                    print("Неверный индекс")
                else:
                    autos.pop(index)
                    print("Автомобиль удален из списка")
                count2-=1
        elif variant == 3:
            if not autos:
                print("Список автомобилей пуст")
                return
            index = int(input("Введите индекс редактируемого автомобиля: "))
            try:
                auto = autos[index]
            except IndexError:
                print("Неверный индекс")
                return
            cnt=int(input("Введите количество параметров,которые вы хотите изменить: "))
            for i in range(1,cnt+1):
                par=str(input("Введите параметр,который вы хотите изменить: "))
                if par=="цвет":
                    color = str(input("Введите новый цвет автомобиля: "))
                if par=="марка":
                    brand = str(input("Введите новую марку автомобиля: "))
                if par=="мощность":
                    power = int(input("Введите новую мощность: "))
                if par=="привод":
                    drive_unit = str(input("Введите новый привод: "))
            auto.color = color
            auto.brand = brand
            auto.power = power
            auto.drive_unit = drive_unit
            print("Автомобиль обновлен")
        elif variant == 4:
            if not autos:
                print("Список автомобилей пуст")
                return
            parametr = input("Введите поле для поиска: ")
            for index, auto in enumerate(autos):
                if parametr in str(auto.__dict__.values()):
                    print(f"Индекс: {index}, Автомобиль: {auto.__dict__}")
        elif variant == 5:
            if not autos:
                print("Список автомобилей пуст")
                return
            index = int(input("Введите индекс автомобиля для отображения: "))
            try:
                auto = autos[index]
            except IndexError:
                print("Неверный индекс")
                return
            
            cnt1=int(input("Введите количество параметров,которые вы хотите посмотреть: "))
            for i in range(1,cnt1+1):
                par1=str(input("Введите параметр,который вы хотите посмотреть: "))
                if par1=="цвет":
                    print(auto.color)
                if par1=="марка":
                    print(auto.brand)
                if par1=="мощность":
                    print(auto.power)
                if par1=="привод":
                    print(auto.drive_unit)
                
        elif variant == 6:
            if not autos:
                print("Список автомобилей пуст")
                
            for index, auto in enumerate(autos):
                print(f"Индекс: {index}, Автомобиль: {auto.__dict__}")


        elif variant == 7:
            print(f"Количество автомобилей в списке: {len(autos)}")

        elif variant == 8:
            if not autos:
                print("Список автомобилей пуст")
                return
            index = int(input("Введите индекс перемещаемого автомобиля: "))
            try:
                auto = autos[index]
            except IndexError:
                print("Неверный индекс")
                return
            shag = int(input("Введите количество позиций для перемещения: "))
            if index + shag < 0 or index + shag >= len(autos):
                print("Неверное количество позиций для перемещения")
            else:
                autos.pop(index)
                autos.insert(index + shag, auto)
                print(f"Автомобиль перемещен на {shag} позиций{' вверх' if shag > 0 else ' вниз'}")
        elif variant == 9:
            file_name = car_manager.choose_file()
            car_manager.write_data(file_name, autos)
        elif variant == 10:
            file_name = car_manager.choose_file()
            read_autos = car_manager.read_data(file_name)
            with open(file_name, 'r') as file:
                file_content = file.read()
                if file_content.strip() == "":
                    print("Файл пуст")
                else:
                    for auto in read_autos:
                        print(auto)
        elif variant == 11:
            file_name = car_manager.choose_file()
            with open(file_name, 'r') as file:
                for line in file:
                    color, brand, power, drive_unit = line.strip().split(',')
                    auto = Auto(color, brand,power,drive_unit)
                    autos.append(auto)
                    
        elif variant == 0:
            break
        

        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
