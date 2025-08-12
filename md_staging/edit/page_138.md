```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_138.jpeg
document_name: edit
page_number: 138
page_id: edit#page_138
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:30Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Explains tab and outlining functionalities in the Edit Control.
- Provides keyboard shortcuts for managing tabs, outlining, and whitespace visibility.
- Describes how to generate a bitmap image of the Edit Control for use in applications.

## Content

### Tab

| Action                    | Key Combination                  |
|---------------------------|-----------------------------------|
| Add leading tab          | TAB with multiple line selection |
| Remove leading tab       | SHIFT+TAB                        |

### Outlining

| Action                        | Key Combination                |
|-------------------------------|---------------------------------|
| Switch on outlining and collapse all | CTRL+M->CTRL+O          |
| Switch off outlining          | CTRL+M->CTRL+P                |
| Toggle outlining              | CTRL+M->CTRL+M                |

### WhiteSpace

| Action            | Key Combination                |
|-------------------|---------------------------------|
| Show white space | CTRL+SHIFT+W                  |

### IntelliSens

| Action               | Key Combination               |
|----------------------|-------------------------------|
| Show context prompt  | CTRL+SHIFT+SPACEBAR          |
| Show context choice  | CTRL+SPACEBAR                |

### 4.6.3 Bitmap Generation

The Edit Control has the ability to generate a bitmap image of itself. The bitmap image looks exactly like an actual snapshot of a live instance of Edit Control. This is achieved through the use of the CreateBitmap method.

#### Code Examples

- **C#**
  ```csharp
  // Creates bitmap of the Edit Control.
  Bitmap bmp = this.editControl1.CreateBitmap();
  ```

- **VB.NET**
  ```vb
  ' Creates bitmap of the Edit Control.
  Dim bmp As Bitmap = Me.editControl1.CreateBitmap()
  ```

## API Reference

### Methods

- `CreateBitmap()`: Creates a bitmap image of the Edit Control.

## Code Examples (Multi-Language)

### C#

```csharp
// Creates bitmap of the Edit Control.
Bitmap bmp = this.editControl1.CreateBitmap();
```

### VB.NET

```vb
' Creates bitmap of the Edit Control.
Dim bmp As Bitmap = Me.editControl1.CreateBitmap()
```

<!-- tags: [Syncfusion Winforms, Edit Control, Bitmap Generation, IntelliSense, WhiteSpace, Outlining, Tab Features, Version 11.4.0.26] 
keywords: [Edit Control, bitmap image, CreateBitmap, IntelliSense, whitespace visibility, outlining, tab functionalities, C#, VB.NET, Code Examples] -->
```