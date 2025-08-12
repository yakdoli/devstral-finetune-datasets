```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_121.jpeg
document_name: XlsIO
page_number: 121
page_id: XlsIO#page_121
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:56:26Z
fidelity: lossless
-->

# Formatting in Excel

## Overview

- Excel removes leading zeros in zip codes, but number formats can be used to retain them.
- Custom number formats for zip codes, social security numbers, and telephone numbers are available.
- The table below explains various custom formatting codes for numbers and text.

## Content

### Information About Number Formats

Excel removes the zero (0) in the zip code. The reason is that zero is not required to display the value of the number. However, since number formats are not about the value, but they are about the appearance, you can use a special format to retain the leading zeros, **00000**.

#### Special Number Formats

In addition to the **00000** Zip Code number format, Excel also has:

- **00000-0000** for Zip-Plus-Four
- **000-00-0000** for Social Security numbers
- **(000)000-0000** for telephone numbers

If you live in a location that needs different zip codes, you can either design your own custom number formats.

#### Custom Formatting Codes

The following table shows various custom formatting codes.

| Number Code | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| General     | General number format.                                                     |
| 0 (zero)    | Digit placeholder. This code pads the value with zeros to fill the format. |
| #           | Digit placeholder. This code does not display extra zeros.                 |
| ?           | Digit placeholder. This code leaves a space for insignificant zeros but does not display them. |
| . (period)  | Decimal number.                                                           |
| %          | Percentage. Microsoft Excel multiplies by 100 and adds the % character.    |
| , (comma)   | Thousands separator. A comma followed by a placeholder scales the number by a thousand. |
| E+ E- e+ e- | Scientific notation.                                                      |

#### Text Codes

| Text Code          | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| $ - + / () : space | These characters are displayed in the number. To display any other character, enclose the character in quotation marks or precede it with a backslash. |
| \character         | This code displays the character you specify. Note Typing !, ^, &, ', ~, {, }, =, <, or > automatically places a backslash in front of the character. |

### Notes

- Excel's number formatting is about appearance, not value.
- You can design custom number formats for special requirements.

## API Reference (if applicable)

Not applicable.

## Code Examples (multi-language supported)

Not applicable.

## Page-level Navigation/TOC (if applicable)

Not applicable.

## Cross References

See also: Custom number formats, leading zeros, zip codes.

## RAG Annotations

<!-- tags: Excel, number formats, custom formatting, leading zeros, zip codes keywords: Excel, number formats, custom formatting, leading zeros, zip codes -->
```