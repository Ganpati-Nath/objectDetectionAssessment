import cv2

def save_cropped_image(frame, bbox, output_path):
    """
    Saves a cropped portion of the frame specified by the bounding box.

    Args:
        frame (ndarray): The input frame from which the object is cropped.
        bbox (list): Bounding box coordinates [x1, y1, x2, y2].
        output_path (str): Path where the cropped image will be saved.
    """
    x1, y1, x2, y2 = bbox
    if 0 <= x1 < x2 <= frame.shape[1] and 0 <= y1 < y2 <= frame.shape[0]:  # Validate bbox within frame
        cropped_image = frame[y1:y2, x1:x2]
        cv2.imwrite(output_path, cropped_image)
    else:
        print(f"Warning: Invalid bounding box {bbox}. Skipping crop.")

def retrieve_subobject_images(hierarchy, frame, output_dir):
    """
    Retrieves and saves cropped images for all subobjects in the hierarchy.

    Args:
        hierarchy (list): List of objects and their subobjects in hierarchical format.
        frame (ndarray): The input frame from which objects are cropped.
        output_dir (str): Directory to save cropped images.
    """
    for obj in hierarchy:
        parent_label = obj['object']
        parent_id = obj['id']
        for sub in obj.get("subobjects", []):
            sub_bbox = sub['bbox']
            sub_label = f"{parent_label}_{sub['object']}_{parent_id}_{sub['id']}"
            cropped_path = f"{output_dir}/{sub_label}.jpg"
            save_cropped_image(frame, sub_bbox, cropped_path)