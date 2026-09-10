# Downloading the dataset

The images are **not stored in this GitHub repository** — GitHub is not built for this, and
Git LFS bandwidth caps would make it unusable. This repo holds documentation, manifests and
checksums; the images live on hosts designed for large public datasets.

Total: **41.9 GB of images (2,751 files), plus 8.66 GB of laser scans (241 files).**

---

## Why it is packaged the way it is

**The images are published as individual files, not one giant archive.** That is deliberate:

- You can download **one capture group** instead of all 41.9 GB.
- Downloads **resume**. A dropped connection at 38 GB does not start over.
- Each file is **individually checksummed**, so corruption is localised, not fatal.
- No 42 GB of scratch space needed just to unpack an archive.

**Nothing is gzipped.** JPEG is already compressed — measured on this dataset, gzip reclaims
**0.2%** while costing hours of CPU and destroying random access. Where archives are offered
(mirrors below), they are **store-only ZIPs**, split per capture group.

---

## Primary — Hugging Face

Resumable, parallel, hash-verified, and the CLI handles retries for you.

```bash
pip install -U 'huggingface_hub[cli]'

# sample pack (~620 MB) — look before you commit to 41.9 GB
./scripts/download.sh --sample

# everything
./scripts/download.sh --full

# just one flight
./scripts/download.sh --group Grid_Down_1
```

Or browse the files directly: **https://huggingface.co/datasets/Matt1Up/chicago-grantpark-photogrammetry**

Raw CLI, if you prefer not to use the wrapper:

```bash
hf download Matt1Up/chicago-grantpark-photogrammetry --repo-type dataset --local-dir ./data --include 'images/*'
```

---

## Laser scans

```bash
./scripts/download.sh --laser        # 241 files, 8.66 GB
```

`.lsp` format — RealityScan reads these directly via `importLaserScanFolder`, and RealityScan
is free. No other software reads `.lsp`. They are `half_res` and `quarter_res`, not full
scanner resolution.

`manifest/laser.csv` lists every file with station, resolution tier, size and SHA-256.
`manifest/laser.sha256` is the checksum list.

---

## Mirror — Internet Archive

Permanent, no account needed, and every item gets a **BitTorrent** file automatically.
Torrent is the friendliest option for the full set: it resumes, verifies, parallelises, and
costs the project nothing.

**https://archive.org/details/chicago-grantpark-photogrammetry-2020**

```bash
# whole set over torrent
aria2c https://archive.org/download/chicago-grantpark-photogrammetry-2020/chicago-grantpark-photogrammetry-2020 _archive.torrent

# or a single group over plain HTTPS, resumable
curl -C - -O https://archive.org/download/chicago-grantpark-photogrammetry-2020/images/Grid_Down_1-1.jpg
```

---

## Sample pack

A small curated subset — enough to judge image quality, overlap and metadata before
committing to the full download. Served from `files.hometwin.io`.

---

## Verifying what you downloaded

```bash
./scripts/verify.sh
```

Checks SHA-256 for every file you actually have and ignores the rest, so partial downloads
verify cleanly. `manifest/checksums.sha256` is the authoritative list;
`manifest/images.csv` additionally carries dimensions, capture time and GPS per image.

## If a mirror is down

All mirrors carry byte-identical files with matching checksums. Pull from whichever works —
`verify.sh` will confirm you got the right bytes regardless of source.
