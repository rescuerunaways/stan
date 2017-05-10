from json import loads, dumps
import re

from app.services.validators.validate_input import validate_field, validate_payload


def process(data):
    json = loads(data)
    validate_field("payload", json)
    return dumps(convert(json))


def convert(data):
    return {"response": list(map(m, filter(f, data["payload"])))}


def f(p):
    return _drm_enabled(p) and _episodes_present(p)


def m(p):
    validate_payload(p)
    return {"image": p["image"]["showImage"], "slug": p["slug"], "title": _normalize(p["title"])}


def _episodes_present(p):
    return "episodeCount" in p and p["episodeCount"] > 0


def _drm_enabled(p):
    return "drm" in p and p["drm"] is True


def _normalize(title):
    return re.sub(' \(.*\)', '', title)
