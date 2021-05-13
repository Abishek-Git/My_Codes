#creating a Linked List
#Adding and Removing items in LinkedList
#Insertion of items in LinkedList in Beginning and End of the LinkedList
#Deleton of item at begining and end of the Linkedlist
#Insertion and Deletion at middle of the Linkdata, nextt

class Node:
    #creating an instance of Node
    def __init__(self, data = None, next = None):
        """[Initialize new Node Each time the Function is called
        and assigning the address of the next node]

        Args:
            data ([any], optional): [data to be stored in new Node]. Defaults to None.
            next ([reference node], optional): [Reference of the next node]. Defaults to None.
        """
        self.data = data 
        self.next = next
    
class LinkedList: 
    #Initializing the LinkedList by instance
    def __init__(self):
        """[Creating a instance for the Linked List and assigning it as Head]
        """
        self.head = None

    def addBEGIN(self, data):
        """[Adding Element in the beginning of the LinkedList ]

        Args:
            data ([Any type]): [data which is added in front of the LinkedList]
        """
        if self.head is None:   
            temp = Node(data)   #If list is empty, create a node and make it Head
            self.head = temp
            return

        temp = Node(data, self.head) #creating a #Node with data
        self.head = temp
        return

    def lengthList(self):
        """[print the Lenght of the LinkedList]

        Returns:
            [type]: [None]
        """
        ittr = self.head
        if ittr is None:    #check if the List is Empty
            print("Link list is Empty")
            return
        count = 0
        while ittr:          #itterate through the last Node
            count += 1
            ittr = ittr.next
        print(count)
        return count


    def printList(self):
        """[print the data in the LinkedList]
        """          
        if self.head is None:
            print("List is Empty")
            return
        ittr = self.head
        lstittr = ""
        while ittr:
            lstittr += str(ittr.data) + '-->' if ittr.next else str(ittr.data)
            ittr = ittr.next
        print(lstittr)


    def addEND(self, data):
        """[adding data at the end of the LinkedList]

        Args:
            data ([Any]): [data to be added at the end of the List]
        """
        ittr = self.head
        if ittr is None:
            temp = self.addBEGIN(data)
            return
        
        while ittr.next:
            ittr = ittr.next
        temp = Node(data)
        ittr.next = temp
        return


    def addMID(self, data, index):
        """[Adding data in the middle of the list based on Index]

        Args:
            data ([Any]): [ ]
            index ([int]): [position of where the element need to be added]

        Raises:
            Exception: [if the index value is greater than LinkedList length
            or it is undefined]
        """
        if index <0 or index>self.lengthList():     #chech the index value is correct
            raise Exception("Index out of Range")
        ittr = self.head
        count = 0
        while count < (index - 1):
            ittr = ittr.next
            count += 1
        temp_next = ittr.next
        temp_val = Node(data, temp_next)
        ittr.next = temp_val
        return

    
    def removeAt(self, index):
        """[Removing value based on index position]
        Args:
            index ([int]): [index position of the value]

        Raises:
            Exception: [index value is not supported]
        """        
        if 0 <= index > self.lengthList():
            raise Exception("index is INVALID")
        
        ittr =  self.head
        count = 0
        while (count-1) < index -2:
            count += 1
            ittr = ittr.next

        temp = ittr.next.next
        del ittr.next.data
        ittr.next = temp
        return

    def removebyVAL(self, value):
        """[remove Linked List data by its value]

        Args:
            value ([Any]): [data which have to be removed by the list]

        Raises:
            Exception: [if the value is not in list]
        """
        ittr = self.head
        count = 0
        while ittr:
            if ittr.data is value:
                self.removeAt(count)
                return
            count += 1
            ittr = ittr.next
        if ittr is None:
            raise Exception("Value is not Found")

        
    def addMUL_value(self, *data):
        """[Adding multiple values by calling AddEnd function]
        """
        for item in data:
            self.addEND(item)
        return
        

    def add_next_by_value(self, prev_data, data):
        """[adding value next to the given value]

        Args:
            prev_data ([Any]): [value before the data]
            data ([Any]): [data to be added]
        """
        ittr = self.head
        index = 0
        while ittr:
            if ittr.data is prev_data:
                self.addMID(data, (index+1))
            ittr = ittr.next
            index += 1
        return

#examples of Adding of data in beginning and end of the List
#Length of the LinkedList
#print data of the LinkedList
if __name__ == '__main__':          #main function
    MyList = LinkedList()
    MyList.addEND(2)
    MyList.addBEGIN(1)
    MyList.addBEGIN("mint")
    MyList.addBEGIN("flavour")
    MyList.addEND("tomato")
    MyList.printList()
    MyList.addMID("potato", 3)
    MyList.addMID("berry", 3)
    MyList.lengthList()
    MyList.printList()
    MyList.removeAt(4)
    MyList.printList()
    MyList.removebyVAL("mint")
    MyList.printList()
    MyList.addMUL_value("toy", "bus")
    MyList.printList()
    MyList.add_next_by_value("berry", "blue")
    MyList.printList()



