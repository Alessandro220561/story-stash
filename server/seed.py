#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Book, ReadingLog, UserLog

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():

        print("Deleting all records...")
        UserLog.query.delete()
        ReadingLog.query.delete()
        User.query.delete()
        Book.query.delete()

        print("Starting seed...")
        # Seed code goes here!
        for i in range(10):
            user = User(
                username=fake.user_name(),
                email = fake.email()
            )
            db.session.add(user)

        book_titles = ['It', 'Malice', 'Project Hail Mary', 'Golden Son', 'The Great Hunt', 'A Game of Thrones', 'Of Blood And Fire', 'The Way of Kings', 'The Hobbit', 'The Lincoln Highway']
        book_authors = ['Stephen King', 'John Gwynne', 'Andy Weir', 'Pierce Brown', 'Robert Jordan', 'George R.R. Martin', 'Ryan Cahill', 'Brandon Sandersen', 'J.R.R. Tolkien', 'Amor Towles']
        book_genres = ['Mystery', 'Horror', 'Fantasy', 'Science Fiction', 'High Fantasy', 'Fiction']

        for i in range(10):
            book = Book(
                title = rc(book_titles),
                author = rc(book_authors),
                genre = rc(book_genres),
                pages = randint(50, 750)
            )
            db.session.add(book)

        for i in range(20):
            reading_log = ReadingLog(
                user_id = randint(1, 10),
                book_id = randint(1, 10),
                start_date = fake.date_time_between(start_date="-30d", end_date="now"),
                end_date = fake.date_time_between(start_date="now", end_date="+30d")
            )
            db.session.add(reading_log)

        for i in range(20):
            user_log = UserLog(
                user_id = randint(1, 10),
                reading_log_id = randint(1, 20),
                favorite = rc([True, False])
            )
            db.session.add(user_log)

        db.session.commit()
        print("Complete.")