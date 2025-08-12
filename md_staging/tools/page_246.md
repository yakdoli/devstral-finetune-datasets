```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_246.jpeg
document_name: tools
page_number: 246
page_id: tools#page_246
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:02:20Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
while (ienum.MoveNext())
{
    dockedctrls.Add(ienum.Current);
}

foreach (Control dockedControl in dockedctrls)
{
    GetDockingRelationship(dockedControl);
    count = count + 1;
}
}
```

### [VB.NET]

```vb
Private Sub InitializeDockControlState()

    Me.dockingManager1.FloatControl(Me.myUserControl11, New Rectangle(250, 250, 220, 260))
    Me.dockingManager1.FloatControl(Me.myUserControl21, New Rectangle(350, 350, 220, 260))

    Me.dockingManager1.DockControl(Me.myUserControl31, Me, DockingStyle.Right, 200)
    Me.dockingManager1.DockControl(Me.myUserControl11, Me.myUserControl21, DockingStyle.Bottom, 200)
End Sub

Private Sub GetDockingRelationship(ByVal dockedControl As Control)
    Dim targetControl As Control
    Dim statusMessage As String = String.Empty

    If TypeOf dockedControl.Parent Is DockHost Then
        Dim dockhost As DockHost = TryCast(dockedControl.Parent, DockHost)
        Dim dhc As DockHostController = TryCast(dockhost.InternalController, DockHostController)
        Dim baseController As DockControllerBase = dhc.DICurrent.dController

        If baseController IsNot Nothing Then
            If TypeOf baseController Is SizingController OrElse TypeOf baseController Is DockHostController Then

                If count <> dockedctrls.Count - 1 Then
                    targetControl =
                    baseController.HostControl.Controls(0)
                End If
            End If
        End If
    End If
End Sub
```

## API Reference (if applicable)
- `InitializeDockControlState()`: Initializes the docking state of user controls by floating and docking them in specific locations.
- `GetDockingRelationship(ByVal dockedControl As Control)`: Retrieves the docking relationship of a specified docked control.

## Code Examples (multi-language supported)
```csharp
// C# Example
while (ienum.MoveNext())
{
    dockedctrls.Add(ienum.Current);
}

foreach (Control dockedControl in dockedctrls)
{
    GetDockingRelationship(dockedControl);
    count = count + 1;
}
}
```

```vb
' VB.NET Example
Private Sub InitializeDockControlState()

    Me.dockingManager1.FloatControl(Me.myUserControl11, New Rectangle(250, 250, 220, 260))
    Me.dockingManager1.FloatControl(Me.myUserControl21, New Rectangle(350, 350, 220, 260))

    Me.dockingManager1.DockControl(Me.myUserControl31, Me, DockingStyle.Right, 200)
    Me.dockingManager1.DockControl(Me.myUserControl11, Me.myUserControl21, DockingStyle.Bottom, 200)
End Sub
```

<!-- tags: [syncfusion, winforms, windows forms, docking, controls, initialization, relationship] keywords: [InitializeDockControlState, GetDockingRelationship, docking, controls, float, dock, location, state] -->
```