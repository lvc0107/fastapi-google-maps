import sys
from pathlib import Path

# Ensure the images_project package is importable when running tests from the repo root
ROOT = Path(__file__).resolve().parents[1]
IMAGES_PROJECT = ROOT / "images_project"
if str(IMAGES_PROJECT) not in sys.path:
    sys.path.insert(0, str(IMAGES_PROJECT))
