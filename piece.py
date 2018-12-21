import Dmove
dm = Dmove

class piece:
    mcount = 0          # mcount는 최단거리를 의미한다. 이 거리를 함수를 통해 다른 말로 변신할수 있는 경우를 포함하여 재계산된다.
    dmcount = 0         # dmcount는 변신하지 않고 도착위치까지 바로 가는 거리이다.
    type=0              # type은 말의 타입을 저장한다.
    def make_piece(self, stype, sx, sy, ex,ey):
        type = stype
        if type==2:                             # type이 2라면 말은 폰이 되고, 폰 이동 함수를 사용한다.
            dmcount = dm.Dmove_2(sx, sy, ex, ey)
        elif type==3:                             # type이 3라면 말은 나이트가 되고, 나이트 이동 함수를 사용한다.
            dmcount = dm.Dmove_3(sx, sy, ex, ey)
        elif type==4:                             # type이 4라면 말은 비숍이 되고, 비숍 이동 함수를 사용한다.
            dmcount = dm.Dmove_4(sx, sy, ex, ey)
        elif type==5:                             # type이 5라면 말은 룩이 되고, 룩 이동 함수를 사용한다.
            dmcount = dm.Dmove_5(sx, sy, ex, ey)
        elif type==6:                             # type이 6라면 말은 퀸이 되고, 퀸 이동 함수를 사용한다.
            dmcount = dm.Dmove_6(sx, sy, ex, ey)
        elif type==7:                             # type이 2라면 말은 킹이 되고, 킹 이동 함수를 사용한다.
            dmcount = dm.Dmove_7(sx, sy, ex, ey)
        self.dmcount = dmcount
        self.mcount = dmcount                       # 처음 말을 만드는 make_piece 선언 시에는 mcount가 dmcount와 동일하게 설정한다.
        self.type = stype