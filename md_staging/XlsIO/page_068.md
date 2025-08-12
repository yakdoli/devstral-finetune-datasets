```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: XlsIO
page_number: 068
page_id: XlsIO#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:53:02Z
fidelity: lossless
-->

## Overview
- Explanation of `UseSystemSeparators`, `Workbooks`, and `Worksheets` properties in the Application object.
- List of public methods and events of the `ExcelEngine` class with their descriptions.

## Content

### Properties

| Property             | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| UseSystemSeparators | True (default) if the system separators of Microsoft Excel are enabled.     |
| Workbooks            | Returns a Workbooks collection that represents all the open workbooks.      |
| Worksheets           | For an Application object, this returns a Sheets collection that represents all the worksheets in the active workbook. For a Workbook object, this returns a Sheets collection that represents all the worksheets in the specified workbook. |

### Public Methods

The following table provides the list of methods and their corresponding descriptions of `ExcelEngine` class:

| Methods              | Description                                                                                     |
|----------------------|--------------------------------------------------------------------------------------------------|
| CentimetersToPoints | Converts a measurement from centimeters to points (one point equals 0.035 centimeters).           |
| ConvertUnits        | Converts units.                                                                                 |
| InchesToPoints      | Converts a measurement from inches to points.                                                    |
| Save                | Saves changes to the active workbook.                                                            |

### Public Events

The following table lists the events of the `ExcelEngine` class and their corresponding descriptions:

| Events                | Description                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| OnPasswordRequired   | This event is fired when the user tries to open a password-protected workbook without specifying a password. It is used to obtain the password. |
| OnWrongPassword      | This event is fired when the user specifies an incorrect password when trying to open a password-protected workbook. It is used to obtain the correct password. |

## Page-level Navigation/TOC (if applicable)
- This page focuses on the public properties, methods, and events related to `ExcelEngine` class in Syncfusion Winforms.

## Cross References
- Refer to related sections or pages within the user guide for additional functionality and implementation details.

<!-- tags: [ExcelEngine, Syncfusion Winforms, Properties, Methods, Events] keywords: [UseSystemSeparators, Workbooks, Worksheets, CentimetersToPoints, ConvertUnits, InchesToPoints, Save, OnPasswordRequired, OnWrongPassword] -->
```