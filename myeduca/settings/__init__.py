from .base import *

env_name = os.getenv('ENV_NAME', 'local')

if env_name == 'local':
    from .local import *
elif env_name == 'pro':
    from .pro import *
else:
    from .base import *
