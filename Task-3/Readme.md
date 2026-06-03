# Task 3: Automated Vulnerability Assessment and Threat Mapping via Tenable Nessus

## 📌 Project Objective
To deploy a localized vulnerability assessment architecture within a Windows environment, resolve enterprise credential and signature database dependency traps, execute an automated credentialless baseline vulnerability audit, and evaluate the final attack surface footprint using CVSS structural scoring metrics.

---

## 🛠️ Environmental Engineering & Troubleshooting Log

During the deployment lifecycle, multiple system and server-side authentication conflicts were encountered and systematically engineered to restore scanner stability.

### 1. Web UI File Asset Sync Errors
* **Symptom:** Browser connections threw a raw JSON system string: `{"error":"The requested file was not found."}`
* **Root Cause Analysis:** Sudden interruptions during the manual signature download phase left the front-end interface web modules unextracted, rendering the server unable to map standard routing paths.
* **Remediation Action:** Executed a structured backend directory repair via the Administrative CLI (`nessuscli.exe fix --reset`) to clear out the stalled execution states.

### 2. Preference Validation Failures
* **Symptom:** Network registration loops threw explicit terminal abort sequences: `Could not validate this preference file.`
* **Root Cause Analysis:** Local application parameters fell completely out of synchronization with the server identity profile, causing Tenable servers to block incoming registration requests.
* **Remediation Action:** Cleared all active credential keys via `nessuscli.exe fix --reset-all`, purged stale local `plugin_feed_info.inc` descriptors, registered a fresh activation token directly through the backend utility agent, and forced an internal database index rebuild using `nessusd.exe -R`.

### 3. Setup Wizard Configuration Bypass
* **Symptom:** Browser-based account generation stalled with a red warning banner: `Error: User could not be added. Check if a user already exists.`
* **Root Cause Analysis:** The frontend configuration layers were wiped out, but the persistent underlying backend data repositories retained the user structural references from previous installation steps.
* **Remediation Action:** Sidestepped the frontend block by injecting an administrative profile securely using the direct engine configuration interface:
  ```cmd
  nessuscli.exe adduser admin
