#!/usr/bin/env python3
"""Copy skills without overwriting existing, different installations."""
import argparse, pathlib, shutil, sys
p=argparse.ArgumentParser()
g=p.add_mutually_exclusive_group(required=True)
g.add_argument('--target',choices=['codex','claude'])
g.add_argument('--dest',type=pathlib.Path)
a=p.parse_args()
root=pathlib.Path(__file__).resolve().parents[1]
dest=a.dest.expanduser() if a.dest else pathlib.Path.home()/('.codex/skills' if a.target=='codex' else '.claude/skills')
sources=sorted((root/'skills').iterdir())
# Preflight all components before any writes.
for src in sources:
 out=dest/src.name
 if out.exists():
  old={str(f.relative_to(out)):f.read_bytes() for f in out.rglob('*') if f.is_file()}
  new={str(f.relative_to(src)):f.read_bytes() for f in src.rglob('*') if f.is_file()}
  if old!=new: sys.exit('已有不同版本，先备份并移走：'+str(out))
dest.mkdir(parents=True,exist_ok=True)
for src in sources:
 out=dest/src.name
 if not out.exists(): shutil.copytree(src,out)
 print('已就绪：',out)
print('请重启 Agent 会话。Agent Reach 程序安装见 README.md。')
