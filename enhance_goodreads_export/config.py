from .entities import AbsoluteUrl


USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/101.0.4951.54 Safari/537.36"
)
BOOK_URL = AbsoluteUrl("https://www.goodreads.com/book/show/{book_id}")
REVIEW_URL = AbsoluteUrl("https://www.goodreads.com/review/edit/{book_id}")
STATS_URL = AbsoluteUrl("https://www.goodreads.com/book/stats?id={book_id}")

BASE_URL = AbsoluteUrl("https://www.goodreads.com")
SIGNIN_URL = AbsoluteUrl("https://www.goodreads.com/user/sign_in")
SIGNIN_POST_URL = AbsoluteUrl("https://www.goodreads.com/ap/signin")


STANDARD_FIELDNAMES = [
    "Book Id",
    "Title",
    "Author",
    "Date Read",
    "Exclusive Shelf",
]

IGNORE_GENRES = {
    "to-read",
    "currently-reading",
    "in-library",
    "own",
    "owned",
    "favorites",
    "books-i-own",
    "default",
    "wish-list",
    "on-hold",
    "library",
    "netgalley",
    "dnf",
    "did-not-finish",
    "owned-not-read",
    "dropped",
    "tbr",
    "amazon",
    "audiobook",
    "audiobook",
    "ebook",
    "favorites",
    "favourites",
    "e-owned",
    "purchased",
    "ebooks-kindle",
    "kindle",
    "on-kindle",
    "reviewed",
    "bought",
    "to-buy",
    "maybe",
    "might-read",
}

IGNORE_GENRE_SUBSTRINGS = {"read-in", "to-read", "read-", "-read", "-tbr", "tbr-"}
