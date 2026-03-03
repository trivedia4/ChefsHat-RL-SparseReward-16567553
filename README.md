

**Student ID:** 16567553
**Module:** 7043SCN – Generative AI and Reinforcement Learning
**Assignment:** Task 2 – Reinforcement Learning
**Variant:** Sparse / Delayed Reward (ID % 7 = 2)

---

## 1. Environment Overview

Chef’s Hat Gym is a competitive, multi-agent, turn-based card game environment. It includes:

* Multi-agent interaction
* Large discrete action space
* Delayed and sparse match rewards
* Non-stationary dynamics due to multiple agents

The environment is Gym-compatible and designed for reinforcement learning experimentation.

---

## 2. Variant Focus – Sparse / Delayed Reward

This project focuses on the Sparse / Delayed Reward variant (ID mod 7 = 2).

In Chef’s Hat, meaningful reward signals are primarily given at match termination. This creates a **credit assignment problem**, where it becomes difficult for the agent to associate earlier actions with final outcomes.

The objective of this project is to investigate whether **reward shaping** can reduce reward sparsity and improve learning behaviour.

---

## 3. Algorithm Selection and Justification

A **Deep Q-Network (DQN)** was selected because:

* The action space is discrete and high-dimensional.
* Neural networks approximate Q-values efficiently.
* Experience replay improves training stability.
* A target network reduces oscillations.
* The dueling architecture separates state-value and advantage estimation.

DQN is therefore suitable for delayed reward competitive environments such as Chef’s Hat.

---

## 4. Experimental Design

Two controlled experiments were conducted:

### Experiment 1 – Original Delayed Reward

* 100 training matches
* 100 testing matches
* Standard reward structure (primarily terminal reward)

### Experiment 2 – Reward Shaping

To reduce sparsity, reward shaping was introduced:

* Terminal rewards amplified (×2)
* Intermediate rewards scaled (×0.2)

The purpose was to provide additional learning signal during match progression and improve credit assignment.

---

## 5. Results

| Setup           | Win Rate |
| --------------- | -------- |
| Original Reward | 22%      |
| Shaped Reward   | 14%      |

---

## 6. Analysis and Critical Discussion

The reward-shaped model did not outperform the original delayed reward model under limited training episodes.

Possible explanations include:

* Intermediate reward scaling may have diluted the importance of terminal reward.
* Only 100 training matches may be insufficient for convergence.
* Stochastic behaviour from random opponents introduces learning noise.
* Reward coefficients were not optimised.

This demonstrates that reward shaping is sensitive to scaling and may not universally improve performance in sparse environments.

The experiment highlights the complexity of reward design and the challenges associated with delayed credit assignment in reinforcement learning.

---

## 7. Limitations

* Limited training duration (100 matches)
* No hyperparameter optimisation
* Evaluation only against random opponents
* No self-play or advanced opponent modelling

Future work could explore:

* Double DQN
* PPO or Actor-Critic methods
* Extended training duration
* Adaptive reward scaling strategies

---

## 8. Reproducibility

To reproduce this experiment:

```bash
git clone https://github.com/YOUR_USERNAME/ChefsHat-RL-SparseReward-16567553
```

Open the notebook in Google Colab with GPU enabled and run all cells sequentially.



## 9. Video Viva

Task 2 Viva Video:
PASTE_YOUR_VIDEO_LINK_HERE



## 10. AI Use Declaration

This assignment is categorised as Amber for AI use.

ChatGPT was used to:

* Assist in structuring code experiments
* Clarify reinforcement learning concepts
* Improve documentation structure

All code implementation decisions were reviewed, modified, tested, and validated manually. All experimental results were generated independently by running the environment in Google Colab.


