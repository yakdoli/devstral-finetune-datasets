```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_665.jpeg
document_name: grid
page_number: 665
page_id: grid#page_665
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:31:01Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Demonstrates how to change the Blink Time and Timer frequency for a `gridGroupingControl` in a Windows Forms application.
- Focuses on updating UI elements such as labels and controls using event handlers for `scroll` events.

## Content

### Setting Blink Time Frequency

```csharp
if (this.gridGroupingControl1.BlinkTime == 0)
    this.labelBlinkTime.Text = String.Format("Disabled.");
else
    this.labelBlinkTime.Text = String.Format("{0} milliseconds.", gridGroupingControl1.BlinkTime);
this.gridGroupingControl1.Refresh();
```

#### Changing Timer Frequency

```csharp
// To change the Timer Frequency.
private void trackBarTimer_Scroll(object sender, System.EventArgs e)
{
    if (this.trackBarTimer.Value == 0)
    {
        timer.Enabled = false;
        this.labelTimerInterval.Text = String.Format("Timer disabled.");
    }
    else
    {
        timer.Interval = 1000 / (this.trackBarTimer.Value * trackBarTimer.Value);
        timer.Enabled = true;
        this.labelTimerInterval.Text = String.Format("Every {0} milliseconds.", timer.Interval);
    }
}
```

### WINFORMS-Specific Implementation

#### Using C# for Timer Frequency Adjustment

```csharp
/* To change the Blink Time Frequency */
private Sub trackBarBlinkFrequency_Scroll(ByVal sender As Object, ByVal e As System.EventArgs) Handles trackBarBlinkFrequency.Scroll
    Me.gridGroupingControl1.BlinkTime = Me.trackBarBlinkFrequency.Value * 100
    If Me.gridGroupingControl1.BlinkTime = 0 Then
        Me.labelBlinkTime.Text = String.Format("Disabled.")
    Else
        Me.labelBlinkTime.Text = String.Format("{0} milliseconds.", gridGroupingControl1.BlinkTime)
    End If
    Me.gridGroupingControl1.Refresh()
End Sub
```

#### Adjusting Timer Frequency

```csharp
/* To change the Timer Frequency. */
Private Sub trackBarTimer_Scroll(ByVal sender As Object, ByVal e As System.EventArgs) Handles trackBarTimer.Scroll
    If Me.trackBarTimer.Value = 0 Then
```

### API Reference

#### Properties
- **gridGroupingControl1.BlinkTime**: Specifies the delay before starting the blink effect. Set to 0 to disable blinking.
- **timer.Interval**: Sets the timer tick frequency in milliseconds.

#### Methods
- **String.Format**: Used for formatting the label text dynamically.
- **Refresh()**: Updates the `gridGroupingControl` to reflect changes in blink settings.

### Code Examples

#### Example: Setting Blink Time

```csharp
this.gridGroupingControl1.BlinkTime = 500; // Sets blink time to 500 milliseconds.
```

#### Example: Disabling Blink

```csharp
this.gridGroupingControl1.BlinkTime = 0; // Disables blinking.
```

#### Example: Timer Interval Calculation

```csharp
timer.Interval = 1000 / (this.trackBarTimer.Value * trackBarTimer.Value); // Adjusts timer frequency based on a formula.
```

## RAG Annotations
<!-- tags: [Syncfusion, Windows Forms, gridGroupingControl, timer, blink time, UI updates] keywords: [gridGroupingControl, BlinkTime, Timer, TrackBar, UI refresh, frequency adjustment, control update] -->
```