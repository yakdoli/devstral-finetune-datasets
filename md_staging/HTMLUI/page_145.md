```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_145.jpeg
document_name: HTMLUI
page_number: 145
page_id: HTMLUI#page_145
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:11:27Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- This section provides an overview of the HTMLUI control in Syncfusion Windows Forms, focusing on its capabilities such as text selection, search, and options for handling large documents.
- Describes the use of the HTMLUI control for flexible layouting and handling various application requirements through HTML-based interfaces.

## Content

### Figure 51: HTMLUISearching Sample

#### Image Description:
The image shows a user interface with the following components:
- **TextSelection** area displaying HTML text content.
- **Refresh** button to update the displayed content.
- **SelectedElements** list box showing selected items like `span sentence3`, `span sentence4`, and `span sentence5`.
- **Text Options** section with buttons for `Search Text (Ctrl+F)` and `Copy Text (Ctrl+C)`.
- The highlighted text in the sample explains the functionality of flexible layout using곳슬 unique Flex-Layout mechanism.

### 4.21 Scrolling

#### Description
The Scroll property of the HTMLUI control assists in handling large HTML documents by ensuring the specified element is visible. The scroll property can be configured based on application needs, and the control supports programmatic scrolling through its scroll properties.

#### Code Examples

##### C#
```csharp
// Scroll controls in such way that the specified element is visible
IHTMLElement elem = this.htmluiControl1.Document.GetElementByUserId("pre");
this.htmluiControl1.ScrollToElement(elem);
```

##### VB.NET
```vb
' Scroll controls in such way that the specified element is visible
Private elem As IHTMLElement = Me.htmluiControl1.Document.GetElementByUserId("pre")
Me.htmluiControl1.ScrollToElement(elem)
```

## API Reference (if applicable)
This section lists the key API elements involved in the scrolling feature:
- **Properties**
  - Scroll: Controls the scrolling behavior for large HTML documents.
- **Methods**
  - ScrollToElement(IHTMLElement elem): Programmatic scrolling to a specific element.

## Code Examples (multi-language supported)
The provided C# and VB.NET examples demonstrate how to programmatically scroll to a specific element in an HTML document using the HTMLUI control.

## RAG Annotations
<!-- tags: [Essential HTMLUI, Syncfusion Winforms, Scrolling, Flex-Layout, Large Documents, Programmatic Scrolling, IHTMLElement] keywords: [HTMLRendering, LayoutEngine, ScrollProperty, ScrollToElement, .NETWindowsForms, LocalizedApplications, ThemedApplications, NetworkUpdates, InterfaceCustomization] -->
```