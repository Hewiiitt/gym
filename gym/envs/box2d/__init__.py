try:
    import Box2D
    from gym.envs.box2d.lunar_lander import LunarLander
    from gym.envs.box2d.lunar_lander import LunarLanderContinuous
    from gym.envs.box2d.bipedal_walker import BipedalWalker, BipedalWalkerHardcore
    from gym.envs.box2d.car_racing import CarRacing
    from gym.envs.box2d.car_racing_v1 import CarRacingV1
    from gym.envs.box2d.car_racing_v2 import CarRacingV2
    from gym.envs.box2d.car_racing_v3 import CarRacingV3
except ImportError:
    Box2D = None
