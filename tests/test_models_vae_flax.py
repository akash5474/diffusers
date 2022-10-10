import os
import unittest

import jax
from diffusers import FlaxAutoencoderKL

from .test_modeling_common_flax import FlaxModelTesterMixin

@unittest.skipIf(os.name != "nt", "jax not supported on windows")
class FlaxAutoencoderKLTests(FlaxModelTesterMixin, unittest.TestCase):
    model_class = FlaxAutoencoderKL

    @property
    def dummy_input(self):
        batch_size = 4
        num_channels = 3
        sizes = (32, 32)

        prng_key = jax.random.PRNGKey(0)
        image = jax.random.uniform(prng_key, ((batch_size, num_channels) + sizes))

        return {"sample": image, "prng_key": prng_key}

    def prepare_init_args_and_inputs_for_common(self):
        init_dict = {
            "block_out_channels": [32, 64],
            "in_channels": 3,
            "out_channels": 3,
            "down_block_types": ["DownEncoderBlock2D", "DownEncoderBlock2D"],
            "up_block_types": ["UpDecoderBlock2D", "UpDecoderBlock2D"],
            "latent_channels": 4,
        }
        inputs_dict = self.dummy_input
        return init_dict, inputs_dict
