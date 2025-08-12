```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_080.jpeg
document_name: common
page_number: 080
page_id: common#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:07Z
fidelity: lossless
-->

## Overview

- The Assembly Manager allows you to install or uninstall assemblies.
- You can perform actions by selecting specific radio buttons for installation or removal of specific versions.
- Framework and version selection for .NET framework-based deployments is explained.
- Note: Caution is advised when using features that affect the GAC to avoid application disruptions.

## Content

### Assembly Management

The Assembly Manager can perform install or uninstall assemblies. To perform this action, select the `Install version x.x.x.x` or `remove version x.x.x.x` radio button. To remove all versions, select the `Remove All Versions` radio button.

#### Note:
Remove All Versions must be used with caution in scenarios where one has applications depending on certain versions of the Syncfusion assemblies installed in the GAC. They may cease to function.

#### Step 7: Select the required option for Framework sections.

### Framework

The Framework group box comprises the checkboxes for the .NET framework versions based on the Visual Studio SDK installed in the machine. The following checkboxes are available:

- **4.0** - Selecting 4.0 ensures installation of 4.0 assemblies into the GAC and assemblies folder. In cases where only Visual Studio 2010 SDK is installed, the 4.0 assemblies have to be deployed.
- **3.5** - Selecting 3.5 ensures installation of 3.5 assemblies into the GAC and assemblies folder. In cases where only Visual Studio 2008 SDK is installed, the 3.5, 2.0 assemblies can be deployed.
- **2.0** - Selecting 2.0 ensures installation of 2.0 assemblies into the GAC and assemblies folder. In cases where only Visual Studio 2005 SDK is installed, the 2.0 assemblies have to be deployed.
- **All** - Selecting All ensures installation of all frameworks (frameworks installed in the machine) assemblies into the GAC and assemblies folder.

#### Note:
By default, 2.0 is enabled in a system where Visual Studio 2008 SDK is installed.

#### Step 8:
Click **Perform Action**. It will start processing.

## RAG Annotations

The following tags and keywords were derived from the content:

Tags: Syncfusion, WinForms, Assembly Manager, GAC, .NET Framework
Keywords: installation, uninstall, versions, dependencies, Syncfusion assemblies, Visual Studio SDK, GAC, deployment

```