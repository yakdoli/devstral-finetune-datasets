<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_079.jpeg
document_name: edit
page_number: 079
page_id: edit#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:58:25Z
fidelity: lossless
-->

---

## Overview

- Describes how to enable and toggle whitespace indicators in Windows Forms.
- Explains the `ShowWhiteSpaces` property and its usage.
- Demonstrates the `ToggleShowingWhiteSpaces` method for dynamic visibility control.

---

## Content

### Enabling Whitespace Indicators

You can enable whitespace indicators by setting the `ShowWhiteSpaces` property to `True`. By default, this property is set to `False`.

#### `ShowWhiteSpaces` Property

| Edit Control Property | Description                                                                                      |
|-----------------------|--------------------------------------------------------------------------------------------------|
| ShowWhiteSpaces       | Gets/sets value indicating whether whitespaces should be shown as special symbols.               |

#### Enabling Whitespace Indicators in Code

You can also toggle the visibility of the whitespace indicators by using the `ToggleShowingWhiteSpaces` method, or by setting the `ShowWhiteSpaces` property to `False`.

#### `ToggleShowingWhiteSpaces` Method

| Edit Control Method           | Description                          |
|------------------------------|--------------------------------------|
| ToggleShowingWhiteSpaces     | Toggles showing of whitespaces.     |

---

### Code Examples

#### C#

```csharp
// Enabling white space indicators.
this.editControl.ShowWhitespaces = true;

// Toggle the visibility of the white space indicators.
this.editControl.ToggleShowingWhiteSpaces();
```

#### VB.NET

```vb
' Enabling white space indicators.
Me.editControl.ShowWhitespaces = True

' Toggle the visibility of the white space indicators.
Me.editControl.ToggleShowingWhiteSpaces()
```

---

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.

---

## Cross References
- For cross-page references without URLs, keep the exact anchor text.

---

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->