---
title: "DICOM - Syncfusion SDK Documentation"
type: "api-documentation"
framework: "syncfusion"
version: "v11"
processing_mode: "Process Isolation (프로세스 격리)"
extracted_date: "1754713698.1044285"
optimized_for: ["llm-training", "rag-retrieval"]
scaling_approach: "3"
---

<!-- 페이지 1 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_001.jpeg
document_name: DICOM
page_number: 001
page_id: DICOM#page_001
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:27:29Z
fidelity: lossless
--> 

# Essential Studio 2013 Volume 4 - v.11.4.0.26  
## Essential DICOM  

### WinForms-specific conventions  
This documentation is focused on the DICOM component of Syncfusion's Essential Studio. It provides information and samples to help users integrate DICOM functionalities into their WinForms applications.  

```csharp
// Example Usage of the DICOM component  
using Syncfusion.Windows.Forms.DICOM;  

DICOM dicom = new DICOM();  
dicom.Load("path_to_dicom_file");  
```

## Overview  
- Description of the DICOM component and its features.  
- Integration details for WinForms applications.  
- Examples demonstrating the usage of DICOM functionalities.  

## Content  
### Introduction to DICOM  
DICOM (Digital Imaging and Communications in Medicine) is a standard for storing and transmitting medical image data. This section explains how Syncfusion's DICOM component facilitates the incorporation of DICOM functionalities into WinForms applications.  

### Features  
- Supports reading and writing DICOM files.  
- Handles various DICOM object types.  
- Provides tools for image manipulation and analysis.  

### Getting Started  
#### Installing the Component  
1. Download and install the latest version of Essential Studio for WinForms.  
2. Add a reference to the Syncfusion.DICOM assembly in your project.  

#### Basic Usage  
1. Create an instance of the DICOM class.  
2. Use methods to load, manipulate, and save DICOM data.  

```csharp
DICOMLoader loader = new DICOMLoader();  
DICOMObject dicomObject = loader.Load("file.dcm");  
```

## API Reference  
### Namespace: Syncfusion.Windows.Forms.DICOM  
#### Class: DICOM  
##### Methods  
- `Load(string filePath)`  
  - Loads a DICOM file from the given file path.  
  - Returns: `DICOMObject`  

- `Save(string filePath, DICOMObject object)`  
  - Saves a DICOM object to the specified file path.  

#### Properties  
- `Data`  
  - Gets or sets the underlying data of the DICOM object.  

- `MetaInfo`  
  - Gets or sets the metadata information of the DICOM object.  

## Code Examples  
#### Simple DICOM File Loading  
```csharp  
using Syncfusion.Windows.Forms.DICOM;  

public class DICOMExample  
{  
    public void LoadDICOMFile()  
    {  
        string filePath = "example.dcm";  
        DICOM dicom = new DICOM();  
        dicom.Load(filePath);  

        // Access DICOM data  
        var data = dicom.Data;  
    }  
}  
```

## Page-level Navigation/TOC (if applicable)  
- [Introduction to DICOM](#introduction-to-dicom)  
- [Features](#features)  
- [Getting Started](#getting-started)  
- [API Reference](#api-reference)  
- [Code Examples](#code-examples)  

## Cross References  
See also:  
- [Syncfusion WinForms Documentation](https://help.syncfusion.com/windowsforms/)  
- [DICOM Standards](https://www.dicomstandard.org/)  

<!-- tags: [Syncfusion, WinForms, DICOM, component, documentation] keywords: [DICOM, WinForms, Essential Studio, v.11.4.0.26, medical imaging, data, API reference, code examples, loading, saving] -->
```

---

<!-- 페이지 2 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_005.jpeg
document_name: DICOM
page_number: 005
page_id: DICOM#page_005
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:27:51Z
fidelity: lossless
-->

# Essential DICOM

## Overview
- Provides guidance on accessing Documentation for Essential DICOM features.
- Includes both online and installed documentation options.

## Content

### Installed Documentation
- **Access Path**: `Dashboard -> Documentation -> Installed Documentation`

### Class Reference

#### Online
- **URL**: [http://help.syncfusion.com/resources](http://help.syncfusion.com/resources)
- **Navigation Instructions**:
  1. Navigate to the Reporting User Guide.
  2. Select `DICOM`.
  3. Click the `Class Reference` link found in the upper right section of the page.

#### Installed Documentation
- **Access Path**: `Dashboard -> Documentation -> Installed Documentation`

## API Reference
- Namespace: `Syncfusion.Essential.DICOM`
- Class: `DICOM`
- Members:
  - Methods
  - Properties
  - Events

## Code Examples
- Example of accessing documentation:
```csharp
// C# example for accessing documentation
Dashboard.GoToDocumentation();
```

## Cross References
- See also:
  - Reporting User Guide
  - DICOM Documentation
  - Class Reference

<!-- tags: [Syncfusion, DICOM, Essential DICOM, Documentation, Class Reference, Winforms, 11.4.0.26] keywords: [DICOM, Documentation, Class Reference, Syncfusion, Winforms] -->
```

---

<!-- 페이지 3 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_009.jpeg
document_name: DICOM
page_number: 009
page_id: DICOM#page_009
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:28:02Z
fidelity: lossless
-->

# Essential DICOM

## Overview
- Demonstrates the process of creating a new WPF application using Visual Studio.
- Guides through integrating Syncfusion.Core and Syncfusion.DICOM.Base libraries into the project.
- Focuses on setting up a WPF application for DICOM-related functionalities.

## Content

### Creating a New WPF Application

The following steps detail the process of creating a new WPF application and integrating the necessary Syncfusion libraries.

1. **Create a New WPF Application**
   - Open Visual Studio and navigate to the "New Project" dialog box.
   - Select "WPF Application" from the list of templates under "Visual C#."
   - Configure the project settings such as the project name, location, and solution name.
   - Ensure the project targets the appropriate .NET Framework version (e.g., 3.5 as shown in the figure).

   **Figure 3: New Project dialog box-WPF Application**
   ![New Project dialog box: WPF Application](New Project dialog box image)

   Upon completion, a new WPF application will be created.

2. **Open the Main Form in the Designer**
   - After creating the WPF application, open the main form of the application in the designer.
   - This will allow you to start designing the user interface for your application.

3. **Add Syncfusion References**
   - Add the required Syncfusion libraries to the project:
     - **Syncfusion.Core**
     - **Syncfusion.DICOM.Base**
   - These references will enable access to Syncfusion's DICOM functionalities within your WPF application.

## API Reference

### Namespaces and Classes
- **Syncfusion.Core**: Provides core functionality for Syncfusion controls and utilities.
- **Syncfusion.DICOM.Base**: Contains base classes and utilities for handling DICOM data.

## Code Examples

### Sample Code for Integrating Syncfusion Libraries

```csharp
// Adding Syncfusion References
using Syncfusion.Core;
using Syncfusion.DICOM.Base;

// Example Usage in Code
public class DICOMApplication
{
    public void InitializeDICOM()
    {
        // Initialize DICOM functionality
        DICOMBase.Initialize();
    }
}
```

## Page-level Navigation/TOC

- Creating a New WPF Application
  - New Project Dialog Box
  - WPF Application Setup
  - Integrating Syncfusion Libraries

## Cross References

- See also: [Syncfusion Core Documentation](https://www.syncfusion.com/documentation/common/uwp/getting-started)
- See also: [Syncfusion DICOM Documentation](https://www.syncfusion.com/documentation/dicom)

<!-- tags: Essential DICOM, WPF, Syncfusion.Core, Syncfusion.DICOM.Base, setup, library integration -->
```

---

<!-- 페이지 4 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_002.jpeg
document_name: DICOM
page_number: 002
page_id: DICOM#page_002
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:27:29Z
fidelity: lossless
-->

# Contents

## Overview

### 1. Overview
- **1.1 Introduction to DICOM** [Page 3]
- **1.2 Use Case Scenario** [Page 3]
- **1.3 Prerequisites and Compatibility** [Page 3]
- **1.4 Documentation** [Page 4]

## Installation and Deployment

### 2. Installation and Deployment
- **2.1 Installation** [Page 6]
- **2.2 Deployment Requirements** [Page 6]

## Getting Started

### 3. Getting Started
- **3.1 Feature Summary** [Page 7]
- **3.2 Adding DICOM to an Application** [Page 7]

## Concepts and Features

### 4. Concepts and Features
- **4.1 DICOM Format** [Page 10]
  - **4.1.1 Properties, Methods, and Events** [Page 10]
    - **4.1.1.1 Properties** [Page 10]
    - **4.1.1.2 Methods** [Page 10]
  - **4.1.2 Adding DICOM to an Application** [Page 11]

## WinForms-specific details
- This page provides an overview of the DICOM library for Syncfusion Winforms. It covers essential topics such as:
  - Understanding the library's use case and prerequisites.
  - The installation and deployment process.
  - Key concepts and features related to DICOM format and integration with Winforms applications.

## Cross References
- References to other relevant pages or sections within the documentation can be found in the **See also:** entries at the end of each section.

<!-- tags: [syncfusion-sdk, dicom, winforms, installation, deployment, concepts, features] keywords: [DICOM, Syncfusion Winforms, overview, features, documentation, properties, methods, events, deployment] -->
```

---

<!-- 페이지 5 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_006.jpeg
document_name: DICOM
page_number: 006
page_id: DICOM#page_006
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:27:42Z
fidelity: lossless
-->

# Essential DICOM

## Installation and Deployment

### 2.1 Installation

For step-by-step installation procedure of Essential Studio, refer to the **Installation** topic under **Installation and Deployment** in the **Common UG**:

- Common UG -> Installation and Deployment -> Installation topic

#### See Also

For licensing, patches, and information on adding or removing selective components, refer to the following topics in **Common UG** under Installation and Deployment:

- Licensing
- Patches
- Add/Remove Components

### 2.2 Deployment Requirements

While deploying an application that references Syncfusion Essential DICOM assembly, the following dependencies must be included in the distribution.

#### DICOM – Windows Forms, WPF

- **Syncfusion.Core.dll**
- **Syncfusion.DICOM.Base.dll**

## Page-level Navigation/TOC (if applicable)

- 2 Installation and Deployment
  - 2.1 Installation
  - 2.2 Deployment Requirements

## Cross References

### Development and Distribution Process

#### Licensing
#### Patches
#### Add/Remove Components

## API Reference (if applicable)

None explicitly listed in this section.

## Code Examples (multi-language supported)

None provided in this section.

## RAG Annotations

<!-- tags: [product, module, control, api, version] keywords: [installation, deployment, licensing, patches, components, dependencies, Syncfusion.Core.dll, Syncfusion.DICOM.Base.dll, Windows Forms, WPF, Common UG, Essential DICOM, Essential Studio] -->
```

---

<!-- 페이지 6 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_010.jpeg
document_name: DICOM
page_number: 010
page_id: DICOM#page_010
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:27:54Z
fidelity: lossless
-->

# 4 Concepts and Features

## 4.1 DICOM Format

### Overview

- Essential DICOM is a 100% native .NET library that converts standard image formats to the DICOM format (.dcm).
- It is a solution for users who need to convert ordinary image formats to the DICOM format.
- Requires a DICOM viewer or an equivalent viewer to view the converted DICOM image.
- Supports the conversion of various image formats: JPEG, BMP, PNG, EMF, TIFF, GIF.

### Supported Image Formats

- JPEG
- BMP
- PNG
- EMF
- TIFF
- GIF

#### 4.1.1 Properties, Methods, and Events

- The following properties and methods are associated with the `DICOMImage` class under the `DICOM Format` section.

##### 4.1.1.1 Properties

The table below lists the properties of the `DICOMImage` class along with their descriptions, types, and data types.

| Property   | Description                               | Type     | Data Type       |
|------------|-------------------------------------------|----------|------------------|
| FileName   | Gets or sets the input image file location | Normal   | String           |
| InputStream| Gets or sets the input image as a Stream.  | Normal   | System.IO.Stream |
| Image      | Gets or sets the input image              | Normal   | System.Drawing   |

### 4.1.1.2 Methods

Further details about the methods will follow in subsequent sections.

## API Reference

The `DICOMImage` class provides properties and methods that facilitate the conversion and handling of DICOM images. The detailed API reference is provided in the table above for properties and will be expanded further with method details in subsequent sections.

## RAG Annotations

<!-- tags: [Essential DICOM, .NET library, DICOM format, DICOMImage class] keywords: [properties, image formats, conversion, DICOM viewer, JPEG, BMP, PNG, EMF, TIFF, GIF] -->
```

---

<!-- 페이지 7 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_003.jpeg
document_name: DICOM
page_number: 003
page_id: DICOM#page_003
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:27:29Z
fidelity: lossless
-->

# Essential DICOM

## 1 Overview

### 1.1 Introduction to DICOM

The Digital Imaging and Communications in Medicine (DICOM) standard was created by the National Electrical Manufacturers Association (NEMA). Its aim is to support the distribution and viewing of medical images from CT, MRI, and other medical modalities. The DICOM format is an extension of the older NEMA standard.

A DICOM file contains a header and the image data. The header stores information about the patient's name, the type of scan, position and dimension of the image, and lots of other data. The image data part contains all the image information. DICOM is the common standard for scans in hospitals.

### 1.2 Use Case Scenario

This feature helps users to convert the standard image formats to the DICOM format for medical communications. It is a standard for handling, storing, printing, and transmitting information in medical imaging.

### 1.3 Prerequisites and Compatibility

This section covers the requirements mandatory for installing Essential DICOM. It also lists operating systems and browsers compatible with the product.

#### Prerequisites

The prerequisites details are listed below:

**Table 1: Prerequisites**

| Development Environments                  |                                                                                                                                                                                                                                                                                   |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Visual Studio 2010 (Ultimate, Premium, Professional and Express)                                                                                                                                                     |
| Visual Studio 2008 (Team System, Professional, Standard & Express)                                                                                                                                                  |
| Visual Studio 2005 (Professional, Standard & Express)                                                                                                                                                                   |
| Silverlight 4.0                                                                                                                                                                                                                  |
| .NET Framework versions                                                                                                                                                 |
| .NET 4.0                                                                                                                                                                                                                          |
| .NET 3.5 SP1                                                                                                                                                                                                                       |
| .NET 2.0                                                                                                                                                                                                                           |

#### Compatibility

## Compliance

© 2013 Syncfusion. All rights reserved. 3 | Page

<!-- tags: [Dicom, Standard, NEMA, Medical Imaging, File Formats] keywords: [DICOM, NEMA, CT, MRI, medical modalities, Visual Studio, .NET Framework, Silverlight, compatibility, prerequisites, installation requirements, medical imaging, communication, handling, storing, printing, transmitting information] -->

---

<!-- 페이지 8 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_007.jpeg
document_name: DICOM
page_number: 007
page_id: DICOM#page_007
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:27:43Z
fidelity: lossless
-->

# Essential DICOM

## Overview

- Essential DICOM is a .NET library that converts standard image formats to the DICOM format.
- It supports JPEG, BMP, PNG, EMF, TIFF, and GIF formats.
- Requires a DICOM Viewer or equivalent to display converted images.
- Demonstrates converting an image to DICOM format and incorporating it into a Windows or WPF application.

## Content

### 3.1 Feature Summary

Essential DICOM is a 100% native .NET library that converts standard image formats to the DICOM format (.dcm). Essential DICOM is a solution for users who need to convert ordinary image formats such as JPEG, BMP, PNG, EMF, TIFF, and GIF to the DICOM format. It requires a DICOM Viewer or an equivalent viewer to view the converted DICOM image.

The following image shows the converted DICOM Image using Essential DICOM.

![Converted DICOM Image](https://i.imgur.com/ExampleDICOMImage.png)
*Figure 1: Converted DICOM Image*

### 3.2 Adding DICOM to an Application

This section illustrates the step-by-step procedure to create the following platform applications:
- Windows
- WPF

#### Windows Application

<!-- tags: [DICOM, image conversion, Windows application, WPF application, .NET library] keywords: [Essential DICOM, DICOM format, image formats, DICOM viewer, Windows, WPF, .NET, Syncfusion Winforms] -->
```html
```

---

<!-- 페이지 9 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_011.jpeg
document_name: DICOM
page_number: 011
page_id: DICOM#page_011
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:27:54Z
fidelity: lossless
-->

# Essential DICOM

## Overview
- Details about saving converted DICOM images to specified files or streams.
- Examples in C# and VB.NET for adding DICOM functionality to an application.

## Content

### Table 5: Methods Table

| Method      | Description                                                                                           | Parameters              | Type    | Return Type |
|-------------|-------------------------------------------------------------------------------------------------------|--------------------------|---------|-------------|
| Save ()     | Saves the converted DICOM Image to the specified file or a Stream.                                    | Save(String)            | Normal  | void        |
|             |                                             | Save(Stream)             |         |             |

### 4.1.2 Adding DICOM to an Application
The following sets of code snippets illustrate the conversion to DICOM Format.

[unclear]

#### C#

```csharp
//Initializing the DICOM Image object.
DICOMImage dcmImage = new DICOMImage((string)this.textBox1.Tag);
//Saving the DICOM image.
dcmImage.Save("Sample.dcm");
```

#### VB.NET

```vb
'Initializing the DICOM Image object.
Dim dcmImage As New DICOMImage(DirectCast(Me.textBox1.Tag, String))
'Saving the DICOM image.
dcmImage.Save("Sample.dcm")
```

## API Reference

### Save()

- **Purpose**: Saves the converted DICOM Image to the specified file or a Stream.
- **Parameters**:
  - `Save(String)`  
  - `Save(Stream)`
- **Type**: Normal  
- **Return Type**: void  

## Code Examples

### C#

```csharp
//Initializing the DICOM Image object.
DICOMImage dcmImage = new DICOMImage((string)this.textBox1.Tag);
//Saving the DICOM image.
dcmImage.Save("Sample.dcm");
```

### VB.NET

```vb
'Initializing the DICOM Image object.
Dim dcmImage As New DICOMImage(DirectCast(Me.textBox1.Tag, String))
'Saving the DICOM image.
dcmImage.Save("Sample.dcm")
```

<!-- tags: [Syncfusion Winforms, DICOM, save, file, stream] keywords: [DICOM, Save, stream, converted image, data conversion, C#, VB.NET, application integration, Save(String), Save(Stream)] -->
```

---

<!-- 페이지 10 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_004.jpeg
document_name: DICOM
page_number: 004
page_id: DICOM#page_004
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:27:29Z
fidelity: lossless
-->

## Compatibility

The compatibility details are listed below:

### Table 2: Compatibility

| Operating Systems               |                                                                 |
|----------------------------------|-----------------------------------------------------------------|
|                                  | - Windows Server 2008 (32 bit and 64 bit)                 |
|                                  | - Windows 7 (32 bit and 64 bit)                           |
|                                  | - Windows Vista (32 bit and 64 bit)                       |
|                                  | - Windows XP                                                |
|                                  | - Windows 2003                                              |

## 1.4 Documentation

Syncfusion provides the following documentation segments to provide all the necessary information pertaining to Essential DICOM.

### Table 3: Documentation

| Type of Documentation            | Location                                                                                                                                                                                                                 |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Readme                          | Windows Forms - `[drive:]`\Program Files\Syncfusion\Essential Studio\<Version Number>\Infrastructure\Data\Release Notes\readme.htm<br> WPF - `[drive:]`\Program Files\Syncfusion\Essential Studio\<Version Number>\Infrastructure\Data\WPF release notes\readme.htm |
| Release Notes                   | Windows Forms - `[drive:]`\Program Files\Syncfusion\Essential Studio\<Version Number>\Infrastructure\Data\Release Notes\Release Notes.htm<br> WPF - `[drive:]`\Program Files\Syncfusion\Essential Studio\<Version Number>\Infrastructure\Data\WPF release notes\Release Notes.htm |
| User Guide (this document)      | Online<br>`http://help.syncfusion.com/resources` (Navigate to the DICOM User Guide.)<br>Note: Click Download as PDF to access a PDF version. |

<!-- tags: [Syncfusion, Essential DICOM, Windows Forms, WPF, User Guide, Release Notes, Readme, Documentation, Version, 11.4.0.26] -->
<!-- keywords: [compatibility, operating systems, Windows Server, Windows 7, Windows Vista, Windows XP, Windows 2003, Syncfusion, Essential DICOM, Syncfusion Winforms, documentation, Release Notes, User Guide, Development, version, 2013, C#] -->
```

---

<!-- 페이지 11 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_008.jpeg
document_name: DICOM
page_number: 008
page_id: DICOM#page_008
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:27:43Z
fidelity: lossless
-->

# Essential DICOM

## Overview

- Guide to creating a Windows Forms Application.
- Steps for adding Syncfusion.Core and Syncfusion.DICOM.Base references.

## Content

### Windows Forms Application

1. **Open Microsoft Visual Studio.**
   - Go to **File** menu and click **New Project**.
   - In the **New Project** dialog box, select **Windows Forms Application** template.
   - Name the project and click **OK**.

   ![Figure 2: New Project dialog box - Windows Forms Application](image.png)

   **Figure 2: New Project dialog box - Windows Forms Application**

   A windows application is created.

2. **Open the main form of the application in the designer.**
3. **Add the** **Syncfusion.Core** **and** **Syncfusion.DICOM.Base** **reference to the project.**

### WPF Application

1. **Open Microsoft Visual Studio.**
   - Go to **File** menu and click **New Project**.
   - In the **New Project** dialog box, select **WPF Application** template.
   - Name the project and click **OK**.

## Page-level Navigation/TOC (if applicable)
- No local TOC present.

## Cross References
- See also:
  - [Syncfusion Winforms Documentation](https://www.syncfusion.com/documentation)
  - [DICOM Standard](https://www.dicomstandard.org)

<!-- tags: [syncfusion winforms, dicom, new project, visual studio, windows forms application, wpf application, syncfusion.core, syncfusion.dicom.base] keywords: [visual studio, windows forms application, new project, wpf application, syncfusion.winforms, dicom, windows application, user interface, .net framework] -->
```

---

<!-- 페이지 12 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_012.jpeg
document_name: DICOM
page_number: 012
page_id: DICOM#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:27:58Z
fidelity: lossless
-->

# Index

## Overview
- A guide to understanding the index structure and key topics related to DICOM within the Syncfusion Winforms user guide.

## Content

### A
- **Adding DICOM to an Application**: 7, 11

### C
- **Concepts and Features**: 10

### D
- **Deployment Requirements**: 6
- **DICOM Format**: 10
- **Documentation**: 4

### F
- **Feature Summary**: 7

### G
- **Getting Started**: 7

### I
- **Installation**: 6
- **Installation and Deployment**: 6
- **Introduction to DICOM**: 3

### M
- **Methods**: 10

### O
- **Overview**: 3

### P
- **Prerequisites and Compatibility**: 3
- **Properties**: 10
- **Properties, Methods, and Events**: 10

### U
- **Use Case Scenario**: 3

<!-- tags: [Syncfusion, Winforms, DICOM, documentation, user guide, reference] keywords: [DICOM, properties, methods, events, documentation, user guide, tutorial, installation, deployment, overview, prerequisites, compatibility] -->
```