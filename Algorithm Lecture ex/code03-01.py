##함수 선언부
def add_data(friend):
    katok.append(None)  # 빈칸 추가
    kLen=len(katok)
    katok[kLen-1] = friend

def insert_data(position,friend): #3,'미나'
    katok.append(None)
    kLend=len(katok)
    for i in range(kLend-1,position,-1):
        katok[i]=katok[i-1]
        katok[i-1]=None
    katok[position]=friend

def delete_data(position):
    katok[position]=None
    kLen=len(katok)
    for i in range(position+1,kLen,1):
        katok[i-1]=katok[i]
        katok[i]=None
    del(katok[kLen-1])


# def insert_data(n,friend):
#     katok.append(None)
#     kLen = len(katok)
#     for i in kLen:
#         katok[kLen]=None
#         if kLen-n ==0:
#             katok[n]=friend
#         else:
#
#             katok[kLen]=katok[kLen-1]
#             kLen[kLen-1]=0
#             katok[kLen-1]=katok[kLen-2]
#             kLen[kLen-n]=None

##전역 변수부
katok=[]

##메인 코드부
# add_data('다현')
# add_data('정연')
# add_data('쯔위')
# add_data('사나')
# add_data('지효')
# add_data('모모')
#
# insert_data(3,'미나')
# delete_data(4)

# #데이터 삽입
# katok.append(None) #1
#
# katok[6]=katok[5] #2
# katok[5]=None
# katok[5]=katok[4]
# katok[4]=None
# katok[4]=katok[3]
# katok[3]=None
#
# katok[3]='미나' #3


# katok.append(None) #빈칸 추가
# katok[0]='다현'
# katok.append(None) #빈칸 추가
# katok[1]='정연'
# katok.append(None) #빈칸 추가
# katok[2]='쯔위'
# katok.append(None) #빈칸 추가
# katok[3]='사나'
# katok.append(None) #빈칸 추가
# katok[4]='지효'

##메인코드
if __name__=="__main__" :

    select = int(input("선택하세요 (1:추가 2:삽입 3:삭제 4:종료)--> "))
    while (select !=4):

        if (select==1):
            data=input("추가할 데이터 --> ")
            add_data(data)
            print(katok)
        elif (select==2):
            pos=int(input("삽입할 위치--> "))
            data=input("추가할 데이터 -->")
            insert_data(pos,data)
            print(katok)
        elif (select==3):
            pos=int(input("삭제할 위치--> "))
            delete_data(pos)
            print(katok)
        elif (select==4):
            print(katok)
            exit
        else:
            print("1~4 중 하나를 입력하세요.")
            continue
