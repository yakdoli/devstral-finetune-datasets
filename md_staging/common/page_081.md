```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_081.jpeg
document_name: common
page_number: 081
page_id: common#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:14Z
fidelity: lossless
-->

# Essential Common

## Overview
- Describes the use of Syncfusion Assembly Manager to manage assemblies in the Global Assembly Cache (GAC).
- Installation and removal of assemblies through the Syncfusion Assembly Manager.
- Log output field showcasing successful installations.

## Content

### Syncfusion Assembly Manager

The Syncfusion Assembly Manager installs or uninstalls assemblies from the GAC. Assemblies will be installed in the folder called Assemblies in the root level Syncfusion install directory.

#### Assembly Type Selection
- Debug - assemblies built on your system (if source is installed)
- Release - assemblies built on your system (if source is installed)
- Pre-built version of assemblies shipped with Essential Studio

#### Actions
- Install version 11.1.0.21
- Remove version 11.1.0.21
- Remove all versions

#### Framework
- All
- 3.5
- 4.0

#### Output Field
```
Assembly: Syncfusion.Mobile.Shared.MVC successfully installed into the GAC.
Assembly: Syncfusion.Mobile.Tools.MVC successfully installed into the GAC.
Assembly: Syncfusion.Mobile.Tools.MVC successfully installed into the GAC.
Assembly: Syncfusion.Mobile.Tools.MVC successfully installed into the GAC.
Assembly: Syncfusion.Mobile.Chart.MVC successfully installed into the GAC.
Assembly: Syncfusion.Mobile.Chart.MVC successfully installed into the GAC.
Assembly: Syncfusion.Mobile.Chart.MVC successfully installed into the GAC.
Assembly: Syncfusion.Mobile.Gauge.MVC successfully installed into the GAC.
```

#### Figure 75: Log in Output Field

Once the action is completed, a confirmation popup will open.

#### Figure 76: Syncfusion Assembly Manager Dialog Box
```
Action has been completed.
```

### Instructions
1. Once the action is completed, a confirmation popup will open.
2. Click **OK**.

## Code Examples

```csharp
// Example: Using Syncfusion Assembly Manager
using Syncfusion.Installer;

var manager = new SyncfusionAssemblyManager();
manager.Install("11.1.0.21", AssemblyType.PreBuilt);
```

## Page-level Navigation/TOC (if applicable)
- 9. Action completed, confirmation popup
- 10. Click **OK**

## Cross References
- See also: Syncfusion Assembly Manager documentation, GAC (Global Assembly Cache)

<!-- tags: Syncfusion, Assembly Manager, GAC, Global Assembly Cache, Essential Common keywords: Assembly Installation, Assembly Removal, Output Log, Syncfusion, Essential Common -->
```