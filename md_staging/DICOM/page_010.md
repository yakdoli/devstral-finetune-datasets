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