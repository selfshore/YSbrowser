"""Run: python offline_trajectory.py --output trajectory.json"""
import argparse
import json
from dataclasses import asdict
from pathlib import Path
from ysbrowser_sdk.sync_api import TrajectoryModel, MotionRequest

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='trajectory.json')
    args = parser.parse_args()
    model = TrajectoryModel()
    plan = model.generate(
        MotionRequest(start=(100, 100), end=(600, 350), target_size=(80, 40), duration_s=0.8, seed=42),
        viewport=(1280, 720),
    )
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(asdict(plan), ensure_ascii=False, indent=2), encoding='utf-8')
    print(target.resolve())

if __name__ == '__main__':
    main()
