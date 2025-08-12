```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_138.jpeg
document_name: common
page_number: 138
page_id: common#page_138
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:57Z
fidelity: lossless
-->

## Essential Common

### Overview
- This page provides instructions for generating localized strings and satellite assemblies using a .csv file for a WPF application.
- It explains the process of changing language settings from English to French for specific control-related texts.
- Instructions include creating and managing directory structures to handle localized resources effectively.

### Content

#### ResourceStrings.csv

The following table shows the contents of `ResourceStrings.csv`:

| Key | Type | Enabled | Value |
| --- | --- | --- | --- |
| Syncfusion.Tools.system:String\_1 | None | TRUE | TRUE | S\_how Quick Access Toolbar below the Ribbon |
| Syncfusion.Tools.system:String\_1 | None | TRUE | TRUE | \_Add &gt;&gt; |
| Syncfusion.Tools.system:String\_1 | None | TRUE | TRUE | \_Remove |
| Syncfusion.Tools.system:String\_1 | None | TRUE | TRUE | Re\_set |
| Syncfusion.Tools.system:String\_1 | None | TRUE | TRUE | \_Modify... |
| Syncfusion.Tools.system:String\_1 | None | TRUE | TRUE | \_Choose commands from |
| Syncfusion.Tools.system:String\_2 | None | TRUE | TRUE | Qui\_k Access Toolbar |
| Syncfusion.Tools.system:String\_2 | None | TRUE | TRUE | Remove from Quick Access ToolBar |
| Syncfusion.Tools.system:String\_2 | None | TRUE | TRUE | Calendrier |
| Syncfusion.Tools.system:String\_2 | None | TRUE | TRUE | Regarder |
| Syncfusion.Tools.system:String\_2 | None | TRUE | TRUE | aucun |
| Syncfusion.Tools.system:String\_2 | None | TRUE | TRUE | aujourd'hui |
| Syncfusion.Tools.AccessTodayTexButton | None | TRUE | TRUE |  |
| Syncfusion.Tools.AccessTodayTexNone | FALSE | TRUE | 0 |
| Syncfusion.Tools.AccessTodayTexNone | FALSE | TRUE | 40 |
| Syncfusion.Tools.CustomizeQATTText | TRUE | TRUE |  |
| Syncfusion.Tools.CustomizeQATT | None | FALSE | TRUE | 3,0,0,0 |
| Syncfusion.Tools.CustomizeQATT | None | TRUE | TRUE | Bold |
| Syncfusion.Tools.CustomizeQATT | None | FALSE | TRUE | Center |

**Note:** We have changed the language from English to French for Calendar control-related texts alone.

#### Steps to Generate Localized Satellite Assembly

1. **Modify the .csv file**: Update the `ResourceStrings.csv` file to include translations for the required strings.
2. **Generate the localized satellite assembly**: Use the modified .csv file to generate the satellite assembly for the application.
3. **Install the assembly**: Install the generated satellite assembly in your application.
4. **Open command prompt**: Navigate to the `en-US` directory.
5. **Create a directory for French (fr-CH)**: Under the `Bin\Debug` folder, create a new directory named `fr-CH` using the `md fr-CH` command.

##### Note
- The directory name should follow a proper culture name.

#### Generating Culturespecific Assembly

6. **Generate your own culture-specific assembly**: Use the following command from the `en-US` folder:
   ```bash
   LocBaml /generate /tran: resourceStrings.csv /out:../fr-CH /cul:fr-CH
   Syncfusion.Tools.WPF.Resources.dll
   ```

#### Verifying the Generated Assembly

- After running the command, verify that the satellite assembly is generated and is located under the `fr-CH` folder.

#### Running the Application with Localization

8. **Modify `App.xaml` to set the CurrentUICulture**: Update the `CurrentUICulture` property in the `App.xaml` file by setting it to `fr-CH`.

**Example C# Code**:
```csharp
public App()
{
    // Code omitted for brevity
}
```

### Conclusion

By following the steps outlined in this document, you can generate and install a localized satellite assembly for your WPF application. This ensures that the application displays the correct language-specific resources, enhancing user experience.

### Tags and Keywords
<!-- tags: [Localization, WPF, Satellite Assembly, Resource Files, Culture Support, Syncfusion Winforms] keywords: [ResourceStrings.csv, culture-specific assembly, fr-CH, en-US, LocBaml, CurrentUICulture, App.xaml] -->
```