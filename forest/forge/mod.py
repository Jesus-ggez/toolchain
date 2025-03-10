try:
    from app import ForgeTree

except ImportError:
    from .app import ForgeTree


def call_tree(branch: dict):
    use_tree: ForgeTree = ForgeTree(
        core_util=branch,
    )

    use_fn: str | None = branch.get('call')

    if use_fn is None:
        return

    funcs: dict = {
        'write': use_tree,
    }

data: dict = {
    'forge': call_tree,
}
