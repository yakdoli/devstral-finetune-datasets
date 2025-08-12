```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_121.jpeg
document_name: edit
page_number: 121
page_id: edit#page_121
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:33Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Demonstrates how to save files with specific encoding styles.
- Explains using the Edit Control to manage and set text encoding styles.
- Lists support for various encoding styles from the `System.Text.Encoding` enumerator.

## Content

### Saving Files with Encoding
Using the `SaveFile` method allows you to specify the encoding and newline style when saving a file.

- **C#[C#]**  
  ```csharp
  this.editControl1.SaveFile("EditControl", Encoding.Unicode, Syncfusion.IO.NewLineStyle.Mac);
  ```

- **VB.NET**  
  ```vb
  Me.editControl1.SaveFile("EditControl", Encoding.Unicode, Syncfusion.IO.NewLineStyle.Mac)
  ```

### Encoding Support
The Edit Control supports all encoding styles from the `System.Text.Encoding` enumerator.

#### Methods for Encoding Style Management
The following methods can be used to get or set the encoding style for text in the Edit Control.

| Edit Control Method | Description |
|----------------------|-------------|
| GetEncoding          | Gets the current text encoding. |
| SetEncoding          | Sets the current text encoding. The options provided are: <br> • ASCII <br> • BigEndianUnicode <br> • Default <br> • UTF32 <br> • UTF7 <br> • UTF8 <br> • Unicode |

### Example Usage

#### Getting and Setting Encoding

- **C#[C#]**  
  ```csharp
  // Gets the current text encoding.
  this.editControl1.GetEncoding();

  // Sets the current text encoding.
  this.editControl1.SetEncoding(Encoding.ASCII);
  ```

- **VB.NET**  
  ```vb
  ' Gets the current text encoding.
  Me.editControl1.GetEncoding()

  // Sets the current text encoding.
  Me.editControl1.SetEncoding(Encoding.ASCII)
  ```

### Summary
The Edit Control in Syncfusion Winforms provides comprehensive support for managing text encodings, enabling developers to easily save files with specific encodings and handle multilingual text effectively.

## Page-level Navigation/TOC
- [Save Files with Encoding](#saving-files-with-encoding)
- [Encoding Support](#encoding-support)
- [Example Usage](#example-usage)

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Edit Control, Encoding, File Save, Text Style Management] keywords: [Syncfusion, Edit Control, Encoding, Encoding Styles, SaveFile, GetEncoding, SetEncoding, System.Text.Encoding] -->
```