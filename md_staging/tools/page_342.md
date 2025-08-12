```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_342.jpeg
document_name: tools
page_number: 342
page_id: tools#page_342
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:07:57Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```text
Dashed,
Dotted,
Inset,
Outline,
Solid,
Bump,
Etched,
Flat,
Raised,
RaisedInner,
RaisedOuter,
Sunken,
SunkenInner and
SunkenOuter.
```

### Note: This setting will be effective only for Office2003, OfficeXP and WindowsXP styles set through ButtonAdv.Appearance property. See `Visual Styles`.

#### [C#]

```csharp
//Sample code for setting "SunkenOuter" Border Style using
//BorderStyleAdv
this.buttonAdv13.BorderStyleAdv =
Syncfusion.Windows.Forms.ButtonAdvBorderStyle.SunkenOuter;
```

#### [VB.NET]

```vb
//Sample code for setting "SunkenOuter" Border Style using
//BorderStyleAdv
Me.buttonAdv13.BorderStyleAdv =
Syncfusion.Windows.Forms.ButtonAdvBorderStyle.SunkenOuter
```

## API Reference

### C# Sample Code

```csharp
using Syncfusion.Windows.Forms;

// Configure ButtonAdv
ButtonAdv button = new ButtonAdv();
button.BorderStyleAdv = Syncfusion.Windows.Forms.ButtonAdvBorderStyle.SunkenOuter;
```

### VB.NET Sample Code

```vb
Imports Syncfusion.Windows.Forms

' Configure ButtonAdv
Dim button As New ButtonAdv()
button.BorderStyleAdv = Syncfusion.Windows.Forms.ButtonAdvBorderStyle.SunkenOuter
```

## RAG Annotations

Syncfusion, WinForms, Office2003, OfficeXP, WindowsXP, ButtonAdv, AppearanceProperty, VisualStyles, BorderStyleAdv, SunkenOuter, Dashed, Dotted, Inset, Outline, Solid, Bump, Etched, Flat, Raised, RaisedInner, RaisedOuter, Sunken, SunkenInner, SunkenOuter

<!-- tags: [WinForms, ButtonAdv, VisualStyles, BorderStyle] keywords: [SunkenOuter, Office2003, OfficeXP, WindowsXP, VisualStyles, BorderStyleAdv] -->
```