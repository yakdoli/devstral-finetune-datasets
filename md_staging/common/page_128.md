```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_128.jpeg
document_name: common
page_number: 128
page_id: common#page_128
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:35Z
fidelity: lossless
-->

## Overview
- This page provides instructions to manage versions of Syncfusion.Core references in a project.
- It outlines steps to ensure correct setup for references and settings in the project.

## Content

### Procedure for Updating Project References

1. **Figure 122: Project in Text Editor**
   
   The figure displays an example of a project file (`.csproj`) opened in a text editor (`Notepad++`). This section includes configurations for build settings such as:
   - Error Reporting
   - Warning Level
   - Platform Target
   - Debug Type
   - Optimization
   - Output Path
   - Define Constants
   - Error Reporting for release mode.

   Below are specific `<Reference>` entries for Syncfusion components:
   ```xml
   <Reference Include="Syncfusion.Core, Version=10.104.0.44, Culture=neutral, PublicKeyToken=632609b4d040f6b4" />
   <Reference Include="Syncfusion.Grid.Base, Version=10.104.0.44, Culture=neutral, PublicKeyToken=3d67ed1f87d4" />
   <Reference Include="Syncfusion.Grid.Windows, Version=10.104.0.44, Culture=neutral, PublicKeyToken=3d67ed1f8" />
   <Reference Include="Syncfusion.Shared.Base, Version=10.104.0.44, Culture=neutral, PublicKeyToken=3d67ed1f87d4" />
   <Reference Include="Syncfusion.Shared.Windows, Version=10.104.0.44, Culture=neutral, PublicKeyToken=3d67ed1" />
   ```

2. **Steps to Update References**

   - **If more than one Syncfusion.Core entry exists in your project, remove those entries.**
   - **Reload your project in Visual Studio.**
   - **Set the Copy Local and Specific Version property set to True for all Syncfusion referenced assemblies.**

## RAG Annotations

<!-- tags: [syncfusion, winforms, project configuration, references, assembly version] keywords: [Syncfusion.Core, reference management, Copy Local, Specific Version, project file, Visual Studio] -->
```