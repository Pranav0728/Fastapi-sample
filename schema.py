def individual_serial(item)->dict:
    return{
        'id': str(item["_id"]),
        'name': item['name'],
        'description':item['description'],
        'price': str(item['price']) 
    }

def list_serial(items)->list:
    return [individual_serial(item) for item in items]
