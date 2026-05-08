from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Create a FastAPI test client."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def restore_activities_state():
    """Reset in-memory activities after each test to avoid state leakage."""
    snapshot = deepcopy(activities)

    yield

    activities.clear()
    activities.update(deepcopy(snapshot))
