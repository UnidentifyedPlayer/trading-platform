class DjangoAppsRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'prototype_app'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read django apps models go to default db.
        """
        if model._meta.app_label not in self.route_app_labels:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write django apps models go to default db.
        """
        if model._meta.app_label not in self.route_app_labels:
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the django apps app is
        involved.
        """
        if (
            obj1._meta.app_label not in self.route_app_labels and
            obj2._meta.app_label not in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the django apps app only appears in the
        default db.
        """
        if app_label not in self.route_app_labels:
            return db == 'default'
        return None