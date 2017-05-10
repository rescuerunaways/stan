from app.errors.error import InvalidRequest


def validate_field(value, data):
    if value not in data:
        raise InvalidRequest()

def validate_payload(p):
    validate_field("image",p)
    validate_field("showImage", p["image"])
    validate_field("slug", p)
    validate_field("title", p)
