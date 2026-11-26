#!/usr/bin/env python3
"""Bootstrap BLE dependencies without invoking dbus-fast's source build backend."""
import os
import shutil
import tarfile
import tempfile
import urllib.request

VERSION = "2.20.0"
URL = "https://files.pythonhosted.org/packages/source/d/dbus-fast/dbus_fast-%s.tar.gz" % VERSION
VENDOR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor")
PACKAGE = os.path.join(VENDOR, "dbus_fast")

def install_dbus_fast():
    if os.path.isdir(PACKAGE) and os.path.isfile(os.path.join(PACKAGE, "__init__.py")):
        return
    os.makedirs(VENDOR, exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp:
        archive_path = tmp.name
    try:
        urllib.request.urlretrieve(URL, archive_path)
        with tarfile.open(archive_path, "r:gz") as archive:
            candidates = [m for m in archive.getmembers()
                          if m.isfile() and "/dbus_fast/" in m.name]
            if not candidates:
                raise RuntimeError("dbus-fast source archive has no package files")
            root = candidates[0].name.split("/dbus_fast/", 1)[0] + "/dbus_fast/"
            staged = tempfile.mkdtemp(prefix="dbus-fast-", dir=VENDOR)
            try:
                for member in candidates:
                    rel = member.name.split(root, 1)[-1]
                    if not rel or rel.startswith("/") or ".." in rel.split("/"):
                        continue
                    target = os.path.join(staged, rel)
                    os.makedirs(os.path.dirname(target), exist_ok=True)
                    src = archive.extractfile(member)
                    if src is None:
                        continue
                    with src, open(target, "wb") as dst:
                        shutil.copyfileobj(src, dst)
                if not os.path.isfile(os.path.join(staged, "__init__.py")):
                    raise RuntimeError("dbus-fast package extraction was incomplete")
                if os.path.isdir(PACKAGE):
                    shutil.rmtree(PACKAGE)
                shutil.move(staged, PACKAGE)
            finally:
                if os.path.isdir(staged):
                    shutil.rmtree(staged)
    finally:
        if os.path.exists(archive_path):
            os.unlink(archive_path)

install_dbus_fast()
