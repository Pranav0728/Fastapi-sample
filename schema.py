def individual_serial(item)->dict:
    return{
        'id': str(item["_id"]),
        'todo': item['todo'],
    }

def list_serial(items)->list:
    return [individual_serial(item) for item in items]
