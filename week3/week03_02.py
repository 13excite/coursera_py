import os
import csv
import functools


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        if self.photo_file_name:
            return os.path.splitext(self.photo_file_name)[1]



class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_whl = body_whl

    def get_body_volume(self):
        if self.body_whl:
            return functools.reduce(lambda x, y: float(x)*float(y), self.body_whl.split('x'))
        return 0


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename,'r') as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
               # print(row)
                if row and row[0].replace(";",""):
                    car_list.append(row)
    except IOError:
        return "Error opening file"
    return car_list[1:]

if __name__ == '__main__':

    cars = []
    trucks = []
    spec_macs = []

    data = get_car_list('_af3947bf3a1ba3333b0c891e7a8536fc_coursera_week3_cars.csv')
   # print(car_data)
    for i in range(len(data) - 1):
        if data[i][0] == "car":
            car = Car(data[i][0], data[i][1], data[i][3], data[i][5], data[i][2])
            cars.append(car)
        elif data[i][0] == "truck":
            truck = Truck(data[i][0], data[i][1], data[i][3], data[i][5], data[i][4])
            trucks.append(truck)
        elif data[i][0] == "spec_machine":
            spec_mac = SpecMachine(data[i][0], data[i][1], data[i][3], data[i][5], data[i][6])
            spec_macs.append(spec_mac)
        else:
            print("No such type:", data[i][0])

        print("Cars:", cars)
        print("Trucks:", trucks)
        print("Spec_macs:", spec_macs)

###   neeed debug, why not attribute car_type
        print(car.car_type)
        for car in range(len(cars)):
            print("photo_car:", cars[car].get_photo_file_ext())

            print("photo_car:", cars[car].get_photo_file_ext())

        for truck in range(len(trucks)):
            print('body_size_track:', trucks[truck].body_whl)
            print("photo_truck:", trucks[truck].get_photo_file_ext())