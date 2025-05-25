# SEAS-8405 Homework 7: Secure Flask App in Docker

**Author**: Daniel Mehditash  
**Course**: SEAS-8405 – Cybersecurity Architecture  
**Institution**: George Washington University  
**Repo**: https://github.com/DannyxMARFI/seas8405-hw7-hardened-app

---

## 🔐 Overview

This project demonstrates how to analyze, secure, and deploy a vulnerable Flask web app using containerization best practices. The original app contained critical security flaws like:

- Hardcoded secrets
- Use of `eval()`
- Command injection via `subprocess(shell=True)`
- Running as `root` in Docker
- Exposed Docker ports
- Missing health checks and input validation

Each vulnerability was remediated with secure coding, hardened configurations, and container-level controls.

---

## 📁 Project Structure

```plaintext
before/
├── app.py                   # Secured Flask app with input validation and safe exec
├── Dockerfile               # Hardened: non-root, HEALTHCHECK, minimal image
├── docker-compose.yml       # Limits (mem, pids), .env support, localhost-only
├── Makefile                 # make start / make check helpers
├── requirements.txt
deliverables/
├── Deliverables.ipynb       # Jupyter notebook documenting full assignment
├── threat_model.md          # STRIDE, MITRE ATT&CK, NIST 800-53 mapping
├── summary_report.md        # 2-page written reflection
├── hardened_architecture_diagram.png
docker_security_fixes.py     # Auto-hardening script for Docker and Compose
