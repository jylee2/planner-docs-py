# Serializer
def docEntity(item) -> dict:
  return {
    "id": str(item["_id"]),
    "title": item["title"],
    "body": item["body"]
  }

def docsEntity(entity) -> list:
  return [docEntity(item) for item in entity]