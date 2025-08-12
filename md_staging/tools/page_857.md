```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_857.jpeg
document_name: tools
page_number: 857
page_id: tools#page_857
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:38:21Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses properties and settings for the MaskedTextBox control in WinForms.
- Covers functionality for ReadOnly and Border properties.
- Demonstrates code examples in both C# and VB.NET.

## Content

### MaskedTextBox Property: ReadOnly

#### Description
Specifies whether the text in the edit control can be changed or not.

#### Code Examples

**[C#]**
```csharp
this.maskedTextBox1.ReadOnly = true;
```

**[VB]**
```vb
Me.maskedTextBox1.ReadOnly = True
```

### 3.5.8.8.3.9 Border Settings

#### Overview
The border settings of the MaskedTextBox control are discussed in this section. The wide variety of border options available for the MaskedTextBox control are detailed below.

#### MaskedTextBox Properties: Border3DStyle

Indicates the style of the 3D border. The options included are as follows:

- RaisedOuter
- SunkenOuter
- RaisedInner
- SunkenInner
- Raised
- Etched
- Bump
- Sunken
- Adjust and Flat

The default value is set to 'Sunken'.

## API Reference (if applicable)
- Refer to the official Syncfusion documentation for complete API details on MaskedTextBox properties and methods.

## Code Examples (multi-language supported)
- Provided above for ReadOnly and Border3DStyle properties in both C# and VB.NET.

## Cross References
- Refer to additional sections or documentation for more detailed information on other MaskedTextBox features.
- See also: [related topics or features in the same document]

### RAG Annotations
<!-- tags: [maskedtextbox, readonly, border3dstyle, winforms, controls, api, version:11.4.0.26] keywords: [mask, edit, border, style, 3d, sunken, raised, etched, bump, flat, readonly, property, control, windows forms, .net, c#, vb.net] -->
```