from .posts import Posts
from .user import User, load_user


def get_model_by_tablename(db, table_fullname):
    """Return class reference mapped to table"""
    for c in db.Model._decl_class_registry.values():
        if hasattr(c, '__table__') and c.__table__.fullname == table_fullname:
            return c