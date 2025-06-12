#~>
from .prelude import SnippetManager

#<·
data: dict = {
    'start': SnippetManager.start,
    'new': SnippetManager.new,
    'use': SnippetManager.use,
    'list': SnippetManager.list_all,
    # 'del': SnippetManager.discard,
}
