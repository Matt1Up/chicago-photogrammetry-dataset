# Reproducing the reconstruction

The dataset solves in RealityCapture / RealityScan, Agisoft Metashape, COLMAP and Meshroom.
Below are the settings that produced the original result, plus the traps specific to *this*
capture.

---

## RealityCapture / RealityScan

Suggested starting settings. These are recommendations, not a record of the original run.

**Alignment**
| setting | value | why |
|---|---|---|
| Image overlap | `Medium` | grid flights have generous overlap already |
| Max features per image | `40000` | default; do not raise for a set this size |
| Max features per mpx | `10000` | |
| Detector sensitivity | `Medium` | urban texture is rich; `High` mostly adds noise here |
| Preselector features | `10000` | |
| Force component rematch | off | leave off unless you get splits |

Run a **draft alignment first.** At 2,751 × 20 MP this is a heavy project; find out that your
settings work before committing to a full run.

**If alignment splits into multiple components**, options in order of preference:

1. Align the daylight groups first, then add the night groups to the existing component.
2. Add control points across two or three shared facades.
3. Enable *Force component rematch* and re-run.

**Reconstruction** — start in `Preview` quality. `Normal` over the whole set is a
many-hour job and needs substantial RAM. Set a reconstruction region first; the full
un-clipped extent includes a lot of distant, thinly-observed skyline you probably do not want.

**Coordinate system** — images are WGS 84 (EPSG:4326). For anything metric, project to a
local system; for Chicago, EPSG:26916 (UTM 16N) or the Illinois State Plane East zone.

---

## Agisoft Metashape

```
Add Photos → all groups
Estimate Image Quality → discard anything below ~0.6
Align Photos:  Accuracy High · Generic preselection on · Reference preselection SOURCE
               Key point limit 40,000 · Tie point limit 10,000
```

Then: Optimize Cameras → Build Depth Maps (Medium) → Build Dense Cloud / Mesh.

---

## COLMAP

```bash
colmap feature_extractor \
  --database_path db.db --image_path images/ \
  --ImageReader.camera_model SIMPLE_RADIAL \
  --ImageReader.single_camera 1

colmap exhaustive_matcher --database_path db.db     # small subsets only
# for the full 2,751 use vocab-tree matching instead:
colmap vocab_tree_matcher --database_path db.db \
  --VocabTreeMatching.vocab_tree_path vocab_tree_flickr100K_words256K.bin

colmap mapper --database_path db.db --image_path images/ --output_path sparse/
```

`--ImageReader.single_camera 1` is correct here — every frame is the same physical lens at a
fixed focal length. Exhaustive matching at this image count is O(n²) and impractical; use the
vocabulary tree.

---

## What to expect

- **Every image carries a valid GPS fix.** All 2,751 have latitude, longitude and altitude in
  EXIF, verified across the set — you can georeference straight from the images with no ground
  control and no filtering.
- **Not every image will align, and that is fine.** Redundant grid coverage means a handful of
  dropped frames cost you nothing.
- **Several passes overlap the same ground** at different altitudes and times of day. For a
  first run, take one `Grid_Down_*` group plus one `Buildings_*` group rather than everything —
  it solves far faster and looks nearly as good.
- The published reconstruction used the full set with terrestrial laser scans registered in
  alongside. Those scans are not in v1.0 — see the README.
