```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_123.jpeg
document_name: XlsIO
page_number: 123
page_id: XlsIO#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:56:26Z
fidelity: lossless
-->

# Essential XlsIO

| Number Code            | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| m                      | Minutes as a number without leading zeros (0-59).                        |
| mm                     | Minutes as a number with leading zeros (00-59).                         |
| s                      | Seconds as a number without leading zeros (0-59).                       |
| ss                     | Seconds as a number with leading zeros (00-59).                        |
| AM/PM am/pm            | Time based on the twelve-hour clock.                                    |
| Miscellaneous Code     | Description                                                               |
| [BLACK], [BLUE],      | These codes display the characters in the specified colors.              |
| [CYAN], [GREEN],      | Note: n is a value from 1 to 56 and refers to the nth color in the color palette. |
| [MAGENTA], [RED],     |                                                                           |
| [WHITE], [YELLOW],    |                                                                           |
| [COLOR n]              |                                                                           |
| [Condition value]      | Condition may be <, >, =, >=, <=, <> and value may be any number.      |
|                        | Note: A number format may contain up to two conditions.                 |

## Number Formatting in XlsIO

XlsIO provides API support for reading and writing the various built-in and custom number formats in a cell by using the **NumberFormat** property of **IRange**. To set the various number formats, use the appropriate typed properties [Number, DateTime, TimeSpan].

The following code example illustrates how to set the format for Number.

### Example Code

```csharp
[C#]

// Applying Number Format.
sheet.Range["C2"].Number = 1000000.00075;
sheet.Range["B2"].Text = "0.00";
sheet.Range["C2"].NumberFormat = "0.00";

sheet.Range["C3"].Number = 1000000.500;
sheet.Range["B3"].Text = "###,##";
sheet.Range["C3"].NumberFormat = "###,##";

sheet.Range["C5"].Number = 10000;
```

<!-- tags: [XlsIO, number formatting, cell formatting, API support, IRange, NumberFormat, typed properties] keywords: [number formats, custom number formats, XlsIO, number formatting, cellular data manipulation, DateTime, TimeSpan] -->
```