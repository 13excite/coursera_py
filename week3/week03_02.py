import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        pass

    def get_photo_file_ext(self):
        pass


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        pass


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        pass

    def get_body_volume(self):
        pass


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        pass


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