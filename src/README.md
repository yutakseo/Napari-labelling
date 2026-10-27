# 라벨러 모듈 구조

실행은 프로젝트 루트에서 `python main.py` 또는 기존 `start.bat` / `start.command`를 사용합니다. 명령행 인자도 그대로 지원합니다 (`python main.py --help`).

기본 입력 이미지, 초기 마스크, 출력 경로와 클래스·브러시·줌 설정은 **config.py**에서 수정합니다. 기본 경로는 프로젝트 루트를 기준으로 하므로 저장소를 다른 위치에 복제해도 그대로 동작합니다: 입력은 `input/`, 출력은 `output/`입니다. 초기 마스크 기본값은 없으며, 필요할 때 `--pseudo-mask` 인자로 지정합니다.

예를 들어 프로젝트에 `input/video.mp4`를 넣었다면 다음처럼 실행할 수 있습니다.

```bash
python main.py input/video.mp4 --fps 10
```

`input/` 폴더에 이미지 파일만 넣은 경우에는 `python main.py`로 실행합니다. 다른 위치의 파일을 사용할 때도 절대 경로를 설정 파일에 저장할 필요 없이, 실행 시 상대 경로를 인자로 넘기면 됩니다.

수도 라벨을 GT로 후처리하려면 `--pseudo-mask`에 수도 마스크 파일 또는 폴더를 지정합니다. 시작 시 수도 마스크는 `pseudo_masks/`에 원본으로 보존되고, 편집 결과만 `masks/`에 저장됩니다. 뷰어 우측 상단에는 현재 프레임의 `Dice (pseudo vs GT)`가 표시됩니다. 이 값은 모든 비배경 클래스를 하나의 foreground로 합산한 Dice입니다.

| 모듈 | 담당 기능 |
| --- | --- |
| `config.py` | 기본 경로, 클래스 정의, 편집 설정 |
| `cli.py` | 명령행 인자와 실행 경로 결정 |
| `classes.py` | 클래스 검증, 색상, 기존 클래스 메타데이터 복원 |
| `images.py` | 이미지 탐색과 RGB 로딩 |
| `masks.py` | 마스크 로딩·합성·미리보기, 영역 채우기 |
| `video.py` | 비디오 정보, FPS 선택, 프레임 추출 |
| `dataset.py` | 데이터셋 준비, 이미지/마스크 매칭, 메타데이터 저장 |
| `history.py` | 레이어별 undo/redo 스냅샷 |
| `input_events.py` | Qt 키보드·마우스·포커스 처리 |
| `types.py` | 콜백과 프레임 데이터 공통 타입 |
| `app.py` | napari UI, 편집 세션, 캐시·자동저장, 실행/종료 |

`main.py`는 `src.app.main()`을 호출하는 진입점입니다. UI 콜백은 세션 상태를 공유하므로 `app.py`에 함께 두었습니다. `CLASS_DEFINITIONS`는 `config.py`의 같은 딕셔너리를 공유하며, 실행 중 클래스 추가·복원이 모든 모듈에 반영됩니다.
