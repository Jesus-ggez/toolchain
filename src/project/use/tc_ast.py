from typing import Any


#~>


#<·
class TcAST:
    file_stack: list[str] = []
    last_token: Any = None
    behavior: Any = None
