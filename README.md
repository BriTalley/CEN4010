
Thomas Vonseggern - CEN4010 -

Wish List Management

 Must be able to create a wishlist of books that belongs to user and has a unique name
 
o Logic: Given a user Id and a wish list name, create the wishlist.

o HTTP Request Type: POST

o Parameters Sent: Wish list name, User Id

o Response Data: None

 Must be able to add a book to a user’s wishlisht
 
o Logic: Given a book Id and a wish list Id, add the book to that wish list.

o HTTP Request Type: POST

o Parameters Sent: Book Id, Wishlist Id

o Response Data: None

 Must be able to remove a book from a user’s wishlist into the user’s shopping cart
 
o Logic: : Given a book Id and a wish list Id, remove the book to that wish list.

o HTTP Request Type: DELETE

o Parameters Sent: Book Id, Wishlist Id

o Response Data: None

 Must be able to list the book’s in a user’s wishlist
 
o Logic: Given a wishlist Id, return a list of the books in that wishlist.

o HTTP Request Type: GET

o Parameters Sent: Wishlist Id

o Response Data: JSON LIST of books in the user’s wishlist.
=======
CEN 4010 - Group 10
