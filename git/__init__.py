# __init__.py
# Copyright (C) 2008, 2009 Michael Trier (mtrier@gmail.com) and contributors
#
# This module is part of GitPython and is released under
# the BSD License: https://opensource.org/license/bsd-3-clause/
# flake8: noqa
# @PydevCodeAnalysisIgnore
from git.exc import *  # @NoMove @IgnorePep8
import inspect
import os
import sys
import os.path as osp

from typing import Optional
from git.types import PathLike

__version__ = "git"


# { Initialization
def _init_externals() -> None:
    """Initialize external projects by putting them into the path"""
    if __version__ == "git" and "PYOXIDIZER" not in os.environ:
        sys.path.insert(1, osp.join(osp.dirname(__file__), "ext", "gitdb"))

    try:
        import gitdb
    except ImportError as e:
        raise ImportError("'gitdb' could not be found in your PYTHONPATH") from e
    # END verify import


# } END initialization


#################
_init_externals()
#################

# { Imports

try:
    from git.config import GitConfigParser  # @NoMove @IgnorePep8
    from git.objects import *  # @NoMove @IgnorePep8
    from git.refs import *  # @NoMove @IgnorePep8
    from git.diff import *  # @NoMove @IgnorePep8
    from git.db import *  # @NoMove @IgnorePep8
    from git.cmd import Git  # @NoMove @IgnorePep8
    from git.repo import Repo  # @NoMove @IgnorePep8
    from git.remote import *  # @NoMove @IgnorePep8
    from git.index import *  # @NoMove @IgnorePep8
    from git.util import (  # @NoMove @IgnorePep8
        LockFile,
        BlockingLockFile,
        Stats,
        Actor,
        rmtree,
    )
except GitError as _exc:
    raise ImportError("%s: %s" % (_exc.__class__.__name__, _exc)) from _exc

# } END imports

# __all__ must be statically defined by py.typed support
# __all__ = [name for name, obj in locals().items() if not (name.startswith("_") or inspect.ismodule(obj))]
__all__ = [
    "Actor",
    "AmbiguousObjectName",
    "BadName",
    "BadObject",
    "BadObjectType",
    "BaseIndexEntry",
    "Blob",
    "BlobFilter",
    "BlockingLockFile",
    "CacheError",
    "CheckoutError",
    "CommandError",
    "Commit",
    "Diff",
    "DiffIndex",
    "Diffable",
    "FetchInfo",
    "Git",
    "GitCmdObjectDB",
    "GitCommandError",
    "GitCommandNotFound",
    "GitConfigParser",
    "GitDB",
    "GitError",
    "HEAD",
    "Head",
    "HookExecutionError",
    "IndexEntry",
    "IndexFile",
    "IndexObject",
    "InvalidDBRoot",
    "InvalidGitRepositoryError",
    "List",
    "LockFile",
    "NULL_TREE",
    "NoSuchPathError",
    "ODBError",
    "Object",
    "Optional",
    "ParseError",
    "PathLike",
    "PushInfo",
    "RefLog",
    "RefLogEntry",
    "Reference",
    "Remote",
    "RemoteProgress",
    "RemoteReference",
    "Repo",
    "RepositoryDirtyError",
    "RootModule",
    "RootUpdateProgress",
    "Sequence",
    "StageType",
    "Stats",
    "Submodule",
    "SymbolicReference",
    "TYPE_CHECKING",
    "Tag",
    "TagObject",
    "TagReference",
    "Tree",
    "TreeModifier",
    "Tuple",
    "Union",
    "UnmergedEntriesError",
    "UnsafeOptionError",
    "UnsafeProtocolError",
    "UnsupportedOperation",
    "UpdateProgress",
    "WorkTreeRepositoryUnsupported",
    "remove_password_if_present",
    "rmtree",
    "safe_decode",
    "to_hex_sha",
]

# { Initialize git executable path
GIT_OK = None


def refresh(path: Optional[PathLike] = None) -> None:
    """Convenience method for setting the git executable path."""
    global GIT_OK
    GIT_OK = False

    if not Git.refresh(path=path):
        return
    if not FetchInfo.refresh():
        return  # type: ignore [unreachable]

    GIT_OK = True


# } END initialize git executable path


#################
try:
    refresh()
except Exception as _exc:
    raise ImportError("Failed to initialize: {0}".format(_exc)) from _exc
#################
