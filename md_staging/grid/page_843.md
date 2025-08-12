```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_843.jpeg
document_name: grid
page_number: 843
page_id: grid#page_843
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:44:14Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
gridGroupingControl1.TopLevelGroupOptions.ShowFilterBar = True
For Each col In _gridGroupingControl2.TableDescriptor.Columns
    col.AllowFilter = True
Next col
```

## Screen shot:

![Figure 326: Paging Support in Windows Grid](RenderImageHere)  

Figure Figure 326: Paging Support in Windows Grid

The following sample illustrates Paging support in the GridGrouping control for a data table populated with 100,000 records.

Note: For more details, refer the following sample link:  
[http://www.syncfusion.com/downloads/Support/DirectTrac/101296/Paging-1289568956.zip](http://www.syncfusion.com/downloads/Support/DirectTrac/101296/Paging-1289568956.zip)

### 4.3.4.4.1 Paging support with a different data source

**Overview**
- This section explains how paging support has been integrated into the GridGroupingControl to improve its performance.
- It supports various data sources such as IEnumerable, Array List, Generic Collection, IBindingList, and DataTable.
- Provides insights into wiring the GridGrouping control to a Pager.

#### Content

Paging support has been provided in the Grid control for Windows Forms to improve the performance of the GridGroupingControl. This feature enables you to load data in an efficient way by storing and retrieving records in pages. Paging support is provided for different data sources. We have provided paging support with IEnumerable, Array List, Generic Collection, IBindingList, and DataTable.

The following code sample illustrates wiring the GridGrouping control to a Pager:

---

## Footer

© 2013 Syncfusion. All rights reserved.
---
<!-- tags: [syncfusion, winforms, gridgroupingcontrol, paging, data sources] keywords: [paging support, gridgroupingcontrol, windows forms, performance, IEnumerable, Array List, Generic Collection, IBindingList, DataTable] -->
```