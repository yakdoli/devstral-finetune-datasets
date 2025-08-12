```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_082.jpeg
document_name: edit
page_number: 082
page_id: edit#page_082
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:59:08Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Focuses on editing controls and their properties in Windows Forms.
- Detailed explanation of how to configure and customize line numbers in the Edit Control.
- Support for both C# and VB.NET code examples.

## Content

### Edit Control Properties and Descriptions

| Edit Control Property         | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| ShowLineNumbers              | Gets / sets value indicating whether line numbers should be shown.        |
| PhysicalLineCount            | Gets the count of lines in the files.                                   |

### Sample Code: Assigning and Getting Line Numbers

#### C#

```csharp
// Assigning Line Numbers to the contents of the Edit Control.
this.editControl1.ShowLineNumbers = true;

// Gets the number of lines in the Edit Control.
int actualLineCount = this.editControl1.PhysicalLineCount;
```

#### VB.NET

```vb
' Assigning Line Numbers to the contents of the Edit Control.
Me.editControl1.ShowLineNumbers = True

' Gets the number of lines in the Edit Control.
Dim actualLineCount As Integer = Me.editControl1.PhysicalLineCount
```

### Customizing Line Numbers

Line numbers can be customized by using the below given Edit Control properties.

| Edit Control Property         | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| LineNumbersAlignment         | Specifies the alignment of line numbers. The options provided are<br><br>`Left`<br>`Right` |
| LineNumbersColor             | Specifies the color of line numbers.                                                             |
| LineNumbersFont              | Specifies the font of line numbers.                                                             |
| SelectOnLineNumberClick      | Gets / sets value indicating whether click on line numbers performs selection.                  |

#### Sample Code: Customizing Line Numbers (C#)

```csharp
```

## API Reference
- **Syncfusion.Windows.Forms.EditControl**
  - `ShowLineNumbers`: Boolean property to enable or disable line numbers.
  - `PhysicalLineCount`: Int32 property to get the number of lines in the Edit Control.
  - `LineNumbersAlignment`: Specifies alignment options (`Left`, `Right`).
  - `LineNumbersColor`: Color property for line numbers.
  - `LineNumbersFont`: Font property for line numbers.
  - `SelectOnLineNumberClick`: Boolean property to enable line number selections.

### Parameters
- **LineNumbersAlignment**:
  - **Options**:
    - `Left`
    - `Right`

<!-- tags: [syncfusion, winforms, editcontrol, Runtime, DesignTime, LineNumbers] keywords: [line numbers, alignment, color, font, selection, physical line count, edit control] -->
```