##함수
class Node(): #노드 만들기
    def __init__(self):
        self.data=None
        self.link=None

def printNodes(start):
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData,insertData):
    global memory,head,current,pre

    #첫 노드 앞에 삽입(다현,화사)
    if findData==head.data:
        node=Node()
        node.data=insertData
        node.link=head
        head=node
        return
    #두번째 노트 이후 앞에 삽입 (사나,솔라)
    current=head
    while current.link !=None:
        pre=current
        current=current.link
        if current.data == findData :
            node=Node() #삽입 처리
            node.data=insertData
            node.link=current
            pre.link=node
            return
    #마지막에 추가할 때
    node=Node()
    node.data=insertData
    current.link=node
    return

def deleteNode(deletData):
    global memory, head, current, pre

    #첫 노드를 삭제할 때
    if deletData==head.data:
        current=head
        head=head.link
        del (current)
        return
    #두번째 이후를 삭제
    current=head
    while current.link !=None:
        pre=current # 프리 나 잡고 있어
        current=current.link #커렌트 다음으로 가
        if current.data == deletData :
            pre.link=current.link
            del(current)
            return

def findNode(findData):
    global memory, head, current, pre
    current=head
    if current.data == findData:
        return current
    while current.link !=None:
        current=current.link #다음으로 이동하자
        if current.data == findData:
            return current
    return Node() #못 찾았으면 빈 노드 돌려줌

##전역
memory=[]
head,pre,current=None,None,None
dataArray=['다현','정연','쯔위','사나','지효']

##메인
node=Node()
node.data=dataArray[0]
head=node #가장 첫번째 노드를 가리키는 head
memory.append(node) #파이썬에서는 메모리 안 해도 됨

for data in dataArray[1:] : #['정연','쯔위','사나','지효']
    pre=node #다현 노드를 잡고 있어라
    node=Node()
    node.data=data
    pre.link=node
    memory.append(node)

printNodes(head)

insertNode('사나','솔라')
printNodes(head)

insertNode('재남 ','문별')
printNodes(head)

deleteNode('쯔위')
printNodes(head)

fNode=findNode('다현')
print(fNode.data)

fNode=findNode('솔라')
print(fNode.data)

fNode=findNode('재남')
print(fNode.data)