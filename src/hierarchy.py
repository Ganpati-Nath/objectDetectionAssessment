def associate_objects(results):
    hierarchy = []
    for obj in results:
        if obj['object'] in ['Car', 'Person']:
            parent_id = obj['id']
            sub_objects = [
                {
                    "object": sub['object'],
                    "id": sub['id'],
                    "bbox": sub['bbox']
                }
                for sub in results if is_subobject(sub, obj)
            ]
            hierarchy.append({
                "object": obj['object'],
                "id": parent_id,
                "bbox": obj['bbox'],
                "subobjects": sub_objects
            })
    return hierarchy

def is_subobject(sub, parent):
    sx1, sy1, sx2, sy2 = sub['bbox']
    px1, py1, px2, py2 = parent['bbox']
    # Check if subobject is within the parent's bounding box
    return (px1 <= sx1 <= px2 and px1 <= sx2 <= px2 and
            py1 <= sy1 <= py2 and py1 <= sy2 <= py2)