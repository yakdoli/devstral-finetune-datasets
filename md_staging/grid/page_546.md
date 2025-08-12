```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_546.jpeg
document_name: grid
page_number: 546
page_id: grid#page_546
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:43Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### 4.2.2.1 Binding to an ArrayList

You can bind an ArrayList that holds objects with public properties. Given below is an example, which substantiates this point.

1. We first define an object called **Person** with two public properties: **FirstName** and **LastName**.
2. We then create an **ArrayList** holding a collection of these objects.
3. To bind this ArrayList to a Grid Data Bound Grid, we set the grid's **DataSource** property after dropping a Grid Data Bound Grid onto the form.

Given below are the code samples for this.

```csharp
[C#]

// Create the Person object class.
public class Person
{
    private string lname;
    private string fname;

    public Person(string fname, string lname)
    {
        this.fname = fname;
        this.lname = lname;
    }

    public string FirstName
    {
        get { return fname; }
        set { fname = value; }
    }

    public string LastName
    {
        get { return lname; }
        set { lname = value; }
    }
}

// Code within your Form Load event handler.
private void Form1_Load(object sender, System.EventArgs e)
{
    ArrayList al = new ArrayList();
    al.Add(new Person("John", "Smith"));
}
```

## API Reference (if applicable)

## Code Examples (multi-language supported)

- **C# Example:**
  ```csharp
  [C#]

  // Create the Person object class.
  public class Person
  {
      private string lname;
      private string fname;

      public Person(string fname, string lname)
      {
          this.fname = fname;
          this.lname = lname;
      }

      public string FirstName
      {
          get { return fname; }
          set { fname = value; }
      }

      public string LastName
      {
          get { return lname; }
          set { lname = value; }
      }
  }

  // Code within your Form Load event handler.
  private void Form1_Load(object sender, System.EventArgs e)
  {
      ArrayList al = new ArrayList();
      al.Add(new Person("John", "Smith"));
  }
  ```

## Page-level Navigation/TOC (if applicable)

## Cross References

### See also:

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```