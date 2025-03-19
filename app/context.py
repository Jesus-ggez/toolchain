#~>
from app.icontext import IContext
from app.errors import (
    ContextError,
    TokenError,
)


spacer: str = '@'


class CreateContext:
    def __init__(
        self,
        context: dict,
        token: str,
    ) -> None:
        self.__validate(context=context,token=token)

        if self._token == spacer:
            return

        if self.__is_initial():
            return

        if self.__no_action():
            return

        if self.__await_to_call():
            return

        if self.__await_args():
            return

        if self.__is_active_timer():
            return

        self.__exec_action()


    def __tokens(self) -> dict:
        context: IContext = IContext()
        return {
            ':': {
                'exec': context.move_next_node,
                'args': 1,
            },
            '?': {
                'exec': context.or_else_node,
                'args': 0,
            },
            '.': {
                'exec': context.call,
                'args': 0,
            },
            '::': {
                'exec': context.select_call,
                'args': '?',
                'need_args': False,
                'fn': '',
            }
        }

    def __await_args(self) -> bool:
        if not self._context['timer'] == '?':
            return False
        is_symbol_keyword: bool = self._token == '·'
        state: bool = self._context['action']['need_args']

        if is_symbol_keyword:
            state: bool = self._context['action']['need_args']
            self._context['action']['need_args'] = not state

        if not is_symbol_keyword:
            self._context['args'].append(self._token)

        return self._context['action']['need_args']


    def __await_to_call(self) -> bool:
        active: bool = self._context['timer'] == '?'

        if active:
            self._context['action']['fn'] = self._token
            self._context['timer'] = 0

        return active


    def __exec_action(self) -> None:
        self._context['action']['exec'](self._context, self._token)
        self.__clean_exec_context()


    def __clean_exec_context(self) -> None:
        self._context['args'] = []
        self._context['action'] = False


    def __no_action(self) -> bool:
        active: bool = self._context['action']

        if not active:
            if not (self._token in self._tokens):
                raise TokenError(f'Invalid Token: {self._token}')

            self._context['action'] = self._tokens[self._token]
            self._context['timer'] = self._tokens[self._token]['args']

        return not active


    def __validate(self, context: dict, token: str) -> None:
        if not context:
            raise ContextError('Context not found')

        if not token:
            raise TokenError(f'Invalid Token: {token}')

        self._tokens: dict = self.__tokens()
        self._context: dict = context
        self._token: str = token


    def __is_initial(self) -> bool:
        active: bool = self._context['init']

        if active:
            IContext().move_next_node(
                context=self._context,
                node_name=self._token,
            )
            self._context['init'] = False

        return active


    def __is_active_timer(self) -> bool:
        active: bool = self._context['timer'] > 0

        if active:
            self._context['timer'] -= 1
            self._context['args'].append(self._token)

        return active


