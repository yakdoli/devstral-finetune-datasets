```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: schedule
page_number: 062
page_id: schedule#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:12:10Z
fidelity: lossless
-->

## 4.3 Metro Theme for Essential Schedule

This feature enables you to apply new Metro styles to the Schedule control.

### Use Case Scenario

The Metro theme support is useful for commercial applications in order to attract end users with inspiring UI look and feel.

### Properties

| Property      | Description                                                                            |
|---------------|-----------------------------------------------------------------------------------------|
| VisualStyle   | This is an enumeration type property. It is used to get or set the visual styles (skins) such as Office2010, Office2007, Office2003, Metro, etc. |

### Events

| Event      | Parameters                   | Description                           |
|------------|-------------------------------|---------------------------------------|
| ThemeChanged | Object sender, EventArgs e | Occurs when the ThemesEnabled property is changed. |

### 4.3.1 Applying Metro Theme to the Schedule Control

You can apply the Metro theme to the Schedule control by setting the GridVisualStyles property as Metro. The following code example illustrates this.

#### Code Example

```csharp
this.scheduleControl1.GetScheduleHost().Schedule.Appearance.VisualStyle = Syncfusion.Windows.Forms.GridVisualStyles.Metro;
```

```vb
Me.scheduleControl1.GetScheduleHost().Schedule.Appearance.VisualStyle = Syncfusion.Windows.Forms.GridVisualStyles.Metro
```

The following screenshot is a sample output for the previous code.

### Summary
- The Metro theme can be applied to the Schedule control.
- This theme support is beneficial for commercial applications to enhance UI appeal.
- The `VisualStyle` property is used to set the theme, and an event `ThemeChanged` is triggered when it is modified.
- Example code in both C# and VB.NET is provided to demonstrate how to apply the Metro theme.
```