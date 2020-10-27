import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = None
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name,
                 carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        try:
            result = body_whl.split('x')
            if(len(result) != 3):
                raise AttributeError
            self.body_length = float(result[0])
            self.body_width = float(result[1])
            self.body_height = float(result[2])
        except Exception:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_good_extern(filename):
    if(len(filename) < 5):
        return False
    ext = (filename.split('.'))

    return (ext[-1] in ['jpg', 'jpeg', 'png', 'gif'] and
            len(ext) == 2 and len(ext[-2]) > 0)


def get_car_list(csv_filename):

    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            print(row)
            if(len(row) < 6 or not isinstance(row[1], str) or
               len(row[1]) == 0 or
               not isfloat(row[5]) or not is_good_extern(row[3])):
                continue
            if(row[0] == 'car'):
                if not row[2].isdigit():
                    continue
                car_list.append(Car(row[1], row[3], row[5], row[2]))

            if(row[0] == 'truck'):
                car_list.append(Truck(row[1], row[3], row[5], row[4]))

            if(row[0] == 'spec_machine'):
                if (len(row) < 7 or not isinstance(row[6], str)
                   or len(row[6]) == 0):
                    continue
                car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))

    return car_list


if __name__ == "__main__":
    cars = get_car_list("week3/coursera_week3_cars.csv")
    for car in cars:
        print(type(car))
