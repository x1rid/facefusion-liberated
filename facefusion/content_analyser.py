
from functools import lru_cache
from typing import List

import facefusion.choices
from facefusion.common_helper import is_macos
from facefusion.execution import has_execution_provider
from facefusion.types import InferenceProvider


# ---------------------------------------------------------
# FULL NSFW BYPASS
# ---------------------------------------------------------

def pre_check() -> bool:
    # Skip NSFW model downloads and integrity checks.
    return True


def get_inference_pool():
    # NSFW models are never loaded.
    return None


def clear_inference_pool() -> None:
    # Nothing to clear.
    pass


def override_inference_providers() -> List[InferenceProvider]:
    if is_macos() and has_execution_provider('coreml'):
        return [facefusion.choices.execution_provider_set.get('cpu')]

    return []


def analyse_stream(vision_frame, video_fps) -> bool:
    return False


def analyse_frame(vision_frame) -> bool:
    return False


@lru_cache()
def analyse_image(image_path: str) -> bool:
    return False


@lru_cache()
def analyse_video(
    video_path: str,
    trim_frame_start: int,
    trim_frame_end: int
) -> bool:
    return False
