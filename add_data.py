#!/usr/bin/env python3
""" data insertion script
"""


def add_data_to_database(db, Drink):
    # Create instances of Drink
    drinks_data = [
        {'name': 'Tea', 'description': 'A hot beverage made by steeping tea leaves in water.'},
        {'name': 'Coffee', 'description': 'A brewed drink prepared from roasted coffee beans.'}
    ]

    try:
        for data in drinks_data:
            existing_drink = Drink.query.filter_by(name=data['name']).first()
            if not existing_drink:
                new_drink = Drink(
                    name=data['name'], description=data['description'])
                db.session.add(new_drink)

        # Commit the session to persist the changes to the database
        db.session.commit()
        print('Data added successfully!')
    except Exception as e:
        # Rollback the session in case of an error
        db.session.rollback()
        print('Error:', str(e))
