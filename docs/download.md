# Downloading the dataset

The images are **not stored in this GitHub repository** — GitHub is not built for this, and
Git LFS bandwidth caps would make it unusable. This repo holds documentation, manifests and
checksums; the images and laser scans live on Hugging Face.

Total: **41.9 GB of images (2,751 files), plus 8.66 GB of laser scans (241 files).**

---

## Why it is packaged the way it is

**The images are published as individual files, not one giant archive.** That is deliberate:

- You can download **one capture group** instead of all 41.9 GB.
- Downloads **resume**. A dropped connection at 38 GB does not start over.
- Each file is **individually checksummed**, so corruption is localised, not fatal.
- No 42 GB of scratch space needed just to unpack an archive.

**Nothing is gzipped.** JPEG is already compressed — measured on this dataset, gzip reclaims
**0.2%** while costing hours of CPU and destroying random access.

---

## Hugging Face

Resumable, parallel, hash-verified, and the CLI handles retries for you.

```bash
pip install -U huggingface_hub

# sample pack (~620 MB) — look before you commit to 41.9 GB
./scripts/download.sh --sample

# everything — images, laser scans, sample
./scripts/download.sh --full

# the 2,751 images only
./scripts/download.sh --images

# just one flight
./scripts/download.sh --group Grid_Down_1
```

Or browse the files directly: **https://huggingface.co/datasets/Matt1up/chicago-grantpark-photogrammetry**

Raw CLI, if you prefer not to use the wrapper. Run it again if it stops — finished files are
skipped.

```bash
# everything
hf download Matt1up/chicago-grantpark-photogrammetry --repo-type dataset --local-dir ./data

# images only
hf download Matt1up/chicago-grantpark-photogrammetry --repo-type dataset --local-dir ./data --include 'images/*'
```

The full set is 3,048 files. If Hugging Face answers `429 Too Many Requests`, that is its rate
limit — wait five minutes and run the same command again, or log in first with `hf auth login`.

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

## Sample pack

A small curated subset — enough to judge image quality, overlap and metadata before
committing to the full download. It is on Hugging Face under `sample/`;
`./scripts/download.sh --sample` fetches it.

---

## Verifying what you downloaded

```bash
./scripts/verify.sh
```

Checks SHA-256 for every image and laser file you actually have and ignores the rest, so
partial downloads verify cleanly. `manifest/checksums.sha256` (images) and
`manifest/laser.sha256` are the authoritative lists; `manifest/images.csv` additionally carries
dimensions, capture time and GPS per image.
