<p align="center"><img src="https://img.shields.io/badge/Gantt_Chart-Link-blue?link=https%3A%2F%2Fcebuinstituteoftechnology-my.sharepoint.com%2F%3Ax%3A%2Fg%2Fpersonal%2Fmarckramon_paraiso_cit_edu%2FESvHrUMQAIdOkJQLlvvrR14BBPw7taN_yPC4nf0f02SzAA%3Fe%3DO2NJAX" alt="shields"> <img src="https://img.shields.io/badge/Figma-Link-red?link=https%3A%2F%2Fwww.figma.com%2Fdesign%2FnyYnjGlbCABuGWIPmFymka%2FCSIT327---IM2%3Fnode-id%3D0-1%26t%3DBPofXEUuE6bjK9Jm-1" alt="shields"></p>


<h1 align="center" id="title">Inventory Management</h1>

<p id="description">Members: Paraiso Gabison Bustamante</p>

____________________ 

 

A Project Proposal 

Presented to the Department of College of Computer Studies 

Cebu Institute of Technology University 

Cebu City, Philippines 

____________________ 

In Partial Fulfillment 

of the Requirements for the Subject 

Information Management 2 

____________________ 

Prepared by: 

Paraiso, Marck Ramon G. 

Gabison, Andrei Mighel A. 

Bustamante, William. 


August 2024

Inventory Management System

This document features the functional Requirements for the Inventory Management System (IMS). This outlines the important features and capabilities the System itself must have to meet the needs/requirements of the inventory managers, warehouse staff, and business administrators effectively.

Functional Requirements Table Illustration:

These functional requirements outline the important and essential features needed for  the Inventory Management System (IMS). The System focuses on delivering a Minimum Viable Product that serves as a foundation for further development. As the project progresses, these requirements may be refined, changed or expanded based on the system’s needs and any new requirements that may need to be added.




Functional Requirements Table:

| Task  | Function                       | Description                                                                 | Priority | Inputs                       | Outputs               |
|-------|---------------------------------|-----------------------------------------------------------------------------|----------|------------------------------|-----------------------|
| T1    | User Authentication and Access  | Secure login process for authorized access.                                 | High     | - Username                   | “Access Granted/Denied!” |
|       | Control                         |                                                                             |          | - Password                   |                       |
| T2    | Product Catalog Management      | Allows creation, management, and categorization of products in a catalog.    | High     | - Product Name               | “Updated Product Catalog!” |
|       |                                 |                                                                             |          | - SKU                        |                       |
|       |                                 |                                                                             |          | - Category                   |                       |
| T3    | Stock Level Tracking            | Monitors and updates stock levels for accurate inventory counts.             | High     | - Returns                    | Alerts (low stock)     |
|       |                                 |                                                                             |          | - Incoming stock             |                       |
|       |                                 |                                                                             |          | - Current Stock Levels       |                       |
| T4    | Export Data                     | Allows exporting of data in Excel/CSV format.                               | Low      | - Inventory Data             | Excel/CSV file         |
| T5    | Manual Order Management         | Allows manual creation and tracking of purchase orders.                     | High     | - Order Date                 | “Orders Created/Updated” |
|       |                                 | Includes details like order date, supplier, and status.                     |          | - Supplier                   |                       |
|       |                                 |                                                                             |          | - Items                      |                       |
| T6    | Search                          | Allows searching for a specific item in the inventory.                      | Medium   | - Item name                  | - Item                |
