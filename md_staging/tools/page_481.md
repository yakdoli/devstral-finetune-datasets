```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_481.jpeg
document_name: tools
page_number: 481
page_id: tools#page_481
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:15:07Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Figure 277 illustrates the border style for DateTimePickerAdv.
- Provides information on setting images for the popup menu of the Calendar using the MonthImageList property.
- Explains setting images for the popup menu of the Calendar control.

## Content

### Figure 277: Border Style for DateTimePickerAdv

#### See Also
- [Background Settings](Background%20Settings)
- [3.5.3.2.3.5 Runtime Features](3.5.3.2.3.5%20Runtime%20Features)

This section covers the below topics:

#### 3.5.3.2.3.5.1 Month Images

We can set images for the popup menu of the Calendar using the `MonthImageList` property of DateTimePickerAdv control.

```csharp
// imageList1
this.imageList1.ImageSize = new System.Drawing.Size(16, 16);
this.imageList1.ImageStream =
    ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));

// ImageList of the PopupMenu of the Popup Calendar
this.dateTimePickerAdv1.MonthImageList = this.imageList1;
```

```vbnet
' imageList1
Me.imageList1.ImageSize = New System.Drawing.Size(16, 16)
Me.imageList1.ImageStream =
    CType(resources.GetObject("imageList1.ImageStream"),
    System.Windows.Forms.ImageListStreamer)

' ImageList of the PopupMenu of the Popup Calendar
Me.dateTimePickerAdv1.MonthImageList = Me.imageList1
```

## API Reference

### Methods
- `MonthImageList`: Accesses the list of images for the popup menu of the Calendar.

### Properties
- `ImageList1`: Properties related to configuring the image list size and stream.

## Code Examples

### C#
```csharp
this.imageList1.ImageSize = new System.Drawing.Size(16, 16);
this.imageList1.ImageStream =
    ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));
this.dateTimePickerAdv1.MonthImageList = this.imageList1;
```

### VB.NET
```vbnet
Me.imageList1.ImageSize = New System.Drawing.Size(16, 16)
Me.imageList1.ImageStream =
    CType(resources.GetObject("imageList1.ImageStream"),
    System.Windows.Forms.ImageListStreamer)
Me.dateTimePickerAdv1.MonthImageList = Me.imageList1
```

## Page-level Navigation/TOC
- [3.5.3.2.3.5.1 Month Images](3.5.3.2.3.5.1%20Month%20Images)

## Cross References
- **See also:**
  - [Background Settings](Background%20Settings)
  - [3.5.3.2.3.5 Runtime Features](3.5.3.2.3.5%20Runtime%20Features)

<!-- tags: [Syncfusion, WinForms, DateTimePickerAdv, MonthImageList, Runtime Features, Calendar Control, Month Images] keywords: [MonthImageList, imageList1, Calendar, Popup Menu, ImageListStreamer, Property, Control, C#, VB.NET] -->
```