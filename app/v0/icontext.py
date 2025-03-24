#~>
from app.errors import TreeError


class IContext:
    def move_next_node(self, context: dict, node_name: str) -> None:
        print(node_name)
        if not (node_name in context['node_pointer']):
            raise TreeError(f'Invalid name branch: {node_name}')

        context['anterior'] = context['node_pointer']
        context['node_pointer'] = context['node_pointer'][node_name]


    def or_else_node(self, context: dict, node_name: str) -> None:
        raise NotImplementedError('Future impl')


    def call(self, context: dict, node_name: str) -> None:
        self.move_next_node(
            node_name=node_name,
            context=context,
        )
        context['node_pointer']()


    def select_call(self, context: dict, argument: str) -> None:
        if not context['args']:
            self.__call_single_arg(
                argument=argument,
                context=context,
            )
            return
        self.__call_with_args(
            context=context,
        )


    def __call_single_arg(self, context: dict, argument: str) -> None:
        self.move_next_node(
            node_name=context['action']['fn'],
            context=context,
        )
        context['node_pointer'](argument)


    def __call_with_args(self, context: dict) -> None:
        self.move_next_node(
            node_name=context['action']['fn'],
            context=context,
        )
        print(context['args'])
        context['node_pointer'](*context['args'])


    def foo(self) -> None: ...
