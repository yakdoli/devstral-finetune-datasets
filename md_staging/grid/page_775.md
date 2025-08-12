```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_775.jpeg
document_name: grid
page_number: 775
page_id: grid#page_775
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:39:33Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
RecordFilterDescriptor("OrderID", cond)
Me.gridGroupingControl1.GetTableDescriptor("Orders").RecordFilters.Add(filter)
```

## Special Characters in Filter Values

To match the special characters like left bracket ([]), question mark (?), number sign (#) and asterisk (*), enclose them in square brackets (like [\#] for # and [?] for * etc.,). The right bracket (]) can't be used within a group to match itself, but it can be used outside a group as an individual character.

This is illustrated in the below example with our Grid Grouping control.

```csharp
[C#]

void Form1_Load(object sender, EventArgs e)
{
    ArrayList rank = new ArrayList();
    RankData rankData = new RankData("aaa");
    rank.Add(rankData);
    rankData = new RankData("bbb#");
    rank.Add(rankData);
    gridGroupingControl1.DataSource = rank;
    string filter = "";
    RecordFilterDescriptor rfd = null;
    Record r = null;

    foreach (RankData a in rank)
    {
        filter = "[WellName] like '" + ReplaceSpcChar(a.WellName) + "'";
        rfd = new RecordFilterDescriptor(filter);
        gridGroupingControl1.TableDescriptor.RecordFilters.Add(rfd);
        int cont = gridGroupingControl1.Table.FilteredRecords.Count;
        r = new Record(gridGroupingControl1.Table);

        // Exception will be thrown here if special characters are not
        // enclosed in square brackets.
        r = gridGroupingControl1.Table.FilteredRecords[0];
        rankData = r.GetData() as RankData;
        gridGroupingControl1.TableDescriptor.RecordFilters.Clear();
    }
}

private string ReplaceSpcChar(string pattern)
{
}
```

## API Reference

### Methods
- **ReplaceSpcChar(string pattern)**
  - **Parameters:**
    - `pattern`: string
  - **Returns:** string

### Properties
- **TableDescriptor.RecordFilters**: Collection of record filter descriptors.

### Events
- None

## Code Examples (multi-language supported)
- The example above demonstrates how to handle special characters in filter values using the Grid Grouping control.

## Cross References
See also:
- Documentation on RecordFilterDescriptor
- Usage of Grouping controls in WinForms

<!-- tags: [syncfusion, windowsforms, filter, specialcharacters, gridgroupingcontrol] keywords: [recordfilterdescriptor, special characters, square brackets, grouping controls, filter values] -->
```