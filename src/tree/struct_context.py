class Context:
    def __init__(self) -> None:
        # token
        self.past_token: str = ''
        self.current_token: str = ''
        self.future_expected_tokens: set = set()

        # position
        self.before_tpos: dict = {}
        self.actual_tpos: dict = {}
        self.timeline_name: str = ''

        # actions
        self.need_values: bool = True
        self.values_to_use: int = 0
        self.type_response: str = ''




