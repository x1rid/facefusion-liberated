# FaceFusion Liberated

> A modified version of FaceFusion with NSFW filter removal and an improved Windows launching experience.

[![Based on FaceFusion](https://img.shields.io/badge/Based%20on-FaceFusion-blue)](https://github.com/facefusion/facefusion)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![License](https://img.shields.io/badge/license-OpenRAIL--AS-green)

---

## About

**FaceFusion Liberated** is a modified fork of [FaceFusion](https://github.com/facefusion/facefusion), an industry-leading face manipulation platform originally developed by Henry Ruhs and contributors.

This fork introduces changes to the original content analysis system and provides a simplified Windows launching experience.

The goal is to make FaceFusion easier to launch and maintain while preserving its core functionality.

## Modifications

This fork includes the following modifications:

- **NSFW Filter Removal:** Disables FaceFusion's original NSFW content-analysis checks, allowing users to process content without the built-in NSFW filtering.
- **Portable Windows Launcher:** Launch FaceFusion using a batch file located in the project directory.
- **Automatic Environment Detection:** Detects the bundled Python environment relative to the project folder.
- **CUDA DLL Preloading:** Attempts to load NVIDIA libraries required by ONNX Runtime for GPU acceleration.

### Important Notice

The original FaceFusion NSFW content-analysis filtering has been disabled in this fork.

Users are responsible for ensuring that their use of this software complies with applicable laws, third-party rights, and the project's license conditions.

## Preview

![FaceFusion Preview](https://raw.githubusercontent.com/facefusion/facefusion/master/.github/preview.png)

## Installation

### Requirements

- Windows 10 or Windows 11
- NVIDIA GPU for CUDA acceleration (optional)
- Required Python environment
- FaceFusion dependencies and models

### Launching on Windows

1. Download or clone this repository.
2. Prepare the required Python environment under `miniconda3\envs\facefusion`.
3. Run `Launch_FaceFusion.bat`.
4. Wait for FaceFusion to start and open in your browser.

**Note:** The launcher works relative to the project directory. The bundled Python environment is not included in this Git repository, so dependencies must be installed separately.

### Manual Launch

You can also launch FaceFusion manually:

```powershell
python facefusion.py run --open-browser
```

Refer to the [official installation documentation](https://docs.facefusion.io/installation) for dependency setup.

## Usage

FaceFusion supports several commands:

```powershell
python facefusion.py [commands] [options]
```

Available commands include:

- `run` – Run the application.
- `headless-run` – Run without the graphical interface.
- `batch-run` – Process multiple files.
- `benchmark` – Run performance benchmarks.
- `force-download` – Download required resources.
- `job-list` – List existing jobs.
- `job-create` – Create a new job.
- `job-submit` – Submit a job for processing.

For the complete command list, run:

```powershell
python facefusion.py --help
```

## Documentation

- [Official FaceFusion Documentation](https://docs.facefusion.io)
- [Original FaceFusion Repository](https://github.com/facefusion/facefusion)

## Credits

FaceFusion Liberated is based on the original [FaceFusion](https://github.com/facefusion/facefusion) project.

Original author and copyright holder: **Henry Ruhs**

All original copyright notices, attributions, and license conditions must be preserved.

This fork contains independent modifications. These modifications do not imply ownership of the original FaceFusion project.

## License

This project retains the original FaceFusion **OpenRAIL-AS** licensing terms.

Refer to the included `LICENSE` file for the complete license text and applicable conditions.

---

**FaceFusion Liberated**  
A modified fork of FaceFusion.
