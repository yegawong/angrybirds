class Action:

    def __init__(self):
        self.iCmdID = 0
        self.bApplyNow = 0
        self.iVelType = 0
        self.fCmdNy = 0
        self.fCmdSpd = 0
        self.fCmdAlt = 0
        self.fCmdPitchDeg = 0
        self.fCmdRollDeg = 0
        self.iTurnDirection = 0
        self.fCmdHeadingDeg = 0
        self.fCmdDeltaHeading = 0
        self.fTime = 0
        self.fCmdThrust = 0
        self.fThrustLimit = 120

    def reset(self):
        self.__init__()


class FireControl:

    def __init__(self):
        # 机动号对应的动作方法
        self.control_func = {
            1: self.level_flight,  # 匀速平飞
            2: self.level_flight_accelerate,  # 平飞加减速
            3: self.quickest_climb,  # 最速爬升
            4: self.accelerate_climb,  # 等航迹角爬升
            5: self.level_turn,  # 水平转弯
            6: self.stable_turn,  # 稳定转弯
            7: self.dive,  # 俯冲
            8: self.beam,  # 横切
            9: self.split_s,  # 破S/半滚倒转
            10: self.jindou,  # 斜筋斗
            11: self.crank,  # 偏置
            12: self.turn_in,  # 转入
            13: self.xiangxiajindou,  # 向下斜筋斗
            14: self.abort,  # 中断
            15: self.snake,  # S型机动
            16: self.cata,  # 拦射
            17: self.kuaizhuan,  # 快转
            18: self.projection,  # 抛射
            19: self.crank_dive,  # 偏置俯冲
        }
        self.action = Action()

    def execute(self, iCmdID, ac):
        self.action.reset()
        func = self.control_func.get(iCmdID)
        func()
        ac.siPlaneControl.iCmdID = self.action.iCmdID
        ac.siPlaneControl.bApplyNow = self.action.bApplyNow
        ac.siPlaneControl.iVelType = self.action.iVelType
        ac.siPlaneControl.fCmdNy = self.action.fCmdNy
        ac.siPlaneControl.fCmdSpd = self.action.fCmdSpd
        ac.siPlaneControl.fCmdAlt = self.action.fCmdAlt
        ac.siPlaneControl.fCmdPitchDeg = self.action.fCmdPitchDeg
        ac.siPlaneControl.fCmdRollDeg = self.action.fCmdRollDeg
        ac.siPlaneControl.iTurnDirection = self.action.iTurnDirection
        ac.siPlaneControl.fCmdHeadingDeg = self.action.fCmdHeadingDeg
        ac.siPlaneControl.fCmdDeltaHeading = self.action.fCmdDeltaHeading
        ac.siPlaneControl.fTime = self.action.fTime
        ac.siPlaneControl.fCmdThrust = self.action.fCmdThrust
        ac.siPlaneControl.fThrustLimit = self.action.fThrustLimit
        return ac

    def level_flight(self):
        self.action.iCmdID = 1
        self.action.iVelType = 0
        self.action.fCmdSpd = 0
        self.action.fCmdHeadingDeg = -500
        self.action.fCmdThrust = 120

    def level_flight_accelerate(self):
        self.action.iCmdID = 2
        self.action.iVelType = 0
        self.action.fCmdSpd = 1.4
        self.action.fCmdHeadingDeg = -500
        self.action.fCmdThrust = 120

    def quickest_climb(self):
        self.action.iCmdID = 3
        self.action.fCmdHeadingDeg = -500
        self.action.fCmdThrust = 120

    def accelerate_climb(self):
        self.action.iCmdID = 4
        self.action.fCmdHeadingDeg = -500
        self.action.fCmdPitchDeg = 20
        self.action.iVelType = 2
        self.action.fCmdSpd = 650
        self.action.fCmdThrust = 120

    def level_turn(self):
        self.action.iCmdID = 5
        self.action.fCmdHeadingDeg = 90
        self.action.fCmdThrust = 120
        self.action.fCmdNy = 5

    def stable_turn(self):
        self.action.iCmdID = 6
        self.action.fCmdHeadingDeg = 90
        self.action.fCmdNy = 3
        self.action.iVelType = 0
        self.action.fCmdSpd = 1
        self.action.fCmdThrust = 120

    def dive(self):
        self.action.iCmdID = 7
        self.action.fCmdHeadingDeg = -500
        self.action.iVelType = 0
        self.action.fCmdSpd = 0
        self.action.fCmdPitchDeg = -30
        self.action.fCmdAlt = 5000
        self.action.fCmdThrust = 70

    def beam(self):
        self.action.iCmdID = 8
        self.action.fCmdHeadingDeg = 90
        self.action.fCmdThrust = 120
        self.action.fCmdNy = 5
        self.action.iVelType = 0
        self.action.fCmdSpd = 1

    def split_s(self):
        self.action.iCmdID = 9
        self.action.fCmdHeadingDeg = 90
        self.action.fCmdThrust = 120
        self.action.fCmdNy = 8
        self.action.iVelType = 2
        self.action.fCmdSpd = 650
        self.action.fCmdRollDeg = 180

    def jindou(self):
        self.action.iCmdID = 10
        self.action.fCmdThrust = 120
        self.action.fCmdHeadingDeg = 180
        self.action.fCmdNy = 3
        self.action.fCmdRollDeg = 50

    def crank(self):
        self.action.iCmdID = 11
        self.action.fCmdHeadingDeg = 60
        self.action.fCmdThrust = 120
        self.action.fCmdNy = 3
        self.action.iVelType = 0
        self.action.fCmdSpd = 0.6

    def turn_in(self):
        self.action.iCmdID = 12
        self.action.fCmdHeadingDeg = 90
        self.action.fCmdThrust = 120
        self.action.fCmdNy = 3
        self.action.iVelType = 0
        self.action.fCmdSpd = 1

    def xiangxiajindou(self):
        self.action.iCmdID = 13
        self.action.fCmdThrust = 120
        self.action.fCmdHeadingDeg = 0
        self.action.fCmdNy = 3
        self.action.fCmdRollDeg = 60

    def abort(self):
        self.action.iCmdID = 14
        self.action.fCmdHeadingDeg = 180
        self.action.fCmdThrust = 120
        self.action.fCmdNy = 6
        self.action.fCmdPitchDeg = -20
        self.action.fCmdRollDeg = 135

    def snake(self):
        self.action.iCmdID = 15
        self.action.fCmdHeadingDeg = 0
        self.action.fCmdThrust = 120
        self.action.fCmdNy = 4
        self.action.fCmdDeltaHeading = 50
        self.action.fTime = 10

    def cata(self):
        self.action.iCmdID = 16
        self.action.fCmdHeadingDeg = 0
        self.action.fCmdThrust = 120
        self.action.fCmdPitchDeg = 7
        self.action.iVelType = 0
        self.action.fCmdSpd = 1.2

    def kuaizhuan(self):
        self.action.iCmdID = 17
        self.action.fCmdHeadingDeg = 0
        self.action.fCmdThrust = 120
        self.action.fCmdNy = 6
        self.action.fCmdRollDeg = 60

    def projection(self):
        self.action.iCmdID = 18
        self.action.fCmdHeadingDeg = 0
        self.action.fCmdThrust = 120
        self.action.fCmdNy = 6
        self.action.fCmdPitchDeg = 90

    def crank_dive(self):
        self.action.iCmdID = 19
        self.action.fCmdHeadingDeg = 60
        self.action.fCmdThrust = 120
        self.action.iVelType = 0
        self.action.fCmdSpd = 0.6
        self.action.fCmdNy = 3
        self.action.fCmdPitchDeg = 60
