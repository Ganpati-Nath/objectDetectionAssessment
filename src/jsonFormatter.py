import json

def format_results_to_json(hierarchy, output_path):
    """
    Formats the hierarchical detection results into a JSON file.

    Args:
        hierarchy (list): The hierarchical object detection results.
        output_path (str): The path to save the formatted JSON file.

    Returns:
        None
    """
    try:
        with open(output_path, "w") as f:
            json.dump(hierarchy, f, indent=4)
        print(f"Formatted JSON saved to {output_path}")
    except IOError as e:
        print(f"Failed to save JSON to {output_path}: {e}")