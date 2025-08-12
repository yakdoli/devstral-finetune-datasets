```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_132.jpeg
document_name: common
page_number: 132
page_id: common#page_132
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:49Z
fidelity: lossless
-->

# Essential Common

## Overview
- Learn how to upgrade a project into a new Syncfusion version.
- Understand the manual and utility-based approaches for upgrading projects.
- Instructions for handling `CopyLocal=True` and `CopyLocal=False` scenarios.

## Content

### 4.5 How to upgrade the project into a new Syncfusion version

#### 4.5.1 Upgrade the Project Using Project Migration Utility
To upgrade the project using the Project Migration Utility, refer to **Project Migration**.

#### 4.5.2 Upgrading the Projects Manually
You can upgrade the project in two methods based on the procedure used in your project to reference the Syncfusion assemblies. They are:

##### CopyLocal=True
1. Set the **SpecificVersion** to **False**.
2. Remove the **bin** and **obj** folders in your local project directory.
3. Replace the latest assemblies with the upgraded assemblies in the **local** folder of your project.
4. Recompile the project.

##### CopyLocal=False
1. Ensure that the old Syncfusion assemblies are removed from GAC.
   - For 2.0 and 3.5 assemblies: (C:\windows\assembly)
   - For 4.0 assemblies: (C:\Windows\Microsoft.NET\assembly\GAC_MSIL)
2. Install the latest Syncfusion assemblies on your machine using the **Syncfusion Assembly Manager**.
3. Set the **SpecificVersion** to **False**.
4. Recompile your project; the latest assemblies from GAC will refer to your project automatically.

## Page-level Navigation/TOC (if applicable)
- 4.5 How to upgrade the project into a new Syncfusion version
  - 4.5.1 Upgrade the Project Using Project Migration Utility
  - 4.5.2 Upgrading the Projects Manually

## Cross References
- **See also:** Project Migration Utility, Syncfusion Assembly Manager.

<!-- tags: [syncfusion, winforms, project migration, version upgrade, specificversion, copylocal] keywords: [upgrade, syncfusion version, specificversion, copylocal=true, copylocal=false, assemblies, gac, bin obj, local folder, recompile] -->
```