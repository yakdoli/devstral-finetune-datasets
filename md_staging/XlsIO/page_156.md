```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_156.jpeg
document_name: XlsIO
page_number: 156
page_id: XlsIO#page_156
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:29Z
fidelity: lossless
-->

## Essential XlsIO

### New Formatting Rule for setting Icon Sets

**Figure 55: New Formatting Rule for setting Icon Sets**

The image shows a dialog box titled **"New Formatting Rule"** where various rule types can be selected to format cells based on specific criteria. The `Edit the Rule Description` section sets up the formatting rule to display icons according to the following conditions:

- **Format all cells based on their values**
- **Format Style:** Icon Sets
- **Icon rules:**
  - Green circle: when value is `>= 67` (Percent)
  - Yellow circle: when value is `>= 33` and `< 67` (Percent)
  - Red circle: when value is `< 33`
- **Icon Style:** `3 Traffic Lights (Unrimmed)`
- **Options:** Reverse Icon Order, Show Icon Only

### Visualizations in XlsIO

XlsIO provides support for visualizations such as DataBar, IconSet, and ColorScale through specific interfaces. These visualizations can be customized by specifying criteria using XlsIO. The following code example illustrates how to apply and customize various visualizations.

#### Code Example in C#

```csharp
// Add condition for the range
IConditionalFormats conditionalFormats = 
    Worksheet.Range["C7:C46"].ConditionalFormats;
IConditionalFormat conditionalFormat = conditionalFormats.AddCondition();
```

---

## API Reference (if applicable)
- The `IConditionalFormats` interface is used for managing conditional formats within a specified range.
- `AddCondition()` method is used to define new conditional formats based on specific criteria.

## Code Examples

### C# Example

The provided C# code demonstrates how to add a conditional format for a specified range within a worksheet. This includes setting up the format rules and criteria programmatically.

```csharp
IConditionalFormats conditionalFormats = 
    Worksheet.Range["C7:C46"].ConditionalFormats;
IConditionalFormat conditionalFormat = conditionalFormats.AddCondition();
```

### Explanation

- **IConditionalFormats**: This interface allows for the management of conditional formatting within a specified range. It provides methods to add or modify conditions.
- **AddCondition()**: This method is used to define a new conditional format, where criteria can be specified programmatically.

## Cross References

See also:
- Documentation on `IConditionalFormats`
- Guidelines for creating and customizing visualizations in XlsIO

---

<!-- tags: [xlsio, conditional-formats, data-visualization, icon-sets, percent-criteria] keywords: [syncfusion, winforms, conditional formatting, data bars, color scales, rules customization] -->
```