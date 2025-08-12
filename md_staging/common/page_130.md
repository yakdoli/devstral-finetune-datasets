```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_130.jpeg
document_name: common
page_number: 130
page_id: common#page_130
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:35Z
fidelity: lossless
-->

### Overview

The document describes resolving access denied errors when accessing essential Studio Windows Forms samples and manually uninstalling the Syncfusion Setup in cases where the uninstall utility is unavailable.

### Content

#### Essential Studio Sample Browser Access

- **Description**:
  - The image shows an "Access Denied" message indicating that the essential Studio Windows Forms Edition Sample Browser was unable to access the folder containing sample files.
  - Error message details:
    - Folder path: `C:\Users\Administrator\Documents\Syncfusion\EssentialStudio\8.1.0.30\Windows`.
    - The issue occurs because the installation of essential Studio was performed under a different user account than the current user account.

#### Solution for Access Denied Error

- **Action**:
  - The administrator should provide access privileges to the folder path for the non-admin user.

---

#### 4.4 How to Uninstall the Syncfusion Setup Manually

- **Purpose**:
  - To uninstall the Syncfusion Setup manually when the uninstall utility is not available due to installation crashes or other issues.

- **Steps to Uninstall Manually**:
  1. **Download and Install Windows Installer Cleanup Utility**:
     - Obtain and install the Windows Installer cleanup utility from the following link: [Windows Installer cleanup](http://Windows%20Installer%20cleanup).
  2. **Remove Syncfusion Product-related Installers**:
     - Use the Windows Installer Cleanup utility to remove the Syncfusion product-related installers for the version being uninstalled.

---

## API Reference

Not applicable in this context.

## Code Examples

None.

## Tags and Keywords

<!-- tags: essentialStudio, windowsForms, sampleBrowser, accessDenied, uninstallUtility, WindowsInstallerCleanup, SyncfusionWinforms, setupUpgrade module: documentation, troubleshooting, uninstallation -->
```