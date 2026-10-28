"""Command-line arguments and runtime path resolution."""

from __future__ import annotations

from .config import DATASET_OUTPUT_PARENT_PATH
from .config import ORIGINAL_IMAGE_INPUT_PATH
from .config import PSEUDO_MASK_INPUT_PATH
from pathlib import Path
import argparse


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Open an image file, image folder, or video file in the napari labeling tool."
    )
    parser.add_argument(
        "input_path",
        nargs="?",
        help="Original image file/folder or video. Defaults to ORIGINAL_IMAGE_INPUT_PATH.",
    )
    parser.add_argument(
        "--pseudo-mask", "--mask-dir",
        dest="pseudo_mask",
        help="Optional read-only pseudo-mask reference. New GT masks start empty.",
    )
    parser.add_argument(
        "--dataset-output", "--output-root",
        dest="dataset_output",
        help="Parent directory where a folder named after the input session is created.",
    )
    parser.add_argument(
        "--fps",
        dest="fps",
        type=float,
        help="Target FPS for video frame extraction. If omitted, the script asks in the terminal.",
    )
    return parser.parse_args(argv)


def _optional_path(value: str | Path | None) -> Path | None:
    if value is None or value == "":
        return None
    return Path(value).expanduser()


def dataset_name_for_input(input_path: Path) -> str:
    """Use an image session's parent name, e.g. 20260911_232403."""
    input_path = Path(input_path).expanduser()
    if input_path.name.lower() == "images" and input_path.parent.name:
        return input_path.parent.name
    if input_path.is_file():
        return input_path.stem
    return input_path.name or "dataset"


def resolve_runtime_paths(argv: list[str] | None = None) -> tuple[Path, Path | None, Path | None, float | None]:
    args = parse_args(argv)
    input_path = _optional_path(args.input_path) or ORIGINAL_IMAGE_INPUT_PATH
    pseudo_mask = (
        _optional_path(args.pseudo_mask)
        if args.pseudo_mask is not None
        else PSEUDO_MASK_INPUT_PATH
    )
    dataset_parent = (
        _optional_path(args.dataset_output)
        if args.dataset_output is not None
        else DATASET_OUTPUT_PARENT_PATH
    )
    dataset_output = Path(dataset_parent).expanduser() / dataset_name_for_input(input_path)
    return Path(input_path).expanduser(), pseudo_mask, dataset_output, args.fps
