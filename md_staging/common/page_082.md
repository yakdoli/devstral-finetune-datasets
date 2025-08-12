```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_082.jpeg
document_name: common
page_number: 082
page_id: common#page_082
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:55Z
fidelity: lossless
--}

## Overview
- The page explains the functionality and usage of the Syncfusion Assembly Manager in managing assemblies.
- It details the installation and removal processes for various versions.
- Notes on changes in functionality compared to earlier versions are provided.

## Content

### Syncfusion Assembly Manager Overview

![Figure: Action Completed](#)
**Figure 77: Action Completed**

#### Assembly Manager Functionality
- The Assembly Manager installs or uninstalls assemblies from the GAC (Global Assembly Cache).
- Assemblies will be installed in the folder called **Assemblies** in the root level Syncfusion install directory.

#### User Interface Breakdown
- **Select Assembly Type**:
  - DEBUG: Assemblies built on your system (if source is installed).
  - RELEASE: Assemblies built on your system (if source is installed).
  - Pre-built version of assemblies shipped with Essential Studio.
- **Action**:
  - Install version 11.1.0.21
  - Remove version 11.1.0.21
  - Remove all versions
- **Framework**:
  - All checked versions: 2.0, 3.5, 4.0.

#### Output Window
- Lists successful installations of assemblies into the assemblies folder:
  - Syncfusion.PdfViewer.Windows
  - Syncfusion.DICOM.Base
  - Syncfusion.ProjO.Base
  - Syncfusion.GeckoHtmlRenderer.Base
  - Syncfusion.HTMLToDLS.Base
  - Syncfusion.OCRProcessor.Base
- Indicates that the action has been completed.

### Important Note
- **Key Change**: In earlier versions, the Assembly Manager also served as a build manager to build custom versions of the Syncfusion Assemblies. This functionality has been moved to a separate Build Manager utility.
- **ToolboxInstaller**: Installation of assemblies to the Visual Studio.NET toolbox is now handled by a separate utility called the ToolboxInstaller.
- **Limitation**: The new Assembly Manager only handles installation of assemblies to the GAC and the assemblies folder. The Assemblies folder is applicable only if Visual Studio.NET is installed.

### Version Switching
- **Previous versions**: Allowed switching to any version of the Syncfusion assemblies installed on the system. This caused compatibility issues and restricted the utility's structure.
- **Current Version**: To switch to another version, you must run the Assembly Manager of the respective version.
- **Preferable Flow**: It is preferable to perform a **Remove All** operation with the Assembly Manager before installing the latest assemblies to ensure clean updates.

### Console Version of the Assembly Manager
- The console version will run at the end of the install process to add the default pre-built version of the Syncfusion assemblies to the Global Assembly Cache (GAC) and the Visual Studio .NET Public Assemblies folders (if applicable).
- The need to run the Assembly Manager only arises when changes have been made to the GAC or when custom versions have been built for debugging purposes.

## Cross References
- See also: Build Manager, ToolboxInstaller, Global Assembly Cache (GAC), Visual Studio.NET Public Assemblies.

<!-- tags: [assembly-manager, syncfusion-assemblies, gac] keywords: [installation, uninstallation, version-switching, compatibility-issues, toolbox-installer, pre-built-assemblies, visual-studio-net] -->
```