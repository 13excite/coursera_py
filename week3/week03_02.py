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
            next(reader)
            i = 0
            for row in reader:
                if len(row) < 7:
                    continue
                if row[0] == 'car':
                    car_list.append(1)
                    car_list[i] = Car(row[0], row[1], row[3], row[5], row[2])
                    i += 1
                if row[0] == 'truck':
                    car_list.append(1)
                    car_list[i] = Truck(row[0], row[1], row[3], row[5], row[4])
                    i += 1
                if row[0] == 'spec_machine':
                    car_list.append(1)
                    car_list[i] = SpecMachine(row[0], row[1], row[3], row[5], row[6])
                    i += 1
    except IOError:
        return "Error opening file"
    return car_list

#if __name__ == '__main__':

   # data = get_car_list('_af3947bf3a1ba3333b0c891e7a8536fc_coursera_week3_cars.csv')
    #test = data[1]
    #print(test.brand)


