```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_725.jpeg
document_name: grid
page_number: 725
page_id: grid#page_725
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:35:24Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

```csharp
Me.gridGroupingControl1.ShowsGroupDevelopmentArea = True
Me.gridGroupingControl1.TopLevelGroupOptions.ShowGroupHeader = True
Me.gridGroupingControl1.TopLevelGroupOptions.ShowGroupFooter = True
Me.gridGroupingControl1.TopLevelGroupOptions.ShowCaption = True
Me.gridGroupingControl1.TopLevelGroupOptions.ShowGroupPreview = True
Me.gridGroupingControl1.ChildGroupOptions.ShowGroupPreview = True
Me.gridGroupingControl1.TableOptions.GroupFooterSectionHeight = 30
Me.gridGroupingControl1.TableOptions.GroupHeaderSectionHeight = 30
Me.gridGroupingControl1.TableOptions.GroupPreviewSectionHeight = 25
Me.gridGroupingControl1.TopLevelGroupOptions.ShowAddNewRecordBeforeDetails = True
Me.gridGroupingControl1.TopLevelGroupOptions.ShowAddNewRecordAfterDetails = True
Me.gridGroupingControl1.ChildGroupOptions.CaptionText = "There are {RecordCount} items under {CategoryName}: {Category}"
```

### Handle the QueryCellStyleInfo event to manipulate the group elements.

```csharp
this.gridGroupingControl.QueryCellStyleInfo += new GridTableStyleInfoEventHandler(gridGroupingControl_QueryCellStyleInfo);

void gridGroupingControl_QueryCellStyleInfo(object sender, GridTableStyleInfoEventArgs e)
{
    if (e.TableCellIdentity.TableCellType == GridTableCellType.GroupFooterSectionCell ||
        e.TableCellIdentity.TableCellType == GridTableCellType.GroupHeaderSectionCell)
    {
        e.Style.Enabled = false;
        if (e.TableCellIdentity.TableCellType == GridTableCellType.GroupFooterSectionCell)
            e.Style.Text = "The details in the footer can be placed by enabling ShowGroupFooter and handling QueryCellStyleInfo";
        if (e.TableCellIdentity.TableCellType == GridTableCellType.GroupHeaderSectionCell)
            e.Style.Text = "The details in the header can be placed by enabling ShowGroupHeader and handling QueryCellStyleInfo";
    }

    if (e.TableCellIdentity.TableCellType == GridTableCellType.GroupPreviewCell)
    {
        Element el = e.TableCellIdentity.DisplayElement;
        e.Style.CellValue = "Preview notes for Group (\" + 
```

<!-- tags: [product, module, control, api, version] keywords: [gridGroupingControl, QueryCellStyleInfo, GridTableCellStyleInfo, GroupFooterSectionCell, GroupHeaderSectionCell, GroupPreviewCell, TableOptions, ShowGroupFooter, ShowGroupHeader, ShowGroupPreview, ShowAddNewRecordBeforeDetails, ShowAddNewRecordAfterDetails, CaptionText, Essential Grid for Windows Forms] -->
```