import os
import sys
import runpy
from pathlib import Path

root = Path(__file__).resolve().parent
environment = root / "miniconda3" / "envs" / "facefusion"
nvidia = environment / "Lib" / "site-packages" / "nvidia"

if not environment.exists():
    raise SystemExit("FaceFusion Python environment not found.")

dll_dirs = [
    str(path / "bin")
    for path in nvidia.iterdir()
    if (path / "bin").is_dir()
]

handles = [os.add_dll_directory(path) for path in dll_dirs]
os.environ["PATH"] = os.pathsep.join(dll_dirs) + os.pathsep + os.environ["PATH"]

import onnxruntime as ort
ort.preload_dlls(directory="")

os.chdir(root)
sys.argv = ["facefusion.py", "run", "--open-browser"]
runpy.run_path(str(root / "facefusion.py"), run_name="__main__")
