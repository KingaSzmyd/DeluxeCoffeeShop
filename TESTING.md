# Deluxe Coffee Shop - Testing
The live site can be viewed here - [Deluxe Coffee Shop](https://msp4-deluxecoffeeshop.herokuapp.com/)).

[Back to README file](https://github.com/KingaSzmyd/MSP4-DeluxeCoffeeShop/blob/main/README.md).

![alt text](media/all-devices-black.png)

## Manual testing 
### Navigation:
1. Checked the navigation bar remains at the top of the page at all times and is never hidden by any other content.
2. Checked the banner at the top of the navigation bar always displays delivery information.
3. Clicked the Deluxe Coffee Shop logo to make sure it’s a link back to the home page.
4. Tested the search bar:
* Checked that it’s centrally aligned and that the placeholder is visible and is displaying on all pages.
* Clicked the button to test what it does:
Loads the products page and shows products that match the search. Submiting an empty search shows an error message telling that.
5.  Checked that the icons linking to the profile page and bag appear to the right of the navigation bar.
6. Checked that they perform as expected for: unregistered users, registered users, admin.
7. Checked that if there are any items in the shopping cart then the number of items will show on the cart icon.
8. Clicked on all the links to ensure they do what they're supposed to do.
* Home and blog take me to the relevant pages.
* All Products, coffees and equipment links have an additional dropdown menu that displays the categories options.
9. Footer:
* Checked the footer sticks to the bottom of home page and never hides any content.
* Checked that the social links are always aligned centrally and that they open in a new tab.
10. Home:
* Checked that the background image isn't pixelated, is positioned well and loads as intended.
* Checked the text overlay box appears and that the relevant text and button is visible within it.
* Tested the call-to-action button and it sends us to the All Products page as desired.
* Checked the overlay box and its contents are always justified and aligned centrally.
* All products are shown as individual cards.
11. Products:
* Checked that all products load as expected.
* Checked that if a filter has been applied that it’s taken effect and products are displaying in the order specified. Correct products are displayed according to which filter has been applied.
* Seen that the sort by… dropdown menu loads and is positioned where intended, underneath the page title and to the right of the page.
* Checked that each selection applies the intended filter and that the cards below are displayed in order of what’s selected.
12. Individual product card test: 
* Checked that every card contains:
- A product image that adjusts dependant to screen width. Checked that this image also links to the products details page.
- Shows the products name.
- Details the products category | price | rating | description | size (if applicable).
* The add to cart button and quantity selector appear at the bottom of the card. A quantity is shown in the box (default number should be 1.
* Tested that the + / – buttons increase or decrease the number. Checked that + gets disabled at 99. Checked that - gets disabled at 1.
* Tested that numbers outside this range can’t be added manually.
* Tested the add button to check that the correct quantity of the item gets added to the bag. Seen that a toast message appears confirming this addition. The toast shows a preview of the bag.
* Checked the bag icon in the navigation bar updates accordingly. Checked the correct number of items have been added to the bag.
13. Product detail page:
* Checked that the correct product has been loaded.
* Checked that all relevant information has been loaded and is displayed as expected.
* The Keep Shopping button appears for all users underneath the products card and this takes me back to the Bottle Shop.
* Check that the edit and delete buttons appear for admin only.
* Checked the edit product button opens the edit product form.
* Checked the delete product button triggers the deletion modal.
14. Bag:
* Checked that at the top of the page a banner informing the user how much more they need to spend to qualify for free delivery shows (if applicable).
* Checked that if items in the cart equate to over €50 then the user is informed they’ve qualified for free delivery.
* Checked that if items do exist in the bag then each individual item line has its own row with the following details: image, product info.
* Checked the rows subtotal has adjusted accordingly.
* Checked the overall totals below adjust.
* Checked that the item is removed from the bag and is no longer displayed.
* Seen that the toast message appears confirming the removal.
* Checked the rest of the bag reacts accordingly.
* Checked that the subtotal is always displayed.
* Tested that each row is responsive to screen width and the most important information is always displayed.
* Checked the totals are shown underneath the last row and are done so in a clear and obvious manner.
* Pressed the checkout button at the bottom, this takes me to the checkout page.
15. Checkout:
* Checked that the order summary section is reflective of the bag page.
* Checked that each line item is listed and matches that of what was in the bag.
* Checked that the subtotal, delivery and total all match too.
* Checked if the user is unregistered all fields will be blank showing the placeholders only.
* Checked if the user is registered and has ordered something previously from the site then these fields could be pre-populated if they have default delivery information saved to their profile.
* Payment: one field that takes the card number, the MM/YY and CVC number.
* Checked the form validates properly by: attempting to send an empty form, attempting to send the form whilst leaving any of the fields empty.
* Attempted to send while leaving the payment field empty. This causes a validation error sent from Stripe.
* Checked that dependent on user status either a link to log in or sign up appears or a check box to save delivery information is shown after the delivery details.
* Clicked the log in link.
* Clicked the sign up link.
* Checked the place order button starts the checkout / Stripe’s payment process.
* Checked the order processing overlay appears to show that something is happening.
* On successful completion of the sent order to the order success page where a summary of the order is displayed.
16. Order confirmation:
* Checked confirmation page loads as it should.
* All information on the confirmation is relevant and correct:
- Order info (order number and order date) is shown.
- Delivery info (address and contact number) is shown.
- Order details shown.
- Billing details (subtotal, delivery and total) are shown.
* Checked that I received the confirmation email sent.
* Checked that Stripe has taken the payment.
* Checked the order now appears in the database.
* Checked that if I’m a registered user the order appears in my profile under order history.
* Checked if my delivery information gets saved.
17. Profile:
* Checked the page is only accessible to registered users.
* Checked that the user’s username appears in the title.
* Seen that the page is split into two sections:
* Saved delivery information form.
* Checked that if the user has default delivery information already saved to their account then the form should be pre-populated with this.
* Checked that if the user has no default delivery information saved to their account then the form should be blank showing the placeholders only.
* Clicked the update info button to test it submits the form.
* A toast appears confirming this information has been saved.
18. Order history.
* Checked that the details of all previous orders made by that user are shown.
* Date and time of order is shown.
* Order number is displayed.
* Order total is shown.
* The order number acts as a link to the order’s confirmation page.
* When clicked the order confirmation page loads and all details are correct and present.
* A toast message appears to say this was a past order.
19. Blog:
* Checked that the page loads as expected and is titled Blog.
* Checked that each post within the blog is represented via a card similar to products on the site.
* Checked that each card contains:
- An image that’s associated with the post.
- Checked this image adjusts dependant on screen width.
- Checked that this image also links to the blog post.
- The date and time posted.
- The article’s title.
- A button that links to the blog post.
20. Blog Posts:
* Checked that the correct article has been loaded.
* Checked that all information has been loaded and is displayed as expected.
* Checked that the title of the article is shown at the top of the page. Followed by:
- An image that adjusts dependant on screen width.
- The date and time that the post was posted underneath the image.
- The article itself.
- Followed by the author at the bottom of the article.
* Checked that the appropriate buttons based on the user’s registration status appear below all this.
* Checked the Back to blog’s button appears for all users and this takes me back to the blog page.
* Seen that the edit and delete buttons appear for admin only.
* Checked the edit post button opens the edit blog form.
* Checked the delete post button triggers the deletion modal.
* Checked that the comments section is different dependent on the user’s registration status.
* If unregistered:
- Checked the comment box is hidden and is replaced with links to sign up or login.
- Checked these links work.
- Checked that other user comments are still displayed.
* If registered:
- Checked that the comment box is shown along with a button to post a comment.
- Checked the placeholder is visible.
- Checked that the form can’t be submitted empty.
- Checked the error toast message appears stating this.
- Checked that a validation message appears underneath the comment box.
- Checked that if a comment is valid it gets posted.
- Seen that the comment appears below.
Checked that the page is responsive and everything gets displayed correctly at all breakpoints.
21. Add product:
* Checked that the form is accessible by admin only.
* Checked the number of fields have a relevant label.
* Checked a category name can be selected from the dropdown menu and is populated with categories from the categories model.
* Successful submission of the form redirected to the newly created products detail page.
* A toast appears confirming that the product has been added.
* Checked that the product now appears in the database.
22. Edit product:
* Checked that the form is accessible by admin only.
* Toast message confirms that you’re now editing the product.
* The form is the same as the one that’s found on the add product page but all fields are pre-populated with the existing data.
* Pressed update product, the updated product loads and a success toast confirms the update.
* Tested that the form still validated the inputted data correctly. The form will then only send if all fields that are required are filled in.
* Successful completion of the form redirected to the product in questions page, which shows the updated information.
23. Add blog post
* Checked that the form is accessible by admin only..
* Checked the number of fields have a relevant label.
* Pressed back to blogs - takes to the blogs page.
* Tested that the form validated the inputted data correctly. The form will then only send if all fields are filled in.
* Successful completion of the form redirected to the newly created blog article page, which will show the post just posted.
24. Edit blog post:
* Checked that the form is accessible by admin only.
* Toast message confirms that you’re now editing the blog post.
* The form is the same as the one that’s found on the add blog post page but all fields are pre-populated with the existing data.
* Pressed back to post this takes me to the blog article.
* Pressed update blog post, the updated article loads and a success toast confirms the update.
* Tested that the form still validated the inputted data correctly. The form will then only send if all fields are filled in.
* Successful completion of the form redirected to the newly updated article page.
25. Delete functions:
* The delete button triggers the deletion process.
26. Deleting a blog post:
* Checked that the function can be performed by admin only.
* When a post is deleted I’m redirected back to the blog page.
* A toast message appears confirming the deletion.
* Checked that it can no longer be found in the database.
26. Deleting a product:
* Checked that the function can be performed by admin only.
* A toast message appears confirming the deletion.
* Checked that it can no longer be found in the database.
### Responsiveness
During the process of building the project all elements and every change were testing by using Chrome DevTools at different breakpoints. 
The responsivness of completed project was also tested by using Chrome DevTools on different devices. 

[The Deluxe Coffee Shop as seen on an iPad]()

### Browser compatibility
I have physically tested my website on the following browsers and devices:
Chrome (desktop and iPhone).
Safari (desktop and iPhone).
### User Stories
1. As a shopper I'd like to:
"View a selection of products and select those I want to purchase."
* The products page is accessible to all users, registered or not.
* Links to view products can be found in the navigation bar, which can be seen at all times.
* There is the call-to-action button placed on the home page redirecting the user to the products page.
* Any time that a product is displayed, the user always has the option to add the product to the bag if they wish to purchase it.
"Filter products based on their type or where they originate from."
* The products can be filtered by their price, name or rating using the filters found in the dropdown menu via the navigation bar
"To search for products by using keywords."
* The search bar can be found in the navigation bar, which can be seen at all times. On smaller devices it toggles using a button with a magnifying glass icon, which makes it apparent to what it is.
* The search is conducted on all products names, type and their description and any matches are shown accordingly.
"Look at individual product details in order to consolidate my decision on whether to purchase the item or not."
* Every product has its own page that gives further information on the product. The pages are accessed via the products card, which are seen throughout. The image is the link.
* Further information gets displayed via a table, which breaks the information up. This means information is always displayed in a clear and informative manner in keeping with the overall style of the site.
* The product can also be added to the bag from here as the add button along with the quantity adjustment buttons are shown.

[Individual product page.]()

"Add items to the bag to purchase at a later point."
* Any time that a product is displayed on the site, the user always has the option to add the product to the bag.
* Every card used throughout the entire site includes the add button along with the quantity adjustment buttons, which add the selected amount of items to the cart.
"Easily view the bag contents and the number of items within it."
* The bag icon found in the navigation bar acts as a direct link to the cart page and as mentioned before the navigation bar is fixed so this link is always visible.
* The checkout link at the bottom of the toast will send the user to the bag page.
"Be given the ability to change the quantity of items within the bag or remove items completely."
To change quantities of an item is on the bag page, which as touched on above is easy to get to due to the link in the fixed navigation bar.
* Quantities can be changing by using the quantity adjustment buttons used throughout the site but this time a user will have to click on the update link instead of add.
* A toast message appears confirming this alteration.
* Items can be completely removed from the bag by clicking the remove link. The bag page is the only place items can be removed from the bag.
* A toast message appears confirming the removal.
"Be rewarded with free delivery, when buying a decent amount of products."
* There is a banner at the navigation bar stating that the customer gets free delivery on orders over €50.
* Additionally when an item is added a toast message will appear confirming this addition as we've established. At the bottom of this toast a message is shown stating how much the user needs to spend to qualify for free delivery.
"Checkout, pay and complete my order easily."
* On the checkout page the order is summarised so that the user is shown what is ordering.
* Adding personal, delivery and payment details is done via a user friendly form.
* Successful completion of the order redirected to their order confirmation page.
"Have order confirmation once my order has been completed."
* Successful completion of an order the user is automatically redirected to the order success page. This page confirms and shows all the information that the user has just inputted as part of the order.
* A success toast message also appears confirming successful completion of the order.
* On top of this an email confirmation is sent out to the email address provided.
* This has been tested as part of my manual testing.
2. 
"Navigate around the site easily and the site to be user friendly."
* The fixed navigation bar so that links are available at the top of every page and at any point.
* This is also the case on smaller devices but the links get placed into a dropdown menu, which is operational by toggling.
"Receive feedback whilst interacting with the site."
* Toast messages appear in the top right of the screen when information needs to be relayed to the user such as when a function has been performed or something has gone wrong.
* Validation messages appear on forms fields when input is invalid or incorrect.
"To sign up and register for an account easily."
* The link to register can be found in the navigation bar.
* Registering is as simple as inputting an email address, username and password.
* For security the password needs to be re-typed.
* A user is clearly informed if the username is in use or if the passwords don’t match.
* All registrations will require email verification to confirm the user is who they say they are.
* An email asking the user to verify themselves via a link is sent to the email address provided.
"To receive email confirmation of registration and have the ability to recover forgotten passwords."
* Email confirmations are sent to verify and confirm registration to The Deluxe Coffee Shop as mentioned above.
* Used Django allauth to handle user registration, logging in, logging out and verifying accounts etc it also handles other account functionality such as resetting lost passwords.
* When the forgot password link is clicked the user is asked to enter an email address and if it matches one that’s associated with a user in the database then they are sent a reset link to create a new password.
* Django allauth handles all this really well and in a very user friendly manner.
"To login and logout easily."
* The link to login can be found in the navigation bar.
* The logging in process is just as simple as registering with only a username or email address being required along with a password.
* Each input field is clearly labelled.
* When successfully logged in a success toast will appear welcoming the user.
* A user is clearly informed if the details provided don’t match.
"A personalised user profile where I can see my order history and set my default delivery information if desired."
* The link that a user can use to access their profile can be found in the navigation bar.
* The page is personalised by including their username in the title.
* The order number here also acts as a link to the order confirmation.
* Saved delivery information can be inputted or is shown via a form on the page.
* Any information inputted and updated here overrides the users default delivery information where it is used in instances such as when checking out.
* The information shown here can get overridden as part of the checkout process if the user selects to save their information via the checkbox.
"To read coffee related articles as I’m a regular consumer of coffee and I’d find a blog interesting."
* Added a blog to the site where coffee related articles and posts can be made. This adds additional purpose to the site making it not just a shop.
* Each article is previewed on its own card and can be clicked upon to open the article to read.
"The ability to comment and interact with other users on the blog posts."
* At the bottom of every blog article there is a comments section where registered users can post questions, thoughts and opinions on the article.
* Comments made on the article are available for all to see.
* The functionality to comment is only available to registered users though. Unregistered users are provided with links to register or sign in here to encourage them to do so.
* A toast message will appear to confirm if the comment has been posted or not.
3. As the site owner / admin I want:
"The ability to add new products to the store." / "The ability to create and post new articles to the blog."
* Adding either a new product or blog post is done via a form.
* The links to access both forms are shown in the navigation bar by clicking the profile link / icon and selecting them from the dropdown menu.
* These links are only visible to admin.
* The pages are only accessible by admin.
* Each input field is clearly labelled and includes a placeholder. 
* Successful completion we get sent to the newly created page and the product/article can be viewed on the site.
"To be able to edit and remove products from the store." / "To be able to edit and remove existing posts from the blog."
* As with adding products and blog posts, editing and removing them can only be done by admin with access to the relevant forms and functionality restricted.
* To access the edit and delete function of a product, admin needs to navigate to the product detail page of the item and the relevant call-to-action buttons will be shown under the table as shown below.
* To access the edit and delete function of a blog post, admin needs to navigate to the blog post in question and the edit and delete buttons will be shown underneath the article.
* Editing either will take you to the relevant form, which will be pre-populated with the data that’s already been inputted.
* Form fields are clearly labelled and all data entered is validated the same as when it’s intially added.
* Any deletion or update is confirmed by a toast message.
* Edit and delete a product buttons.