'''
참고사항
1. 주어진 변수 외에 본인이 사용하거나 main 동작 중에 입력받으면 좋겠다 하는 함수가 있으면 변수를 추가하셔도 좋습니다!
2. 기본적으로 세팅한 변수는 각 클래스의 __init__에 명시되어 있으니 참고하시면 되겠습니다!
3. 이 .py 파일의 main 부분은 나중에 추가해서 다시 업로드 하겠습니담.. 일단 함수 만들어주세용...
4. 여러분들 깃에 commit 하기 전에 꼭 카톡방에 다 했다 올려주시고 대기해주세용...! (제일 중요중요)
    >> 최악의 경우는 충돌 생겨서 처음부터 다시 할 수도...
'''


import random
import numpy

# 구분선 출력 함수
def printLine():
    for i in range(50):
        print("-", end='')
    print("\n", end='')

#구이연's part
# 참가자의 순서를 정하는 함수
# 함수 input하는 매개변수는 원하는 대로 추가하셔도 됩니다.
def indexSet(parti_list):
    random.shuffle(parti_list)
    order_dict = {i:parti_list[i] for i in range(4)}

    return order_dict

class BlockInfo:
  number = "-1"
  color = "검"
  def __init__(self, number, color):
    self.number = number
    self.color = color

class Block:
    # 1~4번째 순서의 사람들이 가질 블럭들 저장하는 변수들 선언, 파이썬은 포인터가 없어서 딕셔너리로 구현해주시면 될 것 같습니다.
    # Ex, Block.blockLine_1[num] == "1-233479", Block.blockLine_3[color] == "검검흰검흰흰", Block.blockLine_2[open] = "TFFTTTFF"
    # index 설명 >> num: 숫자 & 조커 값을 문자열로 저장(순차적으로), color: 블럭이 흰색인지 검은색인지 저장하는 문자열, open: 블럭이 open 됐는지 여부를 저장하는 문자열

    toDistribute = []  # 나눠줄 블럭들을 모아놓을 리스트

    def __init__(self):
        self.blockLine_0 = {"num": [], "color": [], "open": []}
        self.blockLine_1 = {"num": [], "color": [], "open": []}
        self.blockLine_2 = {"num": [], "color": [], "open": []}
        self.blockLine_3 = {"num": [], "color": [], "open": []}
        self.blockLeft = {"num": [], "color": []}  # 분배하고 나중에 하나씩 가져갈 블럭들 넣어놓는 곳

        self.makeToDistribute()

    def makeToDistribute(self):
        for i in range(0, 12):
            temp = BlockInfo(str(i), "검")
            self.toDistribute.append(temp)
        for i in range(0, 12):
            temp = BlockInfo(str(i), "흰")
            self.toDistribute.append(temp)
        self.toDistribute.append(BlockInfo("-", "검"))
        self.toDistribute.append(BlockInfo("-", "흰"))

    # 이정현's part
    # 난수 발생시켜서 네명의 사용자에게 블럭들 주는 함수
    def giveBlock(self):
        random.shuffle(self.toDistribute)
        for i in range(0, 4):
            num = []
            color = []
            open = ["F", "F", "F"]
            for j in range(0, 3):
                temp = self.toDistribute.pop()
                for k in range(0, len(num)):
                    if temp.number != '-' and num[k] != '-':
                        if int(temp.number) < int(num[k]):
                            hold_num = num[k:]
                            hold_color = color[k:]
                            num.append(temp.number)
                            color.append(temp.color)
                            num.append(hold_num)
                            color.append(hold_color)
                            break

                        elif (int(temp.number) == int(self.toDistribute[k].number)) and (temp.color == "검") and (self.toDistribute.color == "흰"):
                            hold_num = num[k:]
                            hold_color = color[k:]
                            num.append(temp.number)
                            color.append(temp.color)
                            num.append(hold_num)
                            color.append(hold_color)
                            break

            if i == 0:
                self.blockLine_0['num'] = num
                self.blockLine_0['color'] = color
                self.blockLine_0['open'] = open
            elif i == 1:
                self.blockLine_1['num'] = num
                self.blockLine_1['color'] = color
                self.blockLine_1['open'] = open
            elif i == 2:
                self.blockLine_2['num'] = num
                self.blockLine_2['color'] = color
                self.blockLine_2['open'] = open
            elif i == 3:
                self.blockLine_3['num'] = num
                self.blockLine_3['color'] = color
                self.blockLine_3['open'] = open

    #박강우's part
    # 블럭들을 게임 시작전 배분하고 나서, 블럭을 정렬하는 함수 (처음 정렬할 때에는 조커블럭의 위치는 사용자가 정할 수 있도록 할 것!)
    def alignBlock(self, i):
        if i == 0:
            blockLine = self.blockLine_0
        elif i == 1:
            blockLine = self.blockLine_1
        elif i == 2:
            blockLine = self.blockLine_2
        elif i == 3:
            blockLine = self.blockLine_3

        n = blockLine["num"].pop()  # 숫자 저장
        s = blockLine["color"].pop()  # 색 저장
        k = blockLine["open"].pop()  # open 여부 저장

        if n != "-":
            temp_check = 0
            for j in range(0, len(blockLine["num"]) - 1):
                if int(blockLine["num"][j]) > int(n):
                    temp_num = blockLine["num"][j:]
                    temp_color = blockLine["color"][j:]
                    temp_open =  blockLine["open"][j:]
                    blockLine["num"] = blockLine["num"][:j]
                    blockLine["color"] = blockLine["color"][:j]
                    blockLine["open"] = blockLine["open"][:j]
                    blockLine["num"].append(n)
                    blockLine["color"].append(s)
                    blockLine["open"].append(k)
                    blockLine["num"].append(temp_num)
                    blockLine["num"].append(temp_color)
                    blockLine["num"].append(temp_open)
                    return

                elif (int(blockLine["num"][j]) == int(n)) and (s == "검") and (blockLine["color"][j] == "흰"):
                    temp_num = blockLine["num"][j:]
                    temp_color = blockLine["color"][j:]
                    temp_open = blockLine["open"][j:]
                    blockLine["num"] = blockLine["num"][:j]
                    blockLine["color"] = blockLine["color"][:j]
                    blockLine["open"] = blockLine["open"][:j]
                    blockLine["num"].append(n)
                    blockLine["color"].append(s)
                    blockLine["open"].append(k)
                    blockLine["num"].append(temp_num)
                    blockLine["num"].append(temp_color)
                    blockLine["num"].append(temp_open)
                    return

                temp_check = j

            if temp_check == len(blockLine["num"]):
                blockLine["num"].append(n)
                blockLine["color"].append(s)
                blockLine["open"].append(k)
                return
        else:
            idx = int(input("조커를 넣을 위치(index: 0~)를 입력하세요: "))
            temp_num = blockLine["num"][idx:]
            temp_color = blockLine["color"][idx:]
            temp_open = blockLine["open"][idx:]
            blockLine["num"] = blockLine["num"][:idx]
            blockLine["color"] = blockLine["color"][:idx]
            blockLine["open"] = blockLine["open"][:idx]
            blockLine["num"].append(n)
            blockLine["color"].append(s)
            blockLine["open"].append(k)
            blockLine["num"].append(temp_num)
            blockLine["num"].append(temp_color)
            blockLine["num"].append(temp_open)
            return

    # 박강우's part
    # 현재 오픈된 블럭을 포함하는 모든 플레이어의 블럭 열을 상대방에게 보여주는 함수
    def showBlock(self, blockLine):
        for i in range(len(blockLine["num"])):
            print(blockLine["num"][i], end="")
        print("")
        for i in range(len(blockLine["color"])):
            print(blockLine["color"][i], end="")
        print("")

    def showBlockOppo(self, blockLine):
        for i in (range(len(blockLine["open"]))):
            if blockLine["open"][j] == "T":
                print(i, end="")
            else:
                print("X", end="")
        print("")
        for i in blockLine["color"]:
            print(i, end="")
        print("")

    #김현준's part
    # 새로운 블럭을 본인의 블럭 열로 가져오는 함수
    def addNew(self, blockLine):
        if self.toDistribute != []:
            temp = self.toDistribute.pop()
            blockLine["num"].append(temp.number)
            blockLine["color"].append(temp.color)
            blockLine["open"].append("F")
        else:
            print("더이상 배분할 블럭이 없습니다.")
            return

class Game:
    # 본인이 함수를 작성하시고 필요한 변수는 여기에 초기화해서 선언하기!!
    # 단, 블럭 열이나 사용자의 정보 또는 함수는 Block 클래스와 Login 클래스의 내용들 사용하기! 추가하지 말고

    currentPlayerId = 0
    opponentPlayerId = ""
    opponentPlayernumidx = []
    opponentPlayernum = []

    def __init__(self):
        pass

    #이정현's part
    # 자신의 차례인 사람이 누구의 블럭을 지목할지, 그 플레이어를 고르는 함수
    def pickPlayer(self, i):
        self.opponentPlayerId = int(input("{0}번 플레이어는 지목할 플레이어의 번호를 입력하세요: ".format(i)))
        return self.opponentPlayerId

    #구이연's part
    # 지목한 플레이어의 블럭이 내가 생각한 블럭이 맞나 확인하는 함수 # 수정 싹 해야함...
    def checkBlock(self, expected, actual):
        if expected['num'] == actual['num'][expected['idx']] and actual['open'][expected['idx']] == 'F':
            if expected['num'] == actual['num'][expected['idx']] :
                print("맞췄습니다.") #여기까지 수정함.
                open_list = list(actual['open'])
                open_list[expected["idx"]] = 'T'
                actual['open'] = ''.join(open_list)
                return 'Y'
        elif expected['num'] != actual['num'][expected['idx']]:
            print('숫자가 틀렸습니다.')
            return 'N1'
        elif actual['open'][expected['idx']] == 'T':
            print("이미 맞춘 블록입니다.")
            return 'N2'


    #김다운's part
    # 자신의 턴을 마칠지, 아니면 주가적으로 블럭을 맞추러 갈지 고르는 함수
    #return 값은 true or false
    def checkBlockAgain(self):
        while (True) :
            check = input("턴을 종료하시겠습니까?(Y/N): ")
            if check == 'Y' or check == 'y' :
                return False
            elif check == 'N' or check == 'n' :
                return True
            else :
                print("올바른 입력을 주십시오.")
                continue


    #김다운's part
    # 승패자가 결정 되었는지 확인하는 함수
    # return 값은 true or false
    def isWinner(self, blockLine):
        for i in range(0, len(blockLine["open"])):
            if blockLine["open"][i] == "F":
                return True
        return False


    #김현준's part
    # 재시작 여부 확인하는 함수
    # return 값은 true or false
    def restart(self):
        printLine()
        while (True) :
            check = input("게임을 재시작하시겠습니까?(Y/N): ")
            if check == 'Y' or check == 'y' :
                printLine()
                return True
            elif check == 'N' or check == 'n' :
                printLine()
                return False
            else :
                print("올바른 입력을 주십시오.")
                continue


# main

my_block = Block()
my_game = Game()
doing = False
while doing == False:
    printLine()
    print("\n게임을 시작합니다!")
    print("블럭은 배분하고 있습니다...")
    my_block.makeToDistribute()
    my_block.giveBlock()
    while True:
        turn = 0
        for i in (my_block.blockLine_0, my_block.blockLine_1, my_block.blockLine_2, my_block.blockLine_3):
            my_block.showBlock(i)

        check = (True, True, True, True)
        for Blocks in (my_block.blockLine_0, my_block.blockLine_1, my_block.blockLine_2, my_block.blockLine_3):
            for i in range(len(Blocks["num"])):
                if my_game.isWinner(Blocks) == False:
                    check[i] = False
                    break

        count = 0
        for i in range(4):
            if check[i] == False:
                count += 1

        if count == 3:
            if my_game.restart() == True:
                pass
            else:
                print("게임을 종료합니다.")
                doing = False
                break
                
        print("다음 플레이어의 차례입니다...")
        turn = turn % 4 + 1
        if turn == 0 and check[0] == True:
            player = my_block.blockLine_0
            print("0번 플레이어의 차례입니다!")
        elif turn == 1 and check[1] == True:
            player = my_block.blockLine_1
            print("1번 플레이어의 차례입니다!")
        elif turn == 2 and check[2] == True:
            player = my_block.blockLine_2
            print("2번 플레이어의 차례입니다!")
        elif turn == 3 and check[3] == True:
            player = my_block.blockLine_3
            print("3번 플레이어의 차례입니다!")

        my_block.addNew(player)
        my_block.alignBlock(turn)

        while True:
            print("블럭을 맞출 상대 플레이어를 선택합니다...")
            while True:
                opponent = my_game.pickPlayer(turn)
                if opponent == 0:
                    opponent = my_block.blockLine_0
                    break
                elif opponent == 1:
                    opponent = my_block.blockLine_1
                    break
                elif opponent == 2:
                    opponent = my_block.blockLine_2
                    break
                elif opponent == 3:
                    opponent = my_block.blockLine_3
                    break
                else:
                    print("다시 0에서 3까지 중에서 올바른 값을 입력해주세요.")

            my_block.showBlock(player)
            my_block.showBlockOppo(opponent)

            expected = {"num": 0, "idx": 0}
            expected["idx"] = int(input("왼쪽에서 몇 번째 블럭을 맞출지 입력하세요: ")) - 1
            expected["num"] = int(input("해당 블럭의 숫자가 무엇일지 맞추세요: "))

            result = my_game.checkBlock(expected, opponent)
            if result == 'Y':
                print("상대방 플레이어의 블럭을 맞추셨습니다!")
                result = my_game.checkBlock()
                if result == True:
                    break
                else:
                    pass
            elif result == 'N1':
                openBlk = int(input("틀렸으므로, 본인의 블럭을 오픈합니다. index 입력(0~):"))
                player["open"][openBlk] = "T"
            else:
                pass
