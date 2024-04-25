import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("tourpackage.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table PACKAGE(id int, AGENT_NAME VARCHAR(25),PACKAGE_TYPE VARCHAR(30),
INCLUSION VARCHAR(120),COST INT, DURATION INT);

"""
cursor.execute(table_info)

## Insert Some more records
cursor.execute('''Insert Into PACKAGE values(14, 'Mountain Retreat','nature', "Hiking trails, cabin stays, mountain views", 25000, 5)''')
cursor.execute('''Insert Into PACKAGE values(15, 'Island Getaway','relax', "Beach resorts, water sports, sunset cruises", 30000, 6)''')
cursor.execute('''Insert Into PACKAGE values(16, 'European Adventure','culture', "Euro rail pass, sightseeing tours, wine tasting", 40000, 8)''')
cursor.execute('''Insert Into PACKAGE values(17, 'Wildlife Expedition','adventure', "Wildlife safaris, jungle lodges, bird watching", 32000, 7)''')
cursor.execute('''Insert Into PACKAGE values(18, 'Coastal Escape','relax', "Seaside cottages, seafood dining, coastal hikes", 27000, 5)''')
cursor.execute('''Insert Into PACKAGE values(19, 'Historical Tour','culture', "Historical sites, guided tours, cultural performances", 22000, 4)''')
cursor.execute('''Insert Into PACKAGE values(20, 'Snowy Getaway','adventure', "Ski resorts, snowboarding, hot springs", 38000, 6)''')
cursor.execute('''Insert Into PACKAGE values(21, 'Tropical Rainforest Retreat','nature', "Rainforest lodges, canopy walks, river cruises", 32000, 7)''')
cursor.execute('''Insert Into PACKAGE values(22, 'Cruise Vacation','relax', "Luxury cruise ship, island stops, onboard entertainment", 45000, 9)''')
cursor.execute('''Insert Into PACKAGE values(23, 'Cultural Immersion','culture', "Homestays, cultural workshops, traditional meals", 25000, 5)''')
cursor.execute('''Insert Into PACKAGE values(24, 'Desert Expedition','adventure', "Desert camps, camel rides, sand dune tours", 30000, 6)''')
cursor.execute('''Insert Into PACKAGE values(11, 'Safari Adventure','adventure', "Game drives, bush walks, safari lodge stays", 35000, 6)''')
cursor.execute('''Insert Into PACKAGE values(12, 'Tropical Paradise','relax', "Beachfront bungalows, snorkeling, island hopping", 28000, 7)''')
cursor.execute('''Insert Into PACKAGE values(13, 'City Exploration','city', "Guided city tours, historical landmarks, local cuisine", 20000, 4)''')
cursor.execute('''Insert Into PACKAGE values(8, 'Adventure Expedition','adventure', "Scuba diving, kayaking, jungle trekking, zip-lining", 23000, 5)''')
cursor.execute('''Insert Into PACKAGE values(1, 'Exotic Holidays','relax', "Flights, accommodation, breakfast, city tours, beach activities", 15000, 3)''')
cursor.execute('''Insert Into PACKAGE values(2, 'Luxury Getaway','luxury', "VIP flights, 5-star accommodation, all-inclusive meals, private excursions" , 50000, 5)''')
cursor.execute('''Insert Into PACKAGE values(3, 'Family Fiesta','family', "Water park tickets, amusement park visits, family-friendly activities", 28000, 7)''')
cursor.execute('''Insert Into PACKAGE values(4, 'Adventure Expedition','adventure', "Scuba diving, kayaking, jungle trekking, zip-lining", 13000, 3)''')
cursor.execute('''Insert Into PACKAGE values(5, 'Exotic Holidays','relax', "Flights, accommodation, breakfast, city tours, beach activities", 25000, 5)''')
cursor.execute('''Insert Into PACKAGE values(6, 'Luxury Getaway','luxury', "VIP flights, 5-star accommodation, all-inclusive meals, private excursions" , 30000, 3)''')
cursor.execute('''Insert Into PACKAGE values(7, 'Family Fiesta','family', "Water park tickets, amusement park visits, family-friendly activities", 14000, 3)''')

# connection.commit()

## Disspaly ALl the records
print("The inserted records are")
# ----------------------------------------------------------------------------------------------------------------------


## create the table
# table_info="""
# Create table CUSTOMER(cust_id int, NAME VARCHAR(25), BOOKED_ON VARCHAR(25),  AGENT_NAME VARCHAR(25), PACKAGE_TYPE VARCHAR(30),
# INCLUSION VARCHAR(120),COST INT, DURATION INT);

# """
# cursor.execute(table_info)

# cursor.execute('''Insert Into CUSTOMER values(14, 'Charlotte', '2024-06-15', 'Mountain Retreat','nature', "Hiking trails, cabin stays, mountain views", 25000, 5)''')
# cursor.execute('''Insert Into CUSTOMER values(15, 'Elijah', '2024-05-20', 'Island Getaway','relax', "Beach resorts, water sports, sunset cruises", 30000, 6)''')
# cursor.execute('''Insert Into CUSTOMER values(16, 'Amelia', '2024-04-10', 'European Adventure','culture', "Euro rail pass, sightseeing tours, wine tasting", 40000, 8)''')
# cursor.execute('''Insert Into CUSTOMER values(17, 'Benjamin', '2024-03-05', 'Wildlife Expedition','adventure', "Wildlife safaris, jungle lodges, bird watching", 32000, 7)''')
# cursor.execute('''Insert Into CUSTOMER values(18, 'Harper', '2024-02-10', 'Coastal Escape','relax', "Seaside cottages, seafood dining, coastal hikes", 27000, 5)''')
# cursor.execute('''Insert Into CUSTOMER values(19, 'Evelyn', '2024-01-25', 'Historical Tour','culture', "Historical sites, guided tours, cultural performances", 22000, 4)''')
# cursor.execute('''Insert Into CUSTOMER values(20, 'William', '2023-12-20', 'Snowy Getaway','adventure', "Ski resorts, snowboarding, hot springs", 38000, 6)''')
# cursor.execute('''Insert Into CUSTOMER values(21, 'James', '2023-11-15', 'Tropical Rainforest Retreat','nature', "Rainforest lodges, canopy walks, river cruises", 32000, 7)''')
# cursor.execute('''Insert Into CUSTOMER values(22, 'Avery', '2023-10-10', 'Cruise Vacation','relax', "Luxury cruise ship, island stops, onboard entertainment", 45000, 9)''')
# cursor.execute('''Insert Into CUSTOMER values(23, 'Logan', '2023-09-05', 'Cultural Immersion','culture', "Homestays, cultural workshops, traditional meals", 25000, 5)''')

# cursor.execute('''Insert Into CUSTOMER values(4, "Jasmine", "2024-01-01", 'Adventure Expedition','adventure', "Scuba diving, kayaking, jungle trekking, zip-lining", 23000, 5)''')
# cursor.execute('''Insert Into CUSTOMER values(6, 'Thompson', '2023-12-15', 'Exotic Holidays','relax', "Flights, accommodation, breakfast, city tours, beach activities", 15000, 3)''')
# cursor.execute('''Insert Into CUSTOMER values(2, 'Lucas', '2024-2-13', 'Luxury Getaway','luxury', "VIP flights, 5-star accommodation, all-inclusive meals, private excursions" , 50000, 5)''')
# cursor.execute('''Insert Into CUSTOMER values(3, 'Patel', '2023-12-23', 'Family Fiesta','family', "Water park tickets, amusement park visits, family-friendly activities", 28000, 7)''')
# cursor.execute('''Insert Into CUSTOMER values(8, 'Ethan', '2023-10-14', 'Adventure Expedition','adventure', "Scuba diving, kayaking, jungle trekking, zip-lining", 13000, 3)''')
# cursor.execute('''Insert Into CUSTOMER values(7, 'Sofia', '2024-03-12', 'Exotic Holidays','relax', "Flights, accommodation, breakfast, city tours, beach activities", 25000, 5)''')
# cursor.execute('''Insert Into CUSTOMER values(1, "Johnson", "2023-11-15", 'Luxury Getaway','luxury', "VIP flights, 5-star accommodation, all-inclusive meals, private excursions" , 30000, 3)''')
# cursor.execute('''Insert Into CUSTOMER values(5, "Liam", "2024-01-19", 'Family Fiesta','family', "Water park tickets, amusement park visits, family-friendly activities", 14000, 3)''')

data=cursor.execute('''Select * from PACKAGE''')

for row in data:
    print(row)

# data=cursor.execute('''Select * from CUSTOMER''')

# for row in data:
#     print(row)

## Commit your changes int he databse
connection.commit()
connection.close()