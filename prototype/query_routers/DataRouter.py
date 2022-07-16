class DataRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'prototype_app'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read prototype_app models go to data_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'data_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write prototype_app models go to data_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'data_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the prototype_app app is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the prototype_app app only appears in the
        'data_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'data_db'
        return None