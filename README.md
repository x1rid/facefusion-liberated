# FaceFusion Liberated

> A modified, community-maintained fork of FaceFusion with a simplified Windows launch experience.

[![Based on FaceFusion](https://img.shields.io/badge/Based%20on-FaceFusion-blue)](https://github.com/facefusion/facefusion)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![License](https://img.shields.io/badge/license-OpenRAIL--AS-green)

---

## About

**FaceFusion Liberated** is a modified fork of [FaceFusion](https://github.com/facefusion/facefusion), an industry-leading face manipulation platform.

This fork aims to provide a more convenient Windows experience while introducing selected modifications to the original source code.

The goal is to make launching and maintaining FaceFusion easier without losing the functionality of the original project.

## Modifications

This fork currently includes the following changes:

- **Portable Windows Launcher:** Launch FaceFusion using a batch file located in the project directory.
- **Automatic Environment Detection:** The launcher locates the bundled Python environment relative to the project folder.
- **CUDA DLL Preloading:** Attempts to load NVIDIA libraries required by ONNX Runtime.
- **Content Analysis Modification:** Changes the original content analyser behavior.

More modifications may be introduced over time.

## Preview

![FaceFusion Preview](https://raw.githubusercontent.com/facefusion/facefusion/master/.github/preview.png)

## Installation

### Requirements

- Windows 10 or Windows 11
- NVIDIA GPU for CUDA acceleration (optional)
- A compatible Python environment
- Required FaceFusion dependencies and models

### Launching on Windows

If you have the required environment installed in the project directory:

1. Download or clone this repository.
2. Make sure the required Python environment is available under `miniconda3\envs\facefusion`.
3. Run `Launch_FaceFusion.bat`.
4. Wait for FaceFusion to start and open in your browser.

**Note:** The launcher is designed to work relative to the project directory. The bundled Python environment is not included in this Git repository, so you must prepare the dependencies separately.

### Manual Launch

You can also launch FaceFusion using:

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

For detailed instructions and information about FaceFusion, visit:

- [Official FaceFusion Documentation](https://docs.facefusion.io)
- [Original FaceFusion Repository](https://github.com/facefusion/facefusion)

## Credits

FaceFusion Liberated is based on the original [FaceFusion](https://github.com/facefusion/facefusion) project.

Original author and copyright holder: **Henry Ruhs**

All original copyright notices, attributions, and license conditions must be preserved.

This repository contains modifications made for FaceFusion Liberated. These modifications do not imply ownership of the original FaceFusion project.

## License

This project retains the original FaceFusion **OpenRAIL-AS** licensing terms.

Please refer to the included `LICENSE` file for the complete license text and applicable conditions.

---

**FaceFusion Liberated**  
A modified fork of FaceFusion.
