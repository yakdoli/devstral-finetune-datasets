```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_087.jpeg
document_name: HTMLUI
page_number: 087
page_id: HTMLUI#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:39Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

```csharp
return new Script();
}
public Script()
{
    if (Global.Document == null)
    {
        MessageBox.Show("Document is NULL");
        return;
    }
}
button = Global.Document.GetElementByUserId("btn");
img = Global.Document.GetElementByUserId("img");
button.Click += new EventHandler(button_Click);
}
public void button_Click(object sender, EventArgs ar)
{
    img.Attributes["src"].Value = "sync.jpg";
}
</script><br/>
</body>
</html>
```

### 4.6.23 SELECT - Select Tag

The `Select` tag is used to create a drop-down list of options that can be selected by the user to give some input to the application. The `select` tag in HTMLUI supports the following attributes that improve the usage of the application.

- **size**: Specifies the number of items to be displayed in the select control in the document.
- **disabled**: Displays a disabled list box in which no items can be selected.

---

### HTML

#### File Location and Name: C:\MyProjects\select\select.html

```html
<html>
    <body>
        <p>
            Essential Studio includes ten component libraries in one great package. Each of these products has a unique and useful feature set.
        </p>
        <select size="2">
            <option>Essential Tools</option>
            <option>Essential Chart</option>
            <option>Essential Grid</option>
            <option>Essential HTMLUI</option>
        </select>
    </body>
</html>
```

---

## API Reference (if applicable)

Namespace: `Essential.HTMLUI`
- Class: `Select`
  - Attributes:
    - **size**: Specifies the number of items to be displayed.
    - **disabled**: Indicates if the list box is disabled.

## Code Examples

1. **C# Example**
   ```csharp
   public void PopulateSelect()
   {
       List<string> options = new List<string> { "Option 1", "Option 2", "Option 3" };
       
       foreach (string option in options)
       {
           SelectOption(option);
       }
   }
   
   private void SelectOption(string option)
   {
       // Add logic to update the selection based on user input.
   }
   ```

2. **JavaScript Example**
   ```javascript
   document.addEventListener("DOMContentLoaded", function() {
       const selectElement = document.getElementById("select-id");
       selectElement.addEventListener("change", function() {
           console.log("Selected option:", selectElement.value);
       });
   });
   ```

---

## Cross References

See also:
- [HTMLUI Drop-Down Controls Documentation](#)
- [Dynamic Dropdown Binding in HTMLUI](#)

---

<!-- tags: [Essential HTMLUI, Select Tag, Dropdown List, Disabled Attribute, List Box, Windows Forms, Syncfusion] keywords: [Select, attributes, size, disabled, dropdown, options, user input, dynamic binding, HTMLUI, WinForms] -->
```