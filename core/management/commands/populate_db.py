# Save this file as: core/management/commands/populate_db.py
# Directory structure: core/management/commands/populate_db.py

"""
Django Management Command to Populate Database with Sample Data
Usage: python manage.py populate_db
"""

from django.core.management.base import BaseCommand
from core.models import Tour, Booking, ContactMessage
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populates the database with sample safari tours and data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')

        # Clear existing data (optional - comment out if you want to keep existing data)
        self.stdout.write('Clearing existing data...')
        Tour.objects.all().delete()
        Booking.objects.all().delete()
        ContactMessage.objects.all().delete()

        # Create Tours
        self.stdout.write('Creating tours...')
        tours_data = [
            {
                'name': 'Maasai Mara Great Migration Safari',
                'description': 'Witness one of nature\'s most spectacular events - the Great Migration. Watch millions of wildebeest, zebras, and gazelles cross the Mara River while predators lie in wait. This 5-day adventure includes luxury tented camps, expert guides, and unforgettable wildlife encounters in Kenya\'s most famous game reserve.',
                'duration_days': 5,
                'price': 2850.00,
                'difficulty': 'moderate',
                'max_group_size': 8,
                'featured': True
            },
            {
                'name': 'Serengeti & Ngorongoro Crater Explorer',
                'description': 'Experience the best of Tanzania\'s northern circuit. Explore the vast Serengeti plains teeming with wildlife, then descend into the Ngorongoro Crater, a UNESCO World Heritage Site and home to the Big Five. Includes visits to Olduvai Gorge and traditional Maasai villages.',
                'duration_days': 7,
                'price': 3500.00,
                'difficulty': 'moderate',
                'max_group_size': 10,
                'featured': True
            },
            {
                'name': 'Amboseli Elephant Paradise',
                'description': 'Get up close with Africa\'s gentle giants against the stunning backdrop of Mount Kilimanjaro. Amboseli National Park is famous for its large elephant herds and breathtaking views. This 3-day safari is perfect for photographers and nature lovers seeking an intimate wildlife experience.',
                'duration_days': 3,
                'price': 1450.00,
                'difficulty': 'easy',
                'max_group_size': 12,
                'featured': True
            },
            {
                'name': 'Lake Nakuru Flamingo Spectacle',
                'description': 'Visit the stunning Lake Nakuru, home to millions of flamingos that turn the lake pink. This 4-day safari also includes game drives where you\'ll spot rhinos, lions, leopards, and over 450 bird species. Stay in comfortable lodges overlooking the lake.',
                'duration_days': 4,
                'price': 1850.00,
                'difficulty': 'easy',
                'max_group_size': 10,
                'featured': False
            },
            {
                'name': 'Samburu Desert Safari Adventure',
                'description': 'Explore Kenya\'s rugged northern frontier in Samburu National Reserve. Encounter unique wildlife species found nowhere else in Kenya including the Grevy\'s zebra, reticulated giraffe, and Somali ostrich. Experience the rich culture of the Samburu people in this off-the-beaten-path adventure.',
                'duration_days': 6,
                'price': 2650.00,
                'difficulty': 'challenging',
                'max_group_size': 8,
                'featured': False
            },
            {
                'name': 'Tsavo East & West Discovery',
                'description': 'Explore Kenya\'s largest national park system, famous for its red elephants and dramatic landscapes. Visit Mzima Springs with its underwater hippo viewing chamber, and search for the legendary "Man-Eaters of Tsavo". A perfect safari for adventurous spirits.',
                'duration_days': 5,
                'price': 2200.00,
                'difficulty': 'moderate',
                'max_group_size': 10,
                'featured': False
            },
            {
                'name': 'Mount Kenya Wilderness Trek',
                'description': 'Combine safari with adventure on this unique trek through Mount Kenya National Park. Hike through pristine mountain forests, spot rare mountain wildlife, and enjoy spectacular alpine scenery. This challenging expedition is ideal for active travelers seeking something different.',
                'duration_days': 8,
                'price': 3200.00,
                'difficulty': 'challenging',
                'max_group_size': 6,
                'featured': False
            },
            {
                'name': 'Gorilla Trekking Uganda Experience',
                'description': 'An unforgettable journey to meet mountain gorillas in their natural habitat in Bwindi Impenetrable Forest. This once-in-a-lifetime experience includes guided treks through dense jungle, luxury lodge accommodation, and the chance to observe these magnificent primates up close.',
                'duration_days': 6,
                'price': 4500.00,
                'difficulty': 'challenging',
                'max_group_size': 8,
                'featured': False
            },
            {
                'name': 'Family Safari Adventure',
                'description': 'Specially designed for families with children. Enjoy game drives in comfortable vehicles, stay in family-friendly lodges with swimming pools, and participate in educational wildlife programs. Visit animal orphanages and learn about conservation efforts. Perfect introduction to safari for young adventurers.',
                'duration_days': 5,
                'price': 1950.00,
                'difficulty': 'easy',
                'max_group_size': 15,
                'featured': False
            },
            {
                'name': 'Luxury Honeymoon Safari',
                'description': 'Celebrate your love in Africa\'s most romantic settings. Stay in exclusive luxury lodges, enjoy private game drives, sundowners in the bush, and special romantic dinners under the stars. Includes champagne breakfasts, couples spa treatments, and personalized service throughout.',
                'duration_days': 7,
                'price': 5500.00,
                'difficulty': 'easy',
                'max_group_size': 4,
                'featured': False
            },
            {
                'name': 'Photography Safari Masterclass',
                'description': 'Designed for photography enthusiasts, this safari offers extended time at prime wildlife locations during golden hour. Includes professional photography guidance, specially modified vehicles with 360-degree views, and visits to the most photogenic locations in the Maasai Mara.',
                'duration_days': 6,
                'price': 3800.00,
                'difficulty': 'moderate',
                'max_group_size': 6,
                'featured': False
            },
            {
                'name': 'Coastal Safari & Beach Retreat',
                'description': 'The perfect combination of safari and beach relaxation. Start with 4 days of game drives in Tsavo, then unwind on the pristine white sands of the Kenyan coast. Includes snorkeling, dhow sailing, and visits to historic Swahili towns like Lamu or Mombasa.',
                'duration_days': 10,
                'price': 4200.00,
                'difficulty': 'easy',
                'max_group_size': 12,
                'featured': False
            },
        ]

        created_tours = []
        for tour_data in tours_data:
            tour = Tour.objects.create(**tour_data)
            created_tours.append(tour)
            self.stdout.write(f'  ✓ Created tour: {tour.name}')

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(created_tours)} tours!'))

        # Create Sample Bookings
        self.stdout.write('\nCreating sample bookings...')

        sample_names = [
            'John Smith', 'Emma Johnson', 'Michael Brown', 'Sarah Davis',
            'David Wilson', 'Lisa Anderson', 'Robert Taylor', 'Jennifer Martinez',
            'William Garcia', 'Emily Rodriguez', 'James Lee', 'Maria Gonzalez'
        ]

        sample_emails = [
            'john.smith@email.com', 'emma.j@email.com', 'michael.b@email.com',
            'sarah.d@email.com', 'david.w@email.com', 'lisa.a@email.com',
            'robert.t@email.com', 'jennifer.m@email.com', 'william.g@email.com',
            'emily.r@email.com', 'james.l@email.com', 'maria.g@email.com'
        ]

        for i in range(15):
            tour = random.choice(created_tours)
            booking = Booking.objects.create(
                tour=tour,
                full_name=random.choice(sample_names),
                email=random.choice(sample_emails),
                phone=f'+1{random.randint(2000000000, 9999999999)}',
                number_of_people=random.randint(1, 6),
                preferred_date=datetime.now().date() + timedelta(days=random.randint(30, 180)),
                special_requests='Looking forward to an amazing experience!'
            )
            self.stdout.write(f'  ✓ Created booking: {booking.full_name} for {booking.tour.name}')

        self.stdout.write(self.style.SUCCESS('Successfully created 15 sample bookings!'))

        # Create Sample Contact Messages
        self.stdout.write('\nCreating sample contact messages...')

        contact_messages = [
            {
                'name': 'Alex Thompson',
                'email': 'alex.t@email.com',
                'subject': 'Question about group discounts',
                'message': 'Hi, I\'m planning a safari for a group of 20 people. Do you offer group discounts? What would be the best tour for a mixed group with different fitness levels?'
            },
            {
                'name': 'Sophie Williams',
                'email': 'sophie.w@email.com',
                'subject': 'Honeymoon safari inquiry',
                'message': 'My fiancé and I are getting married in June and would love to book a honeymoon safari. Can you help us plan something special and romantic?'
            },
            {
                'name': 'Marcus Johnson',
                'email': 'marcus.j@email.com',
                'subject': 'Photography equipment',
                'message': 'I\'m a professional photographer interested in your Photography Safari. What camera equipment do you recommend bringing? Are there any restrictions?'
            },
            {
                'name': 'Rachel Green',
                'email': 'rachel.g@email.com',
                'subject': 'Family safari with young children',
                'message': 'We have two children aged 6 and 8. Are your family safaris suitable for kids this age? What safety measures do you have in place?'
            },
            {
                'name': 'Daniel Martinez',
                'email': 'daniel.m@email.com',
                'subject': 'Custom itinerary request',
                'message': 'I\'m interested in combining the Maasai Mara with a visit to Zanzibar. Can you create a custom 12-day itinerary for us?'
            },
        ]

        for msg_data in contact_messages:
            message = ContactMessage.objects.create(**msg_data)
            self.stdout.write(f'  ✓ Created message from: {message.name}')

        self.stdout.write(self.style.SUCCESS('Successfully created 5 contact messages!'))

        # Summary
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write(self.style.SUCCESS('DATABASE POPULATION COMPLETE!'))
        self.stdout.write('=' * 60)
        self.stdout.write(f'Total Tours: {Tour.objects.count()}')
        self.stdout.write(f'Total Bookings: {Booking.objects.count()}')
        self.stdout.write(f'Total Contact Messages: {ContactMessage.objects.count()}')
        self.stdout.write(f'Featured Tours: {Tour.objects.filter(featured=True).count()}')
        self.stdout.write('=' * 60)
        self.stdout.write('\nYou can now:')
        self.stdout.write('  1. Visit http://127.0.0.1:8000/ to see your website')
        self.stdout.write('  2. Login to admin at http://127.0.0.1:8000/admin/')
        self.stdout.write('  3. Manage tours, bookings, and messages')
        self.stdout.write('\nEnjoy your M&M Africa Safaris website! 🦁🌍')