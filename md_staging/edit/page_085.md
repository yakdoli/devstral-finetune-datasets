```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_085.jpeg
document_name: edit
page_number: 085
page_id: edit#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:59:29Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- 1. Explains how to display bookmarks using the Edit Control.
- 2. Describes enabling the indicator margin for displaying custom indicators or bookmarks.
- 3. Details customizing bookmarks and toggling their visibility.

## Content

### Displaying Bookmarks

#### Overview
The Edit Control provides an indicator margin for displaying custom indicators or bookmarks. This feature can be enabled using the `ShowIndicatorMargin` property. The following table explains the key properties related to this functionality:

| Edit Control Property        | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| `ShowIndicatorMargin`       | Gets/sets the value indicating whether bookmarks and indicator margins should be visible. |
| `MarkerAreaWidth`           | Gets/sets the width of the marker area.                                   |

#### Code Examples

##### C#
```csharp
// Displays the Indicator margin.
this.editControl1.ShowIndicatorMargin = true;

// Sets the width of the Indicator margin.
this.editControl1.MarkerAreaWidth = 20;
```

##### VB.NET
```vb
' Displays the Indicator margin.
Me.editControl1.ShowIndicatorMargin = True

' Sets the width of the Indicator margin.
Me.editControl1.MarkerAreaWidth = 20
```

### Customizing Bookmarks

#### Overview
You can either display the default bookmark image (like in Visual Studio.NET) or display custom images as indicators. This can be done via the methods of the Edit Control. The following table outlines a key method for customizing bookmarks:

| Edit Control Method       | Description                          |
|--------------------------|--------------------------------------|
| `BookmarkToggle`         | Sets a bookmark to the current line. |

#### Note
At any given point of time, each line can have only one indicator or bookmark associated with it.

#### Customization Details
You can either use the default bookmark image or customize it with your own images. This is achieved by using the relevant methods available in the Edit Control, such as `BookmarkToggle`.

---

## API Reference (if applicable)

### Methods
- **`BookmarkToggle`**
  - **Description**: Sets a bookmark to the current line.
  - **Parameters**: None.
  - **Returns**: None.
  - **Exceptions**: None explicitly mentioned.

### Properties
- **`ShowIndicatorMargin`**
  - **Type**: `bool`
  - **Description**: Indicates whether bookmarks and indicator margins should be visible.
  - **Default**: `false`
  - **Required**: No

- **`MarkerAreaWidth`**
  - **Type**: `int`
  - **Description**: Specifies the width of the marker area.
  - **Default**: `0`
  - **Required**: No

---

## Code Examples (Multi-Language Supported)

##### C#
```csharp
// Enabling indicator margin and setting its width.
this.editControl1.ShowIndicatorMargin = true;
this.editControl1.MarkerAreaWidth = 20;

// Toggling a bookmark on the current line.
this.editControl1.BookmarkToggle();
```

##### VB.NET
```vb
' Enabling indicator margin and setting its width.
Me.editControl1.ShowIndicatorMargin = True
Me.editControl1.MarkerAreaWidth = 20

' Toggling a bookmark on the current line.
Me.editControl1.BookmarkToggle()
```

---

## Page-level Navigation/TOC (if applicable)

### Local TOC
- [Displaying Bookmarks](#displaying-bookmarks)
- [Customizing Bookmarks](#customizing-bookmarks)

---

<!-- tags: [edit control, indicator margin, bookmarks, custom indicators, syncfusion winforms] keywords: [edit control, indicator, margins, bookmarks, customization, Toggle, MarkerAreaWidth, ShowIndicatorMargin, Visual Studio.NET] -->
```