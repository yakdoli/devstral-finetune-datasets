``` markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_081.jpeg
document_name: edit
page_number: 081
page_id: edit#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:59:11Z
fidelity: lossless
-->

## Overview
- This section details the configuration of whitespace indicators and line numbers in the Edit Control for Windows Forms.
- It provides examples in both C# and VB.NET for customizing the whitespace indicators such as TabString, SpaceChar, and NewLineString.
- Explains how to enable line numbers and highlight the current line using specific properties in the Edit Control.

## Content

### Whitespace Indicators

The following table describes the properties related to whitespace indicators:

| Property     | Description                                                                 |
|--------------|-------------------------------------------------------------------------------|
| TabString    | Gets / sets string that represents Tab in WhiteSpace mode.                  |
| SpaceChar    | Gets / sets character that represents line feed in WhiteSpace mode.         |

#### Custom Indicators for Whitespace

**C# Example:**
```csharp
// Custom indicator for Line Feed.
this.editControl1.WhiteSpaceIndicators.NewLineString = "LF";

// Custom indicator for Tab.
this.editControl1.WhiteSpaceIndicators.TabString = "TAB";

// Custom indicator for Space Character.
this.editControl1.WhiteSpaceIndicators.SpaceChar = "s";
```

**VB.NET Example:**
```vb
' Custom indicator for Line Feed.
Me.editControl1.WhiteSpaceIndicators.NewLineString = "LF"

' Custom indicator for Tab.
Me.editControl1.WhiteSpaceIndicators.TabString = "TAB"

' Custom indicator for Space Character.
Me.editControl1.WhiteSpaceIndicators.SpaceChar = "s"
```

##### See Also

- [Spaces and Tabs](#spaces-and-tabs)

### 4.4.7 Line Numbers and Current Line Highlighting

Line Numbers can be automatically assigned to the contents of the Edit Control by enabling its `ShowLineNumbers` property.

#### Get the Number of Lines in the Edit Control

The number of lines in the Edit Control can be obtained by using the `PhysicalLineCount` property. This property returns the actual number of lines in the Edit Control, without considering lines that might be hidden due to a collapsed outlining block or new lines that might have been added because of wordwrap.

#### Key Points
- Use `ShowLineNumbers` to display line numbers automatically.
- Use `PhysicalLineCount` for retrieving the total number of lines in the control.

<!-- tags: [product, module, control, api, version?] keywords: [Edit Control, Whitespace Indicators, Line Numbers, ShowLineNumbers, PhysicalLineCount, TabString, SpaceChar, NewLineString, Syncfusion WinForms, C#, VB.NET] -->
```