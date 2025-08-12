```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_079.jpeg
document_name: common
page_number: 079
page_id: common#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:57Z
fidelity: lossless
-->

## Overview

- Describes the Syncfusion Assembly Manager, a tool for installing or uninstalling assemblies from the Global Assembly Cache (GAC).
- Explains the process of selecting the required assembly type and action for managing assemblies.
- Outlines the functionality of different options available in the Assembly Type section.
- Provides instructions on how to perform the necessary actions using the Assembly Manager.

## Content

### Syncfusion Assembly Manager

Figure 74: Syncfusion Essential Studio Assembly Manager

#### Select Assembly Type

The Assembly Manager installs or uninstalls assemblies from the GAC. Assemblies are installed in the folder called **Assemblies** in the root level Syncfusion install directory.

1. **Select Assembly Type**
   - **Pre-built Assemblies**: These are the assemblies shipped with Essential Studio. Selecting this mode triggers the Assembly Manager to install the pre-built Assemblies.
   - **Debug and Release Assemblies**: Debug or Release mode will trigger the Assembly Manager to install custom versions built from the source code using **Build Manager**. These assemblies can be used only when the source code for at least one of the Essential Studio products has been installed. This will then install custom versions built from source code, installed on your machine (Applicable only to versions of the product that comes with the source code).

   > **Note:** The Build Manager application has to be run to build debug or release versions of the assemblies before the Assembly Manager can install the custom built assemblies.

2. **Select Action**
   - **Install version 11.1.0.21**
   - **Remove version 11.1.0.21**
   - **Remove all versions**

### Action

#### Select the required option for the Action sections.

## Code Examples

No code examples are provided in this section.

## Page-level Navigation/TOC (if applicable)

No local Table of Contents is present in this section.

## Cross References

See also:
- Related sections on building assemblies and using the Build Manager.
- Documentation on managing assemblies in the Global Assembly Cache (GAC).

## API Reference (if applicable)

No API reference is present in this section.

<!-- tags: [Syncfusion Assembly Manager, GAC, Assembly Management, Essential Studio, Build Manager, version 11.1.0.21] keywords: [Select Assembly Type, Pre-built Assemblies, Debug Assemblies, Release Assemblies, Custom Built Assemblies, Build Manager] -->
```