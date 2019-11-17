import argparse
import numpy as np
from smac.env import StarCraft2Env


# import whatever you need to defined and load your trained model

def test_model(model, env, num_runs=50):
    """
    :param model:
    :param env:
    :param num_runs:
    :return:
    """
    wins = []
    for i in range(num_runs):
        ############### you can design your test routines on here. ###############

        # A routine of yours to infer the action(s) from the state or observation
        # actions = model(state)

        ##########################################################################

        reward, terminated, info = env.step(actions)

        if terminated:
            win = True if info['battle_won'] else False
        wins.append(float(win))

    return np.average(wins)


def load_model(model_path):
    """
    :param model_path:
    :return: the loaded model (an instance of torch.nn.Module expected)
    """

    """
    do whatever you want to load model. 
    In the end of this code block, we expect to get loaded_model = model
    """

    return loaded_model


def main(model_path):
    env = StarCraft2Env(map_name="8m",
                        window_size_x=1920 / 3,
                        window_size_y=1080 / 3)

    loaded_model = load_model(model_path)
    mean_wr = test_model(load_model, env, num_runs=50)
    return mean_wr


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, help='path to your model')
    args = parser.parse_args()
    mean_wr = main(args.path)

    print("Your average winning rate is {}".format(mean_wr))
