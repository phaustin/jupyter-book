from jupyter_book.commands import main
from pathlib import Path
import shutil

if __name__ == "__main__":
    this_dir = Path().resolve()
    build_dir = this_dir / "mini_book/_build"
    if build_dir.is_dir():
        print(f"removing {build_dir}")
        shutil.rmtree(build_dir)
    main()
