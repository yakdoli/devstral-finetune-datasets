```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: edit
page_number: 050
page_id: edit#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:57:00Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- The page explains the Right-To-Left (RTL) support in the `Edit` control.
- It demonstrates the layout for Arabic text and provides properties and API examples for enabling RTL functionality.

### Figure 11: Right-To-Left Layout of Arabic

The screenshot shows the `EditControl` with Arabic text rendered from right to left. The text is displayed within an `EditControl` control, indicating full support for bi-directional text.

## Properties

### Table 1: Property Table

| Property          | Description                                         | Type      | Data Type | Reference links |
|-------------------|-----------------------------------------------------|-----------|-----------|-----------------|
| RenderRightToLeft | Gets or sets a value indicating whether to render the content of the control in RightToLeft layout. | Boolean   | Boolean   |                 |

### Enabling Right-To-Left in EditControl

RTL can be enabled in `EditControl` with the Application Programming Interface (API) `RenderRightToLeft` as given in the following codes:

#### C#

```csharp
this.editControl1.RenderRightToLeft = true;
```

#### VB.NET

```vb
Me.editControl1.RenderRightToLeft = True
```

### Sample Link

## API Reference

- `RenderRightToLeft`
  - **Type:** `Boolean`
  - **Description:** Gets or sets a value indicating whether to render the content of the control in RightToLeft layout.
  - **Data Type:** `Boolean`
  - **Default:** `false`
  - **Required:** No

## Code Examples

### Python Example

```python
# This is a placeholder for a Python example if applicable.
# As of now, the SDK does not provide specific examples in Python.
# Please refer to the official documentation for supported examples.
```

### See also:
- [RTL Support in Syncfusion Winforms Documentation](https://documentation.syncfusion.com/windowsforms/)

## Page-level Navigation/TOC
- [RTL Support](#rtl-support)
  - [Properties](#properties)
  - [Enabling Right-To-Left](#enabling-right-to-left-in-editcontrol)
  - [Sample Link](#sample-link)
  - [API Reference](#api-reference)
  - [Code Examples](#code-examples)

### Figure: Right-To-Left Layout of Arabic

The figure demonstrates how the `EditControl` can display Arabic text in a right-to-left direction.

## Tags and Keywords
<!-- tags: [WinForms, RightToLeft, EditControl, RTL, Arabic, bi-directional text, properties, API, version] keywords: [Syncfusion WinForms, RightToLeft, EditControl, RTL, Arabic, bi-directional text, properties, API] -->
```