<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">project_title</h3>

  <p align="center">
    The Assignment

    **🌐 Relational Databases & API Rest Development Project | Building an E-commerce API with Flask, SQLAlchemy, Marshmallow, and MySQL**

### **OVERVIEW**

In this assignment, you will create a **fully functional e-commerce API** using Flask, Flask-SQLAlchemy, Flask-Marshmallow, and MySQL. The API will manage **Users, Orders, and Products** with proper relationships, including **One-to-Many** and **Many-to-Many** associations. You will also learn to set up a MySQL database, define models, implement serialization with Marshmallow, and develop RESTful **CRUD endpoints**.

---

## **🎯 LEARNING OBJECTIVES**

* **Database Design:** Create models with relationships in SQLAlchemy and MySQL.  
* **API Development:** Develop a RESTful API with CRUD operations using Flask.  
* **Serialization:** Use Marshmallow schemas for input validation and data serialization.  
* **Testing:** Ensure the API is fully functional using Postman and MySQL Workbench.

---

💬 **Project Presentation Reminder**  
As part of your final deliverables for this module, you’ll also give a short presentation of your project. This can be done live during a [weekly Q\&A session](https://codingtemple.disco.co/events/UHJvZHVjdEFwcDoyNzQwMTU=?calendarTab=upcoming), recorded and submitted to Google Classroom, or shared directly with your Student Success Manager. If you'd like to schedule a 1-on-1 presentation, [click here to book a time](https://scheduler.zoom.us/d/nsl-rf0v/software-engineering-1-on-1-presentations).  
---

## **🗂 RELATIONSHIPS**

* **One User → Many Orders (One-to-Many):** A user can place multiple orders.  
* **Many Orders ←→ Many Products (Many-to-Many):** An order can contain multiple products, and a product can belong to multiple orders. (This will require an **association table**.)

Review Lesson 3: Intro to ORM’s to help set up your database models with the appropriate relationships.

---

## **🔧 REQUIREMENTS**

### **Set Up MySQL Database**

1. Open **MySQL Workbench**.  
2. Create a new database named ecommerce\_api.

### **Install Dependencies and Initialize Flask App**

Set up a virtual environment:

```py
python3 -m venv venv
```

**Activate the virtual environment:**

**Mac/Linux:** source venv/bin/activate

**Windows:** venv\\Scripts\\activate

**Install dependencies:**

```py
pip install Flask Flask-SQLAlchemy Flask-Marshmallow marshmallow-sqlalchemy mysql-connector-python
```

### **Configure App with Database URI**

Update the **SQLAlchemy URI** in your app.py file:

```py
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:<YOUR PASSWORD>@localhost/ecommerce_api'
```

---

## 

## **🗃 DATABASE MODELS**

Create the following tables in SQLAlchemy:

### **User Table**

* **id:** Integer, primary key, auto-increment  
* **name:** String  
* **address:** String  
* **email:** String (must be unique)

### **Order Table**

* **id:** Integer, primary key, auto-increment  
* **order\_date:** DateTime (learn to use **DateTime** in SQLAlchemy)  
* **user\_id:** Integer, foreign key referencing User

### **Product Table**

* **id:** Integer, primary key, auto-increment  
* **product\_name:** String  
* **price:** Float

### **Order\_Product Association Table**

* **order\_id:** Integer, foreign key referencing Order  
* **product\_id:** Integer, foreign key referencing Product

Ensure this **association table** prevents duplicate entries for the same product in an order.

---

## **📦 MARSHMALLOW SCHEMAS**

Implement the following Marshmallow schemas for serialization and validation:

* **UserSchema**  
* **OrderSchema**  
  * **IMPORTANT:** SQLAlchemyAutoSchemas do not automatically recognize Foreign Keys as schema fields, and won’t recognize user\_id.  
  * To include user\_id as part of the schema you must add include\_fk \= True as a property in the Meta subclass under the model attribute.  
* **ProductSchema**

Include appropriate fields and validation for each schema.

## **🚀 IMPLEMENT CRUD ENDPOINTS**

Develop the following **RESTful endpoints**:

### **User Endpoints**

* **GET /users**: Retrieve all users  
* **GET /users/\<id\>**: Retrieve a user by ID  
* **POST /users**: Create a new user  
* **PUT /users/\<id\>**: Update a user by ID  
* **DELETE /users/\<id\>**: Delete a user by ID

### **Product Endpoints**

* **GET /products**: Retrieve all products  
* **GET /products/\<id\>**: Retrieve a product by ID  
* **POST /products**: Create a new product  
* **PUT /products/\<id\>**: Update a product by ID  
* **DELETE /products/\<id\>**: Delete a product by ID

### **Order Endpoints**

* **POST /orders**: Create a new order (requires **user ID** and **order date**)  
* **PUT /orders/\<order\_id\>/add\_product/\<product\_id\>**: Add a product to an order (prevent duplicates)  
* **DELETE /orders/\<order\_id\>/remove\_product**: Remove a product from an order  
* **GET /orders/user/\<user\_id\>**: Get all orders for a user  
* **GET /orders/\<order\_id\>/products**: Get all products for an order

---

## **🧪 TESTING**

* **Run Database Setup:** Ensure that calling db.create\_all() creates all required tables in MySQL.  
* **Use Postman:** IMPORTANT In Postman create a Collection and add a request for each of your API endpoints to the collection. Then export the collection and include it in your project folder as shown [here](https://www.loom.com/share/7fe9acc1589448ce87b2f49274e3753a)  
* **Verify Data:** Use **MySQL Workbench** to ensure data is being correctly stored in the database.

---

## **📋 DELIVERABLES**

Submit a **Python script** containing:

* Database models for **Users, Orders, Products,** and **Order\_Product** association.  
* Fully functional CRUD endpoints for **users, products, and orders**.  
* Validated and serialized data using **Marshmallow schemas**.

---

## **🚀 BONUS TASKS (Optional):**

* Add **additional endpoints** for advanced order management.  
* Implement **pagination** for user or product listings.  
* Add **JWT authentication** for user operations.

---

## **📥 HOW TO SUBMIT**

* Submit your completed **Python script** via Google Classroom in a GitHub Repository.  
* Ensure all endpoints are functional, and data is correctly stored in MySQL.

---

## **📊 ASSESSMENT CRITERIA (100%)**

| Criteria | Weight | Description |
| ----- | ----- | ----- |
| **Database Models** | 30% | Proper setup of models with relationships. |
| **API Functionality** | 40% | Fully functional CRUD endpoints for all resources. |
| **Serialization & Validation** | 20% | Correct use of Marshmallow schemas. |
| **Code Quality** | 10% | Clean, organized code with comments. |

## 

## **📚 RESOURCES**

* [Flask Documentation](https://flask.palletsprojects.com/en/stable/)  
* [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.readthedocs.io/en/stable/)  
* [Marshmallow Documentation](https://marshmallow.readthedocs.io/)  
* [MySQL Connector Documentation](https://dev.mysql.com/doc/connector-python/en/)


    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    &middot;
    <a href="https://github.com/github_username/repo_name/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/github_username/repo_name/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started. To avoid retyping too much info, do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`, `project_license`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/github_username/repo_name/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=github_username/repo_name" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the project_license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
