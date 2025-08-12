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