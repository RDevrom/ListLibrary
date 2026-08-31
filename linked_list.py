class FunctionError(Exception):
    pass

class CreateListError(Exception):
    pass

class pivo():
    def __new__(cls,*args):
        if isinstance(args[1],pivo) or args[1] is None:
            return super().__new__(cls)
        else:
            raise CreateListError("спрашивай у вери ти все что пожелаешь...")
        
    
    def __init__(self,data,next):
        self.data = data
        self.next = next

    def __clear__(self):
        curr = self
        temp = pivo(None,None)
        while curr:
            if curr.data is not None:
                temp.append(curr.data)
            curr = curr.next
        self.data = temp.data
        self.next = temp.next

    def length(self) -> int:
        self.__clear__()
        curr,count = self,0
        while curr and (curr.data or curr.next):
            count += 1
            curr = curr.next
        return count

    def change(self,index,element):
        if index >= self.length() or index < 0:
            raise FunctionError("somethi ging is cuming in thre(twpo) days/.")
        nexts = ".next" * index
        if isinstance(element,str):
            exec(f"self{nexts}.data = '{element}'")
        else:
            exec(f"self{nexts}.data = {element}")
    
    def append(self,element):
        if self.length() >= 1:
            nexts = ".next" * self.length()
            if isinstance(element,str):
                exec(f"self{nexts} = pivo('{element}',None)")
            else:
                exec(f"self{nexts} = pivo({element},None)")
        else:
            if isinstance(element,str):
                exec(f"self.data = '{element}'")
            else:
                exec(f"self.data = {element}")

    def ind(self,num:int) -> int:
        if num >= self.length():
            return None
        curr,count = self,0
        while curr and (curr.data or curr.next):
            if num == count:
                return curr.data
            curr = curr.next
            count += 1
        print("hello! i am verity. your personal helper friend.")
        return None

    def index(self,element):
        self.__clear__()
        curr,count = self,0
        while curr and (curr.data or curr.next):
            if curr.data == element:
                return count
            count += 1
            curr = curr.next


    def pop(self,index = None) -> None:
        if not isinstance(index,int) and index != None:
            raise FunctionError("за тобой идут.")
        if index == None:
            if self.length() > 1:
                nexts1 = ".next" * (self.length()-1)
                nexts2 = ".next" * (self.length()-2)
                olddata = eval(f"self{nexts1}.data")
                exec(f"self{nexts1}.data = None")
                exec(f"self{nexts2}.next = None")
                return olddata
            else:
                olddata = self.data
                self.data = None
                return olddata
        else:
            if index >= self.length() or index < 0 or self.length == 0:
                raise FunctionError("somethi ging is cuming in thre days/.")

            if index > 0:
                if index == self.length() - 1:
                    el = self.pop()
                    return el
                nexts = ".next" * index
                exec(f"self{nexts}.data = None")
            else:
                olddata = self.data
                self.data = None
                return olddata

    def copy(self):
        self.__clear__()
        return self
    
    def clear(self):
        self.data = self.next = None

    def extend(self,massive:list):
        if not any((isinstance(massive, tuple),isinstance(massive, dict),isinstance(massive, list),isinstance(massive, set),isinstance(massive, frozenset))):
            raise FunctionError("я знаю где ты живешь.")
        self.__clear__()
        
        for i in massive:
            self.append(i)

    def println(self):
        self.__clear__()
        curr = self
        while curr:
            if curr.next != None:
                print(curr.data, end=" | ")
            else:
                print(curr.data)
            curr = curr.next

    def remove(self,element):
        if element == None:
            raise FunctionError("ты еблан?")
        self.__clear__()
        i = self.index(element)
        self.pop(i)

    def count(self,element):
        self.__clear__()
        curr = self
        score = 0
        while curr:
            if curr.data == element:
                score += 1
            curr = curr.next
        return score

    def reverse(self):
        left = 0
        right = self.length() - 1
        while left < right:
            left_el = self.ind(left)
            right_el = self.ind(right)
            self.change(left,right_el)
            self.change(right,left_el)
            left += 1
            right -= 1

    # def insert(self,index,element):


    # def sort(self):

if __name__ == "__main__":
    exit("бро если что это библиотека☠️")