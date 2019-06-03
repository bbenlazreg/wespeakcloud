from app import db
from app.models import Menu

class Seeder(object):
    def populate_database(self):
        record = Menu.query.first()
        if not record:
            new_record = Menu(name="Pasta")
            new_record2 = Menu(name="Burger")
            new_record3 = Menu(name="Salad")
            new_record4 = Menu(name="Risotto")
            new_record5 = Menu(name="Cookie")
            db.session.add(new_record)
            db.session.add(new_record2)
            db.session.add(new_record3)
            db.session.add(new_record4)
            db.session.add(new_record5)
            db.session.commit()

if __name__ == '__main__':
    print("Seeding...")
    seeder = Seeder()
    seeder.populate_database()
    print("Seeding complete.")
