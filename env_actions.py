from dotenv import load_dotenv
from typing import Any
import os


#~>
from src.core.errors import safe_exec


#<·
load_dotenv()


@safe_exec
def use_test_env() -> Any:
    test_mode: str = os.getenv('test', 'false').lower()

    if test_mode == 'false':
        return

    snippet_url: str = os.getenv('snippet_database_url', '')
    project_url: str = os.getenv('project_database_url', '')

    sqlito: str = 'sqlite://'

    snippet_db: str = snippet_url.removeprefix(sqlito)
    project_db: str = project_url.removeprefix(sqlito)

    for db_path in (snippet_db, project_db):
        ctt_path: str = os.path.expandvars(db_path)

        res = os.path.exists(ctt_path)

        if res:
            os.remove(db_path)
