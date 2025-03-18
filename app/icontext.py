from app.errors import TreeError


class IContext:
    def move_next_node(self, context: dict, node_name: str) -> None:
        if not (node_name in context['pointer']):
            raise TreeError(f'Invalid name branch: {node_name}')

        context['anterior'] = context['pointer']
        context['pointer'] = context['pointer'][node_name]


    def or_else_node(self, context: dict) -> None:
        raise NotImplementedError('Future impl')


    def call(self, context: dict, node_name: str) -> None:
        self.move_next_node(
            node_name=node_name,
            context=context,
        )
        print('pre call')
        context['pointer']()


    def foo(self): ...
