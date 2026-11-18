<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=170&section=header&text=SVG%20Accessibility%20Check&fontColor=ffffff&fontSize=38&animation=fadeIn" alt="SVG Accessibility Check banner" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&duration=3000&pause=900&color=14B8A6&center=true&vCenter=true&width=820&lines=Catch%20missing%20accessible%20names%20in%20SVG%20artwork" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/svg-a11y-check)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/svg-a11y-check)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/svg-a11y-check?style=flat)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/svg-a11y-check)

<img src="assets/illustration.svg" alt="SVG Accessibility Check illustration" width="92%"/>
</div>

## :compass: Overview

A dependency-free Python checker for local SVG files. It looks for missing accessible names and image roles, while respecting intentionally decorative SVGs marked aria-hidden.

## :sparkles: Features

- :white_check_mark: Scans individual SVG files or whole directories
- :white_check_mark: Checks title or aria-label and role=img semantics
- :white_check_mark: Ignores intentionally decorative aria-hidden SVGs
- :white_check_mark: Reports malformed XML and exits non-zero on issues

## :clapper: Demo

```bash
python main.py examples --recursive
```

The example runs locally; no hosted service or upload is required.

## :rocket: Quick Start

```bash
python -m pip install -r requirements.txt
python main.py examples --recursive
```

Run `python main.py --help` to see all supported options.

## :toolbox: Tech Stack

- Python 3.10+ standard library (ElementTree)
- Automated tests: unittest
- Local-first processing

## :file_folder: Folder Structure

```text
svg-a11y-check/
├── main.py
├── requirements.txt
├── tests/test_core.py
├── examples/sample.svg
└── assets/illustration.svg
```

## :world_map: Roadmap

- [x] Core workflow and CLI
- [x] Example input and tests
- [ ] Additional report formats
- [ ] Continuous integration on supported platforms

## :handshake: Contributing

Issues and pull requests are welcome. Keep changes focused, document behavior changes, and add tests for new features.

## :page_facing_up: License

MIT - see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated wave footer" width="100%"/></div>
