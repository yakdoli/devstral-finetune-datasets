<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_999.jpeg
document_name: grid
page_number: 999
page_id: grid#page_999
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:55:00Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
    ret = " >= 40";
    break;
}
    e.Style.CellValue = String.Format("{0}: {1} Items.", ret,
    e.TableCellIdentity.DisplayElement.ParentGroup.GetChildCount();
}
}
```

## [VB.NET]

' Subscribe to QueryCellStyleInfo event to display custom group caption.
```vb.net
    AddHandler Me.gridGroupingControl1.QueryCellStyleInfo, AddressOf
    gridGroupingControl1_QueryCellStyleInfo
    
    Private Sub gridGroupingControl1_QueryCellStyleInfo(ByVal sender As
    Object, ByVal e As GridTableCellStyleInfoEventArgs)
        If Not (e.TableCellIdentity.GroupedColumn Is Nothing) AndAlso Not
        (e.TableCellIdentity.DisplayElement.ParentGroup Is Nothing) AndAlso
        TypeOf e.TableCellIdentity.DisplayElement.ParentGroup.Category Is
        Integer Then
            
            If TypeOf e.TableCellIdentity.DisplayElement Is CaptionRow _
            AndAlso e.TableCellIdentity.GroupedColumn.Name = "Col2" Then
                Dim cat As Integer =
                Fix(e.TableCellIdentity.DisplayElement.ParentGroup.Category)
                Dim ret As String = ""
                Select Case cat
                    Case 1
                        ret = " < 10"
                    Case 2
                        ret = "10 - 19"
                    Case 3
                        ret = "20 - 29"
                    Case 4
                        ret = "30 - 39"
                    Case 5
                        ret = " >= 40"
                End Select
                e.Style.CellValue = String.Format("{0}: {1} Items.", ret,
                e.TableCellIdentity.DisplayElement.ParentGroup.GetChildCount())
            End If
        End If
    End Sub
```

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridGroupingControl
  - **Properties**:
    - `QueryCellStyleInfo`: Trigger to customize group caption displaying.
  - **Methods**:
    - `GetChildCount()`: Returns the number of child items in a group.
  - **Events**:
    - `QueryCellStyleInfo`: Event triggered before grid cell style is applied.

## Code Examples

### C#
```csharp
// Subscribe to QueryCellStyleInfo event
this.gridGroupingControl1.QueryCellStyleInfo += GridGroupingControl1_QueryCellStyleInfo;
    
private void GridGroupingControl1_QueryCellStyleInfo(object sender, GridTableCellStyleInfoEventArgs e)
{
    if (e.TableCellIdentity.GroupedColumn != null &&
        e.TableCellIdentity.DisplayElement.ParentGroup != null &&
        e.TableCellIdentity.DisplayElement.ParentGroup.Category is int)
    {
        if (e.TableCellIdentity.DisplayElement is CaptionRow &&
            e.TableCellIdentity.GroupedColumn.Name == "Col2")
        {
            int cat = (int)e.TableCellIdentity.DisplayElement.ParentGroup.Category;
            string ret = "";
            switch (cat)
            {
                case 1:
                    ret = " < 10";
                    break;
                case 2:
                    ret = "10 - 19";
                    break;
                case 3:
                    ret = "20 - 29";
                    break;
                case 4:
                    ret = "30 - 39";
                    break;
                case 5:
                    ret = " >= 40";
                    break;
            }
            e.Style.CellValue = string.Format("{0}: {1} Items.", ret,
                                             e.TableCellIdentity.DisplayElement.ParentGroup.GetChildCount());
        }
    }
}
```

### VB.NET
```vb.net
' Subscribe to QueryCellStyleInfo event
AddHandler Me.gridGroupingControl1.QueryCellStyleInfo, AddressOf
gridGroupingControl1_QueryCellStyleInfo

Private Sub gridGroupingControl1_QueryCellStyleInfo(ByVal sender As
Object, ByVal e As GridTableCellStyleInfoEventArgs)
    If Not (e.TableCellIdentity.GroupedColumn Is Nothing) AndAlso Not
    (e.TableCellIdentity.DisplayElement.ParentGroup Is Nothing) AndAlso
    TypeOf e.TableCellIdentity.DisplayElement.ParentGroup.Category Is
    Integer Then
        If TypeOf e.TableCellIdentity.DisplayElement Is CaptionRow _
        AndAlso e.TableCellIdentity.GroupedColumn.Name = "Col2" Then
            Dim cat As Integer =
            Fix(e.TableCellIdentity.DisplayElement.ParentGroup.Category)
            Dim ret As String = ""
            Select Case cat
                Case 1
                    ret = " < 10"
                Case 2
                    ret = "10 - 19"
                Case 3
                    ret = "20 - 29"
                Case 4
                    ret = "30 - 39"
                Case 5
                    ret = " >= 40"
            End Select
            e.Style.CellValue = String.Format("{0}: {1} Items.", ret,
            e.TableCellIdentity.DisplayElement.ParentGroup.GetChildCount())
        End If
    End If
End Sub
```

<!-- tags: [syncfusion, winforms, essentialgrid, gridgroupingcontrol, querycellstyleinfo] keywords: [custom group caption, col2, category switch, display element, child count] -->