from fastapi import APIRouter

from models.doc import Doc
from config.db import client
from schemas.doc import docEntity, docsEntity

router = APIRouter()
db = client.doc

@router.get('/api/docs')
async def find_all_docs():
  return docsEntity(db.docs.find())

@router.post('/api/create-doc')
async def create_doc(doc: Doc):
  new_doc_id = db.docs.insert_one(dict(doc)).inserted_id
  return {
    "success": True,
    "new_doc_id": str(new_doc_id)
  }