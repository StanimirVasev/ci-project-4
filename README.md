# **CamShop** #

![Image of site on many screens](/media/readme_images/site_responsive_image.png)

## **Introduction** ##

CamShop was created and built by Stanimir Vasev as final milestone project for Code Institute. The website is a Django e-commerce website for a leading provider of high-quality cameras and accessories. Users of the site are able to purchase camera equipment whether they have registered or checkout as a guest. Registered users however benefit from more access to certain features on the site such as having order history in their profile section.

<hr>

## **Table of contents** ## 

### **1. User Experience** ###
* 1.1 Target audience 
* 1.2 User stories
* 1.3 Design choices
* 1.4 Wireframes
* 1.5 Database Design

### **2. Features** ###
* 2.1 Homepage 
* 2.2 Top header
* 2.3 Navbar
* 2.4 The Shop Page
* 2.5 Product Details
* 2.6 Product Review
* 2.7 The Profile
* 2.8 The Shopping Bag
* 2.9 The Checkout Page
* 2.10 Purchase Complete
* 2.11 Stripe 
* 2.12 Sign Up and Emails
* 2.13 Login
* 2.14 Toasts

### **3. Technologies/Languages Used** ###
* 3.1 Gitpod/Github
* 3.2 HTML5
* 3.3 CSS
* 3.4 JavaScript
* 3.5 JQuery
* 3.6 Python
* 3.7 Django
* 3.8 Bootstrap 
* 3.9 Google fonts
* 3.10 Font Awesome
* 3.11 Favicon Generator
* 3.12 Stripe 
* 3.13 Heroku
* 3.14 Canva Pro

### **4. Testing** ###
* 4.1 Testing
* 4.2 Development Issues

### **5. Deployment** ###
* 5.1 Deployment and cloning

### **6. Credits** ###
* 6.1 Media
* 6.2 Code 
* 6.3 Acknowledgements

### **7. Future Features To Develop** ###
* 7.1 - Social media login
* 7.2 - Social media share buttons
* 7.3 - Paypal Payment Option
* 7.4 - Wishlist
* 7.5 - Sort by price functionality
* 7.6 - Dark Mode
* 7.7 - Shopping Cart

### **8. Disclaimer** ###
* 8.0 Disclaimer on project

<br>
<hr>

<details>
<summary><strong>
1. User Experience (UX)
</strong></summary>
<br>

#### **1.1 - Target Audience** ####

* The target audience for CamShop includes:

* Photography Enthusiasts and Hobbyists: Individuals who are passionate about photography and seek high-quality cameras, lenses, and accessories to enhance their hobby.

* Professional Photographers: Experienced professionals looking for advanced equipment and accessories to meet their specific needs for various photography genres.

* Photography Students and Amateurs: Those who are learning photography and require reliable, user-friendly gear and educational resources to develop their skills.

* Tech-Savvy Consumers: People interested in the latest photography technology and innovations, including both new and seasoned buyers keen on staying updated with industry trends.

* Blog Readers: Individuals seeking valuable insights, tips, and tutorials related to photography through our blog.

* This diverse audience in the UK values high-quality products, expert advice, and a supportive community to assist them in their photography pursuits.

<hr>

#### **1.2 - User Stories** ####

* The main aim of the site is to educate photography enthusiasts and experts and sell them various types of camera equipment. Users who search for, and come to the site are already involved in photography, they just need to educate themselves on latest equipment and trends before they can make a purchase. Therefore the website aims to provide smooth buying experience with as few barriers as possible from product view to taking payment. 


The site functionality will allow users to search and view all of the products on the site in detail, proceed straight to  checkout where they can to complete the order if they so wish. The site also offers features that are only available to registered users such as the profile page which displays the order history information. While the site offers features that are only available to logged in users, it will not lose sales by forcing people to register to complete a purchase.<br><br>

* <strong>User story - Site Owner</strong><br>

* I want to be able to offer my customers a wide range of of camera equipment - camera bodies, lenses, optical accessories, bateries and more.

* I want to be able to manage all of the items that my store sells myself so i can: Add, edit, update and remove different items quickly and easily depending on how they are selling.

* I want to offer my customers a simple, efficient and user friendly shopping experience so they come back and purchase from the site again.

* I want to offer educational content on photography topics such as Portrait, Wildlife, Night photography and more information on the latest camera equipment available on the market.

* I want to encourage my users to register so they can save their details and streamline the purchasing process for next time. This will allow me to build a customer database and analyse buying trends and also allow me to email them personalised content to bring them back to the store.

* I want to provide guest users the ability to purchase from the store without registration so the store doesn’t lose any potential sales.

#### **1.2 - User Stories** ####

* The site includes easy navigation, various product and blog categories and subcategories to search and view with a few clicks and contact information to make it easier for the user to get in touch with the store owner. The website has clean but interactive design to ensure users can find their desired products or information quickly but still feel engaged by interacting with the visual elements. <br><br>

* <strong>User story - Site User</strong><br>

* I want to be able to search for and view all of the products in the store in a easy manner.

* I want to be able to browse multiple products but also review individual products and their details such as price, product description, product review by specialist, stock availability, rating, and a product image.

* I want to be able to register for an account quickly and effortlessly so that I can have a personal profile if I become a frequent user.

* I want to log in and out with ease so that I can manage my account securely with just a few clicks.

* I want to easily recover my password if I forget it so that I can regain access to my account without hassle.

* I want to access my profile at any time so that I can view my order history and details.

* I want to be able to easily adjust the quantity of a product once I decide to purchase it so that I can add more items to my cart with just a few clicks.

* I want to be able to experience a quick and simple checkout process so that I can complete my purchase efficiently, even if I choose not to register for an account.

* I want to be able to fully review and adjust my cart before proceeding to checkout so that I can add or remove products and correct quantities if needed.

* I want to be able to see a detailed order confirmation after completing my purchase so that I can verify that all aspects of my order are correct.

* I want to be able to view my order history in my registered account so that I can review past orders and details whenever I need.

* I want to feel secure about the safety of my payment information.


* I want to be able to keep track of my purchases at any time on the site so i can: keep track of the value of goods in my cart so i can avoid spending to much money

<hr>

#### **1.3 - Design Choices** ####
<br>

**FONTS**

* For the website i decided to use the google font style of Lato as it is a clean, modern, and highly legible typeface that enhances the overall readability and aesthetic of the site. Its versatility makes it suitable for various types of content and ensures a consistent and professional look throughout the website.


**ICONS**

* I have integrated icons throughout the website to enhance user experience by making it more intuitive and engaging. All the icons used are sourced from Font Awesome, ensuring a high-quality and consistent design across the site.

**COLOURS**

* In the design of the CamShop website, I've used a palette that emphasises clarity and style. The primary colours include:

* Black (#000): Utilised for buttons, text, and borders, providing a strong contrast and modern aesthetic.
* Orange (#FFA500): Used for overlay, highlights, button hover effects, and background colours to create vibrant accents and draw attention.
* White (#FFFFFF): Applied as the background colour for various elements to ensure readability and a clean appearance.
* Grey (#555): A softer text colour for general content to reduce strain and enhance readability.

* Additional styling includes various shades of grey for borders and shadows to create depth and separation between elements. These colours work together to create a cohesive and visually appealing experience across the site.


**IMAGES**

* Most of the images used on the CamShop website were sourced from Canva Pro, ensuring a professional and consistent visual style. For camera product images, I have sourced high-quality visuals from [Photosynthesis](https://magazin.photosynthesis.bg/).
<hr>

#### **1.4 - Wireframes ** ####
<br>

* The wire frames for the site can be found here: 

<hr>

#### **1.5 - Database Design** ####
<br>

* Django works with SQL databases by default, I used SQLite during development. Heroku provides a PostgreSQL database for deployment. Below you can find all of the models used in this project and also a visualization of the database schema and its relationships and structure.<br>

* **The Database Schema**

* **Models Overview**

<strong>Products/Models/`Product`:</strong>

* class Product:
    * category: ForeignKey (Category, null=True, blank=True, on_delete=SET_NULL)
    * subcategory: ForeignKey (Subcategory, null=True, blank=True, on_delete=SET_NULL)
    * sku: CharField (max_length=254, null=True, blank=True)
    * name: CharField (max_length=254)
    * description: TextField
    * price: DecimalField (max_digits=6, decimal_places=2)
    * rating: DecimalField (max_digits=6, decimal_places=2, null=True, blank=True)
    * image_url: URLField (max_length=1024, null=True, blank=True)
    * image: ImageField (null=True, blank=True)
    * stock_status: BooleanField (default=True, verbose_name='In Stock')

<strong>Products/Models/`Category`:</strong>

* class Category:
    * name: CharField (max_length=254)
    * friendly_name: CharField (max_length=254, null=True, blank=True)

<strong>Products/Models/`Subcategory`:</strong>

* class Subcategory:
    * category: ForeignKey (Category, null=True, blank=True, on_delete=SET_NULL)
    * name: CharField (max_length=254)
    * friendly_name: CharField (max_length=254, null=True, blank=True)

<strong>Reviews/Models/`ProductReview`:</strong>

* class ProductReview:
    * review_title: CharField (max_length=90)
    * reviewed_product: ForeignKey (Product, on_delete=CASCADE, related_name='reviews')
    * reviewer: ForeignKey (UserProfile, on_delete=CASCADE)
    * review: TextField (max_length=500)
    * date: DateTimeField (auto_now_add=True)

<strong>Products/Models/`UserProfile`:</strong>

* class UserProfile:
    * user: OneToOneField (User, on_delete=CASCADE)
    * default_phone_number: CharField (max_length=20, null=True, blank=True)
    * default_street_address1: CharField (max_length=80, null=True, blank=True)
    * default_street_address2: CharField (max_length=80, null=True, blank=True)
    * default_town_or_city: CharField (max_length=40, null=True, blank=True)
    * default_county: CharField (max_length=80, null=True, blank=True)
    * default_postcode: CharField (max_length=20, null=True, blank=True)
    * default_country: CountryField (blank_label='Country', null=True, blank=True)

<strong>Checkout/Models/`Order`:</strong>

* class Order:
    * order_number: CharField (max_length=32, editable=False)
    * user_profile: ForeignKey (UserProfile, on_delete=SET_NULL, null=True, blank=True, related_name='orders')
    * full_name: CharField (max_length=50)
    * email: EmailField (max_length=254)
    * phone_number: CharField (max_length=20)
    * country: CountryField (blank_label='Country *')
    * postcode: CharField (max_length=20, null=True, blank=True)
    * town_or_city: CharField (max_length=40)
    * street_address1: CharField (max_length=80)
    * street_address2: CharField (max_length=80, null=True, blank=True)
    * county: CharField (max_length=80, null=True, blank=True)
    * date: DateTimeField (auto_now_add=True)
    * delivery_cost: DecimalField (max_digits=6, decimal_places=2, default=0)
    * order_total: DecimalField (max_digits=10, decimal_places=2, default=0)
    * grand_total: DecimalField (max_digits=10, decimal_places=2, default=0)
    * original_bag: TextField (default='')
    * stripe_pid: CharField (max_length=254, default='')

<strong>Checkout/Models/'OrderLineItem':</strong>

* class OrderLineItem:
    * order: ForeignKey (Order, on_delete=CASCADE, related_name='lineitems')
    * product: ForeignKey (Product, on_delete=CASCADE)
    * quantity: IntegerField (default=0)
    * lineitem_total: DecimalField (max_digits=6, decimal_places=2, editable=False)

<strong>Blog/Models/'BlogCategory':</strong>

* class BlogCategory:
    * name: CharField (max_length=254)
    * friendly_name: CharField (max_length=254, null=True, blank=True)

<strong>Blog/Models/'Post':</strong>

* class Post:
    * title: CharField (max_length=254)
    * friendly_title: CharField (max_length=254, blank=True)
    * body: TextField
    * created_on: DateTimeField (auto_now_add=True)
    * blog_categories: ForeignKey (BlogCategory, on_delete=CASCADE, related_name="posts")
    * image_url: URLField (max_length=1024, null=True, blank=True)
    * image: ImageField (null=True, blank=True)

<hr>

<details>
<summary><strong> 2. Features </strong></summary>
<br>

#### **2.1 - Homepage** ####

* The homepage of CamShop greets visitors with a warm message: "Welcome to CamShop!" It introduces the ease of purchasing professional photography equipment from anywhere in the UK effortlessly.

* The page features two main sections:

  * The Shop Section showcases photography gear with a compelling image, inviting users to explore CamShop's extensive range. It caters to both seasoned professionals and enthusiastic amateurs, providing them with the perfect camera options. Users can easily navigate to view all products through a dedicated link.

  * In the Learn Section, users are encouraged to enhance their photography skills through educational content. This section offers valuable insights into camera equipment and photography techniques. Users can access a diverse array of blog posts covering tips and techniques by navigating to the blog list page.

<hr>

#### **2.2 - Top header** ####

* The top header provides key features for a streamlined user experience:

* Search: A search icon is prominently displayed, allowing users to easily search for products. Tapping this icon opens a search form where users can enter their queries and find relevant products.

* User Account: A user icon provides quick access to account-related options. Depending on the user's authentication status, this includes links to register or log in for new users, and for authenticated users, options to view their profile, log out, or access management features for products and blogs if they are superusers/admins.

* Cart: A cart icon displays the current total amount of items in the user's shopping bag. If there are items in the cart, the total amount is shown; otherwise, it indicates that the cart is empty.

<hr>

#### **2.3 - The Navbar** ####

* * The desktop navigation menu offers a comprehensive browsing experience:

* Main Menu: This includes links to the homepage and a range of product categories. Each category has a dropdown menu that lists related subcategories such as Zoom Lenses, Optical Accessories, Beginner Cameras and more, allowing users to browse products more specifically. There is also an option to view all products or sort them by price, rating, or category.

* Blog Categories: A dedicated dropdown menu for blog categories helps users access various blog topics such as Portrait, Wildlife and Night photography. This menu includes links to individual blog categories as well as an option to view all blog posts.

* Search: A search feature is integrated into the navigation menu, enabling users to search for products directly from the header.

* User Account: Authenticated users have access to account management options. Superusers can access additional management features for products and blogs. All users can view their profile or log out. Unauthenticated users can register or log in from the same menu.

* Cart: The navigation includes a cart icon that shows the total amount in the shopping bag, providing users with easy access to their cart status.

* On mobile devices the navbar shrinks and can be opened if you click on the hamburger icon on the top left of the page. After clicking all of the items will again be visible for the user to navigate the site. 

<hr>

#### **2.4 - The Products Page** ####

* The Products page provides a comprehensive view of all available items, allowing users to easily browse and find what they are looking for. At the top of the page, users will see a header that dynamically displays the category or subcategory they are currently viewing. If no specific category or subcategory is selected, it defaults to "All Products."

* Users have the option to sort products based on several criteria. The sorting dropdown allows them to choose from options such as price (low to high or high to low), rating (low to high or high to low), name (A-Z or Z-A), and category (A-Z or Z-A). The current sorting selection is highlighted to make it clear what criteria is being used.

* The page displays products in a grid format, with each product showcased in a card layout. Each product card includes an image, name, price, and rating. If available, the product image is displayed; otherwise, a placeholder image is used. Users can view product details by clicking on the product image or the "View details" button. For users with administrative rights, options to edit or delete products are also available directly from the product card.

* Below the product listings, the page includes pagination controls to navigate through multiple pages of products. Users can move between pages using "Previous" and "Next" buttons and select specific page numbers.

* A "Back to Top" button is included for user convenience, allowing users to quickly return to the top of the page.

* Additionally, the page includes JavaScript functionality for sorting and page navigation, ensuring a smooth and interactive browsing experience.

<hr>

#### **2.5 - Product Detail Page** ####

* The Product Detail page provides in-depth information about a specific product, allowing users to make informed purchasing decisions.

* At the top of the page, the product’s image is prominently displayed. If the product has an image, it is shown in high resolution and can be clicked to view in a larger format. If no image is available, a placeholder image is displayed instead.

* To the right of the product image, users can find detailed information about the product. This includes the product's name, price, and rating. If a rating is available, it is shown alongside the average rating score. Users are also informed about the product's stock status, indicating whether it is "In Stock" or "Out of Stock."

* For administrative users, additional options are provided to edit or delete the product.

* The product description offers a detailed overview of the product’s features and specifications. Users can also add the product to their shopping bag directly from this page. They can specify the quantity they wish to purchase using an input field with increment and decrement buttons. If the product is out of stock, the "Add to Bag" button is disabled, and the button's label reflects the stock status.

* Below the product details, there is a section dedicated to specialist reviews. If reviews are available, they are displayed with details such as the reviewer’s name, review date, title, and content. If no reviews are present, a message indicates that reviews will be added soon.

* The page also includes a "Keep Shopping" button, which allows users to return to the product listings and continue browsing.

<hr>

#### **2.6 - Add Product Page** ####

* The Add Product page allows administrators to add new products to the store’s catalogue. This page is accessible only to users with appropriate permissions, ensuring that only authorised personnel can manage product listings. 

* At the top of the page, there is a simple header section, maintaining consistency with the rest of the site. The main content area is structured to provide a user-friendly interface for adding new products. The page title "Product Management" and the subtitle "Add a Product" clearly indicate the purpose of the page. 

* The form is designed with a focus on simplicity and clarity. Each field from the form is rendered using Django’s crispy forms for a clean and consistent look. The form includes fields for all necessary product information, except for the image field which is handled separately for better visual feedback. 

* When an image is uploaded, a JavaScript snippet provides feedback by displaying the name of the selected file. 

* At the bottom of the form, there are two buttons: Cancel, which takes the user back to the products page without saving any changes, and Add Product, which submits the form and adds the new product to the catalogue. 

* A small JavaScript function updates the UI to show the name of the selected image file, providing immediate feedback to the user about the chosen image.

<hr>

#### **2.7 - Edit Product Page** ####

* The Edit Product page allows administrators to update the details of existing products in the store’s catalogue. This page is designed to be intuitive, ensuring that authorised users can easily make necessary changes to product listings. 

* Similar to the Add Product page, the header section provides a consistent look and feel with the rest of the site. The content area focuses on providing an efficient interface for editing product details. The page title "Product Management" and the subtitle "Edit a Product" clearly communicate the page’s purpose. 

* The form is populated with the current details of the product, allowing users to see existing information and make necessary changes. The form includes fields for all editable product information. 

* Like the Add Product page, the image field is handled separately. A JavaScript snippet provides visual feedback by displaying the name of the selected file.

* At the bottom of the form, there are two buttons: Cancel, which takes the user back to the products page without saving any changes, and Update Product, which submits the form and updates the product details in the catalogue. 

* A JavaScript function updates the UI to show the name of the selected image file, providing immediate feedback to the user about the chosen image.

The Add and Edit Product pages ensure that product management tasks are straightforward, reducing the chances of errors and enhancing the efficiency of store administration.

<hr>

#### **2.7 - Add Review Page** ####

* The Add Review page allows authenticated users, specifically administrators, to leave reviews for products. This page is designed to ensure that only authorised users can provide feedback, maintaining the integrity of the reviews on the website. At the top of the page, there is a white background overlay with a banner that prominently displays the text "Add a Review." The banner is styled to catch the user’s attention and clearly indicate the page’s purpose.

* For authenticated users, the main content area provides a user-friendly form for submitting reviews. The form is styled with clarity and simplicity in mind, using Django’s crispy forms for a consistent look. The form includes all necessary fields for a review, such as the review title, content, and rating. There is a pre-filled, disabled input field displaying the current user’s username to remind the user that they are logged in and their review will be associated with their account. Below the form, there are two buttons: a Cancel button that redirects the user back to the products page without saving any changes and a Submit Review button that submits the form and saves the review.

* If the user is not authenticated, the page displays a message informing them that only admin users are allowed to leave reviews. This section provides a clear explanation and includes a button that redirects unauthenticated users to the login page, encouraging them to log in if they have the necessary permissions.

* This structure ensures that only authorised reviews are submitted, maintaining the quality and trustworthiness of the feedback on the website.

<hr>

#### **2.8 - Profile Page** ####

* The Profile page allows users to view and update their personal information, specifically their default delivery details, and also review their order history. The page is designed to be user-friendly and informative, offering a seamless experience for users to manage their account details.

* The layout starts with a header container, followed by an overlay to provide a clear background for the main content. The main content is divided into two primary sections: Default Delivery Information and Order History.

* In the Default Delivery Information section, users can update their personal details. This section includes a form that is rendered using Django’s crispy forms for consistent styling. The form contains various fields for the user to input their delivery information. At the bottom of the form, there is a centrally aligned Update Information button, allowing users to submit their changes. This form is processed through the POST method to ensure that any updates are securely sent to the server.

* The Order History section provides a detailed view of the user’s past orders. This section includes a responsive table that lists all previous orders. Each row in the table contains the order number (with a link to more detailed order information), the date of the order, a list of items in the order, and the total cost of the order. The order items are displayed in a nested list format to keep the table organised and easy to read.

* Overall, the Profile page is designed to be functional and accessible, ensuring that users can easily update their delivery information and track their order history in a clear and organised manner.

<hr>

#### **2.8 - Bag/Cart Page** ####

* The Bag/Cart page provides users with a detailed overview of their selected products, allowing them to review, update, or remove items before proceeding to checkout. It features a clean and organised layout with essential functionalities for a smooth shopping experience.

* The page begins with a header container, followed by an overlay that serves as a background for the main content. The main content section is structured into several rows and columns for optimal organisation and readability.

* The page features a messages section to display any success messages, such as item additions or updates, using a Bootstrap alert component.

* If there are items in the user's bag, the items are displayed in a responsive table. Each table row represents a product and includes the following details: 

  * Product image: A thumbnail of the product with a fallback image if none is available. 
  * Product information: 
    * Name and SKU of the product. 
    * Price: Unit price of the product. 
    * Quantity: An input field allowing users to adjust the quantity of the product. This section includes buttons to increment or decrement the quantity. 
    * Subtotal: Calculated price based on the product quantity.

* Users can update the quantity of a product by clicking the "Update" link, which submits a form to adjust the quantity. They can also remove an item from their bag by clicking the "Remove" link, which triggers an AJAX request to delete the item and refresh the page.

* Below the product table, the page displays a summary of the bag's total cost, including the bag total, delivery cost, and grand total. If the user is close to qualifying for free delivery, a message is displayed indicating how much more they need to spend.

* At the bottom of the page, users can choose to continue shopping by clicking the "Keep Shopping" button or proceed to checkout by clicking the "Secure Checkout" button.

* If the user's bag is empty, a message is displayed along with a "Keep Shopping" button, encouraging users to browse the products.

* The page also includes a JavaScript block to handle form submissions for updating quantities and removing items, ensuring a smooth and interactive user experience. The included script for quantity input management is provided through a separate template, enhancing modularity and maintainability.

<hr>

#### **2.8 - Checkout Page** ####

* The Checkout page provides a seamless and efficient way for users to finalise their purchases. It includes an order summary and a form for entering delivery and payment details. 

* The page starts with a container for the header, followed by an overlay that serves as a background for the main content. The main content is structured into rows and columns for better organisation and readability.

* The order summary section is displayed on the right for larger screens and on top for smaller screens. It shows the number of products and includes the following details for each item: 

* Product image with a link to the product detail page, product name and quantity, and subtotal calculated based on the product quantity. 

* Below the product list, a summary of the order total, delivery cost, and grand total is provided.

* The left column (or the bottom section on smaller screens) contains the checkout form, which includes fields for user details and delivery information. The form is organised into fieldsets for clarity: 

  * Details (full name and email), 
  * Delivery (phone number, street address, town or city, county, postcode, and country). 
  * If the user is authenticated, there is an option to save the delivery information to their profile.

* The payment section includes a placeholder for a Stripe card element and fields to handle potential errors. The form also includes a hidden input field to pass the client secret for payment processing. At the bottom of the form, there are buttons for adjusting the bag and completing the order. A message indicates the total amount that will be charged to the user's card.

* A loading overlay is included to indicate processing during the checkout process. JavaScript is used to handle the Stripe payment integration and provide a responsive and interactive user experience. The Stripe public key and client secret are included via Django template tags. The script for managing the Stripe elements is loaded from a static file.

<hr>

#### **2.9 - Checkout Success Page** ####

* The layout ensures the user receives a clear, comprehensive summary of their order and provides easy navigation options post-purchase.

* Depending on how the user arrived at the checkout success page, there is either a button to return to the profile page or a button to explore more products.

<hr>

#### **2.10 - Blogs Page** ####

* This page showcases a collection of blog posts in a grid layout. Each blog post is represented by a card that includes an image, the title, and the blog category if assigned. 

* Users can view more details by clicking on either the image or the "Read more" button. 

* For administrators, there are additional options to edit or delete posts, which are only visible to users with superuser permissions.

* The blog posts are displayed with responsive design elements, ensuring a seamless viewing experience across different screen sizes. 

* The page includes pagination controls to navigate between multiple pages of blog posts. 

* Additionally, a "Back to Top" button is provided for user convenience, allowing easy navigation back to the top of the page.

<hr>

#### **2.11 - Blog Details Page** ####

* The blog detail page offers a comprehensive view of an individual blog post. At the top, the page prominently displays the title of the blog post, providing clear identification of the content. 

* Below the title, information such as the publication date and the blog's category are shown, giving context to the post. 

* If the user has administrative privileges, additional links are provided to either edit or delete the post, facilitating content management directly from the page.

* The main content area features the full text of the blog post, presented with rich formatting to preserve its structure and style. This allows readers to engage with the post's content in its entirety. 

* Additionally, a button at the bottom of the page provides an easy way to navigate back to the main blog list, allowing users to continue browsing other posts seamlessly. 

* This setup ensures that readers can fully explore and interact with individual blog posts while maintaining easy access to the broader collection of blog entries.

<hr>

#### **2.12 - Blog Category Page** ####

* The blog category page displays a collection of blog posts that belong to a specific category. At the top of the page, the category name is prominently shown, followed by a horizontal rule for visual separation.

* The page then lists the blog posts in a grid format, with each post displayed in a card layout. 

* Each card includes an image representing the post, which links to the detailed view of the post. If a post does not have an associated image, a default image is shown. 

* Below the image, the title of the post is displayed, and further details, including the category and edit/delete links (for superusers), are provided.

* If no posts are available within the selected category, a message is shown indicating the absence of posts. 

* Additionally, the page includes pagination controls to navigate through multiple pages of posts if there are more posts than can fit on a single page. A button for returning to the top of the page is also available to enhance navigation.

<hr>

#### **2.13 - Add Blog Page** ####

* Similar like the Add Product page, the add blog page allows users to create and submit a new blog post. At the top, there is a section for the page header that includes a heading and a subtitle indicating the purpose of the page.

The main content area contains a form for adding a new blog post. This form includes fields for entering blog details such as the title, content, and category. Users can also upload an image to accompany the blog post. Each form field is rendered using Django's crispy forms for consistent styling. There is an option to cancel the form submission and return to the blog list or submit the form to add the new blog post.

* The page includes a script that updates the displayed file name when a new image is selected, helping users confirm the image they are uploading.

<hr>

#### **1.14 - Edit Blog Page** ####

* Similar to the Edit Product page, the edit blog page is designed for users to modify an existing blog post. It starts with a page header that includes a title and subtitle, indicating the page's purpose.

* In the content area, the user is presented with a form pre-filled with the current details of the blog post. The form allows users to update various fields such as the title, content, and category, as well as upload a new image if desired. Each field is rendered individually, and there is a label associated with each input for clarity.

* At the bottom of the form, users have the option to either cancel their changes and return to the blog post details page or submit the form to update the blog post. There is also a JavaScript function that updates the displayed file name when a new image is selected, providing feedback on the file being uploaded.

<hr>

#### **2.15 - Toasts** ####

* Toast notifications serve to provide users with feedback on their actions or system statuses in a non-intrusive manner. They briefly display important messages or updates and are designed to be visually distinctive based on the context, such as success, warning, error, or informational messages.

* A success toast indicates a successful action or operation, showing a "Success!" message with a green highlight and a white background. The body of the toast details the successful outcome and includes additional information such as a summary of recently added items in a shopping bag, their total cost, and options for proceeding to checkout. It features a call-to-action button to guide users to secure checkout if relevant.

* A warning toast alerts users to potential issues or actions needing attention. It displays a "Warning!" message. The content warns users about what they need to be cautious of or what action they should take.

* An error toast notifies users of problems or failed actions, with an "Error!" message highlighted in red. This toast clearly conveys that something has gone wrong. The body provides details about the error, helping users understand what went wrong and suggesting possible resolutions.

* An info toast provides general updates or information. It displays an "Info" message. The content gives users updates or changes that are not urgent but still important, using a different background to differentiate it from success, warning, and error messages.

* All toasts include a close button allowing users to dismiss the notification manually. They also feature custom styling to ensure visual consistency and includes additional content based on user actions, such as details of a shopping bag or specific error messages.

<hr>

#### **2.16 - Sign up and real email notifications via gmail ** ####

* To become a registered user, individuals can complete the sign-up process quickly and easily. Start by clicking the 'My Account' icon in the top right corner of the page on desktop or in the top row on mobile. From the dropdown menu, select 'Register.'

* On the sign-up page, users will be required to provide their email address, create a unique username, and set a password of their choice. The form includes validation checks to ensure all required fields are filled in. If any fields are missing, a pop-up will appear indicating which fields need to be completed.

* If a user attempts to register with an email address or username that is already in use, they will receive a notification when trying to submit the form, informing them that the email or username is already taken.

* Once the form is completed with valid details, users will be notified that an email has been sent to the address they provided. They must then verify their email by clicking the link included in the email. After clicking the link, the user will be directed to a confirmation page on the site, where they need to click the 'Confirm Email Address' button. Following confirmation, the user will be redirected to the login page.

<hr>

#### **2.17 - Login page ** ####

* The login page is designed to be straightforward. Users need to enter their username or email address and their password to access their account. Both fields are required, and the form will not submit unless the details are entered correctly.

* Additional features on the login page include the "Remember Me" option, which allows users to stay logged in without needing to re-enter their details in future sessions. There is also a "Forgot Password" link for users who need to recover their password. By clicking this link, users are prompted to enter their email address, and reset instructions will be sent to them. If a user lands on the login page without an account, a notice will direct them to register.

* Upon clicking the "Forgot Password" link, users will receive an email with instructions on how to reset their password. Following the link in the email will direct them to a page where they can enter a new password.

<hr>

#### **2.18 - Stripe Integration ** ####

* This project integrates Stripe to handle payment processing, fulfilling a key requirement of the MS4 project. Once users have completed their shopping and added items to their cart, they proceed to the checkout page. At this stage, a payment intent is created in the Stripe dashboard, which is visible in the Stripe events section.

* Upon submitting their details in the checkout form and passing validation checks, users click the "Pay Now" button If the payment is successfully processed, users are directed to an order confirmation page that provides a detailed breakdown of their order.

* In the Stripe dashboard, key events related to the payment are tracked. Each event captures crucial data, including the amount charged, billing address, and contact details. Additionally, metadata includes the shopping bag item IDs, quantities, and whether the user has opted to save their delivery address information. For anonymous users (those who are not registered or logged in), this information is also reflected in the metadata.

* The shipping address is another vital piece of information captured by Stripe. Currently, the project uses the same address for both shipping and billing.

* Webhooks are used in this project to manage scenarios where users may close their browser either intentionally or unintentionally after placing an order and pressing the "Pay Now" button. In such cases, webhooks ensure that the order is still recorded in Django and all payment details are sent to Stripe. This mechanism helps prevent situations where a user is billed but does not receive their items, ensuring a smooth and reliable transaction process.

<hr>

#### **2.19 - Footer** ####

* The footer provides essential information and navigation for users. 

* It includes an "About Us" section that describes the company and its mission to deliver high-quality cameras and accessories. 

* The "Contact Us" section lists the company’s address, phone number, and email address. 

* The "Follow Us" section features social media icons linking to the company’s profiles on platforms like Facebook, Twitter, Instagram, and YouTube. 

* At the bottom, there is a copyright notice for the current year, indicating that all rights are reserved. The design features a dark background with white text for clarity and contrast.

<hr>

#### **2.20 - Future Developments** ####

* Analytics and Monitoring: To better understand user behaviour and improve site performance, future updates will include the integration of advanced tracking and analytics tools. These tools will monitor user interactions, page performance, and site errors, providing valuable data that can be used to make informed, data-driven improvements to the site.

* User Feedback Mechanism: A user feedback mechanism will be introduced to allow users to provide feedback or report issues directly through the site. By offering options for users to share their experiences and concerns, we will gather valuable insights, enabling prompt responses to user needs and continuous enhancement of the user experience.

* Documentation and Support: Comprehensive documentation will be developed to support both users and administrators. This will include FAQs, troubleshooting guides, and detailed contact information for technical support. These resources will ensure users have access to the necessary information to navigate and resolve any issues they encounter, while also providing clear guidance for administrators managing the site.

* Company Pages: Additional company pages will be created to enhance transparency and engagement. These will include an "About Us" page to provide information about the company, a "Our Culture" page to showcase the company's values and work environment, and a "Careers" page to outline job opportunities and career development within the company. These pages will help build a stronger connection with users and potential employees by highlighting the company's mission, culture, and career prospects.

<details>
<summary><strong>
3. Technologies/Languages Used
</strong></summary>
<br>

* 3.1 - [Gitpod](https://www.gitpod.io/)
* 3.2 - [HTML5](https://html.com/html5/#What_is_HTML)
* 3.3 - [CSS](https://en.wikipedia.org/wiki/CSS)
* 3.4 - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* 3.5 - [JQuery](https://jquery.com/)
* 3.6 - [Python](https://www.python.org/)
* 3.7 - [Django](https://www.djangoproject.com/)
* 3.8 - [Bootstrap](https://getbootstrap.com/)
* 3.9 - [Google fonts](https://fonts.google.com/)
* 3.10 - [Font Awesome](https://fontawesome.com/)
* 3.11 - [Favicon](https://favicon.io/favicon-generator/)
* 3.12 - [Stripe](https://stripe.com/)
* 3.13 - [Heroku](https://www.heroku.com/)

</details>
<hr>

<details>
<summary><strong>
4. Testing
</strong></summary>

<br>

#### **4.1 Testing** ####

* Testing information can be found below:

<details>
<summary><strong>
1. Automated Testing
</strong></summary>
<br>

#### **1.1 HTML Code Validating** ####

* All of the HTML files were tested on the [W3C HTML Markup Validation website](https://validator.w3.org/)<br>
* The results from the test were as follows:<br>

**Warning that appears on all pages** 

* The HTML checker reports an error due to a duplicate id of "user-options". However, this issue is not a problem and can be disregarded. The id "user-options" appears in both the base.html file, which is used for the desktop version, and the mobile-top-header.html file, which is used for the mobile version. Despite having the same id, these elements serve the same function but are specific to different device views. This duplication does not impact the site's functionality. I have included this note in the README to acknowledge awareness of the issue.<br>

**1 Homepage (home/templates/home/index.html)**

* Apart from the duplicate-id error at the top of this section, all the HTML passes with no errors.

* Initially, I had this warning but I have fixed it: 

* Warning: The type attribute is unnecessary for JavaScript resources. <script type="text/javascript">

**2. Products page (products/templates/products/products.html)**

* Apart from the warning duplicate-id error and JS warning, the rest of the HTML has no errors. JS warning was fixed.

**3. Product details (products/templates/products/product_details.html)**

* Apart from the warning duplicate-id error and JS warning, I had 3 Errors: Unclosed element div. and 1 Fatal Error for unclosed form. I fixed those issues and now the html template has no other issues left.

**4. Bag/Cart (bag/templates/bag.html)**

* Apart from the warning duplicate-id error and JS warning, the rest of the HTML has no errors. JS warning was fixed.

**5. Checkout (checkout/templates/checkout.html)**

* Apart from the warning duplicate-id error, JS warning, and 1 warning for empty h1 for my spinner. the rest of the HTML has no errors. JS warning was fixed and I replaced the h1 with div instead and added text to fix the issue.

**6. Checkout Success (checkout/templates/checkout_success.html)**

* Apart from the warning duplicate-id error and JS warning, the rest of the HTML has no errors. JS warning was fixed.

**7. Blog (blog/templates/blog.html)**

* Apart from the warning duplicate-id error, JS warning, and 1 extra unnecessary div, the rest of the HTML has no errors. JS and div warning were fixed.

**8. Blog Detail (blog/templates/blog_detail.html)**

* Apart from the warning duplicate-id error and JS warning, the rest of the HTML has no errors. JS warning was fixed.

**9. Blog Category (blog/templates/blog_category.html)**

* Apart from the warning duplicate-id error and JS warning, the rest of the HTML has no errors. JS warning was fixed.

**10. Add Product (products/templates/add_product.html)**

* Apart from the warning duplicate-id error and JS warning, the rest of the HTML has no errors. JS warning was fixed. 

* There was another Error: Element p not allowed as child of element strong in this context. but as this was coming from custom_widget_templates/custom_clearable_file_input.html come that I copy/pasted, I didn't want to break the code. I would have replaced the paragraph with a div.

**11. Add Blog (blog/templates/add_blog.html)**

* Apart from the warning duplicate-id error and JS warning, the rest of the HTML has no errors. JS warning was fixed. 

**12. Edit Product (products/templates/edit_product.html)**

* Apart from the warning duplicate-id error and JS warning, there were 4 more errors. 

* Error: An img element must have an alt attribute, except under certain conditions. As this error is related to the images that are added from AWS, I am unsure how to add alt text. 

* Info: Trailing slash on void elements has no effect and interacts badly with unquoted attribute values. - I removed  the trailing slash from br.

* The other 2 errors were coming from custom_widget_templates/custom_clearable_file_input.html come that I copy/pasted, I didn't want to break the code. I would have replaced the paragraph with a div.

* JS warning was fixed. 

**12. Edit Blog (blog/templates/edit_blog.html)**

* Apart from the warning duplicate-id error and JS warning, the rest of the HTML has no errors. JS warning was fixed. 


**13. Signup (templates/allauth/account/signup.html)**

* Apart from the warning duplicate-id error and JS warning, the rest of the HTML has no errors.

**13. Login (templates/allauth/account/login.html)**

* Apart from the warning duplicate-id error and JS warning, the rest of the HTML has no errors.

**13. Profile (profiles/templates/profile.html)**

* Apart from the warning duplicate-id error and JS warning, I had 2 more errors caused by a need for an extra closing div. The errors were as listed below but were fixed. JS warning was fixed as well.

* Error: End tag for body seen, but there were unclosed elements.

* Error: Unclosed element div.

<hr>

#### **1.2 CSS Code Validating** ####

* The main CSS files were tested on the [W3C CSS  Validation website](https://jigsaw.w3.org/css-validator/)<br>

* I tested base.css first and got a message 'Congratulations! No Errors Found. This document is validated as CSS level 3 + SVG !'

* I tested profile.css second and got a message 'Congratulations! No Errors Found. This document is validated as CSS level 3 + SVG !'

* I tested checkout.css third and got a message 'Congratulations! No Errors Found. This document is validated as CSS level 3 + SVG !'

<hr>

#### **1.3 JavaScript Code Validating** ####

* The testing for the script.js file was carried out on [JShint.com](https://jshint.com/) The results from the test were as follows:<br>

**1. bag/templates/bag/bag.html**

* Tested the JS in bag template which gave me 7 warnings, I fixed 1 missing semicolon but the rest of the code. Unfortunately, I couldn't figure out how to fix the rest of the warnings as Jshint was showing them on the first script element.

* For reference, the six warnings are listed below:
Expected an identifier and instead saw '<'.
Expected an assignment or function call and instead saw an expression.
Missing semicolon.
Expected an assignment or function call and instead saw an expression.
Unclosed regular expression.
Unrecoverable syntax error. (100% scanned).

**2. products/templates/products.html**

* Tested the JS in products template which gave me 6 warnings, I fixed 1 missing semicolon but the rest of the code. Unfortunately, I couldn't figure out how to fix the rest of the warnings as Jshint was showing them on the first script element.

Five warnings
1	Expected an identifier and instead saw '<'.
1	Expected an assignment or function call and instead saw an expression.
1	Missing semicolon.
5	Unclosed regular expression.
5	Unrecoverable syntax error. (17% scanned).

**3. products/templates/products/includes/quantity_input_script.html**

* Tested the JS in quantity_input_script which gave me 8 warnings, I fixed 2 missing semicolon but the rest of the code. Unfortunately, I couldn't figure out how to fix the rest of the warnings as Jshint was showing them on the first script element.

**4. templates/base.html**

* Tested the JS in base.html which gave me 6 warnings, Unfortunately, I couldn't figure out how to fix the warnings as Jshint was showing them on the script element.

Six warnings
1	Expected an identifier and instead saw '<'.
1	Expected an assignment or function call and instead saw an expression.
1	Missing semicolon.
2	Expected an assignment or function call and instead saw an expression.
3	Unclosed regular expression.
3	Unrecoverable syntax error. (100% scanned).

**5. stripe_elements.js file**
* Tested the JS in stripe_elements.js which gave me multiple warnings about undefined variables 

* However, as this code is taken from the Stripe official documentation it appears to be correct so i have noted this here. 

**6. country_field.js file**

* Tested the JS in country_field.js which gave me multiple warnings about undefined variables. Unfortunately, it wasn't something I could fix and it seems like the code is working correctly.

<hr>

#### **1.4 Python Code Validating** ####

* The testing for the python files were carried out on [CI Python Linter](https://pep8ci.herokuapp.com/) The results from the test were as follows:<br>

* Webhooks_handler.py has 4 warnings, however, i left the code here as it has to do with Stripe's official documentation.

93: E501 line too long (80 > 79 characters)
94: E501 line too long (80 > 79 characters)
125: E501 line too long (103 > 79 characters)
164: E501 line too long (89 > 79 characters)

* Webhook.py had 1 warning, however, i left the code here as it has to do with Stripe's official documentation.

43: E501 line too long (86 > 79 characters)

* All of the other python code has passed the pep8 checks. I have used flake8 and fixed a wide range of issues. There are however some lines of code that showed up as needing tweaking. Some of these items from Flake8 i have ignored, the reason for each of these can be found below:

* ./reviews/views.py:36:13: F841 local variable 'e' is assigned to but never used - Reason: When I remove the variable 'e', flake8 is satisfied but pep8 CI linter gives me an error saying that I shouldn't use bare except.

* Certain lines in the settings.py file exceed 79 characters, as indicated. However, these lines were generated automatically when the project was created and reflect Django's default settings. As these settings were not manually written by me, I will be disregarding these particular warnings and will not modify them, as they were automatically configured.

* For the Files: /.vscode/arctictern.py, ./blog/migrations/0001_initial.py, ./checkout/migrations/0001_initial.py, ./products/migrations/0001_initial.py, ./profiles/migrations/0001_initial.py, ./reviews/migrations/0001_initial.py:

* Some lines in these files exceed 79 characters. These files include automatically generated code, especially migration files created by Django and configuration files. As these files are auto-generated and not manually written by me, I will not be adjusting them or addressing these specific warnings.


</details>
<hr>

<details>
<summary><strong>
2. Manual Testing
</strong></summary>
<br>

#### **2.1 Manual testing desktop** ####

* All desktop testing was carried out on Chrome.

**1. Homepage testing**

* The homepage renders as expected, with no layout issues.
* Clicking the 'CamShop' logo correctly returns the user to the homepage.
* When the search bar is used without any input, it navigates the user to the "All Products" page and displays a toast error message as designed.
* All dropdown menus expand properly upon clicking and display the correct submenu options.
* Each option in the dropdown menus has been tested, and all links direct the user to the intended pages.
* The images on the "Shop" and "Learn" cards show up as intended.
* The links on the "Shop" and "Learn" cards function correctly and lead to the appropriate destinations.
* The footer is displayed accurately, and users can contact the site owner or interact with the social media icons without issues.

**2. Account, Profile, Add Blog and Add Product**

* Clicking the "My Account" icon and selecting the "Sign Up" option correctly directs users to the sign-up page.
* I have tested the sign-up process with multiple emails. New user accounts were successfully created as expected.
* Clicking the "My Account" icon and choosing the "Log In" option properly navigates users to the log-in page.
* If a user enters an incorrect username or password, the page reloads with a warning message stating: "The username and/or password you specified are not correct."
* If a user submits the log-in form with only the username or password, validation messages prompt them to complete all required fields.
* When attempting to create an account with an already used email address, users receive an error message indicating that the email address is associated with another account.
* Users can click the "Forgot my password" link, enter their email address, and receive a password reset link. The reset email, including the username and link, is sent as expected.
* I have successfully logged in and out of accounts multiple times, with the correct toast notifications confirming login and logout appearing in the top right corner.
* Upon logging in, users can view their profile page and order history as expected on all browsers.
* As an admin, you can see 'My Profile', 'Blog Managemenet' and 'Product Management' under My Account. All links work as expected and the admin can add new blogs or products successfully. If they don't select an image, a placeholder image will be displayed.
* Clicking on a past order number on the profile page correctly opens and displays the order details.
* When the cart is empty, clicking the cart button shows the message "Shopping cart is empty" and provides a link to visit the store.
* Attempting to bypass an empty cart by typing "checkout" in the URL redirects users to the products page with a warning toast indicating that the cart is empty.

**3. Products Page**

* The products page accurately displays all available items for sale. Users can click on the navigation and get different categories or filter such as filter by price.
* The layout adjusts appropriately when resizing the screen, ensuring a consistent experience across all browsers.

**4. Product Details Page**

* Product details are displayed correctly and consistently across all browsers.
* If a user attempts to set the quantity to 0 and add the item to the cart, a validation error is shown, indicating that the minimum quantity allowed is 1.
* Users can add items to the cart as expected by selecting a quantity and clicking the "Add to Cart" button.
* Users can see the specialist review that was added by the admin or get a placeholder message if the admin hasn't added one yet.
* Users can click on 'Keep shopping' button and be redirected to all products page.

**5. Bag/Cart Page**

* If a user accesses the cart with no items, they will see a message indicating the cart is empty and will be given an option to return to the store.
* When items are added to the cart, users can adjust the quantity and update the cart, with changes accurately reflected across all browsers.
* Pressing the remove button successfully removes items from the cart.
* Clicking the secure checkout button directs the user to the checkout page.

**6. Checkout Page**

* The checkout page displays correctly and automatically populates the logged-in user's delivery address.
* Orders placed using Stripe test card details have been successfully processed on.
* People can see the total cost of their bag/cart.


**7. Confirmation Page**

* After placing an order, the order confirmation page is generated and displayed correctly, with all order details accurately shown. The order history is also added in My Profile section.

**8. Blog Page**

* The blog page displays correctly, showcasing four blog cards per row as intended.
* Each blog card includes an image, text, category, and other relevant details.
* Admin users can see and use the edit and delete buttons on each blog card to manage content.

**9. Blog Category Page**

* The blog category page correctly displays the heading indicating the selected category along with "Blog."
* The page shows the appropriate categories and lists blog posts relevant to the selected category.

**10. Blog Detail Page**

* The blog detail page loads correctly, displaying the heading, category, and full text of the blog post.
* For admins, the page provides "Edit" and "Delete" buttons.
* The blog post details include title, published date, category, and content.

<hr>

#### **2.1 Manual testing mobile** ####
<br>

* To reduce repetition of the desktop results, for the mobile testing i have just highlighted the different functionalities that mobile users may experience while using the site on a mobile device. I have carried out all of the exact same manual tests on mobile devices as i did on the desktop.

Mobile testing was carried out on the following devices:<br>
1. iPhone SE/12 Pro (Via Chrome Dev Tools)
2. iPad Air (Via Chrome Dev Tools)

**1. iPhone 12 Pro**

* On shopping bag/cart page, the quantity selector works but covers the number of units you have. All links work correctly but this could be improved.
* On blog detail page, the header appears quite big sometimes depending on how long the copy is. Font size could be reduced based on certain situations where copy is too long. Also, there is quite a bit whitespace at the bottom between reviews and footer. This could be improved.
* Everything else works as expected.

**2. iPhone SE**

* Icons in the navigation aren't properly aligned with hamburger icon. This could be improved.
* On shopping bag/cart page, the quantity selector works but covers the number of units you have. All links work correctly but this could be improved.

**3. iPad Air**

* Font is quite small on blog body and product description. This could be enlarged to improve user readability and experience.

</details>
<hr>

<details>
<summary><strong>
3. Responsiveness
</strong></summary>
<br>

**3.1 Chrome Dev Tools**
* I have tested the site’s responsiveness using Google DevTools, covering screen sizes from a maximum of 1870px x 767px down to a minimum of 320px x 480px. The site performs as expected across all tested dimensions.

</details>
<hr>

#### **3.2 Development Issues** ####
<br>

* SECRET_KEY Issue

* When I began building the project, I started making commits to GitHub but realised that I had exposed my secret_key value to github. I have removed this key and created a new one with django secret_key generator I found on Google. I then stored all my variables in Gitpod and Heroku. I then replaced the secret key with this code in settings.py: `SECRET_KEY = os.environ.get('SECRET_KEY')`. The new SECRET_KEY is secured and no longer exposed and the old one has been discarded. 
<hr>

**2. Stripe Webhooks**

*In my Stripe webhooks, I was constantly encountering 4 out of 4 errors but I found the Stripe debugging PDF in Slack and watched the lecturer's video and I managed to get 3 out of 4. I struggled for a bit to realise how to get 4 out of 4 and I spoke with my mentor to test this functionality together. After inspecting the flow, he reassured me that everything is working correctly as we are getting the order pid in Django admin and the payment in Stripe.

**3. Mobile Navbar Icons**

* During mobile testing, I discovered that on smaller screen sizes, the navbar icons were being pushed down onto a separate line. This occurred on mobile devices with smaller screens.

* The issue was caused by the text, icons, and padding being too large for the smaller screen sizes.


**4. Shopping cart/bag quantity selector**

* During mobile testing, I discovered that the quantity selector works fine but doesn't display well and hides the unit box on smaller screens. Media query has to be updated for smaller screens.

</details>

<hr>

<details>
<summary><strong>
5. Deployment
</strong></summary>
<br>

#### **Deployment to Heroku and Cloning Instructions** ####

* Below are the following steps i undertook to deploy the site to Heroku. If you are looking to clone this project and work on it you can follow the step by step guide below as it details every step i took to deploy to Heroku. Cloning from the repository instructions are found below the Heroku and AWS instructions below. 

1. Navigate to the Heroku website [Here]( https://www.heroku.com/)

2. Give your app a name and select the region closest to you. Once completed, click the "Create App" button.

3. Click on the "Resources" tab and type "Postgres" in the add-ons search bar. Select "Heroku Postgres" from the results. A pop-up will open; choose the "Hobby Dev - Free" plan and click "Provision."

4. Navigate back to Gitpod and install the following packages:<br>
`pip3 install dj_database_url`  
`pip3 install psycopg2-binary`

5. Freeze your requirements.txt file with:<br> 
`pip3 freeze > requirements.txt`

6. In settings.py, add: `import dj_database_url`

7. Update the DATABASES section in settings.py. Comment out the default configuration and insert:<br>
`DATABASES = {`<br>
`'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))`<br>
`}`

You can find your DATABASE_URL in your Heroku Config Vars. Warning: DATABASE_URL is an environmental variable and should not be shown in version control, so ensure you don't push this to GitHub.</strong></em>

8. You need to make all migrations but first, view the migrations with:`python3 manage.py showmigartions`

9. Then run: `python3 manage.py migrate`

10. After migration, upload all the products for the store again with:<br>
`python3 manage.py loaddata categories`<br>
`python3 manage.py loaddata subcategories`
`python3 manage.py loaddata products`

It is crucial to load categories first, as all products fall into a category. In my project, I used 3 fixtures files stored in my products app.

11. Create a superuser to log in with: `python3 manage.py createsuperuser`

12. Save, commit, and push your project to GitHub. Uncomment the original DATABASES configuration, ensuring the DATABASE_URL is not pushed to the public domain.

13. Use an if-else statement in settings.py to switch between Postgres and the default database based on the availability of the DATABASE_URL variable.<br>

14. Install Gunicorn to act as the web server:`pip3 install Gunicorn` and then freeze again (`pip3 freeze > requirements.txt`).

15. Create a Procfile in the root directory to instruct Heroku on how to run the app. Write this code inside: `web: gunicorn <Project Name>.wsgi:application`

16. Log in to Heroku via the terminal. You can log in with your username and password.

17. Temporarily disable the collection of static files until AWS setup is complete:<br>
`heroku config:set DISABLE_COLLECTSTATIC=1 --app Heroku Project Name`

18. In settings.py, add the allowed hosts for both local and Heroku:<br>
`ALLOWED_HOSTS = ["<heroku appname>.herokuapp.com", "localhost"]` 

19. Save, commit, and push your changes to GitHub. Then push to Heroku to start building the app:
`heroku git:remote -a <heroku appname>`
`git push heroku master`

* Heroku should now start building the app, and your Heroku URL should be visible in the terminal. Note: At this point, your project won't have any static files, so don't worry if the site looks different from development. This will be resolved in the next section on AWS (Amazon Web Services).

20. o save time, set up automatic deployment when you push to GitHub. Go back to your Heroku dashboard and click on the "Deploy" tab. Here you will see "GitHub Connect to GitHub."

Search for your repository name. Once you see the repository, click on the connect button next to it.

21. Scroll down and enable automatic deploys. Click "Enable Automatic Deploys." Now, every time you push to GitHub, your app should update on Heroku.

#### **Amazon Web Services - AWS and Cloning Instructions** ####

* For this project, I used Amazon Web Services (AWS) to store static files and images. Below are the steps I followed to set this up. If you are looking to clone this project and work on it, you can follow this guide.

1. Open up [Amazon Web Services](https://aws.amazon.com/) in your browser
2. Click on "Create AWS Account."
3. Complete all required questions during the sign-up process.
4. Once registration is complete, navigate to your AWS dashboard.
5. Use Amazon S3 services. To find it quickly, type "S3" into the search bar.
6. Select S3, then click on "Create Bucket." Name your bucket something relevant to the project. Select the region closest to you from the dropdown menu.
7. Uncheck the box that says "Block all public access." AWS may warn you, but you can ignore this since the static files need to be public. Click the "Create bucket" button.
8. Set the settings in the bucket:

> Go to bucket properties.<br>
> Turn on static web hosting.<br>
> in the index and error text inputs, add index.html and error.html and then save.<br>

9. On the permissions tab, fill out the CORS configuration section.

10. Go to the bucket policy tab and select policy generator. Set it up as follows:<br>
> Type of Policy: S3 bucket policy<br>
> In Principal enter * to select all principals<br>
> From the action dropdown, select "GetObject"<br>
> For your ARN, copy and paste it from the bucket policy page<br>
> Click "Add Statement"<br>
> Click "Generate Policy"<br>
> Copy and paste the generated policy into your bucket policy<br>
> BAdd /* to the end of the resources key<br>
> Click save.<br>

11. Go to Access Control List and set "List objects" permission to everyone (public).

12. Create a new group and user to access the bucket. In the search box, type "IAM" (Identity Access Management):
> Click "Create a new group" and name it something like manage-<project name>.
> Click through the pages and create the group.<br>

13. Create a group policy:
> Click on "Policies" in the menu and then "Create policy."
> Select the JSON tab and import managed policies.
> Search for "AmazonS3FullAccess" and import it.
> In the resources section, paste in the ARN used previously. Enter the ARN twice, adding /* at the end of the second one.
> Click through to review policy, give it a name and description, and generate the policy.

14. Click on "Groups" from the side menu, select the group you created, click "Attach policy," search for the policy you created, and attach it.

15. Create a user:
> Click "Users" from the menu, then "Add user."
> Create a username, select programmatic access, and click next.
> Select the group to add your user to, click through to the end, and create the user.
> Download the CSV file containing the user keys needed to access the app.

Warning: Do not share the keys from this CSV file with anyone or make them public by pushing them to your GitHub.

#### **Connect bucket to Django and Cloning Instructions** ####

* To connect Django to the AWS S3 bucket, follow these steps:

1. Install necessary packages:
`pip3 install boto3`
`pip3 install django-storages`

2. This ensures the new packages are added to requirements.txt and deployed to Heroku.
`pip3 freeze > requirements.txt`

3. Update settings.py - Add storages to the INSTALLED_APPS section in settings.py.

4. Create an environment variable called USE_AWS to run the code on Heroku. Include the following settings in settings.py:

5. Go to the Heroku settings tab and click "Reveal Config Vars." Set up the necessary environment variables, ensuring USE_AWS is set to True.

6. Delete the DISABLE_COLLECTSTATIC variable from Heroku.

7. In Gitpod, create a custom_storages.py file to instruct Django to use Amazon S3 for storing static and media files. Add the following classes:

> `class StaticStorage(S3Boto3Storage):`<br>
> `location = settings.STATICFILES_LOCATION`<br>

> `class MediaStorage(S3Boto3Storage):`<br>
> `location = settings.MEDIAFILES_LOCATION`<br>

8. Save, commit, and push changes<br><br>

#### **Add Media files to AWS and Cloning Instructions** ####

* To upload images to S3, follow these steps:

1. In your AWS bucket, create a new folder called media.

2. Select the media folder and upload all your image folders and files. Ensure permissions are set to Everyone (Public access). 

3. Update your HTML code to reflect the new media storage location. Change image src attributes from:
src="media/..." to src="{{ MEDIA_URL }}<insert image name and file type>".

#### **Stripe and Cloning Instructions** ####

* The final step is to add the Stripe keys to the config variables. You can obtain these values from your Stripe dashboard.
* Ensure all config variables match the ones in your settings.py file. Below are the steps to complete this process:

* Retrieve Stripe Keys
> Go to your Stripe dashboard and obtain the necessary API keys.

* Set Config Variables in Heroku

> Navigate to your Heroku app's settings tab.
> Click on "Reveal Config Vars."
> Add the following config variables with their corresponding values from your Stripe dashboard:
> STRIPE_PUBLIC_KEY
> STRIPE_SECRET_KEY
> Any other Stripe-related variables you have in your settings.py.
> Update settings.py
> Ensure the config variables in your settings.py file match those in Heroku. For example:

> STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
> STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
* By following these steps, you can successfully integrate Stripe with your project and ensure all necessary configuration variables are properly set up for deployment.

#### **Cloning From Original Repository Instructions** ####

* To clone the project's repository to your local computer, follow these steps:

1. Visit the project's repository on GitHub: https://github.com/StanimirVasev/ci-project-4
2. Click on the "Code" tab above the files.
3. Select "HTTPS" from the dropdown menu.

4.Click on the clipboard icon to copy the repository URL: https://github.com/StanimirVasev/ci-project-4

5. Launch your IDE and open the terminal.

6. Navigate to the directory where you want to clone the project.

7.In the terminal, type git clone followed by the copied URL: git clone https://github.com/StanimirVasev/ci-project-4

8. Press Enter to create your local clone.

9. Install all the required packages by running: `pip3 install -r requirements.txt`

10. Configure the following environment variables for the project to work (yours will have to be unique):

> DJANGO_SECRET_KEY = your secret key<br>
> STRIPE_PUBLIC_KEY = your stripe public key<br>
> STRIPE_SECRET_KEY = your stripe secret key<br>
> STRIPE_WH_SECRET = your stripe webhook secret<br>
> IN_DEVELOPMENT = True<br>
> Your Stripe variables can be found on your Stripe dashboard.<br>
> Generate a Django secret key [here](https://djecrety.ir/)<br>

12. Check for migrations by running: `python3 manage.py makemigrations --dry-run`

* Plan the migrations: `python3 manage.py migrate --plan`

* f there are no issues, apply the migrations: `python3 manage.py migrate`

* Create a superuser for the project by running the command: `python3 manage.py createsuperuser`

* Start the development server: `python3 manage.py runserver`

* By following these steps, you can successfully clone and set up the project on your local machine.

</details>
<hr>

<details>
<summary><strong>
6. Credits
</strong></summary>
<br>

#### **6.1 Media** ####

As mentioned previously, I have used Canva Pro to source and create most of the images on the site. For example, all blog images, homepage images, etc are created on Canva. However, the product images have been sourced from Photosynthesis. All credits belong to them.


#### **6.2 Code** ####

* The Django walkthrough project "Boutique Ado" provided by Code Institute was used as a resource during the development of this project. Credit goes to the lecturers at Code Institute for creating the instructional materials and tutorial videos.
* I have also reviewed various Student examples and other materials provided by Code Institute in Slack and website. 

<hr>

#### **6.3 Acknowledgements** ####

* Thank you to all of the tutor team at Code Institute who were always on hand whenever i needed their support.
* A big thank you to my mentor Rohit who always gives me great feedback on my ideas and is able to point me in the right direction.
* A final big thank you to all of the other students, CI alumni and CI staff who were always willing to help out and advise on the official CI Slack channels.

</details>

<hr>

<details>
<summary><strong>
8. Disclaimer
</strong></summary>
<br>

* This website and all of its content was completed for my final assessment project with Code Institute. The site is strictly for educational purposes only, there is no commercial revenue and being generated from the site.

</details>