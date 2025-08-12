```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_132.jpeg
document_name: HTMLUI
page_number: 132
page_id: HTMLUI#page_132
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:10:39Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Demonstrates setting background color in HTMLUI using the Body Tag's bgColor attribute.
- Includes a sample showcasing HTMLUIBackColor functionality.
- Explains the HTML Format implementation for dynamic formatting in HTMLUI.

## Content

### HTMLUI BackColor Sample

![Figure 43: HTMLUIBackColor Sample](# "Figure 43: HTMLUIBackColor Sample")

**Figure 43: HTMLUIBackColor Sample**

*By default, this sample can be found under the following location:*

```
C:\Documents and Settings\username\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\HTMLUI.Windows\ Samples\2.0\HTMLUI Appearance\HTMLUIBackColor
```

### 4.15 HTML Format

#### Overview of HTML Format

HTMLUI allows the user to apply formats to the elements at run time. The **HTMLFormat** class creates a format for the HTML elements displayed in the HTMLUI control. The user can apply the format on the execution of some events based on the necessity of the application.

#### Implementation

[C#]

```csharp
// Implementation of HTMLFormat interface
Hashtable html = this.htmluiControl1.Document.GetElementsByUserIdHash();
BaseElement div = html["div1"] as BaseElement;

HTMLFormat format = new HTMLFormat("ClickedPara");
```

## API Reference

### HTMLUIBackColor

**Properties:**
- `BackColor` (sets the background color of the HTMLUI control)

### HTMLFormat

**Methods:**
- `ApplyFormat()`: Applies the specified format to the HTML elements.
- `Dispose()`: Disposes of any unmanaged resources used by the format.

**Parameters:**
- `ElementId`: Identifier for the HTML element to which the format is to be applied.
- `FormatName`: Name of the format to be applied.

## Code Examples

#### Example: Applying HTML Format

```csharp
// Get the HTML element by its ID
Hashtable html = this.htmluiControl1.Document.GetElementsByUserIdHash();
BaseElement div = html["div1"] as BaseElement;

// Create a new HTMLFormat object
HTMLFormat format = new HTMLFormat("ClickedPara");

// Apply the format to the element
div.ApplyFormat(format);
```

## Related Topics

- [HTMLUI Basics](#)
- [Styling HTMLUI Elements](#)

<!-- tags: [HTMLUI, BackColor, HTMLFormat, WindowsForms, Syncfusion, EssentialStudio, 11.4.0.26] keywords: [htmlui, background color, formatting, windows forms, document, sample, code] -->
```