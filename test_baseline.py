import angrybirds
import gym
import traceback
from angrybirds.lib import logger
from angrybirds.plugins.game.firecontroller.fc import FireControl


def main():
    env = gym.make('BaselineEnv-v0', log_level=logger.INFO, select_side='RED')
    try:
        obs, reward, done, info = env.reset()
        print(obs[0].AATargetDataListNum, "%.2f" % (obs[0].sFighterPara.dLongtitude_rad),
              "%.2f" % (obs[0].sFighterPara.dLatitude_rad))
        print(obs[1].AATargetDataListNum, obs[1].sFighterPara.dLongtitude_rad,
              obs[1].sFighterPara.dLatitude_rad)
        while True:
            fc = FireControl()
            ac1 = env.coder.generate_aiiputdata()
            ac2 = env.coder.generate_aiiputdata()
            ac1 = fc.execute(1, ac1)
            ac2 = fc.execute(2, ac2)
            ac1.siPlaneControl.fCmdHeadingDeg = 0
            ac1.siPlaneControl.fCmdSpd = 0.8
            ac2.siPlaneControl.fCmdHeadingDeg = 180
            ac2.siPlaneControl.fCmdSpd = 0.8
            actions = ac1
            obs, reward, done, info = env.step(actions)
            print("\rstep: {}                   ".format(env.step_num), end='')
            # print(obs[0].AATargetDataListNum, "%.2f"%(obs[0].sFighterPara.dLongtitude_rad*57.324), "%.2f"%(obs[0].sFighterPara.dLatitude_rad*57.324))
            # print(obs[1].AATargetDataListNum, obs[1].sFighterPara.dLongtitude_rad, obs[1].sFighterPara.dLatitude_rad)
            if done:
                print('step done')
                print(obs[0].sOtherInfo.nEndReason, obs[1].sOtherInfo.nEndReason)
                print('step done test')
                obs, reward, done, info = env.step(actions)
                print(obs[0].sOtherInfo.nEndReason, obs[1].sOtherInfo.nEndReason)
                break
            if info['crash'] is True:
                break
        obs, reward, done, info = env.reset()
        print(obs[0].AATargetDataListNum, "%.2f" % (obs[0].sFighterPara.dLongtitude_rad),
              "%.2f" % (obs[0].sFighterPara.dLatitude_rad))
        print(obs[1].AATargetDataListNum, obs[1].sFighterPara.dLongtitude_rad,
              obs[1].sFighterPara.dLatitude_rad)
        while True:
            fc = FireControl()
            ac1 = env.coder.generate_aiiputdata()
            ac2 = env.coder.generate_aiiputdata()
            ac1 = fc.execute(1, ac1)
            ac2 = fc.execute(2, ac2)
            ac1.siPlaneControl.fCmdHeadingDeg = 0
            ac1.siPlaneControl.fCmdSpd = 0.8
            ac2.siPlaneControl.fCmdHeadingDeg = 180
            ac2.siPlaneControl.fCmdSpd = 0.8
            actions = ac1
            obs, reward, done, info = env.step(actions)
            print("\rstep: {}                   ".format(env.step_num), end='')
            # print(obs[0].AATargetDataListNum, "%.2f"%(obs[0].sFighterPara.dLongtitude_rad*57.324), "%.2f"%(obs[0].sFighterPara.dLatitude_rad*57.324))
            # print(obs[1].AATargetDataListNum, obs[1].sFighterPara.dLongtitude_rad, obs[1].sFighterPara.dLatitude_rad)
            if done:
                print('step done')
                print(obs[0].sOtherInfo.nEndReason, obs[1].sOtherInfo.nEndReason)
                print('step done test')
                obs, reward, done, info = env.step(actions)
                print(obs[0].sOtherInfo.nEndReason, obs[1].sOtherInfo.nEndReason)
                break
            if info['crash'] is True:
                break
    except Exception:
        print("got exception:", traceback.format_exc())
    finally:
        env.close()


if __name__ == '__main__':
    main()
