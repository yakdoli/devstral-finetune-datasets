```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_059.jpeg
document_name: common
page_number: 059
page_id: common#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:50Z
fidelity: lossless
-->

# Essential Common

## Overview
- Steps to manage Syncfusion assemblies using the Assembly Manager.
- Highlighting the process of removing and installing specific versions of assemblies.

## Content

### Figure 52: Assembly Manager

Assembly Manager installs or uninstalls assemblies from the GAC. Assemblies will be installed in the folder called Assemblies in the root level Syncfusion install directory.

- **Select Assembly Type**:
  - Debug - assemblies built on your system (if source is installed)
  - Release - assemblies built on your system (if source is installed)
  - Pre-built version of assemblies shipped with Essential Studio

- **Action**:
  - Install version 11.1.0.21
  - Remove version 11.1.0.21
  - Remove all versions

- **Framework**:
  - All
  - 3.5
  - 4.0

#### Output
Syncfusion Assembly Manager. Copyright, Syncfusion, Inc. 2001-2013.  
Initialization complete. Ready.

---

1. **Select the Remove all versions radio button.**
2. **Click Perform Action.** All versions will be removed.
3. **Select Install version x.x.x.x.**
   > **Note:** x.x.x.x has to be replaced with the corresponding Essential Studio Version.
4. **Click Perform Action.** The assemblies for that specific version will be configured in your machine.
   > **Note:** You can also revert to specific patch assemblies by copying the patch assemblies from the Patch folder and add them in the precompiledassemblies folder.

## Code Examples

No specific code examples provided in this section.

## Page-level Navigation/TOC
- Essential Common
- Detailed explanation of Assembly Manager functionality.

## Cross References
- See also: Assembly Manager documentation, GAC, precompiled assemblies.

<!-- tags: [Syncfusion Winforms, Assembly Manager, GAC, Framework] keywords: [Syncfusion, Assembly, GAC, Framework, Pre-built version, Debug, Release, Install, Remove] -->
```