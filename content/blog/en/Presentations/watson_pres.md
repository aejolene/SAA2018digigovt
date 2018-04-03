Title: Can you make me a map? Making Louisiana’s cultural resources records accessible
Date: 2018-04-03
Category: presentations
Tags: gis, sensitive-data
Slug: map-watson
Authors: Rachel Watson

[Rachel Watson](rwatson@crt.la.gov)


In October of 2004 the Louisiana Department of Culture, Recreation and Tourism, Office of Cultural Development (OCD) and the LA Department of Transportation and Development (DOTD) signed an interagency agreement to develop a comprehensive statewide cultural resources GIS system, the Louisiana Cultural Resources Map. The State Historic Preservation Office is part of OCD which house the Division of Archaeology (DOA) and Division of Historic Preservation (DHP). Staff constraints prevented an in-house development, so we hired a contractor. DOTD administered the contract. The requirements were that the firm hired would use the most current version of ArcView, ArcView SDE, and ArcView IMS to develop the system and the accompanying website and would have experience dealing with historic properties. A local Baton Rouge engineering firm, Gulf Engineers Consultants, Inc. hereafter referred to as GEC, Inc. won the contract.



We now maintain our desktop applications and website utilizing ESRI products. We have migrated the online map to ArcGIS online. To maintain the system, in the face of uncertain budgets, we have implemented a fee. The fee, $1300 for an annual subscription, is used to purchase hardware, storage, and maintain software maintenance.



## HISTORY OF THE PROJECT:


The project was to be completed in two Phases over the period of three years. Phase I consisted of two tasks: Task 1 - Digitization of site data, and Task 2 - Database and Web interface design and implementation. Much of Task 1 required on-site personnel and Task 2 required input and coordination with DOA, DHP, and DOTD personnel. Phase II consisted of scanning the archaeological site forms, the standing structure forms, and the cultural resources reports.



Before digitization, a geodatabase was created with four feature classes projected in UTM NAD 83 Zone 15 Meters. This data set was developed from a previous database; known as the Louisiana Computerized Archaeological Database (LACAD), which the DOA had created to keep track of our site file information and to be able to use this information to answer specific questions. The LACAD was a great help when we began the process of developing the geo-database since we had already identified what the DOA felt were important searchable criteria. Any of these categories are searchable.

For the completion of this task, GEC housed two employees as well as the required computer hardware and software on the premises of the DOA. Through scanning digitizing directly from the DOA map collection, GEC digitized approximately 17,000 archaeological sites into the three geodatabase feature classes. A state-wide set of DRGs in NAD 83 was used as a reference in digitizing. DRG, or digital raster graphic, is raster image of a scanned USGS standard series topographic map, usually including the original border information, referred to as the map collar, map surround, or marginalia. Source maps are georeferenced to the surface of the earth, fit to the universal transverse Mercator (UTM) projection, and scanned at a minimum resolution of 250 dpi.  The accuracy and datum of a DRG match the accuracy and datum of the source map. As sites were digitized, the trinomial site number was entered as a unique identifier.

Approximately 54,000 historic standing structure sites were digitized into point features. Historic Districts were saved as polygon features. For those structures with inadequate maps, their location was captured through a combination of scanning maps and digitizing from records, similar to the process for Archaeological sites. DHP had begun work on a database containing information regarding their standing structure information. For structures with existing database records, geocoding will be accomplished by importing existing databases into a tabular format (.dbf) compliant with the geocoding criteria. These steps include parsing the address, standardizing abbreviated values, assigning each address element to a category known as a match key, indexing the needed categories, searching the reference data, assigning a score to each potential candidate, filtering the list of candidates based on the minimum match score, and delivering the best match. The locations represented in the formatted tables were processed through the use of EZLocate geocoding software. Geocoded sites were checked for accuracy against the USGS and non-USGS maps and corrected as needed. Records that are not able to be geocoded required slight manipulation (e.g., modifying highway names/numbers, spellings). Sites that cannot be geocoded will be researched and digitized directly into the system. After all the sites are entered in digital format either by hand or through geocoding, the standing structure resource number will be entered as a unique identifier.

An inventory of any new archaeological sites and historic standing structures registered with DOA and DHP during the digitizing process will be conducted at the completion of the digitization process. These new sites will be checked and digitized in the final week of Task 1. This will ensure an up-to-date geodatabase. DHP and DOA personnel will be trained in data entry so that future updates can be conducted in-house.



It was planned that the geodatabases would undergo quality assurance/ quality control or (QA/QC) procedures on a weekly basis to determine accuracy and to accurately report progress. Progress reports were to be delivered to DOTD, DOA, and DHP on a biweekly basis. However, when Hurricane Katrina and Rita struck the Gulf coast in 2005 this procedure was not followed for a reason explained later in the paper.

With input from DOA and DHP, GEC attributed the feature classes of the geodatabase with relevant data from the site forms and standing structure forms. A hyperlink field was created in each feature class to attach scanned documents while completing document conversion or Phase II. Metadata is being completed for each feature class. Metadata is the information that describes the content, quality, condition, origin, and other characteristics of data or other pieces of information. Metadata for spatial data may describe and document its subject matter; how, when, where, and by whom the data was collected; availability and distribution information; its projection, scale, resolution, and accuracy; and its reliability with regard to some standard.

GEC used ArcIMS and .Net technology to create a secure web interface housed at the (DCRT). Queries were developed on categories specified by DOA and DHP. The Web site displays the cultural resources data over DRG Quad maps. Additionally, site numbers are displayed as the cursor passes over a site (similar to a “tool tip”); clicking on a site while its layer is active will display the site data; and clicking on the hyperlink field in a site’s data will access a scan of the original site forms or historic standing structure documents – as they become and available. We have since migrated the website to an ArcGIS online platform.



GEC scanned approximately 108,000 pages of standing structure forms, photos, and documents for DHP and 668,000 pages of reports and site forms for DOA as the remaining money permits. Working with CRT personnel, GEC will develop an indexing system to enable easy filing and retrieval of scanned documents. All scanned documents will then be indexed accordingly and entered into the appropriate hyperlink field created in Phase I, Task 2, Database Design and Web Interface.



The contract for GEC to begin work was signed during the first week of August 2005. On August 29, 2005, Hurricane Katrina made landfall on the Gulf Coast. Needless to say our priority for how to complete this project changed. We needed to digitize the most affected parishes as soon as possible so that the information was available for FEMA and NO-COE. Within a month Hurricane Rita also made landfall and the list of parishes that needed to be completed had increased. DOTD agreed to allow GEC to accelerate the project to meet the needs of recovery for the state. Due to staff constraints in both the DOA and DHP, this did not allow for the QA/QC process to go ahead as planned. This caused us to launch the website earlier than expected which caused several problems that will be discussed later in this paper.



We worked with the Federal Emergency Management Agency (FEMA) and the Louisiana Governor’s Office of Homeland Security (GOSHEP) to further supplement missing data and purchase hardware to maintain the Louisiana Cultural Resources Map. As part of an alternative mitigation measure for the Hazardous Mitigation Grant Program, we agreed that GOSHEP would purchase server equipment and FEMA would resurvey nine historic districts in New Orleans, survey City Park in New Orleans, and analyze archaeological collection from the University of New Orleans that had been impacted by the historic flooding.



We partnered with the New Orleans Corps of Engineers to digitize all the cultural resources management survey coverage. NO-COE had put aside money to digitize the survey coverage of all of their properties within the state. However, they realized that they had enough funds to create a survey coverage for the entire state. This was obviously beneficial for NO-COE to meet their Section 106 responsibilities.



## HOW THE SYSTEM WORKS:



There are two separate websites; the structures and historic district data, and the archaeological site and survey reports are in a password-protected website. The legend and layers list, print, and query (still being developed) function are in the title banner.



The search bar defaults to the address locator. However, the user can search for all the following categories; archaeological sites, reports, cities, and public survey lines. Search categories within archaeological includes; site number, name, parish, site components, characteristics, affiliation, function, material, and feature type. These characteristics were defined on our LACAD form available on the department website. Searchable categories for survey reports include; report number, title, author, and date.



Additional widgets on the site include the base map, add data, select tool, draw, and coordinate conversions. The base map widget allows the user to change the map view. The add data widget allows the user to upload a shapefile or kmz/kml. Furthermore, the add data widget give the user access to from ESRI AcrGIS Online content or a URL for another GIS service.  The select tool allows the user to select records within a geographic region. The draw tool is useful for measuring distances and drawing buffers around features. Finally, the coordinate conversion tool lets the user enter a coordinate in latitude/longitude or UTM.



The site contains a coordinate bar that tracks the geographic location of the mouse. The coordinate bar will default to show the latitude and longitude. You can place a point to get the UTM.



## Issues:



Since we had to change our strategy after the hurricanes, we launched the website before the geodatabases were complete. When we launched the website, GEC was still in the process of doing the data entry. Some sites had little more than geographical information in the database. Also, the task of scanning and hyperlinking the sites & standing structure forms was not complete. This required researcher to continue to visit the office until we completed the data entry



We did have problems that were not a result of the storms. Much of the information from the LACAD database was in code. We had to convert the code. Since you can select for numerous entries under the categories designated for the LACAD sheet, this means there has to be more than one field in the database. We migrated the data from Microsoft Access to SQL. Migrating the website to ArcGIS online solved the data query issues.



Another problem that we found in working with the archaeological data was the lack of information provided on site forms. Some of our site forms consist of little more than a circle on a map if we are lucky. In some instances, there are reports of a site somewhere within a Section, Township, and Range. In these cases, we included the record in the geodatabase, but they do not display on the online map.



We discovered that because we did not use a placeholder in our trinomial site identification number, it made indexing the scanned pdfs difficult. We had to re-index the geodatabase placeholder for the archaeological site forms to make the hyperlinks work.



As soon as we launched the website, many entities contacted us about obtaining the actual layer data; this posed an interesting problem for us. Although, the standing structure information is public, both State and Federal law protect the archaeological information. There are several things that we needed to consider. One, how do we protect this information once we have released it? Two, how often do we offer updates on this information? And three, do we charge a fee for the release of the information? We feel that data-share agreements will solve this problem. However, these agreements take time.



We did implement an annual fee of $1300 in 2017. The fee has allowed us to self-generate funds to pay for GIS software license renewals to maintain the system at the time of ever shirking budgets. Furthermore, we have used the money to continue training for the GIS staff to help maintain the system. We currently have twenty-six subscribers. Subscribers include federal agencies, state agencies, and CRM firms. Researchers and Native American tribes have free access to the system. Free access requires a research statement to document the use of the system falls within the fee exemption.



## FUTURE PROJECTS:



Currently, the access to the archaeological site information is restricted. We are planning to create maps that the general public can view without site-specific information. As part of other programmatic agreements as a result of Section 106 projects associated with hurricane recovery, archaeological probability maps are being created for New Orleans. We are hoping to incorporate these maps into our system as a management tool.



DOA and DOTD developed a driving trail to highlight thirty-nine mounds in Northeast Louisiana. The format is in a brochure form. We plan to convert the brochure into a driving story map formatted for tablets and phones. Furthermore, we plan to develop a story map of archaeological sites on public lands.

Finally, we are working to update the report and data submission standards to aid in maintaining an up to date system. Submission standards will include new media requirement and online site form submissions.



## CONCLUSIONS:



Creating a comprehensive GIS system can be a daunting task. However, we spent many hours in planning sessions to come up with what we felt is the best and most efficient way to implement this project. However, you know what they say about the best-laid plans. The partnering between state agencies to create a comprehensive system was very successful. Exploring partnership opportunities can be of great help to agencies with budget constraints.



Most of our responses to the system have been positive. CRM firms, State and Federal Agencies, and individuals with GIS experience have found the system easy to use. We believe we have developed a powerful tool to make well-informed decisions concerning cultural resource management.
