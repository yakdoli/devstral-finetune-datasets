```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_389.jpeg
document_name: grid
page_number: 389
page_id: grid#page_389
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### 4.1.4.7.3 Using the GridStyleInfo Class

By using the GridRangeInfo class and the properties of the GridStyleInfo class, you can write code illustrating how to enter values into a grid and how to affect the appearance of these displayed values. In the sections that follow, you will learn how to create a Grid object and place it on a form. Then you can set the style values by using the Grid classes discussed so far: GridStyleInfo, GridRangeInfo, and GridControl.

#### 4.1.4.7.3.1 Setting GridStyleInfo Properties

There are several ways of setting the GridStyleInfo properties. If you want to set them for a particular cell, you need to use the row and column values as indexers on the GridControl object to retrieve the GridStyleInfo object that is associated with a particular cell. But, to change a BaseStyle, a ColumnStyle, or a RowStyle, you will have to use different accessory methods to retrieve the style which is under consideration. In the code samples that follow, we will show you several ways of changing particular styles.

**Note:** In this section, we are working with the cell-oriented Grid control which allows us to explicitly set individual cell and row properties. In the column-oriented Grid Data Bound Grid, explicitly setting individual cell and row properties is not supported. Instead, events are used to set these properties on demand. You can see samples in the Grid Data Bound Grid section.

It comprises the following sections:

##### 4.1.4.7.3.1.1 Through Code

Given below is the code to help you create GridStyleInfo properties.

```csharp
// Add some text to cell (2,3).
gridControl1[2, 3].CellValue = "Essential";

// Create a GridStyleInfo.
GridStyleInfo style = new GridStyleInfo();
```

## Page-level Navigation/TOC (if applicable)

- 4.1.4.7.3 Using the GridStyleInfo Class
  - 4.1.4.7.3.1 Setting GridStyleInfo Properties
    - 4.1.4.7.3.1.1 Through Code

## Cross References

See also: GridControl, GridRangeInfo, GridStyleInfo.

<!-- tags: [Essential Grid for Windows Forms, GridControl, GridRangeInfo, GridStyleInfo] keywords: [GridControl, GridRangeInfo, GridStyleInfo, cell-oriented Grid, column-oriented Grid, Data Bound Grid, setting GridStyleInfo properties, Through Code] -->
```