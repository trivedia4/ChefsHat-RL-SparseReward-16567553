
"""
Chef's Hat Gym – Sparse / Delayed Reward Variant
Student ID: 16567553
Module: 7043SCN – Generative AI and Reinforcement Learning

This script compares:
1. Original delayed reward DQN
2. Reward-shaped DQN

Environment: Chef's Hat Gym
"""

import os
import asyncio
import ast
import glob
import pandas as pd
import nest_asyncio

from agents.random_agent import RandomAgent
from agents.agent_dqn import DQNAgent
from rooms.room import Room

nest_asyncio.apply()


async def run_experiment(training: bool,
                         model_path: str,
                         matches: int,
                         output_folder: str,
                         reward_mode: str = "original"):

    room = Room(
        run_remote_room=False,
        room_name="SparseRewardRoom",
        max_matches=matches,
        output_folder=output_folder,
        save_game_dataset=True,
        save_logs_game=False,
        save_logs_room=False,
    )

    # Connect 3 Random baseline agents
    for i in range(3):
        room.connect_player(
            RandomAgent(
                name=f"Random{i}",
                log_directory=room.room_dir,
                verbose_log=False
            )
        )

    # Connect DQN Agent
    agent = DQNAgent(
        name="DQN",
        train=training,
        log_directory=room.room_dir,
        model_path=model_path,
        load_model=not training,
    )

    # Reward shaping logic
    if reward_mode == "shaped":
        original_remember = agent.remember

        def shaped_remember(state, possible_actions, action, reward,
                            next_state, next_possible_actions, done):

            if done:
                reward = reward * 2.0
            else:
                reward = reward * 0.2

            original_remember(state,
                              possible_actions,
                              action,
                              reward,
                              next_state,
                              next_possible_actions,
                              done)

        agent.remember = shaped_remember

    room.connect_player(agent)
    await room.run()


def calculate_winrate(folder: str):

    dataset_path = glob.glob(folder + "/*/dataset/game_dataset.pkl.csv")[0]

    df = pd.read_csv(dataset_path, index_col=0)
    end_matches = df[df["Action_Type"] == "END_MATCH"]

    wins = 0
    total = len(end_matches)

    for s in end_matches["Match_Score"]:
        score_dict = ast.literal_eval(s)

        # Lower score = better ranking in Chef's Hat
        if score_dict["DQN"] == min(score_dict.values()):
            wins += 1

    return total, wins, wins / total


if __name__ == "__main__":

    print("Running Original Reward Experiment...")
    asyncio.run(
        run_experiment(True,
                       "outputs_original/model_original.h5",
                       100,
                       "outputs_original",
                       "original")
    )

    asyncio.run(
        run_experiment(False,
                       "outputs_original/model_original.h5",
                       100,
                       "outputs_original_test",
                       "original")
    )

    print("Running Shaped Reward Experiment...")
    asyncio.run(
        run_experiment(True,
                       "outputs_shaped/model_shaped.h5",
                       100,
                       "outputs_shaped",
                       "shaped")
    )

    asyncio.run(
        run_experiment(False,
                       "outputs_shaped/model_shaped.h5",
                       100,
                       "outputs_shaped_test",
                       "shaped")
    )

    print("\nFinal Results:")

    total_o, wins_o, rate_o = calculate_winrate("outputs_original_test")
    print(f"Original Reward → Win Rate: {rate_o:.2f}")

    total_s, wins_s, rate_s = calculate_winrate("outputs_shaped_test")
    print(f"Shaped Reward → Win Rate: {rate_s:.2f}")
