book_reviews
# CEN4010
 ## Book Reviews and Commenting API

### POST /reviews/add/
Adds a new review to the database.

Required JSON fields:
- book_id (string)
- username (string)
- rating (integer from 1 to 5)
- comment (text)

Example JSON:
{
  "book_id": "456",
  "username": "cvd_demo",
  "rating": 4,
  "comment": "Solid read with great pacing."
}



### GET /reviews/<book_id>/
Returns all reviews for a specific book ID.

Example URL:  
http://127.0.0.1:8000/reviews/456/

Expected Response:
[
  {
    "id": 1,
    "book_id": "456",
    "username": "cvd_demo",
    "rating": 4,
    "comment": "Solid read with great pacing.",
    "created_at": "2025-03-24T23:59:49.789Z"
 

CEN 4010 - Group 10
main
