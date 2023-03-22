from gym.envs.registration import register

register(
    id='SelfplayEnv-v0',
    entry_point='angrybirds.envs:SelfplayEnv',
    kwargs={'log_level': 'ERROR'},
)

register(
    id='BaselineEnv-v0',
    entry_point='angrybirds.envs:BaselineEnv',
    kwargs={
        'log_level': 'ERROR',
        'select_side': 'BLUE',
        'opponent': 'Nigel'  # Nigel Mauro   @TODO EarlPig
    },
)


def make_fn(env_id):
    import gym
    return lambda: gym.make(env_id)
