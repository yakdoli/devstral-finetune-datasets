```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_122.jpeg
document_name: XlsIO
page_number: 122
page_id: XlsIO#page_122
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:55:29Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Overview of formatting codes for displaying text, dates, and time in XlsIO.
- Detailed descriptions of various formatting codes and their uses.
- Instructions for using asterisks, underscores, and placeholders for text alignment and formatting.

## Content

### Number Code
| Number Code | Description |
|-------------|-------------|
| "text"      | This code displays the text.                                       |
| *           | This code repeats the next character in the format to fill the column width. <br> Note: Only one asterisk per section of a format is allowed.                                       |
| _ (underscore) | This code skips the width of the next character. This code is commonly used as "_)" (without the quotation marks) to leave space for a closing parenthesis in a positive number format when the negative number format includes parentheses. <br> This allows the values to line up at the decimal point. |
| @           | Text placeholder.                                                   |

### Date Code
| Date Code | Description |
|-----------|-------------|
| m         | Month as a number without leading zeros (1-12). |
| mm        | Month as a number with leading zeros (01-12).  |
| mmm       | Month as an abbreviation (Jan - Dec).           |
| mmmm      | Unabbreviated Month (January - December).       |
| d         | Day without leading zeros (1-31).               |
| dd        | Day with leading zeros (01-31).                 |
| ddd       | Week day as an abbreviation (Sun - Sat).        |
| dddd      | Unabbreviated week day (Sunday - Saturday).     |
| yy        | Year as a two-digit number (for example, 96).  |
| yyyy      | Year as a four-digit number (for example, 1996). |

### Time Code
| Time Code | Description |
|-----------|-------------|
| h         | Hours as a number without leading zeros (0-23). |
| hh        | Hours as a number with leading zeros (00-23).   |

<!-- tags: [Essential XlsIO, formatting codes, number codes, date codes, time codes] keywords: [text formatting, character repetition, text placeholder, date formatting, time formatting] -->
```