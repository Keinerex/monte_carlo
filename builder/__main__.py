import argparse
import os.path
from pathlib import Path

import PyInstaller.__main__

BASE_DIR = Path(__file__).resolve().parent.parent

project_root = os.path.join(BASE_DIR, "src\main.py")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--icon", type=Path, help="path to icon")
    p = parser.parse_args()

    arguments = [
        project_root,
        "--windowed",
        "--onefile",
    ]

    if p.icon:
        arguments.append(f"--icon={p.icon.absolute()}")

    PyInstaller.__main__.run(arguments)


if __name__ == "__main__":
    main()
