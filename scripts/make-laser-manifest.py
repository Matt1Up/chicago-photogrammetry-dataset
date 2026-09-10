#!/usr/bin/env python3
"""Build manifest/laser.csv + laser.sha256 from a folder of RealityScan .lsp files.

Usage: scripts/make-laser-manifest.py <lsp_dir> [repo_root]

Columns: filename, station, res_tier, part, bytes, sha256
Station and tier are parsed from RealityScan's naming:
  {half,quarter}_res_trees_Scan_<station>_<part>.lsp
"""
import csv, hashlib, json, os, re, sys

src = os.path.abspath(sys.argv[1])
root = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(root, "manifest"); os.makedirs(out, exist_ok=True)

files = sorted(f for f in os.listdir(src) if f.lower().endswith(".lsp"))
if not files: sys.exit(f"no .lsp in {src}")
print(f"{len(files)} .lsp files in {src}")

pat = re.compile(r'^(half|quarter)_res_.*_Scan_(\d+)_(\d+)\.lsp$', re.I)
rows, sums = [], []
for i, name in enumerate(files, 1):
    p = os.path.join(src, name)
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""): h.update(c)
    d = h.hexdigest()
    m = pat.match(name)
    rows.append({"filename": name,
                 "station": m.group(2) if m else "",
                 "res_tier": m.group(1).lower() if m else "",
                 "part": m.group(3) if m else "",
                 "bytes": os.path.getsize(p), "sha256": d})
    sums.append(f"{d}  laser/{name}")
    if i % 40 == 0 or i == len(files): print(f"  hashed {i}/{len(files)}")

with open(os.path.join(out, "laser.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["filename","station","res_tier","part","bytes","sha256"])
    w.writeheader(); w.writerows(rows)
with open(os.path.join(out, "laser.sha256"), "w") as fh:
    fh.write("\n".join(sums) + "\n")

total = sum(r["bytes"] for r in rows)
stations = sorted({r["station"] for r in rows if r["station"]})
tiers = {}
for r in rows: tiers[r["res_tier"]] = tiers.get(r["res_tier"], 0) + 1
summary = {"files": len(rows), "bytes": total, "gib": round(total/2**30, 2),
           "stations": len(stations), "tiers": tiers}
json.dump(summary, open(os.path.join(out, "laser-summary.json"), "w"), indent=2)
print(json.dumps(summary, indent=2))
