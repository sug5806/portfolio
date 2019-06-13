import random

class MasterSlaveRouter:
    def db_for_read(self, model, **hints):
        return random.choice(['read1'], )

    def db_for_write(self, model, **hints):
        # return None 과 똑같음
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('default', 'read1')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_relation(self, db, app_label, model_name=None, **hints):
        return True