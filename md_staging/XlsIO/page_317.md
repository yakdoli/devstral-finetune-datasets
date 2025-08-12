```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_317.jpeg
document_name: XlsIO
page_number: 317
page_id: XlsIO#page_317
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:09:34Z
fidelity: lossless
-->

# Essential XlsIO

## Content

### 4.3.3 Sheet Options

**Overview**

- 1. Explains how to scale pages length and width wise during printing.
- 2. Demonstrates scaling options using code examples in C# and VB.NET.
- 3. Introduces the use of the "Sheet" tab in the "Page Setup" dialog for customizing sheet printing options.

**Figure 115: Page Setup - Page Scaling**

The dialog box shown in the figure provides options for adjusting the orientation, scaling, paper size, print quality, and more. The scaling section allows you to fit content to a specified number of pages wide and tall.

**Description**

XlsIO allows you to scale the pages length and width wise while printing. The following code example illustrates this:

#### Scaling Example

**C#**

```csharp
sheet.PageSetup.FitToPagesTall = 2;
sheet.PageSetup.FitToPagesWide = 3;
```

**VB.NET**

```vb
sheet.PageSetup.FitToPagesTall = 2;
sheet.PageSetup.FitToPagesWide = 3;
```

**Sheet Options**

Spreadsheets can be large. The **Sheet tab** in the **Page Setup** dialog box can be used to print only the cells required by the user. MS Excel provides various options for customizing the sheet for printing through the **Sheet tab**.

## API Reference

- **FitToPagesTall**: Adjusts the number of pages tall to fit the content.
- **FitToPagesWide**: Adjusts the number of pages wide to fit the content.

## Code Examples

### C#

```csharp
sheet.PageSetup.FitToPagesTall = 2;
sheet.PageSetup.FitToPagesWide = 3;
```

### VB.NET

```vb
sheet.PageSetup.FitToPagesTall = 2;
sheet.PageSetup.FitToPagesWide = 3;
```

## Cross References

- For more details on **Page Setup** options and how to customize Excel printing, refer to the relevant sections in the Excel documentation or the XlsIO user guide.

<!-- tags: [xlsio, page setup, sheet options, printing settings, scaling options, programming examples, syncfusion windows forms, sheet tab] keywords: [orientation, scaling, paper size, print quality, fit to pages, sheet customization, c#, vb.NET, xlsio user guide] -->
```