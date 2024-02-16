#!/usr/bin/env python3
""" data insertion script
"""

def add_data_to_database(db, Drink):
    # Create instances of Drink
    drink1 = Drink(
        name='Tea', description='A hot beverage made by steeping tea leaves in water.')
    drink2 = Drink(
        name='Coffee', description='A brewed drink prepared from roasted coffee beans.')

    try:
        # Add objects to the session
        db.session.add(drink1)
        db.session.add(drink2)

        # Commit the session to persist the changes to the database
        db.session.commit()
        print('Data added successfully!')
    except Exception as e:
        # Rollback the session in case of an error
        db.session.rollback()
        print('Error:', str(e))
