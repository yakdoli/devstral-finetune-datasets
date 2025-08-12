```html
<!--  
source: image  
domain: syncfusion-sdk  
task: pdf-ocr-to-markdown  
language: en (keep original; do not translate)  
source_filename: page_288.jpeg  
document_name: XlsIO  
page_number: 288  
page_id: XlsIO#page_288  
product: Syncfusion Winforms  
version: 11.4.0.26  
timestamp: 2025-08-09T11:08:48Z  
fidelity: lossless  
-->  

# Essential XlsIO  

## Overview  

- The document describes the usage of `Essential XlsIO` for creating and managing Form Controls in Excel workbooks.  
- It details support for Text Box, Check Box, and Combo Box controls.  
- Explains how `Essential XlsIO` enhances form appearance and user friendliness without requiring Microsoft Excel.  

## Content  

### 4.2.8 Form Controls  

Essential XlsIO provides support to read and write the Text Box, Check Box, and Combo Box controls. It enables creating forms that are highly user-friendly and enhances the appearance of the forms.  

**Note:** Essential XlsIO provides support to read and write Form controls. Support for Active X Form controls is not yet available.  

This section explains the usage of the following Form controls:  

#### 4.2.8.1 Text Box  

Essential XlsIO can now read and write text boxes. The `ITextBoxShape` interface lets you add a new text box inside a worksheet. The `IFill` interface is used to customize the inner appearance of the textbox. The `IShapeLineFormat` interface is used to modify the border. Various other properties like Horizontal and Vertical Alignment, Alternative Text, Text Rotation, and so on, are also supported.  

#### Code Examples  

##### [C#]  

```csharp
// Creates a new Text Box.  
ITextBoxShape textbox = sheet.TextBoxes.AddTextBox(3, 7, 25, 100);  
textbox.Text = "Essential XlsIO";  

// Reads a Text Box.  
ITextBoxShape shape1 = sheet.TextBoxes[0];  
shape1.Name = "First TextBox";  
shape1.Fill.ForeColor = Color.Gold;  
shape1.Fill.BackColor = Color.Black;  
shape1.Fill.Pattern = ExcelGradientPattern.Pat_90_Percent;  
```  

##### [VB.NET]  

```vbnet

```  

## API Reference  

### ITextBoxShape  

- **Functions:**  
  - `AddTextBox`  
  - `ReadTextBox`  

### IFill  

- Properties:  
  - `ForeColor`  
  - `BackColor`  
  - `Pattern`  

## Code Examples  

See the examples provided under the [C#] and [VB.NET] sections above.  

## Page-level Navigation/TOC  

- Form Controls  
  - Text Box  
    - Creating a Text Box  
    - Reading a Text Box  

## Cross References  

- Related sections: Business Intelligence\Power Chart  

## RAG Annotations  

<!-- tags: [Essential XlsIO, Form Controls, Text Box, Check Box, Combo Box, ITextBoxShape, IFill, IShapeLineFormat, C#, VB.NET, Microsoft Excel]  
keywords: [Essential XlsIO, Form Controls, Text Box, Check Box, Combo Box, ITextBoxShape, IFill, IShapeLineFormat, C#, VB.NET, Microsoft Excel] -->
```