class FunctionError(Exception): # класс ошибки для неправильного выполнения функций списка
    pass

class CreateListError(Exception): # класс ошибки для неверного создания списка
    pass

class pivo():
    def __new__(cls,*args):
        # print(args)
        if isinstance(args[1],pivo) or args[1] is None:
            return super().__new__(cls)
        else:
            raise CreateListError("спрашивай у вери ти все что пожелаешь...") # знает где ты жиь
        
    
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
        del temp

    def length(self) -> int:
        self.__clear__()
        curr,count = self,0
        while curr:
            count += 1
            curr = curr.next
        return count

    def change(self,index,element):
        if index >= self.length() or index < 0:
            raise FunctionError("somethi ging is cuming in thre(twpo) days/.")
        count = 0
        curr = self
        while curr:
            if count == index:
                curr.data = element
                break
            curr = curr.next
            count += 1

    def append(self,element):
        curr = self
        if self.data:
            while curr.next:
                curr = curr.next
            curr.next = pivo(element,None)
        else: # если длина - 0(нет вообще ничего, список буквально pivo(None,None)), то заменяет data
            self.data = element

    def ind(self,num:int) -> int:
        if num >= self.length():
            raise IndexError
        self.__clear__()
        curr,count = self,0
        while curr:
            if num == count:
                return curr.data
            curr = curr.next
            count += 1
        raise FunctionError("ьы тупой такогьо нет") # знает где ты живёшь

    def index(self,element):
        self.__clear__()
        curr,count = self,0
        while curr:
            if curr.data == element:
                return count
            count += 1
            curr = curr.next


    def pop(self,index = None) -> None:
        if not isinstance(index,int) and index != None or self.data == None:
            raise FunctionError("за тобой идут.") # нашли у подмостка веритев.
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
            if index >= self.length() or index < 0 or not self.data:
                raise FunctionError("somethi ging is cuming in thre days/.") # somet hing cruel
            if index > 0: #TODO НЕРАБОЧЕЕ ГОВНО ПОТОМУ ЧТО ДОПУСТИМ ЕСТЬ "1,2,3" УДАЛЯЮ ИНДЕКС ПЕРВЫЙ ПОЛУЧАЕТСЯ СПИСОК "1" НУ КОРОЧЕ ОТВЯЗЫВАЕТ И СДЕЛАЙ ТАК ЧТОБЫ ОН ПРОСТО NONE СТАНОВИЛСЯ И ВСЁ В ПРИЦНИПЕ НУ SELF.DATA
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
        self.__clear__()
        a = pivo(None,None)
        b = a
        curr = self
        while curr:
            b.next = pivo(curr.data,None)
            b = b.next
            curr = curr.next
        return a
    
    def clear(self):
        self.data = self.next = None

    def extend(self,massive:list):
        if not any((isinstance(massive, tuple),isinstance(massive, dict),isinstance(massive, list),isinstance(massive, set),isinstance(massive, frozenset))):
            raise FunctionError("я знаю где ты живешь.") # (вери ти.)

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
        prev = None
        curr = self
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp
        return prev

    def centre(self):
        slow = fast = self
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def insert(self,index,element):
        if index < 0:
            raise FunctionError("здесь кто то здесь?")
        # if index >= self.length():
        #     self.append(element)
        #     return
        curr = self
        count = 0
        while count != index:
            count += 1
            curr = curr.next
        olddata,oldnext = curr.data,curr.next
        curr.data = element
        curr.next = pivo(olddata,oldnext)

    # def sort(self):
import time
if __name__ == "__main__":
    # exit("бро если что это библиотека☠️")