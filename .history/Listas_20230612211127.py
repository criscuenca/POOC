class Metodos():
    


    def ingreso(self,lis,tam):
        i=0
        while(i<tam):
            print("Ingrese el [",i,"] valor de la lista")
            num=int(input("numero "))
            lis.append(num)
            i=i+1
    def impresion(self,lis,tam):
        for i in range(tam):
            print(lis[i])

#metodo apppend
    list = []
    list
    list.append(5)
    list
    list.append(27)
    list
    list.append(3)
    list
    list.append(15)
    list
    list.append(12)
    list
    list.append(18)
    list.append(6)
    print(list)
    
    #metodo clear
    list = [5,27,3,15,12,18,6]
    list.clear()
    print(list)
    
#metodo extend

list = [5,27,3,15,12,18,6]
list.extend([50,55,60,65])
print(list)

#metodo count

list = [5,27,3,15,12,18,6,1,2,3,4,5,7,10,4,11,5,19,4,5]
print(list.count(5))
print(list.count(4))

#metodo index

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list.index(5))
print(list.index(10))
print(list.index(17))
print(list.index(20))


#metodo insert

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list.insert(21,22)
list.insert(21,23)
list.insert(21,24)
list.insert(21,25)
list.insert(21,30)
print(list)

#metodo pop

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop())
print(list)

#metodo remove

list = ["perro","gato","Vaca","Loro","lobo","Vaca","perro"]
list.remove("perro") 
print(1)
print(list)
list.remove("Vaca") 
print(1)
print(list)

#metodo reverse
list = ["perro","gato","Vaca","Loro","lobo","Vaca","perro"]
list.reverse()
print(list)
list.reverse()
print(list)
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list.reverse()
print(list)


#metodo sort
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,-5,-1,-8,-9,-6,80,-30,-50,50]
list2 = ["perro","gato","Vaca","Loro","lobo","Vaca","perro"]
list.sort()
print(list)
list2.sort()
print(list2) 
list.sort(reverse=True)
print(list)


list2.sort(reverse=True)
print(list)