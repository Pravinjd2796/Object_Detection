import json
import os

def save_results(results, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    with open(os.path.join(output_folder, 'detections.json'), 'w') as f:
        json.dump(results, f)

def load_results(input_folder):
    with open(os.path.join(input_folder, 'detections.json'), 'r') as f:
        results = json.load(f)
    return results


