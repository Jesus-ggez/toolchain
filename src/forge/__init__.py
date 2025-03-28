#~>
from .snippet.prelude import SnippetManager


call: SnippetManager = SnippetManager()
data: dict = {
    'snippet': {
        'start': call.start,
        'new': call.new,
        'use': call.use,
    }
}
