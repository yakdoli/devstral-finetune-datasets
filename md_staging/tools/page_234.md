```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_234.jpeg
document_name: tools
page_number: 234
page_id: tools#page_234
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:52:08Z
fidelity: lossless
-->

## 3.4.3.8.10 InitializeControlOnLoad Event

The InitializeControlOnLoad event occurs when the DockingManager is not able to locate a control during a LoadDockState call.

### Event Data

The event handler receives an argument of type InitializeControlOnLoadEventArgs containing data related to this event. The following InitializeControlOnLoadEventArgs property provides information specific to this event.

| Member         | Description                                |
|----------------|--------------------------------------------|
| ControlName    | The Name property of the control.         |

### Code Example

```csharp
[C#]
protected void DockingManager_InitializeControlOnLoad(object sender, InitializeControlOnLoadEventArgs args)
{
    Console.WriteLine("InitializeControlOnLoad Event is Raised for the Control : " + args.ControlName);
    DockingManager dockingmgr = sender as DockingManager;
    switch (args.ControlName)
    {
        case "Suite Logo":
            this.ActivateSuiteLogoControl(dockingmgr, false);
            break;
        case "Suite Info":
            this.ActivateSuiteInfoControl(dockingmgr, false);
            break;
        case "Tools Info":
            this.ActivateToolsInfoControl(dockingmgr, false);
            break;
        case "Tools Logo":
            this.ActivateToolsLogoControl(dockingmgr, false);
            break;
        case "Grid Logo":
            this.ActivateGridLogoControl(dockingmgr, false);
            break;
        case "Grid Info":
            this.ActivateGridInfoControl(dockingmgr, false);
            break;
    }
}
```

<!-- tags: [Syncfusion Winforms, InitializeControlOnLoad, DockingManager, LoadDockState, Event, C#] keywords: [InitializeControlOnLoad, DockingManager, LoadDockState, Control, Event, C#] -->
```