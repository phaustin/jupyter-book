#!/Users/phil/a50037/envs/ebp/bin/python3.7
# -*- coding: utf-8 -*-
import re
import sys
from jupyter_book.commands import main
import shutil

if __name__ == "__main__":
    this_dir = Path().resolve()
    build_dir = this_dir / "testbook/_build"
    shutil.rmtree(build_dir)
    main()
