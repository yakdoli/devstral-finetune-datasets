```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_088.jpeg
document_name: tools
page_number: 088
page_id: tools#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:20:00Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The `ResetFont()` method can reset the `Font` property to its default value.
- Details on `CommandBar` size properties and their settings.
- Instructions for adjusting the size of the `CommandBar` using its properties during design time.

## Content

### 3.3.3.6.3 Length and Height Settings

The properties that define the dimensions for the `CommandBar` are given below. During design time, the control's size can be changed by editing these property values.

| CommandBar Property | Description |
|---------------------|-------------|
| MaxLength           | Gets / sets the maximum linear dimension of the `CommandBar`. |
| MinLength           | Gets / sets the minimum linear dimension of the `CommandBar`. |
| OccupyFullRow       | Indicates whether the `CommandBar` should occupy the entire row when docked. |
| MinHeight           | Gets / sets the ideal lateral dimension of the `CommandBar`. |
| IntegralHeight      | Gets / sets the incremental step by which the `CommandBar`'s lateral dimension increases when wrapped. |

#### Code Examples

##### C#

```csharp
this.commandBar1.MaxLength = 201;
this.commandBar1.MinLength = 51;
this.commandBar1.OccupyFullRow = true;
this.commandBar1.MinHeight = 27;
this.commandBar1.IntegralHeight = 2;
```

##### VB.NET

```vb
Me.commandBar1.MaxLength = 201
Me.commandBar1.MinLength = 51
Me.commandBar1.OccupyFullRow = True
Me.commandBar1.MinHeight = 27
Me.commandBar1.IntegralHeight = 2
```

<!-- tags: [CommandBar, SizeSettings, DesignTime, ControlProperties] keywords: [Syncfusion, WinForms, CommandBar, MaxLength, MinLength, OccupyFullRow, MinHeight, IntegralHeight] -->
```