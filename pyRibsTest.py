import numpy as np

from ribs.archives import GridArchive
from ribs.emitters import EvolutionStrategyEmitter
from ribs.schedulers import Scheduler

import matplotlib.pyplot as plt
from ribs.visualize import grid_archive_heatmap

archive = GridArchive(
    solution_dim=10,
    dims=[20, 20],
    ranges=[(-1, 1), (-1, 1)],
)
emitters = [
    EvolutionStrategyEmitter(
        archive,
        x0=[0.0] * 10,
        sigma0=0.1,
    ) for _ in range(3)
]
scheduler = Scheduler(archive, emitters)

for itr in range(1000):
    solutions = scheduler.ask()

    # Optimize the 10D negative Sphere function.
    objective_batch = -np.sum(np.square(solutions), axis=1)

    # Measures: first 2 coordinates of each 10D solution.
    measures_batch = solutions[:, :2]

    scheduler.tell(objective_batch, measures_batch)



grid_archive_heatmap(archive)
plt.show()