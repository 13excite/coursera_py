import os
import csv
import functools


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        if self.photo_file_name:
            return os.path.splitext(self.photo_file_name)[1]



class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

    def get_body_volume(self):
        if self.body_whl:
            return functools.reduce(lambda x, y: float(x)*float(y), self.body_whl.split('x'))
         return 0


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    reader = csv.reader(csv_filename)
    for row in reader:
        if row and row[0].replace(";",""):
            car_list.append(row[0].strip().split(';'))
    return car_list[1:]

with open('_af3947bf3a1ba3333b0c891e7a8536fc_coursera_week3_cars.csv', 'r') as f:
    data = get_car_list(f)
    print(data)
    print(len(data[0]))