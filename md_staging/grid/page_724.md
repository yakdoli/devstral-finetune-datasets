```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_724.jpeg
document_name: grid
page_number: 724
page_id: grid#page_724
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:36:24Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

| {Category} | Displays the CaptionSection.ParentGroup.Category. |
| --- | --- |
| {RecordCount} | Displays the CaptionSection.ParentGroup.GetFilteredRecordCount(). |
| Summary Tokens | Allows you to display any item you enter as a Summary Column. See discussion below. |

## Custom Summary Tokens

Any summary item you add can be included in the CaptionText. You have the option of hiding summaries, so it is possible to add summaries only for the purpose of displaying values in the CaptionText. If you have added a summary row named Row1, and a Summary columns named Column1, then you can also use the value of this summary item in the caption with the token {Row1.Column1}.

## Example

Here is a sample implementation that illustrates the usage of the above properties.

1.  Set up a Grid Grouping control and bind a data source into it.
2.  Setup the necessary Group Options as required.

### C#

```csharp
// Group Options Settings.
this.gridGroupingControl.ShowGroupDropArea = true;
this.gridGroupingControl.TopLevelGroupOptions.ShowGroupHeader = true;
this.gridGroupingControl.TopLevelGroupOptions.ShowGroupFooter = true;
this.gridGroupingControl.TopLevelGroupOptions.ShowCaption = true;
this.gridGroupingControl.TopLevelGroupOptions.ShowGroupPreview = true;
this.gridGroupingControl.ChildGroupOptions.ShowGroupPreview = true;
this.gridGroupingControl.TableOptions.GroupFooterSectionHeight = 30;
this.gridGroupingControl.TableOptions.GroupHeaderSectionHeight = 30;
this.gridGroupingControl.TableOptions.GroupPreviewSectionHeight = 25;
this.gridGroupingControl.TopLevelGroupOptions.ShowAddNewRecordBeforeDetails = true;
this.gridGroupingControl.TopLevelGroupOptions.ShowAddNewRecordAfterDetails = true;
this.gridGroupingControl.ChildGroupOptions.CaptionText = "There are {RecordCount} items under {CategoryName} : {Category}";
```

### VB.NET

```vb
' Group Options Settings.
```

## Cross References

See also:
- **Getting Started**: For initial setup and basic usage of **Grid** controls.
- **Grouping and Aggregation**: Detailed configurations for grouping, aggregating, and displaying summary data in grid controls.

<!-- tags: [syncfusion, winforms, grid, caption, summary, tokens, grouping, recordcount, category, aggregation, user-interface] keywords: [captiontext, groupedcontrols, summarytokens, recordcount, category, captionsection, filtering, groupingoptions] -->
```