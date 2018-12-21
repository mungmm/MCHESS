# Dmove 함수
# Direct Move를 의미하며, 시작지점(x,y)부터 도착지점(x,y)까지 가기위한 이동횟수를 반환합니다.

def Dmove_2(sx, sy, ex, ey): # 폰 이동
    if (sx == ex) and (ey > sy):  # 폰은 남쪽 방향으로 1칸씩만 이동 가능
        return ey - sy
    else:  # 폰으로는 도착지점에 갈 수 없는 경우, 9999번 반환
        return 9999

def Dmove_3(sx, sy, ex, ey): # 나이트 이동
    if (abs(ex - sx) == 1 and (ey == sy)) or (abs(ey - sy) == 1 and (ex == sx)):  # 동서남북 1칸 거리인 경우, 3번 이동 필요
        return 3
    elif (abs(ex - sx) == 2 and (ey == sy)) or (abs(ey - sy) == 2 and (ex == sx)):  # 동서남북 2칸 거리인 경우, 2번 이동필요
        return 2
    elif (abs(ex - sx) == 3 and (ey == sy)) or (abs(ey - sy) == 3 and (ex == sx)):  # 동서남북 3칸 거리인 경우, 5번 이동필요
        return 5
    elif (abs(ex - sx) == 4 and (ey == sy)) or (abs(ey - sy) == 4 and (ex == sx)):  # 동서남북 4칸 거리인 경우, 2번 이동필요
        return 2
    elif (abs(ex - sx) == 5 and (ey == sy)) or (abs(ey - sy) == 5 and (ex == sx)):  # 동서남북 5칸 거리인 경우, 3번 이동필요
        return 3
    elif (abs(ex - sx) == 6 and (ey == sy)) or (abs(ey - sy) == 6 and (ex == sx)):  # 동서남북 6칸 거리인 경우, 4번 이동필요
        return 4
    elif (abs(ex - sx) == 7 and (ey == sy)) or (abs(ey - sy) == 7 and (ex == sx)):  # 동서남북 7칸 거리인 경우, 5번 이동필요
        return 5
    elif abs(ex - sx) == 1 and abs(ey - sy) == 1:  # 대각선방향 1칸 거리인 경우, 4번 이동 필요
        return 4
    elif abs(ex - sx) == 2 and abs(ey - sy) == 2:  # 대각선방향 2칸 거리인 경우, 4번 이동 필요
        return 4
    elif abs(ex - sx) == 3 and abs(ey - sy) == 3:  # 대각선방향 3칸 거리인 경우, 2번 이동 필요
        return 2
    elif abs(ex - sx) == 4 and abs(ey - sy) == 4:  # 대각선방향 4칸 거리인 경우, 4번 이동 필요
        return 4
    elif abs(ex - sx) == 5 and abs(ey - sy) == 5:  # 대각선방향 5칸 거리인 경우, 4번 이동 필요
        return 4
    elif (abs(ex - sx) == 1 and abs(ey - sy) == 2) or (
            abs(ey - sy) == 1 and abs(ex - sx) == 2):  # 동서남북 1칸 + 대각선 1칸 거리인 경우, 1번 이동 필요 - ★기본이동
        return 1
    elif (abs(ex - sx) == 1 and abs(ey - sy) == 3) or (
            abs(ey - sy) == 1 and abs(ex - sx) == 3):  # 동서남북 2칸 + 대각선 1칸 거리인 경우, 2번 이동 필요
        return 2
    elif (abs(ex - sx) == 2 and abs(ey - sy) == 3) or (
            abs(ey - sy) == 2 and abs(ex - sx) == 3):  # 동서남북 1칸 + 대각선 2칸 거리인 경우, 3번 이동 필요
        return 3
    elif (abs(ex - sx) == 1 and abs(ey - sy) == 4) or (
            abs(ey - sy) == 1 and abs(ex - sx) == 4):  # 동서남북 3칸 + 대각선 1칸 거리인 경우, 3번 이동 필요
        return 3
    elif (abs(ex - sx) == 2 and abs(ey - sy) == 4) or (
            abs(ey - sy) == 2 and abs(ex - sx) == 4):  # 동서남북 2칸 + 대각선 2칸 거리인 경우, 2번 이동 필요
        return 2
    elif (abs(ex - sx) == 3 and abs(ey - sy) == 4) or (
            abs(ey - sy) == 3 and abs(ex - sx) == 4):  # 동서남북 1칸 + 대각선 3칸 거리인 경우, 3번 이동 필요
        return 3
    elif (abs(ex - sx) == 1 and abs(ey - sy) == 5) or (
            abs(ey - sy) == 1 and abs(ex - sx) == 5):  # 동서남북 4칸 + 대각선 1칸 거리인 경우, 4번 이동 필요
        return 4
    elif (abs(ex - sx) == 2 and abs(ey - sy) == 5) or (
            abs(ey - sy) == 2 and abs(ex - sx) == 5):  # 동서남북 3칸 + 대각선 2칸 거리인 경우, 3번 이동 필요
        return 3
    elif (abs(ex - sx) == 3 and abs(ey - sy) == 5) or (
            abs(ey - sy) == 3 and abs(ex - sx) == 5):  # 동서남북 2칸 + 대각선 3칸 거리인 경우, 4번 이동 필요
        return 4
    elif (abs(ex - sx) == 1 and abs(ey - sy) == 6) or (
            abs(ey - sy) == 1 and abs(ex - sx) == 6):  # 동서남북 5칸 + 대각선 1칸 거리인 경우, 3번 이동 필요
        return 3
    elif (abs(ex - sx) == 2 and abs(ey - sy) == 6) or (
            abs(ey - sy) == 2 and abs(ex - sx) == 6):  # 동서남북 4칸 + 대각선 2칸 거리인 경우, 4번 이동 필요
        return 4
    elif (abs(ex - sx) == 3 and abs(ey - sy) == 6) or (
            abs(ey - sy) == 3 and abs(ex - sx) == 6):  # 동서남북 3칸 + 대각선 3칸 거리인 경우, 3번 이동 필요
        return 3
    elif abs(ex - sx) > 3 and abs(ey - sy) > 3:  # 대각선으로 3칸 거리 이상 떨어진 경우(위의 경우에 해당 안 될 시에만), 반복적으로 거리를 좁힘
        if ex > sx:
            ssx = sx + 3
        else:
            ssx = sx - 3
        if ey > sy:
            ssy = sy + 3
        else:
            ssy = sy - 3
        return 2 + Dmove_3(ssx, ssy, ex, ey)  # 2번 이동 추가, 나이트이동 반복
    elif abs(ex - sx) < 6 and abs(ey - sy) > 7:  # x는 가까우나 y는 먼 경우, y만 반복적으로 거리를 좁힘
        if ey > sy:
            ssy = sy + 4
        else:
            ssy = sy - 4
        return 2 + Dmove_3(sx, ssy, ex, ey)  # 2번 이동 추가, 나이트이동 반복
    elif abs(ey - sy) < 6 and abs(ex - sx) > 7:  # y는 가까우나 x는 먼 경우, y만 반복적으로 거리를 좁힘
        if ex > sx:
            ssx = sx + 4
        else:
            ssx = sx - 4
        return 2 + Dmove_3(ssx,sy,ex,ey) # 2번 이동 추가, 나이트이동 반복
def Dmove_4(sx, sy, ex, ey): # 비숍 이동
    if (abs(ey - sy) == abs(ex - sx)):  # 대각선 방향으로 한번에 갈 수 있는 경우 (x거리와 y거리가 동일)
        return 1
    elif ((abs(ey - sy) + abs(ex - sx)) % 2 == 0):  # 대각선 방향으로 두번에 갈 수 있는 경우
        return 2
    else:  # 비숍으로는 도착지점에 갈 수 없는 경우(다른 대각선상에 있는 경우)
        return 9999

def Dmove_5(sx, sy, ex, ey): # 룩 이동
    if (sx == ex) or (sy == ey):  # 한번에 갈 수 있는 경우(x나 y 둘 중 하나가 동일한 경우)
        return 1
    else:  # 그 외에는 2번만에 도착 가능
        return 2

def Dmove_6( sx, sy, ex, ey):    # 퀸 이동
    if (sx == ex) or (sy == ey) or (abs(ey - sy) == abs(ex - sx)):  # 한번에 갈 수 있는 경우(룩의경우 + 비숍의경우)
        return 1
    else:  # 그 외에는 2번만에 도착 가능
        return 2

def Dmove_7(sx, sy, ex, ey): # 킹 이동
    xx = abs(ex - sx)  # 킹으로 도착지점에 가려면
    yy = abs(ey - sy)  # x거리와 y거리 중 먼 거리만큼 이동해야함
    if xx > yy:
        return xx
    else:
        return yy
