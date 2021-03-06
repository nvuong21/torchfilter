"""Reference implementations for training state estimators with learnable parameters.

These are written with a custom [model
manager](https://brentyi.github.io/fannypack/utils/experiment_management/) for
brevity, but can be easily translated to raw PyTorch.
"""

from ._train_dynamics import train_dynamics_recurrent, train_dynamics_single_step
from ._train_filter import train_filter
from ._train_kalman_filter_measurement import train_kalman_filter_measurement
from ._train_particle_filter_measurement import train_particle_filter_measurement
from ._train_virtual_sensor import train_virtual_sensor

__all__ = [
    "train_dynamics_recurrent",
    "train_dynamics_single_step",
    "train_kalman_filter_measurement",
    "train_filter",
    "train_particle_filter_measurement",
    "train_virtual_sensor",
]
