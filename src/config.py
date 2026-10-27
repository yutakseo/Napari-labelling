"""User-editable paths, class definitions, and application defaults."""

from __future__ import annotations

from pathlib import Path


# Keep default paths portable when the repository is moved or cloned.  The
# values resolve from this file's location, rather than from the current
# working directory or a machine-specific drive letter.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# 사용자가 설정할 세 가지 경로
# This is the active labeling source. Its images and original pseudo-labels
# remain untouched; each run writes the editable GT session below output/.
DEFAULT_SESSION_ROOT = PROJECT_ROOT / "input" / "노드1_전달용" / "20260911_232403"

# 1) 원본 이미지 파일, 이미지 폴더 또는 비디오
ORIGINAL_IMAGE_INPUT_PATH = DEFAULT_SESSION_ROOT / "images"

# 2) 최초 라벨로 사용할 수도 마스크 파일 또는 마스크 폴더(None 가능)
PSEUDO_MASK_INPUT_PATH: Path | None = DEFAULT_SESSION_ROOT / "masks"

# 3) 학습용 데이터셋을 생성할 상위 폴더
DATASET_OUTPUT_PARENT_PATH = PROJECT_ROOT / "output"

# Add, remove, or rename classes here.  The numeric key is the value saved in
# the multi-class mask; names and colours are reflected in the labeling UI.
CLASS_DEFINITIONS: dict[int, dict[str, object]] = {
    # GT is cyan so it remains visually distinct from the orange pseudo-only overlay.
    1: {"name": "class_1", "color": (0.0, 0.75, 1.0, 1.0)},
}

RGB_EXTS   = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".webp"}
MASK_EXTS  = {".png", ".tif", ".tiff", ".bmp"}
VIDEO_EXTS = {".mp4", ".avi", ".mov", ".mkv", ".mpg", ".mpeg", ".wmv", ".m4v"}

# 비디오 프레임 저장 포맷
FRAME_EXT = ".png"
FRAME_NAME_FMT = "{idx:06d}"
FPS_DIR_PREFIX = "fps_"

# Brush
BRUSH_MIN = 1
BRUSH_MAX = 100
BRUSH_STEP = 1
BRUSH_WHEEL_STEP = 3

# Zoom
ZOOM_MIN = 0.1
ZOOM_MAX = 20.0
ZOOM_STEP = 0.1
ZOOM_WHEEL_RATIO = 1.1

# Undo history (per layer)
MAX_HISTORY = 60
FRAME_CACHE_LIMIT = 4
AUTOSAVE_DELAY_MS = 700
CHANGE_SCAN_MS = 500

