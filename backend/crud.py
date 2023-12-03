from peewee import *
from models import db, Sight
from playhouse.shortcuts import model_to_dict, update_model_from_dict

def createResponce(status: bool, data):
    return {
        'status': status,
        'data': data,
    }

def model_crud(model: Sight):
    def create(data):
        db.connect()
        instance = model.create(**data)
        db.close()
        return createResponce(True, model_to_dict(instance))

    def read(id):
        db.connect()
        instance = model.get_or_none(model.id == id)
        db.close()
        if instance == None:
            return createResponce(False, 'Not found. Nothing to read.')
        return createResponce(True, model_to_dict(instance))
    
    def read_all():
        instances = list(map(model_to_dict, model.select()))
        return createResponce(True, instances)
    
    def update(id, data):
        db.connect()
        instance = model.get_or_none(model.id == id)
        if instance == None:
            db.close()
            return createResponce(False, 'Not found. Nothing to update.')
        update_model_from_dict(instance, data)
        instance.save()
        db.close()
        return createResponce(True, model_to_dict(instance))
    
    def delete(id):
        db.connect()
        instance = model.get_or_none(model.id == id)
        if instance == None:
            db.close()
            return createResponce(False, 'Not found. Nothing to delete.')
        instance.delete_instance()
        db.close()
        return createResponce(True, 'Successfully deleted.')
    
    return {
        'create': create,
        'read': read,
        'read_all': read_all,
        'update': update,
        'delete': delete
    }