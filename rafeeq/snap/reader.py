from rafeeq.samples import load_sample


def read_snap(photo_bytes: bytes) -> dict:
    """Read a photo. Demo: returns the sample.

    Later: OpenCV cleanup, then a vision-language model.
    """
    return load_sample("snap_result")