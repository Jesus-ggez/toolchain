#~>
from .snippet.prelude import SnippetManager


call: SnippetManager = SnippetManager()
data: dict = {
    'snippet': {
        'new': call.start
    }
}
