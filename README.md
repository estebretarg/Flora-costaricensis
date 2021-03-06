# Flora-costaricensis

Flora costaricensis is a professional botanical identification tool for mayor vascular plant species present in Costa Rica.

It was designed for botanists, dendrologists, forestal engineers, agronomists or other plant related fields.

This tool intend to help researchers and other environmental sciences professionals to complete or advance projects faster. Accelerating the conservation efforts and at the same time contributing to the environmental agenda. Also it will be a great learn tool for students.

Imagine make a forestall inventory in a fraction of a time with an accurate census of species. 

It is an easy to use tool with interactive and settable dichotomous keys based on the descriptions and keys from the "Manual de Plantas de Costa Rica" ("Handbook of the Plants of Costa Rica") <a href= "README.md/#Bibliography:" target = "_self">*refer to bibliography</a>* 

# Desired features:
<ul>
  <li>Settable workspaces based on parameters (elevation, humidity, life zone, family, genus, ...etc.).</>
  <li>Main "global" environment to explore all plants from Costa Rica.</>
  <li>Select a species and track the hierarchy (inverse search).</>
  <li>Pin favorite species and store them on customizable file sets.</>
  <li>Include extensive and detailed characteristics for each species.</>
  <li>If the species has cultural or industrial usages it will be marked whit an icon-based symbology.</>
  <li>Attach own photos to the species and compare them with global public data bases.</>
  <li>Make geo-references when you successfully identify a specie with the app contributing to the distribution maps</>
</ul>
  If you are interested in suggest more features please contact me from the contact information on my Github profile.
  
# Challenges:
<ul>
  <li>The species names are changing constantly due to advanced ADN research.</>
  <li>Financial support: We need to find interested institutions who can support the project and get recognition of the public as green-nature interested companies.</>
</ul>

# Methodology:

Species are stored in an SQLite database distributed in different tables deppending on the species Division.

Division:

<ul>
  <li>Gimonspermas</>
  <li>Angiospermas</>
</ul>

Each table include the next columns:

<table>
  <tr>
    <th>Family</th>
    <th>Genera</th>
    <th>Species</th>
    <th>Description</th>
    <th>Life_zone</th>
    <th>Elevation</th>
    <th>Slope</th>
  </tr>
</table>

****The elevation is stored as a range of values between the first value and the second value available in the book.***

# Legal Disclaimers:

All legal related matters are pending, if you are interested in collaborate in legal matters please contact me on the channels provided on my Github profile.

# Bibliography:

  Hammel, B. E., Troyo, S., & Garden., M. B. (2010). Manual de plantas de Costa Rica. Missouri Botanical Garden Press.
