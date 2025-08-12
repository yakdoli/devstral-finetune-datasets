```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_080.jpeg
document_name: edit
page_number: 080
page_id: edit#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:58:49Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
Me.editControl1.ToggleShowingWhiteSpaces()
```

## Showing / Hiding Indicators

You can selectively show / hide the whitespace indicators by using the following subproperties of the WhiteSpaceIndicators property - ShowSpaces, ShowTabs, and ShowNewLines.

| Edit Control Property | Description |
|------------------------|-------------|
| ShowSpaces            | Indicates whether spaces should be replaced with symbols. |
| ShowTabs              | Indicates whether tabs should be replaced with symbols. |
| ShowNewLines          | Indicates whether new lines should be replaced with symbols. |

### C\#

```csharp
// Custom indicator for Line Feed.
this.editControl1.WhiteSpaceIndicators.ShowSpaces = true;

// Custom indicator for Tab.
this.editControl1.WhiteSpaceIndicators.ShowTabs = true;

// Custom indicator for Space Character.
this.editControl1.WhiteSpaceIndicators.SpaceNewLines = true;
```

### VB.NET

```vb
' Custom indicator for Line Feed.
Me.editControl1.WhiteSpaceIndicators.ShowSpaces = True

' Custom indicator for Tab.
Me.editControl1.WhiteSpaceIndicators.ShowTabs = True

' Custom indicator for Space Character.
Me.editControl1.WhiteSpaceIndicators.SpaceNewLines = True
```

You can also set the indicators to indicate single spaces, tabs, and line feeds by using the NewLineString, TabString, and SpaceChar subproperties of the WhiteSpaceIndicators property, as shown below.

| Edit Control Property | Description |
|------------------------|-------------|
| NewLineString         | Gets / sets string that represents line feed in WhiteSpace mode. |

<!-- tags: [product, module, control, api, version?] keywords: [whiteSpaceIndicators, showSpaces, showTabs, showNewLines, newlineString, tabString, spaceChar, essential edit, windows forms, indicator, symbol, line feed, tab, space character] -->
```