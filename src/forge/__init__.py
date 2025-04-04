#~>
from .snippet.prelude import SnippetManager
from .project.prelude import ProjectManager


call_snippet: SnippetManager = SnippetManager()
call_project: ProjectManager = ProjectManager()


data: dict = {
    'snippet': {
        'start': call_snippet.start,
        'new': call_snippet.new,
        'use': call_snippet.use,
    },
    'project': {
        'start': call_project.start,
        'new': call_project.new,
        'use': call_project.use,
    }
}
