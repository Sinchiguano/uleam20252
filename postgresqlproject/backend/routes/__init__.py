from flask import Blueprint
api_bp = Blueprint("api", __name__, url_prefix="/api/v1")

from .students import *      # noqa: F401,F403
from .courses import *       # noqa: F401,F403
from .enrollments import *   # noqa: F401,F403
