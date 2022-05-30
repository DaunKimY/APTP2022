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
#import pygame
# import socket, threading

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
        self.blockLine_0 = {"num": [], "color": "", "open": ""}
        self.blockLine_1 = {"num": [], "color": "", "open": ""}
        self.blockLine_2 = {"num": [], "color": "", "open": ""}
        self.blockLine_3 = {"num": [], "color": "", "open": ""}
        self.blockLeft = {"num": [], "color": ""}  # 분배하고 나중에 하나씩 가져갈 블럭들 넣어놓는 곳

        self.makeToDistribute()

    def makeToDistribute(self):
        for i in range(0, 12):
            temp = self.BlockInfo(str(i), "검")
            self.toDistribute.append(temp)
        for i in range(0, 12):
            temp = self.BlockInfo(str(i), "흰")
            self.toDistribute.append(temp)
        self.toDistribute.append(self.BlockInfo("-", "검"))
        self.toDistribute.append(self.BlockInfo("-", "흰"))

    # 이정현's part
    # 난수 발생시켜서 네명의 사용자에게 블럭들 주는 함수
    def giveBlock(self):
        random.shuffle(self.toDistribute)
        for i in range(0, 4):
            num = []
            color = ""
            open = "FFF"
            for j in range(0, 3):
                temp = self.toDistribute.pop()
                num.append(temp.number)
                color += temp.color
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

        num_for_left_blocks = []
        color_for_left_blocks = ""
        for i in range(0, 14):
            temp = self.toDistribute.pop()
            num_for_left_blocks.append(temp.number)
            color_for_left_blocks += temp.color
        self.blockLeft['num'] = num_for_left_blocks
        self.blockLeft['color'] = color_for_left_blocks

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

        cnt = 0
        for p in range(0, len(blockLine["num"])):
            if blockLine["num"][p] == '-':
                cnt += 1  # 조커 있으면 cnt값 1 증가
        if cnt == 0:  # 조커 없을 때
            for j in range(0, len(blockLine["num"]) - 1):
                if blockLine["num"][j] > blockLine["num"][j + 1]:  # 왼쪽 숫자가 더 클 때
                    n = blockLine["num"][j]  # 숫자 저장
                    s = blockLine["color"][j]  # 색 저장
                    blockLine["num"][j] = blockLine["num"][j + 1]  # 오름차순 정렬
                    blockLine["num"][j + 1] = n  # 오름차순 정렬
                    blockLine["color"][j] = blockLine["color"][j + 1]  # 색깔도 바꾸기
                    blockLine["color"][j + 1] = s  # 색깔도 바꾸기
                elif blockLine["num"][j] == blockLine["num"][j + 1]:  # 연속하는 숫자가 같을 때
                    if blockLine["color"][j] == "흰":  # 왼쪽 블럭가 흰색이면
                        blockLine["color"][j] = "검"  # 왼쪽 블럭을 검정색
                        blockLine["color"][j + 1] = "흰"  # 오른쪽 블럭을 흰색으로

        elif cnt == 1:  # 조커 1개일 때
            for j in range(0, len(blockLine[i]["num"]) - 1):
                if blockLine["num"][j] == '-':  # j번째 숫자가 조커일 때
                    joker = blockLine["num"][j]  # 조커 저장
                    joker_c = blockLine["color"][j]  # 색 저장
                    blockLine["num"][j] = blockLine["num"][
                        len(blockLine["num"]) - 1]  # 마지막 숫자랑 조커 위치 바꾸기
                    blockLine["num"][len(blockLine["num"]) - 1] = joker  # 마지막 숫자랑 조커 위치 바꾸기
                    blockLine["color"][j] = blockLine["color"][
                        len(blockLine["num"]) - 1]  # 색깔도 바꾸기
                    blockLine["color"][len(blockLine["num"]) - 1] = joker_c  # 색깔도 바꾸기
                if blockLine["num"][j] > blockLine["num"][j + 1]:  # 왼쪽 숫자가 더 클 때
                    n = blockLine["num"][j]  # 숫자 저장
                    s = blockLine["color"][j]  # 색 저장
                    blockLine["num"][j] = blockLine["num"][j + 1]  # 오름차순 정렬
                    blockLine["num"][j + 1] = n  # 오름차순 정렬
                    blockLine["color"][j] = blockLine["color"][j + 1]  # 색깔도 바꾸기
                    blockLine["color"][j + 1] = s  # 색깔도 바꾸기
                elif blockLine["num"][j] == blockLine["num"][j + 1]:  # 연속하는 숫자가 같을 때
                    if blockLine["color"][j] == "흰":  # 왼쪽 블럭가 흰색이면
                        blockLine["color"][j] = "검"  # 왼쪽 블럭을 검정색
                        blockLine["color"][j + 1] = "흰"  # 오른쪽 블럭을 흰색으로
            if blockLine["num"][len(blockLine["num"]) - 1] == '-':  # 조커가 존재해서 조커를 맨 뒤로 보낸 상황일 때
                self.idx = int(input('몇번째 자리에 조커를 넣으시겠습니까?(1~): '))  # 조커 어디에 넣을지 질문
                for k in range(len(blockLine["num"]), self.idx, -1):  # 마지막 자리부터 한 칸씩 왼쪽으로 이동해서 원하는 자리에 위치
                    store = blockLine["num"][k - 1]  # 조커 저장
                    store_c = blockLine["color"][k - 1]  # 조커 색 저장
                    blockLine["num"][k - 1] = blockLine["num"][k - 2]  # 조커 왼쪽으로 이동
                    blockLine["num"][k - 2] = store  # 조커 왼쪽으로 이동
                    blockLine["color"][k - 1] = blockLine["color"][k - 2]  # 색깔도 이동
                    blockLine["color"][k - 2] = store_c  # 색깔도 이동

        elif cnt == 2:  # 조커가 2개일 때
            if blockLine["num"][len(blockLine["num"]) - 1] == '-' and blockLine[i]["num"][
                len(blockLine["num"]) - 2] == '-':  # 뒤에 2개가 다 조커일 때
                for j in range(0, len(blockLine["num"] - 3)):
                    if blockLine["num"][j] > blockLine["num"][j + 1]:  # 왼쪽 숫자가 더 클 때
                        n = blockLine["num"][j]  # 숫자 저장
                        s = blockLine["color"][j]  # 색 저장
                        blockLine["num"][j] = blockLine["num"][j + 1]  # 오름차순 정렬
                        blockLine["num"][j + 1] = n  # 오름차순 정렬
                        blockLine["color"][j] = blockLine["color"][j + 1]  # 색깔도 바꾸기
                        blockLine["color"][j + 1] = s  # 색깔도 바꾸기
                    elif blockLine["num"][j] == blockLine["num"][j + 1]:  # 연속하는 숫자가 같을 때
                        if blockLine["color"][j] == "흰":  # 왼쪽 블럭가 흰색이면
                            blockLine["color"][j] = "검"  # 왼쪽 블럭을 검정색
                            blockLine["color"][j + 1] = "흰"  # 오른쪽 블럭을 흰색으로
                self.idx1 = int(input('조커가 두 개입니다. 첫번째 조커를 어디에 넣으시겠습니까?: '))  # 첫번째 조커 어디에 넣을지 질문
                self.idx2 = int(input('조커가 두 개입니다. 두번째 조커를 어디에 넣으시겠습니까?: '))  # 두번째 조커 어디에 넣을지 질문
                for k in range(len(blockLine["num"]) - 1, self.idx1,
                               -1):  # 끝에서 두 번째 자리에 위치한 조커부터 한 칸씩 왼쪽으로 이동해서 원하는 자리에 위치
                    store = blockLine["num"][k - 1]  # 조커 저장
                    store_c = blockLine["color"][k - 1]  # 조커 색 저장
                    blockLine["num"][k - 1] = blockLine["num"][k - 2]  # 조커 왼쪽으로 이동
                    blockLine["num"][k - 2] = store  # 조커 왼쪽으로 이동
                    blockLine["color"][k - 1] = blockLine["color"][k - 2]  # 색깔도 이동
                    blockLine["color"][k - 2] = store_c  # 색깔도 이동
                for k in range(len(blockLine["num"]), self.idx2, -1):  # 끝에 위치한 조커부터 한 칸씩 왼쪽으로 이동해서 원하는 자리에 위치
                    store = blockLine["num"][k - 1]  # 조커 저장
                    store_c = blockLine["color"][k - 1]  # 조커 색 저장
                    blockLine["num"][k - 1] = blockLine["num"][k - 2]  # 조커 왼쪽으로 이동
                    blockLine["num"][k - 2] = store  # 조커 왼쪽으로 이동
                    blockLine["color"][k - 1] = blockLine["color"][k - 2]  # 색깔도 이동
                    blockLine["color"][k - 2] = store_c  # 색깔도 이동

            elif blockLine["num"][len(blockLine["num"]) - 1] == '-' and blockLine["num"][
                len(blockLine["num"]) - 2] != '-':  # 맨 끝에만 조커가 있을 때
                for j in range(0, len(blockLine["num"]) - 2):
                    if blockLine["num"][j] == '-':  # j번째 숫자가 조커일 때
                        joker = blockLine["num"][j]  # 조커 저장
                        joker_c = blockLine["color"][j]  # 색 저장
                        blockLine["num"][j] = blockLine["num"][
                            len(blockLine["num"]) - 2]  # 마지막에서 두 번째 숫자랑 조커 위치 바꾸기
                        blockLine["num"][len(blockLine["num"]) - 2] = joker  # 마지막 숫자랑 조커 위치 바꾸기
                        blockLine["color"][j] = blockLine["color"][
                            len(blockLine["num"]) - 2]  # 색깔도 바꾸기
                        blockLine["color"][len(blockLine["num"]) - 2] = joker_c  # 색깔도 바꾸기
                for j in range(0, len(blockLine["num"] - 3)):
                    if blockLine["num"][j] > blockLine["num"][j + 1]:  # 왼쪽 숫자가 더 클 때
                        n = blockLine["num"][j]  # 숫자 저장
                        s = blockLine["color"][j]  # 색 저장
                        blockLine["num"][j] = blockLine["num"][j + 1]  # 오름차순 정렬
                        blockLine["num"][j + 1] = n  # 오름차순 정렬
                        blockLine["color"][j] = blockLine["color"][j + 1]  # 색깔도 바꾸기
                        blockLine["color"][j + 1] = s  # 색깔도 바꾸기
                    elif blockLine["num"][j] == blockLine["num"][j + 1]:  # 연속하는 숫자가 같을 때
                        if blockLine["color"][j] == "흰":  # 왼쪽 블럭가 흰색이면
                            blockLine["color"][j] = "검"  # 왼쪽 블럭을 검정색
                            blockLine["color"][j + 1] = "흰"  # 오른쪽 블럭을 흰색으로
                self.idx1 = int(input('조커가 두 개입니다. 첫번째 조커를 어디에 넣으시겠습니까?: '))  # 첫번째 조커 어디에 넣을지 질문
                self.idx2 = int(input('조커가 두 개입니다. 두번째 조커를 어디에 넣으시겠습니까?: '))  # 두번째 조커 어디에 넣을지 질문
                for k in range(len(blockLine["num"]) - 1, self.idx1,
                               -1):  # 끝에서 두 번째 자리에 위치한 조커부터 한 칸씩 왼쪽으로 이동해서 원하는 자리에 위치
                    store = blockLine["num"][k - 1]  # 조커 저장
                    store_c = blockLine["color"][k - 1]  # 조커 색 저장
                    blockLine["num"][k - 1] = blockLine["num"][k - 2]  # 조커 왼쪽으로 이동
                    blockLine["num"][k - 2] = store  # 조커 왼쪽으로 이동
                    blockLine["color"][k - 1] = blockLine["color"][k - 2]  # 색깔도 이동
                    blockLine["color"][k - 2] = store_c  # 색깔도 이동
                for k in range(len(blockLine["num"]), self.idx2, -1):  # 끝에 위치한 조커부터 한 칸씩 왼쪽으로 이동해서 원하는 자리에 위치
                    store = blockLine["num"][k - 1]  # 조커 저장
                    store_c = blockLine["color"][k - 1]  # 조커 색 저장
                    blockLine["num"][k - 1] = blockLine["num"][k - 2]  # 조커 왼쪽으로 이동
                    blockLine["num"][k - 2] = store  # 조커 왼쪽으로 이동
                    blockLine["color"][k - 1] = blockLine["color"][k - 2]  # 색깔도 이동
                    blockLine["color"][k - 2] = store_c  # 색깔도 이동

            elif blockLine["num"][len(blockLine["num"]) - 1] != '-' and blockLine["num"][
                len(blockLine["num"]) - 2] == '-':  # 끝에서 두 번째 자리에만 조커가 있을 때
                for j in range(0, len(blockLine["num"]) - 2):
                    if blockLine["num"][j] == '-':  # j번째 숫자가 조커일 때
                        joker = blockLine["num"][j]  # 조커 저장
                        joker_c = blockLine["color"][j]  # 색깔도 저장
                        blockLine["num"][j] = blockLine["num"][
                            len(blockLine["num"]) - 1]  # 마지막 숫자랑 조커 위치 바꾸기
                        blockLine["num"][len(blockLine["num"]) - 1] = joker  # 마지막 숫자랑 조커 위치 바꾸기
                        blockLine["color"][j] = blockLine["color"][
                            len(blockLine["num"]) - 1]  # 색깔도 바꾸기
                        blockLine["color"][len(blockLine["num"]) - 1] = joker_c  # 색깔도 바꾸기
                for j in range(0, len(blockLine["num"] - 3)):
                    if blockLine["num"][j] > blockLine["num"][j + 1]:  # 왼쪽 숫자가 더 클 때
                        n = blockLine["num"][j]  # 숫자 저장
                        s = blockLine["color"][j]  # 색 저장
                        blockLine["num"][j] = blockLine["num"][j + 1]  # 오름차순 정렬
                        blockLine["num"][j + 1] = n  # 오름차순 정렬
                        blockLine["color"][j] = blockLine["color"][j + 1]  # 색깔도 바꾸기
                        blockLine["color"][j + 1] = s  # 색깔도 바꾸기
                    elif blockLine["num"][j] == blockLine["num"][j + 1]:  # 연속하는 숫자가 같을 때
                        if blockLine["color"][j] == "흰":  # 왼쪽 블럭가 흰색이면
                            blockLine["color"][j] = "검"  # 왼쪽 블럭을 검정색
                            blockLine["color"][j + 1] = "흰"  # 오른쪽 블럭을 흰색으로
                self.idx1 = int(input('조커가 두 개입니다. 첫번째 조커를 어디에 넣으시겠습니까?: '))  # 첫번째 조커 어디에 넣을지 질문
                self.idx2 = int(input('조커가 두 개입니다. 두번째 조커를 어디에 넣으시겠습니까?: '))  # 두번째 조커 어디에 넣을지 질문
                for k in range(len(blockLine["num"]) - 1, self.idx1,
                               -1):  # 끝에서 두 번째 자리에 위치한 조커부터 한 칸씩 왼쪽으로 이동해서 원하는 자리에 위치
                    store = blockLine["num"][k - 1]  # 조커 저장
                    store_c = blockLine["color"][k - 1]  # 조커 색 저장
                    blockLine["num"][k - 1] = blockLine["num"][k - 2]  # 조커 왼쪽으로 이동
                    blockLine["num"][k - 2] = store  # 조커 왼쪽으로 이동
                    blockLine["color"][k - 1] = blockLine["color"][k - 2]  # 색깔도 이동
                    blockLine["color"][k - 2] = store_c  # 색깔도 이동
                for k in range(len(blockLine["num"]), self.idx2,
                               -1):  # 끝에 위치한 조커부터 한 칸씩 왼쪽으로 이동해서 원하는 자리에 위치
                    store = blockLine["num"][k - 1]  # 조커 저장
                    store_c = blockLine["color"][k - 1]  # 조커 색 저장
                    blockLine["num"][k - 1] = blockLine["num"][k - 2]  # 조커 왼쪽으로 이동
                    blockLine["num"][k - 2] = store  # 조커 왼쪽으로 이동
                    blockLine["color"][k - 1] = blockLine["color"][k - 2]  # 색깔도 이동
                    blockLine["color"][k - 2] = store_c  # 색깔도 이동

            elif blockLine["num"][len(blockLine["num"]) - 1] != '-' and blockLine["num"][
                len(blockLine["num"]) - 2] != '-':  # 끝에서 2개 다 조커가 아닐 때
                for j in range(0, len(blockLine["num"]) - 2):
                    if blockLine["num"][j] == '-' and blockLine["num"][
                        len(blockLine["num"]) - 1] != '-':  # 처음 발견한 조커 맨 뒤로 보내기
                        joker1 = blockLine["num"][j]  # 조커 저장
                        joker1_c = blockLine["color"][j]  # 색 저장
                        blockLine["num"][j] = blockLine["num"][
                            len(blockLine["num"]) - 1]  # 마지막 숫자랑 조커 위치 바꾸기
                        blockLine["num"][len(blockLine["num"]) - 1] = joker1  # 마지막 숫자랑 조커 위치 바꾸기
                        blockLine["color"][j] = blockLine["color"][
                            len(blockLine["num"]) - 1]  # 색깔도 바꾸기
                        blockLine["color"][len(blockLine["num"]) - 1] = joker1_c  # 색깔도 바꾸기
                    elif blockLine["num"][j] == '-' and blockLine["num"][
                        len(blockLine["num"]) - 1] == '-':  # 맨 뒤로 조커를 보낸 상태에서 조커를 하나 더 찾을 때
                        joker2 = blockLine["num"][j]  # 조커 저장
                        joker2_c = blockLine["color"][j]  # 색 저장
                        blockLine["num"][j] = blockLine["num"][
                            len(blockLine["num"]) - 2]  # 마지막에서 두 번째 숫자랑 조커 위치 바꾸기
                        blockLine["num"][len(blockLine["num"]) - 2] = joker2  # 마지막에서 두 번째 숫자랑 조커 위치 바꾸기
                        blockLine["color"][j] = blockLine["color"][
                            len(blockLine["num"]) - 2]  # 색깔도 바꾸기
                        blockLine["color"][len(blockLine["num"]) - 1] = joker2_c  # 색깔도 바꾸기
                for j in range(0, len(blockLine["num"] - 3)):
                    if blockLine["num"][j] > blockLine["num"][j + 1]:  # 왼쪽 숫자가 더 클 때
                        n = blockLine["num"][j]  # 숫자 저장
                        s = blockLine["color"][j]  # 색 저장
                        blockLine["num"][j] = blockLine["num"][j + 1]  # 오름차순 정렬
                        blockLine["num"][j + 1] = n  # 오름차순 정렬
                        blockLine["color"][j] = blockLine["color"][j + 1]  # 색깔도 바꾸기
                        blockLine["color"][j + 1] = s  # 색깔도 바꾸기
                    elif blockLine["num"][j] == blockLine["num"][j + 1]:  # 연속하는 숫자가 같을 때
                        if blockLine["color"][j] == "흰":  # 왼쪽 블럭가 흰색이면
                            blockLine["color"][j] = "검"  # 왼쪽 블럭을 검정색
                            blockLine["color"][j + 1] = "흰"  # 오른쪽 블럭을 흰색으로
                self.idx1 = int(input('조커가 두 개입니다. 첫번째 조커를 어디에 넣으시겠습니까?: '))  # 첫번째 조커 어디에 넣을지 질문
                self.idx2 = int(input('조커가 두 개입니다. 두번째 조커를 어디에 넣으시겠습니까?: '))  # 두번째 조커 어디에 넣을지 질문
                for k in range(len(blockLine[i]["num"]) - 1, self.idx1,
                               -1):  # 끝에서 두 번째 자리에 위치한 조커부터 한 칸씩 왼쪽으로 이동해서 원하는 자리에 위치
                    store = blockLine["num"][k - 1]  # 조커 저장
                    store_c = blockLine["color"][k - 1]  # 조커 색 저장
                    blockLine["num"][k - 1] = blockLine["num"][k - 2]  # 조커 왼쪽으로 이동
                    blockLine["num"][k - 2] = store  # 조커 왼쪽으로 이동
                    blockLine["color"][k - 1] = blockLine["color"][k - 2]  # 색깔도 이동
                    blockLine["color"][k - 2] = store_c  # 색깔도 이동
                for k in range(len(blockLine["num"]), self.idx2,
                               -1):  # 끝에 위치한 조커부터 한 칸씩 왼쪽으로 이동해서 원하는 자리에 위치
                    store = blockLine["num"][k - 1]  # 조커 저장
                    store_c = blockLine["color"][k - 1]  # 조커 색 저장
                    blockLine["num"][k - 1] = blockLine["num"][k - 2]  # 조커 왼쪽으로 이동
                    blockLine["num"][k - 2] = store  # 조커 왼쪽으로 이동
                    blockLine["color"][k - 1] = blockLine["color"][k - 2]  # 색깔도 이동
                    blockLine["color"][k - 2] = store_c  # 색깔도 이동

    # 박강우's part
    # 현재 오픈된 블럭을 포함하는 모든 플레이어의 블럭 열을 상대방에게 보여주는 함수
    def showBlock(self, blockLine):
        for i in blockLine["num"]:
            print(i, end="")
        print("")
        for i in blockLine["color"]:
            print(i, end="")
        print("")

    def showBlockOppo(self, blockLine):
        for i,j in (blockLine["num"], range(len(blobkLine["open"]))):
            if blobkLine["open"][j] == "T":
                print(i, end="")
            else:
                print("X", end="")
        print("")
        for i in blockLine["color"]:
            print(i, end="")
        print("")

    #김현준's part
    # 새로운 블럭을 본인의 블럭 열로 가져오는 함수
    def addNew(self, blockLine, blockLeft):
        if blockLeft["num"] != "":
            blockLine["num"].append(blockLeft["num"][0])
            blockLine["color"].append(blockLeft["color"][0])
            blockLine["open"].append("F")
            blockLeft["num"] = blockLeft[1:len(blockLeft["num"])]
            blockLeft["color"] = blockLeft[1:len(blockLeft["color"])]
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
        if expected['num'] == actual['num'][expected['idx']] and actual['open'][expected['idx']] == F :
            if expected['num'] == actual['num'][expected['idx']] :
                print("맞췄습니다.") #여기까지 수정함.
                open_list = list(actual['open'])
                open_list[expected["idx"]] = 'T'
                actual['open'] = ''.join(open_list)
                return 'Y'
        elif expected['num'] != actual['num'][expected['idx']] :
            print('숫자가 틀렸습니다.')
            return 'N1'
        elif actual['open'][expected['idx']] == 'T' :
            print("이미 맞춘 블록입니다.")
            return 'N2'


    #김다운's part
    # 자신의 턴을 마칠지, 아니면 주가적으로 블럭을 맞추러 갈지 고르는 함수
    #return 값은 true or false
    def checkBlockAgain(self):
        while (True) :
            check = input("턴을 종료하시겠습니까?(Y/N): ")
            if check == 'Y' or check == 'y' :
                return false
            elif check == 'N' or check == 'n' :
                return true
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
                return true
            elif check == 'N' or check == 'n' :
                printLine()
                return false
            else :
                print("올바른 입력을 주십시오.")
                continue


# main


doing = False
while doing == False:
    printLine()
    print("\n게임을 시작합니다!")
    print("블럭은 배분하고 있습니다...")
    Block.giveBlock()
    print("조커를 포함한 각 플레이어의 블럭을 정렬하고 있습니다..")
    for i in range(4):
        Block.alignBlock(i)

    while True:
        for i in (Block.blockLine_0, Block.blockLine_1, Block.blockLine_2, Block.blockLine_3):
            Block.showBlock(i)

        check = (True, True, True, True)
        for i, Blocks in enumerate(Block.blockLine_0, Block.blockLine_1, Block.blockLine_2, Block.blockLine_3):
            if Game.isWinner(Blocks) == False:
                check[i] = False

        count = 0
        for i in range(4):
            if check[i] == False:
                count += 1

        if count == 3:
            if Game.restart() == True:
                pass
            else:
                print("게임을 종료합니다.")
                break

        print("다음 플레이어의 차례입니다...")
        turn = turn % 4 + 1
        if turn == 0 and check[0] == True:
            player = Blobk.blobkLine_0
            print("0번 플레이어의 차례입니다!")
        elif turn == 1 and check[1] == True:
            player = Blobk.blobkLine_1
            print("1번 플레이어의 차례입니다!")
        elif turn == 2 and check[2] == True:
            player = Blobk.blobkLine_2
            print("2번 플레이어의 차례입니다!")
        elif turn == 3 and check[3] == True:
            player = Blobk.blobkLine_3
            print("3번 플레이어의 차례입니다!")

        addBlock(player, Block.blockleft)

        while True:
            print("블럭을 맞출 상대 플레이어를 선택합니다...")
            while True:
                opponent = Game.pickPlayer(turn)
                if opponent == 0:
                    opponent = Blobk.blobkLine_0
                    break
                elif opponent == 1:
                    opponent = Blobk.blobkLine_1
                    break
                elif opponent == 2:
                    opponent = Blobk.blobkLine_2
                    break
                elif opponent == 3:
                    opponent = Blobk.blobkLine_3
                    break
                else:
                    print("다시 0에서 3까지 중에서 올바른 값을 입력해주세요.")

            Block.showBlock(player)
            Block.showBlockOppo(opponent)

            expected = {"num": 0, "idx": 0}
            expected["idx"] = int(input("왼쪽에서 몇 번째 블럭을 맞출지 입력하세요: ")) - 1
            expected["num"] = int(input("해당 블럭의 숫자가 무엇일지 맞추세요: "))

            result = Game.checkBlock(expected, opponent)
            if result == 'Y':
                print("상대방 플레이어의 블럭을 맞추셨습니다!")
                result = Game.checkBlock()
                if result == True:
                    break
                else:
                    pass
            elif result == 'N1':
                print("틀렸으므로, 본인이 이번 턴에 가져온 블럭을 오픈합니다.")
                #
                pass
            else:
                pass
