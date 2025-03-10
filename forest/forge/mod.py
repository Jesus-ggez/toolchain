try:
    from app import ForgeTree

except:
    from .app import ForgeTree


data: dict = {
    'forge': ForgeTree,
}
