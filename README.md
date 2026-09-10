# Chicago / Grant Park — Aerial Photogrammetry + Terrestrial Laser Dataset

**2,751 aerial photos (41.9 GB) plus the terrestrial laser scans (8.7 GB, 43 stations) over
Grant Park and downtown Chicago, June 2020.** CC BY 4.0.

> ## 🏆 Winner — RealityCapture #RCmonthlyChallenge, August 2020
>
> This reconstruction and its [companion tree scan](https://github.com/Matt1Up/tree-photogrammetry-dataset) were both named
> winners of Capturing Reality's monthly challenge, announced by **RealityScan** — the makers
> of RealityCapture — on 17 September 2020 in
> **[Winners of AUGUST #RCmonthlyChallenge ▶](https://www.youtube.com/watch?v=PfzdaZbUrFc)**.
>
> The video description credits the win as *"@Matt1up — Tree and Chicago city"*, and the
> Chicago model appears in the reel under a `created by: @Matt1up` title card.

![Grant Park reconstruction](preview/hero.jpg)

---

## Grant Park, June 2020

Lollapalooza was cancelled that year. A friend was playing the virtual one and wanted the
Chicago skyline behind him, so I flew the park and the surrounding downtown over two days.

The laser scanner went on the festival field itself — the two softball diamonds and the
floodlit courts where Perry's Stage normally stands. That ground got the detail. The city
around it was backdrop.

Downtown was empty. That part is not repeatable.

![The scanned ground](preview/site-field.jpg)

*The field, empty. Perry's Stage is built over those diamonds and courts.*

## The reconstruction

[![Chicago scan flythrough](preview/video-scan.jpg)](https://vimeo.com/486278234/2233b44140)

*Grant Park flythrough — click to watch on Vimeo*

[![How it was made](preview/video-reel.jpg)](https://vimeo.com/485263221)

*Creation reel — the capture and processing pipeline, click to watch on Vimeo*

Full project write-up: **[mattguertin.com/portfolio/chicago](https://mattguertin.com/portfolio/chicago/)**

| | |
|---|---|
| ![](preview/render-1.jpg) | ![](preview/render-2.jpg) |

## What's in the dataset

| | |
|---|---|
| **Images** | 2,751 JPEG · 41.94 GB |
| **Sensor** | Hasselblad L1D-20c — 1" 20 MP CMOS (DJI Mavic 2 Pro) |
| **Resolution** | 5467 × 3582 (2,297) · 5464 × 3070 (400) · 5366 × 3575 (54) |
| **Lens** | 10.3 mm — 28 mm full-frame equivalent, f/2.8 |
| **Geotagging** | GPS lat/lon/altitude in EXIF — **valid on all 2,751**, none missing |
| **Bounds** | 41.867317 – 41.874759 N · −87.624511 – −87.619413 W |
| **Altitude** | 183 – 315 m above sea level |
| **Captured** | 27–28 June 2020, 06:52 to 19:49 |
| **Laser** | 241 files · 8.66 GB · 43 stations — [see below](#laser-scans) |

### Capture groups

Images are named by the flight that produced them, so you can take a subset without
downloading everything.

| group | images | captured | altitude a.s.l. |
|---|---:|---|---|
| `Grid_Down_1` | 485 | 27 Jun, 11:33–11:49 | 240–289 m |
| `First_Flight_` | 400 | 27 Jun, 06:52–07:32 | 221–310 m |
| `Grid_Down_2` | 372 | 27 Jun, 11:55–12:14 | 281–298 m |
| `Park_Overhead_` | 354 | 28 Jun, 13:47–14:06 | 183–298 m |
| `Grid_Down_4` | 282 | 27 Jun, 19:59–20:14 | 202–285 m |
| `Buildings_3` | 258 | 28 Jun, 06:55–07:13 | 211–315 m |
| `Sunday_Night_Buildings` | 216 | 28 Jun, 19:33–19:47 | 203–214 m |
| `Buildings_2` | 154 | 28 Jun, 06:36–06:48 | 206–314 m |
| `Buildings_1` | 81 | 28 Jun, 06:17–06:23 | 225–315 m |
| `Buildings_4` | 54 | 28 Jun, 06:04–06:17 | 189–311 m |
| `Grid_Down_3` | 54 | 27 Jun, 19:57–19:59 | 234–235 m |
| `Park_Trees_NEW` | 24 | 28 Jun, 13:51–13:53 | 184–193 m |
| `Sunday_Night_Street` | 17 | 28 Jun, 19:48–19:49 | 211–216 m |
| **total** | **2,751** | | |

Group names are the flight names from capture. Times and altitudes above are read from EXIF,
not estimated. Note `First_Flight_` is the only 16:9 group (5464 × 3070); everything else is
3:2 apart from `Buildings_4` at 5366 × 3575.

## The capture rig

![FARO Focus S150 scanning beside the Metra tracks, Grant Park](preview/rig-laser-1.jpg)

Aerial capture with a DJI Mavic 2 Pro (Hasselblad L1D-20c). Terrestrial laser with a FARO
Focus S150, concentrated on the festival field rather than spread over the whole site.

## Scale

The drone images are registered to the laser point cloud. **The laser is the scale reference —
GPS was not used for scale.**

Accuracy is best inside the laser coverage, which is the festival field. Outside that the
photogrammetry extrapolates from that anchor, and drift increases with distance from it.

If you re-align these images on their own, you get correct geometry at arbitrary scale. To get
back to metric you need the laser cloud as a registration target, or ground control.

## Download

**→ [huggingface.co/datasets/Matt1up/chicago-grantpark-photogrammetry](https://huggingface.co/datasets/Matt1up/chicago-grantpark-photogrammetry)**

Click the **Files** tab and download whatever you want in a browser — no tooling, no account.
This GitHub repo holds the documentation, manifests and checksums; the images and laser scans
live there.

**One file, straight from a browser or the shell:**

```bash
curl -O https://huggingface.co/datasets/Matt1up/chicago-grantpark-photogrammetry/resolve/main/images/Buildings_1-1.jpg
```

**Everything, as a git repo** (needs git-lfs — this is 50 GB):

```bash
git clone https://huggingface.co/datasets/Matt1up/chicago-grantpark-photogrammetry
```

**Or use the helper script**, which is just a wrapper around the Hugging Face CLI and adds
resume, parallel transfers and hash checking:

```bash
pip install -U 'huggingface_hub[cli]'

./scripts/download.sh --sample              # ~620 MB, look before committing to 42 GB
./scripts/download.sh --full                # all 2,751 images
./scripts/download.sh --laser               # the 241 laser scan files
./scripts/download.sh --group Grid_Down_1   # one flight
```

More detail and mirrors in **[docs/download.md](docs/download.md)**.

## Reproducing the reconstruction

See **[docs/reproduce.md](docs/reproduce.md)** for alignment settings. The images are ordinary
geotagged JPEGs, so any structure-from-motion tool will read them — RealityScan, Metashape,
COLMAP, Meshroom.

The GPS in EXIF will place the reconstruction roughly on the map, but it is not the scale
reference — see [Scale](#scale) above.

## Gaussian splatting

No camera poses ship with this set, so run COLMAP or **GLOMAP** first — GLOMAP does global
structure-from-motion and is far faster than COLMAP on 2,751 images.

Vanilla 3DGS is built for bounded scenes of a few hundred images and will run out of memory on
a city block. The large-scale variants are what you want: CityGaussian, VastGaussian,
Hierarchical 3DGS, Octree-GS, Scaffold-GS.

Downsample to ~1600 px wide before training. Nothing trains at 5467 px, and the originals are
here so you can pick your own resolution.

## Notes

- **Three sensor crops appear in the set.** 5467 × 3582 for most of it, 5464 × 3070 for the
  `First_Flight_` group, and 5366 × 3575 for 54 frames. Same lens throughout; the solver should
  still be told to treat them as one camera.
- **These are Lightroom exports, not raw.** EXIF records processing in Lightroom Classic 9.3.
- **The renders carry a "Capturing Reality" watermark.** It was a RealityCapture Challenge
  entry on a promotional licence. Preview renders only, never the dataset images.
- **Several passes cover the same ground** at different altitudes and times of day. A curated
  subset aligns faster than all 2,751.

## Laser scans

![Grant Park laser point cloud](preview/rig-laser-2.jpg)

*Registered laser point cloud — Grant Park tree line and ground plane.*

**241 files, 8.66 GB, 43 scan stations**, from a FARO Focus S150. This is the scale reference
the images are registered to.

| tier | files |
|---|---:|
| `quarter_res` | 209 |
| `half_res` | 32 |

Two things to know before you download them:

**They are in RealityScan's `.lsp` format.** RealityScan imports them directly with
`importLaserScanFolder`, and RealityScan is free. Nothing else reads `.lsp`. An **E57**
conversion (the open ASTM standard, readable by CloudCompare, Metashape, Autodesk, Blender)
is planned — open an issue if you need it and I will prioritise it.

**They are downsampled.** `half_res` and `quarter_res`, not full scanner resolution.

```bash
./scripts/download.sh --laser
```

`manifest/laser.csv` lists every file with its station, resolution tier and SHA-256.

## Licence

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Released under [Creative Commons Attribution 4.0 International](LICENSE).
**You may use this commercially, and you may train models on it.** You must give credit.

```
Chicago / Grant Park Aerial Photogrammetry Dataset — Matthew Guertin, 2020.
Licensed CC BY 4.0. https://github.com/Matt1Up/chicago-photogrammetry-dataset
```

See [CITATION.cff](CITATION.cff) for BibTeX and academic citation formats.

## Related

- **[Tree photogrammetry dataset](https://github.com/Matt1Up/tree-photogrammetry-dataset)** —
  812 images of a single tree, with camera poses.
- **[mattguertin.com](https://mattguertin.com)** — portfolio and other work.

---

Captured, processed and released by **Matthew Guertin**.
If you build something with this, I would genuinely like to see it — open an issue.
