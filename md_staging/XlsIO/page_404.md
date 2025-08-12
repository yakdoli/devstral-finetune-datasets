```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_404.jpeg
document_name: XlsIO
page_number: 404
page_id: XlsIO#page_404
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:22Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- XlsIO allows scrolling to the first row in the bottom pane and first column in the right pane with freeze panes.
- Split Panes feature enables viewing multiple copies of the worksheet and scrolling independently in each pane.
- HorizontalSplit and VerticalSplit properties are provided for splitting the window.

## Content

### Freeze Pane Navigation

**Figure 148: XlsIO with Freeze Pane**

XlsIO also allows you to scroll to the first row in the bottom pane and first column in the right pane. It helps you to navigate to the top row while opening a spreadsheet with a large number of rows/columns. Note that this works only with the sheet that has the freeze panes.

#### Code Example: Setting Visible Panes

##### C#

```csharp
// Sets first visible row in the bottom pane.
sheet.FirstVisibleRow = 2;

// Sets first visible column in the right pane.
sheet.FirstVisibleColumn = 2;
```

##### VB.NET

```vbnet
' Sets first visible row in the bottom pane.
sheet.FirstVisibleRow = 2

' Sets first visible column in the right pane.
sheet.FirstVisibleColumn = 2
```

**Note:** FirstVisibleColumn and FirstVisibleRow indexes are "zero-based".

### Split Pane

#### Subsection: 4.7.1.2 Split Pane

A very handy feature of Excel is its ability to view more than one copy of your worksheet, and scroll through each pane of your worksheet independently. You can do this by using a feature called Split Panes, which can be used to split your worksheet both horizontally and vertically. This is enabled in MS Excel by selecting the Split option from the Window menu.

While using Split Panes, the panes of your worksheet work simultaneously. If you make a change in one, it will simultaneously appear in the other.

XlsIO provides support for splitting the window through the HorizontalSplit and VerticalSplit properties. Following code example illustrates this.

### Code Example: Splitting the Window

**C#**

```csharp
// Code to be added here for HorizontalSplit and VerticalSplit properties
```

## Page-level Navigation/TOC (if applicable)

### See also:
- [Split Panes in Excel]
- [HorizontalSplit and VerticalSplit properties]

<!-- tags: [XlsIO, freeze pane, split pane, HorizontalSplit, VerticalSplit, Syncfusion Winforms] keywords: [scrolling, worksheet, panes, navigation, split, pane, independent scrolling, simultaneous changes, zero-based indexes] -->
```