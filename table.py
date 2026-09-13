class FunctionError(Exception):
    pass

class CreateListError(Exception):
    pass

class table():
    def __new__(cls,*args):
        if isinstance(args[1],table) or args[1] is None: # args[1] is ".next" field. args[0] is .data field.
            return super().__new__(cls)
        else:
            raise CreateListError(".next must be an instance of table or None")
        
    
    def __init__(self,data,next) -> None:
        self.data = data
        self.next = next

    def __clear__(self) -> None:
        """
        Service function.
        """
        curr = self
        temp = table(None,None)
        while curr:
            if curr.data is not None:
                temp.append(curr.data)
            curr = curr.next
        self.data = temp.data
        self.next = temp.next

    def length(self) -> int:
        """
        Returns length of your table.
        """
        self.__clear__()
        curr,count = self,0
        while curr:
            count += 1
            curr = curr.next
        return count

    def change(self,index:int,element) -> None:
        """
        Changes .data on {index} to {element}.
        """
        if index >= self.length() or index < 0:
            raise IndexError
        count = 0
        curr = self
        while curr:
            if count == index:
                curr.data = element
                break
            curr = curr.next
            count += 1

    def append(self,element) -> None:
        """
        Adds {element} at the end of the table.
        """
        curr = self
        if self.data:
            while curr.next:
                curr = curr.next
            curr.next = table(element,None)
        else: # если длина - 0(нет вообще ничего, список буквально table(None,None)), то заменяет data
            self.data = element

    def ind(self,index:int) -> int:
        """
        Returns an element from {index}.
        """
        if index >= self.length():
            raise IndexError
        self.__clear__()
        curr,count = self,0
        while curr:
            if index == count:
                return curr.data
            curr = curr.next
            count += 1

    def index(self,element):
        """
        Returns index of {element}.
        """
        self.__clear__()
        curr,count = self,0
        while curr:
            if curr.data == element:
                return count
            count += 1
            curr = curr.next
        raise FunctionError("There is no element here")

    def pop(self,index:int = None) -> None:
        """
        Returns element that will be removed.

        If {index} == None or you have left blank call of a method removes last element of the table.
        Elif {index} is an instance of non-negative integer removes element on {index}.
        """
        if not isinstance(index,int) and index != None:
            raise IndexError
        if self.data == None:
            raise FunctionError("Empty table")
        if index == None:
            if self.next != None:
                curr = self
                while curr.next.next:
                    curr = curr.next
                olddata = curr.next.data
                curr.next = None
                return olddata
            else:
                olddata = self.data
                self.data = None
                return olddata
        else:
            if index >= self.length() or index < 0:
                raise IndexError
            if not self.data:
                raise FunctionError("Empty table")
            if index > 0:
                curr = self
                count = 0
                while count != index:
                    curr = curr.next
                    count += 1
                olddata = curr.data
                curr.data = None
                return olddata
            else:
                olddata = self.data
                self.data = None
                return olddata

    def copy(self):
        """
        Returns an independent copy of table.
        """
        self.__clear__()
        a = table(None,None)
        b = a
        curr = self
        while curr:
            b.next = table(curr.data,None)
            b = b.next
            curr = curr.next
        return a
    
    def clear(self) -> None:
        """
        Clears table
        """
        self.data = self.next = None

    def extend(self,massive:list) -> None:
        """
        Add items from iterable {massive}
        """
        if not any((isinstance(massive, tuple),isinstance(massive, dict),isinstance(massive, list),isinstance(massive, set),isinstance(massive, frozenset))):
            raise ValueError("Argument must be a massive")

        for i in massive:
            self.append(i)

    def println(self) -> None:
        """
        Prints table
        """
        self.__clear__()
        curr = self
        while curr:
            if curr.next != None:
                print(curr.data, end=" | ")
            else:
                print(curr.data)
            curr = curr.next

    def remove(self,element) -> None:
        """
        Removes {element} from table
        """
        if element == None:
            raise ValueError("Argument can't be None")
        curr = self
        while curr:
            if curr.data == element:
                curr.data = None
        raise FunctionError("There is no element here")

    def count(self,element) -> int:
        """
        Counts {element} in table and returns its quantity
        """
        self.__clear__()
        curr = self
        score = 0
        while curr:
            if curr.data == element:
                score += 1
            curr = curr.next
        return score

    def reverse(self) -> None:
        """
        Reversing table's elements
        """
        prev = None
        curr = self
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp
        self.data = prev.data
        self.next = prev.next

    def centre(self):
        """
        Returns centre of table
        """
        slow = fast = self
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def insert(self,index:int,element) -> None:
        """
        Inserts {element} on {index}
        """
        if index < 0:
            raise FunctionError("Index can't be negative")
        curr = self
        count = 0
        while count != index and curr.next:
            count += 1
            curr = curr.next
        if not curr.next:
            curr.next = table(element,None)
            return
        olddata,oldnext = curr.data,curr.next
        curr.data = element
        curr.next = table(olddata,oldnext) 

    # def sort(self):

if __name__ == "__main__":
    exit("bro it's a library btw(arch)☠️")
