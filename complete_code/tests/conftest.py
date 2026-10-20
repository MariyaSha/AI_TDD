import threading

import pytest
from werkzeug.serving import make_server

from app import app


@pytest.fixture(scope='session')
def live_url():
    server = make_server('127.0.0.1', 0, app, threaded=True)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f'http://127.0.0.1:{server.server_port}'
    server.shutdown()
    thread.join()
