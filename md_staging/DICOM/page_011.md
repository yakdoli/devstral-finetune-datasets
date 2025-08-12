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