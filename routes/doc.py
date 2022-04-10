from fastapi import APIRouter
from bson.objectid import ObjectId

from models.doc import Doc
from config.db import client
from schemas.doc import docEntity, docsEntity

router = APIRouter()
db = client.doc

@router.get('/api/docs')
async def get_docs():
  return docsEntity(db.docs.find())

@router.get('/api/doc/{id}')
async def get_doc(id):
  return docEntity(db.docs.find_one({"_id": ObjectId(id)}))

@router.post('/api/create-doc')
async def create_doc(doc: Doc):
  new_doc_id = db.docs.insert_one(dict(doc)).inserted_id
  return {
    "success": True,
    "new_doc_id": str(new_doc_id)
  }

@router.put('/api/doc/{id}')
async def edit_doc(id, doc: Doc):
  db.docs.find_one_and_update({"_id": ObjectId(id)},{
    "$set": dict(doc)
  })
  return docEntity(db.docs.find_one({"_id": ObjectId(id)}))

@router.delete('/api/doc/{id}')
async def delete_doc(id):
  db.docs.find_one_and_delete({"_id": ObjectId(id)})
  return {
    "success": True
  }