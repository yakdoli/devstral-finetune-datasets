```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_129.jpeg
document_name: common
page_number: 129
page_id: common#page_129
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:53Z
fidelity: lossless
-->

## Overview

- Describes how to manage references in a Windows Forms application.
- Explains the significance of "Copy Local" property and its implications for deployment.
- Details a method to overcome "Access Denied" errors for non-admin users when accessing the Sample Browser.

## Content

### Property Window

Figure 123 illustrates the Property Window in a Visual Studio solution. The window shows the properties for a reference to a Syncfusion assembly, highlighting the "Copy Local" property set to True. This indicates that the reference will be copied to the output directory during the build process.

---

### Steps to Configure References

1. Open the `Solution Explorer` in Visual Studio.
2. Locate and select the desired reference from the project's list of references.
3. Open the `Properties` window and ensure the `Copy Local` property is set to `True`.
4. Verify that the other properties such as `Resolved`, `Runtime Version`, and `Specific Version` are configured appropriately.
5. Repeat the process for all necessary references.
6. Rebuild your application to apply the changes.

---

### 4.3 How to overcome Sample Browser Access Denied Error for a Non-Admin User

When an administrator installs the Essential Studio setup in a machine, a non-admin user encounters an "Access Denied" error when attempting to run the Sample Browser from the Dashboard. This issue arises because the non-admin user tries to access the `Admin` folder where the samples are installed.

#### Problem Description

- **Cause**: The Samples are by default stored in the `Admin` folder, which is not accessible to non-admin users.
- **Symptom**: A message box appears indicating that the user lacks the necessary permissions to access the folder.

#### Solution

To allow non-admin users to access the Sample Browser:

1. **Run as Administrator**:
   - Right-click on the Sample Browser and select "Run as administrator."
   - This allows the user to temporarily access the protected folder with admin privileges.

2. **Relocate Samples**:
   - Move the Sample Browser files to a location accessible by non-admin users (e.g., `C:\Program Files (x86)\Syncfusion\EssentialStudio\SampleBrowser`).
   - Update the installation path to reflect the new location.

3. **Change Folder Permissions**:
   - Right-click on the `Admin` folder and select "Properties."
   - Navigate to the "Security" tab and add the desired user with "Full Control" permissions.
   - Apply the changes so that the user can now access the Samples.

---

## Cross References

- Refer to the documentation on configuring assembly references for more detailed guidance.
- For further assistance with Syncfusion product setup and deployment, consult the official Support Portal.

---

<!-- tags: [windowsforms, deployment, accessdenied, samplebrowser, nonadmin] keywords: [property window, copy local, rebuild, access denied, solution explorer, syncfusion assemblies, admin folder, non-admin user, sample browser, dashboard] -->
```