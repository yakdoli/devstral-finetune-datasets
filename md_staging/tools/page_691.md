```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_691.jpeg
document_name: tools
page_number: 691
page_id: tools#page_691
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:37Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
This page provides an overview of the visual styles and events associated with the `SplitContainerAdv` control in Windows Forms. It includes examples of different visual styles and the programming interface for handling events.

## Content

### Visual Styles for SplitContainerAdv

The `SplitContainerAdv` control provides various visual styles for customizing the appearance of the split container. The figure below illustrates the different visual styles available:

- **Default Style**
- **Mozilla Style**
- **VS 2005 Style**
- **Office XP Style**
- **Office 2003 Style**
- **Office 2007 Silver Style**
- **Office 2007 Blue Style**
- **Office 2007 Black Style**

**Figure 429: Visual Styles for SplitContainerAdv**

### Events

#### Thumbnail Arrow Settings

The events available for the `SplitContainerAdv` control include:

##### 3.5.6.4.4 Events

The events available for the `SplitContainerAdv` control are as follows:

- **SplitterMoved Event**: This event is triggered when the splitter is moved to a new position.

```csharp
private void splitContainerAdv2_SplitterMoved(object sender, SplitterMoveEventArgs args)
{
    MessageBox.Show("The Splitter has moved from : " +
```

## API Reference (if applicable)
- Namespace: `Syncfusion.Windows.Forms.Tools`
- Class: `SplitContainerAdv`
- Event: `SplitterMoved`

### Code Examples

```csharp
private void splitContainerAdv2_SplitterMoved(object sender, SplitterMoveEventArgs args)
{
    MessageBox.Show("The Splitter has moved from : " + 
}
```

## See Also
- [Thumbnail Arrow Settings](#Thumbnail-Arrow-Settings)

## Page-level Navigation/TOC
- **Visual Styles for SplitContainerAdv**
- **Events**
  - **Thumbnail Arrow Settings**
  - **3.5.6.4.4 Events**

## Cross References
- `SplitContainerAdv`
- `SplitterMoveEventArgs`
- `MessageBox`

## RAG Annotations
<!-- tags: [product, Windows Forms, SplitContainerAdv, events, visual styles, C#] keywords: [SplitContainerAdv, SplitterMoved, events, visual styles, Windows Forms, C#] -->
```