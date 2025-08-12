```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_013.jpeg
document_name: common
page_number: 013
page_id: common#page_013
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:30Z
fidelity: lossless
-->

# Essential Common

## Overview
- Instructions for installing and uninstalling Syncfusion Essential Studio using command line options.
- Focus on the administration mode for setups and clean uninstalls.
- Detailed steps include file extractions, command-line arguments, and silent mode installations.

## Content

### Steps to Install Syncfusion Essential Studio

1. Double-click the Syncfusion Essential Studio Setup file. The self-Extractor wizard opens and extracts the package automatically.
2. The SyncfusionEssentialStudio_(version).exe file will be extracted into the Temp folder.
3. Run `%temp%`. The Temp folder will open. The SyncfusionEssentialStudio_(version).exe file will be available in one of the folders.
4. Copy the SyncfusionEssentialStudio_(version).exe file in local drive. Example: `D:\temp`
5. Cancel the wizard.
6. Open the command prompt in administrator mode and pass the following arguments:
   ```
   "Setup file path\SyncfusionEssentialStudio_(version).exe" Install /PIDKEY:"(product unlock key)" /InstallPath:C:\Program Files\Syncfusion\x.x.x
   ```
   Example:
   ```
   "D:\Temp\SyncfusionEssentialStudio_11.1.0.1.exe" Install /PIDKEY:"product unlock key" /InstallPath:C:\Syncfusion\x.x.x
   ```
7. Setup will be installed.

#### Note:
"`x.x.x` needs to be replaced with the Essential Studio version installed on your machine, and product unlock key needs to be replaced with the unlock key for that version."

### 1.3.3.2 Command Line Uninstall Options

Syncfusion Essential Studio supports uninstalling the setup through command line in silent mode. The following steps illustrate this:

1. If you don’t have the extracted setup (SyncfusionEssentialStudio_(version).exe) then follow the steps from 2 to 7.
2. Double-click the Syncfusion Essential Studio Setup file. The self-Extractor wizard opens and extracts the package automatically.
3. The SyncfusionEssentialStudio_(version).exe file will be extracted into the Temp folder.
4. Run `%temp%`. The Temp folder will open. The SyncfusionEssentialStudio_(version).exe file will be available in one of the folders.
5. Copy the SyncfusionEssentialStudio_(version).exe file in local drive. Example: `D:\temp`
6. Cancel the wizard.
7. Open the command prompt in administrator mode and pass the following arguments:
   ```
   "Setup file path\SyncfusionEssentialStudio_(version).exe" /uninstall true
   ```
   Example:
   ```
   "D:\Temp\SyncfusionEssentialStudio_11.1.0.1.exe" /uninstall true
   ```
8. Setup will be uninstalled.

#### Note:
"`x.x.x` need to be replaced with the Essential studio version installed in your machine and the product unlock key needs to be replaced with the unlock key for that version."

<!-- tags: [Syncfusion, Essential Studio, Command Line, Installation, Uninstallation] keywords: [SyncfusionEssentialStudio, self-Extractor, PIDKEY, product unlock key, silent mode, Setup] -->
```