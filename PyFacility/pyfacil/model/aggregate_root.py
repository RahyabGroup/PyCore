from pyutil.method_call.async_call.celery.celery_task import celery_task

__author__ = 'H.Rouhani'


class AggregateRoot:
    _id = None

    def create_async(self):
        yield from self.writer.create_async(self)

    @celery_task
    def create(self):
        self.writer.create(self)

    def edit_async(self):
        yield from self.writer.update_async(self)

    @celery_task
    def edit(self):
        self.writer.update(self)

    @classmethod
    def get_by_id_async(cls, id):
        return (yield from cls.reader.get_by_id_async(id))

    @classmethod
    def get_by_id(cls, id):
        return cls.reader.get_by_id(id)

    @classmethod
    def id_exists_async(cls, id):
        return (yield from cls.reader.exist_id_async(id))

    @classmethod
    def id_exists(cls, id):
        return cls.reader.exist_id(id)
