```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: common
page_number: 083
page_id: common#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:11Z
fidelity: lossless
-->

# Essential Common

## Overview
- Details the installation locations of Syncfusion assemblies.
- Explains the structure of the Assemblies folder and the Global Assembly Cache (GAC).
- Provides specific paths for different .NET Framework versions (2.0, 3.5, 4.0).
- Highlights the role of Build Manager in managing Syncfusion assemblies.

## Content

### Syncfusion Assemblies
The Syncfusion assemblies are installed in the following two locations:
- **Assemblies folder**
- **Global Assembly Cache (GAC)**

#### The Assemblies folder
In the **Assemblies** folder, the assemblies will be available in the following installation path:
```
[SYSTEM DRIVE]:\Program Files\Syncfusion\Essential Studio\x.x.x\Assemblies
```

**Note:**
- The sub-folder `3.5` is used with .NET 3.5.
- The sub-folder `2.0` is used with .NET 2.0.
- In most cases, `[System Drive]:\` is `C:\`.

#### Global Assembly Cache (GAC)
- In **2.0 and 3.5 GAC**, assemblies will be available in the installation path:
  ```
  [System Drive]:\WINDOWS\assembly
  ```
- In **4.0 GAC**, assemblies will be available in the installation path:
  ```
  [System Drive]:\WINDOWS\Microsoft.NET\assembly\GAC_MSIL
  ```

#### Essential Studio and PreCompiledAssemblies
Essential Studio ships the pre-built 2.0, 3.5, and 4.0 .NET Framework versions of the Syncfusion assemblies. These assemblies are located in the `PreCompiledAssemblies` folder:
```
[SYSTEM DRIVE]:\Program Files\Syncfusion\Essential Studio\x.x.x\PreCompiledAssemblies\x.x.x\2.0
```
If you work with multiple target environments, you will see that each appropriate version is installed in the GAC for true side-by-side use.

**Working with Syncfusion Assemblies**:
- Syncfusion assemblies built and tested with specific .NET Framework versions increase reliability.
- They allow controls to leverage features specific to the target .NET environment.
- For example, .NET 2.0 variants offer features specific to the .NET 2.0 environment.

### 1.13.3 Build Manager
**Build Manager** allows you to build or debug the assemblies using the Syncfusion source code.

#### Launching Build Manager
<!-- This section is left intentionally blank for future content. -->

## Page-level Navigation/TOC
- **Syncfusion Assemblies**
  - The Assemblies folder
  - Global Assembly Cache (GAC)
  - PreCompiledAssemblies
- **Build Manager**
  - Launching Build Manager

<!-- tags: [Syncfusion, Winforms, Assemblies, GAC, Build Manager, .NET Framework, 2.0, 3.5, 4.0, version 11.4.0.26] keywords: [syncfusion assemblies, global assembly cache, assemblies folder, essential studio, precompiled assemblies, build manager, side-by-side use, .NET Framework versions, reliability, specific features, source code] -->
```