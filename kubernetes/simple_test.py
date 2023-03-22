import os
import ray
import gym
import angrybirds
from angrybirds.plugins.game.firecontroller.fc import FireControl


def make_env():
    isdone = False
    while not isdone:
        try:
            env = gym.make('Slingshot-v0', log_level='INFO')
            isdone = True
        except:
            env.close()
            isdone = False
    return env


@ray.remote(num_cpus=4)
class DataCollector(object):

    def __init__(self):
        self.env = make_env()
        fc = FireControl()
        ac1 = self.env.coder.generate_aiiputdata()
        ac2 = self.env.coder.generate_aiiputdata()
        ac1 = fc.execute(1, ac1)
        ac2 = fc.execute(2, ac2)
        ac1.siPlaneControl.fCmdHeadingDeg = 0
        ac1.siPlaneControl.fCmdSpd = 0.8
        ac2.siPlaneControl.fCmdHeadingDeg = 180
        ac2.siPlaneControl.fCmdSpd = 0.8
        self.actions = [ac1, ac2]

    def collect_data(self, max_ep, max_step):
        data = []
        try:
            for i_episode in range(max_ep):
                state = self.env.reset()
                for t in range(max_step):  # Don't infinite loop while learning
                    state = self.env.step(self.actions)
                    data.append(state)
                    if state[0].sOtherInfo.bOver or state[1].sOtherInfo.bOver:
                        break
        except Exception:
            self.env.close()
            self.env = make_env()
        return data

    def select_action(self, state):
        return self.actions


def main():
    parallel_number = 6  # number = head node num + worker node nume * n
    max_ep = 1
    max_step = 1000
    ray_config = {}
    # ray_host = os.environ.get("RAY_HEAD_SERVICE_HOST", "localhost")
    # ray_port = os.environ.get("RAY_HEAD_SERVICE_PORT", 6379)
    ray_host = '39.99.45.101'   # SLB IP IPV4(public)
    ray_port = 6379
    ray_config["address"] = f"{ray_host}:{ray_port}"

    ray.init(**ray_config)
    data_collectors = [DataCollector.remote() for _ in range(parallel_number)]

    for _ in range(2):
        data_id = [d.collect_data.remote(max_ep=max_ep, max_step=max_step) for d in data_collectors]
        import time
        t0 = time.perf_counter()
        ready_ids, remaining_ids = ray.wait(data_id, num_returns=parallel_number, timeout=60.0)
        t1 = time.perf_counter()
        if len(ready_ids) == len(data_id):
            datas = ray.get(ready_ids)
            step_num = len(datas[0])
        else:
            step_num = 0
            print("not done !!!")
        t2 = time.perf_counter()
        print("parallel number: {} step total:{},{}s,ray get result:{}s".format(
            parallel_number, step_num, str(t1 - t0), str(t2 - t1)))

    # for i in range(1, parallel_number+1):
    #     t_data = data_collectors[0:i]
    #     data_id = [d.collect_data.remote(max_ep=max_ep, max_step=max_step) for d in t_data]
    #     import time
    #     t0 = time.perf_counter()
    #     ready_ids, remaining_ids = ray.wait(data_id, num_returns=i, timeout=480.0)
    #     t1 = time.perf_counter()
    #     if len(ready_ids) == len(data_id):
    #         datas = ray.get(ready_ids)
    #         step_num = len(datas[0])
    #     else:
    #         step_num = 0
    #         print("not done !!!")
    #     t2 = time.perf_counter()
    #     print("parallel number: {} step total:{},{}s,ray get result:{}s".format(
    #         i, step_num, str(t1 - t0), str(t2 - t1)))
    # [print(len(data)) for data in datas]
    ray.shutdown()


if __name__ == '__main__':
    main()
