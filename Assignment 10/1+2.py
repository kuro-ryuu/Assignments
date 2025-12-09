import time
class Elevator:
    def __init__(self, b_floor, t_floor):
        self.b_floor = b_floor
        self.t_floor = t_floor
        self.position = b_floor
    def go_to_floor(self, selected_floor):
        if selected_floor < self.b_floor or selected_floor > self.t_floor:
            print("No valid floor selected")
            return
        print(f"Currently moving from F{self.position} to F{selected_floor}")
        while self.position < selected_floor:
            self.floor_up()
        while self.position > selected_floor:
            self.floor_down()
    def floor_up(self):
        if self.position < self.t_floor:
            self.position += 1
            time.sleep(0.892)
            print(f"Floor: {self.position}")
            
        else:
            print("!!At top floor!!")
    def floor_down(self):
        if self.position > self.b_floor:
            self.position -= 1
            time.sleep(0.892)
            print(f"Floor: {self.position}")
            
        else:
            print("!!At bottom floor!!")

# e = Elevator(-2, 40)
# e.go_to_floor(40)

class Building:
    def __init__(self, b_floor, t_floor, elevator_amount):
        self.b_floor = b_floor
        self.t_floor = t_floor
        self.elevator_amount = elevator_amount
        self.elevator_list = []
        for _ in range(elevator_amount):
            self.elevator_list.append(Elevator(b_floor, t_floor))

    def run_elevator(self, elevator_no, selected_floor):
        if elevator_no < 1 or elevator_no > self.elevator_amount:
            print("Invalid elevator amount selected")
            return
        self.elevator_list[elevator_no-1].go_to_floor(selected_floor)
    
    def fire_alarm(self):
        for _ in range(4):
            time.sleep(1)
            print("weeooo weeeeooo weeeooo weeeooo SECOND WARNING INCOMING WEEEOEEEOEOEE")
        print("the fire nation attacked or sum so run for your life maybe idk")
        for i in range(self.elevator_amount):
            self.run_elevator(i, self.b_floor)

b = Building(-2, 40, 4)
b.run_elevator(1, 3)
b.run_elevator(2, 4)
b.run_elevator(3, 5)
b.fire_alarm()