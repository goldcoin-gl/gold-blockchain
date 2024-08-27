from __future__ import annotations

import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("GOLD_ROOT", "~/.gold/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("GOLD_KEYS_ROOT", "~/.gold_keys"))).resolve()

SIMULATOR_ROOT_PATH = Path(os.path.expanduser(os.getenv("GOLD_SIMULATOR_ROOT", "~/.gold/simulator"))).resolve()
