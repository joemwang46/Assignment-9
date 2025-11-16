import os
import json
from logger import Logger

def test_logger_singleton():
    a = Logger()
    b = Logger()
    assert a is b

def test_logger_logs_event(tmp_path):
    path = tmp_path / "events.json"
    log = Logger(path=str(path))
    log.events.clear()

    log.log("TestEvent", {"x": 1})
    assert len(log.events) == 1
    assert log.events[0]["type"] == "TestEvent"

def test_logger_saves_json(tmp_path):
    path = tmp_path / "events.json"
    log = Logger(path=str(path))
    log.events.clear()

    log.log("TestEvent", {"y": 2})
    log.save()

    with open(path, "r") as f:
        data = json.load(f)

    assert data[0]["type"] == "TestEvent"
    assert data[0]["data"]["y"] == 2
