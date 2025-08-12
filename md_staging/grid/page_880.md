```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_880.jpeg
document_name: grid
page_number: 880
page_id: grid#page_880
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:33Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
"+style.CellType.ToString();
    else
        info = style.TableCellIdentity.ToString();
}
    
listBox1.Items.Clear();
listBox1.Items.Add("MousePosition: " + ptClient.ToString());
listBox1.Items.Add("Category Keys: " +
                  displayElement.ParentChildTable.CategoriesToString());
listBox1.Items.Add("Display Element Type: " +
                  displayElement.GetType().Name);
listBox1.Items.Add("Cell Information: " + info);
}
```

### [VB.NET]

```vb
Private Sub TableControl_MouseMove(ByVal sender As Object, ByVal e As MouseEventArgs)
    Dim ptClient As New Point(e.X, e.Y)
    Dim tableControl As GridTableControl = Me.groupingGrid1.TableControl

    Dim style As GridTableCellStyleInfo =
                    tableControl.PointToTableCellStyle(ptClient)
    Dim displayElement As Element =
                    style.TableCellIdentity.DisplayElement
    Dim info As String = ""

    If Not (style Is Nothing) Then
        If Not (style.TableCellIdentity.Column Is Nothing) Then
            info = "Field Name - " & style.TableCellIdentity.Column.Name &
                   ", Field Value - """ & style.CellValue.ToString() &
                   """, Field Type - " & style.CellType.ToString()
        Else
            info = style.TableCellIdentity.ToString()
        End If
    End If
    listBox1.Items.Clear()
    listBox1.Items.Add("MousePosition: " & ptClient.ToString())
    listBox1.Items.Add("Category Keys: " &
                  displayElement.ParentChildTable.CategoriesToString())
    listBox1.Items.Add("Display Element Type: " &
                  displayElement.GetType().Name)
    listBox1.Items.Add("Cell Information: " & info)
End Sub
```

2. Here is a sample output.
```html

---

**© 2013 Syncfusion. All rights reserved.**

880 | Page
```

<!-- tags: [syncfusion, windows-forms, essential-grid, tablecontrol_mousemove, mouseeventargs, gridtablecontrol, gridtablecellstyleinfo] keywords: [parentchildtable, categories, displayelement, fieldname, fieldvalue, fieldtype, cellinformation, cursorposition, categorykeys, displayelementtype, listbox] -->
```