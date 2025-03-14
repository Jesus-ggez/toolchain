from .struct_context import Context


class Actions:
    def move_node(self, context: Context) -> None:
        _current = context.actual_tpos.get(
            context.timeline_name
        )
        if _current is None:
            raise ValueError(f'Invalid action<MvNode>: {context.current_token}')

        context.before_tpos = _current

