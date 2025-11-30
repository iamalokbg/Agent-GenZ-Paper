import json

def safe_json(data):
    try:
        return json.loads(data)
    except:
        return data

def merge_dicts(a, b):
    merged = a.copy()
    merged.update(b)
    return merged
