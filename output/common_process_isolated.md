---
title: "common - Syncfusion SDK Documentation"
type: "api-documentation"
framework: "syncfusion"
version: "v11"
processing_mode: "Process Isolation (프로세스 격리)"
extracted_date: "1754712430.4280906"
optimized_for: ["llm-training", "rag-retrieval"]
scaling_approach: "3"
---

<!-- 페이지 1 -->

```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_001.jpeg
document_name: common
page_number: 001
page_id: common#page_001
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:58:45Z
fidelity: lossless
-->

# Essential Common

## Overview
- Documentation for **Essential Studio 2013 Volume 4 - v.11.4.0.26**.
- Focuses on **Syncfusion Winforms** components.
- Covers **common** functionalities and utilities.

## Content

### Introduction

The **Essential Common** section in the **Essential Studio 2013 Volume 4 - v.11.4.0.26** provides comprehensive details on the common features and functionalities available in Syncfusion Winforms. This includes various utilities, tools, and components that are integral to building robust and efficient desktop applications.

#### Key Features
- **Utility Classes**: Focuses on providing generic and reusable functionality.
- **Common Components**: Includes controls and elements that are often used across different applications.
- **Integration**: Details how these common components can be integrated seamlessly with other Syncfusion components for a cohesive user experience.

## API Reference

This section will cover the namespaces and classes involved in the **Essential Common** functionality. For brevity, only an example snippet is provided here. The complete API reference can be found in the full documentation.

### Example API

#### Namespace: `Syncfusion.Windows.Forms.Common`

```csharp
// Example of a common utility class
public class CommonUtility
{
    public static void FormatDataObject(DataObject dataObject)
    {
        // Implementation for formatting data objects
    }

    public static void SerializeObject(object objToSerialize, string filePath)
    {
        // Implementation for serializing objects
    }

    // Other utility methods
}
```

## Code Examples

### Example 1: Using Common Utility Functions

```csharp
using Syncfusion.Windows.Forms.Common;

// Example usage of the CommonUtility class
void ProcessData()
{
    var dataObject = new DataObject();
    // Populate dataObject with data

    CommonUtility.FormatDataObject(dataObject);

    // Serialize the data object to a file
    CommonUtility.SerializeObject(dataObject, "C:\\Data\\Backup.dat");
}
```

### Example 2: Integrating Common Components

```csharp
using Syncfusion.Windows.Forms.Common;

// Example of using a common component
void InitializeCommonComponent()
{
    // Instantiate a common component
    var component = new CommonComponent();
    
    // Configure properties
    component.Property1 = "Value1";
    component.Property2 = true;

    // Add the component to the form
    this.Controls.Add(component);
}
```

## Cross References

See also:
- **Syncfusion Winforms Documentation**
- **Essential Studio Overview**
- **Other Volume Documentation for Version 11.4.0.26**

## RAG Annotations
<!-- tags: [winforms, essential-studio, common-utilities, volume-4, 11.4.0.26] keywords: [Syncfusion, Winforms, common components, utility classes, data object formatting, serialization, integration, controls] -->
```

---

<!-- 페이지 2 -->

```html
<!--\
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_005.jpeg
document_name: common
page_number: 005
page_id: common#page_005
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:05Z
fidelity: lossless
-->

# Essential Common

The following table defines the conventions used in the documentation:

| Convention Name | Explanation | Description |
|------------------|-------------|-------------|
| Bold            | The Open dialog | UI elements such as names of tabs, menus, buttons, dialog boxes, and windows will be set to bold. |
| Italic          | The IsEnable property | The property, method, and event name and text that must be typed exactly as shown will be italicized. |
| Plus sign       | Ctrl+Click | Represents a combination of keys. |
| Version number  | x.x.x.x | Represents version number. This should be replaced with the version installed on the user's machine. |
| Note            | [Note:](./Note.svg) | Represents important information. |
| Example         | Example | Represents an example. |
| Tip             | [Tip:](./Tip.svg) | Represents useful hints that will help you in using the controls/features. |
| Additional Information | [Additional Information:](./AdditionalInformation.svg) | Represents additional information on the topic. |

## 1.2 Minimum software requirements

The following are the system requirements for Essential Studio:

| Operating System | All windows and client server |
|-------------------|--------------------------------|
| .NET Framework versions | 4.0 or higher |
| Visual Studio | 2005 or higher |
| MVC | MVC3 or higher |
| Silverlight | Silverlight 4 or higher |
| Windows Phone SDK | Windows 7 - Windows Phone SDK v7.1<br>Windows 8 - Windows Phone SDK v7.1 or higher |

<!-- tags: [product, Essential Studio, system requirements, software requirements] keywords: [Operating System, .NET Framework, Visual Studio, MVC, Silverlight, Windows Phone SDK, Windows] -->
```

---

<!-- 페이지 3 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_009.jpeg
document_name: common
page_number: 009
page_id: common#page_009
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:17Z
fidelity: lossless
-->

# Essential Common

## Overview
- Installation folder configuration for Syncfusion Essential Studio.
- Steps to choose installation and samples locations.
- Option to uninstall previously installed Syncfusion assemblies from the Global Assembly Cache (GAC).

## Content

### Installation Folder

| Version: 11.1.0.21 Date: 01/30/2013 |
| --- |
| **Installation Location** |
| C:\Program Files (x86)\Syncfusion\Essential Studio\11.1.0.21\ |
| **Samples Location** |
| C:\Users\Kannanns\AppData\Local\Syncfusion\EssentialStudio\11.1.0.21\ |
| ☐ Uninstall previously installed Syncfusion assemblies from GAC. |

**Figure 4: Installation Folder**

**Note:** You can also browse to choose a location by clicking **Browse**. If you have already installed any other respective version setup, you will not be able to change the install path.

### Installation Steps

1. **Uninstall GAC Assemblies:**  
   Select the **Uninstall previously installed Syncfusion assemblies from GAC** check box if you want to uninstall the previously installed Syncfusion assemblies from GAC. Unselect this if you want to maintain the previously installed assemblies.

2. **Install Default Location:**  
   To install in the displayed default location, click **Next**.

3. **Select Platforms:**  
   Select the platforms to install.

---

## Code Examples

No code examples provided in this section.

---

## Page-level Navigation/TOC

- Overview
- Content
  - Installation Folder
  - Installation Steps

---

## Cross References

- Refer to the section on "Uninstalling Assemblies" for more details on GAC operations.

---

<!-- tags: [syncfusion, winforms, installation, essential studio] keywords: [installation folder, samples location, gac, uninstall assemblies, platform selection] -->
```

---

<!-- 페이지 4 -->

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

---

<!-- 페이지 5 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_017.jpeg
document_name: common
page_number: 017
page_id: common#page_017
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:50Z
fidelity: lossless
-->

# Essential Common

## Overview
- Setup instructions for Syncfusion Mobile MVC installation.
- Specifies installation directory paths.
- Option to uninstall previously installed Syncfusion assemblies.

## Installation Folder

### Installation Location
- **Installation Location**: 
  - Path: `C:\Program Files (x86)\Syncfusion\Essential Studio\11.1.0.21\`
- **Samples Location**: 
  - Path: `C:\Users\Kannanns\AppData\Local\Syncfusion\EssentialStudio\11.1.0.21\`

### Uninstallation Option
- **Uninstall previously installed Syncfusion assemblies from GAC**: 
  - Check box option to uninstall previous assemblies if desired.

### Action Buttons
- **BACK**: Returns to the previous step.
- **INSTALL**: Initiates the installation process at the displayed default location.

## Note
You can also browse to choose a location by clicking Browse. If you already installed any other platform setup, it won't allow you to change the install path again.

## Steps for Installation
1. **Select Uninstall Previously Installed Syncfusion Assemblies from GAC**: 
   - If you want to uninstall the previously installed Syncfusion assemblies from GAC, select this box. Do not select if you wish to maintain the previously installed assemblies.
2. **Install at the Displayed Default Location**: 
   - Click Install to proceed with the installation.

## API Reference (if applicable)
- None explicitly mentioned in the provided content.

## Code Examples (multi-language supported)
- No code examples provided in the screenshot.

## RAG Annotations
<!-- tags: [product, installation, uninstallation, syncfusion, mobile MVC, GAC] keywords: [installation folder, samples location, uninstall previously installed assemblies, syncfusion assemblies, GAC, essential common, syncfusion winforms, 11.4.0.26] -->
```

---

<!-- 페이지 6 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: common
page_number: 021
page_id: common#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:05Z
fidelity: lossless
-->

# 1.5 Source code

## Overview

After 9.4.0.62, Essential Studio Source has been removed from the product setup. To access the source code, install the Essential Studio Source Code Add-on Setup. You can access the Essential Studio Source Code Add-on Setup from the dashboard. You can also access it from the Product Downloads and Keys page using your support account in Direct-Trac.

## 1.5.2 Step-by-Step Installation

The following steps show how to install the Essential Studio Source Code Add-on Setup.

### Installation Steps

1. Double-click the Syncfusion Essential Studio Source code add-on installer setup file. The Syncfusion Essential Studio Source Installer wizard opens.

   ![Unified Installer](insert_image_here "Figure 14: Unified Installer")

   *Figure 14: Unified Installer*

2. Click Next.

<!-- tags: [source code, essential studio, installation, add-on] keywords: [source code, essential studio, installation, add-on setup, syncfusion, 9.4.0.62] -->
```

---

<!-- 페이지 7 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_025.jpeg
document_name: common
page_number: 025
page_id: common#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:14Z
fidelity: lossless
-->

# Essential Common

## Overview
- The page presents the initial setup screen for the Syncfusion Essential Studio Source code add-on.
- It guides users through the installation process, highlighting the steps involved.
- The License Agreement is introduced as the next step after the initial setup wizard.

## Content

### Syncfusion Essential Studio Source Code Add-on 2013 Vol 1 Setup

#### Welcome Screen
The installation wizard introduces the Syncfusion Essential Studio. The following steps are outlined:

1. **Welcome**  
   - Thank you for the information provided. Authorized features have been unlocked.
   - The Setup Wizard has the necessary information to proceed with installation.

2. **Collecting Information**  
   - This step involves gathering details required for installation.

3. **Installing**  
   - The actual installation process will occur here.

4. **Completed**  
   - Upon successful completion, the installer will indicate that the setup is finished.

- **Date:** 27/02/2013
- **Version:** 11.1.0.21

#### Instructions for Proceeding
The user is prompted to:
- Click **Next** to continue with the installation process.
- Click **Back** to return to the previous screen.
- Click **Cancel** to exit the Setup Wizard.

### Steps to Proceed

7. Click **Next**. The License Agreement screen opens.

## Code Examples

API Reference and code examples are not present on this page.

## Cross References

See also: Installation, License Agreement, Setup Wizard

## RAG Annotations

<!-- tags: [installation, license agreement, setup wizard, version 2013] keywords: [Syncfusion Essential Studio, Source code add-on, authenticated features, installation process, setup] -->
```

---

<!-- 페이지 8 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_029.jpeg
document_name: common
page_number: 029
page_id: common#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:26Z
fidelity: lossless
-->

## Essential Common

### Overview

- This page documents the installation process for the Essential Studio Source Code Add-on.
- Provides steps for configuring and installing the add-on.
- Highlights the functionality of essential studio components, emphasizing ease of use.

### Content

#### Installation Process

<figure>
<div align="center">
**Syncfusion Essential Studio Source code add-on installer Setup**
</div>
- **Welcome (Step 1)**: The installation process begins with a welcome screen.
- **Collecting Information (Step 2)**: The installer collects necessary data for the installation.
- **Installing (Step 3)**: The installation process starts, with a status bar indicating the progress (approximately 5 minutes).
- **Completed (Step 4)**: The installation process ends with a completed screen.

![](image.png)  
**Figure 22: Installing Essential Studio Source Code**

**Note:** The Completed screen is displayed once the selected package is installed.

### Essential Studio Components

- The image depicts several components:  
  - **Orange Book**: Essential Studio Enterprise
  - **Purple Book**: Essential Studio
  - **Green Book**: Essential Studio
  - **Blue Book**: Essential Studio

#### Key Features
- Hundreds of controls to simplify development and user experience.
- Dependencies and integrations are managed during the installation process.

#### Success Indicators
- Successful installation is confirmed upon reaching the completed screen.

### Code Example

#### Setting Up Source Code Add-on
While the image does not include specific code snippets, users should ensure proper configuration of the setup environment before initiating the installation.

### API Reference

#### Installation Status
- **Status:** The status bar visually indicates the progress of the installation process.  
  This ensures the user is aware of the current stage in the setup.

### Page-Level Navigation/TOC
- Overview
- Content
  - Installation Process
  - Essential Studio Components
  - Key Features
  - Success Indicators
  - Code Example
  - API Reference

<!-- tags: [Essential Studio, Source Code Add-on, Installation, WinForms] keywords: [Syncfusion, Essential Studio, Source Code Add-on, Installation Progress, Components] -->
```

---

<!-- 페이지 9 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_033.jpeg
document_name: common
page_number: 033
page_id: common#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:40Z
fidelity: lossless
-->

## Overview

- This page discusses the availability of both **online** and **local documentation** for Syncfusion products.
- It explains how to access the **offline user guide** through the **Utilities > Documentation** menu.
- Guidance is provided for users on how to install or download local documentation if it is not already installed.

## Content

### Online Documentation

We have provided comprehensive documentation online to help you better understand our products.

- **User Guide**: Provides a step-by-step introduction and instructions for using the product.
- **Class Reference**: Detailed reference of all classes, methods, and properties used in the product.

### Local Documentation

Documentation pertaining to our products can be installed with your copy of Syncfusion's local resources. Explore the three categories of documentation to have a better idea of our products.

- **VS2005/VS2008 Class Reference and User Guide**
- **VS2010 Class Reference**
- **VS2010 User Guide**

#### Offline User Guide

**Figure 26: Offline User Guide**

![](https://example.com/image_url) <!-- Placeholder for the image shown in the document -->

**Note**: If you not installed local documentation, then prompt will open to download the setup.

### Online Documentation

**Syncfusion provides comprehensive documentation online to help you understand Essential Studio product better. This can be accessed from the Utilities > Documentation > Online Documentation.**

## API Reference

### Getting Started with Offline Documentation
- **Installation**: Ensure local documentation is installed with your Syncfusion product copy.
- **Access**: Navigate through the utilities menu to access the user guide and class reference for different Visual Studio versions.

### Local Documentation Setup
- **VS2005 and VS2008**: Contains documentation references for these specific versions.
- **VS2010**: Includes both class reference and user guide tailored for VS2010.

## Code Examples

### Retrieving Documentation Context
```csharp
// Example: Accessing Documentation
public void AccessDocumentation()
{
    // Navigate to local documentation via Syncfusion Utility Menu
    var documentationPath = "Utilities\\Documentation\\Local Documentation";
    // Open the required documentation file
    Process.Start(documentationPath);
}
```

## Page-level Navigation/TOC

- **Online Documentation**
  - User Guide
  - Class Reference
- **Local Documentation**
  - Installation and Setup
  - Accessing User Guide
  - Class Reference

## Cross References

See also:
- **Syncfusion Product Documentation**: For a complete overview of available resources.
- **Syncfusion Website**: For support and updates.

<!-- tags: [syncfusion, winforms, essential studio, documentation, version 11.4.0.26] keywords: [online documentation, local documentation, user guide, class reference, winforms, syncfusion, essential studio] -->
```

---

<!-- 페이지 10 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: common
page_number: 037
page_id: common#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:56Z
fidelity: lossless
-->

# Essential Common

## Overview
- Steps for setting up the Syncfusion Essential Studio Link Install.
- Welcome screen and initial setup options.
- Guidance on selecting Build Machine or Production Machine.

## Content

### Installation Process

#### Step 2: Unzip Completion

On completion of the unzip operation, the Setup - Syncfusion Essential Studio Link Install dialog box opens.

```html
<figure>
  <img src="Syncfusion_Essential_Studio_Link_Install_Screen.png" alt="Figure 28: Extracting Setup">
  <caption>Figure 28: Extracting Setup</caption>
</figure>
```

#### Step 3: Welcome Screen

The following welcome screen appears:

```html
<figure>
  <img src="Syncfusion_Essential_Studio_Link_Welcome_Screen.png" alt="Figure 29: Welcome Screen">
  <caption>Figure 29: Welcome Screen</caption>
</figure>
```

##### Dialog Content
- **Title**: Welcome to the Syncfusion Essential Studio Link Install 2013 Vol. 1 Setup
- **Options**:
  - Build Machine
  - Production Machine
- **Information**:
  - The Setup Wizard will install Essential Studio assemblies on your computer.
  - Click "Next" to continue or "Cancel" to exit the Setup Wizard.
- **Version**: 11.1.0.21
- **Date**: 19/02/2013

#### Step 3: Select Machine Type

**Select Build Machine or Production Machine as required.**

**Note**: Select Build Machine to configure assemblies in development machine. Select Production Machine to configure assemblies in server machine.

#### Step 4: User Information Screen

Click Next. The User Information screen opens.

---

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, installation, setup, Build Machine, Production Machine, Version 11.1.0.21] keywords: [Syncfusion Essential Studio, Link Install, Development Machine, Server Machine, User Information] -->
```

---

<!-- 페이지 11 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: common
page_number: 041
page_id: common#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:09Z
fidelity: lossless
-->

# Essential Common

## Overview
- Screenshots and instructions for setting up the installation folder for Syncfusion Essential Studio.
- Step-by-step guide through the installation process, detailing how to choose options for installation.
- Provides the option to install assemblies to the Global Assembly Cache (GAC).

## Content

### Installation Folder Selection

#### Figure: Select the Installation Folder screen
- **Welcome**
- **Collecting Information**
- **Installing**
- **Completed**

**Figure 33: Select the Installation Folder screen**

1. To install in the displayed default location, click `Next`.

**Note**: You can also browse to choose a location by clicking *Browse*.

2. Select **Do you want the assemblies to be installed to GAC?** to install the assemblies in the GAC.
3. Click `Next`. The *Ready to Install* dialog opens.

## API Reference (if applicable)
- No specific API reference is provided in this section.

## Code Examples (if applicable)
- No code examples are present in this section.

## Cross References
- Refer to the Syncfusion documentation for more detailed information on installation procedures.

<!-- tags: [syncfusion, essential studio, installation, setup, gac] keywords: [installation folder, global assembly cache, gac, essential studio, setup wizard] -->
```

---

<!-- 페이지 12 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_045.jpeg
document_name: common
page_number: 045
page_id: common#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:19Z
fidelity: lossless
-->

# Essential Common

## Overview
- Guides through the setup process of Syncfusion Essential Studio Digitally Signed Assemblies.
- Describes the steps involved in extracting and initiating the installation.
- Highlights the welcome screen for the Syncfusion Essential Studio installation.

## Content

### Installation Process

#### Step 1: Extracting Setup

The first step in the installation process involves extracting the setup files. This is illustrated in **Figure 37: Extracting Setup**.

**Figure 37: Extracting Setup**

On completion of the unzip operation, the **Setup - Syncfusion Essential Studio Digitally Signed Assemblies** dialog box opens, as shown below.

---

#### Step 2: Welcome Screen

After the extraction is complete, the Welcome Screen appears, guiding the user through the installation process. The screen provides an overview of the setup steps and version details. Refer to **Figure 38: Welcome Screen** for more details.

**Figure 38: Welcome Screen**

- **Welcome Screen Layout**:
  - **Header**: Displays the Syncfusion logo and version information ("Essential Studio 2013 Vol 1").
  - **Setup Steps**: Lists the four main steps of the installation:
    1. Welcome
    2. Collecting Information
    3. Installing
    4. Completed
  - **Information Panel**: Provides a brief description of the current step, prompting the user to click "Next" to proceed.

---

#### Step 3: User Information Screen

After clicking "Next" on the Welcome Screen, the User Information screen opens, where users can provide additional details as part of the installation process.

### Figures

1. **Figure 37: Extracting Setup**
2. **Figure 38: Welcome Screen**

## RAG Annotations

<!-- tags: [syncfusion, setup, installation, essential studio, digitally signed assemblies] keywords: [installation process, welcome screen, unzip operation, setup steps, user information screen] -->
```

---

<!-- 페이지 13 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: common
page_number: 049
page_id: common#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:32Z
fidelity: lossless
-->

## Essential Common

### Installation Overview

- The installation process involves selecting the installation folder for the **Syncfusion Essential Studio 2013 Vol 1**.
- The installation folder defaults to `C:\Program Files (x86)\Syncfusion\Essential Studio\Digitally Signed As`, but it can be changed using the **Browse...** button.
- The setup proceeds through four stages: **Welcome**, **Collecting Information**, **Installing**, and **Completed**.

### Installation Steps

1. **Welcome**: Initial welcome screen to prepare for installation.
2. **Collecting Information**: Step to specify the installation location.
   - **Folder**: The field where the installation path can be entered or selected.
   - **Browse...**: Option to navigate and select a different installation location.
3. **Installing**: The installation process will commence after confirming the details.
4. **Completed**: The final confirmation once the installation is finished.

#### Figure 42: Select the Installation Folder screen

- **Note**: You can also browse to choose a location by clicking **Browse**.

```plaintext
9. Click Next. The setup type screen opens.
```

### Additional Details

- **Installation Date**: 19/02/2013
- **Version**: 11.1.0.21

## Summary

This page outlines the procedure for selecting and confirming the installation folder for the **Syncfusion Essential Studio 2013 Vol 1** application. The user is guided through the setup process, allowing them to customize the installation path and proceed with the installation.

<!-- tags: [syncfusion-sdk, winforms, installation, essential-studio] keywords: [installation-folder, browse, windows, vol-1, setup-type, 2013] -->
```

---

<!-- 페이지 14 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: common
page_number: 053
page_id: common#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:44Z
fidelity: lossless
-->

## Overview
- Steps to complete the installation of Essential Studio Digitally Signed Assemblies 2013 Vol 1.
- Instructions to exit the Setup Wizard after the assembly installation is complete.
- Explanation of Syncfusion's patch setup for adding new features or fixing issues.

## Content

### Essential Studio Digitally Signed Assemblies Installation

#### Figure 46: Installation Completed
![Syncfusion Essential Studio Digitally Signed Assemblies Installation Screenshot](syncfusion_installation.png)

The installation process is complete. The final step in the installation wizard is as follows:

12. Click **Finish** to exit the Setup Wizard. Assemblies will be installed.

### 1.9 Patches

#### Overview of Patches

Syncfusion provides patch setup to install a new assembly, either to add new features or to fix issues.

##### 1.9.1 Installing a Patch Setup

The following procedure illustrates how to install a patch:

**Note:** Before installing the patch, ensure that the Essential Studio version corresponding to the patch is installed on your machine.

---

## API Reference
- None applicable in this section.

## Code Examples
- None applicable in this section.

## Page-level Navigation/TOC
- None applicable in this section.

## Cross References
- None applicable in this section.

<!-- tags: [syncfusion, essential-studio, digitally-signed-assemblies, installation, patches, setup-wizard, 2013 vol 1] keywords: [install, syncfusion setup, patch installation, essential studio] -->
```

---

<!-- 페이지 15 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_057.jpeg
document_name: common
page_number: 057
page_id: common#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:55Z
fidelity: lossless
-->

# Essential Common

## Overview

- Installing the Syncfusion Essential Studio Service Pack 
- Detailed steps for precompiled assemblies backup
- Process involved in updating precompiled assemblies

## Content

### Installation Process

#### Figure 50: Installing

The screenshot displays the installation interface of the Syncfusion Essential Studio Service Pack 11.1.0.21. It indicates that the setup is currently taking a backup of the precompiled assemblies from the installed location. The progress bar shows the ongoing progress, and a `Cancel` button is available for user interaction.

**Note:** The patch will be installed on your computer, and a dialog box will appear when the installation is completed.

This section provides a visual representation of the installation process and clarifies the steps and expected outcomes, ensuring a smooth and informed setup experience.

## Page-level Navigation/TOC (if applicable)

- Installation Process
  - Figure 50: Installing
  - Notes on installation completion

## Cross References

See also:
- Documentation for Syncfusion Essential Studio
- Backing up precompiled assemblies

## RAG Annotations

<!-- tags: [syncfusion-sdk, syncfusion-winforms, install-process, precompiled-assemblies, version-11.4.0.26] keywords: [installation, precompiled assemblies, backup, patch installation, service pack, dialog box, setup interface] -->
```


---

<!-- 페이지 16 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: common
page_number: 061
page_id: common#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:08Z
fidelity: lossless
-->

# Essential Common

Note: You need to install Syncfusion Essential Studio of the same version and Mercury QuickTestProfessional before installing this add-on.

## 1.11 CAB Add-on

The Syncfusion Essential CAB Enabling Kit provides extensible support for working with CAB easily. It helps developers to enhance the look and feel of their applications as well as speed up the development process with customizable UIs. The workspaces are components or controls that encapsulate visual effects and layout strategies without affecting the business logic.

The Essential CAB Enabling Kit offers the following workspaces and UI Elements:

### Workspaces
- Dockable Workspace
- DockingClientPanel Workspace
- GroupBar Workspace
- PopupControlContainer Workspace
- SplashPanel Workspace
- SplitContainerAdv Workspace
- TabControlAdv Workspace
- TabbedMDIManagerWorkspace
- XPTaskPane workspace

### UI Elements
- XP Menus
- TreeViewAdv
- StatusBarAdv
- StatusStripEx
- ContextMenuStripEx
- RibbonControlAdv
- XPTaskBar

### Pre-Requisites
- Visual Studio 2005/2008
- Microsoft Composite UI Application Block Framework
- Syncfusion Essential Studio (Essential Tools – Windows Forms)

## 1.12 Samples

Providing the online and offline samples.
```


<!-- tags: [syncfusion-sdk, CAB Add-on, UI Elements, WinForms, version 11.4.0.26] keywords: [Syncfusion Essential CAB Enabling Kit, Dockable Workspace, DockingClientPanel Workspace, GroupBar Workspace, PopupControlContainer Workspace, SplashPanel Workspace, SplitContainerAdv Workspace, TabControlAdv Workspace, TabbedMDIManagerWorkspace, XPTaskPane workspace, XP Menus, TreeViewAdv, StatusBarAdv, StatusStripEx, ContextMenuStripEx, RibbonControlAdv, XPTaskBar, Visual Studio, Microsoft Composite UI Application Block Framework, Offline Samples, Online Samples] -->

---

<!-- 페이지 17 -->

```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_065.jpeg
document_name: common
page_number: 065
page_id: common#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:21Z
fidelity: lossless
-->

# Essential Common

## Overview
- Describes user interface components for creating interactive ASP.NET MVC mobile applications and WPF applications.
- Lists tools and controls available for mobile and desktop platforms.

## Content

### Mobile MVC

#### Tools for Mobile

The **Essential Tools Mobile** is a collection of professional user interface components designed to create interactive ASP.NET MVC mobile applications. Key features include:
- Dialog, ListBox, Menu, Tab, ToolBar, ScrollPanel, Auto-complete text box, Button, Rating, Header, Footer, and Waiting Popup.
- Extensive client-side and server-side support.
- View-side customization for all components.
- Built-in Skins support for all components.
- Support for W3C-XHTML and W3C-CSS.
- Supports all browsers that support HTML 5.

**Figure 56: Essential Studio Mobile MVC Sample Browser**

![Figure 56: Essential Studio Mobile MVC Sample Browser](#)

### WPF

#### Tools for WPF

The **Essential Tools WPF** is a collection of UI components for the WPF framework, designed to create robust and appealing UI applications with full customization through templates. Essential Tools also includes extensive UI controls for building real-world WPF applications with docking and Office 2007/2010-style ribbons.

**Figure 57: Essential Studio WPF Sample Browser**

![Figure 57: Essential Studio WPF Sample Browser](#)

- **Tools**
  - Product Showcase
  - Docking Manager
  - Ribbon
  - RichTextBox
  - Tree View
  - Multicolumn Tree View
  - Editor Controls
  - PropertyGrid
  - Menu Control
  - ToolBar/Adv
  - Busy Indicator
  - Button Controls
  - Tab Controls
  - TabNavigation
- **Featured Samples**
  - Portfolio Analyser
  - Localization Demo
  - Office UI
  - Windows Explorer Demo
  - Registration Form
  - Menu Merging
  - Lazy Loading

### Silverlight

12. Silverlight

## API Reference (if applicable)

<!-- This page does not contain specific API references. -->

## Code Examples (if applicable)

<!-- This page does not contain specific code examples. -->

## Page-level Navigation/TOC (if applicable)

<!-- This page does not contain a local Table of Contents. -->

## Cross References

See also:
- **Essential Studio Mobile MVC Sample Browser**
- **Essential Studio WPF Sample Browser**

<!-- tags: [essential tools, mobile mvc, wpf, silverlight, user interface components, syncfusion, version: 11.4.0.26] keywords: [mobile, desktop, tools, controls, interactive applications, w3c-standards, html5, ui components, cortical-ui, w3c-xhtml, w3c-css] -->
```

---

<!-- 페이지 18 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_069.jpeg
document_name: common
page_number: 069
page_id: common#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:40Z
fidelity: lossless
-->

## WinForms: Essential Studio Sample Browser

### Overview
- Showcase of Essential Studio for WinRT XAML with various sample applications.
- Detailed online samples for various platforms including ASP.NET, ASP.NET MVC, Mobile MVC, Silverlight, Windows Phone, WinRT, and WPF.

### Content

#### Showcase

![Figure: Essential Studio WinRT Sample Browser](#)
*Figure 61: Essential Studio WinRT Sample Browser*

The figure above illustrates a variety of sample applications provided by Essential Studio for WinRT XAML, including:
- Patient Monitor
- Weather Analysis
- Airline Reservation
- Car Dashboard
- Invoice Generator
- Document Viewer
- SSRS Report Viewer
- Organizational Chart
- Sales Analysis
- Unit Diagram

#### 1.12.2 Online Samples

##### Overview
Online samples are provided for the ASP.NET, ASP.NET MVC, Mobile MVC, Silverlight, Windows Phone, WinRT, and WPF platforms.

##### Links to Online Samples

The table below lists the links to the online samples.

| Platform        | Online link                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| ASP.NET         | [http://asp.syncfusion.com/demos](http://asp.syncfusion.com/demos)         |
| ASP.NET MVC     | [http://mvc.syncfusion.com/demos/ui/grid](http://mvc.syncfusion.com/demos/ui/grid)    |
| Mobile MVC      | [http://mvc.syncfusion.com/demos/ui/mob](http://mvc.syncfusion.com/demos/ui/mob)      |
| Silverlight     | [http://silverlight.syncfusion.com/samples/silverlight/](http://silverlight.syncfusion.com/samples/silverlight/) |
| Windows Phone   | [http://www.syncfusion.com/products/windows-phone](http://www.syncfusion.com/products/windows-phone) |
| WinRT           | [http://www.syncfusion.com/products/winrt](http://www.syncfusion.com/products/winrt) |

#### Cross References
- **Online Sample Access**: Links to detailed online samples for various platforms.

### RAG Annotations
<!-- tags: [Essential Studio, WinRT, XAML, sample browser, online samples, platforms] keywords: [WinRT, XAML, sample applications, online samples, ASP.NET, ASP.NET MVC, Mobile MVC, Silverlight, Windows Phone, WinRT, WPF] -->
```

---

<!-- 페이지 19 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_073.jpeg
document_name: common
page_number: 073
page_id: common#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:54Z
fidelity: lossless
-->

## Updates

The "Updates" section will show you the latest version availability of Syncfusion Essential Studio.

### Figure 67: Updates

![](attachment://EssentialStudioUpdates.png)

The image indicates:

- Your current version of Essential Studio is v10.4.0.67.
- A new version of Essential Studio is available: v11.1.0.21.

## Product Platforms

This section allows you to access the product samples available for each platform.

### Figure 68: Platforms

![](attachment://EssentialStudioPlatforms.png)

The available platforms include:

- ASP.NET MVC
- ASP.NET
- Windows Forms
- WPF
- Silverlight
- Windows Phone
- Mobile MVC
- WinRT

## Accessing Product Samples

Syncfusion provides numerous online and local samples to help you better understand the controls. You can access these samples by following the steps below:

1. **Open the Syncfusion Dashboard.**

---
<!-- tags: [product, module, control, api, version?] keywords: [Essential Studio, Updates, Product Platforms, Accessing Product Samples] -->
```

---

<!-- 페이지 20 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_077.jpeg
document_name: common
page_number: 077
page_id: common#page_077
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:04Z
fidelity: lossless
--> 

## Essential Common

- **Documentation** - This provides access to view the online documentation and installed documentation.
- **License Manager** - This allows you to manage the licensing information such as the validity of license key and also the products that are licensed with this key.
- **License Agreement** – This allows you to navigate to the Software License Agreement.

### Other Information

Other information available in the dashboard includes:

- **Messages** - This section allows you to view the user registration information, i.e. whether the user is registered or not.

![Message](image.png)

*Figure 72: Message*

- **Sales FAQ** - Clicking this link directs you to FAQ page, which lists common sales-related queries and other sales contact information.
- **Contact Support** - Clicking this link directs you to Direct-Trac Login page to contact our support team.

## 1.13.2 Assembly Manager

The Assembly Manager is used to install and uninstall the assemblies to and from the GAC and Public Assemblies folder under the installed location. It is used to install and uninstall the assemblies into the GAC.

### Launching the Assembly Manager

Use the following steps to run the Assembly Manager:

1. Open the Syncfusion Dashboard.
2. Click **Utilities > Assembly Management**.
3. Click **Launch** button for **Assembly Manager**.

```

---

<!-- 페이지 21 -->

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

---

<!-- 페이지 22 -->

```md
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_085.jpeg
document_name: common
page_number: 085
page_id: common#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:29Z
fidelity: lossless
-->

## Essential Common

### Overview
- Instructions on using the Syncfusion Build Manager.
- Settings for configuring the architecture and dependencies for building Syncfusion assemblies.
- Explanation of the sections in the Build Manager window.

### Content

#### Figure 78: Syncfusion Essential Studio Build Manager

**Build Manager Settings:**
This window contains seven sections.

**1. Framework Version**
- Select one of the following .NET versions:
  - .NET 2.0
  - .NET 3.5
  - .NET 4.0
  - .NET 4.5 (selected in the image)

**2. PlatformType**
- Choose one of the following options:
  - All
  - Base
  - Windows
  - Web
  - WPF
  - MVC
  - Silverlight
  - Mobile Web
  - WinRT

**3. Product**
- Select the product or choose "All" from the dropdown menu.

**4. Assembly Type**
- Choose between:
  - Debug
  - Release

**5. Dependencies**
- Use PreBuilt
- Use Dependencies (checkbox)

**6. Strong Key**
- Use Strong Key (checkbox)
- Choose File button to specify a file

**7. Output**
- Displays build-related information and status messages.

**Buttons Available**
- Perform Build
- Copy Output
- View Log(s)
- Launch Assembly Manager
- Exit

### Steps for Configuration

1. Open the Syncfusion Essential Studio Build Manager.
2. Select the required settings in the Build Manager window.
3. Use the various sections to configure the build parameters as needed.

### Build Manager Settings

**This window contains seven sections:**

**Framework Version**
- Define the .NET framework version to use for the build process.

#### Page-level Navigation/TOC (if applicable)
- None

#### See also:
- Syncfusion Build Manager documentation
- .NET Framework versions
- Platform and product dependencies

<!-- tags: [syncfusion-sdk, build-manager, windows, .net-framework] keywords: [syncfusion, build, framework version, dependencies, strong key, output, perform build, copy output, view logs, launch assembly manager, exit] -->
```

---

<!-- 페이지 23 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_089.jpeg
document_name: common
page_number: 089
page_id: common#page_089
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:45Z
fidelity: lossless
-->

## Overview
- Adding and managing product keys in the Syncfusion License Manager.
- Extending evaluation periods and unlocking additional products using product keys.
- Steps to remove a license key from the License Manager.

## Content

### Key Management in Syncfusion License Manager

4. Click **OK**. The entered key will be displayed in the log.

#### License Key Details
- **Key**:
  ```
  @exampleKey555Examplekey555exampleKey555ExampleKey555
  ```
- **Version**: Essential Studio version 11.1.0.*
- **Licensed Products**:
  - Syncfusion Essential Aspnet Binary
  - Syncfusion Essential Aspnetmvc Binary
  - Syncfusion Infrastructure Library Core
  - Syncfusion Essential Mobilemvc Binary
  - Syncfusion Infrastructure Library Shared
  - Syncfusion Essential Silverlight Binary
  - Syncfusion Essential Windowsfoms Binary
  - Syncfusion Essential Windowsphone Binary
  - Syncfusion Essential Wint Binary
  - Syncfusion Essential Wpf Binary

**Diagnostic: Email Checksum = Hc642**

#### Figure: Key Added
![Figure 82: Key Added](#figure-82-key-added)

By adding an additional product key, you can also:
- Extend evaluation period (applicable for evaluation versions of Essential Studio).
- Unlock additional products.

#### Removing a Product Key

**Removing a Product Key**

This option allows you to remove a product key from the License Manager window. It allows you to remove an incorrectly added or old license key.

**The following are the steps to remove a license key:**

1. Open the **Syncfusion License Manager** dialog.
2. Select the key to be removed. The selected key will be highlighted.

## References

© 2013 Syncfusion. All rights reserved.

<!-- tags: [license-manager, product-key, essential-studio, evaluation-version, unlocking-products, key-removal, license-management] keywords: [license manager, product key, essential studio, evaluation, unlocking, key removal, license management] -->
```

---

<!-- 페이지 24 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_093.jpeg
document_name: common
page_number: 093
page_id: common#page_093
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:59Z
fidelity: lossless
-->

## Overview
- This section explains the configuration of controls in the Toolbox and introduces the Multi-Target Manager utility in Syncfusion WinForms.
- Guides users on reseting the toolbox if the installed controls are not properly reflected and outlines the utility's limitations based on framework versions.
- Explains the utility of using Multi-Target Manager in Visual Studio 2008 and its role in managing multiple framework versions.

## Content

### Toolbox Configuration

The Syncfusion Toolbox Installer ensures the correct configuration of controls in the Toolbox. Here is an information window indicating successful configuration:

**Figure 86: Information**

**Note:**
- You need to reset the toolbox if the installed controls are not reflected properly in the Toolbox.
- This tool will configure only the controls which are located under Installed Location] \Assemblies \ [Framework version].

### **1.13.6 Multi-Target Manager**

#### Overview
MultiTarget Manager helps in managing multiple .NET frameworks in your Visual Studio 2008 project, i.e., switching between multiple frameworks.

**Note:**
This is not essential for VS 2010 because Common Language Runtime (CLR) is different for both the 3.5 and 4.0 frameworks. VS 2010 selects the required .NET framework assembly for the corresponding projects. 3.5 and 4.0 are the only frameworks configured; the MultiTarget Manager utility allows you to work on framework 2.0 with VS 2010.

#### When to Use Multi-Target Manager?
When Essential Studio is installed in a machine comprising both 2.0 and 3.5 frameworks, then by default the target framework is set to 3.5 and the following registry entry AssemblyFoldersEx is also set to 3.5 assemblies. You can use the Multi-Target Manager to change the target framework to 2.0.

#### Registry Key
The registry key involved is:

```
HKLM\Software\Microsoft\.NetFramework\v2.0.50727\AssemblyFoldersEx\Syncfusion Essential Studio 3.5
```

#### Launching MultiTarget Manager
1. Open the Syncfusion Dashboard.
2. Click Utilities > Assembly Management.
3. Click the **Launch** button for Multi-Target Manager.

## References
- [Syncfusion Documentation]
- [Visual Studio 2008 and 2010 Frameworks]
- [Multi-Target Manager Usage]

<!-- tags: [syncfusion, winforms, multiframe, toolbox, multi-target] keywords: [syncfusion winforms, multiframe support, toolbox configuration, vs2008, vs2010, multitargeting, assembly management] -->
```

---

<!-- 페이지 25 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_097.jpeg
document_name: common
page_number: 097
page_id: common#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:14Z
fidelity: lossless
-->

# Essential Common

1. Open the command prompt in administrator mode and navigate to the following location:  
   {Installed Drive}\{ProgramFiles Folder}\Syncfusion\Essential Studio\{version}\Utilities\Project Migration\  
   Eg: C:\Program Files (x86)\Syncfusion\Essential Studio\11.3.0.30\Utilities\Project Migration\  

2. Run the `ProjectMigrationConsole.exe` with the following arguments:  
   `/source:"sourcepath" /studio:"Essential Studio version" /framework:"[v3.5] / [v2.0] / [v4.0] / [v4.5]" /backup:"Backupfolderpath" /hintpath:"[False] / [True]"`  
   Eg: `/source:"C:\Users\Vadivel\Documents\Visual Studio 2012\Projects\WindowsFormsApplication3" /studio:"11.2.0.25" /framework:"v4.0" /backup:"E:\ProjectMigrationBackup\WindowsFormsApplication3" /hintpath:"False"`

The following screen shot illustrates this.  

[Image description: The image is cropped or is empty. Please refer to the original document.]

## 1.13.8 Project Templates

Syncfusion provides Project Templates for the ASP.NET MVC platform to automatically refer the necessary reference and resource files in an application. However, this is not applicable to other platforms. In the other platforms (such as Windows Forms, WPF, Silverlight, and ASP.NET), the Syncfusion controls will be automatically configured in the Microsoft Visual Studio Toolbox after the setup has been installed, and the controls can be used in the application by simply dragging them from the toolbox.

<!-- tags: [Syncfusion Winforms, Project Migration, Project Templates] keywords: [Syncfusion, Essential Studio, Windows Forms, WPF, Silverlight, ASP.NET MVC, Toolbox, Project Templates, Project Migration] -->
```

---

<!-- 페이지 26 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_101.jpeg
document_name: common
page_number: 101
page_id: common#page_101
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:27Z
fidelity: lossless
-->

# Essential Common

## Overview

- This page provides instructions for installing Syncfusion Oribase Studio 1.1.0.69.
- It outlines the license agreement and steps to accept the terms.
- Follow the installation process detailed in the guide.

## Content

### Install Process

The installation process is divided into four steps:

1. **Welcome**
   - Introduction to the installation process.

2. **Collecting Information**
   - Gathering necessary information for installation.

3. **Installing**
   - The actual software installation.

4. **Completed**
   - Confirmation of successful installation.

#### License Agreement

**Figure 94: License Agreement screen**

The License Agreement screen is displayed as part of the installation process:

- **License Agreement Text:**
  - **Content:** 
    - The Software License Agreement is a legal agreement between the user (You, Your, or Customer) and Syncfusion, Inc., a Delaware corporation. 
    --syncfusion licenses its products on a per-copy basis, site basis, and enterprise basis. The right to use any given copy of Syncfusion software products is set forth in this Agreement.
    - In cases of site or enterprise licenses, additional terms and conditions apply.

- **Options:**
  - I accept the terms in the License Agreement.
  - I do not accept the terms in the License Agreement.

#### Steps to Accept and Continue

1. On accepting the terms, click the **I accept the terms in the License Agreement** option.
2. Click **Next.** The Select the Installation Folder screen opens.

## API Reference

This section is not applicable as the content focuses on installation instructions.

## Code Examples

No code examples are provided in this section.

## Page-level Navigation/TOC

- **Welcome**
- **Collecting Information**
- **Installing**
- **Completed**

## Cross References

- Refer to the user guide for additional installation troubleshooting and tips.

## RAG Annotations

<!-- tags: [product, synchronization, install, license, agreement, software, user guide] keywords: [Syncfusion, Oribase Studio, installation, license terms, accept terms, next, installation folder] -->
```

---

<!-- 페이지 27 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_105.jpeg
document_name: common
page_number: 105
page_id: common#page_105
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:40Z
fidelity: lossless
-->

# Essential Common

## Overview
- Overview of the Orubase Studio setup process.
- Step-by-step guidelines to install the Orubase Studio.
- Note regarding the completion screen after installation.

## Content

### Orubase Studio Installation Wizard

The Orubase Studio installation process involves the following stages:

1. **Welcome**
2. **Collecting Information**
3. **Installing**
4. **Completed**

The current status indicates that the installation process is in progress.

### Figure 98: Installing

The setup wizard is in the "Installing" stage, as shown in the figure below:

```plaintext
Installing Orubase Studio
Please wait while the setup wizard installs Orubase Studio. This will take a few minutes.
Status:
```

The green progress bar indicates the current progress of the installation.

---

### Note:
The completed screen is displayed once the selected package is installed.

## Page-level Navigation/TOC (if applicable)
- Installing the Orubase Studio
- Steps of the Installation Process
- Completion Notification

## Cross References
- See also: Other setup guides for additional software installations.

<!-- tags: [Syncfusion Winforms, Orubase Studio, Installation, Setup Wizard, End-to-end enterprise mobile development solution] keywords: [Orubase Studio, installation, setup wizard, progress bar, completion screen] -->
```


---

<!-- 페이지 28 -->

```html
<!--  
source: image  
domain: syncfusion-sdk  
task: pdf-ocr-to-markdown  
language: en (keep original; do not translate)  
source_filename: page_109.jpeg  
document_name: common  
page_number: 109  
page_id: common#page_109  
product: Syncfusion Winforms  
version: 11.4.0.26  
timestamp: 2025-08-09T04:04:51Z  
fidelity: lossless  
-->  

# Essential Common  

## Overview  

- The section explains the installation process of the Syncfusion Metro Studio tool.  

## Content  

### Installation Process  

The image depicts the user interface during the unzip operation, as shown in **Figure 102: Unzip Operation**.  

```  
--- Setup - Syncfusion Metro Studio ---  
Please wait while Setup installs Syncfusion Metro Studio installer on  
your computer  

Finishing installation...  

[Unzip progress bar fully green]  

Cancel  
```  

**Figure 102: Unzip Operation**  

3. **When the unzip operation is complete, the Syncfusion Metro Studio Setup dialog box opens.**  

## API Reference  

*(No API reference content visible in the provided image)*  

## Code Examples  

*(No code examples visible in the provided image)*  

## Page-level Navigation/TOC (if applicable)  

*(No table of contents visible in the provided image)*  

## Cross References  

See related sections in the user guide for detailed instructions on using Syncfusion Metro Studio.  

<!-- tags: [syncfusion-sdk, winforms, setup, installation] keywords: [syncfusion metro studio, unzip operation, dialog box, essential common] -->
```

---

<!-- 페이지 29 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_113.jpeg
document_name: common
page_number: 113
page_id: common#page_113
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:01Z
fidelity: lossless
-->

## License Agreement Overview

- This page explains the installation process for Syncfusion Metro Studio 2.0.1.1 and details the terms of the software license agreement.
- Users are required to accept the license agreement and choose an installation folder as part of the installation procedure.

## Content

### License Agreement

The image shows the setup interface for Syncfusion Metro Studio 2.0.1.1, structured as follows:

#### Left Panel: Setup Progress
- **Sections listed:**
  - Welcome
  - Collecting Information
  - Installing
  - Completed

#### Main Panel: License Agreement
- **Title:** License Agreement
- **Instruction:** Please read the following license agreement carefully.
- **Content:**
  - The Software License Agreement is a legal agreement between the user ("You") and Syncfusion, Inc., a Delaware corporation located at 2501 Aerial Center Parkway, Suite 200, Morrisville, NC 27560.
  - The license is for Syncfusion Metro Studio, which includes over 1500 metro style icons ("Icons") usable in metro style applications for Windows®, other desktop, web, and mobile platforms.
  - The package also includes an icon customization tool for modifying attributes such as size.

#### Agreement Acceptance
- **Options:**
  - "I accept the terms in the License Agreement" (selected)
  - "I do not accept the terms in the License Agreement"

#### Navigation Buttons
- **Buttons:**
  - Back
  - Next
  - Cancel

#### Date Information
- **Date:** 07/16/2012

#### Steps to Proceed
- **Step 8:** After reading the terms, click the "I accept the terms in the License Agreement" option.
- **Step 9:** Click Next. Then Choose the Installation folder.

---

## Page-level Navigation/TOC
- If applicable, include a brief Table of Contents or cross-references here.

## RAG Annotations
<!-- tags: electrical, installation, license, agreement, metro-style, synfusion metro studio, setup process keywords: terms of use, installation folder, license acceptance -->
```

---

<!-- 페이지 30 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_117.jpeg
document_name: common
page_number: 117
page_id: common#page_117
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:17Z
fidelity: lossless
-->

# Essential Common

## Content

### Figures

**Figure 110: Installation Completed**

The configuration displayed includes:

- **Metro Studio Setup Completed**
- **Click Finish to exit the setup wizard.**

### Steps to Complete the Installation

12. Click **Finish** to exit the Setup Wizard. This will initiate the installation of the **Syncfusion Metro Studio Installer** on your computer.

### Note

The Syncfusion Metro Studio Installer will be installed on your computer, and you will be informed with a dialog box when the installation is completed.

## Cross References

See also:

- Syncfusion Metro Studio

## RAG Annotations

<!-- tags: [Syncfusion, Syncfusion Winforms, Metro Studio, Installation, Setup Wizard] keywords: [Syncfusion, Metro Studio, Installation, Setup Wizard, Installer, Configuration] -->
```

---

<!-- 페이지 31 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_121.jpeg
document_name: common
page_number: 121
page_id: common#page_121
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:25Z
fidelity: lossless
-->

## Content

### Adding Controls to the Toolbox

#### Step 1: Create a New Tab in the Toolbox

1. **Open the Toolbox** in your Visual Studio project.
2. **Right-click** on the Toolbox and select **Choose Items...** to access the options for adding new controls.

   - **Figure 113:** The screenshot shows a new tab titled "Syncfusion" being added to the toolbox. Various control categories are visible, such as **Printing**, **Dialogs**, and **WPF Interoperability**.

#### Step 2: Customize the Toolbox Content

3. **Customize the Toolbox** by selecting specific controls or categories to enhance your project's functionality.

   - **Figure 114:** A context menu is displayed after right-clicking on the "Syncfusion" tab in the toolbox. The "Choose Items..." option is highlighted, allowing you to manage which controls are included in the toolbox.

### Explanation

Adding controls to the toolbox in Visual Studio can streamline the development process by making frequently used components easily accessible. The steps outlined above help you create a custom tab, such as the "Syncfusion" tab shown in the figures, allowing you to organize and add only the necessary controls for your project.

### Example of Custom Controls in the Toolbox

The toolbox shown in the figures includes various controls:

- **Printing:** Includes controls for managing print-related tasks.
- **Dialogs:** Contains dialog boxes such as **ColorDialog**, **FolderBrowserDialog**, and others for user interaction.
- **WPF Interoperability:** Enhances functionality for WPF-related features.
- **Syncfusion Controls:** Added under the custom "Syncfusion" tab, providing various Syncfusion-specific controls.

## API Reference

None provided in the current context.

## Code Examples

No code examples are provided in the current context.

## Page-level Navigation/TOC

- Step 1: Create a New Tab in the Toolbox
  - Description and steps for creating a new tab.
- Step 2: Customize the Toolbox Content
  - Description and steps for customizing the toolbox content.

## Cross References

None provided in the current context.

## RAG Annotations

<!-- tags: Syncfusion Winforms, controls, toolbox, customization, version: 11.4.0.26 -->
<!-- keywords: toolbox, Syncfusion, controls, add, customize, Visual Studio, figure, dialog, printing, interoperability -->

---

<!-- 페이지 32 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_125.jpeg
document_name: common
page_number: 125
page_id: common#page_125
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:40Z
fidelity: lossless
-->

# MultiTarget Manager

## Overview
- Configure the MultiTarget Manager to manage licensing.
- Understand the steps to enable licensing successfully.
- Address file modifications and resolve them.

## Content

### Step-by-Step Process

1. **Click Fix It.**
2. The Syncfusion Licensing Enabler dialog box opens.

#### Figure 117: MultiTarget Manager

The Syncfusion Licensing Enabler dialog box appears with the following message:

```
Syncfusion Licensing Enabler

Result
Licensing changes were made successfully.

What to do next
• Please RE-BUILD & RE-START your application. Your application will have complete licensing support for all Syncfusion controls. If difficulties continue, please close VS.NET and remove the OBJ and BIN folders for your application before continuing.

Note
• You may be asked to re-load your VS.NET project if your project file was modified by the licensing enabler (in most cases).
```

#### Figure 118: Syncfusion Licensing Enabler

Click **OK** to proceed.

3. **Click OK.**
4. The File Modification Detected dialog box opens.

#### Figure 119: File Modification Detected

The dialog box displays the following message:

```
File Modification Detected

The project 'testapp' has been modified outside the environment.
Press Reload to load the updated project from disk.
Press Ignore to ignore the external changes. The changes will be used the next time you open the project.
```

#### Options
- **Reload**: Load the updated project from disk.
- **Ignore**: Ignore the external changes for now.

**Recommendation**: Click **Reload** to ensure all changes are applied correctly.

5. **Click Reload.**

### Notes
- After enabling licensing, ensure to rebuild and restart your application for the changes to take effect.
- Addressing file modifications correctly ensures a smooth development environment.

## RAG Annotations

<!-- tags: [Syncfusion, Winforms, MultiTarget Manager, Licensing, File Modification] keywords: [Syncfusion Licensing Enabler, Visual Studio, OBJ, BIN folders, RE-BUILD, RE-START] -->
```

---

<!-- 페이지 33 -->

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

---

<!-- 페이지 34 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_133.jpeg
document_name: common
page_number: 133
page_id: common#page_133
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:10Z
fidelity: lossless
-->

## Core Reference and Properties

### Reference Properties

The properties window in Syncfusion provides detailed information about the components referenced in your project. For instance, the `Syncfusion.Chart.Silverlight` reference includes the following details:

- **Name**: Syncfusion.Chart.Silverlight
- **Aliases**: `global`
- **Copy Local**: `True`
- **Culture**: (Empty)
- **File Type**: Assembly
- **Identity**: Syncfusion.Chart.Silverlight
- **Path**: C:\Program Files (x86)\Syncfusion\Essential Studio\8.1.0.30\ass...
- **Resolved**: `True`
- **Runtime Version**: v2.0.50727
- **Specific Version**: `True`
- **Strong Name**: `True`
- **Version**: 8.104.0.30

### Copy Local

**Description**: Indicates whether the reference will be copied to the output directory.

**Figure 126: Properties Window**

![Properties Window](#)

## Switching the Framework Version While Upgrading the Project

### Overview
- Provides guidance on switching the framework version during project upgrades.
- Utilizes the **MultiTarget Manager** from the Syncfusion Dashboard.

### Detailed Instructions
1. **Switching Framework Version**:
   - Use the **MultiTarget Manager** to switch the framework version.
   - After switching, remove the `bin` and `obj` folders from your local project directory.
   - Recompile your project to ensure compatibility with the new framework version.

**Reference**: For more details, refer to **Multi-Target Manager**.

## Migrating the Resource Files

### Overview
- Explains how to migrate resource files (.resx) to a newer version of the framework.
- Ensures that resource files are compatible with the updated environment.

### Steps to Migrate Resource Files
1. **Open the Migration Tool**:
   - Navigate to: **Start > Syncfusion > Essential Studio x.x.x.x > Utilities > Migration > ConvertResx(Framework 2.0, 3.5 or 4.0)**.
2. **Choose ResX Files**:
   - Click the **Choose ResX Files** option to begin the conversion process.
3. **Select Files to Convert**:
   - Select the `.resx` files that need to be converted to the newer framework version.

### Note
Ensure that all steps are followed to avoid any issues during the migration process.

## Performance Considerations

### Overview
- While migrating resource files, be aware of performance impacts and best practices.
- Follow the guidelines for smooth and efficient migration without compromising application performance.

### See also
- **Multi-Target Manager**: For detailed instructions on framework version management.
- **Essential Studio Documentation**: For comprehensive insights into migrating and upgrading projects.

<!-- tags: [Syncfusion, Winforms, Essential Studio, Resource Migration, Framework Version, MultiTarget Manager] keywords: [Syncfusion.Chart.Silverlight, .resx files, Copy Local, Multi-Target Manager, Framework, Migration, Resource Files] -->
```

---

<!-- 페이지 35 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_137.jpeg
document_name: common
page_number: 137
page_id: common#page_137
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:27Z
fidelity: lossless
-->

# Essential Common

You can use this satellite assembly to utilize the localization support for your culture. The following steps will help you to extract the resource strings to a .csv file using the LocBaml.exe file, as a major part of enabling localization.

## Overview
- Utilizing satellite assemblies for localization support.
- Extracting resource strings to a .csv file using LocBaml.exe.
- Steps to extract and customize resource strings.

## Content

The Syncfusion.Tools.WPF.Resources.dll is sufficient to generate the localization support for the Syncfusion controls. This assembly will be available in the following installation location:

### Installation Location

```
(Installed_location)\Syncfusion\Essential Studio\<Version Number>\Assemblies\3.5
```

### Steps to Enable Localization

1. **Download the LocBaml.exe file**  
   From the following location:  
   ```
   http://files.syncfusion.com/support/Tools.WPF/UG/LocBaml.zip
   ```

2. **Copy the exe file and Syncfusion.Tools.WPF.Resources.dll**  
   To the following location:  
   ```
   <Your Application>\bin\Debug\en-US
   ```

3. **Open the command prompt**  
   Navigate to the same directory as mentioned above.

4. **Generate the .csv file**  
   Use the following command to generate the .csv file from the existing Syncfusion.Tools.WPF.Resources.dll:  
   ```
   (Your Application)\bin\Debug\en-US LocBaml /parse Syncfusion.Tools.WPF.Resources.dll /out:resourceStrings.csv
   ```

5. **Edit the .csv file**  
   - The .csv files can be edited via MS Excel or Notepad.  
   - This file contains string resources with the default text in the English language.  

   Open the .csv file using MS Excel or Notepad, and change the texts based on your culture.

### Example Customization: English to French

The following illustrates customization from English to French.

<!-- tags: [Syncfusion Winforms, localization, resource strings, .csv file, LocBaml, string localization, satellite assembly] -->
```

---

<!-- 페이지 36 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_141.jpeg
document_name: common
page_number: 141
page_id: common#page_141
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:40Z
fidelity: lossless
-->

# Essential Common

## Overview
- Demonstrates how to apply cultural settings to the Ribbon Control in WinForms.
- Instructions to set the UI culture programmatically using C# code in `MainPage.xaml.cs` or `App.xaml.cs`.
- Visual examples showing the Ribbon Control under different culture settings.

## Content

### Setting the UI Culture in C# Code

#### In MainPage.xaml.cs
The UI culture can be set in the constructor of the `MainPage` class as follows:

```csharp
public MainPage()
{
    System.Threading.Thread.CurrentThread.CurrentUICulture = new
    System.Globalization.CultureInfo("fr-FR");

    InitializeComponent();
}
```

#### In App.xaml.cs
Alternatively, the UI culture can be set during the application startup in `App.xaml.cs`:

```csharp
private void Application_Startup(object sender, StartupEventArgs e)
{
    System.Threading.Thread.CurrentThread.CurrentUICulture = new
    System.Globalization.CultureInfo("fr-FR");

    this.RootVisual = new MainPage();
}
```

### Visual Illustrations

#### Figure 132: Ribbon Control for Invariant Culture

[![Figure 132: Ribbon Control for Invariant Culture](https://via.placeholder.com/800x400.png?text=Figure+132%3A+Ribbon+Control+for+Invariant+Culture)](./assets/image1.png)

**Description:** This figure shows the Ribbon Control without any specific cultural localization applied.

#### Figure 133: French Culture assigned as Current UI Culture

[![Figure 133: French Culture assigned as Current UI Culture](https://via.placeholder.com/800x400.png?text=Figure+133%3A+French+Culture+assigned+as+Current+UI+Culture)](./assets/image2.png)

**Description:** This figure illustrates the Ribbon Control after setting the culture to French (`fr-FR`), displaying labels and other elements in French.

## Cross References
- For more information on internationalization and localization using Syncfusion controls, refer to the relevant sections in the Syncfusion WinForms User Guide.

<!-- tags: [syncfusion, winforms, ribbon-control, ui-culture, localization, culture] keywords: [MainPage.xaml.cs, App.xaml.cs, CultureInfo, CurrentUICulture, French culture, invariant culture, Ribbon Control, WinForms] -->
```

---

<!-- 페이지 37 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_145.jpeg
document_name: common
page_number: 145
page_id: common#page_145
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:55Z
fidelity: lossless
-->

# Essential Common

## Overview

- Toolbox Configuration Utility and its usage at page 120.
- Instructions on upgrading projects using the Project Migration Utility at page 132.
- Manual project upgrading process at page 132.
- Reference to User Guide starting at page 32.
- Details about Utilities starting from page 70.
- Explanation of the issue with the unlock key being displayed as invalid during setup at page 134.
- Information on Windows and ASP.NET at page 142.
- Overview of WPF starting from page 136.

## Content

### Toolbox Configuration Utility
- Description or instructions regarding the configuration of tools and utilities in the Toolbox.

### Upgrading the Project Using Project Migration Utility
- **Upgrade the Project Using Project Migration Utility**
- Detailed steps or considerations for automatically upgrading projects using the provided utility.
- **Upgrading the Projects Manually**
- Instructions for manually upgrading projects in cases where the automatic method is not applicable.

### User Guide
- Reference to the main User Guide document.

### Utilities
- Information or instructions related to various utility features.

### Unlock Key Issue
- Explanation or troubleshooting details for when the unlock key is displayed as invalid during the setup process.

### Windows and ASP.NET
- Information specific to using Syncfusion components with Windows and ASP.NET environments.

### WPF
- Overview or specific guidance for implementing Syncfusion components with Windows Presentation Foundation (WPF).

## API Reference

- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required.
- Returns: Type + description.
- Exceptions: bullet list.

## Code Examples

- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

## Page-level Navigation/TOC

- Local Table of Contents for this page, if present, kept as a bullet/numbered list with links/text as shown.

## Cross References

- See also: bullet list of explicit links/texts present on the page.

## RAG Annotations

<!-- tags: [common, toolbox, project migration, user guide, utilities, unlock key, windows, asp.net, wpf] keywords: [toolbox configuration, project migration utility, user guide, utilities, unlock key issue, windows and asp.net, wpf, syncfusion, winforms] -->
```

---

<!-- 페이지 38 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_002.jpeg
document_name: common
page_number: 002
page_id: common#page_002
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:58:45Z
fidelity: lossless
-->

# Contents

1. **Essential Studio**
   - 1.1 **Terminology** ..... 4
   - 1.2 **Minimum software requirements** ..... 5
   - 1.3 **Essential Studio Enterprise Installer**
     - 1.3.1 **Overview** ..... 6
     - 1.3.2 **Step-by-Step Installation** ..... 6
     - 1.3.3 **Command Line**
       - 1.3.3.1 **Command line installation** ..... 12
       - 1.3.3.2 **Command Line Uninstall Options** ..... 13
   - 1.4 **Essential Studio Installer for Individual Platforms**
     - 1.4.1 **Overview** ..... 14
     - 1.4.2 **Step-by-Step Installation** ..... 14
     - 1.4.3 **Command Line**
       - 1.4.1.1 **Command line installation** ..... 19
       - 1.4.1.2 **Command Line Uninstall Options** ..... 20
   - 1.5 **Source code**
     - 1.5.1 **Overview** ..... 21
     - 1.5.2 **Step-by-Step Installation** ..... 21
   - 1.6 **Documentation setup**
     - 1.6.1 **User Guide** ..... 32
     - 1.6.2 **Class Reference** ..... 34
   - 1.7 **Link Install Setup** ..... 36
   - 1.8 **Digitally Signed Assemblies Setup** ..... 44
   - 1.9 **Patches**
     - 1.9.1 **Installing a Patch Setup** ..... 53
     - 1.9.2 **Reverting a Patch** ..... 58
   - 1.10 **QTP Add-on** ..... 60
   - 1.11 **CAB Add-on** ..... 61
   - 1.12 **Samples**
     - 1.12.1 **Offline Samples** ..... 62
     - 1.12.2 **Online Samples** ..... 69

<!-- tags: [Syncfusion Winforms, installation, documentation, setup, patches] keywords: [Essential Studio, Minimum software requirements, Enterprise Installer, Source code, Documentation setup, Patches, QTP Add-on, CAB Add-on, Samples, Online Samples, Offline Samples] -->
```

---

<!-- 페이지 39 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_006.jpeg
document_name: common
page_number: 006
page_id: common#page_006
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:01Z
fidelity: lossless
-->

## Essential Studio Enterprise Installer

### 1.3.1 Overview

The Essential Studio single installer includes all of the following platforms. There is also a separate installer for individual platforms. For more information refer to the **Platform installer** section.

- ASP.NET
- ASP.NET MVC
- Mobile MVC
- Silverlight
- Windows Forms
- Windows Phone
- WinRT
- WPF

**Note:** Windows Phone and WinRT can only be installed on Windows 8.

### 1.3.2 Step-by-Step Installation

The following procedure illustrates how to install Essential Studio setup:

1. Double-click the **Syncfusion Essential Studio Setup** file. The self-Extractor wizard opens and extracts the package automatically.

![](image/WinZip_Self-Extractor.SyncfusionEssentialStudio_11.1.0.21_03072013_0439...png)

## WinZip Self-Extractor - syncfusionessentialstudio_11.1.0.21_03072013_0439...
- Thank you for choosing Syncfusion Essential Studio.
- Please wait while setup prepares the Windows Installer package for installation. This process will complete within a minute. Afterwards, setup will start.
- Unzipping: SyncfusionEssentialStudio_11.1.0.21.exe

<!-- tags: [Syncfusion Winforms, Essential Studio Enterprise Installer, Installation, Platform installer, Overview, Step-by-Step Installation, Version: 11.4.0.26] keywords: [Essential Studio, Windows Phone, WinRT, ASP.NET, extractor, self-extractor, package installation, setup, Winforms] -->
```

---

<!-- 페이지 40 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_010.jpeg
document_name: common
page_number: 010
page_id: common#page_010
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:13Z
fidelity: lossless
-->

# Essential Common

## Overview
- Describes the process of selecting platforms for installation.
- Provides a detailed guide on installing Syncfusion Studio.
- Includes platform-specific notes for Windows Phone and WinRT.

## Content

### Select Platform

**Figure 5: Select Platform**

![Select Platform Screenshot](https://example.com/image) <!--Visual representation of platform selection interface-->

The interface allows selection of various platforms for installation:

- **Web Platforms:**
  - [ ] ASP.NET
  - [ ] ASP.NET MVC
- **Mobile Platforms:**
  - [ ] Mobile MVC
- **Legacy Platforms:**
  - [ ] Silverlight
- **UI Frameworks:**
  - [ ] Windows Forms
  - [ ] WPF
- **Platform-Specific Notes:**
  - Windows Phone
  - WinRT (XAML)

*Note:* Windows Phone and WinRT platforms will install only on Windows 8.

### Installation Steps

1. **Select Platforms**: Choose the desired platforms for installation.
2. **Click Install**: Proceed with the installation process by clicking the "Install" button.

**Buttons:**
- **BACK**: Return to the previous screen.
- **INSTALL**: Begin the installation process for the selected platforms.

## Page-level Navigation/TOC

- **Select Platform**
- **Installation Steps**

<!-- tags: [installation, Syncfusion Studio, platform selection] keywords: [Windows Forms, WPF, ASP.NET MVC, Mobile MVC, Silverlight, Windows Phone, WinRT] -->
```

---

<!-- 페이지 41 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_014.jpeg
document_name: common
page_number: 014
page_id: common#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:24Z
fidelity: lossless
-->

## 1.4 Essential Studio Installer for Individual Platforms

### 1.4.1 Overview

Separate platform setups are provided from version 11.1.0.21. There are 8 platforms:

1. ASP.NET
2. ASP.NET MVC
3. Mobile MVC
4. Silverlight
5. Windows Forms
6. Windows Phone (only on Windows 8)
7. WinRT (only on Windows 8)
8. WPF

Windows Phone and WinRT platform setups will only install on the Windows 8 OS.

### 1.3.2 Step-by-Step Installation

The following procedure illustrates how to install Essential Studio:

1. Double-click the Syncfusion Essential Studio platform Setup file. The self-Extractor wizard opens and extracts the package automatically.

![Self-Extractor](image.png)
*Figure 8: Self-Extractor*

#### Note: The WinZip self-Extractor will extract the `syncfusionessentialsstudio_(version).exe` dialog, displaying the unzip operation of the package.

```markdown
# Copyright Notice
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [syncfusion sdk, essential studio, installer, platforms, step-by-step installation, winforms] keywords: [syncfusion, essential studio, setup, platform-specific installations, windows phone, winrt, windows 8, self-extractor, unzip operation, version 11.1.0.21] -->
```

---

<!-- 페이지 42 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_018.jpeg
document_name: common
page_number: 018
page_id: common#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:34Z
fidelity: lossless
-->

## Essential Common: Overview

- Describes the installation process of Essential Studio for Mobile MVC.
- Highlights the inclusion of 21 new HTML & JavaScript client-side controls.

## Content

### Installing Essential Studio for Mobile MVC

The image shows the installation window for Essential Studio for Mobile MVC, specifically version 11.1.0.21, dated 02/14/2013. Here are the key elements visible:

- **Title:** "SYNCFUSION Mobile MVC"
- **Description:** Indicates the installation of Essential Studio for Mobile MVC.
- **Features:**
  - 21 new HTML & JavaScript client-side controls are highlighted.
  - Icons representing JSON, grid views, document editing, and code editing are displayed.
- **Status:** The installation status is shown as "Install Initialize."
- **Actions:** A prominent "CANCEL" button is visible for user intervention.

### Image Recap

The installation progress bar is not yet completed, suggesting that the installation process is in the initialization phase. The window provides a clear visual guide to the features being installed and allows for user cancellation if needed.

### Figure: Essential Studio Installation

Refer to **Figure 12: Installing Essential Studio**, which illustrates the installation progress window for Essential Studio.

## Cross References

- See also: Documentation on [unclear] for more details on the specific controls and their features.

<!-- tags: [essential-studio, mobile-mvc, html, javascript, client-side-controls, syncfusion] keywords: [installation, syncfusion, json, grid, document, code, essential studio, mobile MVC] -->
```

---

<!-- 페이지 43 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: common
page_number: 022
page_id: common#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:46Z
fidelity: lossless
-->

# Essential Common

(Note: Inno script extracts the syncfusionessentialstudiosourcecodeaddoninstallersetup.exe dialog, displaying the unzip operation of the package.)

## Overview
- The Inno script is used to extract the setup for the Syncfusion Essential Studio Source Code Add-on.
- The unzip operation is displayed, showing the installation progress.

## Content

### Installation Process

#### Figure 15: Unzip Operation
This figure illustrates the unzip operation process during the installation of the Syncfusion Essential Studio Source Code Add-on.

![Setup - Syncfusion Essential Studio Source Code Add-on Installer](#)

1. **Installation Prompt**
    - The setup utility begins installing the Syncfusion Essential Studio Source Code Add-on on the computer.
    - A progress bar indicates the current stage of the installation, which is "Finishing installation..." as shown in the dialog box.

#### Dialog Box Behavior
3. **On completion of the unzip operation**, the **Setup - Syncfusion Essential Studio Source Code Add-on Installer** dialog box opens, allowing the user to monitor and manage the installation process.

## Page-level Navigation/TOC (if applicable)
- This section provides a detailed walkthrough of the installation steps for the Syncfusion Essential Studio Source Code Add-on, focusing on the unzip operation.

### Cross References
- Refer to previous sections or documentation for the initial steps leading up to the unzip operation.

<!-- tags: [Syncfusion, Winforms, installation, unzip operation, add-on] keywords: [Inno script, setup, progress bar, source code add-on, installation dialog] -->
```

---

<!-- 페이지 44 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_026.jpeg
document_name: common
page_number: 026
page_id: common#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:57Z
fidelity: lossless
-->

# Essential Common

## Overview
- Describes the installation process of the Syncfusion Essential Studio source code add-on.
- Highlights the license agreement step, including acceptance terms.
- Guides users through selecting the setup type after accepting the license agreement.

## Content

### Installation Process

#### Syncfusion Essential Studio Source Code Add-On Installer Setup

- **Welcome**: This is the initial step where you start the installation process.
- **Collecting Information**: Here, you will be asked for necessary information related to the installation.
- **Installing**: This step handles the actual installation of the software.
- **Completed**: Once the installation is complete, you will see this step confirming the installation is finished.

#### License Agreement

Figure 19: License Agreement

- **License Terms**: The license agreement displayed in the installer outlines the legal terms between the user and Syncfusion, Inc.
- **Key Points**:
  - **Terms and Conditions**: Includes details about licensing options, such as per-copy, site, and enterprise licenses.
  - **Copyright**: Specifically mentions that the software is licensed to the user under the terms detailed in the agreement.
- **Action**:
  - **Step 8**: After reading the terms, click the "I accept the terms in the License Agreement" option.
  - **Step 9**: Click Next. The "Choose the Setup Type" screen will appear.

## API Reference

- **Namespace**: None explicitly mentioned in this section.
- **Class**: None explicitly mentioned in this section.
- **Members**: None explicitly mentioned in this section.

## Code Examples

No code examples are present in this section.

## Page-level Navigation/TOC

No additional navigation or TOC present in this section.

## Cross References

- None explicitly mentioned in this section.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, installation, license agreement, setup type, common, user guide] keywords: [Syncfusion Essential Studio, source code add-on, license terms, per-copy license, site license, enterprise license, installation process, accept terms, next screen] -->
```

---

<!-- 페이지 45 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_030.jpeg
document_name: common
page_number: 030
page_id: common#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:10Z
fidelity: lossless
-->

# Essential Common

## Overview
- This page details the completion of the installation for the Syncfusion Essential Studio Source code add-on.
- It outlines the final steps to complete the installation and provides guidance on next actions after installation.

## Content

### Installation Process Recap
The installation wizard for the Syncfusion Essential Studio Source code add-on proceeds through four stages:

1. **Welcome**: Initial welcome screen for the user.
2. **Collecting Information**: Gathering necessary information for the installation.
3. **Installing**: The actual installation process.
4. **Completed**: Finalizing the installation.

#### Figure 23: Installation Completed
The image below shows the completion screen for the installation:

| Date       | Version       |
|------------|---------------|
| 27/02/2013 | 11.1.0.21     |

---

### Finalizing the Installation
13. Click **Finish** to exit the Setup Wizard. This will initiate the installation of the Syncfusion Essential Studio Source Installer on your computer.

#### Note:
The Syncfusion Essential Studio Source Installer will be installed on your computer, and you will be informed with a dialog box when the installation is completed.

---

## Cross References
- Refer to the installation guide for further details on the installation process.

<!-- tags: [Syncfusion, Essential Studio, Source code add-on, Installation, Winforms] keywords: [Syncfusion, Essential Studio, Source code add-on, Installation, Wizard, UI, Setup, Visual Studio] -->
```

---

<!-- 페이지 46 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_034.jpeg
document_name: common
page_number: 034
page_id: common#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:21Z
fidelity: lossless
-->

## 1.6.2 Class Reference

### Local documentation

A complete set of documentation for Class Reference is provided under the following headers:

#### Installed Documentation

Documentation pertaining to Essential Studio can be installed with your copy of Syncfusion local resources. Explore the following three categories of documentation to have a better idea of Essential Studio products.

- Visual Studio 2005/ Visual Studio 2008 Class Reference
- Visual Studio 2010 Class Reference
- Visual Studio 2012 Class Reference

This local documentation can be accessed from the Dashboard > Utilities > Documentation > Local Documentation.

---

### Online Documentation

We have provided comprehensive documentation online to help you better understand our products.

#### User Guide
#### Class Reference

### Local Documentation

Documentation pertaining to our products can be installed with your copy of Syncfusion's local resources. Explore the three categories of documentation to have a better idea of our products.

- VS2005/VS2008 Class Reference and User Guide
- VS2010 Class Reference
- VS2010 User Guide

<!-- tags: [product, syncfusion-sdk, essential-studio, winforms, documentation, class-reference, installed-documentation, online-documentation] keywords: [syncfusion, essential studio, class reference, visual studio, 2005, 2008, 2010, 2012, documentation, user guide, local documentation, installed resources] -->
```

---

<!-- 페이지 47 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_038.jpeg
document_name: common
page_number: 038
page_id: common#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:32Z
fidelity: lossless
-->

# Essential Common

## Overview
- Setup process for Syncfusion Essential Studio.
- Request for user information including User Name, Organization, and Unlock Key.
- Steps for entering this information and proceeding with the installation.

## Content

### User Information Screen

![Figure 30: User Information screen](attachment:User_Information_Screen)

**Figure 30: User Information screen**

#### Steps to Enter Information:
1. **Enter your User Name, Organization, and Unlock Key** in the corresponding text boxes provided.
2. **Click Next**.

#### Note:
*The unlock key is validated and the preceding Welcome screen opens.*

### Description

The setup wizard for **Syncfusion Essential Studio Link Install 11.1.0.21** requires users to provide essential information to proceed with the installation. The steps are outlined as follows:

1. **Welcome Screen**: The initial screen welcomes users and indicates the version being installed.
   - **Version**: `11.1.0.21`
   - **Date**: `19/02/2013`

2. **Collecting Information**: Users are prompted to fill in the required fields:
   - **User Name**: The user is required to enter their name in the provided textbox.
   - **Organization**: The organization name or relevant details should be filled in here.
   - **Unlock Key**: A valid unlock key is necessary to proceed. Users can obtain a free evaluation key by clicking the **Get a Free Evaluation Key** button.

3. **Installing**: Once the information is validated, the installation process will continue as described in the subsequent steps.

4. **Completed**: Upon successful completion of installation, the setup wizard will inform the user that the installation is finished.

### Call to Action
- Ensure all fields are correctly filled out to avoid errors during the installation process.
- Use the provided options (e.g., "Get a Free Evaluation Key") if needed.

## API Reference

This page does not contain any specific API references but focuses on the installation and setup process through a user interface.

## Code Examples

No code examples are present on this page. The content is instructional and forms part of the installation guide.

## Page-level Navigation/TOC

This section of the documentation focuses on the initial steps of the installation process, particularly the **User Information** screen. Subsequent sections will likely cover the installation itself, post-installation setup, and other relevant topics.

## Cross References

### See also:
- Other installation guides for different versions of Syncfusion Essential Studio.
- Supplemental documentation on obtaining evaluation keys or managing licenses.

<!-- tags: [syncfusion-sdk, winforms, installation, setup, user-information, essential-studio] keywords: [syncfusion, essential studio, user name, organization, unlock key, evaluation key] -->
```

---

<!-- 페이지 48 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_042.jpeg
document_name: common
page_number: 042
page_id: common#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:47Z
fidelity: lossless
--> 

## Overview

- Essential Common
- Setup Wizard for Syncfusion Essential Studio
- Ready to install Essential Studio 2013 Vol 1
- Steps: Welcome, Collecting Information, Installing, and Completed

## Content

### Syncfusion Essential Studio Installation

The Syncfusion Essential Studio installation process is displayed in the setup wizard window.

#### Installation Steps

1. **Welcome** - The setup wizard is ready to begin the installation of Essential Studio.
2. **Collecting Information** - Information is being gathered to proceed with the installation.
3. **Installing** - The installation process is currently active.
4. **Completed** - Indicates when the installation process has been successfully completed.

#### Figure 34: Ready to Install

![Syncfusion Installation](Syncfusion Installation)

- **Date**: 19/02/2013
- **Version**: 11.1.0.21

##### Installation Instructions
- **Step 13**: Click **Install** to continue with the installation.
- Options:
  - **Back**: Allows you to review or change any of your installation settings.
  - **Cancel**: Option to exit the wizard.

## Page-level Navigation/TOC (if applicable)
- Setup process for Syncfusion Essential Studio.
- Step-by-step guide through the installation UI.

## Cross References
- Related documentation or user guides on Syncfusion Essential Studio installation.
- Reference materials for additional setup options or troubleshooting.

<!-- tags: [Syncfusion, Essential Studio, Installation, Winforms, UI, Setup Wizard] keywords: [Syncfusion, Essential Studio, 2013, Vol 1, Installation, Setup, Steps, Date, Version, Install, Back, Cancel, User guide, documentation, ready to install] -->
```

---

<!-- 페이지 49 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_046.jpeg
document_name: common
page_number: 046
page_id: common#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:59Z
fidelity: lossless
--> 

# Essential Common

![Syncfusion Essential Studio Digitally Signed Assemblies Setup](image_of_the_setup_window)

## Overview
- Instructions for entering user information in the setup process.
- Entering required details such as User Name, Organization, and Unlock Key to proceed with installation.
- Validating the Unlock Key to continue.

## Content

### User Information Screen

#### Figure 39: User Information screen
![User Information screen](image_of_user_information_screen)

The User Information screen prompts the user to provide the following details:

1. **Welcome**: Indicates the beginning of the setup process.
2. **Collecting Information**: Fields for entering User Name, Organization, and Unlock Key.
3. **Installing**: The installation phase will start after the required information is provided.
4. **Completed**: Final screen once the installation is finished.

#### Steps to Follow:
- **Step 4**: Enter your **User Name**, **Organization**, and **Unlock Key** in the corresponding text boxes provided.
- **Step 5**: Click **Next**.

#### Note:
The Unlock Key is validated, and the preceding Welcome screen opens.

### Validation of Unlock Key
- After entering the Unlock Key, the system validates it to ensure the user is authorized to proceed.
- Upon successful validation, the installation continues to the next phase.

## API Reference (if applicable)
No specific API reference required for this context.

## Code Examples (if applicable)
No code examples are provided in this section.

## Page-level Navigation/TOC (if applicable)
No additional navigation elements are present.

## Cross References
No cross-references are provided in this section.

<!-- tags: [essential_common, user_information, unlock_key, installation_guidelines, syncfusion_winforms] keywords: [user_name, organization, unlock_key, installation_process] -->
``` 


---

<!-- 페이지 50 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: common
page_number: 050
page_id: common#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:11Z
fidelity: lossless
-->


## Overview
- Guides users through the installation process of Syncfusion Essential Studio using the "Setup Type" selection.
- Provides options for "Typical," "Custom," and "Complete" setups based on user needs and expertise.
- Emphasizes selecting the appropriate setup type to ensure a tailored installation experience.

## Content

### Installation Process

The setup process for Syncfusion Essential Studio is divided into the following steps:

#### Step 1: Welcome
- The initial screen welcomes users to the installation process and prompts them to choose the appropriate setup type.

#### Step 2: Collecting Information
- Users provide necessary information required for the installation.

#### Step 3: Installing
- The installation process begins, installing chosen components and features.

#### Step 4: Completed
- The installation process is successfully completed, indicating that all desired components are installed.

#### Setup Type Selection

##### Typical
- Installs the most common program features, recommended for most users.
  - **Description:** Installs core functionalities.
  
##### Custom
- Allows users to choose specific program features and where they will be installed, suited for advanced users.
  - **Description:** Offers flexibility for advanced configurations.

##### Complete
- Installs all available program features, consuming the most disk space (Recommended for users requiring full functionality).
  - **Description:** Ensures all possible features are available post-installation.

#### Interact with the Setup
- **Previous Button:** Navigate back to the previous screen.
- **Next Button:** Proceed to the next step in the installation.
- **Cancel Button:** Abandons the installation process.

### Figure: Setup Type
The user interface shows the setup type selection screen with options for "Typical," "Custom," and "Complete."

#### Step 10: Selecting the Setup Type
- Users should select their preferred setup type based on their needs.
- **Example:** To install the complete setup, click the "Complete" option.

## Installation Details

- **Date:** 19/02/2013
- **Version:** 11.1.0.21

## API Reference

This page does not include specific API references as it is primarily focused on the installation guide.

## Code Examples

No code examples are provided on this page as it focuses on the setup process for users.

## Page-level Navigation/TOC

- **Step 1:** Welcome
- **Step 2:** Collecting Information
- **Step 3:** Installing
- **Step 4:** Completed
- **Setup Type Selection:** 
  - Typical
  - Custom
  - Complete

## Cross References

- Refer to the official Syncfusion documentation for detailed technical guides and API references.

<!-- tags: [Syncfusion Winforms, Installation, Setup Type] keywords: [Syncfusion Essential Studio, Typical, Custom, Complete, Installation Process, Setup Guide, Version 11.1.0.21] -->
```

---

<!-- 페이지 51 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_054.jpeg
document_name: common
page_number: 054
page_id: common#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:30Z
fidelity: lossless
-->

## Essential Common

### Overview
- Instructions for installing the Syncfusion Essential Studio Service Pack using the Unified Installer.

### Content

#### Installing the Syncfusion Essential Studio Service Pack

1. Double-click the Syncfusion Essential Studio patch setup file. The Syncfusion Essential Studio Service Pack opens.

![Figure 47: Unified Installer](attachment:Figure47_UnifiedInstaller.png)
*Figure 47: Unified Installer*

2. Click Next. The Assembly Manager opens.

---

## API Reference

- [Syncfusion License File Documentation](#)
- [Syncfusion Installation Guide](#)
- [Essential Studio Service Pack Details](#)

## Code Examples

### Features:
- **Unified Installer**: Automates the installation and management of Syncfusion components.

```csharp
// Sample installation code snippet
using Syncfusion.Licensing;

class Program
{
    static void Main()
    {
        SyncfusionLicenseProvider.RegisterLicense("YourLicenseKey");
        
        // Example installation logic
        // This is a placeholder for the actual installation logic.
    }
}
```

## Page-level Navigation/TOC
### 1. Essential Common
#### Overview
##### Installation Instructions
### Content
#### Installing the Syncfusion Essential Studio Service Pack
#### Unified Installer

---

### References
- [Syncfusion Documentation Home](https://help.syncfusion.com/)
- [Syncfusion Installation Documentation](https://help.syncfusion.com/products/installation)

<!-- tags: [syncfusion-sdk, winforms, essential-studio, service-pack, installation] keywords: [syncfusion license, essential studio, service pack, unified installer, installation guide, assembly manager] -->
```

---

<!-- 페이지 52 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_058.jpeg
document_name: common
page_number: 058
page_id: common#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:42Z
fidelity: lossless
-->

## Completing the Syncfusion Essential Studio Service Pack 11.1.0.21 Setup

### Figure 51: Installation Completed

![Figure 51: Installation Completed](https://github.com/yourusername/yourrepo/blob/master/Figure_51.png)

6. Click **Finish**.

The new assemblies will be placed in the **Pre-Compiled Assemblies** folder. These new assemblies can be referenced in your project.

## 1.9.2 Reverting a Patch

### Overview
- The patch install process involves backing up and storing assemblies in specific folders.
- Provides steps to revert the patch if necessary.

### Content

#### Reverting a Patch
The patch install will take a backup of the release assemblies and store them in the **Backup Assemblies** folder. The patch assemblies will also be stored in the **Patch** folder. You can revert back if needed.

#### Revert back to release assemblies
The following are the steps to revert to the release assemblies:

1. Copy the release assemblies from the **Backup Assemblies** folder.
2. Paste them in the **precompiledassemblies** folder.
3. Open **Dashboard > Utility > Assembly Management > Assembly Manager**.

### API Reference
- No specific APIs or methods are referenced in this section. Refer to the Syncfusion documentation for detailed API usage.

### Code Examples
No code examples are provided in this section. Refer to the Syncfusion documentation for code examples related to assembly management.

### Page-level Navigation/TOC
- **1.9.2 Reverting a Patch**
  - Reverting a Patch
  - Revert back to release assemblies

### Cross References
- Refer to the **Dashboard > Utility > Assembly Management > Assembly Manager** section for detailed assembly management options.

<!-- tags: [Syncfusion Winforms, Essential Studio, Service Pack, Patch, Revert, Pre-Compiled Assemblies, Backup Assemblies, Assembly Management, Version 11.4.0.26] keywords: [Syncfusion, Essential Studio, Service Pack 11.1.0.21, Reverting a Patch, Pre-Compiled Assemblies, Backup Assemblies, Assembly Management, Revert to Release Assemblies] -->
```


---

<!-- 페이지 53 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: common
page_number: 062
page_id: common#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:55Z
fidelity: lossless
-->

## Offline Samples

The samples from Syncfusion Essential Studio setup are provided. The samples are installed at the location below. The sample will be run from **IIS** or **Local server**. The installed samples are configured for IIS 7.0 and IIS 7.5 installed machines, otherwise the samples will run from the local server.

You can run the samples from the Dashboard's **Run Samples** button for each platform.

### Figure 53: Offline run samples

The Sample Browser is an application provided by Syncfusion to help users easily browse through these installed samples. The sample browsers for the platforms are shown below.

#### ASP.NET

```html
<!-- tags: [Syncfusion, Essential Studio, Offline Samples, Sample Browser, ASP.NET, Windows Forms, WPF, Silverlight, Mobile MVC, Windows Phone, WinRT, Utilities, License Management, IIS, Local server] keywords: [Samples, Installed Locations, IIS, Local Server, Sample Browser, ASP.NET, Project Template, Code Snippets, UI, Reporting, BI, Web Applications] -->
```
```

---

<!-- 페이지 54 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_066.jpeg
document_name: common
page_number: 066
page_id: common#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:05Z
fidelity: lossless
-->

## Essential Common

### Overview

- Demonstrates the `Essential Studio Silverlight` components and their various categories such as Chart, Grid, Diagram, and more.
- Focuses on the `Silverlight Chart` component, highlighting its performance optimization and features.
- Lists key components including `Silverlight Chart`, `GridDataControl`, `Gantt`, `Maps`, and others, emphasizing their roles in the `Silverlight` environment.

### Content

#### 12. Silverlight [Overview]
The Silverlight section provides an in-depth look at the Silverlight Chart component, discussing its capabilities and features:

**Figure 58: Essential Studio Silverlight Sample Browser**

##### Chart
- **Showcase**
  - Basic Charts
  - Accumulation Charts
  - Circular Charts
  - Financial Charts
  - Fast Charts

**Chart Description**
- The `SfChart` is a high-performance charting component designed to optimize performance under various usage scenarios.
- It can handle a large number of data points, even across multiple series, and manage frequent real-time updates efficiently while maintaining low memory and CPU usage.

#### Web Page Layout
The image displays the Silverlight Sample Browser with the following layout:

1. **Top Navigation Bar**
   - Contains the logo and search functionality.
   - Includes a navigation bar with options like `Chart`, `Showcase`, and other chart-related categories.

2. **Component Overview**
   - Lists various Silverlight controls and components.
   - Arranged in a grid format, showcasing:
     - **Chart**
     - **Grid**
     - **Gantt**
     - **Maps**
     - **Reports**

3. **Footer**
   - Copyright notice: "Copyright Syncfusion Inc. 2001 - 2013. All rights reserved."

#### 13. Windows Forms [Next Section]
This page transitions into the Windows Forms section, indicating the next part of the document.

## Page-level Navigation/TOC
- [12. Silverlight]
- [13. Windows Forms]

## Cross References
- The document refers to various components such as `SfChart`, `GridDataControl`, and others, suggesting their usage and integration within different platforms like Silverlight and Windows Forms.

<!-- tags: [essential-studio, silverlight, winforms, component, performance, chart, grid, gantt, maps, reports] keywords: [silverlight chart, sychfusion winforms, component overview, sample browser, real-time updates, large data points, performance optimization] -->
```

---

<!-- 페이지 55 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_070.jpeg
document_name: common
page_number: 070
page_id: common#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:20Z
fidelity: lossless
-->

## Essential Common

### Content

| WPF | http://silverlight.syncfusion.com/samples/WPF/Samples/WPFSampleBrowser/UI/Tools/Tools.htm |
| --- | --- |

#### 1.13 Utilities

##### 1.13.1 Dashboard

This section provides details on the structure and composition of the Syncfusion Essential Studio dashboard. It also elaborates on navigating within the dashboard to access various utilities and product samples.

![Dashboard](Figure 62: Dashboard)

The dashboard structure can be split into the following:

### Menu

The Menu includes the menu bar which accommodates five menus:

1. **File** - Allows you to exit the dashboard, which can alternatively be done by clicking × in the right top corner of the dashboard.

### Page-Level Navigation/TOC

- **1.13 Utilities**
  - **1.13.1 Dashboard**

### Cross References

See also:
- [http://silverlight.syncfusion.com/samples/WPF/Samples/WPFSampleBrowser/UI/Tools/Tools.htm](http://silverlight.syncfusion.com/samples/WPF/Samples/WPFSampleBrowser/UI/Tools/Tools.htm)

<!-- tags: [product, module, control, api, version?] keywords: [dashboard, structure, navigation, utilities, samples, syncfusion, essential studio, winforms] -->
```

---

<!-- 페이지 56 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_074.jpeg
document_name: common
page_number: 074
page_id: common#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:30Z
fidelity: lossless
-->

## Overview
Essential Studio for Mobile MVC, now with support for MVC 4 and client-side rendering, provides 35 controls for pixel-perfect web application development across various platforms, including iOS, Android, and Windows Phone. The dashboard interface allows users to easily select and explore platform-specific options, run samples, and access comprehensive documentation and notes for the respective products.

## Essential Studio for Mobile MVC

- **Now with support for MVC 4 and client-side rendering**
- **35 controls for creating pixel perfect web applications for iOS, Android, and Windows phone**

### Dashboard

Figure 69: Dashboard  
[Dashboard interface showing various platform options and utility tools for Essential Studio]

### Steps for Interacting with the Dashboard

1. Select the required platform. Options for the selected platform will be displayed on the right.
2. Click any of the following to know more about the selected product:
   - **Run Samples** to run the locally installed samples.
   - **Online Samples** to view online samples.
   - **Explore Samples** to open local installed location.
   - **Explore Source** to view the source (requires source license and source add-on setup).
   - **Online Documentation** to view the documentation help contents for the respective products.
   - **Release Notes** to view the release notes content.
   - **Read Me** to view the read me content.
   - **What’s New** to view the what’s new content.

### Note
You can explore source only when you have source license and installed the source add-on setup.

## Checking Prerequisites

### Tools and Utilities
The dashboard provides easy access to utilities and tools such as:
- **Sales**: Access sales modules.
- **Contact Support**: Contact customer support.
- **Recheck**: Recheck required prerequisites.
- **Administrator Level Access Required**: Indicates admin-level permissions needed for certain features.

## Copyright Notice
Copyright 2001-2013 Syncfusion Inc. All rights reserved.

## Further Resources
The dashboard includes quick links to essential resources:
- **Online Samples**: View sample applications developed using Essential Studio controls.
- **Explore Source**: Access source code if you have installed the source add-on setup.
- **Online Documentation**: Comprehensive help documentation for Syncfusion products.
- **Release Notes**: Updates and changes in the latest releases.
- **Read Me**: Access documentation or notes for the selected product.
- **What’s New**: View the latest features and enhancements in the current version.

<!-- tags: [product, module, control, api, version?] keywords: [essential studio, mobile mvc, mvc 4, client-side rendering, mobile web app, iOS, Android, Windows Phone, Syncfusion Winforms] -->
```

---

<!-- 페이지 57 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_078.jpeg
document_name: common
page_number: 078
page_id: common#page_078
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:46Z
fidelity: lossless
-->

# Figure 73: Launch Assembly Manager

## Overview
- This section provides instructions for opening the Assembly Manager utility in Syncfusion Studio.
- The Assembly Manager is used to resolve conflicts between different Syncfusion assemblies or frameworks.
- Includes an alternative method to launch the Assembly Manager from the installation directory.

## Content

4. **The Syncfusion Assembly Manager x.x.x.x window opens.**

### Note:
You can also open the Assembly Manager from the following location:

```
(Installed location)\Syncfusion\Essential Studio\x.x.x.x\Utilities\Assembly
Manager\AssemblyManagerWindows.exe
```

## API Reference
(not applicable for this specific page segment)

## Code Examples
(not applicable for this specific page segment)

## Page-level Navigation/TOC
(not applicable for this specific page segment)

## Cross References
- **See also:** Multi-Target Manager, Assembly Conflict Resolution

<!-- tags: [syncfusion, essential studio, assembly manager, multi-target manager, conflict resolution, winforms] keywords: [launch, essential studio, assembly manager, multi-target manager, conflict, resolution, version 11.4.0.26] -->
```

---

<!-- 페이지 58 -->

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

---

<!-- 페이지 59 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: common
page_number: 086
page_id: common#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:15Z
fidelity: lossless
-->

# Essential Common

## Overview
- Describes the configuration options for building assemblies in Syncfusion Winforms using .NET Framework versions.
- Details the Product, Platform Type, Assembly Type, Dependencies, Strong Key, and Output settings.
- Explains the default selections and how to customize these settings for specific build requirements.

## Content

### Framework Version
The Framework Version group box provides four option buttons: .NET 2.0, .NET 3.5, .NET 4.0, and .NET 4.5. If Visual Studio 2012 is not installed, the .NET 4.0 option is selected by default. If Visual Studio 2010 is not installed, .NET 3.5 is selected by default. If Visual Studio 2008 is not installed, .NET 2.0 is selected by default. You can change the default option by clicking another option button. The specified version of the .NET Framework is used to rebuild the assemblies.

### Product
The Product group box includes a drop-down list box where the default selection is "All." You can change the default option by selecting one of the products in the list box.

### Platform Type
Syncfusion products utilize a common base library forming the basis for Windows and Web variants. The library category for the build is specified using the Product Type. This frame offers eight option buttons, with "All" selected by default. You can select the required product's option button to perform the build operation.

**Note:** Assemblies that are not built and pre-compiled assemblies with the product will automatically be used.

### Assembly Type
This frame includes two option buttons: Debug and Release. Debug is selected by default. To choose the release mode for the assembly, select "Release." Here, the user can switch between Debug and Release modes for product configurations. Building the debug version allows stepping into Syncfusion assemblies during application debugging.

### Dependencies
This section allows you to specify whether dependent assemblies of the product need to be used. If the "Use PreBuilt Dependencies" check box is selected, the dependent assemblies from the selected Product frame will be taken from the "Pre-Compiled Assemblies" folder, which exists under the installed location. Rebuilding assemblies can be restricted to specific assemblies by enabling pre-built dependencies, in which case other assemblies would use precompiled variants installed with the product.

### Strong Key
This feature enables the installation of compiled assemblies in the Global Assembly Cache (GAC). Select the "Use Strong Key" check box and choose a `.snk` file to achieve this.

### Output

## API Reference (if applicable)
- Refer to the Syncfusion Winforms documentation for specific namespace and class references for configuration options and build parameters.

## Code Examples (multi-language supported)
- Implement configuration settings programmatically by utilizing the relevant namespaces and settings documented in the Syncfusion Winforms SDK.

## Page-level Navigation/TOC (if applicable)
- Refer to the table of contents or navigation within the Syncfusion Winforms documentation for further details on related topics.

## Cross References
- See also: Syncfusion documentation for detailed instructions on build configurations and assembly management.

<!-- tags: [Syncfusion, Winforms, assembly, configuration, build, .NET Framework] keywords: [Framework Version, Product, Platform Type, Assembly Type, Dependencies, Strong Key, Output] -->
```

---

<!-- 페이지 60 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_090.jpeg
document_name: common
page_number: 090
page_id: common#page_090
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:34Z
fidelity: lossless
-->

# Essential Common

## Overview

- Steps to manage and copy product keys using Syncfusion License Manager.
- Instructions for removing and copying product keys.
- Note on logging when a product key has been added.

## Content

### Managing Product Keys

**Figure 83: Remove Key**

![](https://i.imgur.com/[figurereplacement].png)

6. Click **Remove Key**. The selected key will be removed.

**Note:** The removal is reflected in the log if the product key was already added.

### Copying a Product Key

You can copy the product key from the License Manager window to the clipboard. The following are the steps to copy the license key:

1. Open the Syncfusion License Manager dialog.
2. Select the required key to be removed. The selected key will be highlighted.

Click **Copy Key**. The selected key is copied. You can paste the key in the required place.

## API Reference (if applicable)

No specific API methods or references are mentioned in this section.

## Code Examples (multi-language supported)

No code examples are provided in this section.

## Page-level Navigation/TOC (if applicable)

No local Table of Contents is present on this page.

## Cross References

No cross-references are explicitly mentioned on this page.

<!-- tags: [syncfusion-sdk, license-manager, product-key, version-11.4.0.26] keywords: [product key, license manager, syncfusion winforms, remove key, copy key] -->
```

---

<!-- 페이지 61 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_094.jpeg
document_name: common
page_number: 094
page_id: common#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:45Z
fidelity: lossless
-->

# Assembly Management

## Overview

- Utility for resolving assembly conflicts between different frameworks of Syncfusion assemblies.
- Accessible via the "Utilities" menu in the program interface.

## Content

### Interface Overview

The interface includes two primary options for managing assemblies:

1. **Multi-Target Manager**
   - **Description:** Use Multi-Target Manager to resolve an assembly conflict between two different frameworks of Syncfusion assemblies.
   - **Action Button:** "Launch"

2. **Assembly Manager**
   - **Description:** Use Multi-Target Manager to resolve an assembly conflict between two different frameworks of Syncfusion assemblies.
   - **Action Button:** "Launch"

Both options are highlighted with a green "Launch" button, indicating the user can initiate the respective tool from this interface.

**Figure 87: Assembly Management**

![Assembly Management Interface](https://example.com/assembly-management-interface.png)
*Figure 87: Assembly Management*

### Alternative Access Method

**Note:** You can also open the Multi-Target Manager from the following location:

`(Installed location)\Syncfusion\Essential Studio\x.x.x.x\Utilities\MultiTargetManager\MultiTargetManager.exe`

### Dialog Box

4. The **Essential Studio MultiTarget Manager x.x.x.x** dialog box opens.

## API Reference

### Multi-Target Manager

- **Purpose:** Resolves assembly conflicts between two different frameworks of Syncfusion assemblies.

### Assembly Manager

- **Purpose:** Resolves assembly conflicts between two different frameworks of Syncfusion assemblies.

## Code Examples

No specific code examples are provided in this section.

## Page-level Navigation/TOC

- Overview
- Interface Overview
- Alternative Access Method
- Dialog Box

## Cross References

- See also: "Utilities" menu in the program interface.

<!-- tags: [assembly management, multi-target manager, syncfusion studio, assembly conflicts, dialog box] keywords: [multi-target manager, assembly manager, essential studio, utilities, access required] -->
```

---

<!-- 페이지 62 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_098.jpeg
document_name: common
page_number: 098
page_id: common#page_098
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:57Z
fidelity: lossless
-->

## 2 Orubase Studio

### 2.1 Overview

Orubase is Syncfusion's framework for developing mobile enterprise applications using a common ASP.NET MVC code base. Orubase helps build apps for mobile devices running Apple iOS, Google Android, and Microsoft Windows Phone.

### 2.2 Step-by-Step installation

The following procedure illustrates how to install the Orubase studio Setup:

1. Double-click the **Syncfusion Orubase Setup** file. The **Self-Extractor wizard** opens and extracts the package automatically.

![Extracting Setup](attachment:WinZip%20Self-Extractor.png)

**Figure 91: Extracting Setup**

2. When the unzip operation is complete, the **Syncfusion Orubase Studio Setup** dialog box opens.

<!-- tags: [syncfusion-sdk, WinForms, Orubase, installation] keywords: [syncfusion, Orubase, mobile applications, ASP.NET MVC, self-extractor, Windows Installer, setup dialog, extraction, WINZIP] -->
```

---

<!-- 페이지 63 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_102.jpeg
document_name: common
page_number: 102
page_id: common#page_102
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:06Z
fidelity: lossless
-->

## Install and Configure the Setup

### Overview

- This section guides you through the installation process of Syncfusion Orubase Studio.
- It highlights the selection of the installation folder and samples folder during the setup process.

## Content

1. **Select the Installation Folder**
   - This screen allows you to choose the folder where the application will be installed.
   - The default folder path provided is:
     ```
     C:\Program Files (x86)\Syncfusion\Orubase Studio\1.1.0.69\
     ```
   - You can change the folder by manually entering a path or by clicking the "Browse..." button.

2. **Steps to Install**
   - **Welcome** (Step 1): Introduction to the installation process.
   - **Collecting Information** (Step 2): Selects the installation folder.
   - **Installing** (Step 3): Begins the installation process with detailed progress information.
   - **Completed** (Step 4): Shows the success message after the installation is complete.

3. **Navigating Installation Screens**
   - **Figure 95: Select the Installation Folder screen** 
     - Displays the interface where you can select the installation folder.
   - **Click Next**: After selecting the installation folder, click "Next" to proceed to the next screen.

4. **Select the Samples Folder**
   - Upon clicking "Next," the "Select the Samples Folder" screen will open, allowing you to specify the location for samples if desired.

## Page-level Navigation/TOC (if applicable)

- **Step-by-Step Installation Guide**
  - Welcome
  - Collecting Information
  - Installing
  - Completed

## Cross References

- Refer to the official Syncfusion documentation for additional setup options and configurations.

<!-- tags: [syncfusion, orubase studio, installation, setup, windows forms] keywords: [installation folder, samples folder, wizard, setup guide] -->
```

---

<!-- 페이지 64 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_106.jpeg
document_name: common
page_number: 106
page_id: common#page_106
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:19Z
fidelity: lossless
-->

## Essential Common

### Overview
- This section documents the installation completion of Syncfusion Orubase Studio.
- The setup wizard has completed all necessary steps for installation.
- The user can now proceed to open the Orubase Dashboard using the provided options.

### Installation Completion

#### Installation Steps Summary
The installation process consists of four main steps, each marked with a different color:
1. **Welcome**: Initial welcome screen.
2. **Collecting Information**: Information gathering phase.
3. **Installing**: Software installation phase.
4. **Completed**: Final completion screen.

#### Final Installation Screen
The final screen confirms the successful completion of the installation:
- **Date**: 02/12/2013
- **Version**: 1.1.0.69
- **Options**:
  - **Run Dashboard**: Checked, indicating the Orubase Dashboard will open.
  - **View Log file**: Available but unchecked.

#### User Instructions
- Click **Finish** to exit the setup wizard.
- Open the **Orubase Dashboard** by selecting the **Run Dashboard** option.

### Running the Dashboard
Once the installation is complete, follow these steps to open the Orubase Dashboard:
1. Click **Finish** to exit the setup wizard.
2. Select **Run Dashboard** to open the Orubase Dashboard.

## Summary
The Syncfusion Orubase Studio 1.1.0.69 has been successfully installed. The user can now open the Orubase Dashboard by following the provided instructions.

<!-- tags: [Syncfusion Winforms, installation, Orubase Studio, setup wizard] keywords: [Syncfusion, Orubase Studio, installation, setup wizard, dashboard, version, log file] -->
```

---

<!-- 페이지 65 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_110.jpeg
document_name: common
page_number: 110
page_id: common#page_110
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:31Z
fidelity: lossless
-->

## Setup Wizard Overview

- This page describes the installation process for Syncfusion Metro Studio 2.
- The setup wizard guides users through the installation steps, allowing them to proceed or cancel at any time.

## Content

### Setup Wizard

![](Syncfusion Metro Studio Setup)
Figure 103: Setup Wizard

The setup wizard screen for Syncfusion Metro Studio 2 displays the following stages:
- **Welcome**
- **Collecting Information**
- **Installing**
- **Completed**

The screen informs the user that the setup wizard will install Metro Studio on their computer. It provides options to click "Next" to continue or "Cancel" to exit the setup wizard. The user's progress is visually indicated on the left side of the screen.

### Instructions

1. **Welcome Screen:**
   - The setup wizard begins with a welcome screen, which introduces the product and provides an overview of the installation process.

2. **Collecting Information:**
   - The next step prompts the user to provide necessary information required for the installation.

3. **Installing:**
   - This stage captures the installation process, where the software components are being placed on the user's computer.

4. **Completed:**
   - Once the installation is successful, a completion screen is displayed indicating that the setup is complete.

#### Interaction Options
- **Click "Next":**
  - Advances the user to the next stage in the setup process.
- **Click "Back":**
  - Allows the user to navigate back to the previous step if needed.
- **Click "Cancel":**
  - Exits the setup wizard at any point.

**Figure 103** shows the initial stage of the setup wizard where the user can choose to proceed or exit. The "Next" button is highlighted, indicating the recommended action to move forward in the installation process. The user information screen is opened after clicking "Next," as per the instructions provided.

```markdown
4. Click Next. The User Information screen opens.
```

## API Reference
No API-related content is directly visible on this page.

## Code Examples
No code examples are present on this page.

## Page-level Navigation/TOC
No local Table of Contents or navigation elements are present on this page.

## Cross References
No explicit cross-references to other pages or sections are provided on this page.

<!-- tags: [Syncfusion, Winforms, Installation, Setup Wizard, Metro Studio, User Interface, Documentation] keywords: [installation, setup wizard, Metro Studio, user information, next step, cancel, collect information, progress, completion screen, software setup] -->
```

---

<!-- 페이지 66 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_114.jpeg
document_name: common
page_number: 114
page_id: common#page_114
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:49Z
fidelity: lossless
-->

## Essential Common

### Setup Type

**Figure 107: Setup Type**

The installation process for Syncfusion Metro Studio 2.0.1.1 is shown in Figure 107. The following steps describe how to complete the installation setup.

1. **Select the Install Folder:**
   - This is the folder where your application will be installed.
   - To install in the default folder, click `Next`. To install in a different folder, enter the required path below or click `Browse`.

---

### Installation Steps

10. Click **Next**. The **Ready to Install** dialog opens.

## Page-level Navigation/TOC (if applicable)

- Setup Type

## Cross References

See also:
- Installation Overview

## RAG Annotations

<!-- tags: [Syncfusion, Winforms, Installation, Setup, Setup Type] keywords: [install folder, Syncfusion Metro Studio, default folder, browse, Ready to Install, Next] -->
```

---

<!-- 페이지 67 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_118.jpeg
document_name: common
page_number: 118
page_id: common#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:58Z
fidelity: lossless
-->

## Overview

- The document outlines the process of completing the installation of Syncfusion Metro Studio 2.
- Describes the functionality provided by Metro Studio Dashboard after the installation of the Metro Studio Source Code Add-on.
- Highlights the creation of icons using Metro Studio Dashboard.

## Content

### Installation Completion

#### Figure 111: Installation Completed

![Installation Completed](#)

The Setup has finished installing Syncfusion Metro Studio on your computer. Click Finish to exit Setup. The option to run Metro Studio is pre-selected.

#### Using Metro Studio Dashboard

Once the Metro Studio Source Code Add-on is installed, Metro Studio Dashboard provides the option to create icons.

#### Metro Studio Dashboard Interface

![Metro Studio Dashboard](#)

- **Icon Category**: Medical
- **Available Icons**:
  - Ambulance
  - Appointment
  - Band Aid
  - Blood
  - Dental
  - Doctor
  - Dropper
  - Eyehospital
  - First Aid
  - Heart
  - Heart ECG
  - Hospital

#### Creating a Project

The dashboard includes a button to "Drop to create a project."

---

### Page-Level Navigation

This section describes the installation and use of Syncfusion Metro Studio 2, focusing on the features available after adding the Metro Studio Source Code Add-on.

---

## API Reference

- **Namespace**: Syncfusion.Windows
- **Class**: MetroStudioDashboard
- **Methods**:
  - `OpenIconEditor()`
  - `RunMetroStudio()`
- **Properties**:
  - `IsAddOnInstalled`
  - `CurrentIconCategory`

---

## Code Examples

```csharp
using Syncfusion.Windows;

// Check if the add-on is installed
if (MetroStudioDashboard.IsAddOnInstalled)
{
    // Open the icon editor
    MetroStudioDashboard.OpenIconEditor();
}
```

---

## Cross References

- Refer to the "Installing Syncfusion Metro Studio" section in the main guide for detailed installation instructions.
- See the "Customizing Icons" section for more information on creating and editing icons using Metro Studio Dashboard.

---

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Metro Studio, Installation, Icon Creation, Dashboard] keywords: [Syncfusion Metro Studio 2, Add-on, Installation Completion, Icon Editor, Metro Studio Dashboard] -->
```

---

<!-- 페이지 68 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_122.jpeg
document_name: common
page_number: 122
page_id: common#page_122
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:12Z
fidelity: lossless
-->

## Content

### 3. The Choose Toolbox Items window opens.

**Figure 114: Choose Items**

**Figure 115: Choose Toolbox Items**

4. Select all the Syncfusion assemblies and then click **OK**. Assemblies will be copied to the newly created Syncfusion toolbox tab.

### 4.2 How to remove the licensing error that pops up each time the application is run

**Applicable to all the older Syncfusion versions (before 8.2.0.x):**

The following information provides troubleshooting tips that will help configure the system for a specific version of Syncfusion Essential Studio, and to avoid common licensing issues due to version conflicts.

1. Open the project in any text editor and ensure that only one **Syncfusion.Core** entry is referenced. If more than one entry is available, remove it.
```markdown

<!-- tags: [syncfusion, winforms, licensing, toolbox] keywords: [choose items, Syncfusion, licensing error, troubleshooting, Syncfusion.Core, version conflicts] -->
```

---

<!-- 페이지 69 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_126.jpeg
document_name: common
page_number: 126
page_id: common#page_126
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:21Z
fidelity: lossless
-->

### Essential Common

#### Overview
- This page discusses the issues related to licensing in Syncfusion applications and provides solutions for embedding licensing information into the output EXE.
- It covers how to resolve licensing errors by rebuilding the application and ensuring compatibility with the correct Syncfusion version.
- It also explains the process for resolving licensing issues for newer Syncfusion versions (8.2.0.x and above), where runtime licensing is no longer required.

## Content

### Licensing Issues and Resolution

This message appears because the `.exe.licenses` file shown in the following screenshot has been modified to include the Syncfusion licensing information. To embed this information into the output exe, the user needs to rebuild the application. Verify whether this file has the Syncfusion version information for which the user has the license. If the file has information for any other version, the **Licensing Error** message will open every time the user runs the application.

![Figure 120: Licensing Error message](https://example.com/image_source)

### Steps to Resolve Licensing Errors

12. Rebuild and run the application again. The above-mentioned messages should no longer be displayed.

### Resolving the Licensing Issues for the latest Syncfusion versions (Applicable to all Syncfusion versions from 8.2.0.x):

**Syncfusion had removed run-time licensing for all Essential Studio products from the version 8.2.0.x.** It is not required to embed the `license.licx` file in your project. Remove the `license.licx` file from the project if it was already added.

### Steps to Resolve Licensing Issues for the latest Syncfusion versions:

1. Ensure that the unlock key for the respective version has been properly installed in the registry using the License Manager utility from the dashboard.

## API Reference

None

## Code Examples

None

## Page-level Navigation/TOC

- Licensing Issues and Resolution
- Steps to Resolve Licensing Errors
- Resolving the Licensing Issues for the latest Syncfusion versions

### Cross References

See also: Syncfusion license manager, `.exe.licenses` file, `license.licx` file

<!-- tags: [product, module, control, api, version?] keywords: [license, licensing, exe.licenses, license.licx, registry, Syncfusion, resharper] -->
```

---

<!-- 페이지 70 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_130.jpeg
document_name: common
page_number: 130
page_id: common#page_130
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:35Z
fidelity: lossless
-->

### Overview

The document describes resolving access denied errors when accessing essential Studio Windows Forms samples and manually uninstalling the Syncfusion Setup in cases where the uninstall utility is unavailable.

### Content

#### Essential Studio Sample Browser Access

- **Description**:
  - The image shows an "Access Denied" message indicating that the essential Studio Windows Forms Edition Sample Browser was unable to access the folder containing sample files.
  - Error message details:
    - Folder path: `C:\Users\Administrator\Documents\Syncfusion\EssentialStudio\8.1.0.30\Windows`.
    - The issue occurs because the installation of essential Studio was performed under a different user account than the current user account.

#### Solution for Access Denied Error

- **Action**:
  - The administrator should provide access privileges to the folder path for the non-admin user.

---

#### 4.4 How to Uninstall the Syncfusion Setup Manually

- **Purpose**:
  - To uninstall the Syncfusion Setup manually when the uninstall utility is not available due to installation crashes or other issues.

- **Steps to Uninstall Manually**:
  1. **Download and Install Windows Installer Cleanup Utility**:
     - Obtain and install the Windows Installer cleanup utility from the following link: [Windows Installer cleanup](http://Windows%20Installer%20cleanup).
  2. **Remove Syncfusion Product-related Installers**:
     - Use the Windows Installer Cleanup utility to remove the Syncfusion product-related installers for the version being uninstalled.

---

## API Reference

Not applicable in this context.

## Code Examples

None.

## Tags and Keywords

<!-- tags: essentialStudio, windowsForms, sampleBrowser, accessDenied, uninstallUtility, WindowsInstallerCleanup, SyncfusionWinforms, setupUpgrade module: documentation, troubleshooting, uninstallation -->
```

---

<!-- 페이지 71 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_134.jpeg
document_name: common
page_number: 134
page_id: common#page_134
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:47Z
fidelity: lossless
-->

## Essential Common

### Overview

- Click Start Converting Files.
- After the conversion, new Resx files maintain the original names.
- Original files are renamed with a `.old` suffix.

### Content

#### 4.6 Why is the unlock key displayed as invalid when installing the setup?

Unlock key can be validated as invalid for two reasons. They are:

- When you install a particular version setup with a mismatched version unlock key. Ensure you enter the correct unlock key for the respective version.
- If the unlock key code has been altered or spaced improperly. Ensure you copy the entire key correctly without any spacing.

---

Early version of 11.1.** 

![Syncfusion Essential Studio Setup - 10.2.0.15](./Syncfusion_Essential_Studio_Setup.png)

---

## Page-level Navigation/TOC (if applicable)

- **4.6 Why is the unlock key displayed as invalid when installing the setup?**

## Cross References

- This section explains the potential reasons for an unlock key validation failure.

---

<!-- tags: [product, essential studio setup, unlock key, version mismatch, validation, syncfusion, winforms] keywords: [unlock key, invalid key, version mismatch, Essential Studio, syncfusion setup, free evaluation key] -->
```

---

<!-- 페이지 72 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_138.jpeg
document_name: common
page_number: 138
page_id: common#page_138
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:57Z
fidelity: lossless
-->

## Essential Common

### Overview
- This page provides instructions for generating localized strings and satellite assemblies using a .csv file for a WPF application.
- It explains the process of changing language settings from English to French for specific control-related texts.
- Instructions include creating and managing directory structures to handle localized resources effectively.

### Content

#### ResourceStrings.csv

The following table shows the contents of `ResourceStrings.csv`:

| Key | Type | Enabled | Value |
| --- | --- | --- | --- |
| Syncfusion.Tools.system:String\_1 | None | TRUE | TRUE | S\_how Quick Access Toolbar below the Ribbon |
| Syncfusion.Tools.system:String\_1 | None | TRUE | TRUE | \_Add &gt;&gt; |
| Syncfusion.Tools.system:String\_1 | None | TRUE | TRUE | \_Remove |
| Syncfusion.Tools.system:String\_1 | None | TRUE | TRUE | Re\_set |
| Syncfusion.Tools.system:String\_1 | None | TRUE | TRUE | \_Modify... |
| Syncfusion.Tools.system:String\_1 | None | TRUE | TRUE | \_Choose commands from |
| Syncfusion.Tools.system:String\_2 | None | TRUE | TRUE | Qui\_k Access Toolbar |
| Syncfusion.Tools.system:String\_2 | None | TRUE | TRUE | Remove from Quick Access ToolBar |
| Syncfusion.Tools.system:String\_2 | None | TRUE | TRUE | Calendrier |
| Syncfusion.Tools.system:String\_2 | None | TRUE | TRUE | Regarder |
| Syncfusion.Tools.system:String\_2 | None | TRUE | TRUE | aucun |
| Syncfusion.Tools.system:String\_2 | None | TRUE | TRUE | aujourd'hui |
| Syncfusion.Tools.AccessTodayTexButton | None | TRUE | TRUE |  |
| Syncfusion.Tools.AccessTodayTexNone | FALSE | TRUE | 0 |
| Syncfusion.Tools.AccessTodayTexNone | FALSE | TRUE | 40 |
| Syncfusion.Tools.CustomizeQATTText | TRUE | TRUE |  |
| Syncfusion.Tools.CustomizeQATT | None | FALSE | TRUE | 3,0,0,0 |
| Syncfusion.Tools.CustomizeQATT | None | TRUE | TRUE | Bold |
| Syncfusion.Tools.CustomizeQATT | None | FALSE | TRUE | Center |

**Note:** We have changed the language from English to French for Calendar control-related texts alone.

#### Steps to Generate Localized Satellite Assembly

1. **Modify the .csv file**: Update the `ResourceStrings.csv` file to include translations for the required strings.
2. **Generate the localized satellite assembly**: Use the modified .csv file to generate the satellite assembly for the application.
3. **Install the assembly**: Install the generated satellite assembly in your application.
4. **Open command prompt**: Navigate to the `en-US` directory.
5. **Create a directory for French (fr-CH)**: Under the `Bin\Debug` folder, create a new directory named `fr-CH` using the `md fr-CH` command.

##### Note
- The directory name should follow a proper culture name.

#### Generating Culturespecific Assembly

6. **Generate your own culture-specific assembly**: Use the following command from the `en-US` folder:
   ```bash
   LocBaml /generate /tran: resourceStrings.csv /out:../fr-CH /cul:fr-CH
   Syncfusion.Tools.WPF.Resources.dll
   ```

#### Verifying the Generated Assembly

- After running the command, verify that the satellite assembly is generated and is located under the `fr-CH` folder.

#### Running the Application with Localization

8. **Modify `App.xaml` to set the CurrentUICulture**: Update the `CurrentUICulture` property in the `App.xaml` file by setting it to `fr-CH`.

**Example C# Code**:
```csharp
public App()
{
    // Code omitted for brevity
}
```

### Conclusion

By following the steps outlined in this document, you can generate and install a localized satellite assembly for your WPF application. This ensures that the application displays the correct language-specific resources, enhancing user experience.

### Tags and Keywords
<!-- tags: [Localization, WPF, Satellite Assembly, Resource Files, Culture Support, Syncfusion Winforms] keywords: [ResourceStrings.csv, culture-specific assembly, fr-CH, en-US, LocBaml, CurrentUICulture, App.xaml] -->
```

---

<!-- 페이지 73 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_142.jpeg
document_name: common
page_number: 142
page_id: common#page_142
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:22Z
fidelity: lossless
-->

## Essential Common

### Figure 134: Customization Dialog for Invariant Culture

![Figure 134](https://i.imgur.com/K0Lq0Xw.png)

### Figure 135: French Culture assigned as Current UI Culture for Customization Dialog

![Figure 135](https://i.imgur.com/zLHh9Yz.png)

### 4.7.3 Windows and ASP.NET

The Windows and ASP.Net products have extended support for Localization.Samples and description is available in the following locations.

#### Product Information

| **Product**                     | **Sample location**                                                                                          |
|---------------------------------|-------------------------------------------------------------------------------------------------------------|
| Tools[ASP.NET]                 | [http://samples.syncfusion.com/ASPNET/8.4.0.10/Web/Tools.Web/samples/3.5/EditorsPackage/Spell%20Check/Localization/cs/SpellCheckWithContextMe](http://samples.syncfusion.com/ASPNET/8.4.0.10/Web/Tools.Web/samples/3.5/EditorsPackage/Spell%20Check/Localization/cs/SpellCheckWithContextMe) |

## Page-Level Navigation/TOC

1. **Chapter 4: Essential Common**
   - Subsection 4.7: [Unclear]
     - **4.7.3:** Windows and ASP.NET

## Cross References

- See also: Syncfusion Localization Samples, Windows and ASP.NET products

## RAG Annotations
<!-- tags: [windows, asp.net, localization, sample, syncfusion, 11.4.0.26] keywords: [customization dialog, invariant culture, french culture, ui culture, localization, wizards, windows, asp.net, essential common] -->
```

---

<!-- 페이지 74 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_003.jpeg
document_name: common
page_number: 003
page_id: common#page_003
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:58:45Z
fidelity: lossless
-->

# Contents

## Essential Common

### 1.13 Utilities

- **1.13.1 Dashboard**: 70
- **1.13.2 Assembly Manager**: 77
- **1.13.3 Build Manager**: 83
- **1.13.4 License Manager**: 87
- **1.13.5 Toolbox Configuration**: 91
- **1.13.6 Multi-Target Manager**: 93
- **1.13.7 Project Migration**: 95
  - **1.13.7.1 Command Line**: 96
- **1.13.8 Project Templates**: 97

### 2 Orubase Studio

- **2.1 Overview**: 98
- **2.2 Step-by-Step installation**: 98

### 3 Metro Studio

- **3.1 Overview**: 108
- **3.2 Step-by-Step Installation**: 108

### 4 Frequently Asked Questions

- **4.1 How to Configure the Toolbox of Visual Studio Manually**: 120
  - **4.1.1 Toolbox Configuration Utility**: 120
  - **4.1.2 Manually Configuring VS Toolbox**: 120
- **4.2 How to remove the licensing error that pops up each time the application is run**: 122
- **4.3 How to overcome Sample Browser Access Denied Error for a Non-Admin User**: 129
- **4.4 How to uninstall the Syncfusion Setup manually**: 130
- **4.5 How to upgrade the project into a new Syncfusion version**: 132
  - **4.5.1 Upgrade the Project Using Project Migration Utility**: 132
  - **4.5.2 Upgrading the Projects Manually**: 132
- **4.6 Why is the unlock key displayed as invalid when installing the setup?**: 134
- **4.7 How to implement Localization Support**: 136
  - **4.7.1 WPF**: 136
  - **4.7.2 Silverlight**: 139
  - **4.7.3 Windows and ASP.NET**: 142
- **4.8 How to redistribute an application on the client machine**: 143

<!-- tags: [syncfusion, winforms, user guide, installation, configuration, troubleshooting, metro studio, syncfusion sdk] keywords: [toolbox configuration, project migration, localization, redistribution, syncfusion setup, visual studio toolbox, licensing error, unlock key, step-by-step installation] -->
```

---

<!-- 페이지 75 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_007.jpeg
document_name: common
page_number: 007
page_id: common#page_007
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:04Z
fidelity: lossless
-->

## Overview
- Guide on installing and configuring Syncfusion Essential Studio using the WinZip self-extractor utility.
- Instructions include entering user details and validating the unlock key to proceed with the installation.

## Content

### Installation and Configuration

#### Figure 1: Self-Extractor
- **Note:** The WinZip self-extractor will extract the `syncfusionessentialstudio_(version).exe` dialog, displaying the unzip operation of the package.

#### Figure 2: User Information

##### Input Fields
- **User Name:** (prefilled as "Syncfusion")
- **Organization:** (prefilled as "Syncfusion")
- **Unlock Key:** (empty text box, required field marked with an asterisk *)

##### Buttons
- **Free Evaluation Key:** Link to obtain an evaluation key.
- **Next:** Button to proceed after entering the required information.

##### Instruction Steps
1. Enter your **User Name**, **Organization**, and **Unlock Key** in the corresponding text boxes provided.
2. Click **Next**.

##### Validation and Agreement
- **Note:** The unlock key is validated and the preceding License agreement screen opens.

### Legal and Copyright

- **Copyright Statement:** © 2013 Syncfusion. All rights reserved.

## RAG Annotations
<!-- tags: [syncfusion, essential studio, winforms, installation, configuration, self-extractor] keywords: [winzip, license agreement, unlock key, evaluation key, user information, organization, syncfusion essential studio] -->
```

---

<!-- 페이지 76 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_011.jpeg
document_name: common
page_number: 011
page_id: common#page_011
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:15Z
fidelity: lossless
-->

# Common

## Overview
- Essential Studio installation in progress.
- Highlighting technical support as unmatched in the industry.

## Content

### Installing Essential Studio

The following figure shows the installation process of Essential Studio:

<div align="center">
<img src="Essential_Studio_Installation.png" alt="Figure: Installing Essential Studio">
</div>

**Figure 6: Installing Essential Studio**

The installation window displays the following information:

- **Version:** 11.1.0.21
- **Date:** 01/30/2013
- **Status:** InstallInitialize

A progress bar indicates the current installation status, and a "CANCEL" button is available for aborting the installation.

## API Reference

This section provides references to the specific APIs or components related to the installation process. Further details can be found in the official Syncfusion documentation.

## Code Examples

No specific code examples are provided in this section. Refer to the Syncfusion Winforms documentation for more detailed examples related to Essential Studio usage.

## Cross References

See also:
- Syncfusion Winforms Documentation for detailed installation and usage instructions.

<!-- tags: [syncfusion, winforms, essential studio, installation, technical support] keywords: [syncfusion, essential studio, installation, unmatched support, 11.1.0.21, 01/30/2013, InstallInitialize, cancel button] -->
```

---

<!-- 페이지 77 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: common
page_number: 015
page_id: common#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:25Z
fidelity: lossless
-->

## Content

### Figure 9: User Information

```html
<div style="position: relative; overflow: hidden;">
  <img src="mock-up-user-information-page.png" alt="Figure 9: User Information" width="100%" />
  <div style="position: absolute; top: 0; right: 0;">
    <span style="font-size: 12px;">Version: 11.1.0.21</span><br />
    <span style="font-size: 12px;">Date: 02/14/2013</span>
  </div>
</div>
```

The figure above shows the user information form with the following fields:

- **User Name**: Input field with "Syncfusion" as a placeholder.
- **Organization**: Input field with "Syncfusion" as a placeholder.
- **Unlock Key**: Input field marked with a red asterisk (*) indicating it is mandatory.
- **Free Evaluation Key**: A button labeled "Free Evaluation Key."
- **NEXT**: A button labeled "NEXT."

### Steps to Enter User Information

1. **Enter User Information**:
   - **User Name**, **Organization**, and **Unlock Key** should be entered in the corresponding text boxes as provided.

2. **Click Next**:
   - After filling in the required fields, click the **NEXT** button to proceed.

### Handle the Unlock Key

- **Note**: The unlock key is validated, and the preceding license agreement screen opens.

## Page-level Navigation/TOC (if applicable)

- This section outlines the user information registration process for Syncfusion Mobile MVC.
- It highlights the necessary fields and the actions required to move forward.

## Cross References

- This section is part of a larger guide focused on the configuration and usage of Syncfusion WinForms controls.
- Refer to other sections for additional details on license validation and further setup steps.

<!-- tags: syncfusion, mobile mvc, user information, license agreement, unlock key, user registration, version: 11.1.0.21, 2013 document, winforms, product setup keywords: user information, unlock key, license agreement, registration, next button, syncfusion mobile mvc -->
```

---

<!-- 페이지 78 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_019.jpeg
document_name: common
page_number: 019
page_id: common#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:39Z
fidelity: lossless
-->



## Installation Completion

### Overview
- After installation, a completion screen is displayed, indicating successful installation of Syncfusion Mobile MVC.
- Options to run the dashboard or view the installation log are provided.
- The setup supports both GUI and command-line installations.

### Installation Complete Screen
![Installation Completed Screen](https://via.placeholder.com/600x400.png?text=Figure%2013:%20Installation%20Completed)

**Figure 13: Installation Completed**

#### Steps to Proceed
1. **Select the Launch Dashboard check box** to launch the Dashboard after installing.
2. **Click Finish**. Essential Studio is installed in your system, and the Syncfusion Essential Studio Dashboard is launched automatically.

### 1.3.3 Command Line

#### Overview
- The Syncfusion Essential Studio platform installer supports both installation and uninstallation through the command line. This section illustrates the command-line installation process.

#### 1.4.1.1 Command line installation

##### Steps for Silent Mode Installation
Follow the steps below to install through the command line in silent mode.

1. **Double-click the Syncfusion Essential Studio platform Setup file**. The self-Extractor wizard opens and extracts the package automatically.
2. **The SyncfusionEssentialStudio(platform)_(version).exe file will be extracted into the Temp folder.**
3. **Run %temp%.** The Temp folder will open. The SyncfusionEssentialStudio(platform)_(version).exe file will be available in one of the folders.

## API Reference (if applicable)

### Overview
- Additional API references and usage examples for command-line operations can be found in the official documentation. The specific code examples may include C# and VB.NET samples.

### Code Examples (multi-language supported)
- Example commands for silent installation using the command line.

## Page-level Navigation/TOC (if applicable)

### Overview
- This page details the installation completion process and provides steps for launching the Dashboard and utilizing command-line options. For further reference, see the related sections.

## Cross References

### Overview
- Refer to the main Syncfusion Winforms documentation for comprehensive details on the installation and configuration of the Syncfusion Essential Studio platform.

<!-- tags: [syncfusion, winforms, essential studio, installation, command line] keywords: [syncfusion winforms, essential studio, installation completion, command line install, silent mode, dashboard, finish] -->
```

---

<!-- 페이지 79 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_023.jpeg
document_name: common
page_number: 023
page_id: common#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:54Z
fidelity: lossless
-->

## Overview
- This page describes the steps for setting up the Syncfusion Essential Studio Source Code add-on for version 2013 Vol 1.
- It follows a setup wizard interface with stages for collecting information, installing, and completing the installation process.
- The document includes a visual guide for users to proceed through the wizard by clicking "Next."

## Content

### Welcome to the Setup Wizard

The image depicts the welcome screen of the Syncfusion Essential Studio Source Code add-on installer for version 2013 Vol 1. The setup wizard comprises several stages:

1. **Welcome**
   - Introduction to the installation process.

2. **Collecting Information**
   - Gathering necessary details for the installation.

3. **Installing**
   - Initiating the installation sequence.

4. **Completed**
   - Concluding the installation process.

The Setup Wizard will install the Essential Studio Source Code add-on on your computer. Users are prompted to click "Next" to continue with the installation or "Cancel" to exit the wizard. The version of the installer is indicated as 11.1.0.21, dated 27/02/2013.

### Step-by-Step Instructions

4. Once the welcome screen is displayed, click **Next**.  
   - The User Information screen will then open for further configuration.

### Figure 16: Setup Wizard
![Setup Wizard](image_url)  
This image provides a visual reference for users to follow the prompts accurately.

## Cross References
- For detailed steps after the User Information screen, see the specific sections in the documentation or user guide.

<!-- tags: [syncfusion, essential studio, winforms, setup wizard, version 2013 vol 1] keywords: [source code add-on, install, setup, version 11.1.0.21, user information] -->
```

---

<!-- 페이지 80 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: common
page_number: 027
page_id: common#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:06Z
fidelity: lossless
-->

# Essential Common

## Overview
- Describes the process to choose the preferred setup type for installing Syncfusion Essential Studio 2013 Vol 1.
- Highlights options for typical, custom, and complete setups.
- Guides users through the installation process with detailed steps.

## Content

### Installation Setup Types

The installation setup offers different options tailored to user needs:

1. **Welcome**
    - Begins the installation process.

2. **Collecting Information**
    - Gathers necessary information for installation.

3. **Installing**
    - Installs the selected program features.

4. **Completed**
    - Confirms the successful completion of the installation.

The user可以选择 one of the following setup types based on their requirements:

- **Typical**
    - Installs the most common program features.
    - Recommended for most users.
    - Suitable for those who want a streamlined installation process.

- **Custom**
    - Allows users to choose specific program features.
    - Recommended for advanced users.
    - Provides flexibility to select only the desired components.

- **Complete**
    - Installs all program features.
    - Requires the most disk space.
    - Suitable for users who want full access to all available features.

### Installation Steps

Once you have chosen your preferred setup type, follow these steps:

10. Choose your preferred setup type. For example, to install the complete setup, click **Complete**.
11. Click **Next**. The **Ready to Install** dialog opens.

### Example Image: Setup Type

![Setup Type](image.png)
*Figure 20: Setup Type*

This dialog outlines the three setup types available for installation:

- **Typical**: Installs the most common program features. Recommended for most users.
- **Custom**: Allows users to choose which program features will be installed and where they will be installed. Recommended for advanced users.
- **Complete**: All program features will be installed. Requires the most disk space.

The **Syncfusion Essential Studio Source code add-on installer Setup** interface guides users through the installation process, ensuring they select the appropriate setup type and proceed to installation.

## API Reference

This section does not contain any API-specific information but provides guidance on selecting and installing specific features during the setup process.

## Code Examples

The document does not provide any code examples but focuses on the installation setup process, helping users navigate through different installation options.

## Cross References

For additional information or detailed setup instructions, refer to the official Syncfusion documentation or support resources.

## RAG Annotations

<!-- tags: [installation, setup, syncfusion, essential studio, user guide] keywords: [setup types, typical, custom, complete, disk space, user preferences] -->
```

---

<!-- 페이지 81 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: common
page_number: 031
page_id: common#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:24Z
fidelity: lossless
-->

## Installing the Essential Studio Source Code Add-on

### Overview
- This section describes the installation process of the Essential Studio Source Code add-on.
- After installation, the Dashboard provides an option to explore the source code.

### Content

#### Installation Complete
![Syncfusion Essential Studio Source Code Add-on Install Wizard Completed](attachment.jpg#page_031)

*Figure 24: Installation Completed*

14. Once the Essential Studio Source Code add-on is installed, the Dashboard provides an option to explore source code.

### Older Version Reference
- This page is referring to the installation guide for the Syncfusion Essential Studio 2013, Version 1.

<!-- tags: [syncfusion, winforms, essential-studio, source-code-addon, installation, dashboard] keywords: [syncfusion essential studio, source code, add-on, installation, explore source code] -->
```

---

<!-- 페이지 82 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: common
page_number: 035
page_id: common#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:32Z
fidelity: lossless
-->

## Overview

- Syncfusion provides comprehensive documentation to help users understand and utilize their Essential Studio products effectively.
- The documentation includes both online and local resources to support different user needs and preferences.
- Figure 27: Offline User Guide illustrates the utility of accessing local documentation installed with Syncfusion's products.

## Content

### Online Documentation

#### Description
Syncfusion provides comprehensive documentation online to help you better understand their products. This can be accessed from the `Utilities > Documentation > Online Documentation` menu option.

#### Figure: Offline User Guide

- **Menu Structure**:
  - **File**
  - **Studio**
  - **Tools**
  - **Help**
  - **Updates**
  - **Registered User**
  - **Version - 11.1.0.21**

- **Navigation Path**:
  - **Essential Studio**
    - **Add-ons**
    - **Utilities**
      - **Toolbox Configuration**
      - **Assembly Management**
      - **Documentation**
      - **License Management**

- **Documentation Options**:
  - **Online Documentation**:
    - **User Guide**
    - **Class Reference**
  - **Local Documentation**:
    - **VS2005/VS2008 Class Reference and User Guide**
    - **VS2010 Class Reference**
    - **VS2010 User Guide**

#### Online Documentation Access
Syncfusion provides comprehensive documentation online to help you better understand their Essential Studio products. This can be accessed from the `Utilities > Documentation > Online Documentation` menu option.

### Local Documentation

#### Overview
Documentation pertaining to Syncfusion products can be installed with your copy of Syncfusion’s local resources. This includes:

- **VS2005/VS2008 Class Reference and User Guide**
- **VS2010 Class Reference**
- **VS2010 User Guide**

## API Reference

### Local Documentation Categories
The three categories of local documentation installed with Syncfusion products are:

- **VS2005/VS2008**:
  - Class Reference
  - User Guide
- **VS2010**:
  - Class Reference
  - User Guide

## Code Examples

No code examples are provided in this section. However, reference code and samples are typically available within the documentation and can be accessed online or locally.

## Page-level Navigation/TOC

- **Online Documentation**
- **Local Documentation**

### References

- **Online Documentation**: Accessible from `Utilities > Documentation > Online Documentation`.
- **Local Documentation**: Installed with Syncfusion’s products, providing comprehensive guides for different Visual Studio versions.

## RAG Annotations

<!-- tags: [Essential Studio, Online Documentation, Local Documentation, User Guide, Class Reference, Visual Studio] keywords: [Syncfusion, comprehensive documentation, essential studio, online documentation, local documentation, user guide, class reference, VS2005, VS2008, VS2010] -->
```

---

<!-- 페이지 83 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_039.jpeg
document_name: common
page_number: 039
page_id: common#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:49Z
fidelity: lossless
-->

# Essential Common

## Overview
- Welcome to the Syncfusion Essential Studio Link Install setup process for version 11.1.0.21.
- The setup involves collecting information, installing, and completing the process to unlock authorized features.
- The license agreement is the next step in the installation process.

## Content

### Syncfusion Essential Studio Link Install Setup
The setup interface is divided into four primary steps:

1. **Welcome**: Welcome message for the setup process.
2. **Collecting Information**: Collection of necessary information.
3. **Installing**: Actual installation of the software.
4. **Completed**: Confirmation that the installation is complete.

#### Screenshot of the Setup Interface
The setup interface displays the following details:
- **Header**: Welcome to the Syncfusion Essential Studio Link Install 2013 Vol. 1 Setup.
- **Message**: Thank you for the information provided. Authorized features have been unlocked. The Setup Wizard has the information needed to proceed with installation. Click Next to continue or Cancel to exit the Setup Wizard.
- **Information at the Bottom**: 
  - Date: 19/02/2013
  - Version: 11.1.0.21
- **Buttons**: 
  - Back
  - Next
  - Cancel

#### Steps to Proceed
7. **Click Next to continue with installation.** The License Agreement screen opens.

## Page-level Navigation/TOC (if applicable)
The current page provides instructions for the initial setup steps, directing the user to proceed with the installation by clicking Next.

<!-- tags: [setup, license agreement, version, install, collection, information, authorized features] keywords: [Syncfusion Essential Studio, Link Install, 2013, 11.1.0.21] -->
```

---

<!-- 페이지 84 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_043.jpeg
document_name: common
page_number: 043
page_id: common#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:01Z
fidelity: lossless
-->

# Essential Common

## Overview

- Installation process for Syncfusion Essential Studio Link Install 11.1.0.21.
- Step-by-step guide through the installation wizard.
- Information on the installation progress and completion.

## Content

### Installation Process

The installation process for Syncfusion Essential Studio Link Install is illustrated in the following figure:

**Figure 35: Installing**

![Syncfusion Essential Studio Link Install 11.1.0.21 Setup](image.png)  
- **Step 1: Welcome**  
  - User is greeted with a welcome screen.

- **Step 2: Collecting Information**  
  - The setup gathers necessary information for installation.

- **Step 3: Installing**  
  - The installer is currently in progress, displaying a status bar to indicate progress.
  - **Note:** This step may take 10-15 minutes on most machines.

- **Step 4: Completed**  
  - The installation is complete, and this screen will be displayed once the selected package is installed.

#### Notable Information

- Date: 19/02/2013
- Version: 11.1.0.21
- Status: The installation is actively in progress.

**Note:** The Completed screen is displayed once the selected package is installed.

## API Reference

<!-- None specific to this page -->

## Code Examples

<!-- None specific to this page -->

## Page-level Navigation/TOC

<!-- None specific to this page -->

## Cross References

See also:
- Syncfusion Winforms Documentation
- Installation and Setup Guides

<!-- tags: [Syncfusion Winforms, installation, Essential Studio, version 11.1.0.21] keywords: [Syncfusion Essential Studio Link Install, installation wizard, progress bar, setup process] -->
```

---

<!-- 페이지 85 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_047.jpeg
document_name: common
page_number: 047
page_id: common#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:13Z
fidelity: lossless
-->

## Overview
- Demonstrates the essential steps to set up the Syncfusion Essential Studio.
- Describes the setup process for digitally signed assemblies.
- Provides guidance on key setup screens such as the License Agreement.

## Content

### Setup Process Overview

The following steps illustrate the process for setting up the Syncfusion Essential Studio **Digitally Signed Assemblies**:

1. **Welcome**  
   - The installer welcomes users to the setup process.
   - **Collecting Information**  
     - The installation wizard gathers the necessary information.

2. **Installing**  
   - The software begins the installation sequence.

3. **Completed**  
   - Once the setup is finalized, this screen signifies the completion of the installation.

#### Welcome Screen

![Figure 40: Setup](attachment:Figure_40_Setup.png)  
*Figure 40: Setup*

The Welcome screen displays essential details about the installation:

- **Header Section:**  
  - "Syncfusion Essential Studio Digitally Signed Assemblies 2013 Vol. 1 Setup"

- **Step Navigation Bar:**  
  - Enumerates steps:  
    - Welcome
    - Collecting Information
    - Installing
    - Completed

- **Main Content:**  
  - A message thanking the user for the provided information.
  - Confirmation that authorized features have been unlocked.
  - Instructions to proceed to the next step using the "Next" button.

- **Footer Section:**  
  - Details such as the date (19/02/2013) and version (11.1.0.21).

#### Continuing with Installation

After the Welcome screen:

6. Click **Next** to continue with installation. The **License Agreement** screen opens.

## Cross References
- See also: Digital Signatures, Installation Procedures, Licensing Agreements.

<!-- tags: [syncfusion-sdk, setup, essentials, digitally_signed_assemblies, winforms] keywords: [syncfusion, setup process, digitally signed, license agreement, essential studio] -->
```

---

<!-- 페이지 86 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: common
page_number: 051
page_id: common#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:26Z
fidelity: lossless
-->

Essential Common

## Overview
- Describes the installation process for Syncfusion Essential Studio Digitally Signed Assemblies.
- Demonstrates the progress bars indicating the status of the installation steps.
- Highlights key installation instructions and highlights (color coding for different phases).

## Content

### Installation Wizard for Syncfusion Essential Studio Digitally Signed Assemblies

The image shows a typical installation wizard interface for installing Syncfusion Essential Studio Digitally Signed Assemblies. Here's an overview based on the steps indicated in the image:

#### Progress Steps

1. **Welcome**
   - The setup wizard starts with the welcome screen.
   - Progress bar shows the current step.

2. **Collecting Information**
   - This phase involves gathering configuration details.
   - Colored as pink to highlight the active phase.

3. **Installing**
   - The actual installation process is initiated.
   - Colored as green to denote progress towards completion.

4. **Completed**
   - Marks the successful conclusion of the installation.
   - The final step displayed when the process is finished.

### Textual Details
- **Ready To Install**
  - The setup wizard is ready to begin the installation of **Syncfusion Essential Studio Digitally Signed Assemblies**.
- **Installation Instructions:**
  - Click "Install" to begin the installation.
  - Click "Back" to review or change any installation settings.
  - Click "Cancel" to exit the wizard.
- **Metadata:**
  - Date: **19/02/2013**
  - Version: **11.1.0.21**

#### Installation Button
- The *Install* button is prominently highlighted, indicating the next action to continue with the installation.

### Figure Caption

Figure 44: **Ready to Install**

### Instructions

11. Click **Install** to continue with the installation.

## Page-level Navigation/TOC (if applicable)

- This section could act as a guide for users pointing them to subsequent steps in the installation process.

## Cross References

- References other sections or modules mentioned in the guide, linking to relevant documentation relevant to Syncfusion Winforms.

<!-- tags: [syncfusion, winforms, installation, setup wizard, digitally signed assemblies] keywords: [syncfusion essential studio, installation process, digitally signed assemblies, setup wizard interface, progress steps, install button] -->
```

---

<!-- 페이지 87 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_055.jpeg
document_name: common
page_number: 055
page_id: common#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:40Z
fidelity: lossless
-->

## Assembly Manager

### Overview
- Guides users through the process of installing assemblies in the Global Assembly Cache (GAC) using the Assembly Manager feature.

### Content

#### Assembly Manager Screen

{% include fig_info.html
class_info="Setup - Syncfusion Essential Studio Service Pack 11.1.0.21"
caption="Figure 48: Assemble Manager Screen"
%}

The **Assembly Manager** helps replace assemblies from precompiled assemblies to the **GAC** and **Assemblies** folder.

1. **Run Assembly Manager**:
   - Select the **Run Assembly Manager** check box to install assemblies in the GAC.

2. **Next**:
   - Click **Next** to proceed. The **Ready To Install** dialog will open.

## Page-level Navigation/TOC (if applicable)
- No table of contents is present on this page.

## Cross References
- Refer to the official Syncfusion documentation for detailed instructions on managing assemblies and GAC operations.

## RAG Annotations
<!-- tags: [syncfusion-sdk, winforms, assembly-manager, gac-installation] keywords: [Assembly Manager, GAC, precompiled assemblies, Syncfusion Essential Studio] -->

<!-- Copyright © 2013 Syncfusion. All rights reserved. -->
```


---

<!-- 페이지 88 -->

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

---

<!-- 페이지 89 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_063.jpeg
document_name: common
page_number: 063
page_id: common#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:04Z
fidelity: lossless
-->

# Essential Common

## Overview
- Covers tools for professional user interface components to create interactive web applications.
- Focuses on ASP.NET tools and their featured samples.
- Describes how to use tools to build robust and high-performance web application interfaces.

## Content

### Tools
- **Tools:**
  - Description: Essential Tools is a collection of professional user interface components to create interactive web applications.
  - Features include robust web application interfaces using the Editors Package (which includes a Date Time control with Drop-Down Calendar).
  
  **Featured controls in Essential Tools:**
  - AutoComplete TextBox
  - Button
  - Calendar
  - CheckBox
  - CogIndicator and Ctrl Manager
  - Drop-Down Calendar
  - Editors:
    - GalleryView
    - Generic Drop-Down
    - Groupbar
    - GridPdf
    - Layout control
    - Menu
    - Multi Column Drop-Down Combo
    - Multi Page
  - Additional controls include Text Box, Tree View, Groupbar, UploaderBox, and more.

### Figure 54: Essential Studio ASP.NET Sample Browser

#### Section: ASP.NET MVC
- Describes the integration and usage of ASP.NET MVC within the web application environment.

### Footer Information
- Copyright © 2001-2013 Syncfusion Inc
- Page navigation links: Forums Documentation Support Sales

## API Reference
- Additional references and documentation for syncing with other Syncfusion products or components.

## Code Examples
- Sample code snippets demonstrating the use of Essential Tools components.

### TOC
- Provides navigation links to relevant sections within the document or external documentation.

### Cross References
- References to other sections or documents related to Essential Tools and ASP.NET MVC implementation.

## RAG Annotations
- **Tags and Keywords:** essential-tools, asp-net, web-application, user-interface-components, syncfusion, dropdown-calendar, date-time-control, auto-complete-textbox.
```

<!-- tags: [essential-tools, asp-net, web-application, user-interface-components] keywords: [essential tools, date time-control, dropdown calendar, auto complete text box, featured samples] -->
```

---

<!-- 페이지 90 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: common
page_number: 067
page_id: common#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:17Z
fidelity: lossless
-->

# Essential Common

## Overview
- Showcase of Windows Forms features and controls provided by Syncfusion.
- Demonstrations of various UI components like Office Style Controls, Docking Package, and CommandBars Package.
- Overview of tools and new sample controls like Ribbon Style and Backstage Demo.

## Content

### Essential Studio Windows Forms Sample Browser

![Figure 59: Essential Studio Windows Forms Sample Browser](https://.../image)

Figure 59: Essential Studio Windows Forms Sample Browser

This section highlights the Essential Studio Windows Forms Sample Browser, showcasing various UI tools and controls available in Syncfusion's library. The browser includes:

- **Tools**:
  - Product Showcase
  - Office Style Controls
  - Docking Package
  - Menus Package
  - CommandBars Package
  - Tabbed MDI Package
  - Tree Package
  - Editors Package
  - Tabs Package
  - Navigation Package
  - Wizard Package

- **Controls Overview**:
  - **Office Style Custom Colors**: Visual design and customization options.
  - **VS 2008 Drag Provider**: Drag and drop functionality demonstration.
  - **New Samples**:
    - **Ribbon Style Demo**: Customizing a ribbon-style UI.
    - **Backstage Demo**: Backstage view in applications.
    - **TileLayout Demo**: Tile-based layout controls.
    - **Clock Demo**: Clock control demonstrated.

The section effectively demonstrates the variety of tools and controls that developers can use to build sophisticated Windows Forms applications.

### Windows Phone

14. Windows Phone

This section introduces the topic of Windows Phone, likely covering the integration or migration of Windows Forms applications for mobile platforms.

## API Reference
No explicit API references are visible in this section.

## Code Examples
No explicit code examples are visible in this section.

## Cross References
See also: Essential Studio Windows Forms, Syncfusion Winforms controls, custom UI styles, ribbon controls, backstage views, tile layouts.

<!-- tags: [product, Windows Forms, tools, controls, office style, ribbon, backstage, tile layout, clock demo] keywords: [customization, drag and drop, showcase, sample browser, UI components, synchronization, mobile platforms, Windows Phone] -->
```

---

<!-- 페이지 91 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_071.jpeg
document_name: common
page_number: 071
page_id: common#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:33Z
fidelity: lossless
-->

# Essential Common

## Navigation and Functionality Overview

This section outlines the essential navigation elements and their functionalities in the Syncfusion Winforms interface, as depicted in the provided figures.

### Figure 63: File

The "File" menu provides options for managing the application, such as exiting. It also allows access to platform-specific products and resources.

### Studio

- **Functionality**: Allows access to the products under each platform. Provides access to view local and online product samples. It also allows access to the online documentation, release notes, and read-me documents for respective products.
- **Alternative Access**: Can be alternatively accessed using the Product Platforms section in the dashboard.

#### Figure 64: Platforms

This figure illustrates the menu structure for selecting different platforms and accessing their respective samples and documentation.

### Tools

- **Functionality**: Allows access to the add-ons and utilities available for various platforms and products. It also allows managing assemblies and licenses. The Toolbox configuration lets users choose from different Visual Studio versions to be installed for their system configuration.
- **Alternative Access**: Can be alternatively accessed through the Utilities & Documentation section.

#### Figure 65: Tools

This figure displays the menu structure for accessing various add-ons, utilities, and license management options.

### Help

- **Functionality**: Allows users to access information about the current installed version by clicking "About." It also provides access to the Direct-Trac support page over the internet.

## Summary

This section describes the key functionalities and menus in the Syncfusion Winforms interface, emphasizing navigation options such as accessing platforms, tools, and help resources.

## References

- **Figures Referenced**:
  - Figure 63: File
  - Figure 64: Platforms
  - Figure 65: Tools

<!-- tags: [Syncfusion Winforms, Navigation, Studios, Tools, Help, Product Platforms, Menu Options, Add-ons, Utilities, License Management, Documentation, Samples] keywords: [Studio, Tools, Help, File, Platforms, Add-ons, Utilities, License Management, Documentation, Samples, Direct-Trac] -->
```

---

<!-- 페이지 92 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_075.jpeg
document_name: common
page_number: 075
page_id: common#page_075
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:46Z
fidelity: lossless
-->

# Essential Common

## Overview
- Lists the prerequisites for all products to work successfully.
- Alerts users if required software is missing.
- Provides a Recommended Software dialog box for troubleshooting.

## Content

### Missing Software
To work successfully, you need to install a list of prerequisites for all of the products. If some of the software is not installed, the dashboard will display an alert. Click **Missing Software**, and a Recommended Software dialog box will open.

![Figure 70: Missing Software](image.png)

### Recommended Software
**Recommended Software** will list the prerequisites for all platforms. A **✓** symbol appears if all recommended software for the platform is installed in your system. A **✗** symbol appears if any recommended software for a platform is not installed in your system before installing Essential Studio.

#### Recheck Option
The recheck option will recheck the prerequisites list and refresh the currently installed software list.

---

## API Reference (if applicable)
Not applicable for this section.

## Code Examples (multi-language supported)
Not applicable for this section.

## Page-level Navigation/TOC (if applicable)
Not applicable for this section.

## Cross References
Not applicable for this section.

<!-- tags: [essential common, missing software, recommended software] keywords: [prerequisites, installed software, alert, dashboard, recheck option, syncfusion winforms, version 11.4.0.26] -->
```

---

<!-- 페이지 93 -->

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

---

<!-- 페이지 94 -->

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

---

<!-- 페이지 95 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_087.jpeg
document_name: common
page_number: 087
page_id: common#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:29Z
fidelity: lossless
-->

## Overview
- This page details the output frame for build operations and introduces the License Manager within Syncfusion Winforms.
- It explains how to launch the License Manager from the Dashboard and its functionality.

## Content

### Output Frame
This frame shows the output, i.e., the status of the build operation, in a text area.

After selecting the required options in the above-mentioned frames, click **Perform Build** inside the output frame.

Note: The build operation is performed, and the status is updated in the text area, inside the output frame. On completion of a build operation, a dialog box is displayed stating that the "Build operation has been completed. Please review build output and log files for additional information".

### 1.13.4 License Manager
The License Manager helps you manage license key information, such as the validity of a Syncfusion key used on your system.

#### Launching License Manager
Follow the steps below to launch the License Manager from the Dashboard:

1. Open the Syncfusion Dashboard.
2. Click **License Management**.
3. Click the **Launch** button for **License Manager**. The **Syncfusion License Manager** dialog box opens.

![Syncfusion License Manager](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyreferrer-fashion-attributeAAAAASUVORK5CYII=)

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

See also:
- Building Operations
- Dashboard
- License Management

<!-- tags: [Syncfusion Winforms, License Manager, Build Operations, Dashboard] keywords: [build operation, license key, Syncfusion License Manager, performs build, status, dialog box, license information, add key, remove key, copy keys] -->
```

---

<!-- 페이지 96 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_091.jpeg
document_name: common
page_number: 091
page_id: common#page_091
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:41Z
fidelity: lossless
-->

# Essential Common

## Overview
- Describes how to configure Syncfusion controls in the Visual Studio .NET toolbox using the Syncfusion Toolbox Installer.
- Guides users through steps to access and utilize the Toolbox Configuration tool.
- Highlights the Windows application aspect of the utility.

## Content

### 1.13.5 Toolbox Configuration
The Syncfusion Toolbox Installer adds the Syncfusion controls into the Visual Studio .NET toolbox. This utility is currently shipped as a console application.

#### Configuring Toolbox
1. **Open the Syncfusion Dashboard.**
2. **Click Utilities > Toolbox Configuration.**

![Toolbox Configuration](./Figure.png)
*Figure 84: Toolbox Configuration*

This application allows users to reconfigure the Visual Studio .NET toolbox from the Syncfusion Dashboard.

3. **Select the Toolbox Installer.**

### WinForms-specific conventions
- The Toolbox Installer ensures that Syncfusion controls are properly integrated into the Visual Studio environment, facilitating their use in WinForms applications.

#### Notes:
- Administrator-level access is required to use the Toolbox Installer.
- The version shown in the image is `Essential Studio Version - 11.1.0.21`.
- The functionality described is designed to streamline the process of adding and managing Syncfusion controls within the Visual Studio .NET environment.

## API Reference (if applicable)
N/A

## Code Examples (multi-language supported)
N/A

## Page-level Navigation/TOC (if applicable)
N/A

## Cross References
See also:
- [Syncfusion Documentation for .NET Controls](https://www.syncfusion.com/documentation)

## RAG Annotations
<!-- tags: [syncfusion, winforms, toolbox, installer, controls, configuration, version:11.1.0.21] keywords: [syncfusion toolbox installer, visual studio .net, toolbox configuration, utilities, administrator access, windows application] -->
```

---

<!-- 페이지 97 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_095.jpeg
document_name: common
page_number: 095
page_id: common#page_095
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:54Z
fidelity: lossless
-->

## Overview
- Overview of using the MultiTarget Manager to configure machine settings for a specific .NET target framework.
- Steps for selecting a target framework version and refreshing an application for building.
- Instructions for migrating projects using Syncfusion’s project migration tool.

## Content

### MultiTarget Manager

#### 1. Using the MultiTarget Manager
Syncfusion Essential Studio Multi-Target Manager is used to configure the machine for a given target framework. To do this:

1. **Figure 88: Essential Studio MultiTarget Manager x.x.x.x Dialog**
   - The dialog allows you to select a target framework from a drop-down list.
   - This configuration process may take 30 seconds to 1 minute.

2. **Select required version**
   - Select the required framework version from the drop-down list provided:
     - **Available Framework versions to target**: `4.0`
   - Click the **Perform Action** button to initiate the configuration.
   - Upon completion, the Multitarget Manager will open a confirmation dialog.

3. **Figure 89: Multitarget Manager**
   - Confirmation message indicates that the requested action has been completed for the `4.0 Framework`.
   - Click **OK** to proceed.

#### 2. Open and refresh an application
- **Open an application**: After the framework is set, open your project.
- **Refresh the application**: Before building, refresh the application to ensure it is ready for the new framework version.

**Note**: The target value and the registry value will be changed to the selected framework version.

### 1.13.7 Project Migration

#### Overview
- The project migration tool facilitates moving project files to a given Syncfusion Essential Studio Version.

#### Steps for migrating a project
1. Open the project migration tool.
2. Select the source project files and the target Syncfusion Essential Studio Version.
3. Follow the prompts to complete the migration process.

This section provides an overview of how to migrate a project using Syncfusion’s migration tool, ensuring a smooth transition to a new version of the framework.

#### Figure 88: Essential Studio MultiTarget Manager x.x.x.x Dialog
![](image.png)
**Caption**: The dialog for selecting and performing an action on a target framework version.

#### Figure 89: Multitarget Manager
![](image.png)
**Caption**: Confirmation dialog indicating the completion of the target framework configuration.

## API Reference (if applicable)
No specific API details are outlined in this section, but you can refer to the relevant Syncfusion documentation for detailed API information about project migration and multi-target framework management.

## Code Examples (if applicable)
No code examples are provided in this section, as the focus is on guiding the migration process rather than showcasing code implementation.

## RAG Annotations
<!-- tags: multitarget-manager, project-migration, .net-framework, syncfusion-essential-studio version:Syncfusion Winforms 11.4.0.26 -->
<!-- keywords: multitarget, framework versions, configuration, build, migration, target framework -->
```

---

<!-- 페이지 98 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_099.jpeg
document_name: common
page_number: 099
page_id: common#page_099
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:13Z
fidelity: lossless
-->

# Essential Common

## Overview
- Explains the setup process for Orubase Studio using the Syncfusion installer.
- Highlights the welcome screen and the steps involved in the installation wizard.
- Provides instructions to proceed with the installation.

## Content

### Welcome Screen
The welcome screen for the Syncfusion Orubase Studio Setup is displayed.

- **Setup Wizard Overview**:
  - The setup wizard will guide you through the installation process, installing Orubase Studio on your computer.
  - User can choose to continue by clicking "Next" or exit the setup wizard by clicking "Cancel."

#### Steps in the Setup Wizard
1. **Welcome**
2. **Collecting Information**
3. **Installing**
4. **Completed**

#### Screenshot Description
The screenshot shows the welcome screen with the following details:
- **Header**: Syncfusion logo and "Orubase Studio" label.
- **Description**: "Welcome to the Syncfusion Orubase Studio Setup."
- **Installation Progress**: The four stages of the setup process are listed on the left.
- **Date and Version**: Current date (02/12/2013) and version (1.1.0.69) displayed at the bottom.
- **Action Buttons**: "Back," "Next," and "Cancel" buttons to guide user interactions.

#### Figure Caption
**Figure 92: Welcome Screen**

## Steps to Proceed

3. Click **Next**. The **User Information** screen opens.

## API Reference (if applicable)
This section is not applicable for the current content.

## Code Examples (if applicable)
No code examples are provided for this section.

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, Orubase Studio, Setup Wizard, Installation Guide] keywords: [Syncfusion, Orubase Studio, Setup Wizard, Welcome Screen, Installation Process] -->

```

---

<!-- 페이지 99 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_103.jpeg
document_name: common
page_number: 103
page_id: common#page_103
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:26Z
fidelity: lossless
-->

# Essential Common

## Overview
- Guide on selecting the installation folder for Syncfusion Orubase Studio.
- Instructions for choosing the default or custom location for storing sample data files.
- Step-by-step process for navigating through the installation wizard.

## Content

**Figure 96: Select the Samples Folder screen**

### Installation Steps

1. **Welcome**
   - Initial screen for the installation process.

2. **Collecting Information**
   - Users can customize the installation location for sample data files.
   - Folder path: `C:\Users\Kannan <> AppData\Local\Syncfusion\Orubase Studio\1.1.0`
   - Option to browse for a different folder path.

3. **Installing**
   - Installation process will proceed based on the selected folder.

4. **Completed**
   - Installation process is finished successfully.

### Notes
- **Note:** You can also browse to choose a location by clicking **Browse**.
- Proceed to the **Install Ready dialog** by clicking **Next**.

#### Screen Details
- **Version:** 1.1.0.69
- **Date:** 02/12/2013
- Buttons:
  - **< Back**: Return to the previous step.
  - **Next**: Proceed to the next step.
  - **Cancel**: Abort the installation process.

## Summary

Follow the steps in the installation wizard to select and confirm the folder for installing Syncfusion Orubase Studio. Use the **Browse** button if you want to designate a custom folder location for your sample data. Once set, click **Next** to move to the next step of the installation process.

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Installation, Orubase Studio, Folder Selection, Sample Data, Version 1.1.0.69] keywords: [installation wizard, select folder, sample data files, version, date, Syncfusion Orubase Studio, navigate installation process] -->
```

---

<!-- 페이지 100 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_107.jpeg
document_name: common
page_number: 107
page_id: common#page_107
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:39Z
fidelity: lossless
-->

# Essential Common

## Overview
- Provides a guided start to using the Orubase Wizard.
- Highlights creating and managing new applications.
- Features access to sample applications, gallery, and video tutorials.
- Indicates the necessity of administrator privileges for certain functions.

## Content

### Orubase Dashboard

#### Getting Started
- **Orubase Wizard**: A tool to assist in setup and configuration.
- **Create new application**: An action to initiate the creation of new applications.

#### Sample applications
- **Samples**: Access for reference materials and tutorials.
- **Sample Gallery**: A collection showcasing different application examples.
- **Video Gallery**: Video resources for tutorial purposes.

#### Administrator access required
- Indicates certain functionalities require administrative privileges.

### Navigation and Utility Features
- **Mac Installer**: Option for installing on Mac systems.
- **Library folder**: Access to stored resources and libraries.
- **Utilities**: Tools and additional functionalities for development.
- **Documentation**: Reference documentation for the application.

---

**See also:**
- Sales Contact
- Support Contact
- www.orubase.com

### Footer
- Copyright information: "Copyright 2001-2013 Syncfusion Inc."
- Powered by Syncfusion.

## API Reference (if applicable)
- None provided on this page.

## Code Examples (multi-language supported)
- None provided on this page.

## Page-level Navigation/TOC (if applicable)
- Not applicable on this page.

### Cross References
- Not applicable on this page.

<!-- tags: [Syncfusion Winforms, Orubase Dashboard, Getting Started, Sample applications, Video Gallery, Utilities, Documentation] keywords: [Orubase Wizard, Create new application, Samples, Sample Gallery, Video Gallery, Mac Installer, Library folder, Administrator access required] -->
```

---

<!-- 페이지 101 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_111.jpeg
document_name: common
page_number: 111
page_id: common#page_111
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:51Z
fidelity: lossless
-->

# Essential Common

## Overview
- Guides users through the process of entering user information during installation.
- Highlights the fields required for user registration: User Name, Organization, and Unlock Key.
- Describes the validation process for the Unlock Key and the subsequent screen transition.

## Content

### Figure 104: User Information

The image shows a user interface screen titled **User Information**, where users are prompted to provide the following details:

- **User Name**: A text box where the user name is entered. Example input: `labuser`.
- **Organization**: A text box intended for the user's organization details.
- **Unlock Key**: A text box for entering the Unlock Key, which is used for validation purposes.

Below the input fields are three buttons:
- **< Back**: Allows users to return to the previous screen.
- **Next**: Proceeds to the next step after entering the required information.
- **Cancel**: Cancels the current action.

#### Instructions for Entering Information

1. **Enter your User Name, Organization, and Unlock Key** in the corresponding text boxes provided.
2. **Click Next** to proceed.

#### Note
* **The unlock key is validated and the preceding welcome screen opens.**

## API Reference

None applicable for this specific section.

## Code Examples

This section does not contain any code examples.

## Page-level Navigation/TOC

No table of contents is present on this page.

## Cross References

This section does not reference any external documents or pages.

<!-- tags: [Syncfusion Winforms, User Information, Unlock Key, User Registration, Installation Guide] keywords: [User Name, Organization, Unlock Key, Validation, Welcome Screen] -->
```

---

<!-- 페이지 102 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_115.jpeg
document_name: common
page_number: 115
page_id: common#page_115
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:05Z
fidelity: lossless
-->

## Essential Common

### Installation

The following screenshot shows the steps involved in installing the Syncfusion Metro Studio 2.0.1.1 Setup.

#### Figure 108: Setup-Installation
![Setup-Installation](https://example.com/Setup-Installation)

11. Click **Install** to continue with the installation.

## Page-level Navigation/TOC
- [Common: Home](#common)
- [Installation](#installation)

<!-- tags: [syncfusion, windowsforms, metro studio, installation, user guide, version 11.4.0.26] keywords: [Syncfusion Metro Studio, installation, setup wizard, essential common, user guide] -->
```

---

<!-- 페이지 103 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_119.jpeg
document_name: common
page_number: 119
page_id: common#page_119
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:12Z
fidelity: lossless
-->

# Essential Common

## Overview
- This section presents detailed features of the Metro Studio Dashboard in the Syncfusion Winforms library.
- Includes illustrations and descriptions of the dashboard elements and functionality.

## Content

### Metro Studio Dashboard

Figure 112: Metro Studio Dashboard  
(A blank space indicates where the figure would typically be placed, showcasing the Metro Studio Dashboard interface.)

```markdown
Illustration: The Metro Studio Dashboard interface includes various interactive dashboard components designed to enhance user experience in Winforms applications.
```

### Features of Metro Studio Dashboard
- **User Interface**: Utilizes a sleek and modern aesthetic suitable for Metro-style applications.
- **Interactive Elements**: Includes widgets, gauges, and customization options to create a personalized dashboard experience.
- **Responsive Design**: Automatic resizing to accommodate different screen sizes and user interactions.

```markdown
Note: The Metro Studio Dashboard is part of the comprehensive set of tools provided by Syncfusion for creating visually appealing and user-friendly UI components.
```

## API Reference

### Class: MetroStudioDashboardControl
Here is a brief list of key properties, methods, and events associated with the `MetroStudioDashboardControl`.

#### Properties
- **DashboardStyle**: Configures the overall style of the dashboard.
- **NavigationMenu**: Controls the appearance of the navigation menu in the dashboard.
- **DashboardWidgets**: Contains the collection of dashboards and widgets to render.

#### Methods
- **InitializeDashboard()**: Initializes the dashboard with default or configured settings.

#### Events
- **DashboardLoaded**: Triggered when the dashboard is successfully loaded.
- **WidgetViewChanged**: Triggered when the user views a different widget in the dashboard.

## Code Examples

### C# Example: Initializing a Metro Studio Dashboard

```csharp
using Syncfusion.Windows.Forms.MetroStudio;

// Create an instance of MetroStudioDashboardControl
MetroStudioDashboardControl metroStudioDashboard = new MetroStudioDashboardControl();

// Set the dashboard style
metroStudioDashboard.DashboardStyle = MetroStudioDashboardStyles.MetroDark;

// Add some widgets to the dashboard
metroStudioWidgetCollection widgets = new metroStudioWidgetCollection();
metroStudioDashboard.DashboardWidgets.Add(widgets);

// Initialize the dashboard
metroStudioDashboard.InitializeDashboard();

// Add event handlers
metroStudioDashboard.DashboardLoaded += 
    new EventHandler(MetroStudioDashboard_DashboardLoaded);
metroStudioDashboard.WidgetViewChanged += 
    new EventHandler(MetroStudioDashboard_WidgetViewChanged);

// Event Handler for DashboardLoaded
private void MetroStudioDashboard_DashboardLoaded(object sender, EventArgs e)
{
    MessageBox.Show("Dashboard has been initialized and loaded.");
}

// Event Handler for WidgetViewChanged
private void MetroStudioDashboard_WidgetViewChanged(object sender, EventArgs e)
{
    MessageBox.Show("The user has changed the widget view.");
}
```

### VB.NET Example: Initializing a Metro Studio Dashboard

```vb
Imports Syncfusion.Windows.Forms.MetroStudio

' Create an instance of MetroStudioDashboardControl
Dim metroStudioDashboard As New MetroStudioDashboardControl()

' Set the dashboard style
metroStudioDashboard.DashboardStyle = MetroStudioDashboardStyles.MetroDark

' Add some widgets to the dashboard
Dim widgets As New metroStudioWidgetCollection()
metroStudioDashboard.DashboardWidgets.Add(widgets)

' Initialize the dashboard
metroStudioDashboard.InitializeDashboard()

' Add event handlers
AddHandler metroStudioDashboard.DashboardLoaded, 
    AddressOf MetroStudioDashboard_DashboardLoaded
AddHandler metroStudioDashboard.WidgetViewChanged, 
    AddressOf MetroStudioDashboard_WidgetViewChanged

' Event Handler for DashboardLoaded
Private Sub MetroStudioDashboard_DashboardLoaded(sender As Object, e As EventArgs)
    MessageBox.Show("Dashboard has been initialized and loaded.")
End Sub

' Event Handler for WidgetViewChanged
Private Sub MetroStudioDashboard_WidgetViewChanged(sender As Object, e As EventArgs)
    MessageBox.Show("The user has changed the widget view.")
End Sub
```

## Cross References

- For additional information on configuring dashboard styles, see the section on **Metro Styles**.
- To learn more about event handling, refer to the **Events Overview** section.

<!-- tags: [Syncfusion Winforms, Metro Studio Dashboard, Dashboard, UI Components, Design] keywords: [Metro, Studio, Dashboard, UI, Winforms, C#, VB.NET, Event Handlers, Widgets, Customization] -->
```

---

<!-- 페이지 104 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_123.jpeg
document_name: common
page_number: 123
page_id: common#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:37Z
fidelity: lossless
-->

## Overview
- Steps to remove folders, ensure assembly versions, and embed a license file in a Syncfusion WinForms project.

## Content

### Steps for Embedding a License

1. Reload the application and then remove the `bin` and `obj` folders.
2. Ensure that the assemblies referred in the project belong to the same version.
3. Recompile your project and run it.
4. In the Solution Explorer, click **Show All Files**.
5. A file called **licenses.licx** with the following entry will be available in the project tree:
   - Syncfusion.Core.Licensing.LicensedComponent
   - Syncfusion.Core.
6. Add the file to the project.
7. Open the properties of this file.
8. Set the **BuildAction** property to **Embedded Resource**.
9. Run the project.

### Embedding the License.licx File

The following are the steps to embed the **License.licx** file as an embedded resource in the project:

1. Open the project.
2. In the **Solution Explorer**, right-click on the project node and then select **Add New Item**.
3. Choose the **licenses.licx** file from the following location:
   ```
   (Installed Drive):\Program Files\Syncfusion\Essential
   Studio\<version>\Templates\licenses.licx file.
   ```
4. The file will be added.
5. In the **Solution Explorer**, click the license file node and then open the **Properties** window.
6. Set the **Build Action** property to **Embedded Resource**.

## Page-level Navigation/TOC (if applicable)
- Steps for Embedding a License
- Embedding the License.licx File

## Cross References
- Refer to the Syncfusion documentation for detailed instructions on version compatibility and assembly management.

<!-- tags: [Syncfusion, WinForms, License Management, Embedding, Version Compatibility] keywords: [licenses.licx, BuildAction, Embedded Resource, Syncfusion.Core.Licensing.LicensedComponent, Solution Explorer] -->
```

---

<!-- 페이지 105 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_127.jpeg
document_name: common
page_number: 127
page_id: common#page_127
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:50Z
fidelity: lossless
-->

## Essential Common

### Figure 121: License Manager

The figure below shows the Syncfusion License Manager interface, which is used to manage and display license keys for Syncfusion products.

![License Manager](https://example.com/license_manager_image.png)

This interface includes options to **Copy Keys**, **Add Key**, and **Remove Key**, as well as a display area that lists the products licensed under the provided key. The example key shown in the figure (@exampleKey555...) is a sample and not valid for actual use. 

The text in the display area indicates that the key licenses **Essential Studio version 10.1.0** and lists the Syncfusion products covered by this license:

- **Syncfusion Essential Bi**
- **Syncfusion Essential Calculate**
- **Syncfusion Essential Chart**
- **Syncfusion Infrastructure Library Core**
- **Syncfusion Essential Diagram**
- **Syncfusion Essential DocIO**
- **Syncfusion Essential Edit**
- **Syncfusion Essential Excelrw**
- **Syncfusion Essential Gauge**

### Instructions

2. **Open your Visual Studio project file in a text editor and ensure that only one Syncfusion.Core reference entry exists in your project.**

This step ensures that your project has a single and correct reference to the Syncfusion.Core library, which is crucial for maintaining the integrity and proper functionality of your application.

## API Reference (if applicable)

There are no API references provided in this page's content. However, for general reference, the Syncfusion.Core library includes essential functionality for integrating Syncfusion's advanced components in your WinForms applications.

## Code Examples

No code examples are provided in this page's content.

## Page-level Navigation/TOC (if applicable)

No local Table of Contents or navigation references are present in this page's content.

## Cross References

No cross-references are provided in this page's content.

## RAG Annotations

<!-- tags: [SyncfusionWinforms, LicenseManager, EssentialStudio, VersionControl] keywords: [Syncfusion License Manager, Essential Studio, version 10.1.0, Syncfusion.Core reference, Visual Studio project, text editor] -->
```

---

<!-- 페이지 106 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_131.jpeg
document_name: common
page_number: 131
page_id: common#page_131
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:03Z
fidelity: lossless
-->

## Essential Common Overview  
- Describes steps for cleaning up and manually removing Syncfusion installed files.  
- Involves the Windows Installer Cleanup tool to manage changes to the system.  
- Guides on locating and manually handling Syncfusion installations across different operating systems.  

## Content  

### Windows Installer Cleanup  

![Windows Installer Cleanup](# "Figure 125: Windows Installer Cleanup")  

3. **Manually remove or delete the Syncfusion installed files from the following location (if it exists):**  

#### Source (Windows XP, Windows Vista, Windows 7):  
- Installed location:  
  ```
  (Installed location)\Syncfusion\Essential Studio\ (version)
  ```
  **Example:**  
  ```
  C:\Program Files\Syncfusion\Essential Studio\9.4.0.62
  ```  

#### Samples (Windows XP):  
- Location:  
  ```
  C:\Syncfusion\ (version)
  ```
  ```
  C:\Syncfusion\9.4.0.62
  ```  

#### Samples (Windows Vista, Windows 7):  
- Location:  
  ```
  C:\Users\<user name>\AppData\Local\Syncfusion\EssentialStudio\ (version)
  ```
  **Example:**  
  ```
  C:\Users\<user name>\AppData\Local\Syncfusion\EssentialStudio\9.4.0.62
  ```  

**Note:** The Samples Location above mentioned is default for corresponding OS. If you are installed samples in any other location, please remove it from that location.  

### Uninstall and Reinstall  

The setup will be uninstalled. You can install it again.  

## API Reference  

No specific APIs referenced in this section.  

## Code Examples  

No code examples provided in this section.  

## Page-level Navigation/TOC  

Not applicable for this page.  

## Cross References  

Refer to the Windows Installer Cleanup section for additional details on uninstalling Syncfusion products.  

## RAG Annotations  

<!-- tags: [Syncfusion Winforms, Windows Installer Cleanup, Uninstalling, Syncfusion Installed Files] keywords: [Syncfusion, Windows Installer, Cleanup, Uninstall, Delete, Source Location, Samples Location, Essential Studio] -->
```

---

<!-- 페이지 107 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_135.jpeg
document_name: common
page_number: 135
page_id: common#page_135
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:17Z
fidelity: lossless
-->

# Essential Common

## Overview
- This section provides instructions on user registration dialog handling in Syncfusion's Essential Studio, focusing on version comparisons and platform-specific nuances.

## Content

### User Registration Dialog

#### Figure 127: User registration dialog (earlier 11.1.*)
- Displays the legacy user registration dialog for versions earlier than 11.1. This dialog typically includes fields for User Name, Organization, and Unlock Key.
- This registration dialog is part of the earlier versions of the software, designed to register or unlock functionalities within the Syncfusion Winforms environment.

#### Newer version of 10.4.*:
- Shows the user registration dialog updated for newer software versions.
- Includes a section for entering a valid Unlock Key, which is necessary to unlock the software features.
- Prompts users to obtain a Free Evaluation Key, providing a reference link to an article for further assistance.

#### Figure 128: User registration dialog (Wrong platform)
- Highlights an issue where users may attempt to use the wrong Unlock Key for the platform: attempting to unlock the ASP.NET setup with a WindowsForms unlock key.
- Provides a message instructing users to refer to a specific article for resolving platform mismatch issues.

### WinForms-specific conventions

#### Registration Process:
- The user is required to enter their details in the provided fields.
- Ensure the correct Unlock Key is provided to avoid issues with incorrect platform registration.
- The "NEXT" button at the bottom confirms the registration or lock attempt.

### Troubleshooting
- In case of version discrepancies or platform mismatches, users are directed to consult the provided article or Syncfusion's support documentation.

## Cross References
- For more detailed troubleshooting or version-specific registration issues, refer to:
  - Article: [http://www.syncfusion.com/support/kb/2322](http://www.syncfusion.com/support/kb/2322)

<!-- tags: [syncfusion-sdk, user-registration, windowsforms, essential-studio, version-updates] keywords: [user registration, platform mismatch, unlock key, free evaluation key, asp.net, windowsforms, version 11.1, version 10.4] -->
```

---

<!-- 페이지 108 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_139.jpeg
document_name: common
page_number: 139
page_id: common#page_139
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:31Z
fidelity: lossless
-->

# Essential Common

```csharp
Thread.CurrentThread.CurrentUICulture = new
System.Globalization.CultureInfo("fr-FR");
Thread.CurrentThread.CurrentCulture = new
System.Globalization.CultureInfo("fr-FR");
)
```

At the end of this process, the application should contain the following to achieve localization:

- Your Application.exe file
- The en-US directory with Resources.dll
- The fr-CH directory with corresponding Resources.dll and Syncfusion Assemblies (if you have set `CopyLocal` to `True`).

## Calendar control in French language

The image below illustrates a Calendar control in the French language.

![](images/media/image140.png){#fig:131}
**Figure 131:** Calendar control localized to French

> **Note:** 
>
> - Localized strings will not be displayed in your application until the created satellite assembly is signed. Send us your newly created assemblies for signing. We will sign your assemblies and send them immediately.
> - It is not required to install satellite assemblies in the GAC or Assemblies folder.
> - Your en-US directory should contain the default satellite assembly, which is available in the Precompiled Assemblies or Assemblies folder.
> - Application culture change should be included before the `InitializeComponent()` method call in the application. It is better to include culture change in the App.xaml file.

## 4.7.2 Silverlight

In Silverlight, the easiest way to accomplish localization is to use a Resource (.resx) file. For each culture you wish to target, you will need a separate set of resources that match that specific culture.

The following are the primary steps for Localizing the Syncfusion Ribbon Control:
```markdown

The following are the primary steps for Localizing the Syncfusion Ribbon Control:
```

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
<!-- tags: [syncfusion, winforms, localization, culture, satellite assembly, french, fr-fr, silverlight, resource file, app.xaml, calendar control] keywords: [localized strings, application localization, satellite assembly signing, GAC, Assemblies folder, Resource (.resx) file, Syncfusion Ribbon Control] -->
```

---

<!-- 페이지 109 -->

```html
<!--source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_143.jpeg
document_name: common
page_number: 143
page_id: common#page_143
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:45Z
fidelity: lossless
-->

# Essential Common

| Feature                     | Location/Link                                                                                                    |
|-----------------------------|---------------------------------------------------------------------------------------------------------------|
| nu.aspx?args=0             | http://samples.syncfusion.com/ASPNET/8.4.0.10/Web/Tools.Web/samples/3.5/EditorsPackage/RichTextEditor/Localization/cs/Localization.aspx?args=0 |
| Chart[Windows]             | (Installed DRIVE):\\Syncfusion\\EssentialStudio\\(version)\\Windows\\Chart.Windows\\Samples\\2.0\\Culture Localization\\Localization Demo\\cs |
| Diagram [Windows]          | (Installed DRIVE):\\Syncfusion\\EssentialStudio\\(version)\\Windows\\Diagram.Windows\\Samples\\2.0\\Localizing Dialogs\\Localization Demo\\cs |
| Chart[ASP.NET]             | Currently does not support localization.                                                                     |
| Diagram[ASP.NET]           | Currently does not support localization.                                                                     |
| Windows Forms [Grid,Tools] | Samples are available in the machine installed with Essential Studio. <br> (Installed DRIVE):\\Syncfusion\\EssentialStudio\\8.4.0.8\\Windows\\Tools.Windows\\Samples\\2.0\\Localization Demo\\Localization Demo |

## 4.8 How to redistribute an application on the client machine

Syncfusion provides support to redistribute an application which uses Syncfusion assemblies. For information on deploying an application on a client machine that uses Syncfusion controls, see **Application Deployment**.

**Note:** Please ignore the **licences.licx file information** provided in the shared link if you are using **Syncfusion Essential Studio v8.4.x.x and later**.

<!-- tags: [Syncfusion Winforms, deployment, localization, redistribution, Essential Studio, localization demo, shared link, ASP.NET, Windows Forms, Diagram, Chart] keywords: [localization, redistribution, deployment, Syncfusion Essential Studio, application deployment, shared link, licenses.licx, controls, client machine, Chart, Diagram, Windows Forms, ASP.NET] -->
```

---

<!-- 페이지 110 -->

```html
<!-- **All metadata is intentionally left blank as per instructions.** -->
```

## Overview
- Syncfusion Essential Studio overview and terminology introduction.
- Describes the scope and components of Essential Studio, including its compatibility with .NET environments and supported frameworks.
- Provides an explanation of terminology used throughout the documentation.

## Content
### Essential Studio

Welcome to the Syncfusion Essential Studio product documentation. This content will help you get started with Essential Studio.

Essential Studio consists of several .NET libraries that provide support for building modern Windows Forms, Windows Phones, WPF, Silverlight, ASP.NET, ASP.NET MVC, MVC Mobile, and WinRT applications. The packages can be used in any .NET environment, including C#, VB.NET, Delphi, and managed C++.

**Note:** The Express Editions of Visual Studio.NET does not have support for toolbox.

### 1.1 Terminology

The Terminology section covers documentation conventions used in this manual.

| Convention          | Example           | Description                                                                                                                                                          |
|---------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Essential Studio     |                 | Essential Studio is a comprehensive library of controls targeting the .NET development platform. The packaging of the products within Essential Studio is such that the products share certain common features such as design patterns, installation programs and several configuration utilities. The term Essential studio is used in these sections, representing the entire package. |

## API Reference (if applicable)
<!-- **No API reference content provided in the image.** -->

## Code Examples (multi-language supported)
<!-- **No code examples provided in the image.** -->

## Page-level Navigation/TOC (if applicable)
<!-- **No table of contents or navigation provided in the image.** -->

## Cross References
- Refer to the "User Guide" for more detailed documentation on Syncfusion Essential Studio.
- See also: "The Express Editions of Visual Studio.NET does not have support for toolbox."

## RAG Annotations
<!-- **No RAG annotations provided in the image.** -->
<!-- tags: [Essential Studio, .NET, Windows Forms, WPF, Silverlight, ASP.NET, ASP.NET MVC, MVC Mobile, WinRT, User Guide] keywords: [Syncfusion, .NET libraries, design patterns, installation programs, configuration utilities, terminology, documentation conventions] -->
```

---

<!-- 페이지 111 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_008.jpeg
document_name: common
page_number: 008
page_id: common#page_008
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:58:57Z
fidelity: lossless
-->

# Essential Common

## Overview
- **License Agreement**: A document outlining the legal terms and conditions of using Syncfusion software.
- **Acceptance of Terms**: Before proceeding, users must accept the terms and conditions as part of the installation process.

### License Agreement

The License Agreement is a legal document between the user and Syncfusion, Inc., a Delaware corporation located at 2501 Aerial Center Parkway, Suite 200, Morrisville, NC 27560. 

#### Key Points:
- Syncfusion licenses its products on a per-copy, site, or enterprise basis.
- The right to use a copy of a Syncfusion software product is determined by this agreement. Additional terms apply to site or enterprise licenses.
- Users are required to carefully read all terms and conditions before downloading or installing the software.

#### Acceptance Check:
1. After reading the terms, check the checkbox labeled "I accept the terms and conditions."
2. Click **Next** to proceed to the **Select the Installation and Samples Folder** screen.

## Installation Steps

1. **Acknowledge the License Agreement**:
   - Carefully review the terms outlined in the License Agreement.
   - Check the box labeled "I accept the terms and conditions."

2. **Proceed with Installation**:
   - Click **Next** to continue to the next step in the installation process.

<!-- tags: [syncfusion-sdk, software-license, license-agreement, installation-steps] keywords: [syncfusion-studio, per-copy basis, site license, enterprise license, terms and conditions, acceptance] -->
```

---

<!-- 페이지 112 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_012.jpeg
document_name: common
page_number: 012
page_id: common#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:09Z
fidelity: lossless
-->

# Essential Common

## Overview
- Installation completion confirmation and next steps after installing Syncfusion Essential Studio.
- Instructions for launching the Dashboard post-installation.
- Support for command line installation and uninstallation.

## Content

### Note
The Completed screen is displayed once the selected platform is installed.

#### Figure 7: Installation Completed

Essential Studio v.11.1.0.21 was successfully installed on your machine.  
Source code is not included with this install. It can be accessed via the Syncfusion Essential Studio dashboard if you have a source license.

- Run Dashboard: ☐ (checked)
- View Log: ☐

**FINISH:**

### Installation Steps
10. Select the **Launch Dashboard** check box to launch the Dashboard after installing.
11. Click **Finish**. Essential Studio is installed in your system and the Syncfusion Dashboard is launched automatically. For more information, refer to *Brief Tour of Dashboard*.

### Note
The Completed screen is displayed once the selected platform is installed.

### 1.3.3 Command Line

Syncfusion Essential Studio supports installing the setup through command line install and uninstall. The following sections illustrate these options.

#### 1.3.3.1 Command line installation

Follow the steps below to install through command line in **silent** mode.

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References
- Refer to the *Brief Tour of Dashboard* for more information.

### RAG Annotations
<!-- tags: [Syncfusion, Winforms, Essential Studio, installation, dashboard, command line, silent mode] keywords: [Essential Studio, installation completion, source code add-on, Dashboard, command line install, uninstall] -->
```

---

<!-- 페이지 113 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_016.jpeg
document_name: common
page_number: 016
page_id: common#page_016
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:21Z
fidelity: lossless
-->

# Essential Common

## Overview
- License Agreement setup for Syncfusion Mobile MVC software.
- Terms and conditions acceptance required before proceeding.

## Content

### License Agreement

This Software License Agreement (the “Agreement”) is a legal agreement between you (“You”, “Your”, or “Customer”), and Syncfusion, Inc., a Delaware corporation with its principal place of business located at 2501 Aerial Center Parkway, Suite 200, Morrisville, NC 27560 (“Syncfusion”).

**Key Points:**
- Syncfusion licenses its products on a per-copy basis, on a site basis, and on an enterprise basis.
- Your right to use any given copy of a Syncfusion software product is generally set forth in this Agreement.
- If your copy of the software product is licensed under a **site license** or an **enterprise license**, additional terms and conditions will apply and will be set forth in a separate written agreement.

**Steps to Proceed:**
1. Carefully read all of the terms and conditions of this Agreement prior to downloading and/or installing or using the Licensed Product (as that term is defined below).
2. After reading the terms, click the **I accept the terms and conditions** check box.
3. Click **Next**. The **Select the Installation and Samples Folder** screen opens.

**Figure 10: License Agreement**

![License Agreement screenshot](https://syncfusion.com/assets/images/license-agreement-screenshot.png)

The screenshot above shows the License Agreement screen where you can review the terms and conditions and accept them by checking the box.

## Step-by-Step Guide

4. **After reading the terms, click the I accept the terms and conditions check box.**
5. **Click Next. The Select the Installation and Samples Folder screen opens.**

## Copyright Information
- **© 2013 Syncfusion. All rights reserved.**
- **Page Number:** 16

<!-- tags: [software license agreement, terms and conditions, syncfusion mobile MVC, site license, enterprise license, installation folder] keywords: [license agreement, syncfusion, mobile MVC, software installation] -->
```

---

<!-- 페이지 114 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_020.jpeg
document_name: common
page_number: 020
page_id: common#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:34Z
fidelity: lossless
-->

## Essential Common

### Installation Steps

1. Copy the `SyncfusionEssentialStudio_(version).exe` file in local drive. Example: `D:\temp`
2. Cancel the wizard.
3. Open the command prompt in administrator mode and pass the following arguments:

    ```
    "Setup file path\SyncfusionEssentialStudio(platform)_(version).exe" Install
    /PIDKEY:“(product unlock key)” /InstallPath:C:\Program Files\Syncfusion\x.x.x
    ```
    
    Example:
    ```
    "D:\Temp\SyncfusionEssentialStudio(platform) _11.1.0.1.exe" Install
    /PIDKEY:“product unlock key” /InstallPath:C:\Syncfusion\x.x.x
    ```

4. Setup will be installed.

**Note:** `x.x.x` needs to be replaced with the Essential Studio version installed in your machine and the product unlock key needs to be replaced with the unlock key for that version. Platform should be replaced with aspnet, aspnetmvc, mobilemvc, silverlight, windowsforms, windowsphone, winrt, or wpf.

### Command Line Uninstall Options

Syncfusion Essential Studio supports uninstalling the setup through command line in silent mode. The following steps illustrate this:

1. If you don’t have the extracted setup (`SyncfusionEssentialStudio(platform)_(version).exe`), then follow the steps from 2 to 7.
2. Double-click the Syncfusion Essential Studio platform Setup file. The self-Extractor wizard opens and extracts the package automatically.
3. The `SyncfusionEssentialStudio(platform)_(version).exe` file will be extracted into the Temp folder.
4. Run `%temp%`. The Temp folder will open. The `SyncfusionEssentialStudio(platform)_(version).exe` file will be available in one of the folders.
5. Copy the `SyncfusionEssentialStudio(platform)_(version).exe` file in local drive. Example: `D:\temp`
6. Cancel the wizard.
7. Open the command prompt in administrator mode and pass the following arguments:

    ```
    “Setup file path\SyncfusionEssentialStudio(platform) _(version).exe” /uninstall true
    ```
    
    Example:
    ```
    “D:\Temp\SyncfusionEssentialStudio(platform)_11.1.0.1.exe” /uninstall true
    ```

8. Setup will be uninstalled.

**Note:** `x.x.x` needs to be replaced with the Essential Studio version installed in your machine and Product unlock key needs to be replaced with the unlock key for that version. Platform should be replaced with aspnet, aspnetmvc, mobilemvc, silverlight, windowsforms, windowsphone, winrt, or wpf.
```

---

<!-- 페이지 115 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: common
page_number: 024
page_id: common#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:50Z
fidelity: lossless
-->

# Essential Common

## Overview
- Guides users through the installation process of the Syncfusion Essential Studio 2013 Vol 1 add-on.
- Focuses on entering user information during the installation sequence.
- Validates the unlock key and transitions to the Welcome screen.

## Content

### Installation Process

#### Step-by-Step Instructions

1. **Welcome Screen:**
   - Displayed at the beginning of the installation process.
   - Guides the user through the necessary steps.

2. **Collecting Information:**
   - User is prompted to provide their **User Name** and **Organization** details.
   - Enters an **Unlock Key** for validation.

   **Figure 17: User Information**
   ![User Information](figure_17_user_information.png)

   - Enter your **User Name**, **Organization**, and **Unlock Key** in the corresponding text boxes provided.
   - Click **Next**.

   **Note:** The unlock key is validated, and the preceding Welcome screen opens.

---

## Page-level Navigation/TOC (if applicable)

- Installation Process
  - Step-by-Step Instructions
    - Welcome Screen
    - Collecting Information

## Cross References

- See also:
  - [Installation Guide for Syncfusion Essential Studio 2013 Vol 1]

---

<!-- tags: [syncfusion-winforms, essential-studio-installation, user-information, unlock-key-validation] keywords: [user name, organization, unlock key, installation guide, validation, welcome screen] -->
```

---

<!-- 페이지 116 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: common
page_number: 028
page_id: common#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:01Z
fidelity: lossless
-->

## Essential Common

### Setup Installation Overview

The following pages focus on the installation process for the Syncfusion Essential Studio Source code add-on. The steps include guiding the user through the installation wizard, gathering necessary information, and initiating the installation. Below is a detailed breakdown of the installation process illustrated in **Figure 21: Setup-Installation**.

### Content
#### Installation Steps
- **Welcome (Step 1):**
  - The setup wizard starts here, welcoming the user to the installation process.
  
- **Collecting Information (Step 2):**
  - The wizard proceeds to collect relevant information necessary for the installation.

- **Ready to Install (Step 3):**
  - This stage confirms readiness to begin the installation of the Essential Studio Source code add-on.
  - The user is prompted to click "Install" to start the process or "Back" to review or change settings.
  - The "Cancel" button is available to exit the wizard.
  
- **Installing (Step 3):**
  - The actual installation process begins here, where the files are deployed on the system.
  
- **Completed (Step 4):**
  - Once the installation is complete, this final step confirms the successful setup.

#### Step-by-Step Instructions
Refer to **Figure 21: Setup-Installation** for detailed progress through the installation steps:

1. **Welcome Screen**
   - A standard welcome screen for the installation wizard.

2. **Collecting Information**
   - The necessary information is gathered to set up the software.

3. **Ready to Install**
   - This screen displays readiness to begin the installation. Click "Install" to proceed.
   - Options to go "Back" or "Cancel" are available if further adjustments are needed.

4. **Installation and Completion**
   - The process of installing files and components is executed, followed by confirmation once completed.

#### Example Instructions for Continuing the Installation
12. Click **Install** to continue with the installation.

### Figure: Setup-Installation
![](Syncfusion Essential Studio Source code add-on installer Setup)

**Date:** 27/02/2013  
**Version:** 11.1.0.21  

## Summary
The installation of the Syncfusion Essential Studio Source code add-on follows a sequential process across four key steps: Welcome, Collecting Information, Ready to Install, and Installation Completion. The user is guided through these steps with clear instructions and options to adjust settings before proceeding to the next step.

<!-- tags: [Syncfusion, WinForms, Essential Studio, Source code installation, Wizard] keywords: [Installation, Add-on, Setup process, Essential Studio Source code, Wizard] -->
```

---

<!-- 페이지 117 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: common
page_number: 032
page_id: common#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:19Z
fidelity: lossless
-->

# Essential Common

## Overview
- 1.6 Documentation setup
- Explore Source
- User Guide and Class Reference documentation provided.
- Detailed information about local and installed documentation for various Visual Studio versions.

## Content

### 1.6 Documentation setup

User Guide and Class Reference documentation is provided.

#### 1.6.1 User Guide

- **Local documentation** - A complete set of documentation for the User Guide is provided under the following headers:
  - Installed Documentation - Documentation pertaining to Essential Studio can be installed with your copy of Syncfusion local resources. Explore the following three categories of documentation to have a better idea of Essential Studio products:
    - Visual Studio 2005/Visual Studio 2008 User Guide
    - Visual Studio 2010 User Guide
    - Visual Studio 2012 User Guide

This local documentation can be accessed from the Dashboard > Utilities > Documentation > Local Documentation.

### Figure 25: Explore Source

![Essential Studio UI](https://i.imgur.com/placeholder.png)

**Description:**  
The image shows the dashboard interface for **Essential Studio**, highlighting the "Explore Source" option. Key elements include various application development options such as ASP.NET MVC, ASP.NET, Windows Forms, WPF, Silverlight, Windows Phone, Mobile MVC, and WinRT. It also features sections for Add-ons, Utilities, and License Management. Tools like the Project Wizard and Run Samples are available, along with UI, Reporting, and BI controls for creating professional ASP.NET MVC web applications. The dashboard indicates enhanced Visual Studio integration and provides links to documentation, release notes, and new features.

<!-- tags: [product, essential-studio, user-guide, documentation, visual-studio, mvc, windows-forms, winrt, addons, utilities, license-management] keywords: [syncfusion, essential studio, user guide, documentation setup, explore source, documentation, visual studio, mvc, windows forms, winrt, add-ons, utilities, license management, project wizard, run samples, ui controls, reporting, bi controls, local documentation, installed documentation] -->
```

---

<!-- 페이지 118 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: common
page_number: 036
page_id: common#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:35Z
fidelity: lossless
-->

# Essential Common

## Overview
- Provides comprehensive documentation for better understanding and configuring Syncfusion controls.
- Covers utilities such as documentation, toolbox configuration, assembly management, and license management.
- Explains the Link Install Setup for configuring Syncfusion controls on build machines.

## Content

### Documentation
**Online Documentation**
We have provided comprehensive documentation online to help you better understand our products.

- **User Guide**
- **Class Reference**

**Local Documentation**
Documentation pertaining to our products can be installed with your copy of Syncfusion's local resources. Explore the three categories of documentation to have a better idea of our products.

- **VS2005/VS2008 Class Reference and User Guide**
- **VS2010 Class Reference**
- **VS2010 User Guide**

### 1.7 Link Install Setup

#### Overview of Link Install Setup
Syncfusion provides the **Link Install Setup** to configure the Syncfusion controls in a build machine in which **Syncfusion Essential Studio** is not installed. This will install Essential Studio assemblies into the target folder. It also registers the product key to enable you to compile a project developed on a build machine.

#### Installing Link Install Setup
The following procedure illustrates how to install **Link Install Setup**:

1. **Double-click the Syncfusion Link Install Setup file.** The self-Extractor wizard opens and extracts the package automatically.

---

### Figure: Syncfusion Link Install Setup process
(WinZip Self-Extractor - essentialstudiolinkinstall.exe)

- **Thank you for choosing Syncfusion Essential Studio Link Install.**
- **Please wait while the setup prepares the Windows Installer package for installation. This process will take less than a minute, and afterwards, setup will start.**
- **Unzipping Essential Studio Link Install.msi**

---

## API Reference
- **Toolbox Configuration**
- **Assembly Management**
- **Documentation**
- **License Management**

## Code Examples
- Use the `essentialstudiolinkinstall.exe` self-extractor for setup.
- Install the required assemblies using the following steps.

### Example Setup Commands
```bash
essentialstudiolinkinstall.exe
```

## Page-level Navigation/TOC
- **Utilities**
  - ToolBox Configuration
  - Assembly Management
  - Documentation
  - License Management
- **Link Install Setup**

## Cross References
- Refer to the installation documentation for steps on configuring and deploying Syncfusion controls.

<!-- tags: [syncfusion, winforms, essentialstudio, linkinstallsetup, documentation, toolboxconfiguration, assemblymanagement, directives, codeexamples] keywords: [essentialsdk, 11.4.0.26, linkinstall, userguide, classreference, vssupport, toolsextensions, license, syncfusioninc, windowsforms] -->
```

---

<!-- 페이지 119 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: common
page_number: 040
page_id: common#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:51Z
fidelity: lossless
-->

# Essential Common

## Overview
- Provides a walkthrough of the installation steps for Syncfusion Essential Studio.
- Highlights the License Agreement screen displayed during the installation process.
- Guides users through accepting the terms and selecting the installation folder.

## Content

### Installation Steps

#### License Agreement Screen
The License Agreement screen is crucial for the installation process. At this stage, users are required to review and accept the terms of the software license agreement.

#### Figure: License Agreement Screen
Below is the detailed content of the License Agreement screen (Figure 32) displayed during the installation process.

#### Text of the License Agreement
**This Software License Agreement (the “Agreement”) is a legal agreement between you (“You,” “Your,” or “Customer”), and Syncfusion, Inc., a Delaware corporation with its principal place of business located at 2501 Aerial Center Parkway, Suite 200, Morrisville, NC 27560 (“Syncfusion”).**

Syncfusion licenses its products on a per-copy basis, on a site basis, and on an enterprise basis. Your right to use any given copy of a Syncfusion software product is generally set forth in this Agreement. In the event that your copy of this software product is licensed under a site license or an enterprise license, additional terms and conditions shall also apply and will be set forth in a legal document.

#### Acceptance Options
- **I accept the terms in the License Agreement:** Choose this option after reading the terms.
- **I do not accept the terms in the License Agreement:** If you do not agree with the terms, select this option to backtrack or cancel the installation.

#### Date and Version
- **Date:** 19/02/2013
- **Version:** 11.1.0.21

#### Instructions for Installation
After reviewing the license agreement:
1. Click the **I accept the terms in the License Agreement** option.
2. Click **Next**. The **Select the Installation Folder** screen will open.

---

## API Reference
None applicable in this context.

## Code Examples
None applicable in this context.

## Page-level Navigation/TOC
- **Installation Steps**
- **License Agreement Screen**

## Cross References
- Refer to the installation guide for complete instructions on installing and configuring Syncfusion WinForms.

## RAG Annotations
<!-- tags: [syncfusion, winforms, installation, license agreement] keywords: [Syncfusion, Install, License Agreement, terms, installation folder] -->
```

---

<!-- 페이지 120 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_044.jpeg
document_name: common
page_number: 044
page_id: common#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:06Z
fidelity: lossless
-->

## Overview

- The installation process of Syncfusion Essential Studio Link 11.1.0.21 includes steps such as Welcome, Collecting Information, Installing, and Completed.
- The Digitally Signed Assemblies Setup feature allows the signing of Syncfusion assemblies with a .pfx file.
- Instructions are provided for a smooth installation and setup of both Essential Studio Link and Digitally Signed Assemblies.

## Content

### Winforms Installation Completed

![Figure 36: Installation Completed](#)
**Figure 36: Installation Completed**

The image shows the completion of the Syncfusion Essential Studio Link installation process. The steps are as follows:

1. **Welcome**
2. **Collecting Information**
3. **Installing**
4. **Completed**

The progress status is visually indicated, with the section currently in progress highlighted in green, and the completed sections in yellow. The interface provides buttons for navigating through the setup process.

### Next Steps

14. Click **Finish** to exit the Setup Wizard. Assemblies will be installed.

### Digitally Signed Assemblies Setup

#### Overview

Syncfusion provides the **Digitally Signed Assemblies Setup**, which signs the Syncfusion assemblies with a `.pfx` file.

#### Installation Steps

The following steps illustrate how to install the **Digitally Signed Assemblies Setup**:

1. Double-click the **Syncfusion Digitally Signed Setup** file. The self-Extractor wizard opens and extracts the package automatically.

---

## API Reference (if applicable)

Not applicable on this page.

## Code Examples (multi-language supported)

Not applicable on this page.

## Page-level Navigation/TOC (if applicable)

Not applicable on this page.

## Cross References

Not applicable on this page.

---

<!-- tags: [syncfusion-sdk, winforms, installation, digitally-signed-assemblies, essential-studio-link] keywords: [installation, setup, digitally signed, pfx, syncfusion assemblies, self-extractor, extraction] -->
```

---

<!-- 페이지 121 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_048.jpeg
document_name: common
page_number: 048
page_id: common#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:19Z
fidelity: lossless
-->

## Overview

- This page covers the process of installing and accepting the license agreement for the Syncfusion Essential Studio 2013 Vol 1.
- It details the steps involved in interacting with the License Agreement screen.
- Includes instructions for selecting the installation folder after accepting the terms.

## Content

### License Agreement Screen

The License Agreement screen is displayed as part of the setup process for the Syncfusion Essential Studio 2013 Vol 1. It includes the following sections:

#### License Agreement Text
- **Essential Studio 2013 Vol 1** is prominently displayed at the top.
- The License Agreement is presented, which outlines the legal terms and conditions between the user and Syncfusion, Inc.
- The terms mention the licensing basis for Syncfusion software products, including per-copy, site, and enterprise licenses.

#### Installation Process Steps
1. **Welcome**
2. **Collecting Information**
3. **Installing**
4. **Completed**

#### User Interaction
- The user is prompted to read the license agreement carefully.
- Two options are provided for accepting or declining the terms:
  - **I accept the terms in the License Agreement**
  - **I do not accept the terms in the License Agreement**

#### Navigation Buttons
- **Back** button to return to the previous screen.
- **Next** button to proceed to the next step.
- **Cancel** button to exit the installation process.

### Instructions for Installation

1. **Accepting the Terms**: After reading the License Agreement, click the **I accept the terms in the License Agreement** option.
2. **Proceeding to the Next Step**: Click the **Next** button. The Select the Installation Folder screen will open.

## API Reference

- The setup process involves no direct references to API calls or methods at this stage. It primarily focuses on user interaction with the installation interface.

## Code Examples

No code examples are shown, as this section focuses on the user interface and setup process.

## Page-level Navigation/TOC (if applicable)

- Not applicable for this page. The content is focused on a single step in the installation process.

## Cross References

See also:
- Installation guidelines for Syncfusion products.
- License Agreement documentation for Syncfusion software.

<!-- tags: [syncfusion, essential studio, license agreement, installation] keywords: [syncfusion essential studio, license agreement, installation folder, setup process, accept terms, next step] -->
```

---

<!-- 페이지 122 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_052.jpeg
document_name: common
page_number: 052
page_id: common#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:35Z
fidelity: lossless
-->

## Essential Common

### Installation of Essential Studio Digitally Signed Assemblies

#### Overview
- Installation process overview for Syncfusion Essential StudioDigitally Signed Assemblies.
- Stages include Welcome, Collecting Information, Installing, and Completed.
- Progress bar indicating the current installation status.

#### Content

**Figure 45: Installing**

The installation process for Syncfusion Essential Studio Digitally Signed Assemblies is as follows:

- **Welcome (Step 1)**: Initialization stage of the installation wizard.
- **Collecting Information (Step 2)**: Gathering necessary information for the installation.
- **Installing (Step 3)**: Core installation phase where assemblies are being installed.
- **Completed (Step 4)**: Confirmation that the installation process has been successfully completed.

A note is included, stating:
> **Note:** The Completed screen is displayed once the selected package is installed.

### Installation Window Details
- **Version**: 11.1.0.21
- **Date**: 19/02/2013

The progress bar is displayed near the bottom of the installation window, along with buttons such as `< Back`, `Next >`, and `Cancel`.

### Cross References
- See also: [Installation Overview](#installation-overview)
- See also: [Syncfusion Winforms Installation Guide](#syncfusion-winforms-installation)

<!-- tags: [syncfusion-sdk, winforms, installation, essential-studio, digitally-signed-assemblies, version-11.1.0.21] keywords: [syncfusion, essential studio, digitally signed assemblies, installation process, progress bar, installation steps, completed screen] -->
```

---

<!-- 페이지 123 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_056.jpeg
document_name: common
page_number: 056
page_id: common#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:01:47Z
fidelity: lossless
-->

# Essential Common

## Overview
- Instructions for installing Syncfusion Essential Studio Service Pack.
- Focus on initiating the installation process.
- Step-by-step guide to proceed with installation.

## Content

### Installation Instructions

1. **Prepare for Installation**
   - Ensure your system meets the prerequisites for installing Syncfusion Essential Studio Service Pack.
   - Launch the installation executable file.

2. **Follow Setup Prompts**
   - The setup will guide you through various steps, including selecting the installation location and choosing components to install.
   - Review the license agreement and accept the terms to continue.

3. **Ready to Install**
   - Upon reaching the final setup screen, verify that everything is configured as desired.
   - The setup window confirms readiness for installation.

4. **Continue with Installation**
   - **Figure 49: Ready to Install**
     - ![Figure 49: Ready to Install](#)
     - The window displays a confirmation message indicating that the setup is ready to begin installing Syncfusion Essential Studio Service Pack 11.1.0.21 on your computer.
     - The options to proceed are:
       - **Back**: Return to the previous screen.
       - **Install**: Proceed with the installation.
       - **Cancel**: Exit the installation process.

5. **Click Install to continue installing.**

## API Reference

- **Main Functionality**
  - This section typically references classes, methods, and events for the product, but in this context, the installation instructions are the primary focus.

## Code Examples

- No code examples are included in this section since the content is focused on installing the software.

## RAG Annotations

<!-- tags: [Syncfusion, Winforms, Installation, Service Pack, 11.4.0.26] keywords: [Essential Studio, Service Pack, Installation, Setup, Syncfusion, Winforms] -->
```

---

<!-- 페이지 124 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: common
page_number: 060
page_id: common#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:00Z
fidelity: lossless
-->

# Essential Common

## Overview
- Provides details on the QTP Add-on for testing Syncfusion controls using Essential Test Studio.
- Emphasizes the integration with Mercury Quick Test Professional and the importance of custom libraries for testing Windows-based controls.
- Lists specific controls supported by Essential Test Studio and new controls added for QTP support.

## Content

### 1.10 QTP Add-on

**Syncfusion supports Quick Test Professional software with the help of Essential Test Studio (termed as QTP add-on), which has been specially designed to meet the requirements of professionals who need to test our controls. Essential Test Studio contains Custom Libraries, which help Quick Test Professional to record and replay the scripts of the application that contains the Syncfusion controls. These custom libraries are built with the help of Quick Test Professional .NET Add-in extensibility. For more details, refer to Mercury Quick Test Professional help.**

**Essential Test Studio supports the following Windows-based controls:**

#### Essential Grid
- Grid control
- Grid Grouping control
- GridDataBoundGrid control
- Grid List control
- TabBar Splitter control

#### Essential Tools
- Docking Package
- Menus Package
- Command Bars Package
- Tree Package
- Editors Package
- Tabs Package
- Navigation Package
- Notification Package

#### New Controls added for QTP support
- ColorPickerAdv
- Scroller Frame
- Ribbon Control
- Chart Control

### Cross References
- Refer to Mercury Quick Test Professional help for more details on the integration and usage of the QTP Add-on.

<!-- tags: [Syncfusion Winforms, QTP Add-on, Essential Test Studio, Mercury Quick Test Professional] keywords: [testing, controls, custom libraries, extensibility, Windows-based controls, Grid controls, Docking Package, Menus Package] -->
```

---

<!-- 페이지 125 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: common
page_number: 064
page_id: common#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:12Z
fidelity: lossless
-->

# Essential Common

## Overview
- This page provides a sample browser displaying the Essential Grid for ASP.NET MVC, highlighting its features and scalability.
- The grid offers high-performance and built-in support for data visualization, JSON, paging, grouping, and Excel-like editing and filtering.
- It is adaptable, simple, flexible, and extensively themeable, making it a preferred choice for data-grid needs.
- Various features such as virtual scrolling, hierarchical grids, and real-time binding are demonstrated in the featured samples.

## Content

### Essential Grid for ASP.NET MVC

**Overview**
- A scalable, high-performance data grid designed for ASP.NET MVC with built-in support for data visualization, JSON, paging, grouping, and Excel-like editing and filtering.

#### Featured Samples
- **Virtual Scrolling**: Demonstrates the grid's ability to handle large datasets efficiently.
- **Excel-like Edit**: Allows editing grid cells in an Excel-like manner.
- **Hierarchical Grid**: Illustrates the creation of nested grids.
- **Hierarchical Column Template**: Shows how to define custom templates for hierarchical columns.
- **Real-Time Binding**: Demonstrates dynamic updates in the grid.

### Navigation and Features
#### Main Menu
- **Grid**
  - Product Showcase
  - Getting Started
  - Rows and Columns
  - Templates
  - Data Binding
  - Editing
  - Paging
  - Sorting
  - Grouping
  - Filtering
  - Cell Merging
  - Hierarchy
  - Summary
  - Formatting
  - Drag-and-Drop
  - Appearance
- **Tools**
- **Chart**
- **Gauge**
- **Diagram**
- **Schedule**
- **DocIO**
- **Pdf**
- **XlsIO**
- **PdfViewer**
- **Reports**
- **OlapGrid**
- **OlapClient**

### Figure: Essential Studio ASP.NET MVC Sample Browser

**Figure 55: Essential Studio ASP.NET MVC Sample Browser**

### Mobile MVC

10. Mobile MVC

---

<!-- tags: [Essential Grid, ASP.NET MVC, Data Grid, Virtual Scrolling, Excel-like Edit, Hierarchical Grid, Real-Time Binding] keywords: [scrolled, edits, hierarchy, binding, grid, virtual, Excel, hierarchical, real-time] -->
```

---

<!-- 페이지 126 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_068.jpeg
document_name: common
page_number: 068
page_id: common#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:26Z
fidelity: lossless
-->

## Essential Common

### Windows Phone Sample Browser

**Figure 60: Essential Studio Windows Phone Sample Browser**

![Figure 60: Essential Studio Windows Phone Sample Browser](https://example.com/image60.png)

#### Overview
- Demonstrates various functionalities including flight reservation, patient monitoring, stock analysis, and sales analysis.
- Utilizes Syncfusion controls to enhance mobile application development for Windows Phone platforms.

#### Content

##### WinRT
An introduction or section on Windows Runtime (WinRT) is mentioned, indicating a focus on platform-specific features or development considerations.

### Additional Resources
For more information or detailed documentation, refer to the [Syncfusion Documentation](https://www.syncfusion.com/documentation).

<!-- tags: [syncfusion, windows phone, sample, winrt, controls, essential studio, mobile, windows phone] keywords: [windows phone sample, winrt, syncfusion, essential studio, mobile development, stock analysis, flight reservation, patient monitoring] -->
```

---

<!-- 페이지 127 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_072.jpeg
document_name: common
page_number: 072
page_id: common#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:35Z
fidelity: lossless
-->

## Overview

- The image illustrates the "Help" section of Syncfusion’s Essential Studio, focusing on the menu options available under the "Help" tab.

## Content

### Essential Studio Help Menu

The figure below shows a user interface snapshot of the "Help" menu within the Syncfusion Essential Studio:

```plaintext
Figure 66: Help

+ Essential Studio
  - File
  - Studio
  - Tools
  - Help
    + About
    + Support
  - Updates
```

### Description

1. **Help Dropdown**:
   - The "Help" tab, located in the menu bar, provides access to two sub-options:
     - **About**: Likely contains information about the software version, build details, and legal notices.
     - **Support**: Provides details on how to get help, such as contacting Syncfusion’s support team or accessing documentation and resources.

2. **Other Menu Options**:
   - **File, Studio, Tools**: These are standard menu options in software applications, typically used for file management, project tools, and utilities.
   - **Updates**: This option is likely for checking and installing software updates.

## API Reference

There are no specific APIs or code examples listed in this section of the user guide.

## Code Examples

There are no code examples available for this page.

## Page-level Navigation/TOC

This page focuses solely on the "Help" menu within the Syncfusion Essential Studio, providing a brief overview of its functionality.

## Cross References

See also: 
- Related sections such as "About," "Support," and "Updates" for more detailed information on accessing help and support.

<!-- tags: [Syncfusion Winforms, Essential Studio, Help Menu] keywords: [Help, About, Support, Updates, Menu Bar] -->
```

---

<!-- 페이지 128 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_076.jpeg
document_name: common
page_number: 076
page_id: common#page_076
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:02:47Z
fidelity: lossless
-->

## Recommended Software

### Overview
- Lists the recommended software configurations for Syncfusion WinForms applications.
- Highlights compatibility with .NET Framework versions and SQL Server versions for various development frameworks (ASP, MVC, WF, WPF, SL, MOB, WRT).
- Indicates installation status with checkmarks for supported configurations.

### Content

#### Recommended Software

| **Framework** | **.NET Framework** | **Additional Requirements** | **Status** |
|---------------|---------------------|-----------------------------|------------|
| **ASP**       | .NET FW 3.5 SP1/4.0/4.5 | SQL Server 2005/2008/2012 | ✓          |
| **MVC**       | .NET FW 3.5 SP1/4.0/4.5 | MVC 2.0/MVC 3.0          | ✓          |
| **WF**        | .NET FW 2.0/3.5 SP1/4.0/4.5 | -                       | ✓          |
| **WPF**       | .NET FW 3.5 SP1/4.0/4.5 | SQL Server 2005/2008/2012 | ✓          |
| **SL**        | .NET FW 4.0/4.5     | Silverlight 4 SDK          | ✓          |
|               |                     | SQL Server 2005/2008/2012   | ✓          |
| **MOB**       | .NET FW 3.5 SP1/4.0/4.5 | MVC 2.0/MVC 3.0          | ✓          |
| **WRT**       | .NET FW 4.5        | Visual Studio 2012         | ✗          |

- **Recheck** and **OK** buttons are available for verification and confirmation of software installation.

#### Other Utilities

This section provides access to additional utilities for enhancing Syncfusion product usage. It includes:

1. **Add-ons**
   - Lists add-on utilities that assist users in utilizing additional Syncfusion services.

2. **Utilities**
   - Displays essential utilities for managing Syncfusion controls:
     - **Toolbox Configuration**: Configures Syncfusion controls for various .NET frameworks with compatible Visual Studio versions.
     - **Assembly Manager**: Manages the installation and uninstallation of Syncfusion Essential Studio assemblies in the GAC and in the Assemblies folders.
     - **Build Management**: Enables building or debugging assemblies using the source installed in Essential Studio's installed location.

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
  
## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

### RAG Annotations
- <!-- tags: [recommended_software, syncfusion_winform, configuration_requirements, assembly_manager, build_management] -->
- keywords: [recommended software, .NET Framework, SQL Server, ASP, MVC, WF, WPF, SL, MOB, WRT, Toolbox Configuration, Assembly Manager, Build Management, Syncfusion Winforms]
```


---

<!-- 페이지 129 -->

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

---

<!-- 페이지 130 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_084.jpeg
document_name: common
page_number: 084
page_id: common#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:22Z
fidelity: lossless
-->

## Launching the Build Manager

The following steps will launch the Build Manager:

1. Open the Syncfusion Dashboard.
2. Click Utilities > Build Management.
3. Click Launch button for Build Manager.
4. The Syncfusion Build Manager x.x.x.x window opens.

**Note:** Build Manager will be available in the Dashboard only when Source code is installed. You can also launch the Build Manager from the following location:

```
C:\Program Files\Syncfusion\Essential Studio\x.x.x.x\Utilities\Build
Manager\buildmanagerwindows.exe
```

## Navigation and Launch Instructions
- **Dashboard Path:** Open the Syncfusion Dashboard and navigate to **Utilities > Build Management** to access the Build Manager.
- **Alternative Path:** If you prefer, directly launch the Build Manager from:
  ```
  C:\Program Files\Syncfusion\Essential Studio\x.x.x.x\Utilities\Build
  Manager\buildmanagerwindows.exe
  ```

## Availability Note
- The Build Manager is accessible via the Dashboard only when the Source code has been installed. Ensure the Source code is installed to use this feature through the Dashboard interface.

## Accessing Build Manager
To ensure the Build Manager is available:
- Confirm that the **Source code** is installed in your environment.
- Alternatively, manually invoke the Build Manager through the provided executable path, bypassing the Syncfusion Dashboard.

## Copyright
© 2013 Syncfusion. All rights reserved.
```

---

<!-- 페이지 131 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_088.jpeg
document_name: common
page_number: 088
page_id: common#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:33Z
fidelity: lossless
-->

## Essential Common

### Adding a Product Key

**Figure 79: Syncfusion License Manager**

The following are the steps to add a product key:

1. **Open the Syncfusion License Manager dialog.**

   **Figure 80: Syncfusion License Manager dialog.**
   
   ![Syncfusion License Manager dialog](https://example.com/syncfusion-license-manager-dialog.png)

2. **Click Add Key.** The following dialog will open:

   **Figure 81: Key Manager**
   
   ![Key Manager](https://example.com/key-manager.png)

3. **Enter the product license key in the space provided.**

### Receive the Copyright
© 2013 Syncfusion. All rights reserved.


## Page-level Navigation/TOC (if applicable)
<!-- tags: [syncfusion, sdk, user-guide, license, manager, key, add] keywords: [syncfusion license manager, add key, product license, steps, essential, common, process] -->
```

---

<!-- 페이지 132 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_092.jpeg
document_name: common
page_number: 092
page_id: common#page_092
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:42Z
fidelity: lossless
-->

## Essential Common

### WinForms-specific conventions

The **Syncfusion Toolbox Installer** adds Syncfusion controls into the Visual Studio .NET toolbox based on the Visual Studio version installed.

#### Framework Options

- **2.0**
- **3.5**
- **4.0**

#### Platform Options

- **ASP.NET**
- **Silverlight**
- **Windows Forms**
- **WPF**

#### Action Options

- **Install VS 2005**
- **Install VS 2005 Controls in VS 2008**
- **Install VS 2008**
- **Install VS 2005 Controls in VS 2010**
- **Install VS 2008 Controls in VS 2010**
- **Install VS 2010**
- **Install VS 2012**

### Toolbox Configuration Options

- **Install VS2005** – Configures Framework 2.0 Syncfusion controls in VS 2005 toolbox.
- **Install VS2008** – Configures Framework 3.5 Syncfusion controls in VS 2008 toolbox.
- **Install VS2010** – Configures Framework 4.0 Syncfusion controls in VS 2010 toolbox.
- **Install VS2012** – Configures Framework 4.0 Syncfusion controls in VS 2012 toolbox.
- **Install VS2005 Controls in VS2008** – Configures Framework 2.0 Syncfusion controls in VS 2008 toolbox.
- **Install VS2005 Controls in VS2010** – Configures Framework 2.0 Syncfusion controls in VS 2010 toolbox.
- **Install VS2008 Controls in VS2010** – Configures Framework 3.5 Syncfusion controls in VS 2010 toolbox.

### Instructions

4. The **Information** dialog will open. Click **OK**.

<!-- tags: [Syncfusion Winforms, Toolbox Installer, control configuration, Visual Studio versions, framework, platform options, action options, configuration options, dialog, Information] keywords: [Syncfusion, Winforms,mite Controlse .NET, Visual Studio, framework 2.0, framework 3.5, framework 4.0, ASP.NET, Silverlight, Windows Forms, WPF,Installation options, perform action, exit] -->
```

---

<!-- 페이지 133 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_096.jpeg
document_name: common
page_number: 096
page_id: common#page_096
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:57Z
fidelity: lossless
-->

# Essential Common

1. You can open the Project Migration Tool from the following location: (Installed location)\Syncfusion\Essential Studio\x.x.x\Utilities\Project Migration\ProjectMigrationWindows.exe.

![Syncfusion Project Migration](syncfusion_project_migration.png)

Figure 90: Syncfusion Project Migration

2. Select the project to be upgraded in the Select project folder field.

**Note:**

- You can also select multiple projects using the Select folder list option.
- The ASP.NET MVC project type is not supported by the Project Migration Tool.

3. Select a folder to store a backup in the Select backup folder field.
4. Enter the Essential Studio version number in the Essential Studio version field (for example, 11.2.0.25).
5. Select the required .NET version from the .NET Framework version drop-down list.
6. Select the Remove hint path from project check box, if you want to remove the hint from the project.
7. Click Perform Action. The utility will upgrade the selected projects to the newer versions.

### 1.13.7.1 Command Line

The following steps illustrate how to run the Project Migration tool through command line.
```html
<!-- tags: [syncfusion, winforms, project migration tool] keywords: [project migration, syncfusion essential studio, command line, asp.net mvc, essential studio version, .net framework version, remove hint path] -->
```
```markdown

```

---

<!-- 페이지 134 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_100.jpeg
document_name: common
page_number: 100
page_id: common#page_100
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:08Z
fidelity: lossless
-->

## Overview
- This section outlines the steps to enter user information during the installation of Syncfusion Orubase Studio, including input fields like User Name, Organization, and Unlock Key.
- The process includes entering the necessary details and proceeding to the License Agreement screen after validation.

## Content

### Installation Process

The screen displayed is part of the installation process for Syncfusion Orubase Studio. The steps are as follows:

#### User Information Screen

<figure>
 <img src="attachment:UserInformationScreen.png" alt="User Information Screen"/>
 <figcaption>Figure 93: User Information screen</figcaption>
</figure>

#### Instructions

1. **Welcome Screen**: The initial stage in the installation process.
2. **Collecting Information**: Enter the required personal and organizational details.
3. **Installing**: The software installation phase begins after providing the required information.
4. **Completed**: Marks the end of the installation process.

#### Input Fields

- **User Name**: A field to input the user's name.
- **Organization**: A text box for the user to add their organization details.
- **Unlock Key**: A required field for entering a valid unlock key.

#### Actions

1. **Get a Free Evaluation Key**: A button to request an evaluation key if needed.
2. **<Back**: Allows returning to the previous screen.
3. **Next**: Proceeds to the next step after entering the required information.
4. **Cancel**: Stops the installation process.

#### Steps to Proceed

1. Enter the **User Name**, **Organization**, and **Unlock Key** in the respective text boxes provided.
2. Click **Next** to advance to the next step.

---

### Note

**The unlock key is validated, and the preceding License Agreement screen opens after validation.**

## API Reference

- **Unlock Key Validation**: After inputting the key, it is validated to ensure it is correct and active.

---

## Code Examples

No specific code examples are provided in this section.

---

## Cross References

- Refer to the License Agreement documentation for details on license terms and conditions.

---

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, Orubase Studio, Installation, Unlock Key, User Information] keywords: [Syncfusion Orubase Studio, User Information, Organization, Unlock Key, Free Evaluation Key, License Agreement] -->
```

---

<!-- 페이지 135 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_104.jpeg
document_name: common
page_number: 104
page_id: common#page_104
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:22Z
fidelity: lossless
-->

## Overview
- Describes the installation process for Syncfusion Orubase Studio.
- Highlights the steps in the installation wizard, focusing on the "Ready to Install" stage.
- Provides instructions to proceed with the installation by clicking the "Install" button.

## Content

### Installation Wizard

The image depicts the installation wizard for Syncfusion Orubase Studio 1.1.0.69. The wizard includes the following steps:

1. **Welcome** - Introduction to the installation process.
2. **Collecting Information** - Gathering necessary system information.
3. **Installing** - The actual installation phase.
4. **Completed** - Confirming successful completion of the installation.

#### Ready to Install
- The setup wizard is ready to begin the installation of Orubase Studio.
- Users can click "Install" to commence the installation.
- Options to "Back" and "Cancel" are provided to navigate or terminate the process.

**Figure: Ready to Install**
![](Syncfusion Orubase Studio 1.1.0.69 Setup - Ready to Install)

### Instructions
10. Click **Install** to continue with the installation.

## Page-level Navigation/TOC (if applicable)
- This section is part of a broader guide, likely titled "Essential Common."
- The page highlights a specific phase in the installation process, making it a critical step in the user guide.

## Cross References
- See also: Other sections related to installation or troubleshooting in the user guide.

<!-- tags: [Syncfusion Winforms, installation, Orubase Studio, wizard, setup] keywords: [installation, installation wizard, Orubase Studio, Syncfusion, setup process, install, back, cancel] -->
```
```

---

<!-- 페이지 136 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_108.jpeg
document_name: common
page_number: 108
page_id: common#page_108
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:34Z
fidelity: lossless
-->

## 3 Metro Studio

### 3.1 Overview

Create attractive icons and path values with Syncfusion Metro Studio.

### 3.2 Step-by-Step Installation

The following are the steps to install the Metro Studio Setup.

1. Double-click the Syncfusion Metro Studio Installer Setup file. The Syncfusion Metro Studio Installer wizard opens.

![Figure 101: Unified Installer](https://example.com/path-to-unified-installer-image.png)

2. Click Next.

### Note: `Inno script` extracts the `syncfusionmetrostudiosetup.exe` dialog, displaying the unzip operation of the package.

<!-- tags: [Syncfusion Windows Forms, Metro Studio, Installation Guide] keywords: [Windows Forms, Metro Studio, Installation, Package, Syncfusion, 11.4.0.26, Step-by-Step, User Guide] -->
```

---

<!-- 페이지 137 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_112.jpeg
document_name: common
page_number: 112
page_id: common#page_112
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:42Z
fidelity: lossless
-->

## Overview

- This page describes the setup process for Syncfusion Metro Studio 2.
- It includes steps to complete the installation and reach the License Agreement screen.
- The interface and features are detailed, demonstrating the user flow.

## Content

### **Installing Metro Studio 2 Setup**

#### Figure 105: Setup

1. The setup wizard guides the user through the installation process for **Syncfusion Metro Studio 2.0.1.1**.
2. The interface contains distinct panels:
   - **Left Panel:** Displays the progress of the installation steps:
     - Welcome
     - Collecting Information
     - Installing
     - Completed
   - **Main Window:** Shows the **Syncfusion Metro Studio 2** branding and welcome message:
     - "Welcome to Syncfusion Metro Studio 2"
   - **Message Area:** Provides a confirmation message:
     ```
     Thank you for the information provided. Authorized features have been unlocked.
     The setup wizard has the information needed to proceed with installation.
     Click Next to continue or Cancel to exit the setup wizard.
     ```
   - **Control Buttons:** Offers option buttons:
     - `< Back`
     - `Next >`
     - `Cancel`

#### Installation Step Details

1. **Welcome:** The initial panel providing an overview of the installation process.
2. **Collecting Information:** The user provides necessary details for the installation.
3. **Installing:** The setup proceeds with the installation of the software.
4. **Completed:** Marks the end of the setup process.

#### Proceeding to License Agreement

- After the initial setup steps, clicking `Next` progresses the user to the **License Agreement** screen.

### Additional Notes

- The setup interface includes branding and version information to ensure clarity.
- The user flow is clearly presented to guide the user through the installation process.

## Page-level Navigation/TOC

- **Setup Steps:**
  - Welcome
  - Collecting Information
  - Installing
  - Completed
- **Proceeding:**
  - Clicking `Next` leads to the License Agreement.

<!-- tags: Metro Studio, Installation, License Agreement, version: 2.0.1.1 -->
```

---

<!-- 페이지 138 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_116.jpeg
document_name: common
page_number: 116
page_id: common#page_116
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:56Z
fidelity: lossless
-->

## Overview
- Guides users through installing Metro Studio 2.0.1.1.
- Highlights customization and export features of icons in Metro Studio.
- Provides instructions for initiating and completing the installation process.

## Content

### Installation of Metro Studio

#### Installing Metro Studio

The figure below illustrates the process of installing **Syncfusion Metro Studio 2.0.1.1**:

- **Welcome:** Initial setup stage.
- **Collecting Information:** Gather necessary details for installation.
- **Installing:** The installation in progress, with a status bar indicating progress.
- **Completed:** The final stage once the installation is finished.

**Features:**
- **Customize and export icons as a group:** The software enables sophisticated icon customization and export capabilities.

**Installation wizard message:**
- A message indicates that the setup wizard is installing Metro Studio, which will take a few minutes.

**Status update:**
- The status bar shows the progress of the installation.

**Navigation options:**
- Buttons for **< Back**, **Next >**, and **Cancel** are available for user interaction during the installation.

**Note:** The completed screen is displayed once the selected package is installed.

---

## API Reference (if applicable)
This section would typically include detailed API information related to the installation or export functionalities of Metro Studio, but it is not visible in the provided image.

## Code Examples (multi-language supported)
This section would include code snippets demonstrating how to programmatically interact with Metro Studio, but such details are not present in the image.

## Page-level Navigation/TOC (if applicable)
This section would contain a table of contents or cross-references, but none are visible in the provided image.

## RAG Annotations
<!-- tags: [Syncfusion, Metro Studio, Installation, Icon Export, Winforms] keywords: [installation wizard, custom icon export, Syncfusion Metro Studio 2.0.1.1, progress bar, completed installation screen] -->
```

---

<!-- 페이지 139 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_120.jpeg
document_name: common
page_number: 120
page_id: common#page_120
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:09Z
fidelity: lossless
-->

# 4 Frequently Asked Questions

This section covers frequently asked questions related to Essential Studio.

## 4.1 How to Configure the Toolbox of Visual Studio Manually

The following are the steps to load the Syncfusion controls in toolbox of visual studio by configuring the toolbox:

### 4.1.1 Toolbox Configuration Utility

To configure the toolbox using Toolbox Configuration Utility, refer to Toolbox Configuration.

### 4.1.2 Manually Configuring VS Toolbox

The following are the steps to configure VS Toolbox manually for Syncfusion tools:

1. **Close all Visual Studio running instances.**
2. **Remove the *.tbd files except the toolbox.tbd from the following location:**

   - **Windows XP:**

     ```
     C:\Documents and Settings\(user name)\Local Settings\Application Data\Microsoft\VisualStudio\10.0
     ```

   - **Vista/Windows 7:**

     ```
     C:\Users\(user name)\AppData\Local\Microsoft\VisualStudio\10.0
     ```

   <img src="safe_note.png" alt="Note: It will take some time to configure the toolbox and create tbd files when initially loading the toolbox in VS2010.">

   3. Re-open the Visual Studio environment. The VS toolbox will be configured.

### Adding Syncfusion controls in the customized toolbox

The following are the steps to add the Syncfusion controls in the user customized toolbox:

1. Open Visual Studio and then create a new tab named **Syncfusion** in the toolbox.
```

---

<!-- 페이지 140 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_124.jpeg
document_name: common
page_number: 124
page_id: common#page_124
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:20Z
fidelity: lossless
-->

# Essential Common

## Overview
- Instructions for configuring the licenses.licx file as an embedded resource.
- Details on resolving licensing errors in a Syncfusion project.
- Steps to manage and fix license issues automatically.

## Content

### Property Window

#### Figure 116: Property Window
The property window shows the configuration for the `licenses.licx` file in the `SampleApplication` project.

- **Build Action**: Embedded Resource
- **Copy to Output Directory**: Do not copy
- **Custom Tool**: Not specified
- **Custom Tool Namespace**: Not specified
- **Miscellaneous**
  - **File Name**: licenses.licx
  - **Full Path**: C:\Users\Varun\Desktop\SampleApplication\licenses.licx

#### Solution Explorer View
The Solution Explorer displays the structure of the `SampleApplication` project, showing:
- Solution 'SampleApplication' (1 project)
  - SampleApplication
    - Properties
    - References
    - bin
    - obj
    - Form1.cs
    - licenses.licx
    - Program.cs
    - SampleApplication.csproj.bak
    - Syncfusion.LicenseEnabler.Licx.Success.log
    - Syncfusion.LicenseEnabler.Project.Success.log

### Licensing Error Handling

6. **A Licensing Error message will open**.

#### Licensing Error Dialogue Box
The dialogue box displays the following error message:

```
Syncfusion Licensing Runtime was not able to detect a valid licx file with an entry for Syncfusion controls in this project. Select 'Fix It' to let the runtime correct this error automatically.
```

- **Buttons**:
  - **View**: Option to view more details about the error.
  - **Fix It**: Automatically resolves the licensing issue.

### Resolving Licensing Issues
To resolve licensing errors:
1. Ensure the licenses.licx file is correctly configured as an embedded resource.
2. Use the "Fix It" option in the licensing error dialogue to automatically correct the error.

## API Reference

This section does not cover specific API elements but provides a general understanding of configuring and troubleshooting licensing issues in Syncfusion WinForms applications.

## Code Examples

No code examples are provided in this specific section, as the focus is on configuring licensing settings.

## Cross References

- Refer to the Syncfusion documentation on configuring and managing licensing files for more information.

<!-- tags: syncfusion, winforms, licensing, licenses.licx, embedded resource, error handling keywords: essential common, property window, solution explorer, licensing error, fix it, configure licenses -->
```

---

<!-- 페이지 141 -->

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

---

<!-- 페이지 142 -->

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

---

<!-- 페이지 143 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_136.jpeg
document_name: common
page_number: 136
page_id: common#page_136
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:03Z
fidelity: lossless
-->

### Overview
- The page explains how to handle incorrect unlock keys during user registration for Syncfusion Studio.
- Guides users on retrieving the correct version-specific license keys using Direct-Trac.
- Details on implementing localization support in WPF applications using Syncfusion Essential Studio products.

## Content

### Figure 129: User Registration Dialog (Wrong Version)

**User Registration Dialog Interface:**
- **User Name:** Syncfusion
- **Organization:** Syncfusion
- **Unlock Key:** *Provided key based on wrong version (10.3.0.1).*
- **Error Message:** You are trying to unlock the 11.1.0.21 setup with a 10.3.0.1 unlock key. Please refer to this article: [http://www.syncfusion.com/support/kb/2322](http://www.syncfusion.com/support/kb/2322).

**Instructions for Correct Implementation:**
If you receive the wrong key information:
1. Provide the specified version and platform key.
2. Log into your support account in Direct-Trac.
3. Navigate to the **Product Downloads and Keys** page from the Direct-Trac customer dashboard.
4. Select the correct version **x.x.x.x** from the **Get Your Key Here** drop-down box to obtain the correct key.

---

### 4.7 How to Implement Localization Support

**Overview:**
- Syncfusion Essential Studio products allow customizing applications for specific languages and cultures of a particular country or region.

**Implementation Steps:**
- Ensure that your Syncfusion WPF application can support localization.

#### 4.7.1 WPF

**Description:**
- Provide details on how to set up localization for WPF applications using Syncfusion controls and APIs.

**Steps:**
- **Setup:** Configure the localization resource files and the language settings in your application.
- **Usage:** Apply localization to Syncfusion controls by specifying the appropriate resource culture.
- **Testing:** Validate the localized application to ensure all controls and text are displayed correctly in the selected language.

**Example Code:**
```csharp
// Example of setting up the default language
System.Threading.Thread.CurrentThread.CurrentUICulture = new System.Globalization.CultureInfo("en-US");
```

**Note:** Ensure that the resource files are correctly named and placed in the appropriate directory for each supported language.

---

### RAG Annotations
<!-- tags: [syncfusion, winforms, localization, license key, wrong version, direct-trac, 11.1.0.21, 10.3.0.1, download, key] keywords: [user registration, unlock key, version mismatch, localization support, wpf, resource files, language settings, culture, i18n, l10n] -->
```

---

<!-- 페이지 144 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_140.jpeg
document_name: common
page_number: 140
page_id: common#page_140
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:19Z
fidelity: lossless
-->

## Essential Common

### Overview
- Add Resources for different cultures.
- Add supported cultures.
- Assign a Current UI Culture to the application.

### Content

#### Add Resources
To localize Syncfusion Silverlight controls, you need to create resource files for each culture.

The following steps illustrate this:
1. Add Resource (.resx) files in the Resources folder for different cultures. (Here, .resx files in a different culture or invariant culture should be placed in the **Resources** folder of your project.)
2. Resource files should be named as `AssemblyName.CultureName.resx` and `AssemblyName.resx` for the invariant culture.

**Where**
- **AssemblyName**: Syncfusion Silverlight Control Assembly Name.
- **CultureName**: Culture Code of the resource that you want to show in the UI.

If your conversion is only for the invariant culture, the .resx file does not need to contain a culture suffix.

**Example:**
- `Syncfusion.Ribbon.Silverlight.fr-FR.resx` – French resource for `Syncfusion.Ribbon.Silverlight` assembly.
- `Syncfusion.Ribbon.Silverlight.resx` – Invariant Culture resource for `Syncfusion.Ribbon.Silverlight` assembly.

#### Add Supported Cultures
It is very important to add supported cultures in the sample application project before you run the application.

Follow the steps below to localize strings for your culture:
1. In the **Solution Explorer**, right-click your sample application project and choose **Unload Project**. The project will be unavailable.
2. Right-click the project again, and select the **Edit SampleProjectName.csproj** option.
3. In the `.csproj` file, find the `<SupportedCultures></SupportedCultures>` tags. By default, the tags will be empty. So, add the cultures that you want to be supported, separating each with a semicolon.

**Example:** `<SupportedCultures>fr-FR</SupportedCultures>`

4. Save the project and reload it by right-clicking the **SampleProjectName.csproj** and choosing **Reload SampleProjectName.csproj**.

#### Assign Current UI Culture to the Application
By default, the Current Culture will be `en-US`. You can change the CurrentUICulture. Here, CurrentUICulture should be set before the **InitializeComponent** in your **Startup** page (here, **MainPage.xaml.cs**) or you can do it in **App.xaml.cs** in the **Application_Startup** event.
```

---

<!-- 페이지 145 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_144.jpeg
document_name: common
page_number: 144
page_id: common#page_144
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:34Z
fidelity: lossless
-->

## Essential Common

### Index

- **How to uninstall the Syncfusion Setup manually**: 130
- **How to upgrade the project into a new Syncfusion version**: 132

### A

- **Assembly Manager**: 77

### B

- **Build Manager**: 83

### C

- **CAB Add-on**: 61
- **Class Reference**: 34
- **Command Line**: 12, 19, 96
- **Command line installation**: 12, 19
- **Command Line Uninstall Options**: 13, 20

### D

- **Dashboard**: 70
- **Digitally Signed Assemblies Setup**: 44
- **Documentation setup**: 32

### E

- **Essential Studio 4**
- **Essential Studio Enterprise Installer**: 6
- **Essential Studio Installer for Individual Platforms**: 14

### F

- **Frequently Asked Questions**: 120

### H

- **How to Configure the Toolbox of Visual Studio Manually**: 120
- **How to implement Localization Support**: 136
- **How to overcome Sample Browser Access Denied Error for a Non-Admin User**: 129
- **How to redistribute an application on the client machine**: 143
- **How to remove the licensing error that pops up each time the application is run**: 122

### I

- **Installing a Patch Setup**: 53

### L

- **License Manager**: 87
- **Link Install Setup**: 36

### M

- **Manually Configuring VS Toolbox**: 120
- **Metro Studio**: 108
- **Minimum software requirements**: 5
- **Multi-Target Manager**: 93

### O

- **Offline Samples**: 62
- **Online Samples**: 69
- **Orubase Studio**: 98

### Overview

- Overview: 6, 14, 21, 98, 108

### P

- **Patches**: 53
- **Project Migration**: 95
- **Project Templates**: 97

### Q

- **QTP Add-on**: 60

### R

- **Reverting a Patch**: 58

### S

- **Samples**: 61
- **Silverlight**: 139
- **Source code**: 21
- **Step-by-Step Installation**: 6, 21, 98, 108

### T

- **Terminology**: 4

### Toolbox

- **Toolbox Configuration**: 91
```

<!-- tags: [Syncfusion Winforms, Installation, Configuration, Licensing, Version Upgrade, Dashboard, Documentation Setup, Offline Samples, Online Samples, Patch Management, Multi-Targeting, Toolbox Configuration, Sanjus Frameworks, Version 11.4.0.26] keywords: [Syncfusion Setup, Assembly Manager, Build Manager, CAB Add-on, Class Reference, Command Line, Dashboard, Digitally Signed Assemblies Setup, Documentation setup, Essential Studio, Enterprise Installer, Individual Platforms, FAQ, Localization Support, Sample Browser Access, Redistribute App, Remove Licensing Error, Patches, Project Migration, Project Templates, Reverting Patch, Samples, Migration, Templates, Synchfusion, Source code, Step-by-Step Installation, Terminology, Toolbox, ToolBox Configuration, Overview, Studio Dashboard, Doc Setup, Offline Online Samples, Patch Management, Multi Targeting] -->
```