from jupyter_book.commands import main
from pathlib import Path
import shutil

if __name__ == "__main__":
    this_dir = Path().resolve()
    build_dir = this_dir / "testbook/_build"
    if build_dir.is_dir():
        shutil.rmtree(build_dir)
    main()
