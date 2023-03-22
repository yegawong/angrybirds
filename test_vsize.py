import angrybirds
import gym
import traceback
import subprocess
from angrybirds.lib import logger
from angrybirds.plugins.game.firecontroller.fc import FireControl


def main():
    env = gym.make('Slingshot-v0', log_level=logger.INFO)
    cmd = "ps -eo vsize,args | grep 'fcsystem 1 2 0' | grep -v 'grep' | awk '{print $1/1024 \" MB\\t\\t\" $11}'"
    fc = FireControl()
    ac1 = env.coder.generate_aiiputdata()
    ac2 = env.coder.generate_aiiputdata()
    ac1 = fc.execute(1, ac1)
    ac2 = fc.execute(2, ac2)
    ac1.siPlaneControl.fCmdHeadingDeg = 0
    ac1.siPlaneControl.fCmdSpd = 0.8
    ac2.siPlaneControl.fCmdHeadingDeg = 180
    ac2.siPlaneControl.fCmdSpd = 0.8
    actions = [ac1, ac2]
    try:
        for i in range(20):
            obs = env.reset()
            while True:
                obs = env.step(actions)
                if obs[0].sOtherInfo.bOver or obs[1].sOtherInfo.bOver:
                    break
            status, output = subprocess.getstatusoutput(cmd)
            print(i, 'Memory', output)
    except Exception:
        print("got exception:", traceback.format_exc())
    finally:
        print("env close")
        env.close()


if __name__ == '__main__':
    main()
