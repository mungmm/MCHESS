import Dmove
import piece

dm = Dmove
piec = piece

def CreatZone(zone, text):                  # CreatZone 함수는 배열을 입력받고, 그 배열에 요소를 추가한다.
    for i in range(0,len(board)):
        if board[i].find(text)!=(-1):           # 입력받은 text가 있는지 줄(행)별로 검색한다. 없다면 다음줄로 넘어간다.
            for j in range(0,len(board[i])):    # 입력받은 text가 해당 줄에 있다면, 몇번째에 있는지(열) 검색한다.
                if board[i][j]==text:           # 찾은 위치를 통해 x값과 y값을 알아낸다.
                    zone.append([0,j,i])                # 0번 : piece클래스(0으로 입력해둔다), 1번 : 위치 x값, 2번 : 위치 y값

def MakePiece(z, type):                     # MakePiece는 CreatZone에서 추가한 요소의 0번항목을 piece클래스로 만들어준다.
    for i in range(0,len(z)):               # piece클래스의 make_piece함수를 통해 위치값과 타입을 입력하고, mcount와 dmcount를 계산한다
        z[i][0] = piec.piece()
        z[i][0].make_piece(type, z[i][1], z[i][2], ex, ey)

def AdjustMcount(n1, n2, bn):               # AdjustMcount 함수는 배열요소(말)이 다른 배열요소(말)을 경유했을 시 최단거리가 짧아지는지 계산하고,
    for nm in range(3,bn):                  # 거리가 짧아진다면 최단거리를 수정한다.
        for i in range(0, len(n1)):         # 최단거리 = 다른말 까지의 최단거리 + 다른말의 (도착위치까지의) 최단거리
            if n1[i][0].mcount==nm:         # <- 최단거리가 짧은 함수 먼저 계산한다
                for j in range(0, len(n2)):
                    if n1[i][0].mcount > n2[j][0].mcount+1:
                        if i+2==2:
                            tmcount = dm.Dmove_2(n1[i][1],n1[i][2],n2[j][1],n2[j][2]) + n2[j][0].mcount
                        elif i+2==3:
                            tmcount = dm.Dmove_3(n1[i][1],n1[i][2],n2[j][1],n2[j][2]) + n2[j][0].mcount
                        elif i+2==4:
                            tmcount = dm.Dmove_4(n1[i][1],n1[i][2],n2[j][1],n2[j][2]) + n2[j][0].mcount
                        elif i+2==5:
                            tmcount = dm.Dmove_5(n1[i][1],n1[i][2],n2[j][1],n2[j][2]) + n2[j][0].mcount
                        elif i+2==6:
                            tmcount = dm.Dmove_6(n1[i][1],n1[i][2],n2[j][1],n2[j][2]) + n2[j][0].mcount
                        elif i+2==7:
                            tmcount = dm.Dmove_7(n1[i][1],n1[i][2],n2[j][1],n2[j][2]) + n2[j][0].mcount
                        if tmcount<n1[i][0].mcount:
                            n1[i][0].mcount = tmcount

if __name__ == '__main__':
    board = []                                              # board는 2차배열로, 체스판 입력내용을 저장함
    count1 = 0; count9 = 0                                  # count1과 count9은 각각 시작위치, 도착위치에 오류가 있는지 검토
    z2 = []; z3 = []; z4 = []; z5 = []; z6 = []; z7 = []    # 변신가능한 말들의 위치를 저장하는 배열
    z = [z2, z3, z4, z5, z6, z7]
    sx=0; sy=0; ex=0; ey=0                                  # sx,sy는 시작위치, ex,ey는 도착위치
    print("먼저, 체스판의 크기를 입력하세요. 입력값 만큼의 길이를 갖는 정사각형이 됩니다.(최대 99)")
    boardN = input()                    # 체스판은 N X N 크기이다. 이때 N을 사용자에게 입력받는다.
    print("체스판을 입력하세요.")     # 체스판에 대한 설명 출력
    print("0 : 빈칸")
    print("1 : 시작위치")
    print("2 : 폰(남쪽으로 한칸 이동가능)")
    print("3 : 나이트(동서남북 한칸 + 대각선방향 한칸 위치로 이동가능)")
    print("4 : 비숍(대각선방향 몇칸이든 이동가능)")
    print("5 : 룩(동서남북 몇칸이든 이동가능)")
    print("6 : 퀸(동서남북 및 대각선방향 몇칸이든 이동가능)")
    print("7 : 킹(인접한 8칸으로 이동가능)")
    print("9 : 도착위치")

    for i in range(0,int(boardN)):                          # N줄(행)만큼 체스판을 입력받는다
        board.append(input())
        if len(board[i])!=int(boardN):                      # 이때, 한줄의 글자수(열)이 N개가 아니라면 오류 반환
            print("%d행의 길이가 잘못되었습니다. 다시 입력해주세요!" %(i+1))

    for i in range(0,len(board)):                       # board 내에 1(시작위치)가 1개가 아니라면 오류 반환
        if board[i].find("1")!=(-1):
            sy=i; sx=board[i].find("1"); count1=count1+1
    if count1!=1:
        print("시작위치가 없거나 많습니다. 다시 입력해주세요!")

    for i in range(0,len(board)):                       # board 내에 9(도착위치)가 1개가 아니라면 오류 반환
        if board[i].find("9")!=(-1):
            ey=i; ex=board[i].find("9"); count9=count9+1
    if count9!=1:
        print("도착위치가 없거나 많습니다. 다시 입력해주세요!")

    CreatZone(z2, "2")      # 체스판에 입력한 말들의 위치를 토대로 배열z에 위치를 입력.
    CreatZone(z3, "3")
    CreatZone(z4, "4")
    CreatZone(z5, "5")
    CreatZone(z6, "6")
    CreatZone(z7, "7")

    for zz in z:            # 각 말들이 도착위치까지 이동하는 데 필요한 이동거리(=최단거리)를 저장한다
        MakePiece(zz, z.index(zz)+2)

    for adjn in range(0,int(boardN)):       # 말들의 최단거리를 수정한다.
        for zz1 in z:                       # 만약, 다른 말의 위치로 가서 변신을 하는 것이 더 최단거리라면,
            for zz2 in z:                   # 최단거리 = 해당 말까지의 최단거리 + 해당 말의 최단위치
                AdjustMcount(zz1, zz2, int(boardN))

    sdmcount = dm.Dmove_7(sx,sy,ex,ey)      # 시작위치에서 도착위치까지 최단거리 저장(변신하지 않고 킹을 이용해 가는경우)

    for n2 in z:                            # 시작위치에서의 최단거리를 수정한다
        for j in range(0,len(n2)):
            if sdmcount > (n2[j][0].mcount + 1):
                tmcount = dm.Dmove_7(sx, sy, n2[j][1], n2[j][2]) + n2[j][0].mcount
                if tmcount < sdmcount:
                    sdmcount = tmcount

    print(sdmcount)                         # 최종 최단거리를 출력한다