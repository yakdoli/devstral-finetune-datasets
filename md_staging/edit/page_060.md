```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: edit
page_number: 060
page_id: edit#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:57:38Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

| Property                       | Description                                                 |
|---------------------------------|-------------------------------------------------------------|
| CurrentLine                     | Gets / sets the current line.                               |
| CurrentLineInstance            | Gets instance of the current line.                          |
| CurrentLineText                 | Gets text of the current line.                              |
| CurrentPosition                 | Gets / sets current position of the cursor in virtual coordinates. |
| PhysicalLineCount               | Gets the count of the lines in the file.                   |

You can use the GoTo method to navigate to any desired position in a file.

| Edit Control Method            | Description                                                                                   |
|---------------------------------|-----------------------------------------------------------------------------------------------|
| GoTo                           | Navigates to the specified position in the opened file.                                     |

## Code Examples

### C#

```csharp
// Gets or sets the current column of the cursor.
this.editControl1.CurrentColumn = 10;

// Gets or sets the current line of the cursor.
this.editControl1.CurrentLine = 7;

// Gets or sets current cursor position.
this.editControl1.CurrentPosition = new Point(10, 2);

this.editControl1.GoTo(7);
```

### VB.NET

```vbnet
' Gets or sets the current column of the cursor.
Me.editControl1.CurrentColumn = 10

' Gets or sets the current line of the cursor.
Me.editControl1.CurrentLine = 7

' Gets or sets current cursor position.
Me.editControl1.CurrentPosition = New Point (10, 2)

Me.editControl1.GoTo(7)
```

<!-- tags: [product, module, control, api, version?] keywords: [Windows Forms, Syncfusion, Edit Control, CurrentLine, CurrentLineInstance, CurrentLineText, CurrentPosition, PhysicalLineCount, GoTo, Navigation, Virtual Coordinates, C#, VB.NET] -->
```