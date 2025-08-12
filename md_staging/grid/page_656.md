```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_656.jpeg
document_name: grid
page_number: 656
page_id: grid#page_656
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:31:33Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
gridGroupingControl1.BlinkTime = 700
For i As Integer = 1 To 20
    gridGroupingControl1.TableDescriptor.Columns(i.ToString()).AllowBlink = True
Next i
gridGroupingControl1.Engine.AddBaseStylesForBlinking()
gridGroupingControl1.BaseStyles(GridEngine.BlinkIncreased).StyleInfo.TextColor = Color.White
gridGroupingControl1.BaseStyles(GridEngine.BlinkReduced).StyleInfo.TextColor = Color.White

gridGroupingControl1.Engine.BaseStyles.Add("CustomStyle")
gridGroupingControl1.BaseStyles("CustomStyle").StyleInfo.TextColor = Color.Black
gridGroupingControl1.BaseStyles("CustomStyle").StyleInfo.BackColor = Color.White

' PrepareViewStyleInfo
Private Sub gridGroupingControl1_TableControlPrepareViewStyleInfo(ByVal sender As Object, ByVal e As GridTableControlPrepareViewStyleInfoEventArgs)
    Dim style As GridTableCellStyleInfo = CType(e.Inner.Style, GridTableCellStyleInfo)
    Dim bs As BlinkState = gridGroupingControl1.GetBlinkState(style.TableCellIdentity)
    If bs <> BlinkState.None Then
        If bs = BlinkState.NewRecord Then
            e.Inner.Style.BaseStyle = "CustomStyle"
        End If
    End If
End Sub
```

3. A timer event is handled to insert and remove the records. This results in frequent list changes at regular intervals.

```csharp
bool skipTimer = false;
private void timer_Tick(object sender, EventArgs e)
{
    if (skipTimer)
        return;
    timerCount++;
    try
    {
        for (int i = 0; i < m_numUpdatesPerTick; i++)
        {
```

## API Reference

### Members
- `BlinkTime`: Gets or sets the blink time for the GridGroupingControl.
- `AllowBlink`: Gets or sets whether a column allows blinking.
- `PrepareViewStyleInfo`: Event that occurs when the grid prepares the view style information.
- `GetBlinkState`: Method to get the blink state for a specific cell in the grid.

## Code Examples

### VB.NET Example
```vb
' Configure blinking for the grid
gridGroupingControl1.BlinkTime = 700
For i As Integer = 1 To 20
    gridGroupingControl1.TableDescriptor.Columns(i.ToString()).AllowBlink = True
Next i
gridGroupingControl1.Engine.AddBaseStylesForBlinking()
gridGroupingControl1.BaseStyles(GridEngine.BlinkIncreased).StyleInfo.TextColor = Color.White
gridGroupingControl1.BaseStyles(GridEngine.BlinkReduced).StyleInfo.TextColor = Color.White
```

### C# Example
```csharp
// Configure blinking for the grid
gridGroupingControl1.BlinkTime = 700;
for (int i = 1; i <= 20; i++)
{
    gridGroupingControl1.TableDescriptor.Columns[i.ToString()].AllowBlink = true;
}
gridGroupingControl1.Engine.AddBaseStylesForBlinking();
gridGroupingControl1.BaseStyles(GridEngine.BlinkIncreased).StyleInfo.TextColor = Color.White;
gridGroupingControl1.BaseStyles(GridEngine.BlinkReduced).StyleInfo.TextColor = Color.White;
```

---

<!-- tags: [grid, gridgroupingcontrol, blinking, style, windows forms, syncfusion, version 11.4.0.26] keywords: [blinktime, allowblink, prepareviewstyleinfo, blinkstate, timer, frequent list changes] -->
```