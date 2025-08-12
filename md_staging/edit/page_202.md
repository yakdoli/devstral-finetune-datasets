```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_202.jpeg
document_name: edit
page_number: 202
page_id: edit#page_202
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:27Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Explains how to autoresize the Edit Control by setting the AutoSize property to True.
- Describes the MinimumSize property, which defines the minimum size of the control in autosize mode.
- Introduces split views in the Edit Control, including horizontal and vertical splitters.

## Content

The Edit Control can be autoresized by setting the AutoSize property to True.

```csharp
this.editControl.AutoSize = true;
```

```vbnet
Me.editControl.AutoSize = True
```

### Minimum Size

The MinimumSize property gets / sets the minimum size of the control in autosize mode.

```csharp
this.editControl.MinimumSize = new System.Drawing.Size(10, 10);
```

```vbnet
Me.editControl.MinimumSize = New System.Drawing.Size(10, 10)
```

### 4.9.1.2 Split Views

Edit Control provides in-built support for horizontal and vertical splitters, which facilitates the splitting of a single document in the Edit Control into several split views so that you can work with multiple different areas of a document at the same time. A maximum of four split views are supported. However, you can also limit the user to perform either a horizontal or vertical split, only if you wish to support two views instead of four.

The vertical and horizontal splitters are always visible, by default. They can be disabled by setting the below given properties to False.

| Edit Control Property          | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| ShowHorizontalSplitters       | Gets / sets value that indicates whether horizontal splitters are visible. |
| ShowVerticalSplitters         | Gets / sets value that indicates whether vertical splitters are visible.   |

## API Reference

### WinForms-specific conventions

- Namespaces: `System.Drawing`, `System.Windows.Forms`
- Properties: `AutoSize`, `MinimumSize`, `ShowHorizontalSplitters`, `ShowVerticalSplitters`

## Code Examples

- **Example 1: Setting AutoSize property**
  ```csharp
  this.editControl.AutoSize = true;
  ```
  ```vbnet
  Me.editControl.AutoSize = True
  ```

- **Example 2: Setting MinimumSize property**
  ```csharp
  this.editControl.MinimumSize = new System.Drawing.Size(10, 10);
  ```
  ```vbnet
  Me.editControl.MinimumSize = New System.Drawing.Size(10, 10)
  ```

```html
<!-- tags: [edit control, autosize, minimum size, split views, windows forms, syncfusion windows forms, control splitter] keywords: [autosize, minimum size, horizontal splitter, vertical splitter, multi-view, dynamic sizing] -->
```