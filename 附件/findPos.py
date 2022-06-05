
class Garage:
    def __init__(self,num,x,properties,isOccupy,position):
        self.num = num #车位号
        self.x = x #距入口位置
        self.properties = properties #车库类型（0表示平行，1表示垂直，2表示倾斜）
        self.isOccupy = isOccupy #是否被占用（0表示未被占用，1表示已被占用）
        self.position = position #车库所在区域（0表示第一段区域，1表示第二段区域，2表示第三段区域）

    def straight(self,dx):
        count = self.position
        return  (dx-8.3*count-5.14-3.85)/5.56+0.926+0.463

    def turn(self):
        count = self.position

        return  2.99*count

    def decelerate(self):
        count = self.position

        return  0.432*count

    def reverse(self):
        kind = self.properties
        if kind == 0:
            time = 2.129
        elif kind == 1:
            time = 3.17
        elif kind == 2:
            time = 3.5
        return 1

    def cost_time(self,dx):
        return self.straight(dx)+self.turn()+self.decelerate()+self.reverse()



class Car:
    def __init__(self,x):
        self.x = x



Garages = [Garage(i,0,0,1,0) for i in range(0, 86)]
for i in range(1,86):
    # random.seed(time.time())

    name = 'garage'+str(i)
    # print(name)
    #确定车位位置
    if i<28:
        Garages[i].x = 2.4*i
        Garages[i].position = 0
        Garages[i].properties = 1
    elif i>=28 and i<30:
        Garages[i].x = 2.4*i
        print(Garages[i].x)
        Garages[i].position = 1
        Garages[i].properties = 1
    elif i >= 30 and i < 32:
        Garages[i].x = 2.4*28 + 8.3 + 2.4*(i-29)
        Garages[i].position = 2
        Garages[i].properties = 3
    elif i >=33 and i < 35:
        Garages[i].x = 2.4*31 + 8.3*2 + 2.4*(i-33)
        Garages[i].position = 2
        Garages[i].properties = 1
    elif i >=35 and i <62:
        Garages[i].x = 2.4*31 + 8.3*2 + 2.4*(i-34)
        Garages[i].position = 3
        Garages[i].properties = 1
    elif i >=62 and i <74:
        Garages[i].x = 5.3*(i-61)
        Garages[i].position = 0
        Garages[i].properties = 0
    elif i >=74 and i<86:
        Garages[i].x = 2.4*31 + 8.2*2 + 5.3*(i-73)
        Garages[i].position = 0
        Garages[i].properties = 0
Garages[2].isOccupy = 0
Garages[5].isOccupy = 0
Garages[9].isOccupy = 0
Garages[13].isOccupy = 0
Garages[45].isOccupy = 0
Garages[52].isOccupy = 0
Garages[53].isOccupy = 0
Garages[54].isOccupy = 0
Garages[64].isOccupy = 0
Garages[67].isOccupy = 0
Garages[78].isOccupy = 0
Garages[81].isOccupy = 0
Garages[82].isOccupy = 0

record={'properties0':0,'properties1':0,'properties2':0}
car = Car(60)

minTime = 9999
for i in range(1,86):
    dis = Garages[i].x - car.x
    if Garages[i].isOccupy==0:
        print(i)
        print(Garages[i].cost_time(dis))
        # dis = Garages[i].x-car.x
        if Garages[i].cost_time(dis)>0 and Garages[i].cost_time(dis)<=minTime:
            key = 'properties' + str(Garages[i].properties)
            record[key]=Garages[i].num
            minTime = Garages[i].cost_time(dis)

print(record)
print(Garages[record['properties0']].cost_time(Garages[record['properties0']].x - car.x))
print(Garages[record['properties1']].cost_time(Garages[record['properties1']].x - car.x))
print(Garages[record['properties2']].cost_time(Garages[record['properties2']].x - car.x))