# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def len_link(list):
    temp=list.val
    nextValue= list.next
    count=0
    while(nextValue != None):
        count+=1
        nextValue = nextValue.next
    return count

def link_to_list(link):
    head = link.val
    nextVal = link.next
    tempList = []

    tempList.append(head);    

    while(nextVal != None):
        value = nextVal.val;
        tempList.append(value)
        nextVal = nextVal.next


    return tempList

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # print(l1)

        output = []
        len1 = len_link(l1)
        len2 = len_link(l2)
    
        list1 = link_to_list(l1)
        list2 = link_to_list(l2)
    
        if(len1 != len2):
            difference = len1 - len2
            if(len1>len2):
                for i in range(abs(difference)):
                    list2.append(0)
            else:
                for i in range(abs(difference)):
                    list1.append(0)
                
        count=False
        for i in range(len(list1)):
            sum = list1[i]+list2[i]
            if count:
                sum += 1
            value = sum % 10
            output.append(value)
        
            if sum>9:
                count = True
            else:
                count = False
            
        if(count):
            output.append(1)
            count = False
        
        outLinked = lst2link(output)
        return outLinked